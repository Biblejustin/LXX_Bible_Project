#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
OUTPUT = ROOT / "output" / "working"


def slugify(text: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "_" for ch in text).strip("_")


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, cwd=ROOT)


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def build_scope_label(book: str, chapter: int | None, chapter_start: int | None, chapter_end: int | None) -> str:
    if chapter is not None:
        return f"{slugify(book)}_{chapter}"
    if chapter_start is not None and chapter_end is not None:
        return f"{slugify(book)}_{chapter_start}_{chapter_end}"
    if chapter_start is not None:
        return f"{slugify(book)}_{chapter_start}_end"
    return slugify(book)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book", required=True)
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--chapter-start", type=int)
    parser.add_argument("--chapter-end", type=int)
    parser.add_argument("--min-importance", choices=["none", "low", "medium", "high"], default="medium")
    parser.add_argument("--source", default="data/raw/lxx_greek/ot_full.csv")
    args = parser.parse_args()

    if args.chapter is not None and (args.chapter_start is not None or args.chapter_end is not None):
        raise SystemExit("--chapter conflicts with --chapter-start/--chapter-end")

    label = build_scope_label(args.book, args.chapter, args.chapter_start, args.chapter_end)
    OUTPUT.mkdir(parents=True, exist_ok=True)

    worksheet = OUTPUT / f"{label}.md"
    translation_only = OUTPUT / f"{label}_translation_only.md"
    translation_diag = OUTPUT / f"{label}_diagnostics.json"
    compare_md = OUTPUT / f"{label}_compare.md"
    compare_csv = OUTPUT / f"{label}_compare.csv"
    compare_diag = OUTPUT / f"{label}_compare_diagnostics.json"

    scope_args: list[str] = ["--book", args.book]
    if args.chapter is not None:
        scope_args += ["--chapter", str(args.chapter)]
    else:
        if args.chapter_start is not None:
            scope_args += ["--chapter-start", str(args.chapter_start)]
        if args.chapter_end is not None:
            scope_args += ["--chapter-end", str(args.chapter_end)]

    py = sys.executable
    run(
        [
            py,
            str(SCRIPTS / "build_fresh_translation.py"),
            "--source",
            args.source,
            *scope_args,
            "--skip-undrafted",
            "--output",
            str(worksheet),
            "--translation-only-output",
            str(translation_only),
            "--diagnostics",
            str(translation_diag),
        ]
    )
    run(
        [
            py,
            str(SCRIPTS / "build_fresh_vs_brenton_compare.py"),
            "--source",
            args.source,
            *scope_args,
            "--min-importance",
            args.min_importance,
            "--output",
            str(compare_md),
            "--csv-output",
            str(compare_csv),
            "--diagnostics",
            str(compare_diag),
        ]
    )

    translation_data = load_json(translation_diag)
    compare_data = load_json(compare_diag)
    print(
        json.dumps(
            {
                "scope": translation_data.get("selected_scope"),
                "drafted_rows": translation_data.get("output_drafted_rows"),
                "compare_rows": compare_data.get("output_compare_rows"),
                "min_importance": compare_data.get("min_importance"),
                "worksheet": str(worksheet),
                "translation_only": str(translation_only),
                "compare_markdown": str(compare_md),
                "compare_csv": str(compare_csv),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
