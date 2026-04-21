#!/usr/bin/env python3
import csv
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


def main() -> None:
    py = sys.executable
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
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
