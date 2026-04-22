#!/usr/bin/env python3
"""Build Logos Personal Book and proofreading DOCX files for the fresh OT."""

from __future__ import annotations

import argparse
import csv
import difflib
import html
import json
import re
import sqlite3
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
        TSK_NT_BOOKS,
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
        TSK_NT_BOOKS,
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
DEFAULT_TRANSLATION_DECISIONS = RESEARCH / "translation_decisions.csv"
DEFAULT_PROPER_NAMES = DATA / "proper_names.csv"
DEFAULT_TRANSLITERATED_PROPER_NAMES = DATA / "proper_name_transliteration_notes.csv"
DEFAULT_NAMES_OF_GOD = DATA / "names_of_god.csv"
DEFAULT_BOOK_INTROS = DATA / "book_intros_template.csv"
DEFAULT_LOGOS_DOCX = OUTPUT / "fresh_translation_ot_logos_bible.docx"
DEFAULT_MT_BRIDGE_DOCX = OUTPUT / "fresh_translation_ot_logos_bible_mt_notes.docx"
DEFAULT_PROOF_DOCX = OUTPUT / "fresh_translation_ot_proofreading.docx"
DEFAULT_DIAGNOSTICS = OUTPUT / "fresh_translation_ot_logos_bible_diagnostics.json"
DEFAULT_README = OUTPUT / "README.md"
DEFAULT_PREVIEW = OUTPUT / "fresh_translation_ot_logos_bible_preview.md"
DEFAULT_VERSIFICATION_MAP = DATA / "versification" / "lxx_to_eng_map.json"
DEFAULT_TEXTUAL_NOTES_HTML = Path.home() / "Desktop" / "The Lexham Textual Notes on the Bible.html"
DEFAULT_LOGOS_ROOT = Path.home() / "Library" / "Application Support" / "Logos4"

TESTAMENT_CONFIG = {
    "ot": {
        "label": "OT",
        "full_label": "Old Testament",
        "source_text": "LXX Greek",
        "title_prefix": "Fresh Translation OT",
        "bridge_label": "MT Notes Bridge",
        "preview_title": "Fresh Translation OT Logos Bible Preview",
        "description": "Fresh Old Testament translation draft.",
    },
    "nt": {
        "label": "NT",
        "full_label": "New Testament",
        "source_text": "Scrivener 1894 Textus Receptus Greek",
        "title_prefix": "Fresh Translation NT TR",
        "bridge_label": "Reference Notes Bridge",
        "preview_title": "Fresh Translation NT TR Logos Bible Preview",
        "description": "Fresh New Testament Textus Receptus translation draft.",
    },
}

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
GENERIC_MT_LXX_NOTE_PREFIX = "The Septuagint differs here from the Masoretic wording."

MT_LXX_DIFFERENCE_RE = re.compile(
    r"\b(?:Masoretic|MT|Hebrew[- ](?:aligned|based)|Hebrew wording|Hebrew text|"
    r"other textual stream|another textual stream|different textual stream|textual tradition)\b",
    flags=re.I,
)

MAX_PHRASE_ANCHOR_CHARS = 120
MAX_VARIANT_DETAIL_PHRASE_CHARS = 100
VARIANT_TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)?")
NUMBER_WORD_VALUES = {
    "a": 1,
    "an": 1,
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}
NUMBER_SCALE_WORDS = {
    "hundred": 100,
    "thousand": 1000,
    "myriad": 10000,
    "myriads": 10000,
}
NUMBER_WORDS = set(NUMBER_WORD_VALUES) | set(NUMBER_SCALE_WORDS) | {"and"}
NUMBER_UNIT_WORDS = {
    "cubit",
    "cubits",
    "day",
    "days",
    "man",
    "men",
    "month",
    "months",
    "shekel",
    "shekels",
    "talent",
    "talents",
    "year",
    "years",
}
SIGNIFICANT_VARIANT_WORDS = {
    "foreigners",
    "grave",
    "hades",
    "philistines",
}
PLACE_ICON_KINDS = {"City", "OtherPlace", "NaturalPlace", "ManMadePlace"}
GENERIC_PLACE_LABEL_STOPLIST = {
    "East",
    "West",
    "North",
    "South",
    "Earth",
    "Land",
    "Sea",
    "River",
    "Mountain",
    "Valley",
    "Wilderness",
}
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
    chapter_scannable: bool = True

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


@dataclass(frozen=True)
class PlaceLink:
    label: str
    reference: str
    icon_kind: str

    @property
    def pb_reference(self) -> str:
        return self.reference.removeprefix("bk.")


@dataclass(frozen=True)
class PlaceLinkSpan:
    start: int
    end: int
    link: PlaceLink


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
    crossref_marker_mode: str = "numeric"
    crossref_marker_restart: str = "none"
    phrase_anchored_translation_notes: int = 0
    verse_anchored_translation_notes: int = 0
    name_meaning_footnotes: int = 0
    supplemental_note_footnotes: int = 0
    brenton_supplemental_footnotes: int = 0
    textual_note_export_footnotes: int = 0
    phrase_anchored_name_meaning_notes: int = 0
    verse_anchored_name_meaning_notes: int = 0
    phrase_anchored_crossref_notes: int = 0
    verse_anchored_crossref_notes: int = 0
    custom_marked_crossref_notes: int = 0
    max_crossref_marker_index_in_chapter: int = 0
    place_link_count: int = 0
    book_preface_pages: int = 0
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

    def add_footnote(self, text: str) -> int:
        self.footnotes.append(FootnoteEntry(text=text))
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


def load_proper_name_labels(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8", newline="") as handle:
        return {row.get("name", "").strip() for row in csv.DictReader(handle) if row.get("name", "").strip()}


def choose_logos_autocomplete_db(logos_root: Path) -> Path | None:
    data_root = logos_root / "Data"
    if not data_root.exists():
        return None
    candidates = sorted(data_root.glob("*/AutoComplete/AutoComplete.db"))
    if not candidates:
        return None
    return max(candidates, key=lambda path: path.stat().st_size)


def is_safe_place_label(label: str, proper_name_labels: set[str]) -> bool:
    if label in proper_name_labels or label in GENERIC_PLACE_LABEL_STOPLIST:
        return False
    if label.startswith("Any ") or "(" in label or ")" in label:
        return False
    if len(label) < 4 or len(label) > 40:
        return False
    return bool(re.match(r"[A-Z]", label))


def load_logos_place_links(logos_root: Path, proper_names_path: Path) -> tuple[dict[str, PlaceLink], dict[str, object]]:
    autocomplete_db = choose_logos_autocomplete_db(logos_root)
    if not autocomplete_db:
        return {}, {
            "enabled": False,
            "reason": "No Logos AutoComplete.db found.",
            "source_db": None,
            "candidate_labels": 0,
        }

    proper_name_labels = load_proper_name_labels(proper_names_path)
    query = """
    SELECT l.LabelText, t.Reference, ik.IconKind, l.IsPrimary
    FROM Labels l
    JOIN Terms t ON t.TermId = l.TermId
    JOIN IconKinds ik ON ik.IconKindId = t.IconKindId
    WHERE l.LanguageId = 1
      AND t.Reference LIKE 'bk.@%'
    """

    with sqlite3.connect(f"file:{autocomplete_db.as_posix()}?mode=ro", uri=True) as conn:
        rows = conn.execute(query).fetchall()

    all_place_refs: dict[str, set[str]] = defaultdict(set)
    primary_place_rows: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for label, reference, icon_kind, is_primary in rows:
        if icon_kind not in PLACE_ICON_KINDS:
            continue
        all_place_refs[label].add(reference)
        if is_primary:
            primary_place_rows[label].append((reference, icon_kind))

    links: dict[str, PlaceLink] = {}
    skipped_ambiguous = 0
    for label, entries in primary_place_rows.items():
        if not is_safe_place_label(label, proper_name_labels):
            continue
        refs = {reference for reference, _icon_kind in entries}
        if len(refs) != 1 or len(all_place_refs.get(label, set())) != 1:
            skipped_ambiguous += 1
            continue
        reference, icon_kind = entries[0]
        links[label] = PlaceLink(label=label, reference=reference, icon_kind=icon_kind)

    return links, {
        "enabled": True,
        "source_db": str(autocomplete_db),
        "candidate_labels": len(links),
        "skipped_ambiguous_labels": skipped_ambiguous,
        "datatype": "BibleKnowledgebase",
        "note": "Links are conservative Personal Book datatype links, not internal Logos Factbook tag overlays.",
    }


def build_place_link_pattern(place_links: dict[str, PlaceLink]) -> re.Pattern[str] | None:
    if not place_links:
        return None
    labels = sorted(place_links, key=len, reverse=True)
    return re.compile(r"(?<![A-Za-z0-9])(" + "|".join(re.escape(label) for label in labels) + r")(?![A-Za-z0-9])")


def find_place_link_spans(
    verse_text: str,
    place_links: dict[str, PlaceLink],
    place_link_pattern: re.Pattern[str] | None,
    occupied: list[tuple[int, int]],  # Kept for call-site clarity; place links may share footnote anchors.
) -> list[PlaceLinkSpan]:
    if not place_link_pattern:
        return []

    spans: list[PlaceLinkSpan] = []
    used: list[tuple[int, int]] = []
    for match in place_link_pattern.finditer(verse_text):
        start, end = match.span(1)
        if any(not (end <= old_start or start >= old_end) for old_start, old_end in used):
            continue
        label = match.group(1)
        link = place_links.get(label)
        if not link:
            continue
        spans.append(PlaceLinkSpan(start=start, end=end, link=link))
        used.append((start, end))
    return spans


def text_runs_with_place_links(
    verse_text: str,
    start: int,
    end: int,
    place_spans: list[PlaceLinkSpan],
) -> list[str]:
    relevant = [span for span in place_spans if start <= span.start and span.end <= end]
    if not relevant:
        return [run(verse_text[start:end])]

    output: list[str] = []
    cursor = start
    for span in relevant:
        if cursor < span.start:
            output.append(run(verse_text[cursor:span.start]))
        label = verse_text[span.start:span.end]
        output.append(run(f"[[{label} >> BibleKnowledgebase:{span.link.pb_reference}]]"))
        cursor = span.end
    if cursor < end:
        output.append(run(verse_text[cursor:end]))
    return output


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


def footnote_ref_run(note_id: int) -> str:
    return (
        f'<w:r>{footnote_reference_style_xml()}'
        f'<w:footnoteReference w:id="{note_id}"/></w:r>'
    )


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
        marker_run = f'<w:r>{footnote_reference_style_xml()}<w:footnoteRef/></w:r>'
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


def load_variant_decisions(path: Path) -> tuple[dict[str, dict[str, str]], dict[str, int]]:
    counts = Counter({"present": int(path.exists())})
    if not path.exists():
        return {}, dict(counts)

    decisions: dict[str, dict[str, str]] = {}
    for row in load_csv(path):
        counts["rows"] += 1
        if row.get("status", "").strip().lower() != "reviewed":
            counts["skipped_unreviewed"] += 1
            continue
        if row.get("lemma", "").strip().lower() != "verse-level variant":
            counts["skipped_non_variant"] += 1
            continue
        ref = normalize_note_ref(row.get("ref", ""))
        chosen = normalize_space(row.get("chosen_rendering", ""))
        alternate = normalize_space(row.get("alternate_renderings", ""))
        if not ref or not chosen or not alternate:
            counts["skipped_incomplete"] += 1
            continue
        if ref in decisions:
            counts["duplicate_refs"] += 1
            continue
        decisions[ref] = row
        counts["included"] += 1
    counts["included_refs"] = len(decisions)
    return decisions, dict(counts)


def load_translation_notes(
    path: Path,
    variant_decisions: dict[str, dict[str, str]] | None = None,
) -> tuple[dict[str, list[TranslationNote]], dict[str, int]]:
    rows = load_csv(path)
    grouped: dict[str, list[TranslationNote]] = defaultdict(list)
    counts = Counter()
    variant_decisions = variant_decisions or {}
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
        if is_generic_mt_lxx_note(row):
            detail = concrete_variant_detail(row.get("ref", ""), variant_decisions)
            if not detail:
                counts["skipped_generic_mt_lxx_without_concrete_detail"] += 1
                continue
            body = detail
            counts["included_concrete_mt_lxx_details"] += 1
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


def merge_translation_notes(
    *note_maps: dict[str, list[TranslationNote]],
) -> dict[str, list[TranslationNote]]:
    merged: dict[str, list[TranslationNote]] = defaultdict(list)
    seen: set[tuple[str, str, str, str]] = set()
    for note_map in note_maps:
        for ref, notes in note_map.items():
            for note in notes:
                key = (ref, note.note_type, note.trigger_phrase, note.display_text)
                if key in seen:
                    continue
                seen.add(key)
                merged[ref].append(note)
    return dict(merged)


def filter_translation_notes_to_verses(
    notes: dict[str, list[TranslationNote]],
    verses: list[Verse],
) -> dict[str, list[TranslationNote]]:
    verse_refs = {verse.ref for verse in verses}
    return {ref: items for ref, items in notes.items() if ref in verse_refs}


def is_generic_mt_lxx_note(row: dict[str, str]) -> bool:
    body = normalize_space(row.get("footnote_text", ""))
    source = row.get("source_basis", "").strip().lower()
    return body.startswith(GENERIC_MT_LXX_NOTE_PREFIX) and source == "variant + witnesses"


def concrete_variant_detail(
    ref: str,
    variant_decisions: dict[str, dict[str, str]],
) -> str | None:
    decision = variant_decisions.get(normalize_note_ref(ref))
    if not decision:
        return None
    chosen = normalize_space(decision.get("chosen_rendering", ""))
    alternate = normalize_space(decision.get("alternate_renderings", ""))
    if not chosen or not alternate or chosen.casefold() == alternate.casefold():
        return None

    difference = extract_number_unit_difference(chosen, alternate)
    if not difference:
        difference = extract_single_local_difference(chosen, alternate)
    if not difference:
        return None

    lxx_phrase, mt_phrase = difference
    return (
        f'LXX/fresh has "{short_variant_phrase(lxx_phrase)}"; '
        f'MT comparison has "{short_variant_phrase(mt_phrase)}".'
    )


def extract_number_unit_difference(chosen: str, alternate: str) -> tuple[str, str] | None:
    chosen_phrases = number_unit_phrases(chosen)
    alternate_phrases = number_unit_phrases(alternate)
    if not chosen_phrases or not alternate_phrases:
        return None
    if len(chosen_phrases) == len(alternate_phrases):
        differences: list[tuple[str, str]] = []
        for left, right in zip(chosen_phrases, alternate_phrases):
            chosen_phrase, chosen_value = left
            alternate_phrase, alternate_value = right
            if chosen_phrase.casefold() != alternate_phrase.casefold() and chosen_value != alternate_value:
                differences.append((chosen_phrase, alternate_phrase))
        if len(differences) == 1:
            return differences[0]
    if len(chosen_phrases) == 1 and len(alternate_phrases) == 1:
        chosen_phrase, chosen_value = chosen_phrases[0]
        alternate_phrase, alternate_value = alternate_phrases[0]
        if chosen_phrase.casefold() != alternate_phrase.casefold() and chosen_value != alternate_value:
            return chosen_phrase, alternate_phrase
    return None


def number_unit_phrases(value: str) -> list[tuple[str, int]]:
    tokens = VARIANT_TOKEN_RE.findall(value)
    phrases: list[tuple[str, int]] = []
    for index, token in enumerate(tokens):
        if token.lower() not in NUMBER_UNIT_WORDS:
            continue
        cursor = index - 1
        while cursor >= 0 and is_number_word_token(tokens[cursor]):
            cursor -= 1
        number_tokens = tokens[cursor + 1 : index]
        while number_tokens and number_tokens[0].lower() == "and":
            number_tokens = number_tokens[1:]
        if not number_tokens or len(number_tokens) > 9:
            continue
        if looks_like_ambiguous_number_shorthand(number_tokens):
            continue
        number_value = parse_number_words(number_tokens)
        if number_value is None:
            continue
        phrases.append((untokenize_variant_tokens([*number_tokens, token]), number_value))
    return phrases


def looks_like_ambiguous_number_shorthand(tokens: list[str]) -> bool:
    lowered = [token.lower() for token in tokens]
    if len(lowered) != 2:
        return False
    first, second = lowered
    return first in {"a", "an", "one"} and NUMBER_WORD_VALUES.get(second, 0) >= 20


def is_number_word_token(token: str) -> bool:
    return all(part in NUMBER_WORDS for part in token.lower().split("-"))


def parse_number_words(tokens: list[str]) -> int | None:
    total = 0
    current = 0
    saw_number = False
    for token in tokens:
        for part in token.lower().split("-"):
            if part == "and":
                continue
            if part in NUMBER_WORD_VALUES:
                current += NUMBER_WORD_VALUES[part]
                saw_number = True
                continue
            if part == "hundred":
                current = (current or 1) * 100
                saw_number = True
                continue
            if part in NUMBER_SCALE_WORDS:
                total += (current or 1) * NUMBER_SCALE_WORDS[part]
                current = 0
                saw_number = True
                continue
            return None
    return total + current if saw_number else None


def extract_single_local_difference(chosen: str, alternate: str) -> tuple[str, str] | None:
    chosen_tokens = VARIANT_TOKEN_RE.findall(chosen)
    alternate_tokens = VARIANT_TOKEN_RE.findall(alternate)
    if not chosen_tokens or not alternate_tokens:
        return None
    matcher = difflib.SequenceMatcher(
        None,
        [token.casefold() for token in chosen_tokens],
        [token.casefold() for token in alternate_tokens],
        autojunk=False,
    )
    differences = [opcode for opcode in matcher.get_opcodes() if opcode[0] != "equal"]
    if len(differences) != 1:
        return None

    _tag, chosen_start, chosen_end, alternate_start, alternate_end = differences[0]
    chosen_span = chosen_tokens[chosen_start:chosen_end]
    alternate_span = alternate_tokens[alternate_start:alternate_end]
    if not chosen_span or not alternate_span:
        return None
    if max(len(chosen_span), len(alternate_span)) > 6:
        return None
    if chosen_start < 2 or alternate_start < 2:
        return None
    if len(chosen_tokens) - chosen_end < 2 or len(alternate_tokens) - alternate_end < 2:
        return None

    # Avoid notes that only explain old-vs-modern English style.
    if not has_substantive_local_difference(chosen_span, alternate_span):
        return None
    return untokenize_variant_tokens(chosen_span), untokenize_variant_tokens(alternate_span)


def has_substantive_local_difference(chosen_span: list[str], alternate_span: list[str]) -> bool:
    chosen_words = {token.casefold() for token in chosen_span}
    alternate_words = {token.casefold() for token in alternate_span}
    style_pairs = {
        ("said", "spoke"),
        ("to", "unto"),
        ("who", "which"),
        ("brothers", "brethren"),
        ("children", "sons"),
        ("happened", "came"),
        ("humbled", "brought"),
    }
    if len(chosen_words) <= 2 and len(alternate_words) <= 2:
        for left, right in style_pairs:
            if left in chosen_words and right in alternate_words:
                return False
            if right in chosen_words and left in alternate_words:
                return False
    if chosen_words <= ANCHOR_STOPWORDS or alternate_words <= ANCHOR_STOPWORDS:
        return False
    if (chosen_words | alternate_words) & SIGNIFICANT_VARIANT_WORDS:
        return True
    return any(
        looks_like_proper_variant_token(token)
        for token in [*chosen_span, *alternate_span]
    )


def looks_like_proper_variant_token(token: str) -> bool:
    return len(token) > 2 and token[:1].isupper() and token.casefold() not in ANCHOR_STOPWORDS


def untokenize_variant_tokens(tokens: list[str]) -> str:
    return " ".join(tokens)


def short_variant_phrase(value: str) -> str:
    value = normalize_space(value)
    if len(value) <= MAX_VARIANT_DETAIL_PHRASE_CHARS:
        return value
    truncated = value[: MAX_VARIANT_DETAIL_PHRASE_CHARS - 3].rsplit(" ", 1)[0]
    return f"{truncated}..."


SOURCE_REF_ONLY_DIVINE_NOTE_MARKERS = (
    "at the hebrew",
    "at the el shaddai",
    "at job",
    "does not preserve",
    "preserves saddai here",
    "hagar's title",
    "bethel title",
    "renders yahweh",
    "city-name line",
    "lxx has iosedek",
    "messianic title differs",
)


def should_scan_divine_note_by_chapter(language: str, note: str) -> bool:
    if language != "Greek LXX":
        return True
    lowered = note.casefold()
    return not any(marker in lowered for marker in SOURCE_REF_ONLY_DIVINE_NOTE_MARKERS)


def load_name_meaning_notes(
    *,
    proper_names_path: Path,
    transliterated_proper_names_path: Path,
    names_of_god_path: Path,
    source_filter: str | None = None,
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
    if transliterated_proper_names_path.exists():
        with transliterated_proper_names_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                counts["transliterated_proper_name_rows"] += 1
                source = normalize_space(row.get("source", ""))
                if source_filter and source and source != source_filter:
                    counts["transliterated_proper_name_skipped_other_source"] += 1
                    continue
                ref = normalize_note_ref(row.get("first_reference", ""))
                name = normalize_space(row.get("name", ""))
                kind = normalize_space(row.get("kind", ""))
                note = normalize_space(row.get("footnote", ""))
                if not ref or not name:
                    counts["transliterated_proper_name_skipped"] += 1
                    continue
                label = {
                    "person": "Personal name",
                    "place": "Place name",
                    "people_group": "People-name",
                    "supernatural_being": "Divine or supernatural name",
                    "transliterated_form": "Transliterated proper noun",
                }.get(kind, "Proper name")
                pieces = [f"{label}: {name}."]
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
                counts["transliterated_proper_name_included"] += 1
    if names_of_god_path.exists():
        raw = names_of_god_path.read_text(encoding="utf-8").replace("“", '"').replace("”", '"')
        reader = csv.DictReader(raw.splitlines())
        for row in reader:
            counts["name_of_god_rows"] += 1
            language = normalize_space(row.get("language", ""))
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
            prefix = f"{language} divine name/title" if language else "Divine name/title"
            pieces = [f"{prefix}: {label}"]
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
                    chapter_scannable=should_scan_divine_note_by_chapter(language, note),
                )
            )
            counts["name_of_god_included"] += 1
    counts["included"] = (
        counts["proper_name_included"]
        + counts["transliterated_proper_name_included"]
        + counts["name_of_god_included"]
    )
    counts["refs"] = len(grouped)
    return dict(grouped), dict(counts)


def is_chapter_scannable_name_note(note: NameMeaningNote) -> bool:
    if not note.chapter_scannable:
        return False
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


def load_book_intros(path: Path) -> tuple[dict[str, dict[str, str]], dict[str, object]]:
    if not path.exists():
        return {}, {
            "present": False,
            "path": str(path),
            "rows": 0,
            "usable_rows": 0,
        }
    rows = load_csv(path)
    intros = {
        row["book_code"].strip(): row
        for row in rows
        if row.get("book_code", "").strip() and book_intro_has_content(row)
    }
    return intros, {
        "present": True,
        "path": str(path),
        "rows": len(rows),
        "usable_rows": len(intros),
    }


def deuterocanonical_future_work(
    book_intros: dict[str, dict[str, str]],
    verses: list[Verse],
) -> dict[str, object]:
    source_codes = {verse.book_code for verse in verses}
    missing = [
        {
            "book_code": code,
            "book_name": row.get("book_name", "").strip() or row.get("intro_title", "").strip(),
            "status": row.get("status", "").strip(),
        }
        for code, row in sorted(
            book_intros.items(),
            key=lambda item: int(item[1].get("canonical_order", "999") or 999),
        )
        if row.get("section", "").strip().lower() == "apocrypha" and code not in source_codes
    ]
    return {
        "status": "future_work",
        "reason": "Book intro metadata exists, but no verse rows are present in current source CSV.",
        "missing_book_count": len(missing),
        "missing_books": missing,
    }


def book_intro_has_content(row: dict[str, str] | None) -> bool:
    if not row:
        return False
    excluded = {"book_code", "book_name", "canonical_order", "section", "intro_title", "status", "source_notes"}
    return any((value or "").strip() for key, value in row.items() if key not in excluded)


def compact_intro_groups(row: dict[str, str]) -> list[tuple[str, str]]:
    def parts(*keys: str) -> str:
        values = [row.get(key, "").strip() for key in keys if row.get(key, "").strip()]
        return " ".join(values).strip()

    witnesses: list[str] = []
    if parts("oldest_fragment", "oldest_fragment_date"):
        witnesses.append("Frag. " + parts("oldest_fragment", "oldest_fragment_date"))
    if parts("oldest_substantial_manuscript", "oldest_substantial_date"):
        witnesses.append("Subst. " + parts("oldest_substantial_manuscript", "oldest_substantial_date"))
    if parts("oldest_complete_hebrew", "oldest_complete_hebrew_date"):
        witnesses.append("Heb. " + parts("oldest_complete_hebrew", "oldest_complete_hebrew_date"))
    if parts("oldest_complete_greek", "oldest_complete_greek_date"):
        witnesses.append("Gk. " + parts("oldest_complete_greek", "oldest_complete_greek_date"))

    external: list[str] = []
    if row.get("oldest_external_reference", "").strip():
        external.append(row["oldest_external_reference"].strip())
    if row.get("oldest_external_reference_author", "").strip():
        external.append("by " + row["oldest_external_reference_author"].strip())
    if row.get("oldest_external_reference_date", "").strip():
        external.append("(" + row["oldest_external_reference_date"].strip() + ")")

    groups = [
        ("Author and Attribution", parts("traditional_author")),
        ("Authorship Basis", parts("authorship_basis")),
        ("Jesus / NT Attribution", parts("jesus_or_nt_attribution")),
        ("Composition Date", parts("composition_date")),
        ("MT Timeline", parts("mt_timeline")),
        ("LXX Timeline", parts("lxx_timeline")),
        ("Historical Setting", parts("historical_setting")),
        ("Purpose", parts("purpose_theme")),
        ("Key Themes", parts("key_themes")),
        ("Outline", parts("outline")),
        ("Earliest Witnesses", " | ".join(witnesses).strip()),
        ("Earliest External Attestation", " ".join(external).strip()),
        ("Textual Notes", parts("textual_notes")),
        ("Conservative Notes", parts("conservative_notes")),
    ]
    return [(label, value) for label, value in groups if value]


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
    fragment = re.sub(r"\bin the which\b", "in which", fragment, flags=re.I)
    fragment = re.sub(r"\bover the which\b", "over which", fragment, flags=re.I)
    fragment = re.sub(r"\brepented not\b", "did not repent", fragment, flags=re.I)
    fragment = re.sub(r"\bbelieved not\b", "did not believe", fragment, flags=re.I)
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


def parse_tsk_crossref_groups(
    testament: str,
) -> tuple[dict[tuple[str, int, int], list[CrossReferenceNote]], dict[str, object]]:
    diagnostics: dict[str, object] = {
        "archive_present": TSK_ZIP.exists(),
        "testament": testament,
        "status": "unparsed",
    }
    if not TSK_ZIP.exists():
        diagnostics["reason"] = "TSK archive not found."
        return {}, diagnostics
    verse_counts = load_kjv_versification()
    if not verse_counts:
        diagnostics["reason"] = "KJV versification data not found."
        return {}, diagnostics

    if testament == "nt":
        book_order = TSK_NT_BOOKS
        base = "modules/comments/zcom/tsk/nt"
    else:
        book_order = TSK_OT_BOOKS
        base = "modules/comments/zcom/tsk/ot"

    index_map = build_tsk_index_map(book_order, verse_counts)
    grouped: dict[tuple[str, int, int], list[CrossReferenceNote]] = defaultdict(list)
    with zipfile.ZipFile(TSK_ZIP) as zf:
        bzv = zf.read(f"{base}.bzv")
        bzs = zf.read(f"{base}.bzs")
        bzz = zf.read(f"{base}.bzz")
        diagnostics[f"{testament}_entries"] = len(bzv) // 10
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


def build_crossrefs_for_verses(
    verses: list[Verse],
    testament: str,
    *,
    enabled: bool,
) -> tuple[dict[str, list[CrossReferenceNote]], dict[str, object]]:
    if not enabled:
        return {}, {
            "enabled": False,
            "reason": "Disabled with --no-crossrefs.",
            "source_counts": {},
            "verses_with_crossrefs": 0,
            "crossref_note_groups": 0,
            "total_crossrefs_after_canonicalization": 0,
        }
    tsk_refs, tsk_diag = parse_tsk_crossref_groups(testament)
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
REFLY_BOLD_REF_LINK_RE = re.compile(
    r'<a\s+href="https://ref\.ly/([^"]+)"[^>]*>\s*'
    r'<span[^>]*font-weight\s*:\s*bold[^>]*>(.*?)</span>\s*</a>',
    flags=re.I | re.S,
)
TEXTUAL_NOTE_PARAGRAPH_RE = re.compile(r"<p\b[^>]*>.*?</p>", flags=re.I | re.S)
TEXTUAL_NOTE_HEADER_LINK_RE = REFLY_BOLD_REF_LINK_RE
TEXTUAL_NOTE_BOLD_RE = re.compile(
    r'<span[^>]*font-weight\s*:\s*bold[^>]*>(.*?)</span>',
    flags=re.I | re.S,
)
TEXTUAL_NOTE_DISPLAY_REF_RE = re.compile(r"^(.+?)\s+(\d+)(?::(\d+))?$")
TEXTUAL_NOTE_SOURCE_BASIS = "textual note export"


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

    return dict(grouped), {
        **dict(counts),
        "brenton_usfm": brenton_diag,
        "tsk_study_notes": {
            "enabled": False,
            "reason": "Excluded from supplemental footnotes; TSK remains enabled for cross-references.",
        },
        "included_refs": len(grouped),
        "included_total": sum(len(items) for items in grouped.values()),
    }


def load_textual_notes_export(
    path: Path,
    verses: list[Verse],
    versification_map: dict[str, str],
) -> tuple[dict[str, list[TranslationNote]], dict[str, object]]:
    verse_refs = {verse.ref for verse in verses}
    standard_refs_to_source_refs: dict[str, list[str]] = defaultdict(list)
    refs_by_chapter: dict[tuple[str, int], list[str]] = defaultdict(list)
    for verse in verses:
        source_ref = source_code_ref(verse)
        standard_ref = versification_map.get(source_ref, source_ref)
        standard_refs_to_source_refs[standard_ref].append(verse.ref)
        refs_by_chapter[(verse.book_name, verse.chapter)].append(verse.ref)
    grouped: dict[str, list[TranslationNote]] = defaultdict(list)
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
    entries = parse_textual_note_export_entries(raw_html)
    counts["source_entries"] = len(entries)
    for entry in entries:
        display_ref = entry["display_ref"]
        body = textual_note_body(entry["blocks"])
        if not body:
            counts["skipped_empty_note_body"] += 1
            continue
        target_refs, fallback_ref = textual_note_target_refs(
            display_ref=display_ref,
            verse_refs=verse_refs,
            standard_refs_to_source_refs=standard_refs_to_source_refs,
            refs_by_chapter=refs_by_chapter,
        )
        if not target_refs:
            counts["skipped_missing_ref"] += 1
            continue
        if fallback_ref:
            counts["included_by_nearest_source_ref"] += len(target_refs)
            body = f"For standard {normalize_textual_display_ref(display_ref)}: {body}"
        elif normalize_textual_display_ref(display_ref) in verse_refs:
            counts["included_by_direct_ref"] += len(target_refs)
        else:
            counts["included_by_versification_map"] += len(target_refs)
        for target_ref in target_refs:
            dedupe_key = (target_ref, body)
            if dedupe_key in seen:
                counts["skipped_duplicate"] += 1
                continue
            seen.add(dedupe_key)
            grouped[target_ref].append(
                TranslationNote(
                    ref=target_ref,
                    note_type="textual",
                    trigger_phrase="",
                    text=body,
                    source_basis=TEXTUAL_NOTE_SOURCE_BASIS,
                )
            )
            counts["included_total"] += 1

    return dict(grouped), {
        **dict(counts),
        "present": True,
        "path": str(path),
        "included_refs": len(grouped),
        "included_total": sum(len(items) for items in grouped.values()),
        "mode": "local_embedded_textual_notes",
    }


def parse_textual_note_export_entries(raw_html: str) -> list[dict[str, object]]:
    entries: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    for paragraph in TEXTUAL_NOTE_PARAGRAPH_RE.findall(raw_html):
        header = textual_note_header(paragraph)
        if header:
            if current:
                entries.append(current)
            current = {"display_ref": header, "blocks": []}
            continue
        if current is None:
            continue
        paragraph_text = strip_html_text(paragraph)
        if paragraph_text:
            current_blocks = current["blocks"]
            assert isinstance(current_blocks, list)
            current_blocks.append(paragraph_text)
    if current:
        entries.append(current)
    return entries


def textual_note_header(paragraph_html: str) -> str | None:
    link_match = TEXTUAL_NOTE_HEADER_LINK_RE.search(paragraph_html)
    if link_match:
        return strip_html_text(link_match.group(2))
    bold_match = TEXTUAL_NOTE_BOLD_RE.search(paragraph_html)
    if not bold_match:
        return None
    bold_text = strip_html_text(bold_match.group(1))
    if TEXTUAL_NOTE_DISPLAY_REF_RE.match(bold_text):
        return bold_text
    return None


def textual_note_body(blocks_value: object) -> str:
    blocks = [str(block) for block in blocks_value] if isinstance(blocks_value, list) else []
    note_blocks = [clean_textual_note_text(block) for block in blocks[2:]]
    note_blocks = [block for block in note_blocks if block and not is_textual_note_export_junk(block)]
    return normalize_space(" ".join(note_blocks))


def is_textual_note_export_junk(value: str) -> bool:
    book_headings = set(STANDARD_BOOK_NAMES.values()) | {"Psalm", "Song of Solomon"}
    return (
        value in book_headings
        or value.startswith("Brannan, Rick")
        or value.startswith("Exported from Logos")
    )


def clean_textual_note_text(value: str) -> str:
    replacements = {
        "\u00a0": " ",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u202f": " ",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    value = re.sub(r"\bLXX\.,", "LXX,", value)
    value = re.sub(r"\s+([,.;:)])", r"\1", value)
    value = re.sub(r"([(])\s+", r"\1", value)
    return normalize_space(value)


def textual_note_target_refs(
    *,
    display_ref: str,
    verse_refs: set[str],
    standard_refs_to_source_refs: dict[str, list[str]],
    refs_by_chapter: dict[tuple[str, int], list[str]],
) -> tuple[list[str], str | None]:
    normalized_ref = normalize_textual_display_ref(display_ref)
    if normalized_ref in verse_refs:
        return [normalized_ref], None
    code_ref = display_ref_to_code_ref(normalized_ref)
    mapped_refs = standard_refs_to_source_refs.get(code_ref or "", [])
    if mapped_refs:
        return mapped_refs, None
    fallback_ref = nearest_source_ref(normalized_ref, refs_by_chapter)
    return ([fallback_ref], fallback_ref) if fallback_ref else ([], None)


def normalize_textual_display_ref(display_ref: str) -> str:
    normalized = normalize_note_ref(display_ref)
    match = TEXTUAL_NOTE_DISPLAY_REF_RE.match(normalized)
    if not match:
        return normalized
    book_name, chapter, verse = match.groups()
    verse = verse or "1"
    return f"{book_name} {int(chapter)}:{int(verse)}"


def nearest_source_ref(
    normalized_ref: str,
    refs_by_chapter: dict[tuple[str, int], list[str]],
) -> str | None:
    match = DISPLAY_REF_RE.match(normalized_ref)
    if not match:
        return None
    book_name, chapter_raw, verse_raw = match.groups()
    chapter = int(chapter_raw)
    verse = int(verse_raw)
    chapter_refs = refs_by_chapter.get((book_name, chapter), [])
    if not chapter_refs:
        return None
    parsed_refs: list[tuple[int, str]] = []
    for ref in chapter_refs:
        ref_match = DISPLAY_REF_RE.match(ref)
        if ref_match:
            parsed_refs.append((int(ref_match.group(3)), ref))
    if not parsed_refs:
        return None
    before = [item for item in parsed_refs if item[0] <= verse]
    if before:
        return max(before)[1]
    return min(parsed_refs)[1]


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


def build_docx(
    *,
    path: Path,
    title: str,
    description: str,
    testament: str,
    verses: list[Verse],
    translation_notes: dict[str, list[TranslationNote]],
    name_notes: dict[str, list[NameMeaningNote]],
    supplemental_notes: dict[str, list[SupplementalNote]],
    crossrefs: dict[str, list[CrossReferenceNote]],
    book_intros: dict[str, dict[str, str]],
    logos: bool,
    datatype: str,
    milestone_mode: str = "lxx",
    versification_map: dict[str, str] | None = None,
    verse_counts: dict[str, list[int]] | None = None,
    footnote_number_restart: str = "chapter",
    place_links: dict[str, PlaceLink] | None = None,
    place_link_pattern: re.Pattern[str] | None = None,
    crossrefs_enabled: bool = False,
) -> BuildStats:
    doc = MinimalDocx(
        title=title,
        subject=(
            f"{description} with translation notes and cross-references"
            if crossrefs_enabled
            else f"{description} with translation, textual, supplemental, and name notes"
        ),
    )
    stats = BuildStats(
        output_kind="logos" if logos else "proofreading",
        milestone_mode=milestone_mode,
        footnote_number_restart=footnote_number_restart,
    )
    add_title_page(
        doc,
        title,
        description=description,
        testament=testament,
        logos=logos,
        datatype=datatype,
        milestone_mode=milestone_mode,
        footnote_number_restart=footnote_number_restart,
        crossrefs_enabled=crossrefs_enabled,
    )

    current_book = ""
    current_chapter = -1
    milestone_ref_counts: Counter[str] = Counter()
    versification_map = versification_map or {}
    verse_counts = verse_counts or {}
    place_links = place_links or {}
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
            intro = book_intros.get(verse.book_code) or book_intros.get(
                LXX_TSK_CODE_MAP.get(verse.book_code, verse.book_code)
            )
            if intro:
                stats.paragraph_count += add_book_preface_page(doc, verse.book_name, intro)
                stats.book_preface_pages += 1
                doc.add_page_break()
        if verse.chapter != current_chapter:
            current_chapter = verse.chapter
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
            place_links=place_links if logos else {},
            place_link_pattern=place_link_pattern if logos else None,
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

    stats.place_link_count = sum(part.count("BibleKnowledgebase:") for part in doc.body)
    stats.footnote_count = len(doc.footnotes)
    stats.duplicate_milestone_refs = sum(count - 1 for count in milestone_ref_counts.values() if count > 1)
    doc.save(path)
    return stats


def add_title_page(
    doc: MinimalDocx,
    title: str,
    *,
    description: str,
    testament: str,
    logos: bool,
    datatype: str,
    milestone_mode: str,
    footnote_number_restart: str,
    crossrefs_enabled: bool,
) -> None:
    doc.add_paragraph([run(title)], style="Title")
    subtitle = "Logos Personal Book source" if logos else "Proofreading and print copy"
    doc.add_paragraph([run(subtitle)], style="Subtitle")
    note_policy = (
        "Includes reviewed translation/textual notes. Generic MT/LXX boilerplate is omitted unless a concrete local difference can be stated."
        if testament == "ot"
        else "Includes reviewed translation/textual notes that match NT references. OT-specific MT/LXX boilerplate is omitted."
    )
    supplemental_policy = (
        "Includes supplemental Brenton USFM footnotes."
        if testament == "ot"
        else "Includes no NT supplemental source-note layer yet."
    )
    vocab_policy = (
        "Hebrew/Greek vocabulary notes are excluded; name/proper-noun meanings remain included separately."
        if testament == "ot"
        else "Greek vocabulary notes are excluded; name/proper-noun meanings remain included separately."
    )
    lines = [
        description,
        note_policy,
        "Includes book preface pages before each book's chapter text.",
        (
            "Includes full available cross-reference set from TSK, with OpenBible fallback where TSK has no row."
            if crossrefs_enabled
            else "Cross-reference footnote layer is excluded because --no-crossrefs was used."
        ),
        "Includes name-meaning notes at first exact occurrence per chapter.",
        supplemental_policy,
        vocab_policy,
        (
            f"Regular footnote numbering restarts by {footnote_number_restart}. "
            "Cross-reference footnotes use normal numeric Word footnote references for Logos Personal Book compatibility when enabled."
        ),
    ]
    if logos:
        lines.append(f"Verse milestones use Logos datatype {datatype}. Compile in Logos as resource type Bible.")
        lines.append("Conservative place-name links use Logos Bible Knowledgebase targets where a local Logos place entity can be matched unambiguously.")
        lines.append("Textual-note export entries are embedded as local notes; no Logos resource-link layer is used.")
        if milestone_mode == "mt":
            lines.append("Milestones are remapped to standard English/MT Bible references for Logos note sharing.")
    for line in lines:
        doc.add_paragraph([run(line)])
    doc.add_page_break()


def add_book_preface_page(doc: MinimalDocx, fallback_book_name: str, intro: dict[str, str]) -> int:
    title = intro.get("intro_title", "").strip() or intro.get("book_name", "").strip() or fallback_book_name
    doc.add_heading(f"{title} Preface", level=2)
    paragraph_count = 1
    for label, value in compact_intro_groups(intro):
        doc.add_paragraph([run(f"{label}. ", bold=True), run(value)])
        paragraph_count += 1
    return paragraph_count


def build_verse_runs(
    *,
    doc: MinimalDocx,
    verse: Verse,
    notes: list[TranslationNote],
    name_notes: list[NameMeaningNote],
    supplemental_notes: list[SupplementalNote],
    crossref_notes: list[CrossReferenceNote],
    place_links: dict[str, PlaceLink],
    place_link_pattern: re.Pattern[str] | None,
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
        place_links,
        place_link_pattern,
        stats,
    )
    runs.extend(text_runs)
    for note in verse_level_notes:
        note_id = doc.add_footnote(note.display_text)
        runs.append(footnote_ref_run(note_id))
        stats.translation_note_footnotes += 1
        if note.source_basis == TEXTUAL_NOTE_SOURCE_BASIS:
            stats.textual_note_export_footnotes += 1
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
        stats.brenton_supplemental_footnotes += 1
    for crossref in verse_level_crossrefs:
        note_id = add_crossref_footnote(doc, crossref, stats)
        runs.append(footnote_ref_run(note_id))
        stats.verse_anchored_crossref_notes += 1
    if logos:
        runs.append(run("{{field-off:Bible}}"))
    return runs, milestone_ref


def add_crossref_footnote(
    doc: MinimalDocx,
    crossref: CrossReferenceNote,
    stats: BuildStats,
) -> int:
    note_id = doc.add_footnote(crossref.display_text)
    stats.crossref_footnotes += 1
    return note_id


def runs_for_text_with_phrase_notes(
    doc: MinimalDocx,
    verse_text: str,
    notes: list[TranslationNote],
    name_notes: list[NameMeaningNote],
    crossrefs: list[CrossReferenceNote],
    place_links: dict[str, PlaceLink],
    place_link_pattern: re.Pattern[str] | None,
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

    place_spans = find_place_link_spans(verse_text, place_links, place_link_pattern, occupied)

    output: list[str] = []
    cursor = 0
    for end in sorted(anchors):
        output.extend(text_runs_with_place_links(verse_text, cursor, end, place_spans))
        for kind, item in anchors[end]:
            if kind == "crossref":
                assert isinstance(item, CrossReferenceNote)
                note_id = add_crossref_footnote(doc, item, stats)
                output.append(footnote_ref_run(note_id))
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
    output.extend(text_runs_with_place_links(verse_text, cursor, len(verse_text), place_spans))
    return output, verse_level, verse_level_names, verse_level_crossrefs


def build_preview(
    path: Path,
    verses: list[Verse],
    notes: dict[str, list[TranslationNote]],
    supplemental_notes: dict[str, list[SupplementalNote]],
    refs: dict[str, list[CrossReferenceNote]],
    title: str,
) -> None:
    lines = [
        f"# {title}",
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
            lines.append(f"- Supplemental notes/links: {supplemental_count}")
            lines.append(f"- Cross-references: {crossref_count}")
            lines.append("")
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def build_readme(
    path: Path,
    *,
    testament: str,
    config: dict[str, str],
    source_path: Path,
    logos_docx: Path,
    mt_bridge_docx: Path,
    proof_docx: Path,
    diagnostics_path: Path,
    preview_path: Path,
    datatype: str,
    footnote_number_restart: str,
    textual_notes_html: Path,
    book_intros_path: Path,
    translation_decisions_path: Path,
    deuterocanonical_work: dict[str, object],
    crossrefs_enabled: bool,
) -> None:
    try:
        book_intros_display = book_intros_path.relative_to(ROOT).as_posix()
    except ValueError:
        book_intros_display = str(book_intros_path)
    try:
        translation_decisions_display = translation_decisions_path.relative_to(ROOT).as_posix()
    except ValueError:
        translation_decisions_display = str(translation_decisions_path)
    try:
        textual_notes_display = textual_notes_html.relative_to(ROOT).as_posix()
    except ValueError:
        textual_notes_display = str(textual_notes_html)
    missing_deuterocanon = [
        item.get("book_name", "")
        for item in deuterocanonical_work.get("missing_books", [])
        if isinstance(item, dict) and item.get("book_name", "")
    ]
    missing_deuterocanon_display = ", ".join(missing_deuterocanon) if missing_deuterocanon else "None"
    try:
        source_display = source_path.relative_to(ROOT).as_posix()
    except ValueError:
        source_display = str(source_path)
    source_note = (
        "- Supplemental Brenton notes: Brenton USFM footnotes are included. TSK study-note text is intentionally excluded because it is too large for this Logos source. Hebrew and Greek vocabulary notes are excluded because Logos already provides lexical lookup layers. Proper-name and divine-title notes are integrated as name-meaning notes."
        if testament == "ot"
        else "- Supplemental source notes: no NT supplemental source-note layer is currently enabled. TSK study-note text is intentionally excluded because it is too large for this Logos source. Greek vocabulary notes are excluded because Logos already provides lexical lookup layers. Proper-name and divine-title notes are integrated as name-meaning notes."
    )
    variant_note = (
        f"- Translation notes: reviewed rows from `data/research/translation_footnotes.csv`. Generic MT/LXX difference rows are skipped unless `{translation_decisions_display}` supports a concrete local detail, such as a substantive number/unit difference. Those concrete rows are labeled `MT/LXX note`."
        if testament == "ot"
        else "- Translation notes: reviewed rows from `data/research/translation_footnotes.csv` plus any local textual-note export entries matching NT references. OT-specific MT/LXX rows are ignored for this NT source."
    )
    future_work_note = (
        f"- Future work: deuterocanonical/apocrypha intro rows exist, but current source text does not yet include these books: {missing_deuterocanon_display}."
        if testament == "ot"
        else "- Future work: NT literal revision is seeded from the public-domain UKJV alignment and still needs verse-by-verse TR Greek review."
    )
    bridge_heading = "MT-note bridge import" if testament == "ot" else "Reference-note bridge import"
    bridge_note = (
        f"Use `{mt_bridge_docx.name}` instead of `{logos_docx.name}` when the goal is to surface notes already anchored to standard MT/English Bible references. The visible verse numbers remain from the LXX source rows, but hidden milestones are remapped to standard Bible references where a reliable mapping is available."
        if testament == "ot"
        else f"`{mt_bridge_docx.name}` is emitted for parity with the OT build. NT TR source rows already use standard NT versification, so this bridge should normally match the main Logos source."
    )
    source_basis_note = (
        f"- Source text: `{source_display}`."
        if testament == "ot"
        else f"- Source text: `{source_display}`, imported from byztxt/greektext-scrivener Scrivener 1894 Textus Receptus text-only files."
    )
    bridge_file_note = (
        "Logos Personal Book source with verse milestones remapped to standard English/MT references so existing reference-anchored Logos notes from MT-based Bibles can show. Compile as resource type `Bible`."
        if testament == "ot"
        else "Logos Personal Book source emitted for parity with the OT reference-bridge output. NT TR source rows already use standard NT milestones. Compile as resource type `Bible`."
    )
    crossref_note = (
        "- Cross-references: TSK primary set from `data/raw/TSK.zip`; OpenBible fallback from `data/raw/cross-references.zip` where TSK has no verse row. TSK catchwords are used as word/phrase anchors when they exactly match the fresh translation; otherwise cross-references remain verse-anchored. See root `NOTICE.md` for public-domain/CC-BY attribution details."
        if crossrefs_enabled
        else "- Cross-references: omitted because `--no-crossrefs` was used."
    )
    content = f"""# Fresh Translation {config["label"]} Logos/Proofreading Files

Generated files:

- `{logos_docx.name}`: Logos Personal Book source. Compile as resource type `Bible`.
- `{mt_bridge_docx.name}`: {bridge_file_note}
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

{bridge_heading}:

{bridge_note}

Scope:

- Source basis: {config["source_text"]}.
{source_basis_note}
- Book preface pages: `{book_intros_display}`. These are inserted before each book's chapter text in all generated DOCX files.
{variant_note}
- Name meanings: `data/proper_names.csv`, `data/proper_name_transliteration_notes.csv`, and `data/names_of_god.csv`. Proper-name notes and unambiguous multi-word divine-title notes are placed at the first exact occurrence per chapter. Ambiguous single-word divine-title notes remain source-reference anchored to avoid assigning the wrong source-language title from English alone.
{source_note}
- Local textual-note export: generated from `{textual_notes_display}` when present. Note text is embedded into this Personal Book as local `Textual note` footnotes; no `logosres:` links or external Logos resource layer are emitted.
{future_work_note}
- Place links: conservative Logos `BibleKnowledgebase` datatype links are added for unambiguous primary place labels found in the local Logos autocomplete database. These are clickable Factbook/place links; Personal Book source does not expose the same internal atlas-pin overlay used by Logos-edition Bibles.
{crossref_note}
- Footnote numbering: one DOCX file with internal Word section metadata set to restart visible footnote numbering by `{footnote_number_restart}`. Cross-reference footnotes use normal numeric Word footnote references because Logos 49 Personal Book import crashes while converting large DOCX files that use custom footnote marks.

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
    variant_decision_counts: dict[str, int],
    textual_export_counts: dict[str, object],
    notes: dict[str, list[TranslationNote]],
    book_intro_diag: dict[str, object],
    deuterocanonical_work: dict[str, object],
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
    place_link_diag: dict[str, object],
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
        "translation_decision_filter": variant_decision_counts,
        "textual_note_export": textual_export_counts,
        "included_translation_note_refs": len(notes),
        "included_translation_note_total": included_note_total,
        "book_prefaces": book_intro_diag,
        "deuterocanonical_future_work": deuterocanonical_work,
        "name_meaning_note_filter": name_note_counts,
        "included_name_meaning_note_refs": len(name_notes),
        "included_name_meaning_note_total": included_name_note_total,
        "supplemental_notes": supplemental_note_counts,
        "included_supplemental_note_refs": len(supplemental_notes),
        "included_supplemental_note_total": included_supplemental_note_total,
        "crossrefs": crossref_diag,
        "place_links": place_link_diag,
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
    parser.add_argument("--translation-decisions", type=Path, default=DEFAULT_TRANSLATION_DECISIONS)
    parser.add_argument("--proper-names", type=Path, default=DEFAULT_PROPER_NAMES)
    parser.add_argument("--transliterated-proper-names", type=Path, default=DEFAULT_TRANSLITERATED_PROPER_NAMES)
    parser.add_argument("--names-of-god", type=Path, default=DEFAULT_NAMES_OF_GOD)
    parser.add_argument("--book-intros", type=Path, default=DEFAULT_BOOK_INTROS)
    parser.add_argument("--logos-docx", type=Path, default=DEFAULT_LOGOS_DOCX)
    parser.add_argument("--mt-bridge-docx", type=Path, default=DEFAULT_MT_BRIDGE_DOCX)
    parser.add_argument("--proof-docx", type=Path, default=DEFAULT_PROOF_DOCX)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--preview", type=Path, default=DEFAULT_PREVIEW)
    parser.add_argument("--versification-map", type=Path, default=DEFAULT_VERSIFICATION_MAP)
    parser.add_argument("--textual-notes-html", type=Path, default=DEFAULT_TEXTUAL_NOTES_HTML)
    parser.add_argument("--lexham-textual-notes-html", type=Path, dest="textual_notes_html", help=argparse.SUPPRESS)
    parser.add_argument("--logos-root", type=Path, default=DEFAULT_LOGOS_ROOT)
    parser.add_argument("--testament", choices=tuple(TESTAMENT_CONFIG), default="ot")
    parser.add_argument(
        "--place-links",
        action="store_true",
        help="Enable experimental Logos Bible Knowledgebase place links. Disabled by default because Personal Books can surface unresolved markup.",
    )
    parser.add_argument("--no-place-links", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--datatype", default="Bible")
    parser.add_argument(
        "--footnote-number-restart",
        choices=("chapter", "book", "continuous"),
        default="chapter",
        help="Visible footnote numbering restart scope inside the single DOCX file.",
    )
    parser.add_argument(
        "--no-crossrefs",
        action="store_true",
        help="Omit the TSK/OpenBible cross-reference footnote layer.",
    )
    args = parser.parse_args()
    config = TESTAMENT_CONFIG[args.testament]

    verses = load_verses(args.source)
    versification_map, versification_map_diag = load_versification_map(args.versification_map)
    variant_decisions, variant_decision_counts = load_variant_decisions(args.translation_decisions)
    base_notes, note_counts = load_translation_notes(args.footnotes, variant_decisions)
    textual_export_notes, textual_export_counts = load_textual_notes_export(
        args.textual_notes_html,
        verses,
        versification_map,
    )
    notes = filter_translation_notes_to_verses(
        merge_translation_notes(base_notes, textual_export_notes),
        verses,
    )
    book_intros, book_intro_diag = load_book_intros(args.book_intros)
    deuterocanonical_work = (
        deuterocanonical_future_work(book_intros, verses)
        if args.testament == "ot"
        else {"enabled": False, "reason": "Not applicable to NT build.", "missing_book_count": 0, "missing_books": []}
    )
    source_name_notes, name_note_counts = load_name_meaning_notes(
        proper_names_path=args.proper_names,
        transliterated_proper_names_path=args.transliterated_proper_names,
        names_of_god_path=args.names_of_god,
        source_filter=args.testament,
    )
    name_notes, name_note_placement_counts = place_name_meaning_notes_by_chapter(verses, source_name_notes)
    name_note_counts = {
        **name_note_counts,
        **{f"placement_{key}": value for key, value in name_note_placement_counts.items()},
    }
    crossrefs, crossref_diag = build_crossrefs_for_verses(
        verses,
        args.testament,
        enabled=not args.no_crossrefs,
    )
    if not args.place_links or args.no_place_links:
        place_links: dict[str, PlaceLink] = {}
        place_link_diag: dict[str, object] = {
            "enabled": False,
            "reason": "Disabled by default; experimental Personal Book place links can surface unresolved markup.",
            "candidate_labels": 0,
        }
    else:
        place_links, place_link_diag = load_logos_place_links(args.logos_root, args.proper_names)
    place_link_pattern = build_place_link_pattern(place_links)
    if args.testament == "ot":
        brenton_supplemental_notes, brenton_supplemental_counts = load_brenton_supplemental_notes(verses)
    else:
        brenton_supplemental_notes = {}
        brenton_supplemental_counts = {
            "enabled": False,
            "reason": "No NT supplemental source-note layer enabled.",
        }
    supplemental_notes = merge_supplemental_notes(brenton_supplemental_notes)
    supplemental_note_counts: dict[str, object] = {
        "brenton_package": brenton_supplemental_counts,
        "included_refs": len(supplemental_notes),
        "included_total": sum(len(items) for items in supplemental_notes.values()),
    }
    verse_counts = json.loads((DATA / "kjv_versification.json").read_text(encoding="utf-8"))

    logos_stats = build_docx(
        path=args.logos_docx,
        title=f"{config['title_prefix']} - Logos Bible Source",
        description=config["description"],
        testament=args.testament,
        verses=verses,
        translation_notes=notes,
        name_notes=name_notes,
        supplemental_notes=supplemental_notes,
        crossrefs=crossrefs,
        book_intros=book_intros,
        logos=True,
        datatype=args.datatype,
        milestone_mode="lxx",
        versification_map=versification_map,
        verse_counts=verse_counts,
        footnote_number_restart=args.footnote_number_restart,
        place_links=place_links,
        place_link_pattern=place_link_pattern,
        crossrefs_enabled=not args.no_crossrefs,
    )
    mt_bridge_stats = build_docx(
        path=args.mt_bridge_docx,
        title=f"{config['title_prefix']} - {config['bridge_label']}",
        description=config["description"],
        testament=args.testament,
        verses=verses,
        translation_notes=notes,
        name_notes=name_notes,
        supplemental_notes=supplemental_notes,
        crossrefs=crossrefs,
        book_intros=book_intros,
        logos=True,
        datatype=args.datatype,
        milestone_mode="mt",
        versification_map=versification_map,
        verse_counts=verse_counts,
        footnote_number_restart=args.footnote_number_restart,
        place_links=place_links,
        place_link_pattern=place_link_pattern,
        crossrefs_enabled=not args.no_crossrefs,
    )
    proof_stats = build_docx(
        path=args.proof_docx,
        title=f"{config['title_prefix']} - Proofreading Copy",
        description=config["description"],
        testament=args.testament,
        verses=verses,
        translation_notes=notes,
        name_notes=name_notes,
        supplemental_notes=brenton_supplemental_notes,
        crossrefs=crossrefs,
        book_intros=book_intros,
        logos=False,
        datatype=args.datatype,
        milestone_mode="lxx",
        versification_map=versification_map,
        verse_counts=verse_counts,
        footnote_number_restart=args.footnote_number_restart,
        place_links={},
        place_link_pattern=None,
        crossrefs_enabled=not args.no_crossrefs,
    )
    build_preview(args.preview, verses, notes, supplemental_notes, crossrefs, config["preview_title"])
    build_readme(
        args.readme,
        testament=args.testament,
        config=config,
        source_path=args.source,
        logos_docx=args.logos_docx,
        mt_bridge_docx=args.mt_bridge_docx,
        proof_docx=args.proof_docx,
        diagnostics_path=args.diagnostics,
        preview_path=args.preview,
        datatype=args.datatype,
        footnote_number_restart=args.footnote_number_restart,
        textual_notes_html=args.textual_notes_html,
        book_intros_path=args.book_intros,
        translation_decisions_path=args.translation_decisions,
        deuterocanonical_work=deuterocanonical_work,
        crossrefs_enabled=not args.no_crossrefs,
    )
    validations = [validate_docx(args.logos_docx), validate_docx(args.mt_bridge_docx), validate_docx(args.proof_docx)]
    diagnostics = build_diagnostics(
        verses=verses,
        note_counts=note_counts,
        variant_decision_counts=variant_decision_counts,
        textual_export_counts=textual_export_counts,
        notes=notes,
        book_intro_diag=book_intro_diag,
        deuterocanonical_work=deuterocanonical_work,
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
        place_link_diag=place_link_diag,
    )
    args.diagnostics.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(diagnostics["outputs"], indent=2))


if __name__ == "__main__":
    main()
