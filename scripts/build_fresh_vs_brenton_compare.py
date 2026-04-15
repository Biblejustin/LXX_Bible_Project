#!/usr/bin/env python3
import argparse
import csv
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = DATA / "raw"
LXX_GREEK = RAW / "lxx_greek"
RESEARCH = DATA / "research"
OUTPUT = ROOT / "output"

DEFAULT_SOURCE = LXX_GREEK / "ot_full.csv"
DEFAULT_BRENTON_ZIP = RAW / "eng-Brenton_usfm.zip"
DEFAULT_DECISIONS = RESEARCH / "translation_decisions.csv"
DEFAULT_FOOTNOTES = RESEARCH / "translation_footnotes.csv"
DEFAULT_OUTPUT = OUTPUT / "fresh_vs_brenton_ot_drafted.md"
DEFAULT_CSV = OUTPUT / "fresh_vs_brenton_ot_drafted.csv"
DEFAULT_DIAGNOSTICS = OUTPUT / "fresh_vs_brenton_ot_drafted_diagnostics.json"
IMPORTANCE_ORDER = {"none": 0, "low": 1, "medium": 2, "high": 3}

BOOK_FILENAME_MAP = {
    "GEN": "02-GENeng-Brenton.usfm",
    "EXO": "03-EXOeng-Brenton.usfm",
    "LEV": "04-LEVeng-Brenton.usfm",
    "NUM": "05-NUMeng-Brenton.usfm",
    "DEU": "06-DEUeng-Brenton.usfm",
    "JOS": "07-JOSeng-Brenton.usfm",
    "JDG": "08-JDGeng-Brenton.usfm",
    "RUT": "09-RUTeng-Brenton.usfm",
    "1SA": "10-1SAeng-Brenton.usfm",
    "2SA": "11-2SAeng-Brenton.usfm",
    "1KI": "12-1KIeng-Brenton.usfm",
    "2KI": "13-2KIeng-Brenton.usfm",
    "1CH": "14-1CHeng-Brenton.usfm",
    "2CH": "15-2CHeng-Brenton.usfm",
    "EZR": "16-EZReng-Brenton.usfm",
    "NEH": "17-NEHeng-Brenton.usfm",
    "EST": "19-ESTeng-Brenton.usfm",
    "JOB": "23-JOBeng-Brenton.usfm",
    "PSA": "24-PSAeng-Brenton.usfm",
    "PRO": "25-PROeng-Brenton.usfm",
    "ECC": "26-ECCeng-Brenton.usfm",
    "SNG": "27-SNGeng-Brenton.usfm",
    "ISA": "28-ISAeng-Brenton.usfm",
    "JER": "29-JEReng-Brenton.usfm",
    "LAM": "30-LAMeng-Brenton.usfm",
    "EZK": "33-EZKeng-Brenton.usfm",
    "DAN": "34-DANeng-Brenton.usfm",
    "HOS": "35-HOSeng-Brenton.usfm",
    "JOL": "36-JOLeng-Brenton.usfm",
    "AMO": "37-AMOeng-Brenton.usfm",
    "OBA": "38-OBAeng-Brenton.usfm",
    "JON": "39-JONeng-Brenton.usfm",
    "MIC": "40-MICeng-Brenton.usfm",
    "NAM": "41-NAMeng-Brenton.usfm",
    "HAB": "42-HABeng-Brenton.usfm",
    "ZEP": "43-ZEPeng-Brenton.usfm",
    "HAG": "44-HAGeng-Brenton.usfm",
    "ZEC": "45-ZECeng-Brenton.usfm",
    "MAL": "46-MALeng-Brenton.usfm",
}


def load_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def matches_book(row: Dict[str, str], book: str | None) -> bool:
    if not book:
        return True
    wanted = book.strip().lower()
    return (
        row.get("book_name", "").strip().lower() == wanted
        or row.get("book_code", "").strip().lower() == wanted
    )


def filter_rows_by_scope(
    rows: List[Dict[str, str]],
    book: str | None,
    chapter: int | None,
    chapter_start: int | None,
    chapter_end: int | None,
) -> List[Dict[str, str]]:
    filtered: List[Dict[str, str]] = []
    for row in rows:
        if not matches_book(row, book):
            continue
        row_chapter = row.get("chapter", "").strip()
        if not row_chapter:
            continue
        chapter_value = int(row_chapter)
        if chapter is not None and chapter_value != chapter:
            continue
        if chapter_start is not None and chapter_value < chapter_start:
            continue
        if chapter_end is not None and chapter_value > chapter_end:
            continue
        filtered.append(row)
    return filtered


def describe_scope(rows: List[Dict[str, str]]) -> str:
    if not rows:
        return "Unknown scope"
    ordered_books: List[str] = []
    for row in rows:
        book_name = row.get("book_name", "").strip()
        if book_name and book_name not in ordered_books:
            ordered_books.append(book_name)
    if len(ordered_books) > 1:
        return f"{ordered_books[0]}-{ordered_books[-1]} ({len(ordered_books)} books)"
    chapters = sorted({int(row.get("chapter", "").strip()) for row in rows if row.get("chapter", "").strip()})
    if not chapters:
        return ordered_books[0]
    if chapters == list(range(chapters[0], chapters[-1] + 1)):
        return f"{ordered_books[0]} {chapters[0]}-{chapters[-1]}"
    return f"{ordered_books[0]} {', '.join(str(ch) for ch in chapters)}"


def clean_usfm_text(text: str) -> str:
    text = re.sub(r"\\f .*?\\f\*", "", text)
    text = re.sub(r"\\x .*?\\x\*", "", text)
    text = re.sub(r"\\add (.*?)\\add\*", r"\1", text)
    text = re.sub(r"\\sc (.*?)\\sc\*", r"\1", text)
    text = re.sub(r"\\[a-z0-9*]+\s*", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_brenton_book(zf: zipfile.ZipFile, filename: str, book_name: str) -> Dict[str, str]:
    text = zf.read(filename).decode("utf-8", errors="replace")
    current_chapter = None
    verses: Dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("\\c "):
            current_chapter = int(line.split()[1])
            continue
        if current_chapter is None or not line.startswith("\\v "):
            continue
        match = re.match(r"\\v\s+(\d+)\s+(.*)", line)
        if not match:
            continue
        verse = int(match.group(1))
        cleaned = clean_usfm_text(match.group(2))
        verses[f"{book_name} {current_chapter}:{verse}"] = cleaned
    return verses


def normalize_for_compare(text: str) -> str:
    text = text.lower()
    text = text.replace("'", "")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def guess_importance(ref: str, fresh: str, brenton: str, decision_count: int, footnote_count: int) -> str:
    fresh_norm = normalize_for_compare(fresh)
    brenton_norm = normalize_for_compare(brenton)
    if decision_count or footnote_count:
        return "high"
    hot_words = [
        "spirit",
        "wind",
        "soul",
        "being",
        "submission",
        "turning",
        "desire",
        "shrewd",
        "crafty",
        "watch",
        "crush",
        "origin",
        "genesis",
        "image",
        "humankind",
        "man",
        "woman",
        "husband",
        "labors",
        "works",
    ]
    if any(word in fresh_norm or word in brenton_norm for word in hot_words):
        return "medium"
    if fresh_norm != brenton_norm:
        return "low"
    return "none"


def build_rows(
    source_rows: List[Dict[str, str]],
    brenton_map: Dict[str, str],
    decision_rows: List[Dict[str, str]],
    footnote_rows: List[Dict[str, str]],
) -> Tuple[List[Dict[str, str]], Dict[str, object]]:
    decisions_by_ref = defaultdict(list)
    footnotes_by_ref = defaultdict(list)
    for row in decision_rows:
        decisions_by_ref[row.get("ref", "").strip()].append(row)
    for row in footnote_rows:
        footnotes_by_ref[row.get("ref", "").strip()].append(row)

    compare_rows: List[Dict[str, str]] = []
    missing_brenton = 0
    for row in source_rows:
        fresh = row.get("draft_translation", "").strip()
        if not fresh:
            continue
        ref = row.get("ref", "").strip()
        brenton = brenton_map.get(ref, "").strip()
        if not brenton:
            missing_brenton += 1
        decision_count = len(decisions_by_ref.get(ref, []))
        footnote_count = len(footnotes_by_ref.get(ref, []))
        importance = guess_importance(ref, fresh, brenton, decision_count, footnote_count)
        compare_rows.append(
            {
                "ref": ref,
                "book_name": row.get("book_name", "").strip(),
                "chapter": row.get("chapter", "").strip(),
                "verse": row.get("verse", "").strip(),
                "fresh_translation": fresh,
                "brenton_translation": brenton,
                "same_normalized": "yes" if normalize_for_compare(fresh) == normalize_for_compare(brenton) else "no",
                "decision_count": str(decision_count),
                "footnote_count": str(footnote_count),
                "importance": importance,
            }
        )
    diagnostics = {
        "drafted_rows_compared": len(compare_rows),
        "books_with_drafts": sorted({row["book_name"] for row in compare_rows}),
        "missing_brenton_rows": missing_brenton,
        "importance_counts": {
            level: sum(1 for row in compare_rows if row["importance"] == level)
            for level in ["high", "medium", "low", "none"]
        },
    }
    return compare_rows, diagnostics


def write_csv(path: Path, rows: List[Dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_markdown(rows: List[Dict[str, str]], diagnostics: Dict[str, object]) -> str:
    lines = [
        "# Fresh vs Brenton OT Comparison",
        "",
        f"Selected scope: {diagnostics['selected_scope']}",
        f"Selected verse rows: {diagnostics['selected_verse_rows']}",
        f"Selected drafted rows: {diagnostics['selected_drafted_rows']}",
        f"Minimum importance: {diagnostics['min_importance']}",
        f"Output compare rows: {diagnostics['output_compare_rows']}",
        "",
        f"Drafted rows compared: {diagnostics['drafted_rows_compared']}",
        f"Books with drafts: {', '.join(diagnostics['books_with_drafts']) if diagnostics['books_with_drafts'] else '[none]'}",
        f"Missing Brenton rows: {diagnostics['missing_brenton_rows']}",
        "",
        "Importance counts:",
        f"- high: {diagnostics['importance_counts']['high']}",
        f"- medium: {diagnostics['importance_counts']['medium']}",
        f"- low: {diagnostics['importance_counts']['low']}",
        f"- none: {diagnostics['importance_counts']['none']}",
        "",
        "Note:",
        "- Whole-OT compare pipeline ready.",
        "- Actual comparison breadth still limited by drafted fresh verses.",
        "",
    ]

    current_book = None
    for row in rows:
        if row["book_name"] != current_book:
            current_book = row["book_name"]
            lines.append(f"## {current_book}")
            lines.append("")
        lines.append(f"### {row['ref']}")
        lines.append("")
        lines.append(f"- importance: {row['importance']}")
        lines.append(f"- decisions: {row['decision_count']}")
        lines.append(f"- footnotes: {row['footnote_count']}")
        lines.append(f"- same_normalized: {row['same_normalized']}")
        lines.append(f"- fresh: {row['fresh_translation']}")
        lines.append(f"- brenton: {row['brenton_translation'] or '[missing]'}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--brenton-zip", default=str(DEFAULT_BRENTON_ZIP))
    parser.add_argument("--decisions", default=str(DEFAULT_DECISIONS))
    parser.add_argument("--footnotes", default=str(DEFAULT_FOOTNOTES))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--csv-output", default=str(DEFAULT_CSV))
    parser.add_argument("--diagnostics", default=str(DEFAULT_DIAGNOSTICS))
    parser.add_argument("--book")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--chapter-start", type=int)
    parser.add_argument("--chapter-end", type=int)
    parser.add_argument("--min-importance", choices=["none", "low", "medium", "high"], default="none")
    args = parser.parse_args()

    source_rows = load_csv_rows(Path(args.source))
    selected_rows = filter_rows_by_scope(
        source_rows,
        args.book,
        args.chapter,
        args.chapter_start,
        args.chapter_end,
    )
    if not selected_rows:
        raise ValueError("No source rows matched requested scope.")
    decision_rows = load_csv_rows(Path(args.decisions))
    footnote_rows = load_csv_rows(Path(args.footnotes))
    brenton_map: Dict[str, str] = {}
    with zipfile.ZipFile(args.brenton_zip) as zf:
        for book_code, filename in BOOK_FILENAME_MAP.items():
            if filename not in zf.namelist():
                continue
            book_rows = [row for row in selected_rows if row.get("book_code", "").strip() == book_code]
            if not book_rows:
                continue
            book_name = book_rows[0]["book_name"].strip()
            brenton_map.update(parse_brenton_book(zf, filename, book_name))

    compare_rows, diagnostics = build_rows(selected_rows, brenton_map, decision_rows, footnote_rows)
    compare_rows = [
        row
        for row in compare_rows
        if IMPORTANCE_ORDER[row["importance"]] >= IMPORTANCE_ORDER[args.min_importance]
    ]
    order_map = {row.get("ref", "").strip(): index for index, row in enumerate(selected_rows)}
    compare_rows.sort(key=lambda row: order_map.get(row["ref"], 10**9))
    diagnostics["selected_scope"] = describe_scope(selected_rows)
    diagnostics["selected_verse_rows"] = len(selected_rows)
    diagnostics["selected_drafted_rows"] = sum(1 for row in selected_rows if row.get("draft_translation", "").strip())
    diagnostics["min_importance"] = args.min_importance
    diagnostics["output_compare_rows"] = len(compare_rows)

    output_path = Path(args.output)
    csv_path = Path(args.csv_output)
    diagnostics_path = Path(args.diagnostics)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(build_markdown(compare_rows, diagnostics), encoding="utf-8")
    write_csv(csv_path, compare_rows)
    diagnostics_path.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False), encoding="utf-8")

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
