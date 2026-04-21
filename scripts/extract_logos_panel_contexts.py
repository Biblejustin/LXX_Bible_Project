#!/usr/bin/env python3
import argparse
import csv
import json
import re
import sqlite3
import urllib.parse
from pathlib import Path
from typing import Dict, List, Tuple

from inspect_logos_local_state import (
    DEFAULT_LOGOS_ROOT,
    PANEL_RE,
    choose_accounts,
    discover_accounts,
    read_only_connect,
)


DEFAULT_OUTPUT_DIR = (
    Path(__file__).resolve().parents[1] / "data" / "research" / "local" / "logos_panel_contexts"
)


def sanitize(text: str) -> str:
    return text.replace("\x00", "")


def write_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def fully_unquote(text: str, passes: int = 3) -> str:
    current = sanitize(text)
    for _ in range(passes):
        updated = urllib.parse.unquote(current)
        if updated == current:
            break
        current = sanitize(updated)
    return sanitize(current)


def parse_pipe_settings(raw: str) -> Tuple[str, Dict[str, str]]:
    if not raw:
        return "", {}
    parts = raw.split("|")
    kind = fully_unquote(parts[0]) if parts else ""
    values: Dict[str, str] = {}
    for part in parts[1:]:
        if "=" not in part:
            continue
        key, value = part.split("=", 1)
        values[fully_unquote(key)] = fully_unquote(value)
    return kind, values


def parse_kv_blob(raw: str) -> Dict[str, str]:
    values: Dict[str, str] = {}
    if not raw:
        return values
    for part in fully_unquote(raw).split("|"):
        if "=" not in part:
            continue
        key, value = part.split("=", 1)
        values[sanitize(key)] = sanitize(value)
    return values


def extract_resource_ids(raw: str) -> str:
    if not raw:
        return ""
    matches = re.findall(r"ResourceId=([^|]+)", fully_unquote(raw))
    return ";".join(dict.fromkeys(matches))


def truncate(text: str, limit: int = 240) -> str:
    text = sanitize(text)
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def normalize_context(text: str) -> str:
    return sanitize(text).replace("\r", " ").replace("\n", " ").strip()


def fetch_history_rows(history_db: Path, account_name: str, limit: int) -> List[Dict[str, str]]:
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
            context = normalize_context(settings.get("Context", "") or position_settings.get("Context", ""))
            row = {
                "source": "history",
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
                "headword": settings.get("Headword", ""),
                "milestone": settings.get("Milestone", ""),
                "position": settings.get("Position", ""),
                "context": context,
                "raw_excerpt": truncate(bookmark or "", 500),
            }
            if any(
                [
                    row["resource_id"],
                    row["reference"],
                    row["report_id"],
                    row["query_text"],
                    row["context"],
                ]
            ):
                rows.append(row)
    return rows


def fetch_layout_rows(layouts_db: Path, account_name: str, limit: int) -> List[Dict[str, str]]:
    query = """
    SELECT LayoutId, Title, CreatedDate, Xml
    FROM Layouts
    WHERE IsDeleted = 0
    ORDER BY CreatedDate DESC
    LIMIT ?
    """
    rows: List[Dict[str, str]] = []
    with read_only_connect(layouts_db) as conn:
        for layout_id, layout_title, created_date, xml in conn.execute(query, (limit,)):
            for panel_kind, raw_settings in PANEL_RE.findall(xml or ""):
                _, settings = parse_pipe_settings(raw_settings)
                position_settings = parse_kv_blob(settings.get("Position", ""))
                inline_search_settings = parse_kv_blob(settings.get("InlineSearchSettings", ""))
                context = normalize_context(settings.get("Context", "") or position_settings.get("Context", ""))
                row = {
                    "source": "layout",
                    "account": account_name,
                    "row_id": str(layout_id),
                    "when": created_date or "",
                    "panel_kind": panel_kind,
                    "title": sanitize(layout_title or ""),
                    "subtitle": "",
                    "resource_id": settings.get("Id", ""),
                    "resource_provider_ids": extract_resource_ids(
                        settings.get("BookResourceProvider", "") or settings.get("BibleResourceProvider", "")
                    ),
                    "reference": settings.get("Reference", ""),
                    "report_id": settings.get("ReportId", ""),
                    "template_name": settings.get("TemplateName", ""),
                    "query_text": settings.get("QueryText", "") or inline_search_settings.get("QueryText", ""),
                    "search_kind": settings.get("SearchKindName", "") or inline_search_settings.get("SearchKindName", ""),
                    "headword": settings.get("Headword", ""),
                    "milestone": settings.get("Milestone", ""),
                    "position": settings.get("Position", ""),
                    "context": context,
                    "raw_excerpt": truncate(fully_unquote(raw_settings), 500),
                }
                if any(
                    [
                        row["resource_id"],
                        row["reference"],
                        row["report_id"],
                        row["query_text"],
                        row["context"],
                    ]
                ):
                    rows.append(row)
    return rows


def build_summary(rows: List[Dict[str, str]]) -> Dict[str, object]:
    by_source: Dict[str, int] = {}
    for row in rows:
        by_source[row["source"]] = by_source.get(row["source"], 0) + 1
    sample = rows[:20]
    return {
        "rows": len(rows),
        "by_source": by_source,
        "sample": sample,
        "notes": [
            "History rows come from HistoryManager/history.db Bookmark values.",
            "Layout rows come from LayoutManager/layouts.db panel Settings XML.",
            "Context values are URL-decoded snippets, not full resource text.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract decodable local Logos panel state and context snippets from history/layout databases."
    )
    parser.add_argument("--logos-root", type=Path, default=DEFAULT_LOGOS_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--account")
    parser.add_argument("--all-accounts", action="store_true")
    parser.add_argument("--history-limit", type=int, default=200)
    parser.add_argument("--layout-limit", type=int, default=40)
    parser.add_argument("--filter")
    args = parser.parse_args()

    accounts = discover_accounts(args.logos_root)
    selected_accounts = choose_accounts(accounts, args.account, args.all_accounts)

    rows: List[Dict[str, str]] = []
    for account in selected_accounts:
        account_name = account["account"].name
        rows.extend(fetch_history_rows(account["history_db"], account_name, args.history_limit))
        rows.extend(fetch_layout_rows(account["layouts_db"], account_name, args.layout_limit))

    if args.filter:
        needle = args.filter.casefold()
        rows = [
            row
            for row in rows
            if needle in json.dumps(row, ensure_ascii=False).casefold()
        ]

    rows.sort(key=lambda row: row["when"], reverse=True)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    contexts_csv = args.output_dir / "panel_contexts.csv"
    summary_json = args.output_dir / "summary.json"
    write_csv(contexts_csv, rows)
    summary_json.write_text(json.dumps(build_summary(rows), indent=2, ensure_ascii=False), encoding="utf-8")

    print(
        json.dumps(
            {
                "panel_contexts_csv": contexts_csv.as_posix(),
                "summary_json": summary_json.as_posix(),
                "accounts_scanned": [row["account"].name for row in selected_accounts],
                "rows": len(rows),
                "filter": args.filter or "",
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
