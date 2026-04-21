#!/usr/bin/env python3
"""Build Logos Personal Book and proofreading DOCX files for the fresh OT."""

from __future__ import annotations

import argparse
import csv
import html
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
        TSK_OT_BOOKS,
        TSK_ZIP,
        build_tsk_index_map,
        canonicalize_cross_references,
        decode_tsk_blob,
        extract_tsk_crossrefs,
        load_kjv_versification,
        parse_brenton_usfm,
        parse_openbible_crossrefs,
        parse_tsk_module,
    )
except ImportError:  # pragma: no cover - supports module execution from repo root.
    from scripts.build_study_bible import (
        OPENBIBLE_BOOK_MAP,
        STANDARD_BOOK_NAMES,
        TSK_OT_BOOKS,
        TSK_ZIP,
        build_tsk_index_map,
        canonicalize_cross_references,
        decode_tsk_blob,
        extract_tsk_crossrefs,
        load_kjv_versification,
        parse_brenton_usfm,
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
DEFAULT_PROPER_NAMES = DATA / "proper_names.csv"
DEFAULT_NAMES_OF_GOD = DATA / "names_of_god.csv"
DEFAULT_LOGOS_DOCX = OUTPUT / "fresh_translation_ot_logos_bible.docx"
DEFAULT_MT_BRIDGE_DOCX = OUTPUT / "fresh_translation_ot_logos_bible_mt_notes.docx"
DEFAULT_PROOF_DOCX = OUTPUT / "fresh_translation_ot_proofreading.docx"
DEFAULT_DIAGNOSTICS = OUTPUT / "fresh_translation_ot_logos_bible_diagnostics.json"
DEFAULT_README = OUTPUT / "README.md"
DEFAULT_PREVIEW = OUTPUT / "fresh_translation_ot_logos_bible_preview.md"
DEFAULT_VERSIFICATION_MAP = DATA / "versification" / "lxx_to_eng_map.json"
DEFAULT_LEXHAM_TEXTUAL_NOTES_HTML = Path.home() / "Desktop" / "The Lexham Textual Notes on the Bible.html"
LEXHAM_TEXTUAL_NOTES_RESOURCE_ID = "lexcontxtntbbl"

DOCX_W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
DOCX_R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CONTENT_TYPES_NS = "http://schemas.openxmlformats.org/package/2006/content-types"

LXX_TSK_CODE_MAP = {
    "DAN": "DAG",
    "EST": "ESG",
}

LOGOS_SOURCE_CODE_MAP = LXX_TSK_CODE_MAP
STANDARD_CODE_BY_BOOK_NAME = {name: code for code, name in STANDARD_BOOK_NAMES.items()}
STANDARD_CODE_BY_BOOK_NAME["Song of Songs"] = "SNG"

CODE_REF_RE = re.compile(r"^([1-3]?[A-Z0-9]+) (\d+):(\d+)$")
DISPLAY_REF_RE = re.compile(r"^(.+?) (\d+):(\d+)$")

GENERIC_FOOTNOTE_PATTERNS = (
    "Brenton differs here. The translation follows the current fresh wording at this verse numbering point.",
)

MT_LXX_DIFFERENCE_RE = re.compile(
    r"\b(?:Masoretic|MT|Hebrew[- ](?:aligned|based)|Hebrew wording|Hebrew text|"
    r"other textual stream|another textual stream|different textual stream|textual tradition)\b",
    flags=re.I,
)

MAX_PHRASE_ANCHOR_CHARS = 120
TSK_PARAGRAPH_RE = re.compile(
    r'<lb type="x-begin-paragraph"/>(.*?)<lb type="x-end-paragraph"/>',
    flags=re.S,
)
TSK_CATCHWORD_RE = re.compile(r'<hi type="italic">(.*?)</hi>', flags=re.S)
ANCHOR_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "for",
    "he",
    "in",
    "is",
    "it",
    "nor",
    "of",
    "on",
    "or",
    "she",
    "the",
    "they",
    "to",
    "was",
    "were",
}


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
        if self.note_type == "mt_lxx":
            prefix = "MT/LXX note"
        elif self.note_type == "textual":
            prefix = "Textual note"
        else:
            prefix = "Translation note"
        basis = f" Source: {self.source_basis}." if self.source_basis else ""
        return f"{prefix}: {self.text}{basis}"


@dataclass(frozen=True)
class CrossReferenceNote:
    trigger_phrase: str
    refs: tuple[str, ...]
    source: str

    @property
    def display_text(self) -> str:
        prefix = (
            f'Cross-references for "{self.trigger_phrase}": '
            if self.trigger_phrase
            else "Cross-references: "
        )
        return prefix + "; ".join(self.refs) + "."


@dataclass(frozen=True)
class NameMeaningNote:
    trigger_phrase: str
    text: str
    note_type: str
    case_sensitive: bool = True

    @property
    def display_text(self) -> str:
        return self.text


@dataclass(frozen=True)
class SupplementalNote:
    text: str
    source: str

    @property
    def display_text(self) -> str:
        return self.text


@dataclass(frozen=True)
class FootnoteEntry:
    text: str
    custom_mark: str | None = None


@dataclass
class BuildStats:
    output_kind: str
    milestone_mode: str = "lxx"
    paragraph_count: int = 0
    footnote_count: int = 0
    crossref_footnotes: int = 0
    translation_note_footnotes: int = 0
    section_break_count: int = 0
    footnote_number_restart: str = "chapter"
    crossref_marker_restart: str = "chapter"
    phrase_anchored_translation_notes: int = 0
    verse_anchored_translation_notes: int = 0
    name_meaning_footnotes: int = 0
    supplemental_note_footnotes: int = 0
    brenton_supplemental_footnotes: int = 0
    lexham_link_footnotes: int = 0
    phrase_anchored_name_meaning_notes: int = 0
    verse_anchored_name_meaning_notes: int = 0
    phrase_anchored_crossref_notes: int = 0
    verse_anchored_crossref_notes: int = 0
    custom_marked_crossref_notes: int = 0
    max_crossref_marker_index_in_chapter: int = 0
    mapped_milestone_refs: int = 0
    fallback_milestone_refs: int = 0
    duplicate_milestone_refs: int = 0


@dataclass(frozen=True)
class MilestoneResolution:
    logos_ref: str
    source_ref: str
    mapped_ref: str
    status: str


class MinimalDocx:
    """Small WordprocessingML writer with real footnote support."""

    def __init__(self, title: str, subject: str) -> None:
        self.title = title
        self.subject = subject
        self.body: list[str] = []
        self.footnotes: list[FootnoteEntry] = []

    def add_paragraph(
        self,
        runs: Iterable[str],
        style: str = "Normal",
        *,
        section_break_after: bool = False,
    ) -> None:
        ppr_parts: list[str] = []
        if style != "Normal":
            ppr_parts.append(f'<w:pStyle w:val="{attr(style)}"/>')
        if section_break_after:
            ppr_parts.append(section_properties_xml(section_type="continuous"))
        ppr = f"<w:pPr>{''.join(ppr_parts)}</w:pPr>" if ppr_parts else ""
        self.body.append(f"<w:p>{ppr}{''.join(runs)}</w:p>")

    def add_heading(self, text: str, level: int = 1, *, section_break_after: bool = False) -> None:
        style = "Heading1" if level == 1 else "Heading2"
        self.add_paragraph([run(text)], style=style, section_break_after=section_break_after)

    def add_page_break(self) -> None:
        self.body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    def add_footnote(self, text: str, *, custom_mark: str | None = None) -> int:
        self.footnotes.append(FootnoteEntry(text=text, custom_mark=custom_mark))
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
            "word/settings.xml": settings_xml(),
            "word/footnotes.xml": footnotes_xml,
        }
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for name, payload in files.items():
                zf.writestr(name, payload)


def attr(text: str) -> str:
    return escape(str(text), {'"': "&quot;"})


def text(text_value: str) -> str:
    return escape(str(text_value))


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalize_note_ref(ref: str) -> str:
    ref = normalize_space(ref)
    if ref.startswith("Psalm "):
        return "Psalms " + ref.removeprefix("Psalm ")
    return ref


def find_trigger_span(
    verse_text: str,
    trigger: str,
    *,
    case_sensitive: bool = False,
) -> tuple[int, int] | None:
    trigger = trigger.strip()
    if not trigger:
        return None
    haystack = verse_text if case_sensitive else verse_text.casefold()
    needle = trigger if case_sensitive else trigger.casefold()
    start = haystack.find(needle)
    while start >= 0:
        end = start + len(trigger)
        before = verse_text[start - 1] if start > 0 else ""
        after = verse_text[end] if end < len(verse_text) else ""
        starts_word = trigger[0].isalnum()
        ends_word = trigger[-1].isalnum()
        if (
            (not starts_word or not before.isalnum())
            and (not ends_word or not after.isalnum())
        ):
            return start, end
        start = haystack.find(needle, start + 1)
    return None


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


def footnote_reference_style_xml() -> str:
    return '<w:rPr><w:rStyle w:val="FootnoteReference"/></w:rPr>'


def footnote_ref_run(note_id: int, *, custom_mark: str | None = None) -> str:
    if custom_mark:
        return (
            f'<w:r>{footnote_reference_style_xml()}'
            f'<w:footnoteReference w:customMarkFollows="1" w:id="{note_id}"/></w:r>'
            f'<w:r>{footnote_reference_style_xml()}<w:t>{text(custom_mark)}</w:t></w:r>'
        )
    return (
        f'<w:r>{footnote_reference_style_xml()}'
        f'<w:footnoteReference w:id="{note_id}"/></w:r>'
    )


def alphabetic_marker(index: int) -> str:
    if index < 1:
        raise ValueError(f"Cross-reference marker index must be positive: {index}")
    letters: list[str] = []
    value = index
    while value:
        value, remainder = divmod(value - 1, 26)
        letters.append(chr(ord("a") + remainder))
    return "".join(reversed(letters))


def section_properties_xml(*, section_type: str | None = None) -> str:
    section_type_xml = f'<w:type w:val="{attr(section_type)}"/>' if section_type else ""
    return (
        "<w:sectPr>"
        '<w:footnotePr><w:numRestart w:val="eachSect"/><w:numFmt w:val="decimal"/></w:footnotePr>'
        f"{section_type_xml}"
        '<w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080" '
        'w:header="720" w:footer="720" w:gutter="0"/>'
        "</w:sectPr>"
    )


def build_document_xml(body_xml: str) -> str:
    section = section_properties_xml()
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<w:document xmlns:w="{DOCX_W_NS}" xmlns:r="{DOCX_R_NS}">'
        f"<w:body>{body_xml}{section}</w:body></w:document>"
    )


def build_footnotes_xml(notes: list[FootnoteEntry]) -> str:
    items = [
        '<w:footnote w:type="separator" w:id="-1"><w:p><w:r><w:separator/></w:r></w:p></w:footnote>',
        '<w:footnote w:type="continuationSeparator" w:id="0"><w:p><w:r><w:continuationSeparator/></w:r></w:p></w:footnote>',
    ]
    for index, note in enumerate(notes, start=1):
        if note.custom_mark:
            marker_run = (
                f'<w:r>{footnote_reference_style_xml()}'
                f'<w:t>{text(note.custom_mark)}</w:t></w:r>'
            )
        else:
            marker_run = (
                f'<w:r>{footnote_reference_style_xml()}'
                "<w:footnoteRef/></w:r>"
            )
        items.append(
            f'<w:footnote w:id="{index}">'
            '<w:p><w:pPr><w:pStyle w:val="FootnoteText"/></w:pPr>'
            f"{marker_run}"
            f'<w:r><w:t xml:space="preserve"> {text(note.text)}</w:t></w:r>'
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
        '<Override PartName="/word/settings.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>'
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
        '<Relationship Id="rId3" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" '
        'Target="settings.xml"/>'
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


def settings_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<w:settings xmlns:w="{DOCX_W_NS}">'
        '<w:footnotePr><w:numRestart w:val="eachSect"/><w:numFmt w:val="decimal"/></w:footnotePr>'
        "</w:settings>"
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
        display_note_type = "mt_lxx" if is_mt_lxx_difference_note(row) else note_type
        note = TranslationNote(
            ref=row["ref"].strip(),
            note_type=display_note_type,
            trigger_phrase=row.get("trigger_phrase", "").strip(),
            text=body,
            source_basis=row.get("source_basis", "").strip(),
        )
        grouped[note.ref].append(note)
        counts["included"] += 1
        if display_note_type == "mt_lxx":
            counts["included_mt_lxx_difference_notes"] += 1
    return dict(grouped), dict(counts)


def load_name_meaning_notes(
    *,
    proper_names_path: Path,
    names_of_god_path: Path,
) -> tuple[dict[str, list[NameMeaningNote]], dict[str, int]]:
    grouped: dict[str, list[NameMeaningNote]] = defaultdict(list)
    counts = Counter()
    if proper_names_path.exists():
        with proper_names_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                counts["proper_name_rows"] += 1
                ref = normalize_note_ref(row.get("first_reference", ""))
                name = normalize_space(row.get("name", ""))
                transliteration = normalize_space(row.get("transliteration", ""))
                meaning = normalize_space(row.get("meaning", ""))
                note = normalize_space(row.get("footnote", ""))
                if not ref or not name:
                    counts["proper_name_skipped"] += 1
                    continue
                pieces = [f"Name meaning: {name}"]
                if transliteration:
                    pieces[-1] += f" ({transliteration})"
                if meaning:
                    pieces[-1] += f" — {meaning}."
                else:
                    pieces[-1] += "."
                if note:
                    pieces.append(note)
                grouped[ref].append(
                    NameMeaningNote(
                        trigger_phrase=name,
                        text=" ".join(pieces),
                        note_type="proper_name",
                        case_sensitive=True,
                    )
                )
                counts["proper_name_included"] += 1
    if names_of_god_path.exists():
        raw = names_of_god_path.read_text(encoding="utf-8").replace("“", '"').replace("”", '"')
        reader = csv.DictReader(raw.splitlines())
        for row in reader:
            counts["name_of_god_rows"] += 1
            ref = normalize_note_ref(row.get("first_reference", ""))
            lemma = normalize_space(row.get("lemma", ""))
            transliteration = normalize_space(row.get("transliteration", ""))
            meaning = normalize_space(row.get("meaning", ""))
            renderings = normalize_space(row.get("english_renderings", ""))
            note = normalize_space(row.get("footnote", ""))
            if not ref or not (transliteration or lemma or renderings):
                counts["name_of_god_skipped"] += 1
                continue
            label = transliteration or lemma or renderings
            pieces = [f"Divine name/title: {label}"]
            if lemma:
                pieces[-1] += f" ({lemma})"
            if meaning:
                pieces[-1] += f" — {meaning}."
            else:
                pieces[-1] += "."
            if renderings:
                pieces.append(f"Common English rendering: {renderings}.")
            if note:
                pieces.append(note)
            trigger = renderings.split(";", 1)[0].split(",", 1)[0].strip() or label
            grouped[ref].append(
                NameMeaningNote(
                    trigger_phrase=trigger,
                    text=" ".join(pieces),
                    note_type="divine_name",
                    case_sensitive=True,
                )
            )
            counts["name_of_god_included"] += 1
    counts["included"] = counts["proper_name_included"] + counts["name_of_god_included"]
    counts["refs"] = len(grouped)
    return dict(grouped), dict(counts)


def is_chapter_scannable_name_note(note: NameMeaningNote) -> bool:
    if note.note_type != "divine_name":
        return True
    # Single-word divine renderings are too ambiguous to infer from English alone
    # (for example, "God" could represent several source-language forms).
    return len(note.trigger_phrase.split()) > 1


def place_name_meaning_notes_by_chapter(
    verses: list[Verse],
    source_notes: dict[str, list[NameMeaningNote]],
) -> tuple[dict[str, list[NameMeaningNote]], dict[str, int]]:
    verse_refs = {verse.ref for verse in verses}
    placed: dict[str, list[NameMeaningNote]] = defaultdict(list)
    counts = Counter()
    scannable_notes: list[NameMeaningNote] = []

    for source_ref, notes in source_notes.items():
        if source_ref not in verse_refs:
            counts["skipped_missing_source_ref"] += len(notes)
            continue
        for note in notes:
            if is_chapter_scannable_name_note(note):
                scannable_notes.append(note)
                counts["chapter_scannable_source_notes"] += 1
            else:
                placed[source_ref].append(note)
                counts["source_ref_anchored_ambiguous_divine_notes"] += 1

    seen_in_chapter: set[tuple[str, int, str]] = set()
    for verse in verses:
        chapter_key = (verse.book_name, verse.chapter)
        for note in scannable_notes:
            seen_key = (*chapter_key, note.display_text)
            if seen_key in seen_in_chapter:
                continue
            if find_trigger_span(
                verse.text,
                note.trigger_phrase,
                case_sensitive=note.case_sensitive,
            ):
                placed[verse.ref].append(note)
                seen_in_chapter.add(seen_key)
                counts["chapter_first_occurrence_notes"] += 1

    counts["placed_refs"] = len(placed)
    counts["placed_total"] = sum(len(notes) for notes in placed.values())
    counts["chapters_scanned"] = len({(verse.book_name, verse.chapter) for verse in verses})
    return dict(placed), dict(counts)


def is_generic_or_brenton_only_note(row: dict[str, str]) -> bool:
    body = row.get("footnote_text", "").strip()
    if any(body == pattern for pattern in GENERIC_FOOTNOTE_PATTERNS):
        return True
    source = row.get("source_basis", "").strip().lower()
    return source == "translation comparison" and body.startswith("Brenton differs here.")


def is_mt_lxx_difference_note(row: dict[str, str]) -> bool:
    haystack = f"{row.get('footnote_text', '')} {row.get('source_basis', '')}"
    return bool(MT_LXX_DIFFERENCE_RE.search(haystack))


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_versification_map(path: Path) -> tuple[dict[str, str], dict[str, object]]:
    if not path.exists():
        return {}, {"present": False, "path": str(path), "mapped_refs": 0}
    payload = json.loads(path.read_text(encoding="utf-8"))
    mapped_refs = payload.get("mapped_refs", {})
    if not isinstance(mapped_refs, dict):
        raise ValueError(f"Invalid versification map payload: {path}")
    return {str(key): str(value) for key, value in mapped_refs.items()}, {
        "present": True,
        "path": str(path),
        "source": payload.get("source", ""),
        "source_url": payload.get("source_url", ""),
        "license": payload.get("license", ""),
        "mapped_refs": len(mapped_refs),
    }


def source_code_ref(verse: Verse) -> str:
    code = LOGOS_SOURCE_CODE_MAP.get(verse.book_code, verse.book_code)
    return f"{code} {verse.chapter}:{verse.verse}"


def parse_code_ref(ref: str) -> tuple[str, int, int] | None:
    match = CODE_REF_RE.match(ref)
    if not match:
        return None
    code, chapter, verse = match.groups()
    return code, int(chapter), int(verse)


def display_ref_to_code_ref(ref: str) -> str | None:
    normalized = normalize_note_ref(ref)
    match = DISPLAY_REF_RE.match(normalized)
    if not match:
        return None
    book_name, chapter, verse = match.groups()
    code = STANDARD_CODE_BY_BOOK_NAME.get(book_name)
    if not code:
        return None
    return f"{code} {int(chapter)}:{int(verse)}"


def validation_code(code: str) -> str:
    return LXX_TSK_CODE_MAP.get(code, code)


def is_valid_standard_ref(ref: str, verse_counts: dict[str, list[int]]) -> bool:
    parsed = parse_code_ref(ref)
    if not parsed:
        return False
    code, chapter, verse = parsed
    chapters = verse_counts.get(validation_code(code), [])
    return 1 <= chapter <= len(chapters) and 1 <= verse <= int(chapters[chapter - 1])


def clamp_to_standard_ref(ref: str, verse_counts: dict[str, list[int]]) -> str | None:
    parsed = parse_code_ref(ref)
    if not parsed:
        return None
    code, chapter, verse = parsed
    chapters = verse_counts.get(validation_code(code), [])
    if not chapters:
        return None
    chapter = min(max(chapter, 1), len(chapters))
    verse = min(max(verse, 1), int(chapters[chapter - 1]))
    return f"{code} {chapter}:{verse}"


def logos_ref_from_code_ref(ref: str) -> str:
    parsed = parse_code_ref(ref)
    if not parsed:
        raise ValueError(f"Invalid code reference: {ref}")
    code, chapter, verse = parsed
    return f"{STANDARD_BOOK_NAMES.get(validation_code(code), code)} {chapter}:{verse}"


def resolve_milestone(
    verse: Verse,
    *,
    mode: str,
    versification_map: dict[str, str],
    verse_counts: dict[str, list[int]],
) -> MilestoneResolution:
    source_ref = source_code_ref(verse)
    if mode == "lxx":
        return MilestoneResolution(verse.logos_ref, source_ref, source_ref, "lxx")
    if mode != "mt":
        raise ValueError(f"Unsupported milestone mode: {mode}")

    mapped_ref = versification_map.get(source_ref, source_ref)
    status = "mapped" if mapped_ref != source_ref else "identity"
    if not is_valid_standard_ref(mapped_ref, verse_counts):
        clamped_ref = clamp_to_standard_ref(mapped_ref, verse_counts)
        if clamped_ref:
            mapped_ref = clamped_ref
            status = "fallback"
        else:
            mapped_ref = source_ref
            status = "unmapped"
    return MilestoneResolution(logos_ref_from_code_ref(mapped_ref), source_ref, mapped_ref, status)


def logos_book_name(book_code: str, fallback: str) -> str:
    name = STANDARD_BOOK_NAMES.get(LXX_TSK_CODE_MAP.get(book_code, book_code), fallback)
    if book_code == "DAN":
        return "Daniel"
    if book_code == "EST":
        return "Esther"
    return name


def clean_tsk_markup(fragment: str) -> str:
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    fragment = re.sub(r"\s+", " ", fragment)
    return fragment.strip(" ;,")


def should_anchor_crossref_trigger(trigger: str) -> bool:
    if not trigger or len(trigger) > MAX_PHRASE_ANCHOR_CHARS:
        return False
    words = re.findall(r"[A-Za-z0-9]+", trigger.casefold())
    if not words:
        return False
    if len(words) == 1 and (len(words[0]) < 4 or words[0] in ANCHOR_STOPWORDS):
        return False
    return True


def extract_tsk_crossref_groups(raw_text: str) -> list[CrossReferenceNote]:
    groups: list[CrossReferenceNote] = []
    blocks = TSK_PARAGRAPH_RE.findall(raw_text)
    if not blocks:
        blocks = [raw_text]
    for block in blocks:
        refs, _note_text = extract_tsk_crossrefs(block)
        cleaned_refs = tuple(canonicalize_cross_references(refs))
        if not cleaned_refs:
            continue
        catchword_match = TSK_CATCHWORD_RE.search(block)
        trigger = clean_tsk_markup(catchword_match.group(1)) if catchword_match else ""
        if not should_anchor_crossref_trigger(trigger):
            trigger = ""
        groups.append(CrossReferenceNote(trigger_phrase=trigger, refs=cleaned_refs, source="tsk"))
    return groups


def parse_tsk_crossref_groups() -> tuple[dict[tuple[str, int, int], list[CrossReferenceNote]], dict[str, object]]:
    diagnostics: dict[str, object] = {
        "archive_present": TSK_ZIP.exists(),
        "status": "unparsed",
    }
    if not TSK_ZIP.exists():
        diagnostics["reason"] = "TSK archive not found."
        return {}, diagnostics
    verse_counts = load_kjv_versification()
    if not verse_counts:
        diagnostics["reason"] = "KJV versification data not found."
        return {}, diagnostics

    index_map = build_tsk_index_map(TSK_OT_BOOKS, verse_counts)
    grouped: dict[tuple[str, int, int], list[CrossReferenceNote]] = defaultdict(list)
    with zipfile.ZipFile(TSK_ZIP) as zf:
        base = "modules/comments/zcom/tsk/ot"
        bzv = zf.read(f"{base}.bzv")
        bzs = zf.read(f"{base}.bzs")
        bzz = zf.read(f"{base}.bzz")
        diagnostics["ot_entries"] = len(bzv) // 10
        blob_cache: dict[int, bytes] = {}
        for index in range(len(bzv) // 10):
            verse_key = index_map.get(index)
            if not verse_key:
                continue
            raw_text = decode_tsk_blob(bzv, bzs, bzz, index, blob_cache)
            if not raw_text:
                continue
            groups = extract_tsk_crossref_groups(raw_text)
            if groups:
                grouped[verse_key].extend(groups)

    diagnostics["status"] = "parsed"
    diagnostics["verses_with_refs"] = len(grouped)
    diagnostics["crossref_groups"] = sum(len(items) for items in grouped.values())
    diagnostics["phrase_anchor_candidates"] = sum(
        1 for items in grouped.values() for item in items if item.trigger_phrase
    )
    diagnostics["total_crossrefs"] = sum(len(item.refs) for items in grouped.values() for item in items)
    return dict(grouped), diagnostics


def build_crossrefs_for_verses(verses: list[Verse]) -> tuple[dict[str, list[CrossReferenceNote]], dict[str, object]]:
    tsk_refs, tsk_diag = parse_tsk_crossref_groups()
    open_refs, open_diag = parse_openbible_crossrefs(limit_per_verse=9999)
    by_ref: dict[str, list[CrossReferenceNote]] = {}
    source_counts = Counter()
    total_refs = 0
    total_groups = 0
    for verse in verses:
        notes = tsk_refs.get(verse.tsk_key, [])
        if notes:
            source_counts["tsk"] += 1
        else:
            refs = open_refs.get(verse.tsk_key, [])
            if refs:
                source_counts["openbible_fallback"] += 1
                cleaned = tuple(canonicalize_cross_references([format_openbible_ref(ref) for ref in refs]))
                notes = [CrossReferenceNote(trigger_phrase="", refs=cleaned, source="openbible")]
        notes = [note for note in notes if note.refs]
        if notes:
            by_ref[verse.ref] = notes
            total_groups += len(notes)
            total_refs += sum(len(note.refs) for note in notes)
    return by_ref, {
        "source_counts": dict(source_counts),
        "verses_with_crossrefs": len(by_ref),
        "crossref_note_groups": total_groups,
        "total_crossrefs_after_canonicalization": total_refs,
        "tsk": tsk_diag,
        "openbible": open_diag,
    }


OPENBIBLE_TARGET_RE = re.compile(
    r"^([1-3]?[A-Za-z]+)\.(\d+)\.(\d+)(?:-([1-3]?[A-Za-z]+)\.(\d+)\.(\d+))?(?: \((\d+)\))?$"
)
LEXHAM_REF_LINK_RE = re.compile(
    r'<a\s+href="https://ref\.ly/([^"]+)"[^>]*>\s*'
    r'<span[^>]*font-weight\s*:\s*bold[^>]*>(.*?)</span>\s*</a>',
    flags=re.I | re.S,
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


def strip_html_text(raw: str) -> str:
    return normalize_space(html.unescape(re.sub(r"<[^>]+>", " ", raw)))


def add_supplemental_note(
    grouped: dict[str, list[SupplementalNote]],
    *,
    ref: str,
    text_value: str,
    source: str,
    verse_refs: set[str],
    seen: set[tuple[str, str]],
    counts: Counter[str],
) -> None:
    normalized_ref = normalize_note_ref(ref)
    normalized_text = normalize_space(text_value)
    if not normalized_ref or normalized_ref not in verse_refs:
        counts[f"{source}_skipped_missing_ref"] += 1
        return
    if not normalized_text:
        counts[f"{source}_skipped_empty"] += 1
        return
    dedupe_key = (normalized_ref, normalized_text)
    if dedupe_key in seen:
        counts[f"{source}_skipped_duplicate"] += 1
        return
    seen.add(dedupe_key)
    grouped[normalized_ref].append(SupplementalNote(text=normalized_text, source=source))
    counts[f"{source}_included"] += 1


def load_brenton_supplemental_notes(
    verses: list[Verse],
) -> tuple[dict[str, list[SupplementalNote]], dict[str, object]]:
    verse_refs = {verse.ref for verse in verses}
    verse_refs_by_tsk_key: dict[tuple[str, int, int], list[str]] = defaultdict(list)
    for verse in verses:
        verse_refs_by_tsk_key[verse.tsk_key].append(verse.ref)

    grouped: dict[str, list[SupplementalNote]] = defaultdict(list)
    counts: Counter[str] = Counter()
    seen: set[tuple[str, str]] = set()

    brenton_records, brenton_diag = parse_brenton_usfm()
    counts["brenton_verse_records"] = len(brenton_records)
    for record in brenton_records:
        for footnote in record.footnotes:
            add_supplemental_note(
                grouped,
                ref=record.ref,
                text_value=f"Brenton note: {footnote}",
                source="brenton_footnote",
                verse_refs=verse_refs,
                seen=seen,
                counts=counts,
            )

    _tsk_crossrefs, tsk_notes, tsk_diag = parse_tsk_module()
    counts["tsk_note_source_refs"] = len(tsk_notes)
    for tsk_key, note_items in tsk_notes.items():
        target_refs = verse_refs_by_tsk_key.get(tsk_key, [])
        if not target_refs:
            counts["tsk_study_note_skipped_missing_ref"] += len(note_items)
            continue
        for ref in target_refs:
            for note_item in note_items:
                add_supplemental_note(
                    grouped,
                    ref=ref,
                    text_value=f"TSK study note: {note_item}",
                    source="tsk_study_note",
                    verse_refs=verse_refs,
                    seen=seen,
                    counts=counts,
                )

    return dict(grouped), {
        **dict(counts),
        "brenton_usfm": brenton_diag,
        "tsk": tsk_diag,
        "included_refs": len(grouped),
        "included_total": sum(len(items) for items in grouped.values()),
    }


def load_lexham_textual_note_links(
    path: Path,
    verses: list[Verse],
    versification_map: dict[str, str],
) -> tuple[dict[str, list[SupplementalNote]], dict[str, object]]:
    verse_refs = {verse.ref for verse in verses}
    standard_refs_to_source_refs: dict[str, list[str]] = defaultdict(list)
    for verse in verses:
        source_ref = source_code_ref(verse)
        standard_ref = versification_map.get(source_ref, source_ref)
        standard_refs_to_source_refs[standard_ref].append(verse.ref)
    grouped: dict[str, list[SupplementalNote]] = defaultdict(list)
    counts: Counter[str] = Counter({"present": int(path.exists())})
    seen: set[tuple[str, str]] = set()
    if not path.exists():
        return {}, {
            "present": False,
            "path": str(path),
            "included_refs": 0,
            "included_total": 0,
        }

    raw_html = path.read_text(encoding="utf-8", errors="replace")
    matches = LEXHAM_REF_LINK_RE.findall(raw_html)
    counts["source_links"] = len(matches)
    for refly_code, display_ref_raw in matches:
        display_ref = strip_html_text(display_ref_raw)
        target_refs = [normalize_note_ref(display_ref)] if normalize_note_ref(display_ref) in verse_refs else []
        if not target_refs:
            code_ref = display_ref_to_code_ref(display_ref)
            target_refs = standard_refs_to_source_refs.get(code_ref or "", [])
            if target_refs:
                counts["lexham_link_matched_by_versification_map"] += 1
        if not target_refs:
            counts["lexham_link_skipped_missing_ref"] += 1
            continue
        target = f"logosres:{LEXHAM_TEXTUAL_NOTES_RESOURCE_ID};ref=Bible.{refly_code.strip()}"
        note_text = (
            "Lexham textual note: "
            f"[[Open LTNB >> {target}]]. "
            "Requires a Logos license for The Lexham Textual Notes on the Bible."
        )
        for target_ref in target_refs:
            add_supplemental_note(
                grouped,
                ref=target_ref,
                text_value=note_text,
                source="lexham_link",
                verse_refs=verse_refs,
                seen=seen,
                counts=counts,
            )

    return dict(grouped), {
        **dict(counts),
        "present": True,
        "path": str(path),
        "resource_id": LEXHAM_TEXTUAL_NOTES_RESOURCE_ID,
        "included_refs": len(grouped),
        "included_total": sum(len(items) for items in grouped.values()),
    }


def merge_supplemental_notes(
    *note_maps: dict[str, list[SupplementalNote]],
) -> dict[str, list[SupplementalNote]]:
    merged: dict[str, list[SupplementalNote]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    for note_map in note_maps:
        for ref, notes in note_map.items():
            for note in notes:
                key = (ref, note.display_text)
                if key in seen:
                    continue
                seen.add(key)
                merged[ref].append(note)
    return dict(merged)


class CrossReferenceMarkerState:
    def __init__(self) -> None:
        self.index = 0

    def reset(self) -> None:
        self.index = 0

    def next_marker(self) -> tuple[str, int]:
        self.index += 1
        return alphabetic_marker(self.index), self.index


def build_docx(
    *,
    path: Path,
    title: str,
    verses: list[Verse],
    translation_notes: dict[str, list[TranslationNote]],
    name_notes: dict[str, list[NameMeaningNote]],
    supplemental_notes: dict[str, list[SupplementalNote]],
    crossrefs: dict[str, list[CrossReferenceNote]],
    logos: bool,
    datatype: str,
    milestone_mode: str = "lxx",
    versification_map: dict[str, str] | None = None,
    verse_counts: dict[str, list[int]] | None = None,
    footnote_number_restart: str = "chapter",
) -> BuildStats:
    doc = MinimalDocx(
        title=title,
        subject="Fresh OT translation draft with translation notes and cross-references",
    )
    stats = BuildStats(
        output_kind="logos" if logos else "proofreading",
        milestone_mode=milestone_mode,
        footnote_number_restart=footnote_number_restart,
    )
    add_title_page(
        doc,
        title,
        logos=logos,
        datatype=datatype,
        milestone_mode=milestone_mode,
        footnote_number_restart=footnote_number_restart,
    )

    current_book = ""
    current_chapter = -1
    crossref_markers = CrossReferenceMarkerState()
    milestone_ref_counts: Counter[str] = Counter()
    versification_map = versification_map or {}
    verse_counts = verse_counts or {}
    for verse in verses:
        if verse.book_name != current_book:
            current_book = verse.book_name
            current_chapter = -1
            if stats.paragraph_count:
                doc.add_page_break()
            book_section_break = footnote_number_restart == "book"
            doc.add_heading(verse.book_name, level=1, section_break_after=book_section_break)
            if book_section_break:
                stats.section_break_count += 1
            stats.paragraph_count += 1
        if verse.chapter != current_chapter:
            current_chapter = verse.chapter
            crossref_markers.reset()
            chapter_section_break = footnote_number_restart == "chapter"
            doc.add_heading(f"Chapter {verse.chapter}", level=2, section_break_after=chapter_section_break)
            if chapter_section_break:
                stats.section_break_count += 1
            stats.paragraph_count += 1

        runs, milestone_ref = build_verse_runs(
            doc=doc,
            verse=verse,
            notes=translation_notes.get(verse.ref, []),
            name_notes=name_notes.get(verse.ref, []),
            supplemental_notes=supplemental_notes.get(verse.ref, []),
            crossref_notes=crossrefs.get(verse.ref, []),
            crossref_markers=crossref_markers,
            logos=logos,
            datatype=datatype,
            milestone_mode=milestone_mode,
            versification_map=versification_map,
            verse_counts=verse_counts,
            stats=stats,
        )
        if logos and milestone_ref:
            milestone_ref_counts[milestone_ref] += 1
        doc.add_paragraph(runs)
        stats.paragraph_count += 1

    stats.footnote_count = len(doc.footnotes)
    stats.duplicate_milestone_refs = sum(count - 1 for count in milestone_ref_counts.values() if count > 1)
    doc.save(path)
    return stats


def add_title_page(
    doc: MinimalDocx,
    title: str,
    *,
    logos: bool,
    datatype: str,
    milestone_mode: str,
    footnote_number_restart: str,
) -> None:
    doc.add_paragraph([run(title)], style="Title")
    subtitle = "Logos Personal Book source" if logos else "Proofreading and print copy"
    doc.add_paragraph([run(subtitle)], style="Subtitle")
    lines = [
        "Fresh Old Testament translation draft.",
        "Includes reviewed translation/textual notes, with MT/LXX difference notes labeled explicitly.",
        "Includes full available cross-reference set from TSK, with OpenBible fallback where TSK has no row.",
        "Includes name-meaning notes at first exact occurrence per chapter.",
        "Includes supplemental Brenton-package notes: Brenton footnotes and TSK study notes.",
        "Hebrew/Greek vocabulary notes are excluded; name/proper-noun meanings remain included separately.",
        f"Regular footnote numbering restarts by {footnote_number_restart}. Cross-reference markers are custom letters and restart by chapter.",
    ]
    if logos:
        lines.append(f"Verse milestones use Logos datatype {datatype}. Compile in Logos as resource type Bible.")
        lines.append("Includes Lexham Textual Notes resource links where the supplied Logos export has a matching verse.")
        if milestone_mode == "mt":
            lines.append("Milestones are remapped to standard English/MT Bible references for Logos note sharing.")
    for line in lines:
        doc.add_paragraph([run(line)])
    doc.add_page_break()


def build_verse_runs(
    *,
    doc: MinimalDocx,
    verse: Verse,
    notes: list[TranslationNote],
    name_notes: list[NameMeaningNote],
    supplemental_notes: list[SupplementalNote],
    crossref_notes: list[CrossReferenceNote],
    crossref_markers: CrossReferenceMarkerState,
    logos: bool,
    datatype: str,
    milestone_mode: str,
    versification_map: dict[str, str],
    verse_counts: dict[str, list[int]],
    stats: BuildStats,
) -> tuple[list[str], str | None]:
    runs: list[str] = []
    milestone_ref: str | None = None
    if logos:
        milestone = resolve_milestone(
            verse,
            mode=milestone_mode,
            versification_map=versification_map,
            verse_counts=verse_counts,
        )
        milestone_ref = milestone.logos_ref
        if milestone.status == "mapped":
            stats.mapped_milestone_refs += 1
        elif milestone.status in {"fallback", "unmapped"}:
            stats.fallback_milestone_refs += 1
        runs.append(run(f"[[@{datatype}:{milestone.logos_ref}]] ", small=True, color="777777"))
    runs.append(run(f"{verse.verse} ", bold=True))
    if logos:
        runs.append(run(" {{field-on:Bible}}"))

    text_runs, verse_level_notes, verse_level_names, verse_level_crossrefs = runs_for_text_with_phrase_notes(
        doc,
        verse.text,
        notes,
        name_notes,
        crossref_notes,
        crossref_markers,
        stats,
    )
    runs.extend(text_runs)
    for note in verse_level_notes:
        note_id = doc.add_footnote(note.display_text)
        runs.append(footnote_ref_run(note_id))
        stats.translation_note_footnotes += 1
        stats.verse_anchored_translation_notes += 1
    for name_note in verse_level_names:
        note_id = doc.add_footnote(name_note.display_text)
        runs.append(footnote_ref_run(note_id))
        stats.name_meaning_footnotes += 1
        stats.verse_anchored_name_meaning_notes += 1
    for supplemental_note in supplemental_notes:
        note_id = doc.add_footnote(supplemental_note.display_text)
        runs.append(footnote_ref_run(note_id))
        stats.supplemental_note_footnotes += 1
        if supplemental_note.source == "lexham_link":
            stats.lexham_link_footnotes += 1
        else:
            stats.brenton_supplemental_footnotes += 1
    for crossref in verse_level_crossrefs:
        note_id, marker = add_crossref_footnote(doc, crossref, crossref_markers, stats)
        runs.append(footnote_ref_run(note_id, custom_mark=marker))
        stats.verse_anchored_crossref_notes += 1
    if logos:
        runs.append(run("{{field-off:Bible}}"))
    return runs, milestone_ref


def add_crossref_footnote(
    doc: MinimalDocx,
    crossref: CrossReferenceNote,
    crossref_markers: CrossReferenceMarkerState,
    stats: BuildStats,
) -> tuple[int, str]:
    marker, index = crossref_markers.next_marker()
    note_id = doc.add_footnote(crossref.display_text, custom_mark=marker)
    stats.crossref_footnotes += 1
    stats.custom_marked_crossref_notes += 1
    stats.max_crossref_marker_index_in_chapter = max(stats.max_crossref_marker_index_in_chapter, index)
    return note_id, marker


def runs_for_text_with_phrase_notes(
    doc: MinimalDocx,
    verse_text: str,
    notes: list[TranslationNote],
    name_notes: list[NameMeaningNote],
    crossrefs: list[CrossReferenceNote],
    crossref_markers: CrossReferenceMarkerState,
    stats: BuildStats,
) -> tuple[list[str], list[TranslationNote], list[NameMeaningNote], list[CrossReferenceNote]]:
    anchors: dict[int, list[tuple[str, TranslationNote | NameMeaningNote | CrossReferenceNote]]] = defaultdict(list)
    verse_level: list[TranslationNote] = []
    verse_level_names: list[NameMeaningNote] = []
    verse_level_crossrefs: list[CrossReferenceNote] = []
    occupied: list[tuple[int, int]] = []

    def is_occupied(start: int, end: int) -> bool:
        return any(not (end <= old_start or start >= old_end) for old_start, old_end in occupied)

    for note in notes:
        trigger = note.trigger_phrase.strip()
        if not trigger or len(trigger) > MAX_PHRASE_ANCHOR_CHARS:
            verse_level.append(note)
            continue
        found = find_trigger_span(verse_text, trigger)
        if not found:
            verse_level.append(note)
            continue
        start, end = found
        if is_occupied(start, end):
            verse_level.append(note)
            continue
        occupied.append((start, end))
        anchors[end].append(("translation", note))

    for name_note in name_notes:
        trigger = name_note.trigger_phrase.strip()
        if not trigger or len(trigger) > MAX_PHRASE_ANCHOR_CHARS:
            verse_level_names.append(name_note)
            continue
        found = find_trigger_span(verse_text, trigger, case_sensitive=name_note.case_sensitive)
        if not found:
            verse_level_names.append(name_note)
            continue
        start, end = found
        if is_occupied(start, end):
            verse_level_names.append(name_note)
            continue
        occupied.append((start, end))
        anchors[end].append(("name", name_note))

    for crossref in crossrefs:
        trigger = crossref.trigger_phrase.strip()
        if not should_anchor_crossref_trigger(trigger):
            verse_level_crossrefs.append(crossref)
            continue
        found = find_trigger_span(verse_text, trigger)
        if not found:
            verse_level_crossrefs.append(crossref)
            continue
        start, end = found
        if is_occupied(start, end):
            verse_level_crossrefs.append(crossref)
            continue
        occupied.append((start, end))
        anchors[end].append(("crossref", crossref))

    output: list[str] = []
    cursor = 0
    for end in sorted(anchors):
        output.append(run(verse_text[cursor:end]))
        for kind, item in anchors[end]:
            if kind == "crossref":
                assert isinstance(item, CrossReferenceNote)
                note_id, marker = add_crossref_footnote(doc, item, crossref_markers, stats)
                output.append(footnote_ref_run(note_id, custom_mark=marker))
                stats.phrase_anchored_crossref_notes += 1
            elif kind == "name":
                note_id = doc.add_footnote(item.display_text)
                output.append(footnote_ref_run(note_id))
                stats.name_meaning_footnotes += 1
                stats.phrase_anchored_name_meaning_notes += 1
            else:
                note_id = doc.add_footnote(item.display_text)
                output.append(footnote_ref_run(note_id))
                stats.translation_note_footnotes += 1
                stats.phrase_anchored_translation_notes += 1
        cursor = end
    output.append(run(verse_text[cursor:]))
    return output, verse_level, verse_level_names, verse_level_crossrefs


def build_preview(
    path: Path,
    verses: list[Verse],
    notes: dict[str, list[TranslationNote]],
    supplemental_notes: dict[str, list[SupplementalNote]],
    refs: dict[str, list[CrossReferenceNote]],
) -> None:
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
            supplemental_count = len(supplemental_notes.get(verse.ref, []))
            crossref_count = sum(len(item.refs) for item in refs.get(verse.ref, []))
            lines.append(f"**{verse.ref}** {verse.text}")
            lines.append(f"- Translation/textual notes: {note_count}")
            lines.append(f"- Supplemental study/textual links: {supplemental_count}")
            lines.append(f"- Cross-references: {crossref_count}")
            lines.append("")
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def build_readme(
    path: Path,
    *,
    logos_docx: Path,
    mt_bridge_docx: Path,
    proof_docx: Path,
    diagnostics_path: Path,
    preview_path: Path,
    datatype: str,
    footnote_number_restart: str,
    lexham_textual_notes_html: Path,
) -> None:
    content = f"""# Fresh Translation OT Logos/Proofreading Files

Generated files:

- `{logos_docx.name}`: Logos Personal Book source. Compile as resource type `Bible`.
- `{mt_bridge_docx.name}`: Logos Personal Book source with verse milestones remapped to standard English/MT references so existing reference-anchored Logos notes from MT-based Bibles can show. Compile as resource type `Bible`.
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

MT-note bridge import:

Use `{mt_bridge_docx.name}` instead of `{logos_docx.name}` when the goal is to surface notes already anchored to standard MT/English Bible references. The visible verse numbers remain from the LXX source rows, but hidden milestones are remapped to standard Bible references where a reliable mapping is available.

Scope:

- Source text: `data/raw/lxx_greek/ot_full.csv`.
- Translation notes: reviewed rows from `data/research/translation_footnotes.csv`. Notes that explicitly mention Masoretic/MT/Hebrew-aligned textual divergence are labeled `MT/LXX note` in the footnotes.
- Name meanings: `data/proper_names.csv` and `data/names_of_god.csv`. Proper-name notes and unambiguous multi-word divine-title notes are placed at the first exact occurrence per chapter. Ambiguous single-word divine-title notes remain source-reference anchored to avoid assigning the wrong source-language title from English alone.
- Supplemental Brenton-package notes: Brenton USFM footnotes and TSK study-note text. Hebrew and Greek vocabulary notes are excluded because Logos already provides lexical lookup layers. Proper-name and divine-title notes are not duplicated here because they are already integrated as name-meaning notes.
- Lexham Textual Notes links: generated from `{lexham_textual_notes_html}` when present. Links use `logosres:{LEXHAM_TEXTUAL_NOTES_RESOURCE_ID};ref=Bible.<ref.ly-code>` and require a Logos license for `The Lexham Textual Notes on the Bible`.
- Cross-references: TSK primary set from `data/raw/TSK.zip`; OpenBible fallback from `data/raw/cross-references.zip` where TSK has no verse row. TSK catchwords are used as word/phrase anchors when they exactly match the fresh translation; otherwise cross-references remain verse-anchored. See root `NOTICE.md` for public-domain/CC-BY attribution details.
- Footnote numbering: one DOCX file with internal Word section metadata set to restart regular visible footnote numbering by `{footnote_number_restart}`. Cross-reference footnotes use custom alphabetic markers (`a`, `b`, `c`, ...), reset at each chapter, so regular translation/name/study notes keep numeric markers.

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
    name_note_counts: dict[str, int],
    name_notes: dict[str, list[NameMeaningNote]],
    supplemental_note_counts: dict[str, object],
    supplemental_notes: dict[str, list[SupplementalNote]],
    crossref_diag: dict[str, object],
    logos_stats: BuildStats,
    mt_bridge_stats: BuildStats,
    proof_stats: BuildStats,
    validations: list[dict[str, object]],
    output_paths: dict[str, str],
    datatype: str,
    versification_map_diag: dict[str, object],
) -> dict[str, object]:
    book_counts = Counter(verse.book_code for verse in verses)
    included_note_total = sum(len(items) for items in notes.values())
    included_name_note_total = sum(len(items) for items in name_notes.values())
    included_supplemental_note_total = sum(len(items) for items in supplemental_notes.values())
    return {
        "datatype": datatype,
        "verse_rows": len(verses),
        "book_count": len(book_counts),
        "book_counts": dict(book_counts),
        "translation_note_filter": note_counts,
        "included_translation_note_refs": len(notes),
        "included_translation_note_total": included_note_total,
        "name_meaning_note_filter": name_note_counts,
        "included_name_meaning_note_refs": len(name_notes),
        "included_name_meaning_note_total": included_name_note_total,
        "supplemental_notes": supplemental_note_counts,
        "included_supplemental_note_refs": len(supplemental_notes),
        "included_supplemental_note_total": included_supplemental_note_total,
        "crossrefs": crossref_diag,
        "versification_map": versification_map_diag,
        "logos_docx": vars(logos_stats),
        "mt_notes_bridge_docx": vars(mt_bridge_stats),
        "proofreading_docx": vars(proof_stats),
        "validations": validations,
        "outputs": output_paths,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--footnotes", type=Path, default=DEFAULT_FOOTNOTES)
    parser.add_argument("--proper-names", type=Path, default=DEFAULT_PROPER_NAMES)
    parser.add_argument("--names-of-god", type=Path, default=DEFAULT_NAMES_OF_GOD)
    parser.add_argument("--logos-docx", type=Path, default=DEFAULT_LOGOS_DOCX)
    parser.add_argument("--mt-bridge-docx", type=Path, default=DEFAULT_MT_BRIDGE_DOCX)
    parser.add_argument("--proof-docx", type=Path, default=DEFAULT_PROOF_DOCX)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--preview", type=Path, default=DEFAULT_PREVIEW)
    parser.add_argument("--versification-map", type=Path, default=DEFAULT_VERSIFICATION_MAP)
    parser.add_argument("--lexham-textual-notes-html", type=Path, default=DEFAULT_LEXHAM_TEXTUAL_NOTES_HTML)
    parser.add_argument("--datatype", default="Bible")
    parser.add_argument(
        "--footnote-number-restart",
        choices=("chapter", "book", "continuous"),
        default="chapter",
        help="Visible footnote numbering restart scope inside the single DOCX file.",
    )
    args = parser.parse_args()

    verses = load_verses(args.source)
    notes, note_counts = load_translation_notes(args.footnotes)
    source_name_notes, name_note_counts = load_name_meaning_notes(
        proper_names_path=args.proper_names,
        names_of_god_path=args.names_of_god,
    )
    name_notes, name_note_placement_counts = place_name_meaning_notes_by_chapter(verses, source_name_notes)
    name_note_counts = {
        **name_note_counts,
        **{f"placement_{key}": value for key, value in name_note_placement_counts.items()},
    }
    crossrefs, crossref_diag = build_crossrefs_for_verses(verses)
    versification_map, versification_map_diag = load_versification_map(args.versification_map)
    brenton_supplemental_notes, brenton_supplemental_counts = load_brenton_supplemental_notes(verses)
    lexham_supplemental_notes, lexham_supplemental_counts = load_lexham_textual_note_links(
        args.lexham_textual_notes_html,
        verses,
        versification_map,
    )
    supplemental_notes = merge_supplemental_notes(brenton_supplemental_notes, lexham_supplemental_notes)
    supplemental_note_counts: dict[str, object] = {
        "brenton_package": brenton_supplemental_counts,
        "lexham_textual_notes": lexham_supplemental_counts,
        "included_refs": len(supplemental_notes),
        "included_total": sum(len(items) for items in supplemental_notes.values()),
    }
    verse_counts = json.loads((DATA / "kjv_versification.json").read_text(encoding="utf-8"))

    logos_stats = build_docx(
        path=args.logos_docx,
        title="Fresh Translation OT - Logos Bible Source",
        verses=verses,
        translation_notes=notes,
        name_notes=name_notes,
        supplemental_notes=supplemental_notes,
        crossrefs=crossrefs,
        logos=True,
        datatype=args.datatype,
        milestone_mode="lxx",
        versification_map=versification_map,
        verse_counts=verse_counts,
        footnote_number_restart=args.footnote_number_restart,
    )
    mt_bridge_stats = build_docx(
        path=args.mt_bridge_docx,
        title="Fresh Translation OT - MT Notes Bridge",
        verses=verses,
        translation_notes=notes,
        name_notes=name_notes,
        supplemental_notes=supplemental_notes,
        crossrefs=crossrefs,
        logos=True,
        datatype=args.datatype,
        milestone_mode="mt",
        versification_map=versification_map,
        verse_counts=verse_counts,
        footnote_number_restart=args.footnote_number_restart,
    )
    proof_stats = build_docx(
        path=args.proof_docx,
        title="Fresh Translation OT - Proofreading Copy",
        verses=verses,
        translation_notes=notes,
        name_notes=name_notes,
        supplemental_notes=brenton_supplemental_notes,
        crossrefs=crossrefs,
        logos=False,
        datatype=args.datatype,
        milestone_mode="lxx",
        versification_map=versification_map,
        verse_counts=verse_counts,
        footnote_number_restart=args.footnote_number_restart,
    )
    build_preview(args.preview, verses, notes, supplemental_notes, crossrefs)
    build_readme(
        args.readme,
        logos_docx=args.logos_docx,
        mt_bridge_docx=args.mt_bridge_docx,
        proof_docx=args.proof_docx,
        diagnostics_path=args.diagnostics,
        preview_path=args.preview,
        datatype=args.datatype,
        footnote_number_restart=args.footnote_number_restart,
        lexham_textual_notes_html=args.lexham_textual_notes_html,
    )
    validations = [validate_docx(args.logos_docx), validate_docx(args.mt_bridge_docx), validate_docx(args.proof_docx)]
    diagnostics = build_diagnostics(
        verses=verses,
        note_counts=note_counts,
        notes=notes,
        name_note_counts=name_note_counts,
        name_notes=name_notes,
        supplemental_note_counts=supplemental_note_counts,
        supplemental_notes=supplemental_notes,
        crossref_diag=crossref_diag,
        logos_stats=logos_stats,
        mt_bridge_stats=mt_bridge_stats,
        proof_stats=proof_stats,
        validations=validations,
        output_paths={
            "logos_docx": str(args.logos_docx),
            "mt_bridge_docx": str(args.mt_bridge_docx),
            "proof_docx": str(args.proof_docx),
            "diagnostics": str(args.diagnostics),
            "readme": str(args.readme),
            "preview": str(args.preview),
        },
        datatype=args.datatype,
        versification_map_diag=versification_map_diag,
    )
    args.diagnostics.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(diagnostics["outputs"], indent=2))


if __name__ == "__main__":
    main()
