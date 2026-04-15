#!/usr/bin/env python3
import argparse
import csv
import html
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, List
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "lxx_greek"
DEFAULT_OUTPUT = DATA / "ot_full.csv"
INDEX_URL = "https://www.sntjohnny.com/original_texts/septuatintgreek/index.htm"
CHAPTER_URL = "https://www.sntjohnny.com/original_texts/septuatintgreek/{book_num:02d}_{chapter:03d}.htm"
SPECIAL_FALLBACKS = {
    ("PRO", 25): "https://www.septuagint.bible/-/paroimiai-solomontos-kephalaio-25",
    ("PRO", 26): "https://www.septuagint.bible/-/paroimiai-solomontos-kephalaio-26",
    ("PRO", 27): "https://www.septuagint.bible/-/paroimiai-solomontos-kephalaio-27",
    ("PRO", 28): "https://www.septuagint.bible/-/paroimiai-solomontos-kephalaio-28",
    ("PRO", 29): "https://www.septuagint.bible/-/paroimiai-solomontos-kephalaio-29",
}

BOOKS = [
    ("GEN", "Genesis"),
    ("EXO", "Exodus"),
    ("LEV", "Leviticus"),
    ("NUM", "Numbers"),
    ("DEU", "Deuteronomy"),
    ("JOS", "Joshua"),
    ("JDG", "Judges"),
    ("RUT", "Ruth"),
    ("1SA", "1 Samuel"),
    ("2SA", "2 Samuel"),
    ("1KI", "1 Kings"),
    ("2KI", "2 Kings"),
    ("1CH", "1 Chronicles"),
    ("2CH", "2 Chronicles"),
    ("EZR", "Ezra"),
    ("NEH", "Nehemiah"),
    ("EST", "Esther"),
    ("JOB", "Job"),
    ("PSA", "Psalms"),
    ("PRO", "Proverbs"),
    ("ECC", "Ecclesiastes"),
    ("SNG", "Song of Solomon"),
    ("ISA", "Isaiah"),
    ("JER", "Jeremiah"),
    ("LAM", "Lamentations"),
    ("EZK", "Ezekiel"),
    ("DAN", "Daniel"),
    ("HOS", "Hosea"),
    ("JOL", "Joel"),
    ("AMO", "Amos"),
    ("OBA", "Obadiah"),
    ("JON", "Jonah"),
    ("MIC", "Micah"),
    ("NAM", "Nahum"),
    ("HAB", "Habakkuk"),
    ("ZEP", "Zephaniah"),
    ("HAG", "Haggai"),
    ("ZEC", "Zechariah"),
    ("MAL", "Malachi"),
]

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


def fetch_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_index_book_blocks(index_html: str) -> List[List[int]]:
    block_match = re.search(r"<blockquote>(.*)</blockquote>", index_html, flags=re.S)
    if not block_match:
        raise ValueError("Could not find OT index block.")
    parts = re.split(r"<br><br>\s*", block_match.group(1))
    chapter_blocks: List[List[int]] = []
    for part in parts:
        chapter_numbers = [int(value) for value in re.findall(r">(\d+)<", part)]
        if chapter_numbers:
            chapter_blocks.append(chapter_numbers)
    return chapter_blocks[: len(BOOKS)]


def normalize_greek_text(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


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


def split_inline_verses(article_text: str, chapter: int) -> List[Dict[str, str]]:
    if article_text.startswith(str(chapter)):
        article_text = article_text[len(str(chapter)) :].strip()
    article_text = re.sub(rf"^\s*{chapter}\s*", "", article_text)
    article_text = re.sub(r"\s+", " ", article_text).strip()

    matches = list(re.finditer(r"(?<!\d)(\d+)\s", article_text))
    verses: List[Dict[str, str]] = []
    if matches and matches[0].start() > 0:
        verse_one_text = article_text[: matches[0].start()].strip(" ;")
        if verse_one_text:
            verses.append({"chapter": str(chapter), "verse": "1", "greek_text": verse_one_text})
    for index, match in enumerate(matches):
        verse_num = int(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(article_text)
        verse_text = article_text[start:end].strip(" ;")
        if verse_text:
            verses.append({"chapter": str(chapter), "verse": str(verse_num), "greek_text": verse_text})
    return verses


def parse_chapter_verses(chapter_html: str) -> List[Dict[str, str]]:
    block_match = re.search(r"<blockquote>(.*?)</blockquote>", chapter_html, flags=re.S)
    if not block_match:
        raise ValueError("Could not find chapter blockquote.")
    block = block_match.group(1).replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n")
    verses: List[Dict[str, str]] = []
    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        match = re.match(r"(\d+):(\d+)\s+(.*)", line)
        if not match:
            continue
        chapter_num = match.group(1)
        verse_num = match.group(2)
        verse_text = normalize_greek_text(match.group(3))
        verses.append(
            {
                "chapter": chapter_num,
                "verse": verse_num,
                "greek_text": verse_text,
            }
        )
    return verses


def parse_fallback_chapter_verses(chapter_html: str, chapter: int) -> List[Dict[str, str]]:
    article_html = extract_article_html(chapter_html)
    article_text = normalize_article_text(article_html)
    return split_inline_verses(article_text, chapter)


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


def load_existing_rows(paths: List[Path]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for path in paths:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8", newline="") as handle:
            rows.extend(csv.DictReader(handle))
    return rows


def fetch_book_chapters(book_num: int, chapter_numbers: List[int]) -> Dict[int, str]:
    chapter_html: Dict[int, str] = {}
    with ThreadPoolExecutor(max_workers=min(12, max(1, len(chapter_numbers)))) as executor:
        futures = {
            executor.submit(fetch_text, CHAPTER_URL.format(book_num=book_num, chapter=chapter)): chapter
            for chapter in chapter_numbers
        }
        for future in as_completed(futures):
            chapter = futures[future]
            chapter_html[chapter] = future.result()
    return chapter_html


def build_rows(include_psalm_151: bool) -> List[Dict[str, str]]:
    index_html = fetch_text(INDEX_URL)
    chapter_blocks = parse_index_book_blocks(index_html)
    rows: List[Dict[str, str]] = []
    for book_num, (book_code, book_name) in enumerate(BOOKS, start=1):
        chapter_numbers = chapter_blocks[book_num - 1]
        if book_code == "PSA" and not include_psalm_151:
            chapter_numbers = [chapter for chapter in chapter_numbers if chapter <= 150]
        primary_chapters = [chapter for chapter in chapter_numbers if (book_code, chapter) not in SPECIAL_FALLBACKS]
        chapter_html = fetch_book_chapters(book_num=book_num, chapter_numbers=primary_chapters)
        for chapter in chapter_numbers:
            fallback_url = SPECIAL_FALLBACKS.get((book_code, chapter))
            if fallback_url:
                verses = parse_fallback_chapter_verses(fetch_text(fallback_url), chapter)
            else:
                verses = parse_chapter_verses(chapter_html[chapter])
            for verse_row in verses:
                rows.append(
                    {
                        "ref": f"{book_name} {verse_row['chapter']}:{verse_row['verse']}",
                        "book_code": book_code,
                        "book_name": book_name,
                        "chapter": verse_row["chapter"],
                        "verse": verse_row["verse"],
                        "greek_text": verse_row["greek_text"],
                        "transliteration": "",
                        "literal_gloss": "",
                        "syntax_notes": "",
                        "draft_translation": "",
                    }
                )
    return rows


def write_rows(path: Path, rows: List[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--merge-existing", action="append", default=[])
    parser.add_argument("--include-psalm-151", action="store_true")
    args = parser.parse_args()

    output_path = Path(args.output)
    existing_rows = load_existing_rows([Path(value) for value in args.merge_existing])
    rows = build_rows(include_psalm_151=args.include_psalm_151)
    if existing_rows:
        rows = merge_existing_rows(rows, existing_rows)
    write_rows(output_path, rows)
    print(f"Wrote {len(rows)} OT verse rows to {output_path}")


if __name__ == "__main__":
    main()
