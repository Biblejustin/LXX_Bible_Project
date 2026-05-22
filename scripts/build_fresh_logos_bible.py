#!/usr/bin/env python3
"""Build Logos Personal Book and proofreading DOCX files for fresh sources."""

from __future__ import annotations

import argparse
import csv
import difflib
import html
import json
import re
import sqlite3
import sys
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Callable, Iterable, TypeVar
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape

from fresh_bible.book_scope import filter_items_by_book
from fresh_bible.cache import cached_result
from fresh_bible.pipeline_common import load_csv, load_required_csv

try:
    from build_study_bible import (
        OPENBIBLE_BOOK_MAP,
        OPENBIBLE_CROSSREFS_ZIP,
        STANDARD_BOOK_NAMES,
        BRENTON_ZIP,
        KJV_V11N_JSON,
        TSK_NT_BOOKS,
        TSK_OT_BOOKS,
        TSK_ZIP,
        build_tsk_index_map,
        canonicalize_cross_references,
        decode_tsk_blob,
        extract_tsk_crossrefs,
        load_kjv_versification,
        parse_brenton_usfm,
        parse_cross_reference,
        parse_openbible_crossrefs,
        parse_tsk_module,
    )
except ImportError:  # pragma: no cover - supports module execution from repo root.
    from scripts.build_study_bible import (
        OPENBIBLE_BOOK_MAP,
        OPENBIBLE_CROSSREFS_ZIP,
        STANDARD_BOOK_NAMES,
        BRENTON_ZIP,
        KJV_V11N_JSON,
        TSK_NT_BOOKS,
        TSK_OT_BOOKS,
        TSK_ZIP,
        build_tsk_index_map,
        canonicalize_cross_references,
        decode_tsk_blob,
        extract_tsk_crossrefs,
        load_kjv_versification,
        parse_brenton_usfm,
        parse_cross_reference,
        parse_openbible_crossrefs,
        parse_tsk_module,
    )


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = DATA / "raw"
RESEARCH = DATA / "research"
OUTPUT = ROOT / "output" / "logos"
CACHE_DIR = ROOT / "output" / "working" / "cache"
INGEST_CACHE_VERSION = "fresh-logos-ingest-v2"

csv.field_size_limit(sys.maxsize)

DEFAULT_SOURCE = RAW / "lxx_greek" / "ot_full.csv"
DEFAULT_NT_SOURCE = RAW / "tr_greek" / "nt_full.csv"
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
DEFAULT_CROSSREF_TARGET_OVERRIDES = DATA / "crossref_target_overrides.csv"
DEFAULT_TEXTUAL_NOTES_HTML = RESEARCH / "textual_notes_export.html"
DEFAULT_LOGOS_ROOT = Path.home() / "Library" / "Application Support" / "Logos4"
GENESIS_CHRONOLOGY_COMPARISON = DATA / "genesis_chronology_comparison.csv"

DOCX_CORE_TIMESTAMP = "2000-01-01T00:00:00Z"
DOCX_ZIP_TIMESTAMP = (2000, 1, 1, 0, 0, 0)
DOCX_DEFAULT_COMPRESSLEVEL = 9
PRINT_RED = "9B1C1C"
PRINT_BLUE = "1F4E79"

REFERENCE_NUMBERING_GUIDE = [
    ("English Psalm 22:1", "Psalms 21:2 here"),
    ("English Psalm 23:1", "Psalms 22:1 here"),
    ("English Psalm 110:1", "Psalms 109:1 here"),
    ("English Psalm 119:1", "Psalms 118:1 here"),
    ("English Jeremiah 31:31", "Jeremiah 38:31 here"),
    ("English Isaiah 9:6", "Isaiah 9:5 here"),
    ("English Micah 5:2", "Micah 5:1 here"),
    ("English Malachi 4:5", "Malachi 3:22 here"),
    ("English Malachi 4:6", "Malachi 3:23 here"),
]

ARTICLE_SUPPLY_POLICY_NOTE = (
    "Article/readability policy: this draft sometimes supplies ordinary English "
    "articles or linking words where Greek uses a compact phrase and English "
    "requires smoother syntax; for example, an articular land phrase may be "
    'rendered "the land of Judah," and a compact proverb may receive "is" or '
    '"the" so the English sentence reads normally.'
)

SOURCE_BASIS_GUIDE = {
    "ot": [
        "OT source basis: this branch translates the normalized LXX Greek source rows in data/raw/lxx_greek/ot_full.csv; it does not revise an English base text.",
        ARTICLE_SUPPLY_POLICY_NOTE,
        "Daniel source basis: Daniel follows the Greek Daniel rows present in the Protestant-canon OT source workspace; the Greek additions (Song of the Three Young Men; Susanna; Bel and the Dragon) are emitted in the separate Deuterocanon edition.",
        "Canon scope: deuterocanonical and apocryphal LXX books are planned as a separate workstream, not folded into this Protestant-canon branch.",
    ],
    "nt": [
        "NT source basis: this branch translates the Scrivener 1894 Textus Receptus stream imported from byztxt/greektext-scrivener text-only files.",
    ],
    "combined": [
        "OT source basis: this branch translates the normalized LXX Greek source rows in data/raw/lxx_greek/ot_full.csv; it does not revise an English base text.",
        "NT source basis: this branch translates the Scrivener 1894 Textus Receptus stream imported from byztxt/greektext-scrivener text-only files.",
        ARTICLE_SUPPLY_POLICY_NOTE,
        "Daniel source basis: Daniel follows the Greek Daniel rows present in the Protestant-canon OT source workspace; the Greek additions (Song of the Three Young Men; Susanna; Bel and the Dragon) are emitted in the separate Deuterocanon edition.",
        "Canon scope: deuterocanonical and apocryphal LXX books are planned as a separate workstream, not folded into this Protestant-canon branch.",
    ],
    "deuterocanon": [
        "Deuterocanon source basis: this separate Logos source translates the LXX deuterocanon/additions Greek rows in data/raw/lxx_deuterocanon/deuterocanon_full.csv; it does not revise an English base text.",
        "Supplemental source basis: the pinned eBible GRCLXX package is primary, with the public-domain eBible Brenton Greek package used only for Prayer of Manasseh and true 2 Maccabees rows absent from GRCLXX.",
        "Output scope: this workstream is emitted as a separate Logos DOCX and is not included in the compact paper proof.",
    ],
}

PSALM_SUPERSCRIPTION_PREFIXES = (
    "A psalm",
    "Alleluia",
    "For end",
    "For the end",
    "For understanding",
    "Of ",
    "Ode",
    "Prayer",
    "Praise of",
    "Psalm",
    "Song",
    "To the end",
    "Understanding",
)

T = TypeVar("T")


def cached_ingest_result(
    label: str,
    dependencies: Iterable[Path],
    params: dict[str, object],
    producer: Callable[[], T],
) -> tuple[T, dict[str, object]]:
    return cached_result(
        label=label,
        dependencies=dependencies,
        params=params,
        producer=producer,
        cache_dir=CACHE_DIR,
        root=ROOT,
        version=INGEST_CACHE_VERSION,
        disable_env="FRESH_BIBLE_DISABLE_CACHE",
    )

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
    "combined": {
        "label": "Greek Heritage Study Bible",
        "full_label": "Old and New Testaments",
        "source_text": "OT LXX Greek and NT Scrivener 1894 Textus Receptus Greek",
        "title_prefix": "The Greek Heritage Study Bible",
        "bridge_label": "Reference Notes Bridge",
        "preview_title": "The Greek Heritage Study Bible Logos Bible Preview",
        "description": "The Greek Heritage Study Bible draft from OT LXX Greek and NT Scrivener 1894 Textus Receptus Greek.",
    },
    "deuterocanon": {
        "label": "LXX Deuterocanon",
        "full_label": "LXX Deuterocanon and Additions",
        "source_text": "LXX deuterocanon/additions Greek source rows",
        "title_prefix": "The Greek Heritage Study Bible Deuterocanon",
        "bridge_label": "Reference Notes Bridge",
        "preview_title": "The Greek Heritage Study Bible Deuterocanon Logos Preview",
        "description": "Separate Logos draft of the LXX deuterocanon and additions for The Greek Heritage Study Bible.",
    },
}

DOCX_W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
DOCX_R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
DOCX_MC_NS = "http://schemas.openxmlformats.org/markup-compatibility/2006"
DOCX_W15_NS = "http://schemas.microsoft.com/office/word/2012/wordml"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CONTENT_TYPES_NS = "http://schemas.openxmlformats.org/package/2006/content-types"

LXX_TSK_CODE_MAP = {
    "DAN": "DAG",
    "EST": "ESG",
}

LOGOS_SOURCE_CODE_MAP = LXX_TSK_CODE_MAP
STANDARD_CODE_BY_BOOK_NAME = {name: code for code, name in STANDARD_BOOK_NAMES.items()}
LEADING_INT_RE = re.compile(r"^(\d+)")

LOGOS_BOOK_NAME_OVERRIDES = {
    "ESGA": "Esther",
    "LJE": "Letter of Jeremiah",
}

LOGOS_DEUTEROCANON_SUPPRESSED_BOOK_CODES = {
    # This source is Greek Ezra B, not the Latin apocalypse normally indexed as
    # 2 Esdras in Logos' Bible datatype.
    "2ES",
}

LOGOS_DEUTEROCANON_SUPPRESSED_CODE_REFS = {
    "TOB 6:19",
    "TOB 7:17",
    "TOB 13:18",
    "WIS 2:25",
    "WIS 9:19",
    "SIR 28:24",
    "SIR 28:25",
    "SIR 36:14",
    "SIR 36:15",
    "SIR 41:23",
    "SIR 41:24",
    "SIR 41:25",
    "SIR 41:26",
    "SIR 41:27",
    "SIR 43:17",
    "BAR 3:38",
    "4MA 12:20",
}


def leading_int_label(value: str, *, field_name: str) -> int:
    match = LEADING_INT_RE.match(value.strip())
    if not match:
        raise ValueError(f"Cannot read numeric {field_name} from label: {value!r}")
    return int(match.group(1))
STANDARD_CODE_BY_BOOK_NAME["Song of Songs"] = "SNG"

CODE_REF_RE = re.compile(r"^([1-3]?[A-Z0-9]+) (\d+):(\d+)$")
DISPLAY_REF_RE = re.compile(r"^(.+?) (\d+):(\d+)$")
CROSSREF_SAME_CHAPTER_RANGE_RE = re.compile(r"^(.+?) (\d+):(\d+)-(\d+)$")
CROSSREF_CHAPTER_RANGE_RE = re.compile(r"^(.+?) (\d+):(\d+)-(\d+):(\d+)$")
CROSSREF_FULL_RANGE_RE = re.compile(r"^(.+?) (\d+):(\d+)-(.+?) (\d+):(\d+)$")

GENERIC_FOOTNOTE_PATTERNS = (
    "Brenton differs here. The translation follows the current fresh wording at this verse numbering point.",
    "Greek line matches current rendering closely here.",
    "Greek preserves its own proper-name form in this register. The translation follows it.",
)
GENERIC_FOOTNOTE_PREFIXES = (
    "Cross-reference review revised malformed literal wording while following the local Greek",
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
TRIGGER_TOKEN_RE = re.compile(r"[A-Za-z0-9]+")
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
    chapter_label: str = ""
    verse_label: str = ""

    @property
    def display_chapter(self) -> str:
        return self.chapter_label or str(self.chapter)

    @property
    def display_verse(self) -> str:
        return self.verse_label or str(self.verse)

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
        return translation_note_display_text(self)


def translation_note_display_text(note: TranslationNote, *, compact_label: bool = False) -> str:
    if note.note_type == "mt_lxx":
        prefix = "MT/LXX" if compact_label else "MT/LXX note"
    elif note.note_type == "textual":
        prefix = "Txt" if compact_label else "Textual note"
    else:
        prefix = "T" if compact_label else "Translation note"
    return f"{prefix}: {reader_facing_note_text(note.text)}"


@dataclass(frozen=True)
class CrossReferenceNote:
    trigger_phrase: str
    refs: tuple[str, ...]
    source: str
    display_phrase: str = ""

    @property
    def display_text(self) -> str:
        phrase = self.display_phrase or self.trigger_phrase
        prefix = (
            f'Cross-references for "{phrase}": '
            if phrase
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
        return name_note_display_text(self)


COMPACT_NAME_NOTE_REPLACEMENTS = (
    ("Hebrew divine name/title:", "Heb:"),
    ("Greek LXX divine name/title:", "Gk:"),
    ("Divine or supernatural name:", "Div:"),
    ("Divine/supernatural-name meaning:", "Nm:"),
    ("Transliterated proper noun:", "Tr:"),
    ("Standard English equivalent:", "Std:"),
    ("Common English rendering:", "Eng:"),
    ("UKJV form:", "UKJV:"),
    ("Personal-name meaning:", "Nm:"),
    ("Personal name:", "Pn:"),
    ("Place-name meaning:", "Nm:"),
    ("Place name:", "Pl:"),
    ("People-name meaning:", "Nm:"),
    ("People-name:", "Ppl:"),
    ("Name meaning:", "Nm:"),
    ("Source form:", "Src:"),
    ("Greek form:", "Gk:"),
)


def name_note_display_text(note: NameMeaningNote, *, compact_label: bool = False) -> str:
    text_value = reader_facing_note_text(note.text)
    if not compact_label:
        return text_value
    for verbose, compact in COMPACT_NAME_NOTE_REPLACEMENTS:
        text_value = text_value.replace(verbose, compact)
    return text_value


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
    run_in_verse_paragraphs: bool = False
    run_in_group_size: int = 0
    pericope_heading_count: int = 0
    footnote_columns: int = 1
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
    suppressed_duplicate_milestone_refs: int = 0
    suppressed_unsupported_milestone_refs: int = 0
    superscription_line_count: int = 0


@dataclass(frozen=True)
class MilestoneResolution:
    logos_ref: str
    source_ref: str
    mapped_ref: str
    status: str


def footnote_restart_xml_value(scope: str) -> str:
    return {
        "book": "eachSect",
        "chapter": "eachSect",
        "continuous": "continuous",
        "page": "eachPage",
    }.get(scope, "eachSect")


class MinimalDocx:
    """Small WordprocessingML writer with real footnote support."""

    def __init__(
        self,
        title: str,
        subject: str,
        *,
        compact_print: bool = False,
        lulu_pod_margins: bool = False,
        footnote_number_restart: str = "chapter",
        footnote_columns: int = 1,
    ) -> None:
        self.title = title
        self.subject = subject
        self.compact_print = compact_print
        self.lulu_pod_margins = lulu_pod_margins
        self.footnote_restart_value = footnote_restart_xml_value(footnote_number_restart)
        self.footnote_columns = footnote_columns
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
            ppr_parts.append(
                section_properties_xml(
                    section_type="continuous",
                    compact_print=self.compact_print,
                    lulu_pod_margins=self.lulu_pod_margins,
                    footnote_restart_value=self.footnote_restart_value,
                    footnote_columns=self.footnote_columns,
                )
            )
        ppr = f"<w:pPr>{''.join(ppr_parts)}</w:pPr>" if ppr_parts else ""
        self.body.append(f"<w:p>{ppr}{''.join(runs)}</w:p>")

    def add_heading(self, text: str, level: int = 1, *, section_break_after: bool = False) -> None:
        style = "Heading1" if level == 1 else "Heading2"
        self.add_paragraph([run(text)], style=style, section_break_after=section_break_after)

    def add_page_break(self) -> None:
        self.body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    def add_table(self, rows: list[list[list[str]]]) -> None:
        if not rows:
            return
        column_count = max(len(row) for row in rows)
        column_width = max(1, 5000 // column_count)
        grid = "".join(f'<w:gridCol w:w="{column_width}"/>' for _ in range(column_count))
        table_rows: list[str] = []
        for row in rows:
            cells: list[str] = []
            for cell_runs in row:
                cells.append(
                    "<w:tc>"
                    f'<w:tcPr><w:tcW w:w="{column_width}" w:type="pct"/></w:tcPr>'
                    f"<w:p>{''.join(cell_runs)}</w:p>"
                    "</w:tc>"
                )
            table_rows.append(f"<w:tr>{''.join(cells)}</w:tr>")
        self.body.append(
            "<w:tbl>"
            "<w:tblPr>"
            '<w:tblW w:w="5000" w:type="pct"/>'
            '<w:tblBorders>'
            '<w:top w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
            '<w:left w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
            '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
            '<w:right w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
            '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
            '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
            "</w:tblBorders>"
            "</w:tblPr>"
            f"<w:tblGrid>{grid}</w:tblGrid>"
            f"{''.join(table_rows)}"
            "</w:tbl>"
        )

    def add_footnote(self, text: str) -> int:
        self.footnotes.append(FootnoteEntry(text=text))
        return len(self.footnotes)

    def save(self, path: Path, *, compresslevel: int = DOCX_DEFAULT_COMPRESSLEVEL) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        document_xml = build_document_xml(
            "\n".join(self.body),
            compact_print=self.compact_print,
            lulu_pod_margins=self.lulu_pod_margins,
            footnote_restart_value=self.footnote_restart_value,
            footnote_columns=self.footnote_columns,
        )
        footnotes_xml = build_footnotes_xml(self.footnotes, compact_print=self.compact_print)
        files = {
            "[Content_Types].xml": content_types_xml(),
            "_rels/.rels": root_rels_xml(),
            "docProps/core.xml": core_props_xml(self.title, self.subject, DOCX_CORE_TIMESTAMP),
            "docProps/app.xml": app_props_xml(),
            "word/document.xml": document_xml,
            "word/_rels/document.xml.rels": document_rels_xml(),
            "word/styles.xml": styles_xml(
                compact_print=self.compact_print,
                lulu_pod_margins=self.lulu_pod_margins,
            ),
            "word/settings.xml": settings_xml(
                footnote_restart_value=self.footnote_restart_value,
                mirror_margins=self.lulu_pod_margins,
            ),
            "word/footnotes.xml": footnotes_xml,
        }
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=compresslevel) as zf:
            for name, payload in files.items():
                info = zipfile.ZipInfo(name, date_time=DOCX_ZIP_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o600 << 16
                zf.writestr(info, payload, compresslevel=compresslevel)


def attr(text: str) -> str:
    return escape(str(text), {'"': "&quot;"})


def text(text_value: str) -> str:
    return escape(str(text_value))


HEBREW_CLUSTER_RE = re.compile(r"[\u0590-\u05ff]+(?:\s+[\u0590-\u05ff]+)*")


def runs_for_plain_text(
    value: str,
    *,
    bold: bool = False,
    italic: bool = False,
    style: str | None = None,
    small: bool = False,
    color: str | None = None,
    size: str | None = None,
    complex_size: str | None = None,
) -> list[str]:
    """Split Hebrew spans into language-tagged RTL runs for Logos import."""
    output: list[str] = []
    cursor = 0
    for match in HEBREW_CLUSTER_RE.finditer(value):
        if cursor < match.start():
            output.append(
                run(
                    value[cursor : match.start()],
                    bold=bold,
                    italic=italic,
                    style=style,
                    small=small,
                    color=color,
                    size=size,
                    complex_size=complex_size,
                )
            )
        output.append(
            run(
                match.group(0),
                bold=bold,
                italic=italic,
                style=style,
                small=small,
                color=color,
                language="he-IL",
                rtl=True,
                size=size,
                complex_size=complex_size,
            )
        )
        cursor = match.end()
    if cursor < len(value):
        output.append(
            run(
                value[cursor:],
                bold=bold,
                italic=italic,
                style=style,
                small=small,
                color=color,
                size=size,
                complex_size=complex_size,
            )
        )
    return output


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


INTERNAL_NOTE_SENTENCE_PATTERNS = (
    re.compile(r"\s*Equivalent source: [^.]+\."),
    re.compile(r"\s*Direct Logos export [^.]+\."),
    re.compile(r"\s*Local Logos word-sense evidence supports [^.]+\."),
)
MECHANICAL_REVIEW_NOTE_RE = re.compile(
    r"^(?:Article review|Cross-reference review) supplied\b"
)
MECHANICAL_REVIEW_SOURCE_RE = re.compile(r"\barticle(?: syntax| supplied)?\b")


def reader_facing_note_text(value: str) -> str:
    text_value = normalize_space(value)
    if not any(marker in text_value for marker in ("Equivalent source:", "Direct Logos export", "Local Logos word-sense evidence supports")):
        return text_value
    for pattern in INTERNAL_NOTE_SENTENCE_PATTERNS:
        text_value = pattern.sub("", text_value)
    return normalize_space(text_value)


def is_mechanical_review_note(note: TranslationNote) -> bool:
    source_basis = normalize_space(note.source_basis).lower()
    return (
        note.note_type == "translation"
        and (
            MECHANICAL_REVIEW_NOTE_RE.match(normalize_space(note.text)) is not None
            or MECHANICAL_REVIEW_SOURCE_RE.search(source_basis) is not None
        )
    )


def filter_reader_facing_translation_notes(
    notes: dict[str, list[TranslationNote]],
) -> tuple[dict[str, list[TranslationNote]], dict[str, int]]:
    filtered: dict[str, list[TranslationNote]] = {}
    counts = Counter(
        {
            "input_refs": len(notes),
            "input_notes": sum(len(items) for items in notes.values()),
        }
    )
    skipped_variants: set[str] = set()
    for ref, items in notes.items():
        kept: list[TranslationNote] = []
        for note in items:
            if is_mechanical_review_note(note):
                counts["skipped_mechanical_review_notes"] += 1
                skipped_variants.add(normalize_space(note.text))
                continue
            kept.append(note)
            counts["included_notes"] += 1
        if kept:
            filtered[ref] = kept
    counts["included_refs"] = len(filtered)
    counts["skipped_mechanical_review_note_variants"] = len(skipped_variants)
    return filtered, dict(counts)


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
    def verse_run(value: str) -> str:
        return run(normalize_bible_text_for_output(value))

    relevant = [span for span in place_spans if start <= span.start and span.end <= end]
    if not relevant:
        return [verse_run(verse_text[start:end])]

    output: list[str] = []
    cursor = start
    for span in relevant:
        if cursor < span.start:
            output.append(verse_run(verse_text[cursor:span.start]))
        label = normalize_bible_text_for_output(verse_text[span.start:span.end])
        output.append(run(f"[[{label} >> BibleKnowledgebase:{span.link.pb_reference}]]"))
        cursor = span.end
    if cursor < end:
        output.append(verse_run(verse_text[cursor:end]))
    return output


def normalize_bible_text_for_output(value: str) -> str:
    """Use KJV-style unmarked speech in the published Bible text."""
    value = value.replace('"', "")
    value = re.sub(r"(?<![A-Za-z0-9])'|'(?![A-Za-z0-9])", "", value)
    value = re.sub(r"\s+([,.;:!?])", r"\1", value)
    return value


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
        if trigger[-1].isalnum() and verse_text[end : end + 2].casefold() in {"'s", "’s"}:
            end += 2
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
    language: str | None = None,
    rtl: bool = False,
    size: str | None = None,
    complex_size: str | None = None,
) -> str:
    props: list[str] = []
    if style:
        props.append(f'<w:rStyle w:val="{attr(style)}"/>')
    if bold:
        props.append("<w:b/>")
    if italic:
        props.append("<w:i/>")
    if size:
        props.append(f'<w:sz w:val="{attr(size)}"/>')
    elif small:
        props.append('<w:sz w:val="18"/>')
    if complex_size:
        props.append(f'<w:szCs w:val="{attr(complex_size)}"/>')
    if color:
        props.append(f'<w:color w:val="{attr(color)}"/>')
    if language:
        props.append(f'<w:lang w:val="{attr(language)}" w:bidi="{attr(language)}"/>')
    if rtl:
        props.append("<w:rtl/>")
    rpr = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
    return f'<w:r>{rpr}<w:t xml:space="preserve">{text(value)}</w:t></w:r>'


def line_break_run() -> str:
    return "<w:r><w:br/></w:r>"


def footnote_reference_style_xml() -> str:
    return '<w:rPr><w:rStyle w:val="FootnoteReference"/></w:rPr>'


def compact_footnote_marker_style_xml(*, compact_print: bool) -> str:
    if not compact_print:
        return footnote_reference_style_xml()
    return (
        "<w:rPr>"
        '<w:vertAlign w:val="baseline"/>'
        "<w:b/>"
        f'<w:color w:val="{PRINT_BLUE}"/>'
        f'<w:sz w:val="{COMPACT_PRINT_FOOTNOTE_SIZE}"/>'
        f'<w:szCs w:val="{COMPACT_PRINT_FOOTNOTE_COMPLEX_SIZE}"/>'
        "</w:rPr>"
    )


def footnote_ref_run(note_id: int) -> str:
    return (
        f'<w:r>{footnote_reference_style_xml()}'
        f'<w:footnoteReference w:id="{note_id}"/></w:r>'
    )


def section_properties_xml(
    *,
    section_type: str | None = None,
    compact_print: bool = False,
    lulu_pod_margins: bool = False,
    footnote_restart_value: str = "eachSect",
    footnote_columns: int = 1,
) -> str:
    section_type_xml = f'<w:type w:val="{attr(section_type)}"/>' if section_type else ""
    if lulu_pod_margins:
        margins = (
            '<w:pgMar w:top="720" w:right="720" w:bottom="720" w:left="1080" '
            'w:header="360" w:footer="360" w:gutter="0"/>'
        )
    elif compact_print:
        margins = (
            '<w:pgMar w:top="720" w:right="540" w:bottom="720" w:left="540" '
            'w:header="360" w:footer="360" w:gutter="0"/>'
        )
    else:
        margins = (
            '<w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080" '
            'w:header="720" w:footer="720" w:gutter="0"/>'
        )
    columns = '<w:cols w:space="720" w:num="1"/>' if compact_print else ""
    footnote_columns_xml = (
        f'<w15:footnoteColumns w15:val="{int(footnote_columns)}"/>'
        if footnote_columns > 1
        else ""
    )
    return (
        "<w:sectPr>"
        f'<w:footnotePr><w:numRestart w:val="{attr(footnote_restart_value)}"/><w:numFmt w:val="decimal"/></w:footnotePr>'
        f"{section_type_xml}"
        '<w:pgSz w:w="12240" w:h="15840"/>'
        f"{margins}"
        f"{columns}"
        f"{footnote_columns_xml}"
        "</w:sectPr>"
    )


def build_document_xml(
    body_xml: str,
    *,
    compact_print: bool = False,
    lulu_pod_margins: bool = False,
    footnote_restart_value: str = "eachSect",
    footnote_columns: int = 1,
) -> str:
    section = section_properties_xml(
        compact_print=compact_print,
        lulu_pod_margins=lulu_pod_margins,
        footnote_restart_value=footnote_restart_value,
        footnote_columns=footnote_columns,
    )
    extra_namespaces = (
        f' xmlns:mc="{DOCX_MC_NS}" xmlns:w15="{DOCX_W15_NS}" mc:Ignorable="w15"'
        if footnote_columns > 1
        else ""
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<w:document xmlns:w="{DOCX_W_NS}" xmlns:r="{DOCX_R_NS}"{extra_namespaces}>'
        f"<w:body>{body_xml}{section}</w:body></w:document>"
    )


COMPACT_PRINT_FOOTNOTE_SIZE = "15"
COMPACT_PRINT_FOOTNOTE_COMPLEX_SIZE = "13"


def strip_redundant_print_name_fields(value: str) -> str:
    head = re.match(r"^(?P<label>Pn|Pl|Ppl|Div|Tr): (?P<name>[^.]+)\. (?P<body>.*)$", value)
    if not head:
        return re.sub(r"^Nm: [^:]{1,80}: ", "Nm: ", value)

    name = normalize_space(head.group("name"))
    body = head.group("body")
    if not name:
        return value

    for label in ("Std", "Src"):
        body = re.sub(
            rf"(?:(?<=^)|(?<=\s)){label}: {re.escape(name)}\. ?",
            "",
            body,
        )
    body = re.sub(
        rf"(?:(?<=^)|(?<=\s))Nm: {re.escape(name)}: ",
        "Nm: ",
        body,
    )
    return normalize_space(f"{head.group('label')}: {name}. {body}")


def compact_print_footnote_text(value: str) -> str:
    value = normalize_space(value)
    value = re.sub(r"\s+[—–]\s+", ": ", value)
    value = value.replace("—", ": ").replace("–", "-")
    value = re.sub(r'^Cross-references for "([^"]+)": ', r"X: \1: ", value)
    value = re.sub(r"^Cross-references: ", "X: ", value)
    if value.startswith("X: "):
        value = re.sub(r"\.$", "", value)
        value = value.replace("; ", " ")
    value = strip_redundant_print_name_fields(value)
    return normalize_space(value)


def build_footnotes_xml(notes: list[FootnoteEntry], *, compact_print: bool = False) -> str:
    items = [
        '<w:footnote w:type="separator" w:id="-1"><w:p><w:r><w:separator/></w:r></w:p></w:footnote>',
        '<w:footnote w:type="continuationSeparator" w:id="0"><w:p><w:r><w:continuationSeparator/></w:r></w:p></w:footnote>',
    ]
    footnote_text_size = COMPACT_PRINT_FOOTNOTE_SIZE if compact_print else None
    footnote_complex_size = COMPACT_PRINT_FOOTNOTE_COMPLEX_SIZE if compact_print else footnote_text_size
    for index, note in enumerate(notes, start=1):
        note_text = compact_print_footnote_text(note.text) if compact_print else note.text
        marker_run = f'<w:r>{compact_footnote_marker_style_xml(compact_print=compact_print)}<w:footnoteRef/></w:r>'
        items.append(
            f'<w:footnote w:id="{index}">'
            '<w:p><w:pPr><w:pStyle w:val="FootnoteText"/></w:pPr>'
            f"{marker_run}"
            f"{''.join(runs_for_plain_text(note_text, size=footnote_text_size, complex_size=footnote_complex_size))}"
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


def settings_xml(*, footnote_restart_value: str = "eachSect", mirror_margins: bool = False) -> str:
    mirror_margins_xml = "<w:mirrorMargins/>" if mirror_margins else ""
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<w:settings xmlns:w="{DOCX_W_NS}">'
        f"{mirror_margins_xml}"
        f'<w:footnotePr><w:numRestart w:val="{attr(footnote_restart_value)}"/><w:numFmt w:val="decimal"/></w:footnotePr>'
        "</w:settings>"
    )


def styles_xml(*, compact_print: bool = False, lulu_pod_margins: bool = False) -> str:
    normal_size = "19" if compact_print else "22"
    title_size = "32" if compact_print else "40"
    heading1_size = "24" if compact_print else "32"
    heading2_size = "21" if compact_print else "26"
    pericope_heading_size = "19" if compact_print else "22"
    footnote_size = COMPACT_PRINT_FOOTNOTE_SIZE if compact_print else "18"
    footnote_complex_size = COMPACT_PRINT_FOOTNOTE_COMPLEX_SIZE if compact_print else footnote_size
    footnote_ref_size = "17" if compact_print else "20"
    heading2_color = f'<w:color w:val="{PRINT_RED}"/>' if compact_print else ""
    footnote_ref_color = f'<w:color w:val="{PRINT_BLUE}"/>' if compact_print else ""
    footnote_line = "150" if compact_print else "200"
    normal_line = "200" if lulu_pod_margins else "220"
    normal_spacing = (
        f'<w:pPr><w:spacing w:before="0" w:after="0" w:line="{normal_line}" w:lineRule="auto"/></w:pPr>'
        if compact_print
        else ""
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        f'<w:styles xmlns:w="{DOCX_W_NS}">'
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
        '<w:name w:val="Normal"/><w:qFormat/>'
        f"{normal_spacing}"
        '<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>'
        f'<w:sz w:val="{normal_size}"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="paragraph" w:styleId="Title">'
        '<w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:qFormat/>'
        '<w:pPr><w:spacing w:after="240"/></w:pPr>'
        f'<w:rPr><w:b/><w:sz w:val="{title_size}"/></w:rPr>'
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
        f'<w:rPr><w:b/><w:sz w:val="{heading1_size}"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="paragraph" w:styleId="Heading2">'
        '<w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:qFormat/>'
        '<w:pPr><w:keepNext/><w:spacing w:before="240" w:after="120"/>'
        '<w:outlineLvl w:val="1"/></w:pPr>'
        f'<w:rPr><w:b/>{heading2_color}<w:sz w:val="{heading2_size}"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="paragraph" w:styleId="PericopeHeading">'
        '<w:name w:val="Pericope Heading"/><w:basedOn w:val="Normal"/><w:qFormat/>'
        '<w:pPr><w:keepNext/><w:spacing w:before="120" w:after="30"/></w:pPr>'
        f'<w:rPr><w:b/><w:i/><w:sz w:val="{pericope_heading_size}"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="character" w:styleId="FootnoteReference">'
        '<w:name w:val="Footnote Reference"/><w:semiHidden/><w:unhideWhenUsed/>'
        f'<w:rPr><w:vertAlign w:val="superscript"/><w:b/>{footnote_ref_color}<w:sz w:val="{footnote_ref_size}"/><w:szCs w:val="{footnote_ref_size}"/></w:rPr>'
        "</w:style>"
        '<w:style w:type="paragraph" w:styleId="FootnoteText">'
        '<w:name w:val="Footnote Text"/><w:basedOn w:val="Normal"/>'
        f'<w:pPr><w:spacing w:before="0" w:after="0" w:line="{footnote_line}" w:lineRule="auto"/></w:pPr>'
        f'<w:rPr><w:sz w:val="{footnote_size}"/><w:szCs w:val="{footnote_complex_size}"/></w:rPr>'
        "</w:style>"
        "</w:styles>"
    )


def load_verses(path: Path) -> list[Verse]:
    rows = load_required_csv(path)
    verses: list[Verse] = []
    for row in rows:
        draft = row.get("draft_translation", "").strip()
        if not draft:
            continue
        chapter_label = row["chapter"].strip()
        verse_label = row["verse"].strip()
        verses.append(
            Verse(
                ref=row["ref"].strip(),
                book_code=row["book_code"].strip(),
                book_name=row["book_name"].strip(),
                chapter=leading_int_label(chapter_label, field_name="chapter"),
                verse=leading_int_label(verse_label, field_name="verse"),
                text=draft,
                chapter_label=chapter_label,
                verse_label=verse_label,
            )
        )
    return verses


MT_ONLY_COMPLETENESS_REFS = {f"Jeremiah 40:{verse}" for verse in range(14, 27)}


def is_mt_only_completeness_verse(verse: Verse) -> bool:
    return verse.ref in MT_ONLY_COMPLETENESS_REFS


def split_psalm_superscription(verse: Verse) -> tuple[str, str] | None:
    if verse.book_name != "Psalms" or verse.verse != 1:
        return None

    sentences: list[str] = []
    cursor = 0
    for match in re.finditer(r"\.\s+", verse.text):
        sentences.append(verse.text[cursor : match.start() + 1].strip())
        cursor = match.end()
    tail = verse.text[cursor:].strip()
    if tail:
        sentences.append(tail)
    if not sentences or not is_psalm_superscription_sentence(sentences[0]):
        return None

    title_sentences: list[str] = []
    body_sentences: list[str] = []
    in_body = False
    for sentence in sentences:
        if not in_body and is_psalm_superscription_sentence(sentence):
            title_sentences.append(sentence)
        else:
            in_body = True
            body_sentences.append(sentence)

    superscription = " ".join(title_sentences).strip()
    body = " ".join(body_sentences).strip()
    if not superscription:
        return None
    return superscription, body


def is_psalm_superscription_sentence(sentence: str) -> bool:
    trimmed = sentence.strip()
    return any(trimmed.startswith(prefix) for prefix in PSALM_SUPERSCRIPTION_PREFIXES)


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
    rows = load_required_csv(path)
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
                english_equivalent = normalize_space(row.get("english_equivalent", ""))
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
                note_text = " ".join(pieces)
                triggers = [name]
                if english_equivalent and english_equivalent != name:
                    triggers.append(english_equivalent)
                    counts["transliterated_proper_name_alternate_triggers"] += 1
                for trigger in triggers:
                    grouped[ref].append(
                        NameMeaningNote(
                            trigger_phrase=trigger,
                            text=note_text,
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


def trigger_index_key(trigger: str, *, case_sensitive: bool) -> tuple[bool, str] | None:
    match = TRIGGER_TOKEN_RE.search(trigger)
    if not match:
        return None
    token = match.group(0)
    return case_sensitive, token if case_sensitive else token.casefold()


def verse_trigger_index_keys(text: str) -> set[tuple[bool, str]]:
    keys: set[tuple[bool, str]] = set()
    for match in TRIGGER_TOKEN_RE.finditer(text):
        token = match.group(0)
        keys.add((True, token))
        keys.add((False, token.casefold()))
    return keys


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
    display_text_cache = {note: note.display_text for note in scannable_notes}
    note_order = {note: index for index, note in enumerate(scannable_notes)}
    notes_by_trigger_token: dict[tuple[bool, str], list[NameMeaningNote]] = defaultdict(list)
    unindexed_notes: list[NameMeaningNote] = []
    for note in scannable_notes:
        key = trigger_index_key(note.trigger_phrase, case_sensitive=note.case_sensitive)
        if key is None:
            unindexed_notes.append(note)
        else:
            notes_by_trigger_token[key].append(note)

    for verse in verses:
        chapter_key = (verse.book_name, verse.chapter)
        candidate_notes = list(unindexed_notes)
        seen_candidates = set(candidate_notes)
        for key in verse_trigger_index_keys(verse.text):
            for note in notes_by_trigger_token.get(key, []):
                if note in seen_candidates:
                    continue
                candidate_notes.append(note)
                seen_candidates.add(note)
        candidate_notes.sort(key=note_order.__getitem__)
        for note in candidate_notes:
            seen_key = (*chapter_key, display_text_cache[note])
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
    if any(body.startswith(prefix) for prefix in GENERIC_FOOTNOTE_PREFIXES):
        return True
    source = row.get("source_basis", "").strip().lower()
    return source == "translation comparison" and body.startswith("Brenton differs here.")


def is_mt_lxx_difference_note(row: dict[str, str]) -> bool:
    haystack = f"{row.get('footnote_text', '')} {row.get('source_basis', '')}"
    return bool(MT_LXX_DIFFERENCE_RE.search(haystack))


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


INTRO_DATE_RANGES = {
    "Hasmonean period": "Hasmonean period, ca. 140-37 BC",
    "Herodian period": "Herodian period, ca. 37 BC-AD 70",
    "Hasmonean-Herodian periods": "Hasmonean-Herodian periods, ca. 140 BC-AD 70",
    "Second Temple period": "Second Temple period, ca. 516 BC-AD 70",
    "Late Second Temple period": "Late Second Temple period, ca. 200 BC-AD 70",
    "Hellenistic period": "Hellenistic period, ca. 332-63 BC",
    "Hellenistic and later": "Hellenistic and later, ca. 332 BC-AD 700",
    "Roman period": "Roman period, ca. 63 BC-AD 324",
    "Second Temple and medieval periods": "Second Temple and medieval periods, ca. 516 BC-AD 1500",
    "late antiquity": "late antiquity, ca. AD 300-700",
    "late antique and later": "late antique and later, ca. AD 300 and later",
    "late antique and medieval": "late antique and medieval, ca. AD 300-1500",
    "late antique and medieval periods": "late antique and medieval periods, ca. AD 300-1500",
    "medieval Ethiopic manuscripts": "medieval Ethiopic manuscripts, ca. AD 500-1500",
    "Second Temple and early Christian periods": "Second Temple and early Christian periods, ca. 516 BC-AD 400",
    "later Second Temple and early Christian periods": "later Second Temple and early Christian periods, ca. 200 BC-AD 400",
    "later Second Temple and after": "later Second Temple and after, ca. 200 BC-AD 400+",
    "Second Temple and later": "Second Temple and later, ca. 516 BC-AD 400+",
    "later biblical and post-biblical reception": "later biblical and post-biblical reception, ca. 7th century BC-AD 400+",
    "Persian period narrative and later canon": "Persian period narrative and later canon, ca. 539-332 BC and later",
    "exilic or late pre-exilic composition using earlier royal records": "exilic or late pre-exilic composition, ca. 7th-6th century BC, using earlier royal records",
    "exilic composition using earlier records and prophetic material": "exilic composition, ca. 6th century BC, using earlier records and prophetic material",
    "patriarchal-era setting; composition date debated": "patriarchal-era setting; composition date debated, broadly ca. 2nd-1st millennium BC",
    "date debated; conservative options range from early monarchy to post-exilic": "date debated; conservative options range from early monarchy to post-exilic, ca. 10th-5th century BC",
    "Hellenistic period composition using earlier story traditions": "Hellenistic period, ca. 332-63 BC, composition using earlier story traditions",
    "exilic frame; likely later composition history": "exilic frame, ca. 6th century BC; likely later composition history, ca. 3rd-1st century BC",
    "Hellenistic period or earlier tradition": "Hellenistic period or earlier tradition, ca. 332-63 BC or earlier",
    "Hellenistic or later": "Hellenistic or later, ca. 332 BC-AD 400",
}


def expand_intro_date(value: str) -> str:
    stripped = value.strip()
    if stripped.lower() == "n/a":
        return ""
    return INTRO_DATE_RANGES.get(stripped, stripped)


def intro_date_sort_year(value: str) -> int:
    text = expand_intro_date(value).replace("–", "-")
    candidates: list[int] = []
    century_phrase_re = re.compile(
        r"((?:early|mid|late|to|and|[-\s]|\d+(?:st|nd|rd|th))+)"
        r"\s+centur(?:y|ies)\s*(BC|AD)",
        re.I,
    )
    for phrase, era in century_phrase_re.findall(text):
        for ordinal in re.findall(r"\d+(?=st|nd|rd|th)", phrase, flags=re.I):
            century = int(ordinal)
            candidates.append(-century * 100 if era.upper() == "BC" else (century - 1) * 100)
    for left, _right in re.findall(r"\b(\d{2,4})\s*-\s*(\d{1,4})\s*BC\b", text, flags=re.I):
        candidates.append(-int(left))
    for year in re.findall(r"\b(\d{2,4})\s*BC\b", text, flags=re.I):
        candidates.append(-int(year))
    for left, _right in re.findall(r"\bAD\s*(\d{1,4})\s*-\s*(\d{1,4})\b", text, flags=re.I):
        candidates.append(int(left))
    for year in re.findall(r"\bAD\s*(\d{1,4})\b", text, flags=re.I):
        candidates.append(int(year))
    return min(candidates) if candidates else 999999


def compact_intro_groups(row: dict[str, str]) -> list[tuple[str, str]]:
    def cell(key: str) -> str:
        value = row.get(key, "").strip()
        normalized = " ".join(value.casefold().split())
        if normalized in {"n/a", "not applicable"}:
            return ""
        if key in {"mt_timeline", "lxx_timeline"} and normalized.startswith(
            ("not applicable", "mt timeline not applicable", "lxx timeline not applicable")
        ):
            return ""
        if key == "oldest_complete_hebrew" and normalized.startswith(
            ("no complete hebrew", "no complete ancient hebrew", "no secure full hebrew")
        ):
            return ""
        if key == "oldest_fragment" and normalized.startswith(
            ("no early hebrew original", "no hebrew original", "no complete hebrew original")
        ):
            return ""
        if key.endswith("_date"):
            return expand_intro_date(value)
        return value

    def parts(*keys: str) -> str:
        values = [cell(key) for key in keys if cell(key)]
        return " ".join(values).strip()

    witnesses: list[tuple[int, int, str]] = []

    def add_witness(label: str, text_key: str, date_key: str) -> None:
        value = parts(text_key, date_key)
        if value:
            witnesses.append((intro_date_sort_year(row.get(date_key, "")), len(witnesses), f"{label} {value}"))

    add_witness("Frag.", "oldest_fragment", "oldest_fragment_date")
    add_witness("Subst.", "oldest_substantial_manuscript", "oldest_substantial_date")
    add_witness("Heb.", "oldest_complete_hebrew", "oldest_complete_hebrew_date")
    add_witness("Gk.", "oldest_complete_greek", "oldest_complete_greek_date")
    witness_text = " | ".join(item[2] for item in sorted(witnesses)).strip()

    external: list[str] = []
    if row.get("oldest_external_reference", "").strip():
        external.append(row["oldest_external_reference"].strip())
    if row.get("oldest_external_reference_author", "").strip():
        external.append("by " + row["oldest_external_reference_author"].strip())
    if row.get("oldest_external_reference_date", "").strip():
        external.append("(" + expand_intro_date(row["oldest_external_reference_date"]) + ")")

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
        ("Earliest Witnesses", witness_text),
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


def local_versification_overrides() -> dict[str, str]:
    overrides: dict[str, str] = {}
    # This source keeps Naboth's vineyard in visible 1 Kings 20 and Ben-hadad's
    # Samaria siege in visible 1 Kings 21, opposite standard English numbering.
    overrides.update({f"1KI 20:{verse}": f"1KI 21:{verse}" for verse in range(1, 30)})
    overrides.update({f"1KI 21:{verse}": f"1KI 20:{verse}" for verse in range(1, 44)})
    # This source omits the standard English Malachi 4:4 line; Elijah is 3:22.
    overrides["MAL 3:22"] = "MAL 4:5"
    overrides["MAL 3:23"] = "MAL 4:6"
    return overrides


def effective_versification_map(
    versification_map: dict[str, str] | None = None,
) -> dict[str, str]:
    merged = dict(versification_map if versification_map is not None else DEFAULT_CROSSREF_VERSIFICATION_MAP)
    merged.update(local_versification_overrides())
    return merged


def normalize_code_ref_code(ref: str) -> str:
    parsed = parse_code_ref(ref)
    if not parsed:
        return ref
    code, chapter, verse = parsed
    return f"{validation_code(code)} {chapter}:{verse}"


def invert_versification_map(versification_map: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for source_ref, standard_ref in effective_versification_map(versification_map).items():
        normalized_standard = normalize_code_ref_code(standard_ref)
        normalized_source = normalize_code_ref_code(source_ref)
        inverted.setdefault(normalized_standard, normalized_source)
    return inverted


def display_ref_from_code_ref(ref: str) -> str | None:
    parsed = parse_code_ref(ref)
    if not parsed:
        return None
    code, chapter, verse = parsed
    return f"{STANDARD_BOOK_NAMES.get(validation_code(code), code)} {chapter}:{verse}"


def source_code_ref(verse: Verse) -> str:
    code = LOGOS_SOURCE_CODE_MAP.get(verse.book_code, verse.book_code)
    return f"{code} {verse.chapter}:{verse.verse}"


def parse_code_ref(ref: str) -> tuple[str, int, int] | None:
    match = CODE_REF_RE.match(ref)
    if not match:
        return None
    code, chapter, verse = match.groups()
    return code, int(chapter), int(verse)


DEFAULT_CROSSREF_VERSIFICATION_MAP, DEFAULT_CROSSREF_VERSIFICATION_DIAG = load_versification_map(
    DEFAULT_VERSIFICATION_MAP
)


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


def crossref_lookup_key(
    verse: Verse,
    versification_map: dict[str, str] | None = None,
) -> tuple[str, int, int]:
    mapped_ref = effective_versification_map(versification_map).get(source_code_ref(verse), source_code_ref(verse))
    parsed = parse_code_ref(normalize_code_ref_code(mapped_ref))
    if not parsed:
        return verse.tsk_key
    code, chapter, verse_num = parsed
    return validation_code(code), chapter, verse_num


def valid_crossref_code_refs(verses: list[Verse]) -> set[str]:
    refs = {normalize_code_ref_code(source_code_ref(verse)) for verse in verses}
    for source_path in (DEFAULT_SOURCE, DEFAULT_NT_SOURCE):
        if not source_path.exists():
            continue
        refs.update(normalize_code_ref_code(source_code_ref(verse)) for verse in load_verses(source_path))
    return refs


def code_ref_for_crossref_endpoint(book_label: str, chapter: str, verse: str) -> str | None:
    parsed = parse_cross_reference(f"{book_label} {int(chapter)}:{int(verse)}")
    if not parsed:
        return None
    code, _label, parsed_chapter, parsed_verse, _end, _raw = parsed
    if parsed_verse is None:
        return None
    return f"{validation_code(code)} {parsed_chapter}:{parsed_verse}"


def crossref_override_key(ref: str) -> str | None:
    normalized = normalize_space(ref.strip())
    match = CROSSREF_FULL_RANGE_RE.match(normalized)
    if match:
        start_book, start_chapter, start_verse, end_book, end_chapter, end_verse = match.groups()
        start_ref = code_ref_for_crossref_endpoint(start_book, start_chapter, start_verse)
        end_ref = code_ref_for_crossref_endpoint(end_book, end_chapter, end_verse)
        return f"{start_ref}-{end_ref}" if start_ref and end_ref else None
    match = CROSSREF_CHAPTER_RANGE_RE.match(normalized)
    if match:
        book, start_chapter, start_verse, end_chapter, end_verse = match.groups()
        start_ref = code_ref_for_crossref_endpoint(book, start_chapter, start_verse)
        end_ref = code_ref_for_crossref_endpoint(book, end_chapter, end_verse)
        return f"{start_ref}-{end_ref}" if start_ref and end_ref else None
    match = CROSSREF_SAME_CHAPTER_RANGE_RE.match(normalized)
    if match:
        book, chapter, start_verse, end_verse = match.groups()
        start_ref = code_ref_for_crossref_endpoint(book, chapter, start_verse)
        end_ref = code_ref_for_crossref_endpoint(book, chapter, end_verse)
        return f"{start_ref}-{end_ref}" if start_ref and end_ref else None
    parsed = parse_cross_reference(normalized)
    if not parsed:
        return None
    code, _label, chapter, verse, _end, _raw = parsed
    if verse is None:
        return None
    return f"{validation_code(code)} {chapter}:{verse}"


def load_crossref_target_overrides(
    path: Path = DEFAULT_CROSSREF_TARGET_OVERRIDES,
) -> dict[str, tuple[str, ...]]:
    if not path.exists():
        return {}
    overrides: dict[str, tuple[str, ...]] = {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            source_ref = normalize_space(row.get("source_ref", ""))
            mapped_refs = tuple(
                normalize_space(item)
                for item in row.get("mapped_refs", "").split(";")
                if normalize_space(item)
            )
            if not source_ref or not mapped_refs:
                continue
            key = crossref_override_key(source_ref)
            if key:
                overrides[key] = mapped_refs
    return overrides


DEFAULT_CROSSREF_TARGET_OVERRIDE_MAP = load_crossref_target_overrides()


def map_code_ref_to_lxx(
    code_ref: str,
    english_to_lxx_map: dict[str, str],
    valid_code_refs: set[str] | None,
) -> str | None:
    mapped_ref = english_to_lxx_map.get(normalize_code_ref_code(code_ref), normalize_code_ref_code(code_ref))
    if valid_code_refs is not None and mapped_ref not in valid_code_refs:
        return None
    return mapped_ref


def format_mapped_range(start_ref: str, end_ref: str) -> str | None:
    start = parse_code_ref(start_ref)
    end = parse_code_ref(end_ref)
    if not start or not end:
        return None
    start_code, start_chapter, start_verse = start
    end_code, end_chapter, end_verse = end
    start_label = STANDARD_BOOK_NAMES.get(validation_code(start_code), start_code)
    end_label = STANDARD_BOOK_NAMES.get(validation_code(end_code), end_code)
    if validation_code(start_code) == validation_code(end_code) and start_chapter == end_chapter:
        return f"{start_label} {start_chapter}:{start_verse}-{end_verse}"
    if validation_code(start_code) == validation_code(end_code):
        return f"{start_label} {start_chapter}:{start_verse}-{end_chapter}:{end_verse}"
    return f"{start_label} {start_chapter}:{start_verse}-{end_label} {end_chapter}:{end_verse}"


def map_cross_reference_to_lxx(
    ref: str,
    english_to_lxx_map: dict[str, str],
    valid_code_refs: set[str] | None = None,
) -> str | None:
    normalized = normalize_space(ref.strip())
    match = CROSSREF_FULL_RANGE_RE.match(normalized)
    if match:
        start_book, start_chapter, start_verse, end_book, end_chapter, end_verse = match.groups()
        start_ref = code_ref_for_crossref_endpoint(start_book, start_chapter, start_verse)
        end_ref = code_ref_for_crossref_endpoint(end_book, end_chapter, end_verse)
    else:
        match = CROSSREF_CHAPTER_RANGE_RE.match(normalized)
        if match:
            book, start_chapter, start_verse, end_chapter, end_verse = match.groups()
            start_ref = code_ref_for_crossref_endpoint(book, start_chapter, start_verse)
            end_ref = code_ref_for_crossref_endpoint(book, end_chapter, end_verse)
        else:
            match = CROSSREF_SAME_CHAPTER_RANGE_RE.match(normalized)
            if match:
                book, chapter, start_verse, end_verse = match.groups()
                start_ref = code_ref_for_crossref_endpoint(book, chapter, start_verse)
                end_ref = code_ref_for_crossref_endpoint(book, chapter, end_verse)
            else:
                parsed = parse_cross_reference(normalized)
                if not parsed:
                    return None
                code, _label, chapter, verse, _end, _raw = parsed
                if verse is None:
                    return normalized
                mapped = map_code_ref_to_lxx(
                    f"{validation_code(code)} {chapter}:{verse}",
                    english_to_lxx_map,
                    valid_code_refs,
                )
                return display_ref_from_code_ref(mapped) if mapped else None
    if not start_ref or not end_ref:
        return None
    mapped_start = map_code_ref_to_lxx(start_ref, english_to_lxx_map, valid_code_refs)
    mapped_end = map_code_ref_to_lxx(end_ref, english_to_lxx_map, valid_code_refs)
    if not mapped_start or not mapped_end:
        return None
    return format_mapped_range(mapped_start, mapped_end)


def map_crossref_refs_to_lxx(
    refs: Iterable[str],
    *,
    versification_map: dict[str, str] | None = None,
    english_to_lxx_map: dict[str, str] | None = None,
    valid_code_refs: set[str] | None = None,
    target_overrides: dict[str, tuple[str, ...]] | None = None,
) -> tuple[tuple[str, ...], Counter[str]]:
    if english_to_lxx_map is None:
        english_to_lxx_map = invert_versification_map(effective_versification_map(versification_map))
    if target_overrides is None:
        target_overrides = DEFAULT_CROSSREF_TARGET_OVERRIDE_MAP
    mapped_refs: list[str] = []
    counts: Counter[str] = Counter()
    seen: set[str] = set()
    for ref in refs:
        counts["input_refs"] += 1
        override_key = crossref_override_key(ref)
        override_refs = target_overrides.get(override_key or "")
        if override_refs:
            candidates = override_refs
            counts["manual_lxx_target_overrides"] += 1
        else:
            mapped_ref = map_cross_reference_to_lxx(ref, english_to_lxx_map, valid_code_refs)
            if not mapped_ref:
                counts["dropped_missing_lxx_target"] += 1
                continue
            candidates = (mapped_ref,)
            if mapped_ref != ref:
                counts["mapped_to_lxx"] += 1
        for mapped_ref in candidates:
            if mapped_ref in seen:
                counts["deduped_after_mapping"] += 1
                continue
            seen.add(mapped_ref)
            mapped_refs.append(mapped_ref)
    counts["output_refs"] += len(mapped_refs)
    return tuple(mapped_refs), counts


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


def should_suppress_logos_bible_milestone(verse: Verse) -> bool:
    source_ref = source_code_ref(verse)
    return (
        verse.book_code in LOGOS_DEUTEROCANON_SUPPRESSED_BOOK_CODES
        or source_ref in LOGOS_DEUTEROCANON_SUPPRESSED_CODE_REFS
    )


def logos_book_name(book_code: str, fallback: str) -> str:
    if book_code in LOGOS_BOOK_NAME_OVERRIDES:
        return LOGOS_BOOK_NAME_OVERRIDES[book_code]
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
    fragment = re.sub(r"\bprevailed not\b", "did not prevail", fragment, flags=re.I)
    fragment = re.sub(r"\bthings in earth\b", "things on earth", fragment, flags=re.I)
    fragment = re.sub(r"\bRamathaim\s*Zophim\b", "Ramathaim-Zophim", fragment, flags=re.I)
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


BROAD_SINGLE_WORD_CROSSREF_TRIGGERS = {
    "about",
    "above",
    "according",
    "after",
    "beginning",
    "before",
    "because",
    "being",
    "child",
    "children",
    "city",
    "come",
    "came",
    "day",
    "days",
    "daughter",
    "daughters",
    "earth",
    "even",
    "every",
    "face",
    "from",
    "god",
    "great",
    "hand",
    "have",
    "heart",
    "house",
    "into",
    "king",
    "land",
    "like",
    "lord",
    "many",
    "man",
    "men",
    "mouth",
    "name",
    "neither",
    "then",
    "people",
    "shall",
    "son",
    "sons",
    "soul",
    "spirit",
    "that",
    "there",
    "this",
    "through",
    "until",
    "way",
    "ways",
    "what",
    "when",
    "where",
    "which",
    "while",
    "whom",
    "whose",
    "with",
    "wife",
    "wives",
    "word",
    "words",
    "your",
}


UNINFORMATIVE_SINGLE_WORD_CROSSREF_TRIGGERS = {
    "about",
    "above",
    "according",
    "after",
    "all",
    "any",
    "before",
    "because",
    "being",
    "came",
    "come",
    "even",
    "every",
    "from",
    "having",
    "have",
    "into",
    "lest",
    "like",
    "many",
    "neither",
    "some",
    "shall",
    "that",
    "there",
    "these",
    "then",
    "this",
    "through",
    "until",
    "what",
    "when",
    "where",
    "which",
    "while",
    "whom",
    "whose",
    "with",
    "without",
    "would",
    "your",
}


UNINFORMATIVE_CROSSREF_TRIGGER_PHRASES = {
    ("a", "certain"),
    ("all", "that"),
    ("all", "the"),
    ("and", "all"),
    ("and", "have"),
    ("and", "he"),
    ("and", "his"),
    ("and", "i"),
    ("and", "the"),
    ("and", "they"),
    ("and", "to"),
    ("and", "was"),
    ("as", "i"),
    ("by", "the"),
    ("for", "the"),
    ("he", "is"),
    ("he", "was"),
    ("he", "went"),
    ("he", "will"),
    ("i", "am"),
    ("i", "have"),
    ("i", "know"),
    ("i", "say"),
    ("i", "will"),
    ("in", "the"),
    ("is", "not"),
    ("it", "is"),
    ("let", "the"),
    ("of", "whom"),
    ("that", "he"),
    ("that", "i"),
    ("that", "the"),
    ("that", "they"),
    ("the", "city"),
    ("the", "day"),
    ("the", "king"),
    ("the", "land"),
    ("the", "people"),
    ("the", "same"),
    ("they", "shall"),
    ("to", "the"),
    ("we", "have"),
    ("we", "know"),
}


def crossref_trigger_words(trigger: str) -> tuple[str, ...]:
    return tuple(re.findall(r"[A-Za-z0-9]+", trigger.casefold()))


def broad_single_word_crossref_trigger(trigger: str) -> bool:
    words = crossref_trigger_words(trigger)
    return len(words) == 1 and words[0] in BROAD_SINGLE_WORD_CROSSREF_TRIGGERS


def uninformative_single_word_crossref_trigger(trigger: str) -> bool:
    words = crossref_trigger_words(trigger)
    return len(words) == 1 and words[0] in UNINFORMATIVE_SINGLE_WORD_CROSSREF_TRIGGERS


def uninformative_crossref_trigger(trigger: str) -> bool:
    words = crossref_trigger_words(trigger)
    return (
        (len(words) == 1 and words[0] in UNINFORMATIVE_SINGLE_WORD_CROSSREF_TRIGGERS)
        or words in UNINFORMATIVE_CROSSREF_TRIGGER_PHRASES
    )


def crossref_book_code(ref: str) -> str:
    parsed = parse_cross_reference(ref.split("-", 1)[0].strip())
    return parsed[0] if parsed else ""


def thin_broad_single_word_crossref_note(
    note: CrossReferenceNote,
    verse: Verse,
) -> CrossReferenceNote | None:
    if note.source != "tsk":
        return note
    if uninformative_crossref_trigger(note.trigger_phrase):
        return None
    if not broad_single_word_crossref_trigger(note.trigger_phrase):
        return note
    verse_book_code = verse.tsk_key[0]
    kept_refs = tuple(ref for ref in note.refs if crossref_book_code(ref) == verse_book_code)
    if not kept_refs:
        return None
    return replace(note, refs=kept_refs)


def localize_crossref_note_phrase(
    note: CrossReferenceNote,
    verse_text: str,
) -> CrossReferenceNote:
    trigger = note.trigger_phrase.strip()
    if not trigger:
        return note
    found = find_trigger_span(verse_text, trigger)
    if not found:
        return replace(note, trigger_phrase="", display_phrase="")
    start, end = found
    fresh_phrase = verse_text[start:end]
    return replace(note, trigger_phrase=fresh_phrase, display_phrase=fresh_phrase)


def prepare_crossref_notes_for_verse(
    verse: Verse,
    notes: list[CrossReferenceNote],
) -> list[CrossReferenceNote]:
    prepared: list[CrossReferenceNote] = []
    for note in notes:
        note = CrossReferenceNote(
            trigger_phrase=getattr(note, "trigger_phrase", ""),
            refs=tuple(getattr(note, "refs", ())),
            source=getattr(note, "source", ""),
            display_phrase=getattr(note, "display_phrase", ""),
        )
        thinned = thin_broad_single_word_crossref_note(note, verse)
        if not thinned:
            continue
        prepared.append(localize_crossref_note_phrase(thinned, verse.text))
    return prepared


def map_crossref_notes_to_lxx(
    notes: list[CrossReferenceNote],
    *,
    versification_map: dict[str, str] | None,
    english_to_lxx_map: dict[str, str] | None = None,
    valid_code_refs: set[str],
) -> tuple[list[CrossReferenceNote], Counter[str]]:
    mapped_notes: list[CrossReferenceNote] = []
    counts: Counter[str] = Counter()
    if english_to_lxx_map is None:
        english_to_lxx_map = invert_versification_map(effective_versification_map(versification_map))
    for note in notes:
        mapped_refs, ref_counts = map_crossref_refs_to_lxx(
            note.refs,
            english_to_lxx_map=english_to_lxx_map,
            valid_code_refs=valid_code_refs,
        )
        counts.update(ref_counts)
        if not mapped_refs:
            counts["dropped_empty_note_after_mapping"] += 1
            continue
        mapped_notes.append(replace(note, refs=mapped_refs))
    return mapped_notes, counts


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


def cached_tsk_crossref_groups(
    testament: str,
) -> tuple[dict[tuple[str, int, int], list[CrossReferenceNote]], dict[str, object]]:
    result, _cache_diag = cached_ingest_result(
        "tsk-crossref-groups",
        [TSK_ZIP, KJV_V11N_JSON],
        {"testament": testament},
        lambda: parse_tsk_crossref_groups(testament),
    )
    grouped, diagnostics = result
    return grouped, diagnostics


def cached_openbible_crossrefs(
    limit_per_verse: int,
) -> tuple[dict[tuple[str, int, int], list[str]], dict[str, object]]:
    result, _cache_diag = cached_ingest_result(
        "openbible-crossrefs",
        [OPENBIBLE_CROSSREFS_ZIP],
        {"limit_per_verse": limit_per_verse},
        lambda: parse_openbible_crossrefs(limit_per_verse=limit_per_verse),
    )
    grouped, diagnostics = result
    return grouped, diagnostics


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
    if testament == "combined":
        ot_tsk_refs, ot_tsk_diag = cached_tsk_crossref_groups("ot")
        nt_tsk_refs, nt_tsk_diag = cached_tsk_crossref_groups("nt")
        tsk_refs: dict[tuple[str, int, int], list[CrossReferenceNote]] = {
            **ot_tsk_refs,
            **nt_tsk_refs,
        }
        tsk_diag: dict[str, object] = {
            "testament": "combined",
            "status": "parsed",
            "ot": ot_tsk_diag,
            "nt": nt_tsk_diag,
            "verses_with_refs": len(tsk_refs),
            "crossref_groups": sum(len(items) for items in tsk_refs.values()),
            "total_crossrefs": sum(len(item.refs) for items in tsk_refs.values() for item in items),
        }
    else:
        tsk_refs, tsk_diag = cached_tsk_crossref_groups(testament)
    open_refs, open_diag = cached_openbible_crossrefs(limit_per_verse=9999)
    by_ref: dict[str, list[CrossReferenceNote]] = {}
    source_counts = Counter()
    mapping_counts: Counter[str] = Counter()
    valid_code_refs = valid_crossref_code_refs(verses)
    english_to_lxx_map = invert_versification_map(effective_versification_map(None))
    total_refs = 0
    total_groups = 0
    for verse in verses:
        lookup_key = crossref_lookup_key(verse)
        if lookup_key != verse.tsk_key:
            mapping_counts["source_refs_mapped_to_standard"] += 1
        notes = tsk_refs.get(lookup_key, [])
        if notes:
            source_counts["tsk"] += 1
        else:
            refs = open_refs.get(lookup_key, [])
            if refs:
                source_counts["openbible_fallback"] += 1
                cleaned = tuple(canonicalize_cross_references([format_openbible_ref(ref) for ref in refs]))
                notes = [CrossReferenceNote(trigger_phrase="", refs=cleaned, source="openbible")]
        notes = prepare_crossref_notes_for_verse(verse, notes)
        notes, note_mapping_counts = map_crossref_notes_to_lxx(
            notes,
            versification_map=None,
            english_to_lxx_map=english_to_lxx_map,
            valid_code_refs=valid_code_refs,
        )
        mapping_counts.update(note_mapping_counts)
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
        "versification_mapping": dict(mapping_counts),
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
    start_book, start_chapter, start_verse, end_book, end_chapter, end_verse, _votes = match.groups()
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


def cached_brenton_usfm() -> tuple[list[Any], dict[str, object]]:
    result, _cache_diag = cached_ingest_result(
        "brenton-usfm",
        [BRENTON_ZIP],
        {},
        parse_brenton_usfm,
    )
    records, diagnostics = result
    return records, diagnostics


def load_brenton_supplemental_notes(
    verses: list[Verse],
) -> tuple[dict[str, list[SupplementalNote]], dict[str, object]]:
    verse_refs = {verse.ref for verse in verses}
    grouped: dict[str, list[SupplementalNote]] = defaultdict(list)
    counts: Counter[str] = Counter()
    seen: set[tuple[str, str]] = set()

    brenton_records, brenton_diag = cached_brenton_usfm()
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
    compact_translation_note_labels: bool = False,
    compact_name_note_labels: bool = False,
    docx_compresslevel: int = DOCX_DEFAULT_COMPRESSLEVEL,
    compact_print: bool = False,
    lulu_pod_margins: bool = False,
    run_in_verse_paragraphs: bool = False,
    run_in_group_size: int = 6,
    pericope_headings: dict[str, str] | None = None,
    output_kind: str | None = None,
    subtitle: str | None = None,
    crossref_policy: str | None = None,
    name_policy: str | None = None,
    supplemental_policy: str | None = None,
    note_label_legend: str | None = None,
    front_matter_sections: list[tuple[str, list[str]]] | None = None,
) -> BuildStats:
    place_links_enabled = bool(place_links)
    footnote_columns = 2 if compact_print else 1
    doc = MinimalDocx(
        title=title,
        subject=(
            f"{description} with translation notes and cross-references"
            if crossrefs_enabled
            else f"{description} with translation, textual, supplemental, and name notes"
        ),
        compact_print=compact_print,
        lulu_pod_margins=lulu_pod_margins,
        footnote_number_restart=footnote_number_restart,
        footnote_columns=footnote_columns,
    )
    stats = BuildStats(
        output_kind=output_kind or ("logos" if logos else "proofreading"),
        milestone_mode=milestone_mode,
        footnote_number_restart=footnote_number_restart,
        run_in_verse_paragraphs=bool(run_in_verse_paragraphs and not logos),
        run_in_group_size=run_in_group_size if run_in_verse_paragraphs and not logos else 0,
        footnote_columns=footnote_columns,
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
        book_prefaces_enabled=bool(book_intros),
        subtitle=subtitle,
        crossref_policy=crossref_policy,
        name_policy=name_policy,
        supplemental_policy=supplemental_policy,
        note_label_legend=note_label_legend,
        front_matter_sections=front_matter_sections,
        place_links_enabled=place_links_enabled,
        compact_print=compact_print,
    )

    current_book = ""
    current_chapter = -1
    milestone_ref_counts: Counter[str] = Counter()
    previous_milestone_ref: str | None = None
    versification_map = versification_map or {}
    verse_counts = verse_counts or {}
    place_links = place_links or {}
    pericope_headings = pericope_headings or {}
    pending_verse_runs: list[str] = []
    pending_verse_count = 0

    def flush_pending_verse_paragraph() -> None:
        nonlocal pending_verse_runs, pending_verse_count
        if not pending_verse_runs:
            return
        doc.add_paragraph(pending_verse_runs)
        stats.paragraph_count += 1
        pending_verse_runs = []
        pending_verse_count = 0

    for verse in verses:
        if verse.book_name != current_book:
            flush_pending_verse_paragraph()
            current_book = verse.book_name
            current_chapter = -1
            previous_milestone_ref = None
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
            flush_pending_verse_paragraph()
            current_chapter = verse.chapter
            chapter_section_break = footnote_number_restart == "chapter"
            doc.add_heading(f"Chapter {verse.display_chapter}", level=2, section_break_after=chapter_section_break)
            if chapter_section_break:
                stats.section_break_count += 1
            stats.paragraph_count += 1

        pericope_heading = pericope_headings.get(verse.ref)
        if pericope_heading:
            flush_pending_verse_paragraph()
            doc.add_paragraph([run(pericope_heading)], style="PericopeHeading")
            stats.paragraph_count += 1
            stats.pericope_heading_count += 1

        verse_translation_notes = translation_notes.get(verse.ref, [])
        verse_name_notes = name_notes.get(verse.ref, [])
        verse_supplemental_notes = supplemental_notes.get(verse.ref, [])
        verse_crossrefs = [] if is_mt_only_completeness_verse(verse) else crossrefs.get(verse.ref, [])
        runs, milestone_ref, emitted_milestone = build_verse_runs(
            doc=doc,
            verse=verse,
            notes=verse_translation_notes,
            name_notes=verse_name_notes,
            supplemental_notes=verse_supplemental_notes,
            crossref_notes=verse_crossrefs,
            place_links=place_links if logos else {},
            place_link_pattern=place_link_pattern if logos else None,
            logos=logos,
            datatype=datatype,
            milestone_mode=milestone_mode,
            versification_map=versification_map,
            verse_counts=verse_counts,
            previous_milestone_ref=previous_milestone_ref,
            stats=stats,
            compact_translation_note_labels=compact_translation_note_labels,
            compact_name_note_labels=compact_name_note_labels,
            verse_number_color=PRINT_RED if compact_print else None,
        )
        if logos and milestone_ref:
            previous_milestone_ref = milestone_ref
            if emitted_milestone:
                milestone_ref_counts[milestone_ref] += 1
        if stats.run_in_verse_paragraphs:
            if pending_verse_runs:
                pending_verse_runs.append(run("\u00a0\u00a0"))
            pending_verse_runs.extend(runs)
            pending_verse_count += 1
            if stats.run_in_group_size and pending_verse_count >= stats.run_in_group_size:
                flush_pending_verse_paragraph()
        else:
            flush_pending_verse_paragraph()
            doc.add_paragraph(runs)
            stats.paragraph_count += 1

    flush_pending_verse_paragraph()
    stats.place_link_count = sum(part.count("BibleKnowledgebase:") for part in doc.body)
    stats.footnote_count = len(doc.footnotes)
    stats.duplicate_milestone_refs = sum(count - 1 for count in milestone_ref_counts.values() if count > 1)
    doc.save(path, compresslevel=docx_compresslevel)
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
    book_prefaces_enabled: bool,
    subtitle: str | None = None,
    crossref_policy: str | None = None,
    name_policy: str | None = None,
    supplemental_policy: str | None = None,
    note_label_legend: str | None = None,
    front_matter_sections: list[tuple[str, list[str]]] | None = None,
    place_links_enabled: bool = False,
    compact_print: bool = False,
) -> None:
    doc.add_paragraph([run(title)], style="Title")
    subtitle_text = subtitle or ("Logos Personal Book source" if logos else "Proofreading and print copy")
    doc.add_paragraph([run(subtitle_text)], style="Subtitle")
    if testament == "ot":
        note_policy = "Includes reviewed translation/textual notes. Generic MT/LXX boilerplate is omitted unless a concrete local difference can be stated."
        default_supplemental_policy = "Includes supplemental Brenton USFM footnotes."
        vocab_policy = "Hebrew/Greek vocabulary notes are excluded; name/proper-noun meanings remain included separately."
    elif testament == "nt":
        note_policy = "Includes reviewed translation/textual notes that match NT references. OT-specific MT/LXX boilerplate is omitted."
        default_supplemental_policy = "Includes no NT supplemental source-note layer yet."
        vocab_policy = "Greek vocabulary notes are excluded; name/proper-noun meanings remain included separately."
    elif testament == "deuterocanon":
        note_policy = "Deuterocanon translation/textual note tables are not enabled yet; this Logos source carries the translated text for review."
        default_supplemental_policy = "Source descriptors remain in the CSV workspace; no supplemental source-note layer is emitted in this separate Logos source yet."
        vocab_policy = "Greek vocabulary notes are excluded; name/proper-noun meanings can be added in a later deuterocanon note pass."
        default_name_policy = "No deuterocanon name-meaning note layer is enabled yet."
    else:
        note_policy = "Includes reviewed OT and NT translation/textual notes. Generic MT/LXX boilerplate is omitted unless a concrete local difference can be stated."
        default_supplemental_policy = "Includes OT supplemental Brenton USFM footnotes where available; no NT supplemental source-note layer yet."
        vocab_policy = "Greek vocabulary notes are excluded; name/proper-noun meanings remain included separately."
        default_name_policy = "Includes name-meaning notes at first exact occurrence per chapter."
    if testament in {"ot", "nt"}:
        default_name_policy = "Includes name-meaning notes at first exact occurrence per chapter."
    supplemental_policy_text = supplemental_policy or default_supplemental_policy
    name_policy_text = name_policy or default_name_policy
    crossref_policy_text = crossref_policy or (
        "Includes full available cross-reference set from TSK, with OpenBible fallback where TSK has no row."
        if crossrefs_enabled
        else "Cross-reference footnote layer is excluded because --no-crossrefs was used."
    )
    lines = [
        description,
        note_policy,
        (
            "Includes book preface pages before each book's chapter text."
            if book_prefaces_enabled
            else "Book preface pages are excluded to keep this copy shorter."
        ),
        crossref_policy_text,
        name_policy_text,
        supplemental_policy_text,
        vocab_policy,
    ]
    if not (compact_print and not logos):
        lines.append(
            f"Regular footnote numbering restarts by {footnote_number_restart}. "
            + (
                "Cross-reference footnotes use normal numeric Word footnote references for Logos Personal Book compatibility when enabled."
                if logos
                else "Cross-reference footnotes use normal numeric Word footnote references when enabled."
            )
        )
    if logos:
        lines.append(f"Verse milestones use Logos datatype {datatype}. Compile in Logos as resource type Bible.")
        lines.append(
            "Conservative place-name links use Logos Bible Knowledgebase targets where a local Logos place entity can be matched unambiguously."
            if place_links_enabled
            else "Place-name links are disabled for this build so Personal Book import stays plain and stable."
        )
        lines.append("Textual-note export entries are embedded as local notes; no Logos resource-link layer is used.")
        if milestone_mode == "mt":
            lines.append("Milestones are remapped to standard English/MT Bible references for Logos note sharing.")
    for line in lines:
        doc.add_paragraph([run(line)])
    if front_matter_sections:
        doc.add_page_break()
        for heading, paragraphs in front_matter_sections:
            doc.add_heading(heading, level=2)
            for paragraph in paragraphs:
                doc.add_paragraph([run(paragraph)])
    if note_label_legend:
        doc.add_heading("Note Label Legend", level=2)
        for legend_line in note_label_legend_lines(note_label_legend):
            doc.add_paragraph([run(legend_line)])
    if testament in SOURCE_BASIS_GUIDE:
        doc.add_heading("Source Basis", level=2)
        for source_line in SOURCE_BASIS_GUIDE[testament]:
            doc.add_paragraph([run(source_line)])
    if testament in {"ot", "combined"}:
        doc.add_heading("Reference Numbering Guide", level=2)
        doc.add_paragraph(
            [
                run(
                    "Visible OT chapter and verse numbers follow the LXX source rows. "
                    "Many familiar English references, especially in Psalms and Jeremiah, "
                    "therefore land at different places in this edition."
                )
            ]
        )
        for english_ref, local_ref in REFERENCE_NUMBERING_GUIDE:
            doc.add_paragraph([run(f"{english_ref}: see {local_ref}.")])
        doc.add_paragraph(
            [
                run(
                    "This branch is a Protestant-canon LXX-based edition. Psalm 151 and "
                    "other deuterocanonical or apocryphal books are reserved for a separate "
                    "LXX deuterocanon workstream."
                )
            ]
        )
    elif testament == "deuterocanon":
        doc.add_heading("Reference Numbering Guide", level=2)
        doc.add_paragraph(
            [
                run(
                    "Visible chapter and verse labels follow the imported LXX deuterocanon/additions source rows. "
                    "Rows with source suffixes keep those suffixes visible in the text; Logos milestones use the numeric base verse where a suffix is present. "
                    "Rows outside Logos' supported Bible datatype ranges remain visible text without hidden Bible milestones."
                )
            ]
        )
    doc.add_page_break()


def note_label_legend_lines(note_label_legend: str) -> list[str]:
    legend = note_label_legend.removeprefix("Print note label legend:").strip()
    parts = [part.strip().rstrip(".") for part in legend.split(";") if part.strip()]
    if len(parts) < 4:
        return [note_label_legend]
    groups = (parts[:3], parts[3:8], parts[8:])
    return ["; ".join(group) + "." for group in groups if group]


def add_book_preface_page(doc: MinimalDocx, fallback_book_name: str, intro: dict[str, str]) -> int:
    title = intro.get("intro_title", "").strip() or intro.get("book_name", "").strip() or fallback_book_name
    doc.add_heading(f"{title} Preface", level=2)
    paragraph_count = 1
    for label, value in compact_intro_groups(intro):
        doc.add_paragraph([run(f"{label}. ", bold=True), run(value)])
        paragraph_count += 1
    if intro.get("book_code", "").strip() == "GEN":
        paragraph_count += add_genesis_chronology_comparison(doc)
    return paragraph_count


def load_genesis_chronology_comparison(path: Path = GENESIS_CHRONOLOGY_COMPARISON) -> list[dict[str, str]]:
    if not path.exists():
        return []
    return load_csv(path)


def add_genesis_chronology_comparison(doc: MinimalDocx) -> int:
    rows = load_genesis_chronology_comparison()
    if not rows:
        return 0

    doc.add_heading("Genesis Chronology Comparison", level=2)
    doc.add_paragraph(
        [
            run(
                "This table compares the ages at which the Genesis patriarchs beget the named son in the current LXX source rows and in the Masoretic Text. "
                "Most LXX ages in Genesis 5 and 11 are about 100 years higher than MT. "
                "The main pre-flood inversion is Methuselah: Genesis 5:25 has LXX 167 and MT 187. "
                "Genesis 11 also includes the second Cainan between Arphaxad and Shelah, the generation cited in Luke 3:36 and absent from MT."
            )
        ]
    )
    table_rows = [
        [
            [run("Patriarch", bold=True)],
            [run("LXX age at son's birth", bold=True)],
            [run("MT age at son's birth", bold=True)],
        ]
    ]
    for row in rows:
        table_rows.append(
            [
                [run(row.get("patriarch", "").strip())],
                [run(row.get("lxx_age_at_son_birth", "").strip())],
                [run(row.get("mt_age_at_son_birth", "").strip())],
            ]
        )
    doc.add_table(table_rows)
    return 2 + len(rows)


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
    previous_milestone_ref: str | None,
    stats: BuildStats,
    compact_translation_note_labels: bool = False,
    compact_name_note_labels: bool = False,
    verse_number_color: str | None = None,
) -> tuple[list[str], str | None, bool]:
    runs: list[str] = []
    milestone_ref: str | None = None
    emitted_milestone = False
    if logos:
        if should_suppress_logos_bible_milestone(verse):
            stats.suppressed_unsupported_milestone_refs += 1
        else:
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
            if milestone.logos_ref == previous_milestone_ref:
                stats.suppressed_duplicate_milestone_refs += 1
            else:
                runs.append(run(f"[[@{datatype}:{milestone.logos_ref}]] ", small=True, color="777777"))
                emitted_milestone = True
    runs.append(run(f"{verse.display_verse} ", bold=True, color=verse_number_color))
    if logos and emitted_milestone:
        runs.append(run(" {{field-on:Bible}}"))

    text_for_notes = verse.text
    superscription = split_psalm_superscription(verse)
    if superscription:
        superscription_text, body_text = superscription
        runs.append(run(f"{superscription_text} ", italic=True))
        stats.superscription_line_count += 1
        text_for_notes = body_text
        if body_text:
            runs.append(line_break_run())

    text_runs, verse_level_notes, verse_level_names, verse_level_crossrefs = runs_for_text_with_phrase_notes(
        doc,
        text_for_notes,
        notes,
        name_notes,
        crossref_notes,
        place_links,
        place_link_pattern,
        stats,
        compact_translation_note_labels=compact_translation_note_labels,
        compact_name_note_labels=compact_name_note_labels,
    )
    runs.extend(text_runs)
    for note in verse_level_notes:
        note_id = doc.add_footnote(
            translation_note_display_text(note, compact_label=compact_translation_note_labels)
        )
        runs.append(footnote_ref_run(note_id))
        stats.translation_note_footnotes += 1
        if note.source_basis == TEXTUAL_NOTE_SOURCE_BASIS:
            stats.textual_note_export_footnotes += 1
        stats.verse_anchored_translation_notes += 1
    for name_note in verse_level_names:
        note_id = doc.add_footnote(name_note_display_text(name_note, compact_label=compact_name_note_labels))
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
    if logos and emitted_milestone:
        runs.append(run("{{field-off:Bible}}"))
    return runs, milestone_ref, emitted_milestone


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
    compact_translation_note_labels: bool = False,
    compact_name_note_labels: bool = False,
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
                note_id = doc.add_footnote(
                    name_note_display_text(item, compact_label=compact_name_note_labels)
                )
                output.append(footnote_ref_run(note_id))
                stats.name_meaning_footnotes += 1
                stats.phrase_anchored_name_meaning_notes += 1
            else:
                note_id = doc.add_footnote(
                    translation_note_display_text(item, compact_label=compact_translation_note_labels)
                )
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
    nt_source_path: Path | None,
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
    place_links_enabled: bool,
    docx_output_set: str,
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
    if nt_source_path is not None:
        try:
            nt_source_display = nt_source_path.relative_to(ROOT).as_posix()
        except ValueError:
            nt_source_display = str(nt_source_path)
    else:
        nt_source_display = ""
    if testament == "ot":
        source_note = "- Supplemental Brenton notes: Brenton USFM footnotes are included. TSK study-note text is intentionally excluded because it is too large for this Logos source. Hebrew and Greek vocabulary notes are excluded because Logos already provides lexical lookup layers. Proper-name and divine-title notes are integrated as name-meaning notes."
        variant_note = f"- Translation notes: reviewed rows from `data/research/translation_footnotes.csv`. Generic MT/LXX difference rows are skipped unless `{translation_decisions_display}` supports a concrete local detail, such as a substantive number/unit difference. Those concrete rows are labeled `MT/LXX note`."
        future_work_note = f"- Separate deuterocanon workstream: LXX deuterocanonical/apocrypha intro rows exist, but this Protestant-canon branch does not include those verse rows. Planned separate-source books: {missing_deuterocanon_display}."
        verse_numbering_note = "- OT Logos files preserve LXX source ordering and visible LXX verse numbers by design, including places where LXX chapter/verse order differs from standard English/MT order."
        ot_shape_notes = (
            "- MT-only completeness insertion: LXX-numbered Jeremiah 40:14-26 supplies MT Jeremiah 33:14-26 in brackets. The footnote marks these verses as present in the MT, absent from the LXX text used here, not quoted in the NT, and included for completeness.\n"
            "- 1 Kings ordering: Naboth vineyard material appears at LXX-numbered 1 Kings 20, while Ben-Hadad battle material appears at LXX-numbered 1 Kings 21. This follows the source order and is not treated as a missing chapter.\n"
            "- Daniel sourcing: Greek Daniel follows the current LXX source workspace and is footnoted where it diverges sharply from familiar Theodotion or MT/Aramaic wording."
        )
    elif testament == "nt":
        source_note = "- Supplemental source notes: no NT supplemental source-note layer is currently enabled. TSK study-note text is intentionally excluded because it is too large for this Logos source. Greek vocabulary notes are excluded because Logos already provides lexical lookup layers. Proper-name and divine-title notes are integrated as name-meaning notes."
        variant_note = "- Translation notes: reviewed rows from `data/research/translation_footnotes.csv` plus any local textual-note export entries matching NT references. OT-specific MT/LXX rows are ignored for this NT source."
        future_work_note = "- Future polish: NT source rows are complete; continue copyediting, note hygiene, and Logos compile spot-checks."
        verse_numbering_note = "- NT Logos files use the standard NT chapter/verse order from the Scrivener TR source rows."
        ot_shape_notes = "- NT source shape: source rows follow the Scrivener 1894 Textus Receptus chapter/verse sequence."
    elif testament == "deuterocanon":
        source_note = "- Supplemental source notes: source descriptors are preserved in `syntax_notes` in the CSV workspace, but no supplemental footnote layer is emitted in this separate Logos source yet."
        variant_note = "- Translation notes: shared OT/NT translation-note tables are not applied to this separate deuterocanon Logos source."
        future_work_note = "- Paper proof scope: this deuterocanon source is intentionally separate and is not included in the compact paper proofreading copy."
        verse_numbering_note = "- Deuterocanon Logos files preserve imported LXX source order and visible source verse labels, including suffix labels such as Greek Esther 1:1α. Hidden Logos milestones use the numeric base verse where suffix labels are present; unsupported Logos Bible datatype ranges are left as visible text without hidden milestones."
        ot_shape_notes = (
            "- Greek Esther shape: `ESG` is the full Greek Esther import. `ESGA` remains available in the source workspace as an additions-only view for review; use the generated progress/worksheet files to audit that view.\n"
            "- Greek Ezra B / 2 Esdras: `2ES` is Greek Ezra B from GRCLXX, not the Latin apocalypse commonly titled 2 Esdras / 4 Ezra in some English traditions. Its Logos Bible milestones are suppressed to avoid false links.\n"
            "- Source row shape: plain embedded source verse labels are split into rows; bracketed source-text sections remain bracketed."
        )
    else:
        source_note = "- Supplemental source notes: OT Brenton USFM footnotes are included where available; no NT supplemental source-note layer is currently enabled. TSK study-note text is intentionally excluded because it is too large for this Logos source. Greek vocabulary notes are excluded because Logos already provides lexical lookup layers. Proper-name and divine-title notes are integrated as name-meaning notes."
        variant_note = f"- Translation notes: reviewed rows from `data/research/translation_footnotes.csv` plus any local textual-note export entries matching included references. Generic MT/LXX difference rows are skipped unless `{translation_decisions_display}` supports a concrete local detail."
        future_work_note = f"- Separate deuterocanon workstream: LXX deuterocanonical/apocrypha intro rows exist, but this Protestant-canon branch does not include those verse rows. Planned separate-source books: {missing_deuterocanon_display}. NT source rows are complete; continue copyediting, note hygiene, and Logos compile spot-checks."
        verse_numbering_note = "- Combined Logos files preserve OT LXX source ordering and visible LXX verse numbers, while NT rows use the standard Scrivener TR chapter/verse sequence."
        ot_shape_notes = (
            "- MT-only completeness insertion: LXX-numbered Jeremiah 40:14-26 supplies MT Jeremiah 33:14-26 in brackets. The footnote marks these verses as present in the MT, absent from the LXX text used here, not quoted in the NT, and included for completeness.\n"
            "- 1 Kings ordering: Naboth vineyard material appears at LXX-numbered 1 Kings 20, while Ben-Hadad battle material appears at LXX-numbered 1 Kings 21. This follows the source order and is not treated as a missing chapter.\n"
            "- Daniel sourcing: Greek Daniel follows the current LXX source workspace and is footnoted where it diverges sharply from familiar Theodotion or MT/Aramaic wording.\n"
            "- NT source shape: source rows follow the Scrivener 1894 Textus Receptus chapter/verse sequence."
        )
    place_link_note = (
        "- Place links: conservative Logos `BibleKnowledgebase` datatype links are added for unambiguous primary place labels found in the local Logos autocomplete database. These are clickable Factbook/place links; Personal Book source does not expose the same internal atlas-pin overlay used by Logos-edition Bibles."
        if place_links_enabled
        else "- Place links: disabled by default; generated DOCX keeps place names as plain text so Personal Book import remains stable."
    )
    bridge_heading = "MT-note bridge import" if testament == "ot" else "Reference-note bridge import"
    if testament == "ot":
        bridge_note = f"Use `{mt_bridge_docx.name}` instead of `{logos_docx.name}` when the goal is to surface notes already anchored to standard MT/English Bible references. The visible verse numbers remain from the LXX source rows, but hidden milestones are remapped to standard Bible references where a reliable mapping is available."
        source_basis_note = f"- Source text: `{source_display}`. Translation work is made from the LXX Greek source rows, not from Brenton or another English base."
        bridge_file_note = "Logos Personal Book source with verse milestones remapped to standard English/MT references so existing reference-anchored Logos notes from MT-based Bibles can show. Compile as resource type `Bible`."
    elif testament == "nt":
        bridge_note = f"`{mt_bridge_docx.name}` is emitted for parity with the OT build. NT TR source rows already use standard NT versification, so this bridge should normally match the main Logos source."
        source_basis_note = f"- Source text: `{source_display}`, imported from byztxt/greektext-scrivener Scrivener 1894 Textus Receptus text-only files."
        bridge_file_note = "Logos Personal Book source emitted for parity with the OT reference-bridge output. NT TR source rows already use standard NT milestones. Compile as resource type `Bible`."
    elif testament == "deuterocanon":
        bridge_note = "The default deuterocanon target emits a Logos-only DOCX. No MT-reference bridge is generated unless the full DOCX output set is requested explicitly."
        source_basis_note = f"- Source text: `{source_display}`. Translation work is made from the separate LXX deuterocanon/additions Greek source rows, not from an English base."
        bridge_file_note = "Optional parity bridge for the separate deuterocanon source. The default Makefile target skips this file."
    else:
        bridge_note = f"`{mt_bridge_docx.name}` remaps OT milestones to standard English/MT references where a reliable mapping is available. NT TR source rows already use standard NT versification."
        source_basis_note = f"- Source text: `{source_display}` plus `{nt_source_display}`. OT translation work is made from the LXX Greek source rows; NT translation work is made from the Scrivener 1894 Textus Receptus Greek stream."
        bridge_file_note = "Combined Logos Personal Book source with OT milestones remapped to standard English/MT references where possible and NT milestones left on their standard references. Compile as resource type `Bible`."
    crossref_note = (
        "- Cross-references: TSK primary set from `data/raw/TSK.zip`; OpenBible fallback from `data/raw/cross-references.zip` where TSK has no verse row. TSK catchwords are used as word/phrase anchors only when they exactly match the fresh translation; otherwise cross-references remain verse-anchored. Broad single-word catchword groups are thinned to same-book links or dropped to avoid loose thematic jumps. See root `NOTICE.md` for public-domain/CC-BY attribution details."
        if crossrefs_enabled
        else "- Cross-references: omitted because `--no-crossrefs` was used."
    )
    concordance_note = "- Greek concordance: not included. Logos provides native dynamic concordance lookup, so this build relies on that capability instead of duplicating it as a static appendix. Print/deuterocanon proof outputs may include compact static concordance material for readers without Logos lookup tools."
    title = config["title_prefix"] if testament in {"combined", "deuterocanon"} else f"Fresh Translation {config['label']}"
    generated_files = [
        f"- `{logos_docx.name}`: Logos Personal Book source. Compile as resource type `Bible`.",
    ]
    if docx_output_set == "all":
        generated_files.extend(
            [
                f"- `{mt_bridge_docx.name}`: {bridge_file_note}",
                f"- `{proof_docx.name}`: clean proofreading/printing copy without Logos milestone or field syntax.",
            ]
        )
    generated_files.extend(
        [
            f"- `{diagnostics_path.name}`: build counts and cross-reference/note diagnostics.",
            f"- `{preview_path.name}`: quick preview sample for spot-checking.",
        ]
    )
    if testament in {"ot", "combined"}:
        key_examples = chr(10).join(f"- {english_ref}: see {local_ref}." for english_ref, local_ref in REFERENCE_NUMBERING_GUIDE)
    elif testament == "deuterocanon":
        key_examples = "- Deuterocanon references follow imported source labels; suffix labels remain visible in the verse text."
    else:
        key_examples = "- No OT LXX/English numbering guide is needed for the NT-only file."
    name_note_line = (
        "- Name meanings: no deuterocanon name-meaning layer is enabled yet; proper-name notes can be added in a later deuterocanon note pass."
        if testament == "deuterocanon"
        else "- Name meanings: `data/proper_names.csv`, `data/proper_name_transliteration_notes.csv`, and `data/names_of_god.csv`. Proper-name notes and unambiguous multi-word divine-title notes are placed at the first exact occurrence per chapter. Ambiguous single-word divine-title notes remain source-reference anchored to avoid assigning the wrong source-language title from English alone."
    )
    name_caution_line = (
        "- Name-meaning caution: not applicable until a deuterocanon name-meaning layer is enabled."
        if testament == "deuterocanon"
        else "- Name-meaning caution: many meanings are seeded from public-domain legacy sources such as Hitchcock's Bible Names Dictionary and are reader aids, not final etymological claims. Correct stronger lexical evidence should replace them as review continues."
    )
    content = f"""# {title} Logos/Proofreading Files

Generated files:

{chr(10).join(generated_files)}

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

Verse numbering:

{verse_numbering_note}
Key examples:

{key_examples}

Scope:

- Source basis: {config["source_text"]}.
{source_basis_note}
- Book preface pages: `{book_intros_display}`. These are inserted before each book's chapter text in all generated DOCX files.
{variant_note}
{name_note_line}
{name_caution_line}
- Literal phrase convention: phrases such as `sons of Israel` and `sons of men` usually preserve Greek son-language intentionally rather than smoothing by default.
{ot_shape_notes}
{source_note}
- Local textual-note export: generated from `{textual_notes_display}` when present. Note text is embedded into this Personal Book as local `Textual note` footnotes; no `logosres:` links or external Logos resource layer are emitted.
{future_work_note}
{place_link_note}
{crossref_note}
{concordance_note}
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
        xml_payloads: dict[str, bytes] = {}
        xml_roots: dict[str, ET.Element] = {}
        for name in entries:
            if name.endswith(".xml"):
                payload = zf.read(name)
                xml_payloads[name] = payload
                try:
                    xml_roots[name] = ET.fromstring(payload)
                except ET.ParseError as exc:
                    xml_errors.append(f"{name}: {exc}")
        result["xml_ok"] = not xml_errors
        result["xml_errors"] = xml_errors
        result["footnote_reference_count"] = xml_payloads.get("word/document.xml", b"").count(b"<w:footnoteReference")
        footnotes_root = xml_roots.get("word/footnotes.xml")
        footnote_nodes = footnotes_root if footnotes_root is not None else []
        result["footnote_body_count"] = sum(
            1
            for node in footnote_nodes
            if node.tag == f"{{{DOCX_W_NS}}}footnote"
            and node.attrib.get(f"{{{DOCX_W_NS}}}type") not in {"separator", "continuationSeparator"}
        )
    return result


def skipped_docx_validation(path: Path, reason: str) -> dict[str, object]:
    return {"path": str(path), "skipped": True, "reason": reason}


def build_diagnostics(
    *,
    verses: list[Verse],
    note_counts: dict[str, int],
    variant_decision_counts: dict[str, int],
    textual_export_counts: dict[str, object],
    notes: dict[str, list[TranslationNote]],
    reader_notes: dict[str, list[TranslationNote]],
    reader_note_filter_counts: dict[str, int],
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
    included_note_total = sum(len(items) for items in reader_notes.values())
    source_note_total = sum(len(items) for items in notes.values())
    included_name_note_total = sum(len(items) for items in name_notes.values())
    included_supplemental_note_total = sum(len(items) for items in supplemental_notes.values())
    return {
        "datatype": datatype,
        "verse_rows": len(verses),
        "book_count": len(book_counts),
        "book_counts": dict(book_counts),
        "translation_note_filter": note_counts,
        "reader_facing_translation_note_filter": reader_note_filter_counts,
        "translation_decision_filter": variant_decision_counts,
        "textual_note_export": textual_export_counts,
        "source_translation_note_refs": len(notes),
        "source_translation_note_total": source_note_total,
        "included_translation_note_refs": len(reader_notes),
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
    parser.add_argument("--nt-source", type=Path, default=DEFAULT_NT_SOURCE)
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
    parser.add_argument("--book", help="Limit generated DOCX/preview/diagnostics to one book name or book code.")
    parser.add_argument(
        "--place-links",
        action="store_true",
        help="Enable experimental Logos Bible Knowledgebase place links. Disabled by default because Personal Books can surface unresolved markup.",
    )
    parser.add_argument("--no-place-links", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--datatype", default="Bible")
    parser.add_argument(
        "--footnote-number-restart",
        choices=("chapter", "book", "page", "continuous"),
        default="chapter",
        help="Visible footnote numbering restart scope inside the single DOCX file.",
    )
    parser.add_argument(
        "--no-crossrefs",
        action="store_true",
        help="Omit the TSK/OpenBible cross-reference footnote layer.",
    )
    parser.add_argument(
        "--docx-compresslevel",
        type=int,
        choices=range(10),
        default=DOCX_DEFAULT_COMPRESSLEVEL,
        metavar="0-9",
        help="ZIP compression level for generated DOCX files; use lower values for ignored working builds.",
    )
    parser.add_argument(
        "--skip-docx-validation",
        action="store_true",
        help="Skip DOCX zip/XML validation for faster ignored working builds.",
    )
    parser.add_argument(
        "--docx-output-set",
        choices=("all", "logos-only"),
        default="all",
        help="Choose which DOCX outputs to generate. Release builds should use all.",
    )
    args = parser.parse_args()
    config = TESTAMENT_CONFIG[args.testament]

    source_verses = (
        [*load_verses(args.source), *load_verses(args.nt_source)]
        if args.testament == "combined"
        else load_verses(args.source)
    )
    verses = filter_items_by_book(
        source_verses,
        args.book,
        book_name=lambda verse: verse.book_name,
        book_code=lambda verse: verse.book_code,
        item_label="verse",
    )
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
    reader_notes, reader_note_filter_counts = filter_reader_facing_translation_notes(notes)
    book_intros, book_intro_diag = load_book_intros(args.book_intros)
    deuterocanonical_work = (
        deuterocanonical_future_work(book_intros, verses)
        if args.testament in {"ot", "combined"}
        else {"enabled": False, "reason": "Not applicable to NT build.", "missing_book_count": 0, "missing_books": []}
    )
    source_name_notes, name_note_counts = load_name_meaning_notes(
        proper_names_path=args.proper_names,
        transliterated_proper_names_path=args.transliterated_proper_names,
        names_of_god_path=args.names_of_god,
        source_filter=None if args.testament == "combined" else args.testament,
    )
    name_notes, name_note_placement_counts = place_name_meaning_notes_by_chapter(verses, source_name_notes)
    name_note_counts = {
        **name_note_counts,
        **{f"placement_{key}": value for key, value in name_note_placement_counts.items()},
    }
    crossrefs_enabled = not args.no_crossrefs and args.testament != "deuterocanon"
    crossrefs, crossref_diag = build_crossrefs_for_verses(
        verses,
        args.testament,
        enabled=crossrefs_enabled,
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
    if args.testament in {"ot", "combined"}:
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
        translation_notes=reader_notes,
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
        crossrefs_enabled=crossrefs_enabled,
        docx_compresslevel=args.docx_compresslevel,
    )
    if args.docx_output_set == "all":
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
            crossrefs_enabled=crossrefs_enabled,
            docx_compresslevel=args.docx_compresslevel,
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
            crossrefs_enabled=crossrefs_enabled,
            docx_compresslevel=args.docx_compresslevel,
        )
    else:
        mt_bridge_stats = BuildStats(
            output_kind="skipped",
            milestone_mode="mt",
            footnote_number_restart=args.footnote_number_restart,
        )
        proof_stats = BuildStats(
            output_kind="skipped",
            milestone_mode="lxx",
            footnote_number_restart=args.footnote_number_restart,
        )
    build_preview(args.preview, verses, reader_notes, supplemental_notes, crossrefs, config["preview_title"])
    build_readme(
        args.readme,
        testament=args.testament,
        config=config,
        source_path=args.source,
        nt_source_path=args.nt_source if args.testament == "combined" else None,
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
        crossrefs_enabled=crossrefs_enabled,
        place_links_enabled=bool(place_links),
        docx_output_set=args.docx_output_set,
    )
    if args.skip_docx_validation:
        validations = [
            skipped_docx_validation(args.logos_docx, "--skip-docx-validation"),
            skipped_docx_validation(args.mt_bridge_docx, "--skip-docx-validation"),
            skipped_docx_validation(args.proof_docx, "--skip-docx-validation"),
        ]
    elif args.docx_output_set == "logos-only":
        validations = [
            validate_docx(args.logos_docx),
            skipped_docx_validation(args.mt_bridge_docx, "--docx-output-set=logos-only"),
            skipped_docx_validation(args.proof_docx, "--docx-output-set=logos-only"),
        ]
    else:
        validations = [validate_docx(args.logos_docx), validate_docx(args.mt_bridge_docx), validate_docx(args.proof_docx)]
    diagnostics = build_diagnostics(
        verses=verses,
        note_counts=note_counts,
        variant_decision_counts=variant_decision_counts,
        textual_export_counts=textual_export_counts,
        notes=notes,
        reader_notes=reader_notes,
        reader_note_filter_counts=reader_note_filter_counts,
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
