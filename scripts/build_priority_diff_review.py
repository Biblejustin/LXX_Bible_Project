#!/usr/bin/env python3
import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "output" / "fresh_vs_brenton_ot_drafted.csv"
DEFAULT_OUTPUT = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.md"
DEFAULT_CSV = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.csv"
DEFAULT_DIAGNOSTICS = ROOT / "output" / "fresh_vs_brenton_ot_priority_review_diagnostics.json"

IMPORTANCE_SCORE = {"none": 0, "low": 1, "medium": 2, "high": 4}
KEYWORD_RE = re.compile(
    r"\b("
    r"spirit|wind|soul|being|covenant|mercy|truth|righteous|righteousness|justice|law|altar|priest|"
    r"sacrifice|sin|forgive|salvation|savior|holy|holiness|lord|god|name|glory|king|anointed|"
    r"firstborn|shepherd|faith|grace|compassion|beloved|virgin|servant|messenger|angel|day one|"
    r"firm span|hades|abyss|seed|offspring|image|created|create|resurrection|repent|peace|judgment"
    r")\b",
    re.IGNORECASE,
)


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def score_row(row: dict[str, str]) -> tuple[int, list[str], list[str]]:
    text = f"{row.get('fresh_translation', '')} {row.get('brenton_translation', '')}"
    keyword_hits = sorted({match.group(0).lower() for match in KEYWORD_RE.finditer(text)})
    decision_count = int(row.get("decision_count", "0") or "0")
    footnote_count = int(row.get("footnote_count", "0") or "0")
    importance = row.get("importance", "none")

    score = 0
    score += IMPORTANCE_SCORE.get(importance, 0)
    score += min(decision_count, 2) * 3
    score += min(footnote_count, 2) * 2
    score += len(keyword_hits) * 2
    score += 0 if row.get("same_normalized", "") == "yes" else 1

    reasons: list[str] = []
    if decision_count:
        reasons.append(f"decisions={decision_count}")
    if footnote_count:
        reasons.append(f"footnotes={footnote_count}")
    if importance != "none":
        reasons.append(f"importance={importance}")
    if keyword_hits:
        reasons.append("keywords=" + ", ".join(keyword_hits[:6]))

    return score, keyword_hits, reasons


def build_priority_rows(rows: list[dict[str, str]], per_book_limit: int, min_score: int) -> list[dict[str, str]]:
    grouped: dict[str, list[tuple[int, int, dict[str, str], list[str], list[str]]]] = defaultdict(list)
    for index, row in enumerate(rows):
        score, keyword_hits, reasons = score_row(row)
        if score < min_score:
            continue
        grouped[row["book_name"]].append((score, index, row, keyword_hits, reasons))

    selected: list[tuple[int, dict[str, str], list[str], list[str]]] = []
    for book_rows in grouped.values():
        ranked = sorted(book_rows, key=lambda item: (-item[0], item[1]))[:per_book_limit]
        selected.extend((item[1], item[2], item[3], item[4]) for item in ranked)

    selected.sort(key=lambda item: item[0])
    out_rows: list[dict[str, str]] = []
    for _, row, keyword_hits, reasons in selected:
        out_rows.append(
            {
                "ref": row["ref"],
                "book_name": row["book_name"],
                "chapter": row["chapter"],
                "verse": row["verse"],
                "importance": row["importance"],
                "priority_score": str(score_row(row)[0]),
                "decision_count": row["decision_count"],
                "footnote_count": row["footnote_count"],
                "keyword_hits": ", ".join(keyword_hits),
                "reasons": "; ".join(reasons),
                "fresh_translation": row["fresh_translation"],
                "brenton_translation": row["brenton_translation"],
            }
        )
    return out_rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_markdown(rows: list[dict[str, str]], per_book_limit: int, min_score: int) -> str:
    by_book: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_book[row["book_name"]].append(row)

    lines = [
        "# OT Priority Difference Review",
        "",
        f"Per-book limit: {per_book_limit}",
        f"Minimum score: {min_score}",
        f"Selected verses: {len(rows)}",
        "",
        "Use:",
        "- review verses most likely to matter for theology or core language choices",
        "- not exhaustive",
        "",
        "## By Book",
    ]
    for book, book_rows in by_book.items():
        lines.append(f"- {book}: {len(book_rows)}")

    for book, book_rows in by_book.items():
        lines.append("")
        lines.append(f"## {book}")
        for row in book_rows:
            lines.append("")
            lines.append(f"### {row['ref']}")
            lines.append(f"- score: {row['priority_score']}")
            lines.append(f"- reasons: {row['reasons']}")
            lines.append(f"- fresh: {row['fresh_translation']}")
            lines.append(f"- brenton: {row['brenton_translation'] or '[missing]'}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--csv-output", default=str(DEFAULT_CSV))
    parser.add_argument("--diagnostics", default=str(DEFAULT_DIAGNOSTICS))
    parser.add_argument("--per-book-limit", type=int, default=6)
    parser.add_argument("--min-score", type=int, default=4)
    args = parser.parse_args()

    source_rows = load_rows(Path(args.source))
    priority_rows = build_priority_rows(source_rows, args.per_book_limit, args.min_score)
    if not priority_rows:
        raise SystemExit("No priority rows selected.")

    output_path = Path(args.output)
    csv_path = Path(args.csv_output)
    diagnostics_path = Path(args.diagnostics)

    output_path.write_text(build_markdown(priority_rows, args.per_book_limit, args.min_score), encoding="utf-8")
    write_csv(csv_path, priority_rows)
    diagnostics_path.write_text(
        json.dumps(
            {
                "source": str(Path(args.source)),
                "selected_rows": len(priority_rows),
                "per_book_limit": args.per_book_limit,
                "min_score": args.min_score,
                "books": sorted({row["book_name"] for row in priority_rows}),
                "output": str(output_path),
                "csv_output": str(csv_path),
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(output_path),
                "csv_output": str(csv_path),
                "diagnostics": str(diagnostics_path),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
