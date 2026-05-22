"""Build a review queue for Greek-heavy lines in Charles 1912 1 Enoch OCR."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "1_enoch_charles_1912_djvu.txt"
AUDIT_OUTPUT = ROOT / "data" / "research" / "1_enoch_charles_1912_greek_ocr_audit.csv"
PROGRESS_OUTPUT = ROOT / "output" / "enoch" / "1_enoch_greek_fragment_audit.md"
DIAGNOSTICS_OUTPUT = ROOT / "output" / "enoch" / "1_enoch_greek_fragment_audit_diagnostics.json"

GREEK_RE = re.compile(r"[\u0370-\u03ff\u1f00-\u1fff]")
CHAPTER_VERSE_RE = re.compile(r"^\s*([IVXLCDM]+)\.\s*(?:(\d+)[,.]?\s*)?")
ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

FIELDNAMES = [
    "source_file",
    "line_number",
    "section_hint",
    "ref_hint",
    "greek_char_count",
    "raw_line",
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


def section_boundaries(lines: list[str]) -> dict[str, int]:
    boundaries: dict[str, int] = {}
    for idx, line in enumerate(lines, 1):
        if "TRANSLATION AND" in line and "NOTES" in line.upper() and "translation_notes" not in boundaries:
            boundaries["translation_notes"] = idx
        if "(CHAPTERS I" in line and "translation_text" not in boundaries:
            boundaries["translation_text"] = idx
    return boundaries


def section_hint(line_number: int, boundaries: dict[str, int]) -> str:
    translation_notes = boundaries.get("translation_notes", 0)
    translation_text = boundaries.get("translation_text", 0)
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

    for line_number, line in enumerate(lines, 1):
        stripped = line.strip()
        match = CHAPTER_VERSE_RE.match(stripped)
        if match:
            chapter = roman_to_int(match.group(1))
            verse = match.group(2)
            if chapter:
                current_ref = f"1 Enoch {chapter}:{verse}" if verse else f"1 Enoch {chapter}"

        greek_count = len(GREEK_RE.findall(line))
        if greek_count < 8:
            continue

        section = section_hint(line_number, boundaries)
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
        "greek_char_threshold": 8,
        "section_boundaries": boundaries,
        "source_status": "Public-domain OCR candidate; not source-grade Greek rows until checked against page images/PDF.",
        "first_line_number": int(rows[0]["line_number"]) if rows else None,
        "last_line_number": int(rows[-1]["line_number"]) if rows else None,
    }
    return rows, diagnostics


def write_csv(rows: list[dict[str, str]]) -> None:
    AUDIT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


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
        f"- Greek-character threshold: {diagnostics['greek_char_threshold']}",
        "",
        "## First Audit Rows",
        "",
    ]
    for row in rows[:12]:
        lines.append(f"- line {row['line_number']} ({row['section_hint']}): {row['raw_line']}")
    PROGRESS_OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_diagnostics(diagnostics: dict[str, object]) -> None:
    DIAGNOSTICS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with DIAGNOSTICS_OUTPUT.open("w", encoding="utf-8") as handle:
        json.dump(diagnostics, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def main() -> int:
    rows, diagnostics = build_rows()
    write_csv(rows)
    write_progress(rows, diagnostics)
    write_diagnostics(diagnostics)
    print({"rows": diagnostics["rows"], "output": str(AUDIT_OUTPUT.relative_to(ROOT))})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
