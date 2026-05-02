#!/usr/bin/env python3
"""Import a separate LXX deuterocanon workspace from eBible GRCLXX USFM."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import zipfile
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
DEUTEROCANON_RAW = RAW / "lxx_deuterocanon"
OUTPUT_DIR = ROOT / "output" / "deuterocanon"

SOURCE_URL = "https://ebible.org/Scriptures/grclxx_usfm.zip"
DETAILS_URL = "https://ebible.org/details.php?id=grclxx"
SOURCE_TITLE = "eBible GRCLXX Septuaginta USFM"
SOURCE_STATUS = "eBible details page labels the source public domain; package includes Orthodox Media Network notice text."
SOURCE_LAST_UPDATED = "2026-02-13"
SOURCE_VERIFIED_DATE = "2026-05-01"

DEFAULT_ARCHIVE = DEUTEROCANON_RAW / "grclxx_usfm.zip"
DEFAULT_OUTPUT = DEUTEROCANON_RAW / "deuterocanon_full.csv"
DEFAULT_MANIFEST = DEUTEROCANON_RAW / "source_manifest.json"
DEFAULT_INVENTORY = OUTPUT_DIR / "lxx_deuterocanon_source_inventory.md"

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
        note="Imported as full Greek Esther for now; additions-only slicing remains a later editorial step.",
    ),
    SourceBook("45-WISgrclxx.usfm", "WIS", "Wisdom", "WIS", "ΣΟΦΙΑ ΣΟΛΟΜΩΝΤΟΣ"),
    SourceBook("46-SIRgrclxx.usfm", "SIR", "Sirach", "SIR", "ΣΟΦΙΑ ΣΕΙΡΑΧ"),
    SourceBook("47-BARgrclxx.usfm", "BAR", "Baruch", "BAR", "ΒΑΡΟΥΧ"),
    SourceBook("48-LJEgrclxx.usfm", "LJE", "Letter of Jeremiah", "LJE", "ΕΠΙΣΤΟΛΗ ΙΕΡΕΜΙΟΥ"),
    SourceBook("49-S3Ygrclxx.usfm", "S3Y", "Song of the Three Young Men", "S3Y", "ΠΡΟΣΕΥΧΗ ΑΖΑΡΙΟΥ ΚΑΙ ΥΜΝΟΣ ΤΩΝ ΤΡΙΩΝ"),
    SourceBook("50-SUSgrclxx.usfm", "SUS", "Susanna", "SUS", "ΣΩΣΑΝΝΑ"),
    SourceBook("51-BELgrclxx.usfm", "BEL", "Bel and the Dragon", "BEL", "ΒΗΛ ΚΑΙ ΔΡΑΚΩΝ"),
    SourceBook("52-1MAgrclxx.usfm", "1MA", "1 Maccabees", "1MA", "ΜΑΚΚΑΒΑΙΩΝ Α"),
    SourceBook("54-1ESgrclxx.usfm", "1ES", "1 Esdras", "1ES", "ΕΣΔΡΑΣ Α"),
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

MISSING_TARGETS = [
    {
        "book_code": "MAN",
        "book_name": "Prayer of Manasseh",
        "reason": "Not present in the pinned GRCLXX USFM package.",
    },
    {
        "book_code": "2MA",
        "book_name": "2 Maccabees",
        "reason": "Not present as 2 Maccabees in the pinned GRCLXX USFM package; the package file named 2MA contains 4 Maccabees by title and content.",
    },
]

EXCLUDED_PACKAGE_FILES = [
    {
        "book_code": "2ES",
        "book_name": "2 Esdras / Greek Ezra B",
        "reason": "In this package this is the Greek Ezra-Nehemiah stream, not the separate deuterocanon work target.",
    },
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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download_archive(path: Path) -> bytes:
    request = Request(SOURCE_URL, headers={"User-Agent": "Codex Bible source importer"})
    with urlopen(request, timeout=60) as response:
        data = response.read()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return data


def load_archive(path: Path, refresh: bool) -> bytes:
    if refresh or not path.exists():
        return download_archive(path)
    return path.read_bytes()


def clean_usfm_text(text: str) -> str:
    text = FOOTNOTE_RE.sub(" ", text)
    text = CROSSREF_RE.sub(" ", text)
    text = USFM_MARKER_RE.sub(" ", text)
    text = text.replace("\ufeff", "")
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_source_note(text: str) -> str:
    text = text.replace("\\f*", " ")
    text = re.sub(r"\\f\s*\+\s*", " ", text)
    text = re.sub(r"\\fr\s+[^\\]+", " ", text)
    text = re.sub(r"\\f[qkva-z0-9]*\s*", " ", text, flags=re.I)
    text = USFM_MARKER_RE.sub(" ", text)
    text = text.replace("\xa0", " ")
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

        if current_verse and not line.startswith("\\"):
            current_parts.append(line)
            continue

        if current_verse and line.startswith("\\") and not re.match(r"^\\[a-z0-9]+\s*$", line, flags=re.I):
            current_parts.append(line)

    flush_current()
    return rows


def import_rows(archive_data: bytes) -> tuple[list[dict[str, str]], dict[str, object]]:
    rows: list[dict[str, str]] = []
    book_stats: dict[str, dict[str, object]] = {}
    with zipfile.ZipFile(BytesIO(archive_data)) as archive:
        available_files = set(archive.namelist())
        for source_book in SOURCE_BOOKS:
            if source_book.source_file not in available_files:
                book_stats[source_book.book_code] = {
                    "book_name": source_book.book_name,
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
            if source_book.source_scope == "chapter":
                parsed_rows = [
                    row for row in parsed_rows if row[0] == source_book.chapter_filter
                ]
            source_note_count = sum(1 for row in parsed_rows if row[3])
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
                "note": source_book.note,
                "status": "imported" if parsed_rows and id_match and title_match else "needs_source_review",
            }

    diagnostics = {
        "rows": len(rows),
        "book_count": len({row["book_code"] for row in rows}),
        "source_note_rows": sum(1 for row in rows if row.get("syntax_notes", "").strip()),
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
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def build_manifest(
    *,
    archive_path: Path,
    archive_sha256: str,
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
        "imported_csv": str(output_path.relative_to(ROOT)),
        "imported_csv_sha256": output_sha256,
        "csv_columns": CSV_COLUMNS,
        "translation_policy": "draft_translation is intentionally blank; this workspace starts from Greek source rows, not from Brenton or another English base.",
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
        "## Source",
        "",
        f"- Source: {manifest['source_title']}",
        f"- Details: {manifest['details_url']}",
        f"- Archive: {manifest['source_url']}",
        f"- Status: {manifest['source_status']}",
        f"- Source last updated: {manifest['source_last_updated']}",
        f"- Verified for this repo: {manifest['source_verified_date']}",
        f"- Archive SHA-256: `{manifest['archive_sha256']}`",
        "",
        "## Import Policy",
        "",
        "- Imported rows preserve Greek source text by verse.",
        "- USFM source descriptors and footnotes are preserved as `syntax_notes`.",
        "- `draft_translation` is intentionally blank.",
        "- Brenton and other English witnesses are not used as the translation base.",
        "- Greek Esther is imported as the full Greek Esther source for now; additions-only slicing remains a later editorial step.",
        "- Importer validates source USFM IDs and Greek title lines before accepting source rows.",
        "- Psalm 151 is imported from the Psalms source file as Psalms 151.",
        "",
        "## Imported Books",
        "",
        "| Code | Book | Rows | Source file | Source ID | Expected title | Validation | Note |",
        "| --- | --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for source_book in SOURCE_BOOKS:
        stat = books.get(source_book.book_code, {})
        rows = stat.get("rows", 0) if isinstance(stat, dict) else 0
        source_id = stat.get("source_usfm_id", "") if isinstance(stat, dict) else ""
        expected_title = stat.get("expected_title", source_book.expected_title) if isinstance(stat, dict) else source_book.expected_title
        validation = stat.get("status", "") if isinstance(stat, dict) else ""
        note = source_book.note or ""
        lines.append(
            f"| {source_book.book_code} | {source_book.book_name} | {rows} | "
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
            f"- Rows with source footnotes: {diagnostics['source_note_rows']}",
            f"- Source ID mismatches: {len(diagnostics['source_validation']['source_id_mismatches'])}",
            f"- Source title mismatches: {len(diagnostics['source_validation']['source_title_mismatches'])}",
            f"- Imported CSV: `{manifest['imported_csv']}`",
            "",
            "## Next Work",
            "",
            "- Translate one book/addition at a time from the Greek rows.",
            "- Decide whether Greek Esther should remain full Greek Esther here or be split into additions-only ranges.",
            "- Add lawful Greek source rows for Prayer of Manasseh and 2 Maccabees if those remain in scope.",
            "- See `output/deuterocanon/missing_source_candidates.md` for checked-but-not-imported source candidates.",
            "- Decide later whether this workstream gets Markdown-only, Logos DOCX, print proof, or full-LXX merged outputs.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--refresh-source", action="store_true")
    args = parser.parse_args()

    archive_path = args.archive if args.archive.is_absolute() else ROOT / args.archive
    output_path = args.output if args.output.is_absolute() else ROOT / args.output
    manifest_path = args.manifest if args.manifest.is_absolute() else ROOT / args.manifest
    inventory_path = args.inventory if args.inventory.is_absolute() else ROOT / args.inventory

    archive_data = load_archive(archive_path, refresh=args.refresh_source)
    archive_sha256 = sha256_bytes(archive_data)
    rows, diagnostics = import_rows(archive_data)
    write_rows(output_path, rows)
    output_sha256 = hashlib.sha256(output_path.read_bytes()).hexdigest()
    manifest = build_manifest(
        archive_path=archive_path,
        archive_sha256=archive_sha256,
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
