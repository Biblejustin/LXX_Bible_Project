#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_script(script_name: str) -> None:
    script_path = ROOT / "scripts" / script_name
    subprocess.run([sys.executable, str(script_path)], check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.parse_args()

    run_script("build_priority_diff_review.py")
    run_script("build_priority_book_reviews.py")
    run_script("build_priority_theme_reviews.py")
    run_script("build_priority_review_queue.py")

    print(
        json.dumps(
            {
                "priority_review": str(ROOT / "output" / "fresh_vs_brenton_ot_priority_review.md"),
                "priority_top100": str(ROOT / "output" / "fresh_vs_brenton_ot_priority_top100.md"),
                "theme_overview": str(ROOT / "output" / "fresh_vs_brenton_ot_theme_overview.md"),
                "theme_index": str(ROOT / "output" / "priority_themes" / "index.md"),
                "book_index": str(ROOT / "output" / "priority_books" / "index.md"),
                "review_queue": str(ROOT / "output" / "fresh_vs_brenton_ot_review_queue.csv"),
                "review_queue_readme": str(ROOT / "output" / "fresh_vs_brenton_ot_review_queue.md"),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
