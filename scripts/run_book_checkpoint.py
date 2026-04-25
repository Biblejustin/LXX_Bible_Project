#!/usr/bin/env python3
import argparse
import csv
import difflib
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
DECISIONS = ROOT / "data" / "research" / "translation_decisions.csv"
FOOTNOTES = ROOT / "data" / "research" / "translation_footnotes.csv"
OUTPUT = ROOT / "output"
PRESERVE_LINE_ENDING_PATHS = [
    ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv",
    ROOT / "output" / "fresh_vs_brenton_ot_drafted.csv",
]

csv.field_size_limit(sys.maxsize)


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, cwd=ROOT)


def count_rows(path: Path) -> int:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def drafted_counts() -> dict[str, tuple[int, int]]:
    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    with SOURCE.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            book = row["book_name"]
            counts[book][1] += 1
            if row["draft_translation"].strip():
                counts[book][0] += 1
    return {book: (done, total) for book, (done, total) in counts.items()}


def preserve_line_endings_from_head(paths: list[Path]) -> list[str]:
    """Keep existing mixed CRLF/LF layout on large tracked CSVs after rewrites."""
    restored: list[str] = []
    for path in paths:
        try:
            head_bytes = subprocess.check_output(
                ["git", "show", f"HEAD:{path.relative_to(ROOT).as_posix()}"],
                cwd=ROOT,
            )
        except subprocess.CalledProcessError:
            continue
        if not path.exists():
            continue

        current_text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        head_lines = head_bytes.decode("utf-8").splitlines(keepends=True)
        head_no_endings = [line.rstrip("\r\n") for line in head_lines]
        current_no_endings = current_text.splitlines()

        out: list[str] = []
        matcher = difflib.SequenceMatcher(None, head_no_endings, current_no_endings, autojunk=False)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                out.extend(head_lines[i1:i2])
            elif tag in {"replace", "insert"}:
                out.extend(line + "\n" for line in current_no_endings[j1:j2])
        path.write_text("".join(out), encoding="utf-8", newline="")
        restored.append(str(path.relative_to(ROOT)))
    return restored


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-sync", action="store_true", help="Do not sync support tables from OT source.")
    parser.add_argument(
        "--skip-contextual-name-decisions",
        action="store_true",
        help="Do not enforce contextual proper-name decisions against OT source.",
    )
    parser.add_argument(
        "--skip-name-notes",
        action="store_true",
        help="Do not regenerate proper-name note coverage before the OT build.",
    )
    parser.add_argument(
        "--no-preserve-csv-line-endings",
        action="store_true",
        help="Do not restore tracked CSV line-ending layout after generated rewrites.",
    )
    parser.add_argument("--smoke-test", action="store_true", help="Run tests/test_smoke.py after build.")
    parser.add_argument("--diff-check", action="store_true", help="Run git diff --check after build.")
    args = parser.parse_args()

    py = sys.executable
    if not args.skip_contextual_name_decisions:
        run([py, str(SCRIPTS / "apply_contextual_proper_name_decisions.py"), "--summary-only"])
    if not args.skip_sync:
        run([py, str(SCRIPTS / "sync_ot_support_text.py")])
    if not args.skip_name_notes:
        run([py, str(SCRIPTS / "update_proper_name_transliteration_notes.py"), "--summary-only"])
    run(
        [
            py,
            str(SCRIPTS / "build_fresh_translation.py"),
            "--source",
            str(SOURCE),
            "--output",
            str(OUTPUT / "fresh_translation_ot_full.md"),
            "--translation-only-output",
            str(OUTPUT / "fresh_translation_ot_full_translation_only.md"),
            "--diagnostics",
            str(OUTPUT / "fresh_translation_ot_full_diagnostics.json"),
        ]
    )
    run(
        [
            py,
            str(SCRIPTS / "build_fresh_vs_brenton_compare.py"),
            "--source",
            str(SOURCE),
            "--output",
            str(OUTPUT / "fresh_vs_brenton_ot_drafted.md"),
            "--csv-output",
            str(OUTPUT / "fresh_vs_brenton_ot_drafted.csv"),
            "--diagnostics",
            str(OUTPUT / "fresh_vs_brenton_ot_drafted_diagnostics.json"),
        ]
    )
    run(
        [
            py,
            str(SCRIPTS / "build_fresh_logos_bible.py"),
            "--testament",
            "ot",
            "--source",
            str(SOURCE),
            "--logos-docx",
            str(OUTPUT / "logos" / "fresh_translation_ot_logos_bible.docx"),
            "--preview",
            str(OUTPUT / "logos" / "fresh_translation_ot_logos_bible_preview.md"),
            "--diagnostics",
            str(OUTPUT / "logos" / "fresh_translation_ot_logos_bible_diagnostics.json"),
            "--mt-bridge-docx",
            str(OUTPUT / "logos" / "fresh_translation_ot_logos_bible_mt_notes.docx"),
            "--proof-docx",
            str(OUTPUT / "logos" / "fresh_translation_ot_proofreading.docx"),
        ]
    )
    restored_line_endings = []
    if not args.no_preserve_csv_line_endings:
        restored_line_endings = preserve_line_endings_from_head(PRESERVE_LINE_ENDING_PATHS)
    if args.diff_check:
        run(["git", "diff", "--check"])
    if args.smoke_test:
        run([py, "-m", "pytest", "-q", "tests/test_smoke.py"])

    counts = drafted_counts()
    done_books = {book: f"{done}/{total}" for book, (done, total) in counts.items() if done == total and total}
    in_progress = {book: f"{done}/{total}" for book, (done, total) in counts.items() if 0 < done < total}

    print(
        json.dumps(
            {
                "drafted_rows": sum(done for done, _ in counts.values()),
                "decision_rows": count_rows(DECISIONS),
                "footnote_rows": count_rows(FOOTNOTES),
                "done_books": done_books,
                "in_progress_books": in_progress,
                "translation_only": str(OUTPUT / "fresh_translation_ot_full_translation_only.md"),
                "compare_csv": str(OUTPUT / "fresh_vs_brenton_ot_drafted.csv"),
                "logos_preview": str(OUTPUT / "logos" / "fresh_translation_ot_logos_bible_preview.md"),
                "enforced_contextual_name_decisions": not args.skip_contextual_name_decisions,
                "synced_support_tables": not args.skip_sync,
                "rebuilt_name_notes": not args.skip_name_notes,
                "preserved_line_endings": restored_line_endings,
                "smoke_test": args.smoke_test,
                "diff_check": args.diff_check,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
