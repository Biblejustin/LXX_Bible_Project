#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from typing import Dict, List

from build_fresh_translation import ensure_source_columns
from fresh_bible.pipeline_common import load_csv


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
DEFAULT_OT_SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
DEFAULT_NT_SOURCE = ROOT / "data" / "raw" / "tr_greek" / "nt_full.csv"
DEFAULT_OUTPUT = OUTPUT / "fresh_translation_full_bible_translation_only.md"
DEFAULT_DIAGNOSTICS = OUTPUT / "fresh_translation_full_bible_translation_only_diagnostics.json"


def ordered_books(rows: List[Dict[str, str]]) -> List[str]:
    books: List[str] = []
    for row in rows:
        book_name = row.get("book_name", "").strip()
        if book_name and book_name not in books:
            books.append(book_name)
    return books


def append_translation_rows(lines: List[str], testament: str, rows: List[Dict[str, str]]) -> None:
    lines.append(f"## {testament}")
    lines.append("")

    current_book = None
    current_chapter = None
    for row in rows:
        book_name = row.get("book_name", "").strip()
        chapter = row.get("chapter", "").strip()
        ref = row.get("ref", "").strip()
        draft = row.get("draft_translation", "").strip()
        if book_name != current_book:
            current_book = book_name
            current_chapter = None
            lines.append(f"### {book_name}")
            lines.append("")
        if chapter != current_chapter:
            current_chapter = chapter
            lines.append(f"#### Chapter {chapter}")
            lines.append("")
        lines.append(f"**{ref}**")
        lines.append("")
        lines.append(draft or "No draft translation recorded.")
        lines.append("")


def build_combined_translation_only_markdown(
    ot_rows: List[Dict[str, str]],
    nt_rows: List[Dict[str, str]],
) -> str:
    books = ordered_books(ot_rows) + ordered_books(nt_rows)
    scope = f"{books[0]}-{books[-1]} ({len(books)} books)" if books else "Unknown scope"
    lines = [
        "# Fresh Translation Draft",
        "",
        f"Scope: {scope}",
        "",
    ]
    append_translation_rows(lines, "Old Testament", ot_rows)
    append_translation_rows(lines, "New Testament", nt_rows)
    return "\n".join(lines).strip() + "\n"


def build_diagnostics(
    ot_rows: List[Dict[str, str]],
    nt_rows: List[Dict[str, str]],
    ot_source_path: Path,
    nt_source_path: Path,
    output_path: Path,
) -> Dict[str, object]:
    ot_books = ordered_books(ot_rows)
    nt_books = ordered_books(nt_rows)
    return {
        "output": str(output_path),
        "scope": f"{ot_books[0]}-{nt_books[-1]} ({len(ot_books) + len(nt_books)} books)",
        "ot_source": str(ot_source_path),
        "nt_source": str(nt_source_path),
        "ot_rows": len(ot_rows),
        "nt_rows": len(nt_rows),
        "total_rows": len(ot_rows) + len(nt_rows),
        "ot_book_count": len(ot_books),
        "nt_book_count": len(nt_books),
        "total_book_count": len(ot_books) + len(nt_books),
        "ot_books": ot_books,
        "nt_books": nt_books,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ot-source", default=str(DEFAULT_OT_SOURCE))
    parser.add_argument("--nt-source", default=str(DEFAULT_NT_SOURCE))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--diagnostics", default=str(DEFAULT_DIAGNOSTICS))
    args = parser.parse_args()

    ot_source_path = Path(args.ot_source)
    nt_source_path = Path(args.nt_source)
    output_path = Path(args.output)
    diagnostics_path = Path(args.diagnostics)

    ot_rows = load_csv(ot_source_path)
    nt_rows = load_csv(nt_source_path)
    ensure_source_columns(ot_rows)
    ensure_source_columns(nt_rows)
    if not ot_rows:
        raise ValueError("No OT source rows found.")
    if not nt_rows:
        raise ValueError("No NT source rows found.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    diagnostics_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(
        build_combined_translation_only_markdown(ot_rows, nt_rows),
        encoding="utf-8",
    )
    diagnostics_path.write_text(
        json.dumps(
            build_diagnostics(ot_rows, nt_rows, ot_source_path, nt_source_path, output_path),
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "translation_only": str(output_path),
                "diagnostics": str(diagnostics_path),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
