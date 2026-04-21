#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path

from build_english_witness_review import load_latest_review_statuses


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.csv"
DEFAULT_CSV = ROOT / "output" / "fresh_vs_brenton_ot_decision_queue.csv"
DEFAULT_MD = ROOT / "output" / "fresh_vs_brenton_ot_decision_queue.md"


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def pick_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    picked = []
    for row in rows:
        decision_count = int(row.get("decision_count", "0") or "0")
        footnote_count = int(row.get("footnote_count", "0") or "0")
        if decision_count or footnote_count:
            picked.append(row)
    return sorted(picked, key=lambda row: (-int(row["priority_score"]), row["ref"]))


def build_csv_rows(rows: list[dict[str, str]], latest_review_statuses: dict[str, str]) -> list[dict[str, str]]:
    out = []
    for idx, row in enumerate(rows, start=1):
        review_status = latest_review_statuses.get(row["ref"], "pending") or "pending"
        out.append(
            {
                "order": str(idx),
                "ref": row["ref"],
                "book_name": row["book_name"],
                "importance": row["importance"],
                "priority_score": row["priority_score"],
                "decision_count": row["decision_count"],
                "footnote_count": row["footnote_count"],
                "keyword_hits": row["keyword_hits"],
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
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_markdown(rows: list[dict[str, str]]) -> str:
    lines = [
        "# OT Decision Queue",
        "",
        f"Rows: {len(rows)}",
        "",
        "Only verses with tracked decision rows or footnotes.",
        "",
    ]
    for row in rows[:60]:
        lines.append(
            f"- {row['order']}. {row['ref']} | score {row['priority_score']} | "
            f"decisions {row['decision_count']} | footnotes {row['footnote_count']} | {row['review_status']}"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--csv-output", default=str(DEFAULT_CSV))
    parser.add_argument("--markdown-output", default=str(DEFAULT_MD))
    args = parser.parse_args()

    rows = pick_rows(load_rows(Path(args.source)))
    csv_rows = build_csv_rows(rows, load_latest_review_statuses())
    write_csv(Path(args.csv_output), csv_rows)
    Path(args.markdown_output).write_text(build_markdown(csv_rows), encoding="utf-8")
    print(args.csv_output)
    print(args.markdown_output)


if __name__ == "__main__":
    main()
