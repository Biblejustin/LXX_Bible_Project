#!/usr/bin/env python3
import argparse
import csv
import html
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "lxx_greek"
DEFAULT_OUTPUT = DATA / "genesis_full.csv"
SOURCE_TEMPLATE = "https://www.septuagint.bible/-/genesis-{chapter}"

CSV_COLUMNS = [
    "ref",
    "book_code",
    "book_name",
    "chapter",
    "verse",
    "greek_text",
    "transliteration",
    "literal_gloss",
    "syntax_notes",
    "draft_translation",
]


def fetch_html(chapter: int) -> str:
    url = SOURCE_TEMPLATE.format(chapter=chapter)
    result = subprocess.run(
        ["curl", "-L", "-s", url],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout


def extract_article_html(page_html: str) -> str:
    match = re.search(
        r'<div class="journal-content-article">(.*?)</div>\s*<!-- custom modification for OG Image start -->',
        page_html,
        flags=re.S,
    )
    if not match:
        raise ValueError("Could not find article body.")
    return match.group(1)


def normalize_article_text(article_html: str) -> str:
    text = article_html
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</p>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_verses(chapter: int, article_text: str) -> List[Tuple[int, str]]:
    if article_text.startswith(str(chapter)):
        article_text = article_text[len(str(chapter)) :].strip()
    article_text = re.sub(rf"^\s*{chapter}\s*", "", article_text)
    article_text = re.sub(r"\s+", " ", article_text).strip()

    matches = list(re.finditer(r"(?<!\d)(\d+)\s", article_text))
    verses: List[Tuple[int, str]] = []
    if matches and matches[0].start() > 0:
        verse_one_text = article_text[: matches[0].start()].strip(" ;")
        if verse_one_text:
            verses.append((1, verse_one_text))
    for index, match in enumerate(matches):
        verse_num = int(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(article_text)
        verse_text = article_text[start:end].strip(" ;")
        if verse_text:
            verses.append((verse_num, verse_text))
    return verses


def build_rows() -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for chapter in range(1, 51):
        page_html = fetch_html(chapter)
        article_html = extract_article_html(page_html)
        article_text = normalize_article_text(article_html)
        for verse_num, verse_text in split_verses(chapter, article_text):
            rows.append(
                {
                    "ref": f"Genesis {chapter}:{verse_num}",
                    "book_code": "GEN",
                    "book_name": "Genesis",
                    "chapter": str(chapter),
                    "verse": str(verse_num),
                    "greek_text": verse_text,
                    "transliteration": "",
                    "literal_gloss": "",
                    "syntax_notes": "",
                    "draft_translation": "",
                }
            )
    return rows


def merge_existing_rows(base_rows: List[Dict[str, str]], existing_rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    existing_by_ref = {row.get("ref", "").strip(): row for row in existing_rows if row.get("ref", "").strip()}
    merged: List[Dict[str, str]] = []
    for row in base_rows:
        current = dict(row)
        existing = existing_by_ref.get(current["ref"])
        if existing:
            for field in CSV_COLUMNS:
                value = existing.get(field, "")
                if value.strip():
                    current[field] = value
        merged.append(current)
    return merged


def load_existing_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: List[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--merge-existing")
    args = parser.parse_args()

    output_path = Path(args.output)
    existing_rows: List[Dict[str, str]] = []
    if args.merge_existing:
        existing_rows = load_existing_rows(Path(args.merge_existing))

    rows = build_rows()
    if existing_rows:
        rows = merge_existing_rows(rows, existing_rows)
    write_rows(output_path, rows)
    print(f"Wrote {len(rows)} Genesis verse rows to {output_path}")


if __name__ == "__main__":
    main()
