#!/usr/bin/env python3
import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.csv"
DEFAULT_OUTPUT_DIR = ROOT / "output" / "priority_books"
DEFAULT_TOP_OUTPUT = ROOT / "output" / "fresh_vs_brenton_ot_priority_top100.md"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def build_book_markdown(book: str, rows: list[dict[str, str]]) -> str:
    lines = [
        f"# {book} Priority Review",
        "",
        f"Selected verses: {len(rows)}",
        "",
    ]
    for row in rows:
        lines.append(f"## {row['ref']}")
        lines.append(f"- score: {row['priority_score']}")
        lines.append(f"- reasons: {row['reasons']}")
        lines.append(f"- fresh: {row['fresh_translation']}")
        lines.append(f"- brenton: {row['brenton_translation'] or '[missing]'}")
        lines.append("")
    return "\n".join(lines)


def build_top_markdown(rows: list[dict[str, str]], limit: int) -> str:
    ranked = sorted(rows, key=lambda row: (-int(row["priority_score"]), row["ref"]))[:limit]
    lines = [
        "# OT Priority Review Top 100",
        "",
        f"Rows: {len(ranked)}",
        "",
    ]
    for row in ranked:
        lines.append(f"## {row['ref']}")
        lines.append(f"- book: {row['book_name']}")
        lines.append(f"- score: {row['priority_score']}")
        lines.append(f"- reasons: {row['reasons']}")
        lines.append(f"- fresh: {row['fresh_translation']}")
        lines.append(f"- brenton: {row['brenton_translation'] or '[missing]'}")
        lines.append("")
    return "\n".join(lines)


def build_index(book_paths: list[tuple[str, Path, int]]) -> str:
    lines = [
        "# OT Priority Review Index",
        "",
        f"Books: {len(book_paths)}",
        "",
    ]
    for book, path, count in book_paths:
        lines.append(f"- {book}: {count} → {path.name}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--top-output", default=str(DEFAULT_TOP_OUTPUT))
    parser.add_argument("--top-limit", type=int, default=100)
    args = parser.parse_args()

    rows = load_rows(Path(args.source))
    by_book: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_book[row["book_name"]].append(row)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    book_paths: list[tuple[str, Path, int]] = []
    for book, book_rows in by_book.items():
        book_path = output_dir / f"{slugify(book)}_priority_review.md"
        book_path.write_text(build_book_markdown(book, book_rows), encoding="utf-8")
        book_paths.append((book, book_path, len(book_rows)))

    index_path = output_dir / "index.md"
    index_path.write_text(build_index(book_paths), encoding="utf-8")

    top_output = Path(args.top_output)
    top_output.write_text(build_top_markdown(rows, args.top_limit), encoding="utf-8")

    print(index_path)
    print(top_output)


if __name__ == "__main__":
    main()
