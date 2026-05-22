"""Build a separate 1 Enoch witness workspace from the Charles 1917 text."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "1_enoch_charles_1917.txt"
OUTPUT_DIR = ROOT / "data" / "raw" / "1_enoch"
CSV_OUTPUT = OUTPUT_DIR / "1_enoch_charles_witness.csv"
MANIFEST_OUTPUT = OUTPUT_DIR / "source_manifest.json"
QUEUE_OUTPUT = ROOT / "data" / "research" / "1_enoch_witness_comparison_queue.csv"
PROGRESS_OUTPUT = ROOT / "output" / "enoch" / "1_enoch_witness_progress.md"
DIAGNOSTICS_OUTPUT = ROOT / "output" / "enoch" / "1_enoch_witness_diagnostics.json"

FIELDNAMES = [
    "ref",
    "book_code",
    "book_name",
    "chapter",
    "verse",
    "base_witness",
    "source_language",
    "source_scope",
    "charles_text_raw",
    "draft_translation",
    "greek_absent_in_ethiopic",
    "ethiopic_absent_in_greek",
    "restored_text",
    "interpolations",
    "supplied_text",
    "emended_text",
    "corrupt_text",
    "comparison_notes",
]
MARKER_FIELDS = [
    "greek_absent_in_ethiopic",
    "ethiopic_absent_in_greek",
    "restored_text",
    "interpolations",
    "supplied_text",
    "emended_text",
    "corrupt_text",
]
QUEUE_FIELDNAMES = [
    "ref",
    "marker_types",
    "draft_translation",
    "comparison_notes",
    *MARKER_FIELDS,
    "next_review",
]

OCP_WITNESS_INVENTORY = {
    "ethiopic": [
        {
            "siglum": "p",
            "name": "Rylands Manuscript 23",
            "scope": "Book of Watchers and Parables in the current OCP transcription",
            "date": "17th or 18th century AD",
        }
    ],
    "greek": [
        {"siglum": "7QEnoch", "name": "7QpapEn gr (7Q4, 8, 11-14)", "scope": "fragmentary"},
        {"siglum": "POxy2069", "name": "Oxyrhynchus Papyrus 2069", "scope": "fragmentary"},
        {"siglum": "CB185", "name": "Chester Beatty 185", "scope": "last chapters in Greek"},
        {"siglum": "V1809", "name": "Vatican Greek 1809 fragment", "scope": "fragmentary"},
        {"siglum": "Gizeh", "name": "Cairo Papyrus 10759 / Codex Panopolitanus", "scope": "Akhmim Greek fragments"},
        {"siglum": "Gizeh2", "name": "Duplicate section of Cairo Papyrus 10759", "scope": "Akhmim duplicate"},
        {"siglum": "Syncellus", "name": "George Syncellus, Chronographia", "scope": "quoted Greek fragments"},
        {"siglum": "Jude", "name": "Jude 14-15", "scope": "New Testament citation"},
    ],
    "aramaic": [
        {"siglum": "4Q201", "name": "4QEnoch a ar"},
        {"siglum": "4Q202", "name": "4QEnoch b ar"},
        {"siglum": "4Q204", "name": "4QEnoch c ar"},
        {"siglum": "4Q205", "name": "4QEnoch d ar"},
        {"siglum": "4Q206", "name": "4QEnoch e ar"},
        {"siglum": "4Q207", "name": "4QEnoch f ar"},
        {"siglum": "4Q208", "name": "4QEnastr a ar"},
        {"siglum": "4Q209", "name": "4QEnastr b ar"},
        {"siglum": "4Q210", "name": "4QEnastr c ar"},
        {"siglum": "4Q211", "name": "4QEnastr d ar"},
        {"siglum": "4Q212", "name": "4QEnoch g ar"},
        {"siglum": "4Q247", "name": "4QApocalypse of Weeks?"},
    ],
}

ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
CHAPTER_START = re.compile(r"^\s*\[?([IVXLCDM]+)\.\s+\[?(?:(\d+)\.\s+)?(.+?)\s*$")
CHAPTER_HEADING = re.compile(r"^\s*([IVXLCDM]+)\.\s+[_=].*")


@dataclass
class ChapterStart:
    line_index: int
    roman: str
    chapter: int
    first_verse: int
    first_text: str


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def roman_to_int(text: str) -> int:
    total = 0
    previous = 0
    for char in reversed(text):
        value = ROMAN_VALUES[char]
        if value < previous:
            total -= value
        else:
            total += value
            previous = value
    return total


def source_sha256() -> str:
    return hashlib.sha256(SOURCE.read_bytes()).hexdigest()


def is_true_chapter_start(line: str) -> ChapterStart | None:
    match = CHAPTER_START.match(line)
    if not match:
        return None
    roman, first_verse_text, remainder = match.groups()
    chapter = roman_to_int(roman)
    if not (1 <= chapter <= 108):
        return None
    remainder = remainder.strip()
    if first_verse_text:
        if re.match(r"\d+\s*[-–]", remainder):
            return None
        return ChapterStart(-1, roman, chapter, int(first_verse_text), remainder)
    if re.match(r"[IVXLCDM]+\.", remainder):
        return None
    if re.match(r"\d+\s*[-–]", remainder):
        return None
    if "_" in remainder or "=" in remainder:
        return None
    if remainder.upper() == remainder and len(remainder) > 12:
        return None
    if not re.match(r"[A-Z‘'\"(]", remainder):
        return None
    return ChapterStart(-1, roman, chapter, 1, remainder)


def is_heading_chapter_start(line: str) -> ChapterStart | None:
    match = CHAPTER_HEADING.match(line)
    if not match:
        return None
    roman = match.group(1)
    chapter = roman_to_int(roman)
    if not (1 <= chapter <= 108):
        return None
    return ChapterStart(-1, roman, chapter, 1, "")


def is_section_heading_start(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if re.match(r"^[IVXLCDM]+(?:[-–][IVXLCDM]+)?\.\s", stripped) and ("_" in stripped or "=" in stripped):
        return True
    if re.match(r"^[IVXLCDM]+\.\s+[IVXLCDM]+\.\s", stripped):
        return True
    if re.match(r"^[IVXLCDM]+(?:[-–][IVXLCDM]+)?\.\s+\d+\s*[-–]\d+\.\s", stripped):
        return True
    return False


def clean_source_markup(text: str) -> str:
    text = re.sub(r"\b\d+_[a-z]\._\s*", "", text)
    text = re.sub(r"\s+_[a-z]\._\s*", " ", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)
    text = re.sub(r"=([^=]+)=", r"\1", text)
    text = text.translate(str.maketrans({"⌜": "", "⌝": "", "⌞": "", "⌟": "", "〚": "", "〛": ""}))
    text = text.replace("‹", "").replace("›", "")
    text = text.replace("†", "")
    text = text.replace("[", "").replace("]", "")
    return normalize_space(text)


def capture(pattern: str, text: str) -> list[str]:
    return [normalize_space(item) for item in re.findall(pattern, text, flags=re.DOTALL) if normalize_space(item)]


def marker_notes(raw_text: str) -> tuple[dict[str, str], str]:
    fields = {
        "greek_absent_in_ethiopic": "; ".join(capture(r"⌜(.*?)⌝", raw_text)),
        "ethiopic_absent_in_greek": "; ".join(capture(r"〚(.*?)〛", raw_text)),
        "restored_text": "; ".join(capture(r"‹(.*?)›", raw_text)),
        "interpolations": "; ".join(capture(r"\[(.*?)\]", raw_text)),
        "supplied_text": "; ".join(capture(r"\((.*?)\)", raw_text)),
        "emended_text": "; ".join(capture(r"=(.*?)=", raw_text)),
        "corrupt_text": "; ".join(capture(r"†(.*?)†", raw_text)),
    }
    notes: list[str] = []
    if fields["greek_absent_in_ethiopic"]:
        notes.append(f"G^g has text absent from Ethiopic: {fields['greek_absent_in_ethiopic']}")
    if fields["ethiopic_absent_in_greek"]:
        notes.append(f"Ethiopic has text absent from G^g/G^s: {fields['ethiopic_absent_in_greek']}")
    if fields["restored_text"]:
        notes.append(f"Charles restored text: {fields['restored_text']}")
    if fields["interpolations"]:
        notes.append(f"Charles marks interpolation: {fields['interpolations']}")
    if fields["supplied_text"]:
        notes.append(f"Charles supplied text: {fields['supplied_text']}")
    if fields["emended_text"]:
        notes.append(f"Charles emended text: {fields['emended_text']}")
    if fields["corrupt_text"]:
        notes.append(f"Charles marks corrupt text: {fields['corrupt_text']}")
    return fields, "; ".join(notes)


def true_chapter_starts(lines: list[str]) -> list[ChapterStart]:
    starts: list[ChapterStart] = []
    for index, line in enumerate(lines):
        start = is_true_chapter_start(line)
        if start:
            start.line_index = index
            starts.append(start)
    seen_chapters = {start.chapter for start in starts}
    for index, line in enumerate(lines):
        start = is_heading_chapter_start(line)
        if start and start.chapter not in seen_chapters:
            start.line_index = index
            starts.append(start)
            seen_chapters.add(start.chapter)
    return sorted(starts, key=lambda item: item.line_index)


def iter_chapter_blocks(lines: list[str], starts: list[ChapterStart]) -> Iterable[tuple[ChapterStart, list[str]]]:
    for idx, start in enumerate(starts):
        next_index = starts[idx + 1].line_index if idx + 1 < len(starts) else len(lines)
        block_lines = [f"{start.first_verse}. {start.first_text}"] if start.first_text else []
        skipping_heading = False
        for line in lines[start.line_index + 1 : next_index]:
            stripped = line.strip()
            if not stripped:
                skipping_heading = False
                continue
            if is_section_heading_start(stripped):
                skipping_heading = True
                continue
            if skipping_heading:
                if re.match(r"^\d+(?:_[a-z]\._)?\.\s+", stripped):
                    skipping_heading = False
                else:
                    continue
            block_lines.append(stripped)
        yield start, block_lines


def split_verses(block_lines: list[str]) -> list[tuple[int, str]]:
    text = "\n".join(block_lines)
    text = re.sub(r"\n+", " ", text)
    verse_pattern = re.compile(r"(?<![\w^])(\d+)(?:_[a-z]\._)?\.\s+")
    matches = list(verse_pattern.finditer(text))
    by_verse: dict[int, list[str]] = {}
    order: list[int] = []
    for idx, match in enumerate(matches):
        verse = int(match.group(1))
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        raw_segment = normalize_space(text[start:end])
        if not raw_segment:
            continue
        if verse not in by_verse:
            by_verse[verse] = []
            order.append(verse)
        by_verse[verse].append(raw_segment)
    return [(verse, normalize_space(" ".join(by_verse[verse]))) for verse in order]


def build_rows() -> tuple[list[dict[str, str]], dict[str, object]]:
    raw = SOURCE.read_text(encoding="utf-8", errors="ignore")
    lines = raw.splitlines()
    starts = true_chapter_starts(lines)
    if not starts:
        raise RuntimeError("No 1 Enoch chapter starts found")

    rows: list[dict[str, str]] = []
    marker_counts: Counter[str] = Counter()
    chapter_counts: Counter[int] = Counter()
    for chapter_start, block_lines in iter_chapter_blocks(lines, starts):
        for verse, raw_verse_text in split_verses(block_lines):
            fields, note = marker_notes(raw_verse_text)
            for key, value in fields.items():
                if value:
                    marker_counts[key] += 1
            chapter_counts[chapter_start.chapter] += 1
            ref = f"1 Enoch {chapter_start.chapter}:{verse}"
            rows.append(
                {
                    "ref": ref,
                    "book_code": "ENO",
                    "book_name": "1 Enoch",
                    "chapter": str(chapter_start.chapter),
                    "verse": str(verse),
                    "base_witness": "R. H. Charles 1917 English translation",
                    "source_language": "English from Ethiopic, with Charles Greek/Syriac/Latin/Aramaic comparison markers",
                    "source_scope": "Separate witness workspace; not Greek deuterocanon source rows",
                    "charles_text_raw": normalize_space(raw_verse_text),
                    "draft_translation": clean_source_markup(raw_verse_text),
                    **fields,
                    "comparison_notes": note,
                }
            )

    diagnostics = {
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": source_sha256(),
        "rows": len(rows),
        "chapters": sorted(chapter_counts),
        "chapter_count": len(chapter_counts),
        "first_ref": rows[0]["ref"] if rows else "",
        "last_ref": rows[-1]["ref"] if rows else "",
        "marker_counts": dict(sorted(marker_counts.items())),
        "missing_chapters": [chapter for chapter in range(1, 109) if chapter not in chapter_counts],
        "source_status": "full Ethiopic-base English witness; extant Greek/Latin evidence partial; Aramaic fragments partial",
    }
    return rows, diagnostics


def comparison_queue_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    queue: list[dict[str, str]] = []
    for row in rows:
        marker_types = [field for field in MARKER_FIELDS if row[field]]
        if not marker_types:
            continue
        if "greek_absent_in_ethiopic" in marker_types or "ethiopic_absent_in_greek" in marker_types:
            next_review = "Compare extant Greek witness with Ethiopic-base Charles text."
        elif {"restored_text", "interpolations", "emended_text", "corrupt_text"} & set(marker_types):
            next_review = "Review Charles editorial marker before using this wording in an appendix."
        else:
            next_review = "Review supplied wording against Ethiopic base and any extant witnesses."
        queue.append(
            {
                "ref": row["ref"],
                "marker_types": "; ".join(marker_types),
                "draft_translation": row["draft_translation"],
                "comparison_notes": row["comparison_notes"],
                **{field: row[field] for field in MARKER_FIELDS},
                "next_review": next_review,
            }
        )
    return queue


def write_csv(rows: list[dict[str, str]]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_queue(rows: list[dict[str, str]]) -> int:
    queue = comparison_queue_rows(rows)
    QUEUE_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with QUEUE_OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=QUEUE_FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(queue)
    return len(queue)


def write_manifest(diagnostics: dict[str, object]) -> None:
    manifest = {
        "workspace": "1 Enoch witness workspace",
        "role": "separate witness/comparison workspace; not imported into deuterocanon or main Bible rows",
        "source_file": str(SOURCE.relative_to(ROOT)),
        "source_sha256": diagnostics["source_sha256"],
        "primary_source": {
            "name": "R. H. Charles, The Book of Enoch (1917)",
            "url": "https://www.gutenberg.org/cache/epub/77935/pg77935.txt",
            "catalog_url": "https://www.gutenberg.org/ebooks/77935",
            "license_status": "Public domain in the United States",
        },
        "comparison_source_pointer": {
            "name": "Online Critical Pseudepigrapha, 1 Enoch",
            "index_url": "https://pseudepigrapha.org/default/index",
            "intro_url": "https://pseudepigrapha.org/docs/intro/1En",
            "status_note": (
                "OCP represents extant Greek and Latin evidence, Aramaic fragments through chapter 8, "
                "and one Ethiopic manuscript for the Book of Watchers and Parables. Use rights vary by witness."
            ),
        },
        "candidate_public_domain_sources": [
            {
                "name": "R. H. Charles, The Book of Enoch or 1 Enoch (Oxford, 1912)",
                "local_file": "data/raw/1_enoch_charles_1912_djvu.txt",
                "url": "https://archive.org/download/bookofenochor1en00char/bookofenochor1en00char_djvu.txt",
                "role": "Greek-fragment candidate; Internet Archive OCR needs PDF/image verification before source-row import",
            }
        ],
        "comparison_witness_inventory": OCP_WITNESS_INVENTORY,
        "outputs": {
            "csv": str(CSV_OUTPUT.relative_to(ROOT)),
            "comparison_queue": str(QUEUE_OUTPUT.relative_to(ROOT)),
            "progress": str(PROGRESS_OUTPUT.relative_to(ROOT)),
            "diagnostics": str(DIAGNOSTICS_OUTPUT.relative_to(ROOT)),
        },
        "diagnostics": diagnostics,
        "validation_command": "make build-enoch-witness",
    }
    with MANIFEST_OUTPUT.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def write_progress(rows: list[dict[str, str]], diagnostics: dict[str, object]) -> None:
    PROGRESS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    marker_counts = diagnostics["marker_counts"]
    sample_refs = ["1 Enoch 1:9", "1 Enoch 3:1", "1 Enoch 4:1", "1 Enoch 108:1"]
    by_ref = {row["ref"]: row for row in rows}
    lines = [
        "# 1 Enoch Witness Workspace",
        "",
        "1 Enoch is kept separate from the Greek deuterocanon source workspace.",
        "This workspace parses the public-domain Charles 1917 English witness from Ethiopic and preserves Charles's comparison markers.",
        "",
        "## Counts",
        "",
        f"- Rows: {diagnostics['rows']}",
        f"- Chapters: {diagnostics['chapter_count']}",
        f"- First ref: {diagnostics['first_ref']}",
        f"- Last ref: {diagnostics['last_ref']}",
        f"- Missing chapters: {', '.join(map(str, diagnostics['missing_chapters'])) or 'None'}",
        f"- Comparison queue rows: {diagnostics['comparison_queue_rows']}",
        "",
        "## Comparison Witness Inventory",
        "",
        "- Ethiopic: Rylands Manuscript 23 (OCP p), 17th or 18th century AD.",
        "- Greek: 7QEnoch, POxy2069, Chester Beatty 185, Vatican Greek 1809, Gizeh/Akhmim, Syncellus, Jude 14-15.",
        "- Aramaic: 4Q201-4Q212 and 4Q247 per OCP inventory; OCP currently includes Aramaic fragments through chapter 8.",
        "",
        "## Marker Counts",
        "",
    ]
    for key, value in marker_counts.items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Sample Rows", ""])
    for ref in sample_refs:
        row = by_ref.get(ref)
        if not row:
            continue
        lines.append(f"### {ref}")
        lines.append("")
        lines.append(row["draft_translation"])
        if row["comparison_notes"]:
            lines.append("")
            lines.append(f"Comparison: {row['comparison_notes']}")
        lines.append("")
    PROGRESS_OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_diagnostics(diagnostics: dict[str, object]) -> None:
    DIAGNOSTICS_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with DIAGNOSTICS_OUTPUT.open("w", encoding="utf-8") as handle:
        json.dump(diagnostics, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def main() -> None:
    rows, diagnostics = build_rows()
    write_csv(rows)
    diagnostics["comparison_queue_rows"] = write_queue(rows)
    write_manifest(diagnostics)
    write_progress(rows, diagnostics)
    write_diagnostics(diagnostics)
    print(
        f"Built {CSV_OUTPUT.relative_to(ROOT)}: "
        f"{diagnostics['rows']} rows, {diagnostics['chapter_count']} chapters"
    )


if __name__ == "__main__":
    main()
