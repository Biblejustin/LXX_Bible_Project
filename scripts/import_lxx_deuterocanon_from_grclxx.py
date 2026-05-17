#!/usr/bin/env python3
"""Import a separate LXX deuterocanon workspace from eBible Greek USFM."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import zipfile
from collections import Counter
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
DEUTEROCANON_RAW = RAW / "lxx_deuterocanon"
OUTPUT_DIR = ROOT / "output" / "deuterocanon"

PRIMARY_SOURCE_KEY = "grclxx"
SUPPLEMENTAL_SOURCE_KEY = "grcbrent"

SOURCE_URL = "https://ebible.org/Scriptures/grclxx_usfm.zip"
DETAILS_URL = "https://ebible.org/details.php?id=grclxx"
SOURCE_TITLE = "eBible GRCLXX Septuaginta USFM"
SOURCE_STATUS = "eBible details page labels the source public domain; package includes Orthodox Media Network notice text."
SOURCE_LAST_UPDATED = "2026-02-13"
SOURCE_VERIFIED_DATE = "2026-05-01"

SUPPLEMENTAL_SOURCE_URL = "https://ebible.org/Scriptures/grcbrent_usfm.zip"
SUPPLEMENTAL_DETAILS_URL = "https://ebible.org/details.php?id=grcbrent"
SUPPLEMENTAL_SOURCE_TITLE = "eBible GRCBRE Brenton Septuagint USFM"
SUPPLEMENTAL_SOURCE_STATUS = "eBible details page labels the Brenton Greek Septuagint source public domain."
SUPPLEMENTAL_SOURCE_LAST_UPDATED = "2026-04-08"
SUPPLEMENTAL_SOURCE_VERIFIED_DATE = "2026-05-03"

DEFAULT_ARCHIVE = DEUTEROCANON_RAW / "grclxx_usfm.zip"
DEFAULT_SUPPLEMENTAL_ARCHIVE = DEUTEROCANON_RAW / "grcbrent_usfm.zip"
DEFAULT_OUTPUT = DEUTEROCANON_RAW / "deuterocanon_full.csv"
DEFAULT_MANIFEST = DEUTEROCANON_RAW / "source_manifest.json"
DEFAULT_INVENTORY = OUTPUT_DIR / "lxx_deuterocanon_source_inventory.md"

CANONICAL_OVERLAP_DRAFT_ALIASES = {
    "2ES": "Ezra",
}

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


@dataclass(frozen=True)
class SourceBook:
    source_file: str
    book_code: str
    book_name: str
    expected_usfm_id: str
    expected_title: str
    source_key: str = PRIMARY_SOURCE_KEY
    source_scope: str = "all"
    chapter_filter: str | None = None
    note: str = ""


SOURCE_BOOKS = [
    SourceBook("41-TOBgrclxx.usfm", "TOB", "Tobit", "TOB", "ΤΩΒΙΤ"),
    SourceBook("42-JDTgrclxx.usfm", "JDT", "Judith", "JDT", "ΙΟΥΔΙΘ"),
    SourceBook(
        "43-ESGgrclxx.usfm",
        "ESG",
        "Greek Esther",
        "ESG",
        "ΕΣΘΗΡ",
        note="Imported as full Greek Esther; `ESGA` separately provides an additions-only view from the suffixed and inline-labeled rows.",
    ),
    SourceBook(
        "43-ESGgrclxx.usfm",
        "ESGA",
        "Greek Esther Additions",
        "ESG",
        "ΕΣΘΗΡ",
        source_scope="esther_additions",
        note="Additions-only view derived from the suffixed and inline-labeled rows in the full GRCLXX Greek Esther source; full Greek Esther remains imported as ESG.",
    ),
    SourceBook("45-WISgrclxx.usfm", "WIS", "Wisdom", "WIS", "ΣΟΦΙΑ ΣΟΛΟΜΩΝΤΟΣ"),
    SourceBook("46-SIRgrclxx.usfm", "SIR", "Sirach", "SIR", "ΣΟΦΙΑ ΣΕΙΡΑΧ"),
    SourceBook("47-BARgrclxx.usfm", "BAR", "Baruch", "BAR", "ΒΑΡΟΥΧ"),
    SourceBook("48-LJEgrclxx.usfm", "LJE", "Letter of Jeremiah", "LJE", "ΕΠΙΣΤΟΛΗ ΙΕΡΕΜΙΟΥ"),
    SourceBook("49-S3Ygrclxx.usfm", "S3Y", "Song of the Three Young Men", "S3Y", "ΠΡΟΣΕΥΧΗ ΑΖΑΡΙΟΥ ΚΑΙ ΥΜΝΟΣ ΤΩΝ ΤΡΙΩΝ"),
    SourceBook("50-SUSgrclxx.usfm", "SUS", "Susanna", "SUS", "ΣΩΣΑΝΝΑ"),
    SourceBook("51-BELgrclxx.usfm", "BEL", "Bel and the Dragon", "BEL", "ΒΗΛ ΚΑΙ ΔΡΑΚΩΝ"),
    SourceBook("52-1MAgrclxx.usfm", "1MA", "1 Maccabees", "1MA", "ΜΑΚΚΑΒΑΙΩΝ Α"),
    SourceBook(
        "53-2MAgrcbrent.usfm",
        "2MA",
        "2 Maccabees",
        "2MA",
        "ΜΑΚΚΑΒΑΙΩΝ Βʹ",
        source_key=SUPPLEMENTAL_SOURCE_KEY,
        note="Imported from the public-domain eBible Brenton Greek Septuagint package because the pinned GRCLXX package's 2MA file contains 4 Maccabees.",
    ),
    SourceBook("54-1ESgrclxx.usfm", "1ES", "1 Esdras", "1ES", "ΕΣΔΡΑΣ Α"),
    SourceBook(
        "58-2ESgrclxx.usfm",
        "2ES",
        "2 Esdras",
        "2ES",
        "ΕΣΔΡΑΣ Β",
        note="Greek Ezra B / 2 Esdras from the primary GRCLXX package; this overlaps canonical Ezra and is included for broad EO appendix coverage. This is not the Latin apocalypse commonly titled 2 Esdras / 4 Ezra in some English traditions.",
    ),
    SourceBook(
        "55-MANgrcbrent.usfm",
        "MAN",
        "Prayer of Manasseh",
        "MAN",
        "ΠΡΟΣΕΥΧΗ ΜΑΝΑΣΣΗ ΥΙΟΥ ΕΖΕΚΙΟΥ",
        source_key=SUPPLEMENTAL_SOURCE_KEY,
        note="Imported from the public-domain eBible Brenton Greek Septuagint package because Prayer of Manasseh is absent from the pinned GRCLXX package.",
    ),
    SourceBook("57-3MAgrclxx.usfm", "3MA", "3 Maccabees", "3MA", "ΜΑΚΚΑΒΑΙΩΝ Γ"),
    SourceBook(
        "53-2MAgrclxx.usfm",
        "4MA",
        "4 Maccabees",
        "2MA",
        "ΜΑΚΚΑΒΑΙΩΝ Δ",
        note="The source package filename/id says 2MA, but the book title is ΜΑΚΚΑΒΑΙΩΝ Δ / 4 Maccabees.",
    ),
    SourceBook(
        "20-PSAgrclxx.usfm",
        "PSA",
        "Psalms",
        "PSA",
        "ΨΑΛΜΟΙ",
        source_scope="chapter",
        chapter_filter="151",
        note="Imported only Psalm 151 from the full Psalms source file.",
    ),
]

MISSING_TARGETS: list[dict[str, str]] = []

EXCLUDED_PACKAGE_FILES = [
    {
        "book_code": "DAG",
        "book_name": "Greek Daniel",
        "reason": "Canonical Daniel is handled by the main OT source; Daniel additions are imported from S3Y, SUS, and BEL.",
    },
]

CHAPTER_RE = re.compile(r"^\\c\s+(\S+)")
VERSE_RE = re.compile(r"^\\v\s+(\S+)\s*(.*)$")
FOOTNOTE_RE = re.compile(r"\\f\s+.*?\\f\*", flags=re.S)
CROSSREF_RE = re.compile(r"\\x\s+.*?\\x\*", flags=re.S)
USFM_MARKER_RE = re.compile(r"\\[a-zA-Z0-9]+\\*?")
USFM_METADATA_RE = re.compile(r"^\\(id|h|toc1|toc2|toc3|mt1)\s+(.+?)\s*$")
VERSE_SUFFIX_RE = re.compile(r"[A-Za-zΑ-Ωα-ω]$")
PLAIN_INLINE_VERSE_RE = re.compile(r"(?<!\S)(\d+(?:[A-Za-zΑ-Ωα-ω])?)\s+")
GREEK_INLINE_VERSE_RE = re.compile(r"(?<!\S)(\d+[Α-Ωα-ω])\s+")
DRAFT_INLINE_VERSE_RE = re.compile(r"\[(\d+(?:[A-Za-zΑ-Ωα-ω])?)\]\s+")
REF_RE = re.compile(r"^(?P<book>.+) (?P<chapter>[^:]+):(?P<verse>\S+)$")

SOURCE_METADATA = {
    PRIMARY_SOURCE_KEY: {
        "source_title": SOURCE_TITLE,
        "source_url": SOURCE_URL,
        "details_url": DETAILS_URL,
        "source_status": SOURCE_STATUS,
        "source_last_updated": SOURCE_LAST_UPDATED,
        "source_verified_date": SOURCE_VERIFIED_DATE,
    },
    SUPPLEMENTAL_SOURCE_KEY: {
        "source_title": SUPPLEMENTAL_SOURCE_TITLE,
        "source_url": SUPPLEMENTAL_SOURCE_URL,
        "details_url": SUPPLEMENTAL_DETAILS_URL,
        "source_status": SUPPLEMENTAL_SOURCE_STATUS,
        "source_last_updated": SUPPLEMENTAL_SOURCE_LAST_UPDATED,
        "source_verified_date": SUPPLEMENTAL_SOURCE_VERIFIED_DATE,
    },
}


def normalize_source_encoding(text: str) -> str:
    return text.replace("ῃ£", "ῄ").replace("υ±", "ΰ")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download_archive(path: Path, url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "Codex Bible source importer"})
    with urlopen(request, timeout=60) as response:
        data = response.read()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def load_archive(path: Path, url: str, refresh: bool) -> bytes:
    if refresh or not path.exists():
        return download_archive(path, url)
    return path.read_bytes()


def verse_has_suffix(verse: str) -> bool:
    return bool(VERSE_SUFFIX_RE.search(verse.strip()))


def split_inline_verse_markers(text: str, pattern: re.Pattern[str]) -> tuple[str, dict[str, str]]:
    matches = list(pattern.finditer(text))
    if not matches:
        return text.strip(), {}
    leading = text[: matches[0].start()].strip()
    segments: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        segment = text[match.end() : end].strip()
        if segment:
            segments[match.group(1)] = segment
    return leading, segments


def expand_esther_addition_rows(
    parsed_rows: list[tuple[str, str, str, str]]
) -> list[tuple[str, str, str, str]]:
    expanded: list[tuple[str, str, str, str]] = []
    for chapter, verse, greek_text, syntax_notes in parsed_rows:
        leading, segments = split_inline_verse_markers(greek_text, GREEK_INLINE_VERSE_RE)
        if verse_has_suffix(verse):
            if leading:
                expanded.append((chapter, verse, leading, syntax_notes))
            elif not segments:
                expanded.append((chapter, verse, greek_text, syntax_notes))
            for inline_verse, segment in segments.items():
                expanded.append((chapter, inline_verse, segment, syntax_notes))
        elif segments:
            for inline_verse, segment in segments.items():
                expanded.append((chapter, inline_verse, segment, syntax_notes))
    return expanded


def expand_plain_inline_verse_rows(
    parsed_rows: list[tuple[str, str, str, str]]
) -> list[tuple[str, str, str, str]]:
    expanded: list[tuple[str, str, str, str]] = []
    for chapter, verse, greek_text, syntax_notes in parsed_rows:
        leading, segments = split_inline_verse_markers(greek_text, PLAIN_INLINE_VERSE_RE)
        if not segments:
            expanded.append((chapter, verse, greek_text, syntax_notes))
            continue
        if leading:
            expanded.append((chapter, verse, leading, syntax_notes))
        else:
            expanded.append((chapter, verse, greek_text, syntax_notes))
        for inline_verse, segment in segments.items():
            expanded.append((chapter, inline_verse, segment, syntax_notes))
    return expanded


def inline_verse_label_count(
    parsed_rows: list[tuple[str, str, str, str]],
    pattern: re.Pattern[str],
) -> int:
    return sum(
        len(split_inline_verse_markers(greek_text, pattern)[1])
        for _chapter, _verse, greek_text, _syntax_notes in parsed_rows
    )


def clean_usfm_text(text: str) -> str:
    text = FOOTNOTE_RE.sub(" ", text)
    text = CROSSREF_RE.sub(" ", text)
    text = USFM_MARKER_RE.sub(" ", text)
    text = text.replace("\ufeff", "")
    text = text.replace("\xa0", " ")
    text = normalize_source_encoding(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_source_note(text: str) -> str:
    text = text.replace("\\f*", " ")
    text = re.sub(r"\\f\s*\+\s*", " ", text)
    text = re.sub(r"\\fr\s+[^\\]+", " ", text)
    text = re.sub(r"\\f[qkva-z0-9]*\s*", " ", text, flags=re.I)
    text = USFM_MARKER_RE.sub(" ", text)
    text = text.replace("\xa0", " ")
    text = normalize_source_encoding(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def source_footnotes(text: str) -> list[str]:
    notes: list[str] = []
    for match in FOOTNOTE_RE.finditer(text):
        note = clean_source_note(match.group(0))
        if note:
            notes.append(note)
    return notes


def extract_usfm_metadata(usfm_text: str) -> dict[str, object]:
    metadata: dict[str, object] = {
        "source_usfm_id": "",
        "source_titles": [],
    }
    titles: list[str] = []
    for raw_line in usfm_text.splitlines():
        line = raw_line.strip()
        match = USFM_METADATA_RE.match(line)
        if not match:
            if line.startswith("\\c "):
                break
            continue
        marker, value = match.groups()
        value = value.strip()
        if marker == "id":
            metadata["source_usfm_id"] = value.split()[0] if value else ""
        elif value and value not in titles:
            titles.append(value)
    metadata["source_titles"] = titles
    return metadata


def parse_usfm_verses(usfm_text: str) -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    current_chapter = ""
    current_verse = ""
    current_parts: list[str] = []
    pending_descriptors: list[str] = []

    def flush_current() -> None:
        nonlocal current_verse, current_parts, pending_descriptors
        if current_chapter and current_verse and current_parts:
            raw_text = " ".join(current_parts)
            greek_text = clean_usfm_text(raw_text)
            notes = source_footnotes(raw_text)
            syntax_note_parts = [f"Source descriptor: {value}" for value in pending_descriptors]
            syntax_note_parts.extend(f"Source footnote: {note}" for note in notes)
            syntax_notes = "; ".join(syntax_note_parts)
            if greek_text:
                rows.append((current_chapter, current_verse, greek_text, syntax_notes))
            pending_descriptors = []
        current_verse = ""
        current_parts = []

    for raw_line in usfm_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        chapter_match = CHAPTER_RE.match(line)
        if chapter_match:
            flush_current()
            current_chapter = chapter_match.group(1).strip()
            continue

        verse_match = VERSE_RE.match(line)
        if verse_match:
            flush_current()
            current_verse = verse_match.group(1).strip()
            current_parts = [verse_match.group(2).strip()]
            continue

        if line.startswith("\\d "):
            descriptor = clean_usfm_text(line)
            if descriptor:
                pending_descriptors.append(descriptor)
            continue

        if line.startswith("\\ip "):
            descriptor = clean_usfm_text(line)
            if descriptor:
                pending_descriptors.append(descriptor)
            continue

        if current_verse and not line.startswith("\\"):
            current_parts.append(line)
            continue

        if current_verse and line.startswith("\\") and not re.match(r"^\\[a-z0-9]+\s*$", line, flags=re.I):
            current_parts.append(line)

    flush_current()
    return rows


def import_rows(source_archives: dict[str, bytes]) -> tuple[list[dict[str, str]], dict[str, object]]:
    rows: list[dict[str, str]] = []
    book_stats: dict[str, dict[str, object]] = {}
    with zipfile.ZipFile(BytesIO(source_archives[PRIMARY_SOURCE_KEY])) as primary_archive, zipfile.ZipFile(
        BytesIO(source_archives[SUPPLEMENTAL_SOURCE_KEY])
    ) as supplemental_archive:
        archives = {
            PRIMARY_SOURCE_KEY: primary_archive,
            SUPPLEMENTAL_SOURCE_KEY: supplemental_archive,
        }
        available_files_by_source = {key: set(archive.namelist()) for key, archive in archives.items()}
        for source_book in SOURCE_BOOKS:
            archive = archives[source_book.source_key]
            available_files = available_files_by_source[source_book.source_key]
            source_metadata = SOURCE_METADATA[source_book.source_key]
            if source_book.source_file not in available_files:
                book_stats[source_book.book_code] = {
                    "book_name": source_book.book_name,
                    "source_key": source_book.source_key,
                    "source_title": source_metadata["source_title"],
                    "source_url": source_metadata["source_url"],
                    "details_url": source_metadata["details_url"],
                    "source_file": source_book.source_file,
                    "source_usfm_id": "",
                    "expected_usfm_id": source_book.expected_usfm_id,
                    "source_titles": [],
                    "expected_title": source_book.expected_title,
                    "source_id_match": False,
                    "source_title_match": False,
                    "status": "missing_source_file",
                    "rows": 0,
                }
                continue
            text = archive.read(source_book.source_file).decode("utf-8-sig", errors="replace")
            metadata = extract_usfm_metadata(text)
            source_titles = metadata["source_titles"]
            title_haystack = " | ".join(source_titles) if isinstance(source_titles, list) else ""
            source_usfm_id = str(metadata["source_usfm_id"])
            id_match = source_usfm_id == source_book.expected_usfm_id
            title_match = source_book.expected_title in title_haystack
            parsed_rows = parse_usfm_verses(text)
            raw_parsed_rows = parsed_rows
            plain_inline_verse_labels_split = 0
            esther_addition_inline_labels_selected = 0
            if source_book.source_scope == "chapter":
                parsed_rows = [
                    row for row in parsed_rows if row[0] == source_book.chapter_filter
                ]
            elif source_book.source_scope == "verse_suffix":
                parsed_rows = [row for row in parsed_rows if verse_has_suffix(row[1])]
            elif source_book.source_scope == "esther_additions":
                esther_addition_inline_labels_selected = inline_verse_label_count(
                    raw_parsed_rows,
                    GREEK_INLINE_VERSE_RE,
                )
                parsed_rows = expand_esther_addition_rows(parsed_rows)
            else:
                plain_inline_verse_labels_split = inline_verse_label_count(
                    raw_parsed_rows,
                    PLAIN_INLINE_VERSE_RE,
                )
                parsed_rows = expand_plain_inline_verse_rows(parsed_rows)
            source_note_count = sum(1 for row in parsed_rows if row[3])
            bracketed_source_text_rows = sum(1 for row in parsed_rows if "[" in row[2] or "]" in row[2])
            for chapter, verse, greek_text, syntax_notes in parsed_rows:
                rows.append(
                    {
                        "ref": f"{source_book.book_name} {chapter}:{verse}",
                        "book_code": source_book.book_code,
                        "book_name": source_book.book_name,
                        "chapter": chapter,
                        "verse": verse,
                        "greek_text": greek_text,
                        "transliteration": "",
                        "literal_gloss": "",
                        "syntax_notes": syntax_notes,
                        "draft_translation": "",
                    }
                )
            book_stats[source_book.book_code] = {
                "book_name": source_book.book_name,
                "source_key": source_book.source_key,
                "source_title": source_metadata["source_title"],
                "source_url": source_metadata["source_url"],
                "details_url": source_metadata["details_url"],
                "source_file": source_book.source_file,
                "source_scope": source_book.source_scope,
                "chapter_filter": source_book.chapter_filter,
                "source_usfm_id": source_usfm_id,
                "expected_usfm_id": source_book.expected_usfm_id,
                "source_titles": source_titles,
                "expected_title": source_book.expected_title,
                "source_id_match": id_match,
                "source_title_match": title_match,
                "rows": len(parsed_rows),
                "source_note_rows": source_note_count,
                "plain_inline_verse_labels_split": plain_inline_verse_labels_split,
                "esther_addition_inline_labels_selected": esther_addition_inline_labels_selected,
                "bracketed_source_text_rows": bracketed_source_text_rows,
                "note": source_book.note,
                "status": "imported" if parsed_rows and id_match and title_match else "needs_source_review",
            }

    diagnostics = {
        "rows": len(rows),
        "book_count": len({row["book_code"] for row in rows}),
        "source_note_rows": sum(1 for row in rows if row.get("syntax_notes", "").strip()),
        "plain_inline_verse_labels_split": sum(
            int(stat.get("plain_inline_verse_labels_split", 0)) for stat in book_stats.values()
        ),
        "esther_addition_inline_labels_selected": sum(
            int(stat.get("esther_addition_inline_labels_selected", 0)) for stat in book_stats.values()
        ),
        "bracketed_source_text_rows": sum(
            int(stat.get("bracketed_source_text_rows", 0)) for stat in book_stats.values()
        ),
        "source_validation": {
            "checked_books": len(book_stats),
            "source_id_mismatches": [
                code for code, stat in book_stats.items() if not stat.get("source_id_match")
            ],
            "source_title_mismatches": [
                code for code, stat in book_stats.items() if not stat.get("source_title_match")
            ],
            "needs_source_review": [
                code for code, stat in book_stats.items() if stat.get("status") == "needs_source_review"
            ],
        },
        "books": book_stats,
        "missing_targets": MISSING_TARGETS,
        "excluded_package_files": EXCLUDED_PACKAGE_FILES,
    }
    return rows, diagnostics


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def load_existing_drafts(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        rows = {}
        for row in reader:
            draft = row.get("draft_translation", "").strip()
            ref = row.get("ref", "").strip()
            if ref and draft:
                rows[ref] = {
                    "draft_translation": draft,
                    "greek_text": normalize_source_encoding(row.get("greek_text", "")),
                }
        return rows


def esther_addition_segment_drafts(
    existing_drafts: dict[str, dict[str, str]]
) -> dict[str, dict[str, str]]:
    segments: dict[str, dict[str, str]] = {}
    for ref, data in existing_drafts.items():
        match = REF_RE.match(ref)
        if not match or match.group("book") != "Greek Esther":
            continue
        chapter = match.group("chapter")
        verse = match.group("verse")
        greek_text = data.get("greek_text", "")
        draft = data.get("draft_translation", "")
        greek_leading, greek_segments = split_inline_verse_markers(
            greek_text, GREEK_INLINE_VERSE_RE
        )
        draft_leading, draft_segments = split_inline_verse_markers(
            draft, DRAFT_INLINE_VERSE_RE
        )

        def add_segment(target_verse: str, target_greek: str, target_draft: str) -> None:
            target_ref = f"Greek Esther Additions {chapter}:{target_verse}"
            if target_greek and target_draft:
                segments[target_ref] = {
                    "greek_text": target_greek,
                    "draft_translation": target_draft,
                }

        if verse_has_suffix(verse):
            if greek_leading and draft_leading:
                add_segment(verse, greek_leading, draft_leading)
            elif not greek_segments and not draft_segments:
                add_segment(verse, greek_text, draft)
            for inline_verse, target_greek in greek_segments.items():
                add_segment(inline_verse, target_greek, draft_segments.get(inline_verse, ""))
        else:
            for inline_verse, target_greek in greek_segments.items():
                add_segment(inline_verse, target_greek, draft_segments.get(inline_verse, ""))
    return segments


def plain_inline_segment_drafts(
    existing_drafts: dict[str, dict[str, str]]
) -> dict[str, dict[str, str]]:
    segments: dict[str, dict[str, str]] = {}
    for ref, data in existing_drafts.items():
        match = REF_RE.match(ref)
        if not match:
            continue
        book = match.group("book")
        chapter = match.group("chapter")
        greek_text = data.get("greek_text", "")
        draft = data.get("draft_translation", "")
        greek_leading, greek_segments = split_inline_verse_markers(
            greek_text, PLAIN_INLINE_VERSE_RE
        )
        draft_leading, draft_segments = split_inline_verse_markers(
            draft, DRAFT_INLINE_VERSE_RE
        )
        if greek_segments and greek_leading and draft_leading:
            segments[ref] = {
                "greek_text": greek_leading,
                "draft_translation": draft_leading,
            }
        for inline_verse, target_greek in greek_segments.items():
            target_draft = draft_segments.get(inline_verse, "")
            target_ref = f"{book} {chapter}:{inline_verse}"
            if target_greek and target_draft:
                segments[target_ref] = {
                    "greek_text": target_greek,
                    "draft_translation": target_draft,
                }
    return segments


def preserve_existing_drafts(
    rows: list[dict[str, str]],
    existing_drafts: dict[str, dict[str, str]],
) -> dict[str, int]:
    counts: Counter[str] = Counter()
    esther_segments = esther_addition_segment_drafts(existing_drafts)
    plain_segments = plain_inline_segment_drafts(existing_drafts)
    for row in rows:
        ref = row["ref"]
        existing = existing_drafts.get(ref)
        canonical_overlap = False
        if row.get("book_code") == "ESGA":
            segment_existing = esther_segments.get(ref)
            if segment_existing:
                existing = segment_existing
                counts["candidate_esther_additions_segment_rows"] += 1
        if not existing and row.get("book_code") == "ESGA":
            source_ref = ref.replace("Greek Esther Additions", "Greek Esther", 1)
            existing = existing_drafts.get(source_ref)
            if existing:
                counts["candidate_esther_additions_rows"] += 1
        segment_existing = plain_segments.get(ref)
        if segment_existing:
            existing = segment_existing
            counts["candidate_plain_inline_segment_rows"] += 1
        if not existing and row.get("book_code") in CANONICAL_OVERLAP_DRAFT_ALIASES:
            source_book = CANONICAL_OVERLAP_DRAFT_ALIASES[row["book_code"]]
            source_ref = f"{source_book} {row['chapter']}:{row['verse']}"
            existing = existing_drafts.get(source_ref)
            if existing:
                canonical_overlap = True
                counts["candidate_canonical_overlap_rows"] += 1
        if not existing:
            continue
        counts["candidate_rows"] += 1
        if not canonical_overlap and existing.get("greek_text", "") != row.get("greek_text", ""):
            counts["skipped_source_text_changed"] += 1
            continue
        row["draft_translation"] = existing["draft_translation"]
        counts["preserved_rows"] += 1
        if row.get("book_code") == "ESGA":
            counts["preserved_esther_additions_rows"] += 1
        if canonical_overlap or row.get("book_code") in CANONICAL_OVERLAP_DRAFT_ALIASES:
            counts["preserved_canonical_overlap_rows"] += 1
    counts["existing_draft_rows"] = len(existing_drafts)
    return dict(counts)


def load_preservation_drafts(output_path: Path) -> dict[str, dict[str, str]]:
    drafts = load_existing_drafts(RAW / "lxx_greek" / "ot_full.csv")
    drafts.update(load_existing_drafts(output_path))
    return drafts


def build_manifest(
    *,
    archive_path: Path,
    archive_sha256: str,
    supplemental_archive_path: Path,
    supplemental_archive_sha256: str,
    output_path: Path,
    output_sha256: str,
    diagnostics: dict[str, object],
) -> dict[str, object]:
    return {
        "source_title": SOURCE_TITLE,
        "source_url": SOURCE_URL,
        "details_url": DETAILS_URL,
        "source_status": SOURCE_STATUS,
        "source_last_updated": SOURCE_LAST_UPDATED,
        "source_verified_date": SOURCE_VERIFIED_DATE,
        "archive": str(archive_path.relative_to(ROOT)),
        "archive_sha256": archive_sha256,
        "supplemental_source_title": SUPPLEMENTAL_SOURCE_TITLE,
        "supplemental_source_url": SUPPLEMENTAL_SOURCE_URL,
        "supplemental_details_url": SUPPLEMENTAL_DETAILS_URL,
        "supplemental_source_status": SUPPLEMENTAL_SOURCE_STATUS,
        "supplemental_source_last_updated": SUPPLEMENTAL_SOURCE_LAST_UPDATED,
        "supplemental_source_verified_date": SUPPLEMENTAL_SOURCE_VERIFIED_DATE,
        "supplemental_archive": str(supplemental_archive_path.relative_to(ROOT)),
        "supplemental_archive_sha256": supplemental_archive_sha256,
        "source_archives": [
            {
                "key": PRIMARY_SOURCE_KEY,
                "source_title": SOURCE_TITLE,
                "source_url": SOURCE_URL,
                "details_url": DETAILS_URL,
                "source_status": SOURCE_STATUS,
                "source_last_updated": SOURCE_LAST_UPDATED,
                "source_verified_date": SOURCE_VERIFIED_DATE,
                "archive": str(archive_path.relative_to(ROOT)),
                "archive_sha256": archive_sha256,
            },
            {
                "key": SUPPLEMENTAL_SOURCE_KEY,
                "source_title": SUPPLEMENTAL_SOURCE_TITLE,
                "source_url": SUPPLEMENTAL_SOURCE_URL,
                "details_url": SUPPLEMENTAL_DETAILS_URL,
                "source_status": SUPPLEMENTAL_SOURCE_STATUS,
                "source_last_updated": SUPPLEMENTAL_SOURCE_LAST_UPDATED,
                "source_verified_date": SUPPLEMENTAL_SOURCE_VERIFIED_DATE,
                "archive": str(supplemental_archive_path.relative_to(ROOT)),
                "archive_sha256": supplemental_archive_sha256,
            },
        ],
        "imported_csv": str(output_path.relative_to(ROOT)),
        "imported_csv_sha256": output_sha256,
        "csv_columns": CSV_COLUMNS,
        "missing_source_candidates_doc": "docs/DEUTEROCANON_MISSING_SOURCES.md",
        "pending_decisions_doc": "docs/DEUTEROCANON_PENDING_DECISIONS.md",
        "validation_command": "make validate-deuterocanon",
        "translation_policy": "Importer-created rows start with blank draft_translation; reruns preserve existing draft translations when the reference and Greek source text still match. The GRCLXX package is the primary source; the public-domain eBible Brenton Greek package supplies Prayer of Manasseh and true 2 Maccabees rows absent from GRCLXX. Greek Ezra B / 2 Esdras is a canonical-overlap appendix stream and preserves its separate Greek source rows for review. This workspace starts from Greek source rows, not from an English base. Additional appendix material is skipped unless a Greek source is present, or unless strong evidence for a Greek source behind the extant text is documented.",
        "diagnostics": diagnostics,
    }


def write_inventory(path: Path, manifest: dict[str, object]) -> None:
    diagnostics = manifest["diagnostics"]
    books = diagnostics["books"]
    lines = [
        "# LXX Deuterocanon Source Inventory",
        "",
        "This is a separate source workspace for the LXX deuterocanon/additions workstream.",
        "It is not folded into the current 66-book Greek Heritage Study Bible outputs.",
        "",
        "## Sources",
        "",
        f"- Source: {manifest['source_title']}",
        f"- Details: {manifest['details_url']}",
        f"- Archive: {manifest['source_url']}",
        f"- Status: {manifest['source_status']}",
        f"- Source last updated: {manifest['source_last_updated']}",
        f"- Verified for this repo: {manifest['source_verified_date']}",
        f"- Archive SHA-256: `{manifest['archive_sha256']}`",
        f"- Supplemental source: {manifest['supplemental_source_title']}",
        f"- Supplemental details: {manifest['supplemental_details_url']}",
        f"- Supplemental archive: {manifest['supplemental_source_url']}",
        f"- Supplemental status: {manifest['supplemental_source_status']}",
        f"- Supplemental source last updated: {manifest['supplemental_source_last_updated']}",
        f"- Supplemental verified for this repo: {manifest['supplemental_source_verified_date']}",
        f"- Supplemental archive SHA-256: `{manifest['supplemental_archive_sha256']}`",
        "",
        "## Import Policy",
        "",
        "- Imported rows preserve Greek source text by verse.",
        "- USFM source descriptors and footnotes are preserved as `syntax_notes`.",
        "- `draft_translation` starts blank on first import; importer reruns preserve existing drafts when the reference and Greek source text still match.",
        "- Brenton English and other English witnesses are not used as the translation base.",
        "- The public-domain eBible Brenton Greek package is used only as a supplemental Greek source for Prayer of Manasseh and true 2 Maccabees.",
        "- Plain embedded verse labels in source rows are split into separate rows; bracketed source-text sections remain bracketed.",
        "- Greek Esther is imported twice: `ESG` is full Greek Esther, and `ESGA` is an additions-only view made from suffixed and inline-labeled GRCLXX Greek Esther rows.",
        "- `2ES` is Greek Ezra B / 2 Esdras from GRCLXX; it overlaps canonical Ezra and keeps separate Greek rows for audit. It is not the Latin apocalypse commonly titled 2 Esdras / 4 Ezra in some English traditions.",
        "- Additional appendix material is skipped unless a Greek source is present, or unless strong evidence for a Greek source behind the extant text is documented.",
        "- Importer validates source USFM IDs and Greek title lines before accepting source rows.",
        "- Psalm 151 is imported from the Psalms source file as Psalms 151.",
        "",
        "## Imported Books",
        "",
        "| Code | Book | Rows | Source | Source file | Source ID | Expected title | Validation | Note |",
        "| --- | --- | ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for source_book in SOURCE_BOOKS:
        stat = books.get(source_book.book_code, {})
        rows = stat.get("rows", 0) if isinstance(stat, dict) else 0
        source_key = stat.get("source_key", source_book.source_key) if isinstance(stat, dict) else source_book.source_key
        source_id = stat.get("source_usfm_id", "") if isinstance(stat, dict) else ""
        expected_title = stat.get("expected_title", source_book.expected_title) if isinstance(stat, dict) else source_book.expected_title
        validation = stat.get("status", "") if isinstance(stat, dict) else ""
        note = source_book.note or ""
        lines.append(
            f"| {source_book.book_code} | {source_book.book_name} | {rows} | {source_key} | "
            f"`{source_book.source_file}` | {source_id} | {expected_title} | {validation} | {note} |"
        )

    lines.extend(
        [
            "",
            "## Missing Target Books",
            "",
            "| Code | Book | Reason |",
            "| --- | --- | --- |",
        ]
    )
    for item in MISSING_TARGETS:
        lines.append(f"| {item['book_code']} | {item['book_name']} | {item['reason']} |")

    lines.extend(
        [
            "",
            "## Excluded Package Files",
            "",
            "| Code | Book | Reason |",
            "| --- | --- | --- |",
        ]
    )
    for item in EXCLUDED_PACKAGE_FILES:
        lines.append(f"| {item['book_code']} | {item['book_name']} | {item['reason']} |")

    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- Imported verse rows: {diagnostics['rows']}",
            f"- Imported book/addition groups: {diagnostics['book_count']}",
            f"- Rows with source notes/descriptors: {diagnostics['source_note_rows']}",
            f"- Plain embedded verse labels split into rows: {diagnostics['plain_inline_verse_labels_split']}",
            f"- Greek Esther addition inline labels selected: {diagnostics['esther_addition_inline_labels_selected']}",
            f"- Rows preserving bracketed source text: {diagnostics['bracketed_source_text_rows']}",
            f"- Preserved draft translation rows: {diagnostics.get('draft_preservation', {}).get('preserved_rows', 0)}",
            f"- Source ID mismatches: {len(diagnostics['source_validation']['source_id_mismatches'])}",
            f"- Source title mismatches: {len(diagnostics['source_validation']['source_title_mismatches'])}",
            f"- Imported CSV: `{manifest['imported_csv']}`",
            f"- Missing source candidates: `{manifest['missing_source_candidates_doc']}`",
            f"- Pending decisions: `{manifest['pending_decisions_doc']}`",
            f"- Validation command: `{manifest['validation_command']}`",
            "",
            "## Next Work",
            "",
            "- Continue proofreading one book/addition at a time against the Greek rows.",
            "- Do not add further appendix material unless it meets the Greek-source threshold documented above.",
            "- See `docs/DEUTEROCANON_MISSING_SOURCES.md` for checked source candidates and final source choice.",
            "- See `docs/DEUTEROCANON_PENDING_DECISIONS.md` for resolved decisions and remaining review notes.",
            "- Use `make validate-deuterocanon` before handoff or commit.",
            "- Decide later whether this workstream gets Markdown-only, Logos DOCX, print proof, or full-LXX merged outputs.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--supplemental-archive", type=Path, default=DEFAULT_SUPPLEMENTAL_ARCHIVE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--refresh-source", action="store_true")
    parser.add_argument(
        "--reset-drafts",
        action="store_true",
        help="Do not preserve existing draft_translation values when reimporting.",
    )
    args = parser.parse_args()

    archive_path = args.archive if args.archive.is_absolute() else ROOT / args.archive
    supplemental_archive_path = (
        args.supplemental_archive if args.supplemental_archive.is_absolute() else ROOT / args.supplemental_archive
    )
    output_path = args.output if args.output.is_absolute() else ROOT / args.output
    manifest_path = args.manifest if args.manifest.is_absolute() else ROOT / args.manifest
    inventory_path = args.inventory if args.inventory.is_absolute() else ROOT / args.inventory

    archive_data = load_archive(archive_path, SOURCE_URL, refresh=args.refresh_source)
    supplemental_archive_data = load_archive(
        supplemental_archive_path,
        SUPPLEMENTAL_SOURCE_URL,
        refresh=args.refresh_source,
    )
    archive_sha256 = sha256_bytes(archive_data)
    supplemental_archive_sha256 = sha256_bytes(supplemental_archive_data)
    rows, diagnostics = import_rows(
        {
            PRIMARY_SOURCE_KEY: archive_data,
            SUPPLEMENTAL_SOURCE_KEY: supplemental_archive_data,
        }
    )
    existing_drafts = {} if args.reset_drafts else load_preservation_drafts(output_path)
    diagnostics["draft_preservation"] = preserve_existing_drafts(rows, existing_drafts)
    write_rows(output_path, rows)
    output_sha256 = hashlib.sha256(output_path.read_bytes()).hexdigest()
    manifest = build_manifest(
        archive_path=archive_path,
        archive_sha256=archive_sha256,
        supplemental_archive_path=supplemental_archive_path,
        supplemental_archive_sha256=supplemental_archive_sha256,
        output_path=output_path,
        output_sha256=output_sha256,
        diagnostics=diagnostics,
    )
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_inventory(inventory_path, manifest)

    print(
        json.dumps(
            {
                "archive": str(archive_path),
                "archive_sha256": archive_sha256,
                "supplemental_archive": str(supplemental_archive_path),
                "supplemental_archive_sha256": supplemental_archive_sha256,
                "output": str(output_path),
                "rows": diagnostics["rows"],
                "book_count": diagnostics["book_count"],
                "manifest": str(manifest_path),
                "inventory": str(inventory_path),
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
