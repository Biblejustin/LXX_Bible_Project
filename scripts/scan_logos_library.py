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


def normalize_locations(rows: List[Dict[str, str]], resource_locations: Dict[str, str]) -> List[Dict[str, str]]:
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
            "resource_location": resource_locations.get(row.get("ResourceId", "") or "", ""),
            "categories": ";".join(categories),
        }
        normalized_row["relevance_score"] = str(score_resource(row, categories))
        normalized.append(normalized_row)
    return normalized


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


def build_summary(account: Dict[str, Path], rows: List[Dict[str, str]], priority_rows: List[Dict[str, str]]) -> Dict[str, object]:
    category_counts = Counter()
    type_counts = Counter()
    for row in rows:
        type_counts[row["type"]] += 1
        for category in filter(None, row["categories"].split(";")):
            category_counts[category] += 1
    return {
        "logos_root": str(account["account"].parents[1]),
        "account": account["account"].name,
        "catalog_db": str(account["catalog_db"]),
        "resource_db": str(account["resource_db"]),
        "documents_dir": str(account["documents_dir"]),
        "total_resources": len(rows),
        "priority_resources": len(priority_rows),
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--logos-root", default=str(DEFAULT_LOGOS_ROOT))
    parser.add_argument("--account")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    args = parser.parse_args()

    logos_root = Path(args.logos_root).expanduser()
    output_dir = Path(args.output_dir).expanduser()
    output_dir.mkdir(parents=True, exist_ok=True)

    account = choose_account(discover_accounts(logos_root), args.account)
    catalog_rows = fetch_catalog_rows(account["catalog_db"])
    resource_locations = fetch_resource_locations(account["resource_db"])
    normalized_rows = normalize_locations(catalog_rows, resource_locations)
    priority_rows = translation_priority_rows(normalized_rows)
    summary = build_summary(account, normalized_rows, priority_rows)

    all_csv = output_dir / "logos_resources_all.csv"
    priority_csv = output_dir / "logos_translation_resources.csv"
    summary_json = output_dir / "logos_scan_summary.json"

    write_csv(all_csv, sorted(normalized_rows, key=lambda row: (row["title"], row["resource_id"])))
    write_csv(priority_csv, priority_rows)
    summary_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print(
        json.dumps(
            {
                "account": account["account"].name,
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
