#!/usr/bin/env python3
"""Build a progress dashboard for the separate LXX deuterocanon workspace."""

from __future__ import annotations

import argparse
import csv
import json
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "data" / "raw" / "lxx_deuterocanon" / "deuterocanon_full.csv"
DEFAULT_MANIFEST = ROOT / "data" / "raw" / "lxx_deuterocanon" / "source_manifest.json"
DEFAULT_OUTPUT = ROOT / "output" / "deuterocanon" / "lxx_deuterocanon_progress.md"
DEFAULT_CSV_OUTPUT = ROOT / "output" / "deuterocanon" / "lxx_deuterocanon_progress.csv"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_manifest(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_book_rows(
    source_rows: list[dict[str, str]],
    manifest: dict[str, object],
) -> list[dict[str, str]]:
    books: OrderedDict[str, dict[str, object]] = OrderedDict()
    for row in source_rows:
        code = row.get("book_code", "").strip()
        current = books.setdefault(
            code,
            {
                "book_code": code,
                "book_name": row.get("book_name", "").strip(),
                "first_ref": row.get("ref", "").strip(),
                "last_ref": row.get("ref", "").strip(),
                "verse_rows": 0,
                "drafted_rows": 0,
                "source_note_rows": 0,
                "chapter_values": [],
            },
        )
        current["last_ref"] = row.get("ref", "").strip()
        current["verse_rows"] = int(current["verse_rows"]) + 1
        if row.get("draft_translation", "").strip():
            current["drafted_rows"] = int(current["drafted_rows"]) + 1
        if row.get("syntax_notes", "").strip():
            current["source_note_rows"] = int(current["source_note_rows"]) + 1
        current["chapter_values"].append(row.get("chapter", "").strip())

    manifest_books = {}
    diagnostics = manifest.get("diagnostics", {})
    if isinstance(diagnostics, dict) and isinstance(diagnostics.get("books"), dict):
        manifest_books = diagnostics["books"]

    output_rows: list[dict[str, str]] = []
    for code, row in books.items():
        source_stat = manifest_books.get(code, {}) if isinstance(manifest_books, dict) else {}
        chapter_values = [value for value in row["chapter_values"] if value]
        chapter_count = len(set(chapter_values))
        verse_rows = int(row["verse_rows"])
        drafted_rows = int(row["drafted_rows"])
        status = "not_started" if drafted_rows == 0 else "in_progress"
        if drafted_rows == verse_rows and verse_rows:
            status = "drafted"
        output_rows.append(
            {
                "book_code": str(row["book_code"]),
                "book_name": str(row["book_name"]),
                "status": status,
                "verse_rows": str(verse_rows),
                "drafted_rows": str(drafted_rows),
                "remaining_rows": str(verse_rows - drafted_rows),
                "chapter_count": str(chapter_count),
                "first_ref": str(row["first_ref"]),
                "last_ref": str(row["last_ref"]),
                "source_file": str(source_stat.get("source_file", "")) if isinstance(source_stat, dict) else "",
                "source_usfm_id": str(source_stat.get("source_usfm_id", "")) if isinstance(source_stat, dict) else "",
                "expected_title": str(source_stat.get("expected_title", "")) if isinstance(source_stat, dict) else "",
                "source_validation": str(source_stat.get("status", "")) if isinstance(source_stat, dict) else "",
                "source_note_rows": str(row["source_note_rows"]),
                "note": str(source_stat.get("note", "")) if isinstance(source_stat, dict) else "",
            }
        )
    return output_rows


def write_progress_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "book_code",
        "book_name",
        "status",
        "verse_rows",
        "drafted_rows",
        "remaining_rows",
        "chapter_count",
        "first_ref",
        "last_ref",
        "source_file",
        "source_usfm_id",
        "expected_title",
        "source_validation",
        "source_note_rows",
        "note",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_progress_markdown(path: Path, rows: list[dict[str, str]], manifest: dict[str, object]) -> None:
    total_rows = sum(int(row["verse_rows"]) for row in rows)
    drafted_rows = sum(int(row["drafted_rows"]) for row in rows)
    missing_targets = []
    diagnostics = manifest.get("diagnostics", {})
    if isinstance(diagnostics, dict) and isinstance(diagnostics.get("missing_targets"), list):
        missing_targets = diagnostics["missing_targets"]
    source_validation = diagnostics.get("source_validation", {}) if isinstance(diagnostics, dict) else {}

    lines = [
        "# LXX Deuterocanon Progress",
        "",
        "Separate workstream. These rows do not feed the 66-book Greek Heritage Study Bible outputs.",
        "",
        "## Summary",
        "",
        f"- Imported groups: {len(rows)}",
        f"- Verse rows: {total_rows}",
        f"- Drafted rows: {drafted_rows}",
        f"- Remaining rows: {total_rows - drafted_rows}",
        f"- Source ID mismatches: {len(source_validation.get('source_id_mismatches', [])) if isinstance(source_validation, dict) else 0}",
        f"- Source title mismatches: {len(source_validation.get('source_title_mismatches', [])) if isinstance(source_validation, dict) else 0}",
        "",
        "## Books",
        "",
        "| Code | Book | Status | Rows | Drafted | Remaining | Chapters | First | Last | Source validation |",
        "| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            "| {book_code} | {book_name} | {status} | {verse_rows} | {drafted_rows} | "
            "{remaining_rows} | {chapter_count} | {first_ref} | {last_ref} | {source_validation} |".format(**row)
        )

    lines.extend(
        [
            "",
            "## Missing Targets",
            "",
            "| Code | Book | Reason |",
            "| --- | --- | --- |",
        ]
    )
    for item in missing_targets:
        if not isinstance(item, dict):
            continue
        lines.append(f"| {item.get('book_code', '')} | {item.get('book_name', '')} | {item.get('reason', '')} |")

    lines.extend(
        [
            "",
            "## Translation Loop",
            "",
            "Use ignored one-book working output while translating:",
            "",
            "```bash",
            "make build-deuterocanon-book BOOK=Tobit",
            "```",
            "",
            "Use full output before handoff or commit:",
            "",
            "```bash",
            "make build-deuterocanon",
            "```",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--csv-output", type=Path, default=DEFAULT_CSV_OUTPUT)
    args = parser.parse_args()

    source = args.source if args.source.is_absolute() else ROOT / args.source
    manifest_path = args.manifest if args.manifest.is_absolute() else ROOT / args.manifest
    output = args.output if args.output.is_absolute() else ROOT / args.output
    csv_output = args.csv_output if args.csv_output.is_absolute() else ROOT / args.csv_output

    source_rows = load_csv(source)
    manifest = load_manifest(manifest_path)
    rows = build_book_rows(source_rows, manifest)
    write_progress_csv(csv_output, rows)
    write_progress_markdown(output, rows, manifest)
    print(json.dumps({"progress": str(output), "csv": str(csv_output), "books": len(rows)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
