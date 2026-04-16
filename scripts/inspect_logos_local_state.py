#!/usr/bin/env python3
import argparse
import csv
import json
import re
import sqlite3
import urllib.parse
from pathlib import Path
from typing import Dict, Iterable, List, Optional


DEFAULT_LOGOS_ROOT = Path.home() / "Library" / "Application Support" / "Logos4"
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "research" / "local" / "logos_state"
PANEL_RE = re.compile(r"<Panel Kind='([^']+)'[^>]*Settings='([^']*)'")


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
        docs_dir = docs_root / data_dir.name
        history_db = data_dir / "HistoryManager" / "history.db"
        layouts_db = docs_dir / "LayoutManager" / "layouts.db"
        if history_db.exists() and layouts_db.exists():
            accounts.append(
                {
                    "account": data_dir,
                    "history_db": history_db,
                    "layouts_db": layouts_db,
                    "wordfind_db": docs_dir / "Documents" / "WordFind" / "WordFind.db",
                    "morphgrid_db": docs_dir / "Documents" / "MorphGrid" / "MorphGrid.db",
                    "guides_db": docs_dir / "Guides" / "guides.db",
                    "library_index_db": data_dir / "LibraryIndex" / "LibraryIndex.db",
                    "library_index_lxn": data_dir / "LibraryIndex" / "index.lxn",
                    "library_index_idx": data_dir / "LibraryIndex" / "index.idx",
                    "concordance_dir": data_dir / "Concordance",
                    "lemmas_discovered_db": data_dir / "ResourceManager" / "Lemmas" / "Discovered.db",
                    "word_senses_discovered_db": data_dir / "ResourceManager" / "WordSenses" / "Discovered.db",
                    "bible_xrefs_discovered_db": data_dir / "ResourceManager" / "BibleCrossReferences" / "Discovered.db",
                    "crossrefs_discovered_db": data_dir / "ResourceManager" / "CrossReferences" / "Discovered.db",
                    "resource_manager_resources": data_dir / "ResourceManager" / "Resources",
                }
            )

    accounts.sort(key=lambda row: row["history_db"].stat().st_mtime, reverse=True)
    return accounts


def choose_accounts(accounts: List[Dict[str, Path]], wanted: Optional[str], all_accounts: bool) -> List[Dict[str, Path]]:
    if not accounts:
        raise FileNotFoundError("No Logos accounts found with history/layout databases.")
    if wanted:
        matches = [row for row in accounts if row["account"].name == wanted]
        if not matches:
            raise FileNotFoundError(f"Requested account not found: {wanted}")
        return matches
    if all_accounts:
        return accounts
    largest = max(
        accounts,
        key=lambda row: row["library_index_lxn"].stat().st_size if row["library_index_lxn"].exists() else 0,
    )
    return [largest]


def write_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def truncate(text: str, limit: int = 240) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def read_header_lines(path: Path, limit_bytes: int = 256) -> List[str]:
    data = path.read_bytes()[:limit_bytes]
    text = data.decode("utf-8", errors="ignore").replace("\x00", "")
    return [line.strip() for line in text.splitlines() if line.strip()]


def parse_settings(raw_settings: str) -> Dict[str, str]:
    settings: Dict[str, str] = {}
    for item in raw_settings.split("|"):
        if "=" not in item:
            continue
        key, value = item.split("=", 1)
        settings[urllib.parse.unquote(key)] = urllib.parse.unquote(value)
    return settings


def fetch_recent_history(history_db: Path, account_name: str, limit: int) -> List[Dict[str, str]]:
    query = """
    SELECT Title, Subtitle, LastVisited, Bookmark
    FROM History
    WHERE IsDeleted = 0
    ORDER BY LastVisited DESC
    LIMIT ?
    """
    rows: List[Dict[str, str]] = []
    with read_only_connect(history_db) as conn:
        for title, subtitle, last_visited, bookmark in conn.execute(query, (limit,)):
            rows.append(
                {
                    "account": account_name,
                    "title": title or "",
                    "subtitle": subtitle or "",
                    "last_visited": last_visited or "",
                    "bookmark": bookmark or "",
                }
            )
    return rows


def interesting_history_rows(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    interesting_prefixes = {"Search", "Bible Word Study", "Factbook "}
    filtered: List[Dict[str, str]] = []
    for row in rows:
        title = row["title"]
        if title in interesting_prefixes or title.startswith("Factbook"):
            filtered.append(row)
    return filtered


def fetch_layout_panels(layouts_db: Path, account_name: str, limit_layouts: int) -> List[Dict[str, str]]:
    query = """
    SELECT LayoutId, Title, CreatedDate, Xml
    FROM Layouts
    WHERE IsDeleted = 0
    ORDER BY CreatedDate DESC
    LIMIT ?
    """
    rows: List[Dict[str, str]] = []
    with read_only_connect(layouts_db) as conn:
        for layout_id, title, created_date, xml in conn.execute(query, (limit_layouts,)):
            for panel_kind, raw_settings in PANEL_RE.findall(xml or ""):
                settings = parse_settings(raw_settings)
                signal = (
                    settings.get("QueryText")
                    or settings.get("SearchQuery")
                    or settings.get("ReportId")
                    or settings.get("TemplateName")
                    or settings.get("Headword")
                )
                if not signal and panel_kind not in {"Search", "Factbook", "BibleWordStudy"}:
                    continue
                rows.append(
                    {
                        "account": account_name,
                        "layout_id": str(layout_id),
                        "layout_title": title or "",
                        "created_date": created_date or "",
                        "panel_kind": panel_kind,
                        "query_text": settings.get("QueryText", ""),
                        "search_query": settings.get("SearchQuery", ""),
                        "search_kind": settings.get("SearchKindName", ""),
                        "report_id": settings.get("ReportId", ""),
                        "template_name": settings.get("TemplateName", ""),
                        "headword": settings.get("Headword", ""),
                        "resource_provider": settings.get("BookResourceProvider", "") or settings.get("BibleResourceProvider", ""),
                        "raw_settings_excerpt": truncate(urllib.parse.unquote(raw_settings), 500),
                    }
                )
    return rows


def count_rows(db_path: Path, table_name: str) -> int:
    if not db_path.exists():
        return 0
    with read_only_connect(db_path) as conn:
        try:
            value = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()
        except sqlite3.DatabaseError:
            return 0
    return int(value[0]) if value else 0


def fetch_resource_files(discovered_db: Path) -> List[str]:
    if not discovered_db.exists():
        return []
    with read_only_connect(discovered_db) as conn:
        try:
            rows = conn.execute("SELECT * FROM ResourceFiles").fetchall()
        except sqlite3.DatabaseError:
            return []
    out: List[str] = []
    for row in rows:
        if row and row[0]:
            out.append(str(row[0]))
    return out


def file_signature_rows(account: Dict[str, Path]) -> List[Dict[str, str]]:
    account_name = account["account"].name
    rows: List[Dict[str, str]] = []

    candidate_paths: List[Path] = [
        account["library_index_db"],
        account["library_index_lxn"],
        account["library_index_idx"],
    ]

    concordance_dir = account["concordance_dir"]
    if concordance_dir.exists():
        concordance_files = sorted(concordance_dir.glob("*.concordance"))
        if concordance_files:
            candidate_paths.append(concordance_files[0])

    for discovered_db_key in [
        "lemmas_discovered_db",
        "word_senses_discovered_db",
        "bible_xrefs_discovered_db",
        "crossrefs_discovered_db",
    ]:
        for resource_file in fetch_resource_files(account[discovered_db_key]):
            candidate_paths.append(Path(resource_file))

    seen: set[Path] = set()
    for path in candidate_paths:
        if path in seen or not path.exists():
            continue
        seen.add(path)
        header_lines = read_header_lines(path)
        rows.append(
            {
                "account": account_name,
                "path": path.as_posix(),
                "suffix": "".join(path.suffixes),
                "size_bytes": str(path.stat().st_size),
                "header_1": header_lines[0] if len(header_lines) > 0 else "",
                "header_2": header_lines[1] if len(header_lines) > 1 else "",
                "header_3": header_lines[2] if len(header_lines) > 2 else "",
            }
        )
    return rows


def build_summary(
    accounts: Iterable[Dict[str, Path]],
    recent_history: List[Dict[str, str]],
    layout_panels: List[Dict[str, str]],
    signatures: List[Dict[str, str]],
) -> Dict[str, object]:
    recent_titles = recent_history[:20]
    recent_panels = layout_panels[:20]
    return {
        "accounts_scanned": [row["account"].name for row in accounts],
        "recent_history_hits": len(recent_history),
        "layout_panel_hits": len(layout_panels),
        "signature_rows": len(signatures),
        "recent_history_sample": recent_titles,
        "layout_panel_sample": recent_panels,
        "notes": [
            "HistoryManager/history.db stores recent panel titles and subtitles.",
            "LayoutManager/layouts.db stores panel XML and can expose QueryText/ReportId/Headword for persisted layouts.",
            "LibraryIndex/index.lxn is SQLite-backed metadata; main index payload lives in adjacent binary index files.",
            "Concordance and supplemental dataset payload files use LRES01 headers and may include encrypted/proprietary content.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect Logos local state that is accessible from disk without touching encrypted payloads.")
    parser.add_argument("--logos-root", type=Path, default=DEFAULT_LOGOS_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--account")
    parser.add_argument("--all-accounts", action="store_true")
    parser.add_argument("--history-limit", type=int, default=100)
    parser.add_argument("--layout-limit", type=int, default=40)
    args = parser.parse_args()

    accounts = discover_accounts(args.logos_root)
    selected_accounts = choose_accounts(accounts, args.account, args.all_accounts)

    history_rows: List[Dict[str, str]] = []
    layout_rows: List[Dict[str, str]] = []
    signature_rows: List[Dict[str, str]] = []
    account_rows: List[Dict[str, str]] = []

    for account in selected_accounts:
        account_name = account["account"].name
        recent_history = fetch_recent_history(account["history_db"], account_name, args.history_limit)
        interesting_history = interesting_history_rows(recent_history)
        layout_panels = fetch_layout_panels(account["layouts_db"], account_name, args.layout_limit)
        signatures = file_signature_rows(account)

        wordfind_count = count_rows(account["wordfind_db"], "WordFinds")
        morphgrid_count = count_rows(account["morphgrid_db"], "MorphGrids")
        guide_count = count_rows(account["guides_db"], "Guides")

        account_rows.append(
            {
                "account": account_name,
                "history_db": account["history_db"].as_posix(),
                "layouts_db": account["layouts_db"].as_posix(),
                "wordfind_count": str(wordfind_count),
                "morphgrid_count": str(morphgrid_count),
                "guide_count": str(guide_count),
            }
        )

        history_rows.extend(interesting_history)
        layout_rows.extend(layout_panels)
        signature_rows.extend(signatures)

    history_rows.sort(key=lambda row: row["last_visited"], reverse=True)
    layout_rows.sort(key=lambda row: row["created_date"], reverse=True)
    signature_rows.sort(key=lambda row: (row["account"], row["path"]))

    args.output_dir.mkdir(parents=True, exist_ok=True)
    accounts_csv = args.output_dir / "accounts.csv"
    history_csv = args.output_dir / "recent_history.csv"
    layouts_csv = args.output_dir / "layout_panels.csv"
    signatures_csv = args.output_dir / "file_signatures.csv"
    summary_json = args.output_dir / "summary.json"

    write_csv(accounts_csv, account_rows)
    write_csv(history_csv, history_rows)
    write_csv(layouts_csv, layout_rows)
    write_csv(signatures_csv, signature_rows)

    summary = build_summary(selected_accounts, history_rows, layout_rows, signature_rows)
    summary_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "accounts_csv": accounts_csv.as_posix(),
                "recent_history_csv": history_csv.as_posix(),
                "layout_panels_csv": layouts_csv.as_posix(),
                "file_signatures_csv": signatures_csv.as_posix(),
                "summary_json": summary_json.as_posix(),
                "accounts_scanned": [row["account"].name for row in selected_accounts],
                "recent_history_hits": len(history_rows),
                "layout_panel_hits": len(layout_rows),
                "signature_rows": len(signature_rows),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
