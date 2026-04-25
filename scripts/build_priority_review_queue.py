#!/usr/bin/env python3
import argparse
import csv
from collections import defaultdict
from pathlib import Path

from build_english_witness_review import load_latest_review_statuses
from build_priority_theme_reviews import classify_row, load_rows


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.csv"
DEFAULT_CSV = ROOT / "output" / "fresh_vs_brenton_ot_review_queue.csv"
DEFAULT_MD = ROOT / "output" / "fresh_vs_brenton_ot_review_queue.md"

THEME_LABELS = {
    "theology_divine_identity": "theology",
    "creation_anthropology": "anthropology",
    "covenant_law_judgment": "covenant/law",
    "ritual_priesthood": "ritual",
    "kingship_messianic": "kingship",
    "death_afterlife": "death/afterlife",
    "textual_lexical": "textual/lexical",
}


def build_queue_rows(rows: list[dict[str, str]], latest_review_statuses: dict[str, str]) -> list[dict[str, str]]:
    ranked = sorted(rows, key=lambda row: (-int(row["priority_score"]), row["ref"]))
    out: list[dict[str, str]] = []
    for order, row in enumerate(ranked, start=1):
        themes = [THEME_LABELS[slug] for slug in classify_row(row)]
        review_status = latest_review_statuses.get(row["ref"], "pending") or "pending"
        out.append(
            {
                "order": str(order),
                "ref": row["ref"],
                "book_name": row["book_name"],
                "importance": row["importance"],
                "priority_score": row["priority_score"],
                "themes": ", ".join(themes),
                "reasons": row["reasons"],
                "fresh_translation": row["fresh_translation"],
                "brenton_translation": row["brenton_translation"],
                "review_status": review_status,
                "decision": "",
                "review_notes": "",
            }
        )
    return out


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_markdown(rows: list[dict[str, str]]) -> str:
    by_theme: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        for theme in row["themes"].split(", "):
            if theme:
                by_theme[theme].append(row)

    lines = [
        "# OT Review Queue",
        "",
        f"Rows: {len(rows)}",
        "",
        "Use CSV for edits.",
        "Use MD for reading order.",
        "",
        "## Theme Counts",
    ]
    for theme, theme_rows in sorted(by_theme.items()):
        lines.append(f"- {theme}: {len(theme_rows)}")

    lines.append("")
    lines.append("## Top 50")
    for row in rows[:50]:
        lines.append(
            f"- {row['order']}. {row['ref']} | score {row['priority_score']} | "
            f"{row['themes']} | {row['review_status']}"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--csv-output", default=str(DEFAULT_CSV))
    parser.add_argument("--markdown-output", default=str(DEFAULT_MD))
    args = parser.parse_args()

    rows = load_rows(Path(args.source))
    queue_rows = build_queue_rows(rows, load_latest_review_statuses())
    write_csv(Path(args.csv_output), queue_rows)
    Path(args.markdown_output).write_text(build_markdown(queue_rows), encoding="utf-8")
    print(args.csv_output)
    print(args.markdown_output)


if __name__ == "__main__":
    main()
