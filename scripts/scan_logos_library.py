#!/usr/bin/env python3
import argparse
import csv
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Dict, Iterable, List, Optional


DEFAULT_LOGOS_ROOT = Path.home() / "Library" / "Application Support" / "Logos4"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "research" / "local" / "logos_scan"


def read_only_connect(path: Path) -> sqlite3.Connection:
    uri = f"file:{path.as_posix()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def discover_accounts(logos_root: Path) -> List[Dict[str, Path]]:
    accounts: List[Dict[str, Path]] = []
    data_root = logos_root / "Data"
    docs_root = logos_root / "Documents"
    if not data_root.exists():
        return accounts
    for data_dir in sorted(p for p in data_root.iterdir() if p.is_dir()):
        catalog_db = data_dir / "LibraryCatalog" / "catalog.db"
        resource_db = data_dir / "ResourceManager" / "ResourceManager.db"
        docs_dir = docs_root / data_dir.name
        if catalog_db.exists() and resource_db.exists():
            accounts.append(
                {
                    "account": data_dir,
                    "catalog_db": catalog_db,
                    "resource_db": resource_db,
                    "documents_dir": docs_dir,
                }
            )
    accounts.sort(key=lambda row: row["catalog_db"].stat().st_mtime, reverse=True)
    return accounts


def choose_account(accounts: List[Dict[str, Path]], wanted: Optional[str]) -> Dict[str, Path]:
    if not accounts:
        raise FileNotFoundError("No Logos account folders with catalog/resource DBs found.")
    if wanted:
        for row in accounts:
            if row["account"].name == wanted:
                return row
        raise FileNotFoundError(f"Requested account not found: {wanted}")
    return accounts[0]


def fetch_catalog_rows(catalog_db: Path) -> List[Dict[str, str]]:
    query = """
    SELECT
        ResourceId,
        Type,
        Title,
        AbbreviatedTitle,
        Authors,
        PublicationDate,
        Languages,
        Subjects,
        Description
    FROM Records
    WHERE Availability = 0 OR Availability = 1 OR Availability = 2 OR Availability IS NULL
    """
    with read_only_connect(catalog_db) as conn:
        conn.row_factory = sqlite3.Row
        return [dict(row) for row in conn.execute(query)]


def fetch_resource_locations(resource_db: Path) -> Dict[str, str]:
    query = """
    SELECT ResourceId, Location
    FROM Resources
    """
    with read_only_connect(resource_db) as conn:
        return {resource_id: location for resource_id, location in conn.execute(query)}


def lower_blob(parts: Iterable[Optional[str]]) -> str:
    return " ".join(part or "" for part in parts).lower()


def classify_resource(row: Dict[str, str]) -> List[str]:
    haystack = lower_blob(
        [
            row.get("Type"),
            row.get("Title"),
            row.get("AbbreviatedTitle"),
            row.get("Subjects"),
            row.get("Languages"),
        ]
    )
    categories: List[str] = []

    if "septuagint" in haystack or re.search(r"\blxx\b", haystack):
        categories.append("septuagint")
    if "reverse-interlinear" in haystack or "interlinear" in haystack:
        categories.append("interlinear")
    if "lexicon" in haystack or "dictionaries" in haystack:
        categories.append("lexicon")
    if "critical-apparatus" in haystack or "apparatus" in haystack:
        categories.append("apparatus")
    if "ancient-manuscript" in haystack or "manuscript" in haystack or "codex" in haystack or "papyri" in haystack:
        categories.append("manuscript")
    if "grammar" in haystack or "syntax" in haystack or "discourse" in haystack:
        categories.append("grammar")
    if "encyclopedia" in haystack or "dictionary" in haystack:
        categories.append("reference")
    if "supplementaldata" in haystack or "syntaxdatabase" in haystack or "clauses" in haystack or "wordsenses" in haystack:
        categories.append("dataset")
    if "bible" in haystack and ("--greek" in haystack or "\tel" in haystack or " el " in f" {haystack} " or "greek new testament" in haystack):
        categories.append("greek_text")

    deduped: List[str] = []
    for category in categories:
        if category not in deduped:
            deduped.append(category)
    return deduped


def score_resource(row: Dict[str, str], categories: List[str]) -> int:
    haystack = lower_blob(
        [
            row.get("Type"),
            row.get("Title"),
            row.get("Subjects"),
            row.get("Languages"),
        ]
    )
    score = 0
    if "septuagint" in haystack or re.search(r"\blxx\b", haystack):
        score += 60
    if "bible. o.t.--greek" in haystack or "bible. n.t.--greek" in haystack:
        score += 35
    if "greek" in haystack or "\tel" in haystack:
        score += 15
    if "lexicon" in categories:
        score += 25
    if "apparatus" in categories:
        score += 25
    if "interlinear" in categories:
        score += 20
    if "grammar" in categories:
        score += 18
    if "dataset" in categories:
        score += 15
    if "manuscript" in categories:
        score += 12
    if "reference" in categories:
        score += 8
    if "greek_text" in categories:
        score += 20
    return score


def normalize_locations(rows: List[Dict[str, str]], resource_locations: Dict[str, str], account_name: str) -> List[Dict[str, str]]:
    normalized: List[Dict[str, str]] = []
    for row in rows:
        categories = classify_resource(row)
        normalized_row = {
            "resource_id": row.get("ResourceId", "") or "",
            "type": row.get("Type", "") or "",
            "title": row.get("Title", "") or "",
            "abbreviated_title": row.get("AbbreviatedTitle", "") or "",
            "authors": row.get("Authors", "") or "",
            "publication_date": row.get("PublicationDate", "") or "",
            "languages": row.get("Languages", "") or "",
            "subjects": row.get("Subjects", "") or "",
            "description": row.get("Description", "") or "",
            "account": account_name,
            "account_ids": account_name,
            "account_count": "1",
            "resource_location": resource_locations.get(row.get("ResourceId", "") or "", ""),
            "resource_locations": resource_locations.get(row.get("ResourceId", "") or "", ""),
            "categories": ";".join(categories),
        }
        normalized_row["relevance_score"] = str(score_resource(row, categories))
        normalized.append(normalized_row)
    return normalized


def merge_account_rows(accounts: List[Dict[str, Path]]) -> List[Dict[str, str]]:
    merged: Dict[str, Dict[str, str]] = {}
    account_sets: Dict[str, set[str]] = {}
    location_sets: Dict[str, set[str]] = {}

    for account in accounts:
        account_name = account["account"].name
        catalog_rows = fetch_catalog_rows(account["catalog_db"])
        resource_locations = fetch_resource_locations(account["resource_db"])
        normalized_rows = normalize_locations(catalog_rows, resource_locations, account_name)
        for row in normalized_rows:
            resource_id = row["resource_id"]
            account_sets.setdefault(resource_id, set()).add(account_name)
            if row["resource_location"]:
                location_sets.setdefault(resource_id, set()).add(row["resource_location"])
            if resource_id not in merged:
                merged[resource_id] = dict(row)

    out: List[Dict[str, str]] = []
    for resource_id, row in merged.items():
        accounts_sorted = sorted(account_sets.get(resource_id, set()))
        locations_sorted = sorted(location_sets.get(resource_id, set()))
        row["account_ids"] = ";".join(accounts_sorted)
        row["account_count"] = str(len(accounts_sorted))
        if accounts_sorted:
            row["account"] = accounts_sorted[0] if len(accounts_sorted) == 1 else "multiple"
        if locations_sorted:
            row["resource_location"] = locations_sorted[0]
            row["resource_locations"] = ";".join(locations_sorted)
        out.append(row)
    return out


def translation_priority_rows(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    filtered = []
    for row in rows:
        score = int(row["relevance_score"])
        categories = set(filter(None, row["categories"].split(";")))
        if score >= 20 or categories.intersection({"septuagint", "lexicon", "apparatus", "greek_text", "interlinear", "grammar"}):
            filtered.append(row)
    return sorted(filtered, key=lambda row: (-int(row["relevance_score"]), row["title"], row["resource_id"]))


def write_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_summary(
    rows: List[Dict[str, str]],
    priority_rows: List[Dict[str, str]],
    accounts: List[Dict[str, Path]],
    selected_account: Optional[Dict[str, Path]] = None,
    merged_accounts: bool = False,
) -> Dict[str, object]:
    category_counts = Counter()
    type_counts = Counter()
    for row in rows:
        type_counts[row["type"]] += 1
        for category in filter(None, row["categories"].split(";")):
            category_counts[category] += 1
    summary = {
        "logos_root": str(accounts[0]["account"].parents[1]) if accounts else "",
        "total_resources": len(rows),
        "priority_resources": len(priority_rows),
        "merged_accounts": merged_accounts,
        "accounts_scanned": [row["account"].name for row in accounts],
        "category_counts": dict(sorted(category_counts.items())),
        "top_types": dict(type_counts.most_common(20)),
        "top_priority_resources": [
            {
                "resource_id": row["resource_id"],
                "title": row["title"],
                "type": row["type"],
                "categories": row["categories"],
                "relevance_score": int(row["relevance_score"]),
            }
            for row in priority_rows[:40]
        ],
    }
    if selected_account is not None and not merged_accounts:
        summary.update(
            {
                "account": selected_account["account"].name,
                "catalog_db": str(selected_account["catalog_db"]),
                "resource_db": str(selected_account["resource_db"]),
                "documents_dir": str(selected_account["documents_dir"]),
            }
        )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--logos-root", default=str(DEFAULT_LOGOS_ROOT))
    parser.add_argument("--account")
    parser.add_argument("--all-accounts", action="store_true")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    args = parser.parse_args()

    logos_root = Path(args.logos_root).expanduser()
    output_dir = Path(args.output_dir).expanduser()
    output_dir.mkdir(parents=True, exist_ok=True)

    accounts = discover_accounts(logos_root)
    if args.all_accounts:
        selected_accounts = accounts
        normalized_rows = merge_account_rows(selected_accounts)
        selected_account = None
    else:
        selected_account = choose_account(accounts, args.account)
        selected_accounts = [selected_account]
        catalog_rows = fetch_catalog_rows(selected_account["catalog_db"])
        resource_locations = fetch_resource_locations(selected_account["resource_db"])
        normalized_rows = normalize_locations(catalog_rows, resource_locations, selected_account["account"].name)
    priority_rows = translation_priority_rows(normalized_rows)
    summary = build_summary(
        normalized_rows,
        priority_rows,
        accounts=selected_accounts,
        selected_account=selected_account,
        merged_accounts=args.all_accounts,
    )

    all_csv = output_dir / "logos_resources_all.csv"
    priority_csv = output_dir / "logos_translation_resources.csv"
    summary_json = output_dir / "logos_scan_summary.json"

    write_csv(all_csv, sorted(normalized_rows, key=lambda row: (row["title"], row["resource_id"])))
    write_csv(priority_csv, priority_rows)
    summary_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print(
        json.dumps(
            {
                "account": selected_account["account"].name if selected_account is not None else None,
                "accounts_scanned": [row["account"].name for row in selected_accounts],
                "merged_accounts": args.all_accounts,
                "all_resources_csv": str(all_csv),
                "translation_resources_csv": str(priority_csv),
                "summary_json": str(summary_json),
                "priority_resources": len(priority_rows),
                "total_resources": len(normalized_rows),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
