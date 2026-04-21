#!/usr/bin/env python3
import argparse
import csv
import json
from pathlib import Path
from typing import Dict, List

from inspect_logos_local_state import DEFAULT_LOGOS_ROOT, choose_accounts, discover_accounts, read_only_connect
from extract_logos_panel_contexts import (
    extract_resource_ids,
    fully_unquote,
    normalize_context,
    parse_kv_blob,
    parse_pipe_settings,
    sanitize,
    truncate,
)


DEFAULT_OUTPUT_DIR = (
    Path(__file__).resolve().parents[1] / "data" / "research" / "local" / "logos_panel_contexts"
)


def write_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def history_rows(history_db: Path, account_name: str, limit: int) -> List[Dict[str, str]]:
    query = """
    SELECT Id, Title, Subtitle, LastVisited, Bookmark
    FROM History
    WHERE IsDeleted = 0
    ORDER BY LastVisited DESC
    LIMIT ?
    """
    rows: List[Dict[str, str]] = []
    with read_only_connect(history_db) as conn:
        for history_id, title, subtitle, last_visited, bookmark in conn.execute(query, (limit,)):
            panel_kind, settings = parse_pipe_settings(bookmark or "")
            position_settings = parse_kv_blob(settings.get("Position", ""))
            inline_search_settings = parse_kv_blob(settings.get("InlineSearchSettings", ""))
            rows.append(
                {
                    "account": account_name,
                    "row_id": sanitize(history_id or ""),
                    "when": last_visited or "",
                    "panel_kind": panel_kind,
                    "title": sanitize(title or ""),
                    "subtitle": sanitize(subtitle or ""),
                    "resource_id": settings.get("Id", ""),
                    "resource_provider_ids": extract_resource_ids(settings.get("ResourceProvider", "")),
                    "reference": settings.get("Reference", ""),
                    "report_id": settings.get("ReportId", ""),
                    "template_name": settings.get("TemplateName", ""),
                    "query_text": settings.get("QueryText", "") or inline_search_settings.get("QueryText", ""),
                    "search_kind": settings.get("SearchKindName", "") or inline_search_settings.get("SearchKindName", ""),
                    "milestone": settings.get("Milestone", ""),
                    "position": settings.get("Position", ""),
                    "context": normalize_context(settings.get("Context", "") or position_settings.get("Context", "")),
                    "raw_excerpt": truncate(fully_unquote(bookmark or ""), 500),
                }
            )
    return rows


def matches(row: Dict[str, str], needle: str) -> bool:
    hay = " ".join(row.values()).casefold()
    return needle.casefold() in hay


def grouped_latest(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    seen: set[str] = set()
    out: List[Dict[str, str]] = []
    for row in rows:
        key = row["resource_id"] or row["title"] or row["panel_kind"]
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Capture latest linked Logos resource rows for a verse/topic needle.")
    parser.add_argument("needle", help="Substring to match, e.g. 11.2.35 or σωτηρία")
    parser.add_argument("--logos-root", type=Path, default=DEFAULT_LOGOS_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--account")
    parser.add_argument("--limit", type=int, default=300)
    args = parser.parse_args()

    accounts = discover_accounts(args.logos_root)
    account = choose_accounts(accounts, args.account, all_accounts=False)[0]
    account_name = account["account"].name

    rows = history_rows(account["history_db"], account_name, args.limit)
    rows = [row for row in rows if matches(row, args.needle)]
    rows.sort(key=lambda row: row["when"], reverse=True)
    latest = grouped_latest(rows)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    safe_name = "".join(ch if ch.isalnum() else "_" for ch in args.needle)[:80].strip("_") or "snapshot"
    csv_path = args.output_dir / f"snapshot_{safe_name}.csv"
    json_path = args.output_dir / f"snapshot_{safe_name}.json"
    write_csv(csv_path, latest)
    json_path.write_text(json.dumps(latest, indent=2, ensure_ascii=False), encoding="utf-8")

    print(
        json.dumps(
            {
                "account": account_name,
                "needle": args.needle,
                "rows_matched": len(rows),
                "rows_grouped": len(latest),
                "csv": csv_path.as_posix(),
                "json": json_path.as_posix(),
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
