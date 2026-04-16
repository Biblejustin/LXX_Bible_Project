#!/usr/bin/env python3
import argparse
import csv
import json
import re
import xml.etree.ElementTree as ET
import zipfile
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = DATA / "raw"
LXX_GREEK = RAW / "lxx_greek"
OUTPUT = ROOT / "output"

DEFAULT_SOURCE = LXX_GREEK / "ot_full.csv"
DEFAULT_BRENTON_ZIP = RAW / "eng-Brenton_usfm.zip"
DEFAULT_MT_ZIP = RAW / "SF_2009-01-20_ENG_UKJV_(UPDATED KING JAMES VERSION).zip"
DEFAULT_PRIORITY = OUTPUT / "fresh_vs_brenton_ot_priority_review.csv"
DEFAULT_OUTPUT = OUTPUT / "fresh_vs_mt_brenton_ot_review.md"
DEFAULT_CSV = OUTPUT / "fresh_vs_mt_brenton_ot_review.csv"
DEFAULT_DIAGNOSTICS = OUTPUT / "fresh_vs_mt_brenton_ot_review_diagnostics.json"
DEFAULT_MT_MATCHES_MD = OUTPUT / "fresh_same_as_mt_differs_from_brenton.md"
DEFAULT_MT_MATCHES_CSV = OUTPUT / "fresh_same_as_mt_differs_from_brenton.csv"
DEFAULT_MT_LEANING_MD = OUTPUT / "fresh_mt_leaning_vs_brenton.md"
DEFAULT_MT_LEANING_CSV = OUTPUT / "fresh_mt_leaning_vs_brenton.csv"
DEFAULT_DIFFERS_BOTH_MD = OUTPUT / "fresh_differs_from_mt_and_brenton.md"
DEFAULT_DIFFERS_BOTH_CSV = OUTPUT / "fresh_differs_from_mt_and_brenton.csv"

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

OT_BOOK_ORDER = [
    "Genesis",
    "Exodus",
    "Leviticus",
    "Numbers",
    "Deuteronomy",
    "Joshua",
    "Judges",
    "Ruth",
    "1 Samuel",
    "2 Samuel",
    "1 Kings",
    "2 Kings",
    "1 Chronicles",
    "2 Chronicles",
    "Ezra",
    "Nehemiah",
    "Esther",
    "Job",
    "Psalms",
    "Proverbs",
    "Ecclesiastes",
    "Song of Solomon",
    "Isaiah",
    "Jeremiah",
    "Lamentations",
    "Ezekiel",
    "Daniel",
    "Hosea",
    "Joel",
    "Amos",
    "Obadiah",
    "Jonah",
    "Micah",
    "Nahum",
    "Habakkuk",
    "Zephaniah",
    "Haggai",
    "Zechariah",
    "Malachi",
]


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def matches_book(row: dict[str, str], book: str | None) -> bool:
    if not book:
        return True
    wanted = book.strip().lower()
    return (
        row.get("book_name", "").strip().lower() == wanted
        or row.get("book_code", "").strip().lower() == wanted
    )


def filter_rows_by_scope(
    rows: list[dict[str, str]],
    book: str | None,
    chapter: int | None,
    chapter_start: int | None,
    chapter_end: int | None,
) -> list[dict[str, str]]:
    filtered: list[dict[str, str]] = []
    for row in rows:
        if not matches_book(row, book):
            continue
        chapter_value = int(row.get("chapter", "").strip())
        if chapter is not None and chapter_value != chapter:
            continue
        if chapter_start is not None and chapter_value < chapter_start:
            continue
        if chapter_end is not None and chapter_value > chapter_end:
            continue
        filtered.append(row)
    return filtered


def describe_scope(rows: list[dict[str, str]]) -> str:
    if not rows:
        return "Unknown scope"
    ordered_books: list[str] = []
    for row in rows:
        book_name = row.get("book_name", "").strip()
        if book_name and book_name not in ordered_books:
            ordered_books.append(book_name)
    if len(ordered_books) > 1:
        return f"{ordered_books[0]}-{ordered_books[-1]} ({len(ordered_books)} books)"
    chapters = sorted({int(row["chapter"]) for row in rows})
    if chapters == list(range(chapters[0], chapters[-1] + 1)):
        return f"{ordered_books[0]} {chapters[0]}-{chapters[-1]}"
    return f"{ordered_books[0]} {', '.join(str(ch) for ch in chapters)}"


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_usfm_text(text: str) -> str:
    text = re.sub(r"\\f .*?\\f\*", "", text)
    text = re.sub(r"\\x .*?\\x\*", "", text)
    text = re.sub(r"\\add (.*?)\\add\*", r"\1", text)
    text = re.sub(r"\\sc (.*?)\\sc\*", r"\1", text)
    text = re.sub(r"\\[a-z0-9*]+\s*", "", text)
    return clean_text(text)


def parse_brenton_book(zf: zipfile.ZipFile, filename: str, book_name: str) -> dict[str, str]:
    text = zf.read(filename).decode("utf-8", errors="replace")
    current_chapter = None
    verses: dict[str, str] = {}
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
        verses[f"{book_name} {current_chapter}:{verse}"] = clean_usfm_text(match.group(2))
    return verses


def load_brenton_map(selected_rows: list[dict[str, str]], zip_path: Path) -> dict[str, str]:
    brenton_map: dict[str, str] = {}
    with zipfile.ZipFile(zip_path) as zf:
        for book_code, filename in BOOK_FILENAME_MAP.items():
            if filename not in zf.namelist():
                continue
            book_rows = [row for row in selected_rows if row.get("book_code", "").strip() == book_code]
            if not book_rows:
                continue
            brenton_map.update(parse_brenton_book(zf, filename, book_rows[0]["book_name"].strip()))
    return brenton_map


def load_mt_map(selected_rows: list[dict[str, str]], zip_path: Path) -> dict[str, str]:
    needed_books = {row["book_name"].strip() for row in selected_rows}
    with zipfile.ZipFile(zip_path) as zf:
        xml_name = zf.namelist()[0]
        root = ET.fromstring(zf.read(xml_name))
    mt_map: dict[str, str] = {}
    for book in root.findall("BIBLEBOOK"):
        bnumber = int(book.attrib["bnumber"])
        if bnumber < 1 or bnumber > len(OT_BOOK_ORDER):
            continue
        book_name = OT_BOOK_ORDER[bnumber - 1]
        if book_name not in needed_books:
            continue
        for chapter in book.findall("CHAPTER"):
            cnumber = int(chapter.attrib["cnumber"])
            for verse in chapter.findall("VERS"):
                vnumber = int(verse.attrib["vnumber"])
                text = clean_text("".join(verse.itertext()))
                mt_map[f"{book_name} {cnumber}:{vnumber}"] = text
    return mt_map


def normalize_for_compare(text: str) -> str:
    text = text.lower()
    text = text.replace("'", "")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def ratio(left: str, right: str) -> float:
    if not left or not right:
        return 0.0
    return SequenceMatcher(None, normalize_for_compare(left), normalize_for_compare(right)).ratio()


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(
                [
                    "ref",
                    "book_name",
                    "chapter",
                    "verse",
                    "priority_score",
                    "importance",
                    "category",
                    "fresh_translation",
                    "mt_translation",
                    "brenton_translation",
                    "fresh_mt_ratio",
                    "fresh_brenton_ratio",
                ]
            )
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_markdown(
    scope_label: str,
    all_rows: list[dict[str, str]],
    mt_same_rows: list[dict[str, str]],
    mt_leaning_rows: list[dict[str, str]],
    differs_rows: list[dict[str, str]],
    diagnostics: dict[str, object],
) -> str:
    lines = [
        "# Fresh vs MT vs Brenton Review",
        "",
        f"Scope: {scope_label}",
        f"Drafted rows checked: {diagnostics['drafted_rows_checked']}",
        f"Rows with MT witness: {diagnostics['rows_with_mt']}",
        f"Rows with Brenton witness: {diagnostics['rows_with_brenton']}",
        f"Rows same as MT, different from Brenton: {len(mt_same_rows)}",
        f"Rows MT-leaning vs Brenton: {len(mt_leaning_rows)}",
        f"Rows different from both: {len(differs_rows)}",
        "",
        "Method:",
        "- `same as MT` = normalized fresh English equals normalized UKJV verse.",
        "- `MT-leaning` = fresh closer to UKJV than Brenton by >= 0.10 ratio and fresh/MT ratio >= 0.75.",
        "- `different from both` = normalized fresh English differs from both UKJV and Brenton.",
        "- similarity ratios included for rough closeness only.",
        "",
        "## Same as MT, Differs from Brenton",
        "",
    ]
    if not mt_same_rows:
        lines.append("[none]")
        lines.append("")
    for row in mt_same_rows:
        lines.extend(
            [
                f"### {row['ref']}",
                f"- priority: `{row['priority_score']}`",
                f"- importance: `{row['importance']}`",
                f"- fresh: {row['fresh_translation']}",
                f"- mt: {row['mt_translation']}",
                f"- brenton: {row['brenton_translation']}",
                "",
            ]
        )
    lines.extend(
        [
            "## MT-Leaning vs Brenton",
            "",
        ]
    )
    if not mt_leaning_rows:
        lines.append("[none]")
        lines.append("")
    for row in mt_leaning_rows:
        lines.extend(
            [
                f"### {row['ref']}",
                f"- priority: `{row['priority_score']}`",
                f"- importance: `{row['importance']}`",
                f"- fresh_mt_ratio: `{row['fresh_mt_ratio']}`",
                f"- fresh_brenton_ratio: `{row['fresh_brenton_ratio']}`",
                f"- fresh: {row['fresh_translation']}",
                f"- mt: {row['mt_translation']}",
                f"- brenton: {row['brenton_translation']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Different from Both",
            "",
        ]
    )
    if not differs_rows:
        lines.append("[none]")
        lines.append("")
    for row in differs_rows:
        lines.extend(
            [
                f"### {row['ref']}",
                f"- priority: `{row['priority_score']}`",
                f"- importance: `{row['importance']}`",
                f"- fresh_mt_ratio: `{row['fresh_mt_ratio']}`",
                f"- fresh_brenton_ratio: `{row['fresh_brenton_ratio']}`",
                f"- fresh: {row['fresh_translation']}",
                f"- mt: {row['mt_translation']}",
                f"- brenton: {row['brenton_translation']}",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def build_filtered_markdown(title: str, rows: list[dict[str, str]]) -> str:
    lines = [f"# {title}", "", f"Rows: {len(rows)}", ""]
    for row in rows:
        lines.extend(
            [
                f"## {row['ref']}",
                f"- priority: `{row['priority_score']}`",
                f"- importance: `{row['importance']}`",
                f"- fresh_mt_ratio: `{row['fresh_mt_ratio']}`",
                f"- fresh_brenton_ratio: `{row['fresh_brenton_ratio']}`",
                f"- fresh: {row['fresh_translation']}",
                f"- mt: {row['mt_translation']}",
                f"- brenton: {row['brenton_translation']}",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--brenton-zip", default=str(DEFAULT_BRENTON_ZIP))
    parser.add_argument("--mt-zip", default=str(DEFAULT_MT_ZIP))
    parser.add_argument("--priority", default=str(DEFAULT_PRIORITY))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--csv-output", default=str(DEFAULT_CSV))
    parser.add_argument("--diagnostics", default=str(DEFAULT_DIAGNOSTICS))
    parser.add_argument("--mt-matches-output", default=str(DEFAULT_MT_MATCHES_MD))
    parser.add_argument("--mt-matches-csv", default=str(DEFAULT_MT_MATCHES_CSV))
    parser.add_argument("--mt-leaning-output", default=str(DEFAULT_MT_LEANING_MD))
    parser.add_argument("--mt-leaning-csv", default=str(DEFAULT_MT_LEANING_CSV))
    parser.add_argument("--differs-both-output", default=str(DEFAULT_DIFFERS_BOTH_MD))
    parser.add_argument("--differs-both-csv", default=str(DEFAULT_DIFFERS_BOTH_CSV))
    parser.add_argument("--book")
    parser.add_argument("--chapter", type=int)
    parser.add_argument("--chapter-start", type=int)
    parser.add_argument("--chapter-end", type=int)
    args = parser.parse_args()

    source_rows = load_csv_rows(Path(args.source))
    selected_rows = filter_rows_by_scope(
        source_rows,
        args.book,
        args.chapter,
        args.chapter_start,
        args.chapter_end,
    )
    selected_rows = [row for row in selected_rows if row.get("draft_translation", "").strip()]
    if not selected_rows:
        raise ValueError("No drafted rows matched requested scope.")

    priority_map = {row["ref"].strip(): row for row in load_csv_rows(Path(args.priority))}
    brenton_map = load_brenton_map(selected_rows, Path(args.brenton_zip))
    mt_map = load_mt_map(selected_rows, Path(args.mt_zip))

    rows: list[dict[str, str]] = []
    rows_with_mt = 0
    rows_with_brenton = 0
    for row in selected_rows:
        ref = row["ref"].strip()
        fresh = row["draft_translation"].strip()
        mt = mt_map.get(ref, "").strip()
        brenton = brenton_map.get(ref, "").strip()
        if mt:
            rows_with_mt += 1
        if brenton:
            rows_with_brenton += 1
        fresh_norm = normalize_for_compare(fresh)
        mt_norm = normalize_for_compare(mt)
        brenton_norm = normalize_for_compare(brenton)
        same_mt = bool(mt) and fresh_norm == mt_norm
        same_brenton = bool(brenton) and fresh_norm == brenton_norm
        if same_mt and not same_brenton and brenton:
            category = "same_as_mt_differs_from_brenton"
        elif mt and brenton and not same_mt and not same_brenton:
            category = "different_from_both"
        elif same_mt and same_brenton:
            category = "same_as_both"
        elif same_brenton and not same_mt and mt:
            category = "same_as_brenton_differs_from_mt"
        elif mt and not brenton:
            category = "missing_brenton"
        elif brenton and not mt:
            category = "missing_mt"
        else:
            category = "other"
        priority = priority_map.get(ref, {})
        rows.append(
            {
                "ref": ref,
                "book_name": row["book_name"].strip(),
                "chapter": row["chapter"].strip(),
                "verse": row["verse"].strip(),
                "priority_score": priority.get("priority_score", "0"),
                "importance": priority.get("importance", "none"),
                "category": category,
                "fresh_translation": fresh,
                "mt_translation": mt,
                "brenton_translation": brenton,
                "fresh_mt_ratio": f"{ratio(fresh, mt):.3f}",
                "fresh_brenton_ratio": f"{ratio(fresh, brenton):.3f}",
            }
        )

    mt_same_rows = [row for row in rows if row["category"] == "same_as_mt_differs_from_brenton"]
    mt_leaning_rows = [
        row
        for row in rows
        if row["mt_translation"]
        and row["brenton_translation"]
        and float(row["fresh_mt_ratio"]) >= float(row["fresh_brenton_ratio"]) + 0.10
        and float(row["fresh_mt_ratio"]) >= 0.75
    ]
    differs_rows = [row for row in rows if row["category"] == "different_from_both"]
    all_review_rows = mt_same_rows + differs_rows

    mt_same_rows.sort(key=lambda row: (-int(row["priority_score"] or 0), row["ref"]))
    mt_leaning_rows.sort(
        key=lambda row: (
            -int(row["priority_score"] or 0),
            -(float(row["fresh_mt_ratio"]) - float(row["fresh_brenton_ratio"])),
            row["ref"],
        )
    )
    differs_rows.sort(
        key=lambda row: (
            -int(row["priority_score"] or 0),
            float(row["fresh_mt_ratio"]),
            float(row["fresh_brenton_ratio"]),
            row["ref"],
        )
    )
    all_review_rows.sort(key=lambda row: (-int(row["priority_score"] or 0), row["ref"]))

    diagnostics = {
        "scope": describe_scope(selected_rows),
        "drafted_rows_checked": len(selected_rows),
        "rows_with_mt": rows_with_mt,
        "rows_with_brenton": rows_with_brenton,
        "category_counts": {
            label: sum(1 for row in rows if row["category"] == label)
            for label in [
                "same_as_mt_differs_from_brenton",
                "different_from_both",
                "same_as_both",
                "same_as_brenton_differs_from_mt",
                "missing_mt",
                "missing_brenton",
                "other",
            ]
        },
        "mt_leaning_count": len(mt_leaning_rows),
    }

    output_path = Path(args.output)
    csv_path = Path(args.csv_output)
    diagnostics_path = Path(args.diagnostics)
    mt_matches_md = Path(args.mt_matches_output)
    mt_matches_csv = Path(args.mt_matches_csv)
    mt_leaning_md = Path(args.mt_leaning_output)
    mt_leaning_csv = Path(args.mt_leaning_csv)
    differs_both_md = Path(args.differs_both_output)
    differs_both_csv = Path(args.differs_both_csv)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        build_markdown(diagnostics["scope"], all_review_rows, mt_same_rows, mt_leaning_rows, differs_rows, diagnostics),
        encoding="utf-8",
    )
    write_csv(csv_path, all_review_rows)
    mt_matches_md.write_text(
        build_filtered_markdown("Fresh Same as MT, Differs from Brenton", mt_same_rows),
        encoding="utf-8",
    )
    write_csv(mt_matches_csv, mt_same_rows)
    mt_leaning_md.write_text(
        build_filtered_markdown("Fresh MT-Leaning vs Brenton", mt_leaning_rows),
        encoding="utf-8",
    )
    write_csv(mt_leaning_csv, mt_leaning_rows)
    differs_both_md.write_text(
        build_filtered_markdown("Fresh Differs from MT and Brenton", differs_rows),
        encoding="utf-8",
    )
    write_csv(differs_both_csv, differs_rows)
    diagnostics_path.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False), encoding="utf-8")

    print(
        json.dumps(
            {
                "output": str(output_path),
                "csv_output": str(csv_path),
                "diagnostics": str(diagnostics_path),
                "mt_matches_output": str(mt_matches_md),
                "mt_matches_csv": str(mt_matches_csv),
                "mt_leaning_output": str(mt_leaning_md),
                "mt_leaning_csv": str(mt_leaning_csv),
                "differs_both_output": str(differs_both_md),
                "differs_both_csv": str(differs_both_csv),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
