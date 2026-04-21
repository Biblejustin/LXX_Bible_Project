#!/usr/bin/env python3
"""Build Logos Personal Book and proofreading DOCX files for the fresh OT."""

from __future__ import annotations

import argparse
import csv
import json
import re
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape

try:
    from build_study_bible import (
        OPENBIBLE_BOOK_MAP,
        STANDARD_BOOK_NAMES,
        canonicalize_cross_references,
        parse_openbible_crossrefs,
        parse_tsk_module,
    )
except ImportError:  # pragma: no cover - supports module execution from repo root.
    from scripts.build_study_bible import (
        OPENBIBLE_BOOK_MAP,
        STANDARD_BOOK_NAMES,
        canonicalize_cross_references,
        parse_openbible_crossrefs,
        parse_tsk_module,
    )


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = DATA / "raw"
RESEARCH = DATA / "research"
OUTPUT = ROOT / "output" / "logos"

DEFAULT_SOURCE = RAW / "lxx_greek" / "ot_full.csv"
DEFAULT_FOOTNOTES = RESEARCH / "translation_footnotes.csv"
DEFAULT_LOGOS_DOCX = OUTPUT / "fresh_translation_ot_logos_bible.docx"
DEFAULT_PROOF_DOCX = OUTPUT / "fresh_translation_ot_proofreading.docx"
DEFAULT_DIAGNOSTICS = OUTPUT / "fresh_translation_ot_logos_bible_diagnostics.json"
DEFAULT_README = OUTPUT / "README.md"
DEFAULT_PREVIEW = OUTPUT / "fresh_translation_ot_logos_bible_preview.md"

DOCX_W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
DOCX_R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CONTENT_TYPES_NS = "http://schemas.openxmlformats.org/package/2006/content-types"

LXX_TSK_CODE_MAP = {
    "DAN": "DAG",
    "EST": "ESG",
}

GENERIC_FOOTNOTE_PATTERNS = (
    "Brenton differs here. The translation follows the current fresh wording at this verse numbering point.",
)

MAX_PHRASE_ANCHOR_CHARS = 120


@dataclass(frozen=True)
class Verse:
    ref: str
    book_code: str
    book_name: str
    chapter: int
    verse: int
    text: str

    @property
    def tsk_key(self) -> tuple[str, int, int]:
        return (LXX_TSK_CODE_MAP.get(self.book_code, self.book_code), self.chapter, self.verse)

    @property
    def logos_ref(self) -> str:
        return f"{logos_book_name(self.book_code, self.book_name)} {self.chapter}:{self.verse}"


@dataclass(frozen=True)
class TranslationNote:
    ref: str
    note_type: str
    trigger_phrase: str
    text: str
    source_basis: str

    @property
    def display_text(self) -> str:
        prefix = "Textual note" if self.note_type == "textual" else "Translation note"
        basis = f" Source: {self.source_basis}." if self.source_basis else ""
        return f"{prefix}: {self.text}{basis}"


@dataclass
class BuildStats:
    output_kind: str
    paragraph_count: int = 0
    footnote_count: int = 0
    crossref_footnotes: int = 0
    translation_note_footnotes: int = 0
    phrase_anchored_translation_notes: int = 0
    verse_anchored_translation_notes: int = 0


class MinimalDocx:
    """Small WordprocessingML writer with real footnote support."""

    def __init__(self, title: str, subject: str) -> None:
        self.title = title
        self.subject = subject
        self.body: list[str] = []
        self.footnotes: list[str] = []

    def add_paragraph(self, runs: Iterable[str], style: str = "Normal") -> None:
        ppr = f'<w:pPr><w:pStyle w:val="{attr(style)}"/></w:pPr>' if style != "Normal" else ""
        self.body.append(f"<w:p>{ppr}{''.join(runs)}</w:p>")

    def add_heading(self, text: str, level: int = 1) -> None:
        style = "Heading1" if level == 1 else "Heading2"
        self.add_paragraph([run(text)], style=style)

    def add_page_break(self) -> None:
        self.body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    def add_footnote(self, text: str) -> int:
        self.footnotes.append(text)
        return len(self.footnotes)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        document_xml = build_document_xml("\n".join(self.body))
        footnotes_xml = build_footnotes_xml(self.footnotes)
        now = datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        files = {
            "[Content_Types].xml": content_types_xml(),
            "_rels/.rels": root_rels_xml(),
            "docProps/core.xml": core_props_xml(self.title, self.subject, now),
            "docProps/app.xml": app_props_xml(),
            "word/document.xml": document_xml,
            "word/_rels/document.xml.rels": document_rels_xml(),
            "word/styles.xml": styles_xml(),
            "word/footnotes.xml": footnotes_xml,
        }
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for name, payload in files.items():
                zf.writestr(name, payload)


def attr(text: str) -> str:
    return escape(str(text), {'"': "&quot;"})


def text(text_value: str) -> str:
    return escape(str(text_value))


def run(
    value: str,
    *,
    bold: bool = False,
    italic: bool = False,
    style: str | None = None,
    small: bool = False,
    color: str | None = None,
) -> str:
    props: list[str] = []
    if style:
        props.append(f'<w:rStyle w:val="{attr(style)}"/>')
    if bold:
        props.append("<w:b/>")
    if italic:
        props.append("<w:i/>")
    if small:
        props.append('<w:sz w:val="18"/>')
    if color:
        props.append(f'<w:color w:val="{attr(color)}"/>')
    rpr = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
    return f'<w:r>{rpr}<w:t xml:space="preserve">{text(value)}</w:t></w:r>'


def footnote_ref_run(note_id: int) -> str:
    return (
        '<w:r><w:rPr><w:rStyle w:val="FootnoteReference"/></w:rPr>'
        f'<w:footnoteReference w:id="{note_id}"/></w:r>'
    )


def build_document_xml(body_xml: str) -> str:
    section = (
        "<w:sectPr>"
        '<w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080" '
        'w:header="720" w:footer="720" w:gutter="0"/>'
        "</w:sectPr>"
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<w:document xmlns:w="{DOCX_W_NS}" xmlns:r="{DOCX_R_NS}">'
        f"<w:body>{body_xml}{section}</w:body></w:document>"
    )


def build_footnotes_xml(notes: list[str]) -> str:
    items = [
        '<w:footnote w:type="separator" w:id="-1"><w:p><w:r><w:separator/></w:r></w:p></w:footnote>',
        '<w:footnote w:type="continuationSeparator" w:id="0"><w:p><w:r><w:continuationSeparator/></w:r></w:p></w:footnote>',
    ]
    for index, note_text in enumerate(notes, start=1):
        items.append(
            f'<w:footnote w:id="{index}">'
            '<w:p><w:pPr><w:pStyle w:val="FootnoteText"/></w:pPr>'
            '<w:r><w:rPr><w:rStyle w:val="FootnoteReference"/></w:rPr><w:footnoteRef/></w:r>'
            f'<w:r><w:t xml:space="preserve"> {text(note_text)}</w:t></w:r>'
            "</w:p></w:footnote>"
        )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<w:footnotes xmlns:w="{DOCX_W_NS}">{"".join(items)}</w:footnotes>'
    )


def content_types_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<Types xmlns="{CONTENT_TYPES_NS}">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '<Override PartName="/word/footnotes.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml"/>'
        '<Override PartName="/docProps/core.xml" '
        'ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
        '<Override PartName="/docProps/app.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
        "</Types>"
    )


def root_rels_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<Relationships xmlns="{REL_NS}">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="word/document.xml"/>'
        '<Relationship Id="rId2" '
        'Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" '
        'Target="docProps/core.xml"/>'
        '<Relationship Id="rId3" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" '
        'Target="docProps/app.xml"/>'
        "</Relationships>"
    )


def document_rels_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<Relationships xmlns="{REL_NS}">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" '
        'Target="styles.xml"/>'
        '<Relationship Id="rId2" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footnotes" '
        'Target="footnotes.xml"/>'
        "</Relationships>"
    )


def core_props_xml(title: str, subject: str, now: str) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" '
        'xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:dcmitype="http://purl.org/dc/dcmitype/" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        f"<dc:title>{text(title)}</dc:title>"
        f"<dc:subject>{text(subject)}</dc:subject>"
        "<dc:creator>Codex Bible Project</dc:creator>"
        "<cp:lastModifiedBy>Codex Bible Project</cp:lastModifiedBy>"
        f'<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>'
        f'<dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>'
        "</cp:coreProperties>"
    )


def app_props_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
        'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
        "<Application>Codex</Application>"
        "</Properties>"
    )


def styles_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<w:styles xmlns:w="{DOCX_W_NS}">'
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
        '<w:name w:val="Normal"/><w:qFormat/>'
        '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="22"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="paragraph" w:styleId="Title">'
        '<w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:qFormat/>'
        '<w:pPr><w:spacing w:after="240"/></w:pPr>'
        '<w:rPr><w:b/><w:sz w:val="40"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="paragraph" w:styleId="Subtitle">'
        '<w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/><w:qFormat/>'
        '<w:pPr><w:spacing w:after="180"/></w:pPr>'
        '<w:rPr><w:i/><w:color w:val="555555"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="paragraph" w:styleId="Heading1">'
        '<w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:qFormat/>'
        '<w:pPr><w:keepNext/><w:spacing w:before="420" w:after="180"/>'
        '<w:outlineLvl w:val="0"/></w:pPr>'
        '<w:rPr><w:b/><w:sz w:val="32"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="paragraph" w:styleId="Heading2">'
        '<w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:qFormat/>'
        '<w:pPr><w:keepNext/><w:spacing w:before="240" w:after="120"/>'
        '<w:outlineLvl w:val="1"/></w:pPr>'
        '<w:rPr><w:b/><w:sz w:val="26"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="character" w:styleId="FootnoteReference">'
        '<w:name w:val="Footnote Reference"/><w:semiHidden/><w:unhideWhenUsed/>'
        '<w:rPr><w:vertAlign w:val="superscript"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="paragraph" w:styleId="FootnoteText">'
        '<w:name w:val="Footnote Text"/><w:basedOn w:val="Normal"/>'
        '<w:pPr><w:spacing w:after="0"/></w:pPr>'
        '<w:rPr><w:sz w:val="18"/></w:rPr>'
        "</w:style>"
        "</w:styles>"
    )


def load_verses(path: Path) -> list[Verse]:
    rows = load_csv(path)
    verses: list[Verse] = []
    for row in rows:
        draft = row.get("draft_translation", "").strip()
        if not draft:
            continue
        verses.append(
            Verse(
                ref=row["ref"].strip(),
                book_code=row["book_code"].strip(),
                book_name=row["book_name"].strip(),
                chapter=int(row["chapter"]),
                verse=int(row["verse"]),
                text=draft,
            )
        )
    return verses


def load_translation_notes(path: Path) -> tuple[dict[str, list[TranslationNote]], dict[str, int]]:
    rows = load_csv(path)
    grouped: dict[str, list[TranslationNote]] = defaultdict(list)
    counts = Counter()
    for row in rows:
        counts["rows"] += 1
        if row.get("status", "").strip().lower() != "reviewed":
            counts["skipped_unreviewed"] += 1
            continue
        note_type = row.get("note_type", "").strip().lower()
        if note_type not in {"translation", "textual"}:
            counts["skipped_note_type"] += 1
            continue
        body = row.get("footnote_text", "").strip()
        if not body:
            counts["skipped_empty"] += 1
            continue
        if is_generic_or_brenton_only_note(row):
            counts["skipped_generic_or_brenton_only"] += 1
            continue
        note = TranslationNote(
            ref=row["ref"].strip(),
            note_type=note_type,
            trigger_phrase=row.get("trigger_phrase", "").strip(),
            text=body,
            source_basis=row.get("source_basis", "").strip(),
        )
        grouped[note.ref].append(note)
        counts["included"] += 1
    return dict(grouped), dict(counts)


def is_generic_or_brenton_only_note(row: dict[str, str]) -> bool:
    body = row.get("footnote_text", "").strip()
    if any(body == pattern for pattern in GENERIC_FOOTNOTE_PATTERNS):
        return True
    source = row.get("source_basis", "").strip().lower()
    return source == "translation comparison" and body.startswith("Brenton differs here.")


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def logos_book_name(book_code: str, fallback: str) -> str:
    name = STANDARD_BOOK_NAMES.get(LXX_TSK_CODE_MAP.get(book_code, book_code), fallback)
    if book_code == "DAN":
        return "Daniel"
    if book_code == "EST":
        return "Esther"
    return name


def build_crossrefs_for_verses(verses: list[Verse]) -> tuple[dict[str, list[str]], dict[str, object]]:
    tsk_refs, _tsk_notes, tsk_diag = parse_tsk_module()
    open_refs, open_diag = parse_openbible_crossrefs(limit_per_verse=9999)
    by_ref: dict[str, list[str]] = {}
    source_counts = Counter()
    total_refs = 0
    for verse in verses:
        refs = tsk_refs.get(verse.tsk_key, [])
        if refs:
            source_counts["tsk"] += 1
        else:
            refs = open_refs.get(verse.tsk_key, [])
            if refs:
                source_counts["openbible_fallback"] += 1
        cleaned = canonicalize_cross_references([format_openbible_ref(ref) for ref in refs])
        if cleaned:
            by_ref[verse.ref] = cleaned
            total_refs += len(cleaned)
    return by_ref, {
        "source_counts": dict(source_counts),
        "verses_with_crossrefs": len(by_ref),
        "total_crossrefs_after_canonicalization": total_refs,
        "tsk": tsk_diag,
        "openbible": open_diag,
    }


OPENBIBLE_TARGET_RE = re.compile(
    r"^([1-3]?[A-Za-z]+)\.(\d+)\.(\d+)(?:-([1-3]?[A-Za-z]+)\.(\d+)\.(\d+))?(?: \((\d+)\))?$"
)


def format_openbible_ref(ref: str) -> str:
    match = OPENBIBLE_TARGET_RE.match(ref.strip())
    if not match:
        return ref
    start_book, start_chapter, start_verse, end_book, end_chapter, end_verse, votes = match.groups()
    start_code = OPENBIBLE_BOOK_MAP.get(start_book)
    if not start_code:
        return ref
    start_label = STANDARD_BOOK_NAMES.get(start_code, start_book)
    label = f"{start_label} {int(start_chapter)}:{int(start_verse)}"
    if end_book and end_chapter and end_verse:
        end_code = OPENBIBLE_BOOK_MAP.get(end_book)
        end_label = STANDARD_BOOK_NAMES.get(end_code or "", end_book)
        if end_code == start_code and end_chapter == start_chapter:
            label += f"-{int(end_verse)}"
        else:
            label += f"-{end_label} {int(end_chapter)}:{int(end_verse)}"
    if votes:
        label += f" ({votes})"
    return label


def build_docx(
    *,
    path: Path,
    title: str,
    verses: list[Verse],
    translation_notes: dict[str, list[TranslationNote]],
    crossrefs: dict[str, list[str]],
    logos: bool,
    datatype: str,
) -> BuildStats:
    doc = MinimalDocx(
        title=title,
        subject="Fresh OT translation draft with translation notes and cross-references",
    )
    stats = BuildStats(output_kind="logos" if logos else "proofreading")
    add_title_page(doc, title, logos=logos, datatype=datatype)

    current_book = ""
    current_chapter = -1
    for verse in verses:
        if verse.book_name != current_book:
            current_book = verse.book_name
            current_chapter = -1
            if stats.paragraph_count:
                doc.add_page_break()
            doc.add_heading(verse.book_name, level=1)
            stats.paragraph_count += 1
        if verse.chapter != current_chapter:
            current_chapter = verse.chapter
            doc.add_heading(f"Chapter {verse.chapter}", level=2)
            stats.paragraph_count += 1

        runs = build_verse_runs(
            doc=doc,
            verse=verse,
            notes=translation_notes.get(verse.ref, []),
            refs=crossrefs.get(verse.ref, []),
            logos=logos,
            datatype=datatype,
            stats=stats,
        )
        doc.add_paragraph(runs)
        stats.paragraph_count += 1

    stats.footnote_count = len(doc.footnotes)
    doc.save(path)
    return stats


def add_title_page(doc: MinimalDocx, title: str, *, logos: bool, datatype: str) -> None:
    doc.add_paragraph([run(title)], style="Title")
    subtitle = "Logos Personal Book source" if logos else "Proofreading and print copy"
    doc.add_paragraph([run(subtitle)], style="Subtitle")
    lines = [
        "Fresh Old Testament translation draft.",
        "Includes reviewed translation/textual notes, excluding generic Brenton comparison notes.",
        "Includes full available cross-reference set from TSK, with OpenBible fallback where TSK has no row.",
        "Name meanings, lexicon entries, and Brenton study-package notes are intentionally excluded.",
    ]
    if logos:
        lines.append(f"Verse milestones use Logos datatype {datatype}. Compile in Logos as resource type Bible.")
    for line in lines:
        doc.add_paragraph([run(line)])
    doc.add_page_break()


def build_verse_runs(
    *,
    doc: MinimalDocx,
    verse: Verse,
    notes: list[TranslationNote],
    refs: list[str],
    logos: bool,
    datatype: str,
    stats: BuildStats,
) -> list[str]:
    runs: list[str] = []
    if logos:
        runs.append(run(f"[[@{datatype} :{verse.logos_ref}]] ", small=True, color="777777"))
    runs.append(run(f"{verse.verse} ", bold=True))
    if refs:
        note_id = doc.add_footnote("Cross-references: " + "; ".join(refs) + ".")
        runs.append(footnote_ref_run(note_id))
        stats.crossref_footnotes += 1
    if logos:
        runs.append(run(" {{field-on:Bible}}"))

    text_runs, phrase_count, verse_level_notes = runs_for_text_with_phrase_notes(doc, verse.text, notes, stats)
    runs.extend(text_runs)
    for note in verse_level_notes:
        note_id = doc.add_footnote(note.display_text)
        runs.append(footnote_ref_run(note_id))
        stats.translation_note_footnotes += 1
        stats.verse_anchored_translation_notes += 1
    if logos:
        runs.append(run("{{field-off:Bible}}"))
    return runs


def runs_for_text_with_phrase_notes(
    doc: MinimalDocx,
    verse_text: str,
    notes: list[TranslationNote],
    stats: BuildStats,
) -> tuple[list[str], int, list[TranslationNote]]:
    anchors: dict[int, list[TranslationNote]] = defaultdict(list)
    verse_level: list[TranslationNote] = []
    lowered = verse_text.casefold()
    occupied: list[tuple[int, int]] = []

    for note in notes:
        trigger = note.trigger_phrase.strip()
        if not trigger or len(trigger) > MAX_PHRASE_ANCHOR_CHARS:
            verse_level.append(note)
            continue
        start = lowered.find(trigger.casefold())
        if start < 0:
            verse_level.append(note)
            continue
        end = start + len(trigger)
        if any(not (end <= old_start or start >= old_end) for old_start, old_end in occupied):
            verse_level.append(note)
            continue
        occupied.append((start, end))
        anchors[end].append(note)

    output: list[str] = []
    cursor = 0
    for end in sorted(anchors):
        output.append(run(verse_text[cursor:end]))
        for note in anchors[end]:
            note_id = doc.add_footnote(note.display_text)
            output.append(footnote_ref_run(note_id))
            stats.translation_note_footnotes += 1
            stats.phrase_anchored_translation_notes += 1
        cursor = end
    output.append(run(verse_text[cursor:]))
    return output, len(anchors), verse_level


def build_preview(path: Path, verses: list[Verse], notes: dict[str, list[TranslationNote]], refs: dict[str, list[str]]) -> None:
    lines = [
        "# Fresh Translation OT Logos Bible Preview",
        "",
        "This preview shows the first three verses of each book with note/cross-reference counts.",
        "",
    ]
    by_book: dict[str, list[Verse]] = defaultdict(list)
    for verse in verses:
        by_book[verse.book_name].append(verse)
    for book, book_verses in by_book.items():
        lines.extend([f"## {book}", ""])
        for verse in book_verses[:3]:
            note_count = len(notes.get(verse.ref, []))
            crossref_count = len(refs.get(verse.ref, []))
            lines.append(f"**{verse.ref}** {verse.text}")
            lines.append(f"- Translation/textual notes: {note_count}")
            lines.append(f"- Cross-references: {crossref_count}")
            lines.append("")
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def build_readme(
    path: Path,
    *,
    logos_docx: Path,
    proof_docx: Path,
    diagnostics_path: Path,
    preview_path: Path,
    datatype: str,
) -> None:
    content = f"""# Fresh Translation OT Logos/Proofreading Files

Generated files:

- `{logos_docx.name}`: Logos Personal Book source. Compile as resource type `Bible`.
- `{proof_docx.name}`: clean proofreading/printing copy without Logos milestone or field syntax.
- `{diagnostics_path.name}`: build counts and cross-reference/note diagnostics.
- `{preview_path.name}`: quick preview sample for spot-checking.

Logos import:

1. Open Logos desktop.
2. Go to `Tools > Personal Books`.
3. Click `Add book`.
4. Set `Type` to `Bible`.
5. Add `{logos_docx.name}` as the body file.
6. Build the book.
7. If Logos exposes advanced datatype/index settings, keep the source milestones on `{datatype}`.

Scope:

- Source text: `data/raw/lxx_greek/ot_full.csv`.
- Translation notes: reviewed rows from `data/research/translation_footnotes.csv`.
- Excluded: generic Brenton comparison notes, name meanings, lexicon entries, vocabulary notes, names-of-God notes, and other Brenton package study notes.
- Cross-references: TSK primary set from `data/raw/TSK.zip`; OpenBible fallback from `data/raw/cross-references.zip` where TSK has no verse row. See root `NOTICE.md` for public-domain/CC-BY attribution details.

Validation:

- The repo validates DOCX package/XML structure locally and checks that macOS can read the generated DOCX. Final Personal Book compilation still needs to be checked inside Logos after each source change.
"""
    path.write_text(content, encoding="utf-8")


def validate_docx(path: Path) -> dict[str, object]:
    result: dict[str, object] = {"path": str(path), "zip_ok": False, "xml_ok": False, "entries": []}
    with zipfile.ZipFile(path) as zf:
        bad = zf.testzip()
        result["zip_ok"] = bad is None
        result["bad_entry"] = bad
        entries = zf.namelist()
        result["entries"] = entries
        xml_errors: list[str] = []
        for name in entries:
            if name.endswith(".xml"):
                try:
                    ET.fromstring(zf.read(name))
                except ET.ParseError as exc:
                    xml_errors.append(f"{name}: {exc}")
        result["xml_ok"] = not xml_errors
        result["xml_errors"] = xml_errors
        result["footnote_reference_count"] = zf.read("word/document.xml").count(b"<w:footnoteReference")
        footnotes_root = ET.fromstring(zf.read("word/footnotes.xml"))
        result["footnote_body_count"] = sum(
            1
            for node in footnotes_root
            if node.tag == f"{{{DOCX_W_NS}}}footnote"
            and node.attrib.get(f"{{{DOCX_W_NS}}}type") not in {"separator", "continuationSeparator"}
        )
    return result


def build_diagnostics(
    *,
    verses: list[Verse],
    note_counts: dict[str, int],
    notes: dict[str, list[TranslationNote]],
    crossref_diag: dict[str, object],
    logos_stats: BuildStats,
    proof_stats: BuildStats,
    validations: list[dict[str, object]],
    output_paths: dict[str, str],
    datatype: str,
) -> dict[str, object]:
    book_counts = Counter(verse.book_code for verse in verses)
    included_note_total = sum(len(items) for items in notes.values())
    return {
        "datatype": datatype,
        "verse_rows": len(verses),
        "book_count": len(book_counts),
        "book_counts": dict(book_counts),
        "translation_note_filter": note_counts,
        "included_translation_note_refs": len(notes),
        "included_translation_note_total": included_note_total,
        "crossrefs": crossref_diag,
        "logos_docx": vars(logos_stats),
        "proofreading_docx": vars(proof_stats),
        "validations": validations,
        "outputs": output_paths,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--footnotes", type=Path, default=DEFAULT_FOOTNOTES)
    parser.add_argument("--logos-docx", type=Path, default=DEFAULT_LOGOS_DOCX)
    parser.add_argument("--proof-docx", type=Path, default=DEFAULT_PROOF_DOCX)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--preview", type=Path, default=DEFAULT_PREVIEW)
    parser.add_argument("--datatype", default="Bible")
    args = parser.parse_args()

    verses = load_verses(args.source)
    notes, note_counts = load_translation_notes(args.footnotes)
    crossrefs, crossref_diag = build_crossrefs_for_verses(verses)

    logos_stats = build_docx(
        path=args.logos_docx,
        title="Fresh Translation OT - Logos Bible Source",
        verses=verses,
        translation_notes=notes,
        crossrefs=crossrefs,
        logos=True,
        datatype=args.datatype,
    )
    proof_stats = build_docx(
        path=args.proof_docx,
        title="Fresh Translation OT - Proofreading Copy",
        verses=verses,
        translation_notes=notes,
        crossrefs=crossrefs,
        logos=False,
        datatype=args.datatype,
    )
    build_preview(args.preview, verses, notes, crossrefs)
    build_readme(
        args.readme,
        logos_docx=args.logos_docx,
        proof_docx=args.proof_docx,
        diagnostics_path=args.diagnostics,
        preview_path=args.preview,
        datatype=args.datatype,
    )
    validations = [validate_docx(args.logos_docx), validate_docx(args.proof_docx)]
    diagnostics = build_diagnostics(
        verses=verses,
        note_counts=note_counts,
        notes=notes,
        crossref_diag=crossref_diag,
        logos_stats=logos_stats,
        proof_stats=proof_stats,
        validations=validations,
        output_paths={
            "logos_docx": str(args.logos_docx),
            "proof_docx": str(args.proof_docx),
            "diagnostics": str(args.diagnostics),
            "readme": str(args.readme),
            "preview": str(args.preview),
        },
        datatype=args.datatype,
    )
    args.diagnostics.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(diagnostics["outputs"], indent=2))


if __name__ == "__main__":
    main()
