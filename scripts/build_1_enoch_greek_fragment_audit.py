"""Build a review queue for Greek-heavy lines in Charles 1912 1 Enoch OCR."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "1_enoch_charles_1912_djvu.txt"
WITNESS_CSV = ROOT / "data" / "raw" / "1_enoch" / "1_enoch_charles_witness.csv"
AUDIT_OUTPUT = ROOT / "data" / "research" / "1_enoch_charles_1912_greek_ocr_audit.csv"
PRIORITY_OUTPUT = ROOT / "data" / "research" / "1_enoch_charles_1912_greek_ocr_priority.csv"
REF_REVIEW_OUTPUT = ROOT / "data" / "research" / "1_enoch_greek_fragment_ref_review.csv"
PROGRESS_OUTPUT = ROOT / "output" / "enoch" / "1_enoch_greek_fragment_audit.md"
DIAGNOSTICS_OUTPUT = ROOT / "output" / "enoch" / "1_enoch_greek_fragment_audit_diagnostics.json"

GREEK_RE = re.compile(r"[\u0370-\u03ff\u1f00-\u1fff]")
CHAPTER_VERSE_RE = re.compile(r"^\s*([IVXLCDM]+)\.\s*(?:(\d+)[,.]?\s*)?")
GREEK_FRAGMENT_VERSE_RE = re.compile(r"^\s*[|\[({<]*\s*(\d{1,3})\.\s+")
PRINTED_PAGE_RE = re.compile(r"^\s*(\d{1,3})\s+The Book of Enoch")
CHAPTER_PAGE_RE = re.compile(r"^\s*(Chapter|Chapters)\s+.+?\s+(\d{1,3})\s*$")
ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

FIELDNAMES = [
    "source_file",
    "line_number",
    "printed_page_hint",
    "heading_hint",
    "section_hint",
    "ref_hint",
    "greek_char_count",
    "raw_line",
    "next_review",
]
REF_REVIEW_FIELDNAMES = [
    "ref_hint",
    "priority_line_count",
    "first_line_number",
    "last_line_number",
    "printed_page_hints",
    "greek_ocr_excerpt",
    "charles_witness_refs",
    "charles_witness_excerpt",
    "charles_comparison_notes",
    "next_review",
]


def roman_to_int(text: str) -> int | None:
    total = 0
    previous = 0
    for char in reversed(text):
        value = ROMAN_VALUES.get(char)
        if value is None:
            return None
        if value < previous:
            total -= value
        else:
            total += value
            previous = value
    return total if 1 <= total <= 108 else None


def source_sha256() -> str:
    return hashlib.sha256(SOURCE.read_bytes()).hexdigest()


def truncate(text: str, limit: int) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def ref_chapter(ref: str) -> str:
    match = re.match(r"^1 Enoch (\d+)", ref)
    return match.group(1) if match else ""


def load_charles_witness_rows() -> tuple[dict[str, dict[str, str]], dict[str, list[dict[str, str]]]]:
    by_ref: dict[str, dict[str, str]] = {}
    by_chapter: dict[str, list[dict[str, str]]] = {}
    if not WITNESS_CSV.exists():
        return by_ref, by_chapter
    with WITNESS_CSV.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            by_ref[row["ref"]] = row
            by_chapter.setdefault(row["chapter"], []).append(row)
    return by_ref, by_chapter


def section_boundaries(lines: list[str]) -> dict[str, int]:
    boundaries: dict[str, int] = {}
    for idx, line in enumerate(lines, 1):
        if "TRANSLATION AND" in line and "NOTES" in line.upper() and "translation_notes" not in boundaries:
            boundaries["translation_notes"] = idx
        if "(CHAPTERS I" in line and "translation_text" not in boundaries:
            boundaries["translation_text"] = idx
        if "Λόγος εὐλογίας" in line and "Ενώχ" in line and "greek_fragment_text" not in boundaries:
            boundaries["greek_fragment_text"] = idx
    return boundaries


def section_hint(line_number: int, boundaries: dict[str, int]) -> str:
    greek_fragment_text = boundaries.get("greek_fragment_text", 0)
    translation_notes = boundaries.get("translation_notes", 0)
    translation_text = boundaries.get("translation_text", 0)
    if greek_fragment_text and line_number >= greek_fragment_text:
        return "greek fragment text"
    if translation_text and line_number >= translation_text:
        return "translation and notes"
    if translation_notes and line_number >= translation_notes:
        return "critical introduction"
    return "front matter and source discussion"


def build_rows() -> tuple[list[dict[str, str]], dict[str, object]]:
    lines = SOURCE.read_text(encoding="utf-8", errors="ignore").splitlines()
    boundaries = section_boundaries(lines)
    rows: list[dict[str, str]] = []
    current_ref = ""
    current_chapter = ""
    current_printed_page = ""
    current_heading = ""

    for line_number, line in enumerate(lines, 1):
        stripped = line.strip()
        section = section_hint(line_number, boundaries)
        page_match = PRINTED_PAGE_RE.match(stripped)
        chapter_page_match = CHAPTER_PAGE_RE.match(stripped)
        if page_match:
            current_printed_page = page_match.group(1)
            current_heading = stripped
        elif chapter_page_match:
            current_printed_page = chapter_page_match.group(2)
            current_heading = stripped

        match = CHAPTER_VERSE_RE.match(stripped)
        if match:
            chapter = roman_to_int(match.group(1))
            verse = match.group(2)
            if chapter:
                current_chapter = str(chapter)
                current_ref = f"1 Enoch {chapter}:{verse}" if verse else f"1 Enoch {chapter}"
        elif section == "greek fragment text" and current_chapter:
            verse_match = GREEK_FRAGMENT_VERSE_RE.match(stripped)
            if verse_match:
                current_ref = f"1 Enoch {current_chapter}:{int(verse_match.group(1))}"

        greek_count = len(GREEK_RE.findall(line))
        if greek_count < 8:
            continue

        if section == "translation and notes":
            review = "Verify against page image/PDF before using as Greek-fragment or variant evidence."
        else:
            review = "Source-status or reception note; do not import as verse text without checking context."
        if greek_count >= 40:
            review = "High-density Greek OCR line; verify against page image/PDF before source-row import."

        rows.append(
            {
                "source_file": str(SOURCE.relative_to(ROOT)),
                "line_number": str(line_number),
                "printed_page_hint": current_printed_page,
                "heading_hint": current_heading,
                "section_hint": section,
                "ref_hint": current_ref,
                "greek_char_count": str(greek_count),
                "raw_line": " ".join(stripped.split()),
                "next_review": review,
            }
        )

    diagnostics = {
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": source_sha256(),
        "line_count": len(lines),
        "rows": len(rows),
        "priority_rows": sum(1 for row in rows if is_priority_row(row)),
        "greek_char_threshold": 8,
        "priority_rule": "Greek fragment text section with at least 40 Greek Unicode characters",
        "section_boundaries": boundaries,
        "source_status": "Public-domain OCR candidate; not source-grade Greek rows until checked against page images/PDF.",
        "first_line_number": int(rows[0]["line_number"]) if rows else None,
        "last_line_number": int(rows[-1]["line_number"]) if rows else None,
    }
    return rows, diagnostics


def is_priority_row(row: dict[str, str]) -> bool:
    return row["section_hint"] == "greek fragment text" and int(row["greek_char_count"]) >= 40


def grouped_ref_review_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_ref, by_chapter = load_charles_witness_rows()
    priority_rows = [row for row in rows if is_priority_row(row)]
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in priority_rows:
        grouped.setdefault(row["ref_hint"] or "unmapped", []).append(row)

    review_rows: list[dict[str, str]] = []
    for ref_hint in sorted(grouped, key=lambda ref: [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", ref)]):
        ref_rows = grouped[ref_hint]
        pages = sorted({row["printed_page_hint"] for row in ref_rows if row["printed_page_hint"]}, key=lambda value: int(value))
        exact_witness = by_ref.get(ref_hint)
        chapter_rows = by_chapter.get(ref_chapter(ref_hint), [])
        if exact_witness:
            witness_refs = exact_witness["ref"]
            witness_excerpt = exact_witness["draft_translation"]
            witness_notes = exact_witness["comparison_notes"]
        elif chapter_rows:
            witness_refs = f"{chapter_rows[0]['ref']}-{chapter_rows[-1]['ref'].split()[-1]}"
            witness_excerpt = " ".join(row["draft_translation"] for row in chapter_rows[:3])
            witness_notes = "; ".join(row["comparison_notes"] for row in chapter_rows[:3] if row["comparison_notes"])
        else:
            witness_refs = ""
            witness_excerpt = ""
            witness_notes = ""
        review_rows.append(
            {
                "ref_hint": ref_hint,
                "priority_line_count": str(len(ref_rows)),
                "first_line_number": ref_rows[0]["line_number"],
                "last_line_number": ref_rows[-1]["line_number"],
                "printed_page_hints": "; ".join(pages),
                "greek_ocr_excerpt": " / ".join(truncate(row["raw_line"], 160) for row in ref_rows[:4]),
                "charles_witness_refs": witness_refs,
                "charles_witness_excerpt": truncate(witness_excerpt, 500),
                "charles_comparison_notes": truncate(witness_notes, 500),
                "next_review": "Verify Greek OCR against page image, then compare with Charles Ethiopic-base witness before drafting.",
            }
        )
    return review_rows


def write_csv(rows: list[dict[str, str]]) -> int:
    AUDIT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    with PRIORITY_OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(row for row in rows if is_priority_row(row))
    ref_review_rows = grouped_ref_review_rows(rows)
    with REF_REVIEW_OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REF_REVIEW_FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(ref_review_rows)
    return len(ref_review_rows)


def write_progress(rows: list[dict[str, str]], diagnostics: dict[str, object]) -> None:
    PROGRESS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 1 Enoch Greek Fragment OCR Audit",
        "",
        "This audit scans the public-domain Charles 1912 OCR for Greek-heavy lines.",
        "It is a review queue only. OCR lines are not source-grade Greek rows until checked against page images or a cleaner transcription.",
        "",
        "## Counts",
        "",
        f"- Source: {diagnostics['source']}",
        f"- Source SHA-256: {diagnostics['source_sha256']}",
        f"- Source lines: {diagnostics['line_count']}",
        f"- Audit rows: {diagnostics['rows']}",
        f"- Priority rows: {diagnostics['priority_rows']}",
        f"- Reference review rows: {diagnostics['ref_review_rows']}",
        f"- Greek-character threshold: {diagnostics['greek_char_threshold']}",
        f"- Priority rule: {diagnostics['priority_rule']}",
        "",
        "## First Audit Rows",
        "",
    ]
    for row in rows[:12]:
        lines.append(f"- line {row['line_number']} ({row['section_hint']}): {row['raw_line']}")
    priority_rows = [row for row in rows if is_priority_row(row)]
    lines.extend(["", "## First Priority Rows", ""])
    for row in priority_rows[:12]:
        lines.append(f"- line {row['line_number']} ({row['ref_hint'] or 'unmapped'}): {row['raw_line']}")
    PROGRESS_OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_diagnostics(diagnostics: dict[str, object]) -> None:
    DIAGNOSTICS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with DIAGNOSTICS_OUTPUT.open("w", encoding="utf-8") as handle:
        json.dump(diagnostics, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def main() -> int:
    rows, diagnostics = build_rows()
    diagnostics["ref_review_rows"] = write_csv(rows)
    write_progress(rows, diagnostics)
    write_diagnostics(diagnostics)
    print(
        {
            "rows": diagnostics["rows"],
            "priority_rows": diagnostics["priority_rows"],
            "output": str(AUDIT_OUTPUT.relative_to(ROOT)),
            "priority_output": str(PRIORITY_OUTPUT.relative_to(ROOT)),
            "ref_review_output": str(REF_REVIEW_OUTPUT.relative_to(ROOT)),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
