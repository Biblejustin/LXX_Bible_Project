#!/usr/bin/env python3
import csv
from functools import lru_cache
from heapq import nsmallest
import html
import json
import re
import struct
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
import zlib
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUTPUT = ROOT / "output"
OUTPUT_PREFIX = "Brenton_UKJV_study_bible_prototype"
OUTPUT_PREFIX_CROSSREFS_ONLY = "Brenton_UKJV_study_bible_crossrefs_only"
OUTPUT_PREFIX_CROSSREFS_NORMAL = "Brenton_UKJV_study_bible_crossrefs_normal"
RIGHTS_MD = ROOT / "data" / "rights_and_rationale.md"
CONVENTIONS_MD = ROOT / "data" / "editorial_conventions.md"
PREFACE_MD = ROOT / "data" / "preface_charts.md"
APPENDIX_MD = ROOT / "data" / "appendix_references.md"
NAME_APPENDIX_MD = ROOT / "data" / "name_meanings_appendix.md"
BOOK_INTROS_CSV = ROOT / "data" / "book_intros_template.csv"
PROPER_NAMES_CSV = ROOT / "data" / "proper_names.csv"
HEBREW_VOCAB_CSV = ROOT / "data" / "hebrew_top_vocab.csv"
GREEK_VOCAB_CSV = ROOT / "data" / "greek_vocabulary.csv"
VOCAB_CLEANUP_CSV = ROOT / "data" / "vocab_cleanup.csv"
NAMES_OF_GOD_CSV = ROOT / "data" / "names_of_god.csv"
KJV_V11N_JSON = ROOT / "data" / "kjv_versification.json"

BRENTON_ZIP = RAW / "eng-Brenton_usfm.zip"
UKJV_ZIP = RAW / "SF_2009-01-20_ENG_UKJV_(UPDATED KING JAMES VERSION).zip"
TSK_ZIP = RAW / "TSK.zip"
KALVESMAKI_CSV = RAW / "Kalvesmaki chart.csv"
KALVESMAKI_HTML = RAW / "Table of Old Testament quotes in the New Testament, in English translation.html"
OPENBIBLE_CROSSREFS_ZIP = RAW / "cross-references.zip"
ENOCH_CHARLES_TXT = RAW / "1_enoch_charles_1917.txt"
NORMAL_CROSSREF_LIMIT = 12

OT_BOOKS = [
    "GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT", "1SA", "2SA",
    "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "EST", "JOB", "PSA", "PRO",
    "ECC", "SNG", "ISA", "JER", "LAM", "EZK", "DAN", "HOS", "JOL", "AMO",
    "OBA", "JON", "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL", "TOB",
    "JDT", "ESG", "WIS", "SIR", "BAR", "LJE", "S3Y", "SUS", "BEL", "1MA",
    "2MA", "1ES", "MAN", "PS2", "3MA", "4MA", "ODA", "PSS", "EZA", "JUB",
    "ENO", "DAG",
]

NT_BOOKS = [
    "MAT", "MRK", "LUK", "JHN", "ACT", "ROM", "1CO", "2CO", "GAL", "EPH",
    "PHP", "COL", "1TH", "2TH", "1TI", "2TI", "TIT", "PHM", "HEB", "JAS",
    "1PE", "2PE", "1JN", "2JN", "3JN", "JUD", "REV",
]

APOCRYPHA_BOOKS = [
    "TOB", "JDT", "WIS", "SIR", "BAR", "LJE", "SUS", "BEL", "1MA", "2MA",
    "1ES", "MAN", "3MA", "4MA", "ENO",
]

FINAL_BOOK_ORDER = [
    "GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT", "1SA", "2SA",
    "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "ESG", "JOB", "PSA", "PRO",
    "ECC", "SNG", "ISA", "JER", "LAM", "EZK", "DAG", "HOS", "JOL", "AMO",
    "OBA", "JON", "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL",
    *NT_BOOKS,
    *APOCRYPHA_BOOKS,
]

TSK_OT_BOOKS = [
    "GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT", "1SA", "2SA",
    "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "ESG", "JOB", "PSA", "PRO",
    "ECC", "SNG", "ISA", "JER", "LAM", "EZK", "DAG", "HOS", "JOL", "AMO",
    "OBA", "JON", "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL",
]
TSK_NT_BOOKS = NT_BOOKS[:]
NT_BOOKS_SET = frozenset(NT_BOOKS)

UKJV_BOOK_MAP = {
    40: ("MAT", "Matthew"),
    41: ("MRK", "Mark"),
    42: ("LUK", "Luke"),
    43: ("JHN", "John"),
    44: ("ACT", "Acts"),
    45: ("ROM", "Romans"),
    46: ("1CO", "1 Corinthians"),
    47: ("2CO", "2 Corinthians"),
    48: ("GAL", "Galatians"),
    49: ("EPH", "Ephesians"),
    50: ("PHP", "Philippians"),
    51: ("COL", "Colossians"),
    52: ("1TH", "1 Thessalonians"),
    53: ("2TH", "2 Thessalonians"),
    54: ("1TI", "1 Timothy"),
    55: ("2TI", "2 Timothy"),
    56: ("TIT", "Titus"),
    57: ("PHM", "Philemon"),
    58: ("HEB", "Hebrews"),
    59: ("JAS", "James"),
    60: ("1PE", "1 Peter"),
    61: ("2PE", "2 Peter"),
    62: ("1JN", "1 John"),
    63: ("2JN", "2 John"),
    64: ("3JN", "3 John"),
    65: ("JUD", "Jude"),
    66: ("REV", "Revelation"),
}

STANDARD_BOOK_NAMES = {
    "GEN": "Genesis",
    "EXO": "Exodus",
    "LEV": "Leviticus",
    "NUM": "Numbers",
    "DEU": "Deuteronomy",
    "JOS": "Joshua",
    "JDG": "Judges",
    "RUT": "Ruth",
    "1SA": "1 Samuel",
    "2SA": "2 Samuel",
    "1KI": "1 Kings",
    "2KI": "2 Kings",
    "1CH": "1 Chronicles",
    "2CH": "2 Chronicles",
    "EZR": "Ezra",
    "NEH": "Nehemiah",
    "EST": "Esther",
    "ESG": "Esther",
    "JOB": "Job",
    "PSA": "Psalms",
    "PRO": "Proverbs",
    "ECC": "Ecclesiastes",
    "SNG": "Song of Solomon",
    "ISA": "Isaiah",
    "JER": "Jeremiah",
    "LAM": "Lamentations",
    "EZK": "Ezekiel",
    "DAN": "Daniel",
    "DAG": "Daniel",
    "HOS": "Hosea",
    "JOL": "Joel",
    "AMO": "Amos",
    "OBA": "Obadiah",
    "JON": "Jonah",
    "MIC": "Micah",
    "NAM": "Nahum",
    "HAB": "Habakkuk",
    "ZEP": "Zephaniah",
    "HAG": "Haggai",
    "ZEC": "Zechariah",
    "MAL": "Malachi",
    "TOB": "Tobit",
    "JDT": "Judith",
    "WIS": "Wisdom",
    "SIR": "Sirach",
    "BAR": "Baruch",
    "LJE": "Letter of Jeremiah",
    "S3Y": "Song of the Three Holy Children",
    "SUS": "Susanna",
    "BEL": "Bel and the Dragon",
    "1MA": "1 Maccabees",
    "2MA": "2 Maccabees",
    "1ES": "1 Esdras",
    "MAN": "Prayer of Manasseh",
    "PS2": "Psalm 151",
    "3MA": "3 Maccabees",
    "4MA": "4 Maccabees",
    "ODA": "Odes",
    "PSS": "Psalms of Solomon",
    "EZA": "Ezra Apocalypse",
    "JUB": "Jubilees",
    "ENO": "1 Enoch",
    "MAT": "Matthew",
    "MRK": "Mark",
    "LUK": "Luke",
    "JHN": "John",
    "ACT": "Acts",
    "ROM": "Romans",
    "1CO": "1 Corinthians",
    "2CO": "2 Corinthians",
    "GAL": "Galatians",
    "EPH": "Ephesians",
    "PHP": "Philippians",
    "COL": "Colossians",
    "1TH": "1 Thessalonians",
    "2TH": "2 Thessalonians",
    "1TI": "1 Timothy",
    "2TI": "2 Timothy",
    "TIT": "Titus",
    "PHM": "Philemon",
    "HEB": "Hebrews",
    "JAS": "James",
    "1PE": "1 Peter",
    "2PE": "2 Peter",
    "1JN": "1 John",
    "2JN": "2 John",
    "3JN": "3 John",
    "JUD": "Jude",
    "REV": "Revelation",
}

OPENBIBLE_BOOK_MAP = {
    "Gen": "GEN", "Exod": "EXO", "Lev": "LEV", "Num": "NUM", "Deut": "DEU",
    "Josh": "JOS", "Judg": "JDG", "Ruth": "RUT", "1Sam": "1SA", "2Sam": "2SA",
    "1Kgs": "1KI", "2Kgs": "2KI", "1Chr": "1CH", "2Chr": "2CH", "Ezra": "EZR",
    "Neh": "NEH", "Esth": "EST", "Job": "JOB", "Ps": "PSA", "Prov": "PRO",
    "Eccl": "ECC", "Song": "SNG", "Isa": "ISA", "Jer": "JER", "Lam": "LAM",
    "Ezek": "EZK", "Dan": "DAG", "Hos": "HOS", "Joel": "JOL", "Amos": "AMO",
    "Obad": "OBA", "Jonah": "JON", "Mic": "MIC", "Nah": "NAM", "Hab": "HAB",
    "Zeph": "ZEP", "Hag": "HAG", "Zech": "ZEC", "Mal": "MAL", "Matt": "MAT",
    "Mark": "MRK", "Luke": "LUK", "John": "JHN", "Acts": "ACT", "Rom": "ROM",
    "1Cor": "1CO", "2Cor": "2CO", "Gal": "GAL", "Eph": "EPH", "Phil": "PHP",
    "Col": "COL", "1Thess": "1TH", "2Thess": "2TH", "1Tim": "1TI", "2Tim": "2TI",
    "Titus": "TIT", "Phlm": "PHM", "Heb": "HEB", "Jas": "JAS", "1Pet": "1PE",
    "2Pet": "2PE", "1John": "1JN", "2John": "2JN", "3John": "3JN", "Jude": "JUD",
    "Rev": "REV",
}

OSIS_BOOK_MAP = {
    **OPENBIBLE_BOOK_MAP,
    "Exod": "EXO",
    "Deut": "DEU",
    "1Kgs": "1KI",
    "2Kgs": "2KI",
    "Esth": "ESG",
    "Dan": "DAG",
    "Matt": "MAT",
    "Phlm": "PHM",
    "Jude": "JUD",
}

REF_BOOK_ALIASES = {
    "Genesis": "GEN", "Gen": "GEN",
    "Exodus": "EXO", "Exod": "EXO", "Exo": "EXO",
    "Leviticus": "LEV", "Lev": "LEV",
    "Numbers": "NUM", "Num": "NUM",
    "Deuteronomy": "DEU", "Deut": "DEU",
    "Joshua": "JOS", "Josh": "JOS",
    "Judges": "JDG", "Judg": "JDG",
    "Ruth": "RUT",
    "1 Samuel": "1SA", "1Sam": "1SA", "I Sam": "1SA",
    "2 Samuel": "2SA", "2Sam": "2SA", "II Sam": "2SA",
    "1 Kings": "1KI", "1Kgs": "1KI", "I Kings": "1KI",
    "2 Kings": "2KI", "2Kgs": "2KI", "II Kings": "2KI",
    "1 Chronicles": "1CH", "1Chr": "1CH", "I Chron": "1CH",
    "2 Chronicles": "2CH", "2Chr": "2CH", "II Chron": "2CH",
    "Ezra": "EZR",
    "Nehemiah": "NEH", "Neh": "NEH",
    "Esther": "EST", "Esth": "EST",
    "Job": "JOB",
    "Psalm": "PSA", "Psalms": "PSA", "Ps": "PSA",
    "Proverbs": "PRO", "Prov": "PRO",
    "Ecclesiastes": "ECC", "Eccl": "ECC",
    "Song of Solomon": "SNG", "Song": "SNG", "Canticles": "SNG",
    "Isaiah": "ISA", "Isa": "ISA",
    "Jeremiah": "JER", "Jer": "JER",
    "Lamentations": "LAM", "Lam": "LAM",
    "Ezekiel": "EZK", "Ezek": "EZK",
    "Daniel": "DAG", "Dan": "DAG",
    "Hosea": "HOS", "Hos": "HOS",
    "Joel": "JOL",
    "Amos": "AMO",
    "Obadiah": "OBA", "Obad": "OBA",
    "Jonah": "JON",
    "Micah": "MIC", "Mic": "MIC",
    "Nahum": "NAM", "Nah": "NAM",
    "Habakkuk": "HAB", "Hab": "HAB",
    "Zephaniah": "ZEP", "Zeph": "ZEP",
    "Haggai": "HAG", "Hag": "HAG",
    "Zechariah": "ZEC", "Zech": "ZEC",
    "Malachi": "MAL", "Mal": "MAL",
    "Matthew": "MAT", "Matt": "MAT",
    "Mark": "MRK",
    "Luke": "LUK",
    "John": "JHN",
    "Acts": "ACT",
    "Romans": "ROM", "Rom": "ROM",
    "1 Corinthians": "1CO", "1Cor": "1CO", "I Cor": "1CO",
    "2 Corinthians": "2CO", "2Cor": "2CO", "II Cor": "2CO",
    "Galatians": "GAL", "Gal": "GAL",
    "Ephesians": "EPH", "Eph": "EPH",
    "Philippians": "PHP", "Phil": "PHP",
    "Colossians": "COL", "Col": "COL",
    "1 Thessalonians": "1TH", "1Thess": "1TH", "I Thess": "1TH",
    "2 Thessalonians": "2TH", "2Thess": "2TH", "II Thess": "2TH",
    "1 Timothy": "1TI", "1Tim": "1TI", "I Tim": "1TI",
    "2 Timothy": "2TI", "2Tim": "2TI", "II Tim": "2TI",
    "Titus": "TIT",
    "Philemon": "PHM", "Phlm": "PHM", "Phm": "PHM",
    "Hebrews": "HEB", "Heb": "HEB",
    "James": "JAS", "Jas": "JAS",
    "1 Peter": "1PE", "1Pet": "1PE", "I Pet": "1PE",
    "2 Peter": "2PE", "2Pet": "2PE", "II Pet": "2PE",
    "1 John": "1JN", "1John": "1JN", "I John": "1JN",
    "2 John": "2JN", "2John": "2JN", "II John": "2JN",
    "3 John": "3JN", "3John": "3JN", "III John": "3JN",
    "Jude": "JUD",
    "Revelation": "REV", "Rev": "REV",
    "Tobit": "TOB", "Tob": "TOB",
    "Judith": "JDT", "Jdt": "JDT", "Jdth": "JDT",
    "Wisdom": "WIS", "Wis": "WIS", "Wisdom of Solomon": "WIS",
    "Sirach": "SIR", "Sir": "SIR", "Ecclesiasticus": "SIR",
    "Baruch": "BAR", "Bar": "BAR",
    "Letter of Jeremiah": "LJE", "Epistle of Jeremiah": "LJE", "Ep Jer": "LJE",
    "Song of the Three": "S3Y", "Song of Three": "S3Y",
    "Susanna": "SUS", "Sus": "SUS",
    "Bel and the Dragon": "BEL", "Bel": "BEL",
    "1 Maccabees": "1MA", "1Macc": "1MA", "1 Macc": "1MA", "1Mac": "1MA",
    "2 Maccabees": "2MA", "2Macc": "2MA", "2 Macc": "2MA", "2Mac": "2MA",
    "3 Maccabees": "3MA", "3Macc": "3MA", "3 Macc": "3MA", "3Mac": "3MA",
    "4 Maccabees": "4MA", "4Macc": "4MA", "4 Macc": "4MA", "4Mac": "4MA",
    "1 Esdras": "1ES", "1Esd": "1ES", "1 Esd": "1ES",
    "Prayer of Manasseh": "MAN", "Pr Man": "MAN",
    "Psalm 151": "PS2", "Ps 151": "PS2",
    "Odes": "ODA", "Ode": "ODA",
    "Psalms of Solomon": "PSS", "Pss Sol": "PSS",
    "1 Enoch": "ENO", "1Enoch": "ENO", "1 Enoch": "ENO",
}

SUPERSCRIPTS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
MAX_MARGIN_REFS_DISPLAY = 4
MARGIN_REF_GROUP_SIZE = 2
HEAVY_CROSSREF_THRESHOLD = 5
EXTREME_CROSSREF_THRESHOLD = 10
EXTREME_COMBINED_LOAD_THRESHOLD = 900

SPACE_RE = re.compile(r"\s+")
PUNCT_FAST_RE = re.compile(r"[;,]\s*[;,]")
PUNCT_NORM_RE = re.compile(r"(?:\s*[;,]\s*){2,}")
USFM_FOOTNOTE_RE = re.compile(r"\\f\s+\+(.*?)\\f\*")
USFM_XREF_RE = re.compile(r"\\x\s+\+.*?\\x\*")
USFM_FOOTNOTE_FIELD_RE = re.compile(r"\\fr\s+[^\\]+|\\(?:fqa|ft|fk|fq)\s+")
USFM_MARKUP_RE = re.compile(r"\\[a-z0-9*]+ ?")
USFM_MARKUP_BARE_RE = re.compile(r"\\[a-z0-9*]+")
USFM_ID_RE = re.compile(r"\\id\s+([A-Z0-9]+)")
USFM_VERSE_RE = re.compile(r"\\v\s+(\d+)\s+(.*)")
TSK_REFERENCE_RE = re.compile(r"<reference\b[^>]*>(.*?)</reference>", re.S)
TSK_REFERENCE_TAG_RE = re.compile(r"<reference\b[^>]*>.*?</reference>", re.S)
TSK_INLINE_TAG_RE = re.compile(r"</?(hi|div|title|catchWord)\b[^>]*>")
TSK_LINE_BREAK_RE = re.compile(r"<lb\b[^>]*>")
XML_TAG_RE = re.compile(r"<[^>]+>")
SEMICOLON_SPACE_RE = re.compile(r"\s*;\s*")
COMMA_SPACE_RE = re.compile(r"\s*,\s*")
DUPLICATE_COMMA_RE = re.compile(r"(?:,\s*){2,}")
DUPLICATE_SEMICOLON_RE = re.compile(r"(?:;\s*){2,}")
DUPLICATE_WORD_RE = re.compile(r"\b([A-Za-z]+)(?:\s+\1\b)+")
ALPHA_WORD_RE = re.compile(r"[A-Za-z][A-Za-z'/-]*")
OPENBIBLE_REF_RE = re.compile(r"([1-3]?[A-Za-z]+)\.(\d+)\.(\d+)$")
OPENBIBLE_TARGET_REF_RE = re.compile(
    r"^([1-3]?[A-Za-z]+)\.(\d+)\.(\d+)"
    r"(?:-([1-3]?[A-Za-z]+)\.(\d+)\.(\d+))?(?: \((\d+)\))?$"
)
CROSS_REFERENCE_VOTE_SUFFIX_RE = re.compile(r"\s+\(\d+\)$")
LATEX_REPLACEMENTS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}
LATEX_ESCAPE_RE = re.compile(r"[\\&%$#_{}~^]")


@dataclass(slots=True)
class VerseRecord:
    book_code: str
    book_name: str
    chapter: int
    verse: int
    text: str
    source: str
    section: Optional[str] = None
    paragraph_start: bool = False
    footnotes: List[str] = field(default_factory=list)
    cross_references: List[str] = field(default_factory=list)
    study_notes: List[str] = field(default_factory=list)
    ref: str = field(init=False)

    def __post_init__(self) -> None:
        self.ref = f"{self.book_name} {self.chapter}:{self.verse}"


def normalize_space(text: str) -> str:
    if not text.isascii():
        text = unicodedata.normalize("NFKC", text)
        text = text.replace("\ufffd", "")
        text = text.replace("\u037e", ";")
        text = text.replace("\u0387", ";")
        text = text.replace("\u00b7", ";")
    text = SPACE_RE.sub(" ", text)
    if PUNCT_FAST_RE.search(text):
        text = PUNCT_NORM_RE.sub("; ", text)
    return text.strip()


def strip_usfm_markup(text: str) -> str:
    text = USFM_FOOTNOTE_RE.sub("", text)
    text = USFM_XREF_RE.sub("", text)
    text = USFM_MARKUP_BARE_RE.sub(" ", text)
    text = text.replace("~", " ")
    return normalize_space(text)


def extract_usfm_footnotes(text: str) -> List[str]:
    notes = []
    for raw in USFM_FOOTNOTE_RE.findall(text):
        body = USFM_FOOTNOTE_FIELD_RE.sub("", raw)
        body = USFM_MARKUP_RE.sub("", body)
        body = normalize_space(body)
        if body:
            notes.append(body)
    return notes


def parse_brenton_usfm() -> Tuple[List[VerseRecord], Dict[str, int]]:
    records: List[VerseRecord] = []
    diagnostics = {"books_seen": 0, "footnotes_extracted": 0}
    with zipfile.ZipFile(BRENTON_ZIP) as zf:
        names = sorted(
            name for name in zf.namelist()
            if name.endswith(".usfm") and not name.startswith(("00-FRT", "01-INT"))
        )
        for name in names:
            raw = zf.read(name).decode("utf-8", "replace").splitlines()
            book_code = None
            book_name = None
            chapter = None
            paragraph_start = False
            section = None
            for line in raw:
                line = line.rstrip()
                if line.startswith("\\id "):
                    m = USFM_ID_RE.match(line)
                    if m:
                        book_code = m.group(1)
                        book_name = STANDARD_BOOK_NAMES.get(book_code, book_code)
                elif line.startswith("\\toc1 "):
                    if not book_code:
                        book_name = line[6:].strip()
                elif line.startswith("\\mt1 ") and not book_name:
                    if not book_code:
                        book_name = line[5:].strip().title()
                elif line.startswith("\\c "):
                    chapter = int(line.split()[1])
                elif line.startswith(("\\s ", "\\s1 ", "\\s2 ", "\\ms ", "\\ms1 ")):
                    section = strip_usfm_markup(line.split(" ", 1)[1])
                elif line.startswith("\\p"):
                    paragraph_start = True
                elif line.startswith("\\v "):
                    if not (book_code and book_name and chapter):
                        continue
                    m = USFM_VERSE_RE.match(line)
                    if not m:
                        continue
                    verse = int(m.group(1))
                    verse_raw = m.group(2)
                    footnotes = extract_usfm_footnotes(verse_raw)
                    text = strip_usfm_markup(verse_raw)
                    if not text:
                        continue
                    records.append(
                        VerseRecord(
                            book_code=book_code,
                            book_name=book_name,
                            chapter=chapter,
                            verse=verse,
                            text=text,
                            source="Brenton LXX",
                            section=section,
                            paragraph_start=paragraph_start,
                            footnotes=footnotes,
                        )
                    )
                    diagnostics["footnotes_extracted"] += len(footnotes)
                    paragraph_start = False
            diagnostics["books_seen"] += 1
    records = [r for r in records if r.book_code in OT_BOOKS]
    return records, diagnostics


def parse_ukjv_xml() -> Tuple[List[VerseRecord], Dict[str, int]]:
    with zipfile.ZipFile(UKJV_ZIP) as zf:
        xml_name = zf.namelist()[0]
        root = ET.fromstring(zf.read(xml_name))
    records: List[VerseRecord] = []
    diagnostics = {"books_seen": 0}
    for book in root.findall("BIBLEBOOK"):
        bnumber = int(book.attrib["bnumber"])
        if bnumber not in UKJV_BOOK_MAP:
            continue
        book_code, raw_book_name = UKJV_BOOK_MAP[bnumber]
        book_name = STANDARD_BOOK_NAMES.get(book_code, raw_book_name)
        diagnostics["books_seen"] += 1
        section = None
        for chapter_el in book.findall("CHAPTER"):
            chapter = int(chapter_el.attrib["cnumber"])
            paragraph_start = True
            for item in chapter_el:
                if item.tag == "CAPTION":
                    section = normalize_space("".join(item.itertext()))
                    continue
                if item.tag != "VERS":
                    continue
                verse = int(item.attrib["vnumber"])
                text = normalize_space("".join(item.itertext()))
                if not text:
                    continue
                records.append(
                    VerseRecord(
                        book_code=book_code,
                        book_name=book_name,
                        chapter=chapter,
                        verse=verse,
                        text=text,
                        source="UKJV",
                        section=section,
                        paragraph_start=paragraph_start,
                    )
                )
                paragraph_start = False
    return records, diagnostics


ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(text: str) -> int:
    total = 0
    prev = 0
    for ch in reversed(text):
        value = ROMAN_VALUES[ch]
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    return total


def strip_enoch_editorial(text: str) -> str:
    text = text.replace("〚", "").replace("〛", "")
    text = text.replace("⌜", "").replace("⌝", "")
    text = text.replace("⌞", "").replace("⌟", "")
    text = text.replace("†", "")
    text = text.replace("=", "")
    text = re.sub(r"\[[^\]]*\]", "", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)
    return normalize_space(text)


def parse_enoch_charles() -> Tuple[List[VerseRecord], Dict[str, object]]:
    if not ENOCH_CHARLES_TXT.exists():
        return [], {"present": False, "chapters_loaded": 0, "records": 0}
    raw = ENOCH_CHARLES_TXT.read_text(encoding="utf-8", errors="ignore")
    start = raw.find("I. 1.")
    end = raw.find("XXXVII. 1.")
    if start == -1 or end == -1 or end <= start:
        return [], {"present": True, "chapters_loaded": 0, "records": 0, "error": "Could not locate chs. 1-36"}
    body = raw[start:end]
    kept_lines: List[str] = []
    for raw_line in body.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            kept_lines.append("")
            continue
        if re.fullmatch(r"[A-Z](?:\^[A-Za-z])?", stripped):
            continue
        kept_lines.append(stripped)
    body = "\n".join(kept_lines)
    chapter_pattern = re.compile(
        r"(?ms)^\s*([IVXLCDM]+)\.\s*(?:(\d+)\.\s*)?([A-Z\"'(].*?)(?=^\s*[IVXLCDM]+\.\s*(?:\d+\.\s*|[A-Z\"'(])|\Z)"
    )
    records: List[VerseRecord] = []
    chapters_seen = set()
    for match in chapter_pattern.finditer(body):
        chapter = roman_to_int(match.group(1))
        if not (1 <= chapter <= 36):
            continue
        chapters_seen.add(chapter)
        first_verse = int(match.group(2)) if match.group(2) else 1
        section_text = f"{first_verse}. {match.group(3).strip()}"
        section_text = re.sub(r"\n+", " ", section_text)
        section_text = strip_enoch_editorial(section_text)
        verse_matches = list(re.finditer(r"(?<!\d)(\d+)\.\s+", section_text))
        seen_verses = set()
        for idx, vm in enumerate(verse_matches):
            verse = int(vm.group(1))
            if verse in seen_verses:
                continue
            start_idx = vm.end()
            end_idx = verse_matches[idx + 1].start() if idx + 1 < len(verse_matches) else len(section_text)
            verse_text = strip_enoch_editorial(section_text[start_idx:end_idx])
            verse_text = re.sub(r"^[—-]\s*", "", verse_text)
            if not verse_text:
                continue
            seen_verses.add(verse)
            records.append(
                VerseRecord(
                    book_code="ENO",
                    book_name="1 Enoch",
                    chapter=chapter,
                    verse=verse,
                    text=verse_text,
                    source="R. H. Charles (1917)",
                    paragraph_start=(verse == 1),
                )
            )
    return records, {"present": True, "chapters_loaded": len(chapters_seen), "records": len(records)}


def parse_kalvesmaki() -> Tuple[Dict[str, List[str]], Dict[str, int]]:
    notes_by_nt_ref: Dict[str, List[str]] = defaultdict(list)
    diagnostics = {"rows": 0, "usable_rows": 0}
    if not KALVESMAKI_CSV.exists():
        return notes_by_nt_ref, diagnostics
    with KALVESMAKI_CSV.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            diagnostics["rows"] += 1
            nt_ref = normalize_space(row.get("NT Reference", ""))
            lxx_text = normalize_space(row.get("LXX/Brenton Text", ""))
            mt_text = normalize_space(row.get("MT/Hebrew Text (AV)", ""))
            notes = normalize_space(row.get("Notes", ""))
            if not nt_ref or nt_ref.startswith("..."):
                continue
            diagnostics["usable_rows"] += 1
            detail = []
            if mt_text:
                detail.append(f"NT quotation aligns more closely with Hebrew/MT here; cf. Brenton LXX: “{lxx_text}”")
            if notes:
                detail.append(notes)
            if detail:
                notes_by_nt_ref[nt_ref].extend(detail)
    return notes_by_nt_ref, diagnostics


def load_kjv_versification() -> Dict[str, List[int]]:
    if not KJV_V11N_JSON.exists():
        return {}
    return json.loads(KJV_V11N_JSON.read_text(encoding="utf-8"))


def build_tsk_index_map(book_order: List[str], verse_counts: Dict[str, List[int]]) -> Dict[int, Tuple[str, int, int]]:
    index_map: Dict[int, Tuple[str, int, int]] = {}
    idx = 2
    for book_code in book_order:
        chapters = verse_counts.get(book_code, [])
        idx += 1  # book intro
        for chapter_num, verse_total in enumerate(chapters, start=1):
            idx += 1  # chapter intro
            for verse_num in range(1, verse_total + 1):
                index_map[idx] = (book_code, chapter_num, verse_num)
                idx += 1
    return index_map


def decode_tsk_blob(bzv: bytes, bzs: bytes, bzz: bytes, index: int, cache: Dict[int, bytes]) -> str:
    buffnum, start, size = struct.unpack_from("<IIH", bzv, index * 10)
    if size == 0:
        return ""
    if buffnum not in cache:
        offset, compressed_size, _ = struct.unpack_from("<III", bzs, buffnum * 12)
        cache[buffnum] = zlib.decompress(bzz[offset:offset + compressed_size])
    return cache[buffnum][start:start + size].decode("utf-8", "replace")


def extract_tsk_crossrefs(raw_text: str) -> Tuple[List[str], Optional[str]]:
    refs = [normalize_space(html.unescape(item)) for item in TSK_REFERENCE_RE.findall(raw_text)]
    refs = [item for item in refs if item]
    note_text = TSK_REFERENCE_TAG_RE.sub(" ", raw_text)
    note_text = TSK_INLINE_TAG_RE.sub(" ", note_text)
    note_text = TSK_LINE_BREAK_RE.sub(" ", note_text)
    note_text = XML_TAG_RE.sub(" ", note_text)
    note_text = normalize_space(html.unescape(note_text)).strip(" ;,")
    if note_text:
        note_text = SEMICOLON_SPACE_RE.sub("; ", note_text)
        note_text = COMMA_SPACE_RE.sub(", ", note_text)
        note_text = DUPLICATE_COMMA_RE.sub(", ", note_text)
        note_text = DUPLICATE_SEMICOLON_RE.sub("; ", note_text)
        note_text = DUPLICATE_WORD_RE.sub(r"\1", note_text)
    return list(dict.fromkeys(refs)), note_text or None


def parse_tsk_module() -> Tuple[Dict[Tuple[str, int, int], List[str]], Dict[Tuple[str, int, int], List[str]], Dict[str, object]]:
    diagnostics: Dict[str, object] = {
        "archive_present": TSK_ZIP.exists(),
        "status": "unparsed",
    }
    if not TSK_ZIP.exists():
        diagnostics["reason"] = "TSK archive not found."
        return {}, {}, diagnostics
    verse_counts = load_kjv_versification()
    if not verse_counts:
        diagnostics["reason"] = "KJV versification data not found."
        return {}, {}, diagnostics

    index_maps = {
        "ot": build_tsk_index_map(TSK_OT_BOOKS, verse_counts),
        "nt": build_tsk_index_map(TSK_NT_BOOKS, verse_counts),
    }
    crossrefs: Dict[Tuple[str, int, int], List[str]] = defaultdict(list)
    notes: Dict[Tuple[str, int, int], List[str]] = defaultdict(list)

    with zipfile.ZipFile(TSK_ZIP) as zf:
        diagnostics["members"] = zf.namelist()
        for testament, base in {
            "ot": "modules/comments/zcom/tsk/ot",
            "nt": "modules/comments/zcom/tsk/nt",
        }.items():
            bzv = zf.read(f"{base}.bzv")
            bzs = zf.read(f"{base}.bzs")
            bzz = zf.read(f"{base}.bzz")
            entries = len(bzv) // 10
            diagnostics[f"{testament}_entries"] = entries
            blob_cache: Dict[int, bytes] = {}
            for index in range(entries):
                verse_key = index_maps[testament].get(index)
                if not verse_key:
                    continue
                raw_text = decode_tsk_blob(bzv, bzs, bzz, index, blob_cache)
                if not raw_text:
                    continue
                refs, note_text = extract_tsk_crossrefs(raw_text)
                if refs:
                    crossrefs[verse_key].extend(refs)
                if has_min_alpha_words(note_text, minimum=5):
                    notes[verse_key].append(note_text)

    cooked_crossrefs = {key: list(dict.fromkeys(values)) for key, values in crossrefs.items()}
    cooked_notes = {key: list(dict.fromkeys(values)) for key, values in notes.items()}
    diagnostics["status"] = "parsed"
    diagnostics["verses_with_refs"] = len(cooked_crossrefs)
    diagnostics["verses_with_notes"] = len(cooked_notes)
    diagnostics["total_crossrefs"] = sum(len(v) for v in cooked_crossrefs.values())
    return cooked_crossrefs, cooked_notes, diagnostics


def has_min_alpha_words(text: str, minimum: int) -> bool:
    if not text:
        return False
    count = 0
    for _ in ALPHA_WORD_RE.finditer(text):
        count += 1
        if count >= minimum:
            return True
    return False


@lru_cache(maxsize=None)
def parse_openbible_ref(raw_ref: str) -> Optional[Tuple[str, int, int, str]]:
    cleaned_ref = raw_ref.strip()
    match = OPENBIBLE_REF_RE.match(cleaned_ref)
    if not match:
        return None
    abbr, chapter, verse = match.groups()
    code = OPENBIBLE_BOOK_MAP.get(abbr)
    if not code:
        return None
    return code, int(chapter), int(verse), cleaned_ref


def parse_openbible_crossrefs(limit_per_verse: int = 8) -> Tuple[Dict[Tuple[str, int, int], List[str]], Dict[str, object]]:
    refs: Dict[Tuple[str, int, int], List[Tuple[int, str]]] = defaultdict(list)
    diagnostics: Dict[str, object] = {
        "archive_present": OPENBIBLE_CROSSREFS_ZIP.exists(),
        "license": "CC-BY 2026-04-06 via openbible.info",
        "rows": 0,
        "usable_rows": 0,
    }
    if not OPENBIBLE_CROSSREFS_ZIP.exists():
        return {}, diagnostics
    with zipfile.ZipFile(OPENBIBLE_CROSSREFS_ZIP) as zf:
        lines = zf.read("cross_references.txt").decode("utf-8", "replace").splitlines()
    for line in lines[1:]:
        diagnostics["rows"] += 1
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        src, dst, votes_raw = parts
        src_parsed = parse_openbible_ref(src)
        if not src_parsed:
            continue
        try:
            votes = int(votes_raw)
        except ValueError:
            continue
        if votes <= 0:
            continue
        diagnostics["usable_rows"] += 1
        code, chapter, verse, _ = src_parsed
        refs[(code, chapter, verse)].append((votes, dst))
    cooked: Dict[Tuple[str, int, int], List[str]] = {}
    for key, values in refs.items():
        ranked = sorted(values, key=lambda item: (-item[0], item[1]))
        cooked[key] = [format_cross_reference_ref(f"{target} ({votes})") for votes, target in ranked[:limit_per_verse]]
    diagnostics["verses_with_refs"] = len(cooked)
    return cooked, diagnostics


def strip_tags(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    return normalize_space(html.unescape(text))


def parse_kalvesmaki_html() -> Tuple[Dict[str, List[str]], Dict[str, int]]:
    notes_by_nt_ref: Dict[str, List[str]] = defaultdict(list)
    diagnostics = {"rows": 0, "usable_rows": 0}
    if not KALVESMAKI_HTML.exists():
        return notes_by_nt_ref, diagnostics
    raw = KALVESMAKI_HTML.read_text(encoding="utf-8", errors="replace")
    table_match = re.search(r"<table\b.*?</table>", raw, flags=re.S | re.I)
    if not table_match:
        return notes_by_nt_ref, diagnostics
    table_html = table_match.group(0)
    for row_html in re.findall(r"<tr\b.*?</tr>", table_html, flags=re.S | re.I):
        cells = re.findall(r"<td\b.*?</td>", row_html, flags=re.S | re.I)
        if len(cells) != 3:
            continue
        diagnostics["rows"] += 1
        nt_cell, lxx_cell, mt_cell = [strip_tags(cell) for cell in cells]
        if nt_cell.startswith("New Testament") or not nt_cell:
            continue
        ref_match = re.match(r"([1-3]?\s?[A-Za-z]+(?:\s+[A-Za-z]+)*)\s+(\d+:\d+)", nt_cell)
        if not ref_match:
            continue
        nt_ref = f"{ref_match.group(1)} {ref_match.group(2)}"
        lxx_text = lxx_cell
        mt_text = mt_cell
        note = f"NT quotation aligns more closely with the Hebrew here; cf. Brenton LXX: “{lxx_text}”"
        notes_by_nt_ref[nt_ref].append(note)
        if mt_text:
            notes_by_nt_ref[nt_ref].append(f"Masoretic/Hebrew comparison: “{mt_text}”")
        diagnostics["usable_rows"] += 1
    return notes_by_nt_ref, diagnostics


def parse_name_meanings() -> List[Tuple[str, str]]:
    items: List[Tuple[str, str]] = []
    if not NAME_APPENDIX_MD.exists():
        return items
    for line in NAME_APPENDIX_MD.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        body = line[2:]
        if " — " not in body:
            continue
        raw_name, raw_meaning = body.split(" — ", 1)
        search_name = raw_name.split(" (", 1)[0].strip()
        items.append((search_name, raw_meaning.strip()))
    items.sort(key=lambda item: len(item[0]), reverse=True)
    return items


def parse_proper_name_footnotes() -> Dict[str, List[str]]:
    notes: Dict[str, List[str]] = defaultdict(list)
    if not PROPER_NAMES_CSV.exists():
        return notes
    with PROPER_NAMES_CSV.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ref = normalize_space(row.get("first_reference", ""))
            name = normalize_space(row.get("name", ""))
            translit = normalize_space(row.get("transliteration", ""))
            meaning = normalize_space(row.get("meaning", ""))
            footnote = normalize_space(row.get("footnote", ""))
            if not ref or not name:
                continue
            pieces = [f"Name meaning: {name}"]
            if translit:
                pieces[-1] += f" ({translit})"
            if meaning:
                pieces[-1] += f" — {meaning}"
            if footnote:
                pieces.append(footnote)
            notes[ref].append(" ".join(pieces))
    return notes


def parse_names_of_god_footnotes() -> Dict[str, List[str]]:
    notes: Dict[str, List[str]] = defaultdict(list)
    if not NAMES_OF_GOD_CSV.exists():
        return notes
    with NAMES_OF_GOD_CSV.open(encoding="utf-8") as f:
        raw = f.read().replace("“", '"').replace("”", '"')
    reader = csv.DictReader(raw.splitlines())
    for row in reader:
        ref = normalize_space(row.get("first_reference", ""))
        translit = normalize_space(row.get("transliteration", ""))
        lemma = normalize_space(row.get("lemma", ""))
        meaning = normalize_space(row.get("meaning", ""))
        renderings = normalize_space(row.get("english_renderings", ""))
        footnote = normalize_space(row.get("footnote", ""))
        if not ref:
            continue
        pieces = [f"Name of God: {translit}"]
        if lemma:
            pieces[-1] += f" ({lemma})"
        if meaning:
            pieces[-1] += f" — {meaning}"
        if renderings:
            pieces.append(f"Common English renderings: {renderings}.")
        if footnote:
            pieces.append(footnote)
        notes[ref].append(" ".join(pieces))
    return notes


def parse_hebrew_vocab_footnotes() -> Dict[str, List[str]]:
    return parse_vocab_footnotes("Hebrew", "Heb. vocab", [HEBREW_VOCAB_CSV, VOCAB_CLEANUP_CSV])


def parse_greek_vocab_footnotes() -> Dict[str, List[str]]:
    return parse_vocab_footnotes("Greek", "Gk. vocab", [GREEK_VOCAB_CSV, VOCAB_CLEANUP_CSV])


def parse_vocab_footnotes(language: str, label: str, paths: List[Path]) -> Dict[str, List[str]]:
    by_key: Dict[Tuple[str, str], str] = {}
    order: List[Tuple[str, str]] = []
    for path in paths:
        if not path.exists():
            continue
        raw = path.read_text(encoding="utf-8")
        raw = raw.replace("“", '"').replace("”", '"')
        reader = csv.DictReader(raw.splitlines())
        for row in reader:
            row_lang = normalize_space(row.get("language", ""))
            if row_lang.lower() != language.lower():
                continue
            ref = normalize_space(row.get("first_reference", ""))
            lemma = normalize_space(row.get("lemma", ""))
            translit = normalize_space(row.get("transliteration", ""))
            meaning = normalize_space(row.get("meaning", ""))
            renderings = normalize_space(row.get("english_renderings", ""))
            footnote = normalize_space(row.get("footnote", ""))
            if not ref:
                continue
            pieces = []
            head = f"{label}: {translit}"
            if lemma:
                head += f" ({lemma})"
            if meaning:
                head += f" = {meaning}"
            pieces.append(head + ".")
            if renderings:
                pieces.append(f"Common English renderings: {renderings}.")
            if footnote:
                pieces.append(footnote)
            key = (ref, lemma or translit or footnote)
            if key not in by_key:
                order.append(key)
            by_key[key] = " ".join(pieces)
    notes: Dict[str, List[str]] = defaultdict(list)
    for ref, identity in order:
        notes[ref].append(by_key[(ref, identity)])
    return notes


def sort_records(records: List[VerseRecord]) -> List[VerseRecord]:
    order = {code: index for index, code in enumerate(FINAL_BOOK_ORDER)}
    return sorted(
        records,
        key=lambda r: (
            order.get(r.book_code, 9999),
            r.chapter,
            r.verse,
            0 if r.source == "Brenton LXX" else 1,
        ),
    )


REF_BOOK_ORDER = {code: idx for idx, code in enumerate(FINAL_BOOK_ORDER)}
CROSS_REFERENCE_BOOK_PATTERN = r"(?:[1-3]\s*)?[A-Za-z]+(?:\s+[A-Za-z]+)*"
CROSS_REFERENCE_FULL_RANGE_RE = re.compile(
    rf"^({CROSS_REFERENCE_BOOK_PATTERN})\s+(\d+):(\d+)-({CROSS_REFERENCE_BOOK_PATTERN})\s+(\d+):(\d+)$"
)
CROSS_REFERENCE_CHAPTER_RANGE_RE = re.compile(
    rf"^({CROSS_REFERENCE_BOOK_PATTERN})\s+(\d+):(\d+)-(\d+):(\d+)$"
)
CROSS_REFERENCE_RE = re.compile(
    rf"^({CROSS_REFERENCE_BOOK_PATTERN})\s+(\d+)(?::(\d+)(?:-(\d+))?)?$"
)


def cross_reference_book_code(book_label: str) -> str:
    book_label = normalize_space(book_label)
    book_code = REF_BOOK_ALIASES.get(book_label)
    if not book_code:
        compact = book_label.replace(" ", "")
        book_code = REF_BOOK_ALIASES.get(compact, "")
    return book_code


def format_cross_reference_ref(ref: str) -> str:
    ref = CROSS_REFERENCE_VOTE_SUFFIX_RE.sub("", normalize_space(ref.strip()))
    match = OPENBIBLE_TARGET_REF_RE.match(ref)
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
        if not end_code:
            return ref
        if end_code == start_code and end_chapter == start_chapter:
            label += f"-{int(end_verse)}"
        elif end_code == start_code:
            label += f"-{int(end_chapter)}:{int(end_verse)}"
        else:
            end_label = STANDARD_BOOK_NAMES.get(end_code, end_book)
            label += f"-{end_label} {int(end_chapter)}:{int(end_verse)}"
    return label


@lru_cache(maxsize=None)
def parse_cross_reference(ref: str) -> Optional[Tuple[str, str, int, Optional[int], Optional[int], str]]:
    ref = format_cross_reference_ref(ref)
    match = CROSS_REFERENCE_FULL_RANGE_RE.match(ref)
    if match:
        book_label, chapter, verse, end_book_label, _end_chapter, _end_verse = match.groups()
        book_label = normalize_space(book_label)
        book_code = cross_reference_book_code(book_label)
        end_book_code = cross_reference_book_code(end_book_label)
        if not book_code or not end_book_code:
            return None
        return (book_code, book_label, int(chapter), int(verse), -1, ref)
    match = CROSS_REFERENCE_CHAPTER_RANGE_RE.match(ref)
    if match:
        book_label, chapter, verse, _end_chapter, _end_verse = match.groups()
        book_label = normalize_space(book_label)
        book_code = cross_reference_book_code(book_label)
        if not book_code:
            return None
        return (book_code, book_label, int(chapter), int(verse), -1, ref)
    match = CROSS_REFERENCE_RE.match(ref)
    if not match:
        return None
    book_label = normalize_space(match.group(1))
    chapter = int(match.group(2))
    verse = int(match.group(3)) if match.group(3) else None
    verse_end = int(match.group(4)) if match.group(4) else verse
    book_code = cross_reference_book_code(book_label)
    if not book_code:
        return None
    return (book_code, book_label, chapter, verse, verse_end, ref)


def sort_cross_reference_key(ref: str) -> Tuple[int, int, int, str]:
    parsed = parse_cross_reference(ref)
    if not parsed:
        return (9999, 9999, 9999, ref)
    book_code, _, chapter, verse, _, raw_ref = parsed
    verse = verse or 0
    return (REF_BOOK_ORDER.get(book_code, 9999), chapter, verse, raw_ref)


def compress_cross_reference_ranges(refs: List[str]) -> List[str]:
    compressed: List[str] = []
    run_book_code = ""
    run_book_label = ""
    run_chapter = -1
    run_start = -1
    run_end = -1

    def flush_run() -> None:
        nonlocal run_book_code, run_book_label, run_chapter, run_start, run_end
        if run_start == -1:
            return
        if run_start == run_end:
            compressed.append(f"{run_book_label} {run_chapter}:{run_start}")
        else:
            compressed.append(f"{run_book_label} {run_chapter}:{run_start}-{run_end}")
        run_book_code = ""
        run_book_label = ""
        run_chapter = -1
        run_start = -1
        run_end = -1

    for ref in refs:
        parsed = parse_cross_reference(ref)
        if not parsed:
            flush_run()
            compressed.append(ref)
            continue
        book_code, book_label, chapter, verse, verse_end, raw_ref = parsed
        if verse is None:
            flush_run()
            compressed.append(raw_ref)
            continue
        if verse_end is not None and verse_end != verse:
            flush_run()
            compressed.append(raw_ref)
            continue
        if (
            run_start != -1
            and book_code == run_book_code
            and chapter == run_chapter
            and verse == run_end + 1
        ):
            run_end = verse
            continue
        flush_run()
        run_book_code = book_code
        run_book_label = book_label
        run_chapter = chapter
        run_start = verse
        run_end = verse

    flush_run()
    return compressed


def canonicalize_cross_references(refs: List[str]) -> List[str]:
    cleaned = []
    for ref in refs:
        normalized = format_cross_reference_ref(ref)
        if parse_cross_reference(normalized):
            cleaned.append(normalized)
    unique = list(dict.fromkeys(cleaned))
    return compress_cross_reference_ranges(sorted(unique, key=sort_cross_reference_key))


def thin_display_cross_references(refs: List[str], normal_limit: Optional[int] = None) -> List[str]:
    # Records canonicalize once during merge; renderers only need optional thinning.
    canonical_refs = [ref for ref in refs if ref]
    if not normal_limit or len(canonical_refs) <= normal_limit:
        return canonical_refs
    if normal_limit <= 1:
        return canonical_refs[:1]
    chosen_indexes = []
    max_index = len(canonical_refs) - 1
    for step in range(normal_limit):
        index = round(step * max_index / (normal_limit - 1))
        if not chosen_indexes or index != chosen_indexes[-1]:
            chosen_indexes.append(index)
    return [canonical_refs[index] for index in chosen_indexes]


def trim_light_edition_records(records: List[VerseRecord]) -> List[VerseRecord]:
    return [record for record in records if record.book_code not in APOCRYPHA_BOOKS]


def merge_records() -> Tuple[List[VerseRecord], Dict[str, object]]:
    brenton, brenton_diag = parse_brenton_usfm()
    ukjv, ukjv_diag = parse_ukjv_xml()
    enoch, enoch_diag = parse_enoch_charles()
    kal_notes, kal_diag = parse_kalvesmaki()
    kal_html_notes, kal_html_diag = parse_kalvesmaki_html()
    tsk_crossrefs, tsk_notes, tsk_diag = parse_tsk_module()
    crossrefs, crossref_diag = parse_openbible_crossrefs()
    proper_name_notes = parse_proper_name_footnotes()
    names_of_god_notes = parse_names_of_god_footnotes()
    hebrew_vocab_notes = parse_hebrew_vocab_footnotes()
    greek_vocab_notes = parse_greek_vocab_footnotes()
    all_records = brenton + ukjv + enoch
    for record in all_records:
        key = (record.book_code, record.chapter, record.verse)
        ref = record.ref
        if key in tsk_crossrefs:
            record.cross_references.extend(tsk_crossrefs[key])
        elif key in crossrefs:
            record.cross_references.extend(crossrefs[key])
        if key in tsk_notes:
            record.study_notes.extend(tsk_notes[key])
        if record.book_code in NT_BOOKS_SET:
            notes = kal_html_notes.get(ref, []) or kal_notes.get(ref, [])
            if notes:
                record.study_notes.extend(notes)
        if ref in names_of_god_notes:
            record.footnotes.extend(names_of_god_notes[ref])
        if ref in proper_name_notes:
            record.footnotes.extend(proper_name_notes[ref])
        if ref in hebrew_vocab_notes:
            record.footnotes.extend(hebrew_vocab_notes[ref])
        if ref in greek_vocab_notes:
            record.footnotes.extend(greek_vocab_notes[ref])
        if record.cross_references:
            record.cross_references = canonicalize_cross_references(record.cross_references)
    name_notes_added = sum(len(v) for v in proper_name_notes.values())
    all_records = sort_records(all_records)
    diagnostics = {
        "brenton": brenton_diag,
        "ukjv": ukjv_diag,
        "enoch_charles": enoch_diag,
        "kalvesmaki_csv": kal_diag,
        "kalvesmaki_html": kal_html_diag,
        "tsk": tsk_diag,
        "openbible_crossrefs": crossref_diag,
        "names_of_god_footnotes_loaded": sum(len(v) for v in names_of_god_notes.values()),
        "proper_name_footnotes_loaded": name_notes_added,
        "hebrew_vocab_footnotes_loaded": sum(len(v) for v in hebrew_vocab_notes.values()),
        "greek_vocab_footnotes_loaded": sum(len(v) for v in greek_vocab_notes.values()),
        "final_book_order": FINAL_BOOK_ORDER,
        "total_records": len(all_records),
    }
    return all_records, diagnostics


def verse_number(n: int) -> str:
    return str(n).translate(SUPERSCRIPTS)


def psalm_mt_label(chapter: int) -> str:
    if 1 <= chapter <= 8:
        return str(chapter)
    if chapter == 9:
        return "9-10"
    if 10 <= chapter <= 112:
        return str(chapter + 1)
    if chapter == 113:
        return "114-115"
    if chapter == 114:
        return "116:1-9"
    if chapter == 115:
        return "116:10-19"
    if 116 <= chapter <= 145:
        return str(chapter + 1)
    if chapter == 146:
        return "147:1-11"
    if chapter == 147:
        return "147:12-20"
    if 148 <= chapter <= 150:
        return str(chapter)
    if chapter == 151:
        return "no MT equivalent"
    return str(chapter)


def chapter_heading(book_code: str, book_name: str, chapter: int) -> str:
    if book_code == "PSA":
        mt = psalm_mt_label(chapter)
        if mt == str(chapter):
            return f"Psalm {chapter}"
        return f"Psalm {chapter} (MT {mt})"
    return f"{book_name} {chapter}"


def render_markdown(
    records: List[VerseRecord],
    diagnostics: Dict[str, object],
    crossrefs_only: bool = False,
    normal_crossrefs: bool = False,
) -> str:
    book_intros = load_book_intros()
    lines = [
        "# Public-Domain Study Bible Prototype",
        "",
        "Prototype build from Brenton LXX OT + UKJV NT.",
        "",
        "## Data Diagnostics",
        "",
        "```json",
        json.dumps(diagnostics, indent=2, ensure_ascii=False),
        "```",
        "",
        "## Editorial Flags",
        "",
        "- TSK public-domain CrossWire module decoded and attached as the primary cross-reference layer.",
        "- OpenBible cross-references remain only as a fallback where TSK is still absent; this layer is CC-BY and provisional.",
        "- Full Kalvesmaki HTML was parsed when present; CSV fallback remains supported.",
        "- Brenton USFM footnotes were extracted and attached inline under each verse.",
        "",
    ]
    if RIGHTS_MD.exists():
        lines.append(RIGHTS_MD.read_text(encoding="utf-8").strip())
        lines.append("")
    if CONVENTIONS_MD.exists():
        lines.append(CONVENTIONS_MD.read_text(encoding="utf-8").strip())
        lines.append("")
    if PREFACE_MD.exists():
        lines.append(PREFACE_MD.read_text(encoding="utf-8").strip())
        lines.append("")

    current_book = None
    current_chapter = None
    paragraph_bits: List[str] = []
    paragraph_notes: List[str] = []

    def flush_paragraph():
        nonlocal paragraph_bits, paragraph_notes
        if paragraph_bits:
            lines.append(" ".join(paragraph_bits).strip())
            lines.append("")
        if paragraph_notes:
            lines.append("Notes:")
            for note in paragraph_notes:
                lines.append(f"- {note}")
            lines.append("")
        paragraph_bits = []
        paragraph_notes = []

    for record in records:
        if record.book_name != current_book:
            flush_paragraph()
            current_book = record.book_name
            current_chapter = None
            lines.append(f"# {record.book_name}")
            lines.append("")
            intro_row = book_intros.get(record.book_code)
            if book_intro_has_content(intro_row):
                lines.extend(render_markdown_intro(intro_row))
        if record.chapter != current_chapter:
            flush_paragraph()
            current_chapter = record.chapter
            lines.append(f"## {chapter_heading(record.book_code, record.book_name, record.chapter)}")
            lines.append("")
        if record.paragraph_start:
            flush_paragraph()
        if record.section and (not lines or lines[-1] != f"*{record.section}*"):
            flush_paragraph()
            lines.append(f"*{record.section}*")
            lines.append("")
        ref = record.ref
        paragraph_bits.append(f"{verse_number(record.verse)} {record.text}")
        if not crossrefs_only:
            for note in record.footnotes:
                paragraph_notes.append(f"{ref} Brenton note: {note}")
            for note in record.study_notes:
                paragraph_notes.append(f"{ref} {note}")
        display_crossrefs = thin_display_cross_references(
            record.cross_references,
            NORMAL_CROSSREF_LIMIT if normal_crossrefs else None,
        )
        if display_crossrefs:
            paragraph_notes.append(f"{ref} Cross-refs: {'; '.join(display_crossrefs)}")
    flush_paragraph()
    if APPENDIX_MD.exists():
        lines.append("")
        lines.append(APPENDIX_MD.read_text(encoding="utf-8").strip())
    if NAME_APPENDIX_MD.exists():
        lines.append("")
        lines.append(NAME_APPENDIX_MD.read_text(encoding="utf-8").strip())
    return "\n".join(lines)


def render_pdf_excerpt(records: List[VerseRecord], markdown_path: Path) -> Optional[Path]:
    try:
        from reportlab.lib.enums import TA_CENTER
        from reportlab.lib.pagesizes import LETTER
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import inch
        from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
    except Exception:
        return None

    pdf_path = OUTPUT / f"{OUTPUT_PREFIX}_excerpt.pdf"
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=LETTER,
        leftMargin=0.8 * inch,
        rightMargin=0.8 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="BookTitle", parent=styles["Heading1"], alignment=TA_CENTER, spaceAfter=10))
    styles.add(ParagraphStyle(name="ChapterTitle", parent=styles["Heading2"], spaceBefore=8, spaceAfter=8))
    styles.add(ParagraphStyle(name="VersePara", parent=styles["BodyText"], fontName="Times-Roman", fontSize=11, leading=15, spaceAfter=8))
    styles.add(ParagraphStyle(name="Footnote", parent=styles["BodyText"], fontName="Times-Italic", fontSize=8.5, leading=10, leftIndent=12, spaceAfter=4))

    story = [
        Paragraph("Public-Domain Study Bible Prototype", styles["BookTitle"]),
        Paragraph(f"Full manuscript source: {markdown_path.name}", styles["BodyText"]),
        Spacer(1, 0.15 * inch),
    ]

    current_book = None
    current_chapter = None
    para_parts: List[str] = []
    note_parts: List[str] = []
    chapter_count = 0

    def flush():
        nonlocal para_parts, note_parts
        if para_parts:
            story.append(Paragraph(" ".join(para_parts), styles["VersePara"]))
        for note in note_parts:
            story.append(Paragraph(note, styles["Footnote"]))
        para_parts = []
        note_parts = []

    for record in records:
        if record.book_name != current_book:
            flush()
            current_book = record.book_name
            current_chapter = None
            story.append(Paragraph(record.book_name, styles["BookTitle"]))
        if record.chapter != current_chapter:
            flush()
            current_chapter = record.chapter
            chapter_count += 1
            story.append(Paragraph(chapter_heading(record.book_code, record.book_name, record.chapter), styles["ChapterTitle"]))
            if chapter_count > 8:
                break
        if record.paragraph_start:
            flush()
        para_parts.append(f"<super>{record.verse}</super> {record.text}")
        ref = record.ref
        for note in record.footnotes:
            note_parts.append(f"{ref} Brenton note: {note}")
        for note in record.study_notes:
            note_parts.append(f"{ref} {note}")
    flush()
    doc.build(story)
    return pdf_path


def latex_escape(text: str) -> str:
    if not LATEX_ESCAPE_RE.search(text):
        return text
    return LATEX_ESCAPE_RE.sub(lambda match: LATEX_REPLACEMENTS[match.group(0)], text)


def chunk_list(items: List[str], size: int) -> List[List[str]]:
    return [items[i:i + size] for i in range(0, len(items), size)]


@lru_cache(maxsize=1)
def load_book_intros() -> Dict[str, Dict[str, str]]:
    if not BOOK_INTROS_CSV.exists():
        return {}
    with BOOK_INTROS_CSV.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {row["book_code"].strip(): row for row in rows if row.get("book_code", "").strip()}


def book_intro_has_content(row: Optional[Dict[str, str]]) -> bool:
    if not row:
        return False
    excluded = {"book_code", "book_name", "canonical_order", "section", "intro_title", "status", "source_notes"}
    for key, value in row.items():
        if key in excluded:
            continue
        if (value or "").strip():
            return True
    return False


def compact_intro_groups(row: Dict[str, str]) -> List[Tuple[str, str]]:
    def parts(*keys: str) -> str:
        values = [row.get(key, "").strip() for key in keys if row.get(key, "").strip()]
        return " ".join(values).strip()

    witnesses = []
    if parts("oldest_fragment", "oldest_fragment_date"):
        witnesses.append("Frag. " + parts("oldest_fragment", "oldest_fragment_date"))
    if parts("oldest_substantial_manuscript", "oldest_substantial_date"):
        witnesses.append("Subst. " + parts("oldest_substantial_manuscript", "oldest_substantial_date"))
    if parts("oldest_complete_hebrew", "oldest_complete_hebrew_date"):
        witnesses.append("Heb. " + parts("oldest_complete_hebrew", "oldest_complete_hebrew_date"))
    if parts("oldest_complete_greek", "oldest_complete_greek_date"):
        witnesses.append("Gk. " + parts("oldest_complete_greek", "oldest_complete_greek_date"))

    external = []
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


def render_markdown_intro(row: Dict[str, str]) -> List[str]:
    lines = [f"> **{row.get('intro_title') or row.get('book_name') or row.get('book_code')} Introduction**", ">"]
    for label, value in compact_intro_groups(row):
        lines.append(f"> **{label}** {value}")
        lines.append(">")
    lines.append("")
    return lines


def render_latex_intro(row: Dict[str, str]) -> List[str]:
    title = row.get("intro_title") or row.get("book_name") or row.get("book_code")
    lines = [
        r"\newpage",
        r"\section*{" + latex_escape(title + " Introduction") + "}",
        r"{\notefont\fontsize{8.7}{10.2}\selectfont",
    ]
    for label, value in compact_intro_groups(row):
        lines.append(r"\noindent\textbf{" + latex_escape(label) + r".} " + latex_escape(value) + r"\par")
        lines.append(r"\vspace{0.18em}")
    lines.extend([
        r"}",
        "",
    ])
    return lines


def verse_layout_tier(combined_load: int, crossref_count: int) -> str:
    if crossref_count <= 4 and combined_load <= 450:
        return "normal"
    if crossref_count >= EXTREME_CROSSREF_THRESHOLD or combined_load >= EXTREME_COMBINED_LOAD_THRESHOLD:
        return "extreme"
    return "heavy"


def format_textual_paragraph_item(record: VerseRecord) -> str:
    notes = list(dict.fromkeys(note.strip() for note in record.footnotes if note.strip()))
    if not notes:
        return ""
    marker = (
        r"{\color{tnaccent}\fontsize{7.8}{7.8}\selectfont\textbf{"
        + str(record.verse)
        + r"}}"
    )
    return marker + r"\," + " ".join(latex_escape(note) for note in notes)


def format_crossref_paragraph_item(record: VerseRecord, normal_crossrefs: bool = False) -> str:
    refs = thin_display_cross_references(
        record.cross_references,
        NORMAL_CROSSREF_LIMIT if normal_crossrefs else None,
    )
    if not refs:
        return ""
    marker = (
        r"{\color{tnaccent}\fontsize{7.8}{7.8}\selectfont\textbf{"
        + str(record.verse)
        + r"}}"
    )
    return marker + r"\," + latex_escape("; ".join(refs))


def format_study_paragraph_item(record: VerseRecord) -> str:
    notes = list(dict.fromkeys(note.strip() for note in record.study_notes if note.strip()))
    if not notes:
        return ""
    marker = (
        r"{\color{tnaccent}\fontsize{7.8}{7.8}\selectfont\textbf{"
        + str(record.verse)
        + r"}}"
    )
    return marker + r"\," + " ".join(latex_escape(note) for note in notes)


def render_latex(
    records: List[VerseRecord],
    diagnostics: Dict[str, object],
    crossrefs_only: bool = False,
    normal_crossrefs: bool = False,
) -> str:
    book_intros = load_book_intros()
    lines = [
        r"\documentclass[10pt,twoside]{article}",
        r"\usepackage[paperwidth=6.125in,paperheight=9.25in,inner=0.60in,outer=0.50in,top=0.44in,bottom=0.60in,footskip=0.22in,headheight=17pt,headsep=0.08in]{geometry}",
        r"\usepackage[svgnames]{xcolor}",
        r"\usepackage{fontspec}",
        r"\setmainfont{Baskerville}",
        r"\newfontfamily\notefont{Times New Roman}",
        r"\usepackage{parskip}",
        r"\usepackage{fancyhdr}",
        r"\usepackage[hang,flushmargin,bottom]{footmisc}",
        r"\usepackage{tabularx}",
        r"\usepackage{titlesec}",
        r"\definecolor{tnaccent}{HTML}{7C2D22}",
        r"\definecolor{tnrule}{HTML}{A45A4A}",
        r"\color{black}",
        r"\titleformat{\section}{\color{tnaccent}\fontsize{13.8}{14.2}\bfseries\scshape\centering}{}{0pt}{}",
        r"\titleformat{\subsection}{\color{tnaccent}\fontsize{10.6}{11.2}\bfseries\scshape}{}{0pt}{}",
        r"\setlength{\parindent}{0pt}",
        r"\interfootnotelinepenalty=100",
        r"\emergencystretch=1.5em",
        r"\raggedbottom",
        r"\sloppy",
        r"\AtBeginDocument{\fontsize{9.5}{11.5}\selectfont}",
        r"\pagestyle{fancy}",
        r"\fancyhf{}",
        r"\fancyhead[LE]{\fontsize{6.6}{7.0}\selectfont\scshape\leftmark}",
        r"\fancyhead[RO]{\fontsize{6.6}{7.0}\selectfont\scshape\rightmark}",
        r"\fancyfoot[LE,RO]{\fontsize{5.8}{5.8}\selectfont\thepage}",
        r"\fancyfoot[LO,RE]{}",
        r"\renewcommand{\sectionmark}[1]{\markboth{#1}{}}",
        r"\renewcommand{\subsectionmark}[1]{\markright{#1}}",
        r"\renewcommand{\headrulewidth}{0.2pt}",
        r"\renewcommand{\footrulewidth}{0pt}",
        r"\renewcommand{\headrule}{\hbox to\headwidth{\color{tnrule}\leaders\hrule height \headrulewidth\hfill}}",
        r"\begin{document}",
        r"\begin{center}{\color{tnaccent}\fontsize{15}{16}\bfseries\scshape Public-Domain Study Bible Prototype}\end{center}",
        r"\bigskip",
    ]
    if RIGHTS_MD.exists():
        rights = RIGHTS_MD.read_text(encoding="utf-8")
        lines.append(r"\newpage")
        for raw_line in rights.splitlines():
            line = raw_line.strip()
            if not line:
                lines.append("")
            elif line.startswith("## "):
                lines.append(r"\section*{" + latex_escape(line[3:]) + "}")
            elif line.startswith("### "):
                lines.append(r"\subsection*{" + latex_escape(line[4:]) + "}")
            elif line.startswith("- "):
                lines.append(r"\noindent$\bullet$ " + latex_escape(line[2:]) + r"\par")
            else:
                lines.append(r"\noindent " + latex_escape(line) + r"\par")
    if CONVENTIONS_MD.exists():
        conventions = CONVENTIONS_MD.read_text(encoding="utf-8")
        lines.append(r"\newpage")
        for raw_line in conventions.splitlines():
            line = raw_line.strip()
            if not line:
                lines.append("")
            elif line.startswith("## "):
                lines.append(r"\section*{" + latex_escape(line[3:]) + "}")
            elif line.startswith("### "):
                lines.append(r"\subsection*{" + latex_escape(line[4:]) + "}")
            elif line.startswith("- "):
                lines.append(r"\noindent$\bullet$ " + latex_escape(line[2:]) + r"\par")
            else:
                lines.append(r"\noindent " + latex_escape(line) + r"\par")
    if PREFACE_MD.exists():
        preface = PREFACE_MD.read_text(encoding="utf-8")
        lines.append(r"\newpage")
        for raw_line in preface.splitlines():
            line = raw_line.strip()
            if not line:
                lines.append("")
            elif line.startswith("## "):
                lines.append(r"\section*{" + latex_escape(line[3:]) + "}")
            elif line.startswith("### "):
                lines.append(r"\subsection*{" + latex_escape(line[4:]) + "}")
            elif line.startswith("|"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if cells and not all(cell.replace("-", "").strip() == "" for cell in cells):
                    lines.append(r"\noindent " + latex_escape(" | ".join(cells)) + r"\par")
            elif line.startswith("- "):
                lines.append(r"\noindent " + latex_escape(line[2:]) + r"\par")
            else:
                lines.append(r"\noindent " + latex_escape(line) + r"\par")
    current_book = None
    current_chapter = None
    paragraph_bits: List[str] = []
    paragraph_textual_notes: List[str] = []
    paragraph_study_notes: List[str] = []
    paragraph_crossrefs: List[str] = []

    def flush():
        nonlocal paragraph_bits, paragraph_textual_notes, paragraph_study_notes, paragraph_crossrefs
        if paragraph_bits:
            lines.append(r"\noindent " + " ".join(paragraph_bits) + r"\par")
        if paragraph_textual_notes and not crossrefs_only:
            lines.append(r"{\notefont\fontsize{6.8}{7.5}\selectfont\noindent{\color{tnaccent}\textit{T: }}\," + r"\enspace ".join(paragraph_textual_notes) + r"\par}")
        if paragraph_study_notes and not crossrefs_only:
            lines.append(r"{\notefont\fontsize{6.8}{7.5}\selectfont\noindent{\color{tnaccent}\textit{N: }}\," + r"\enspace ".join(paragraph_study_notes) + r"\par}")
        if paragraph_crossrefs:
            lines.append(
                r"{\notefont\fontsize{6.8}{7.5}\selectfont\noindent{\color{tnaccent}\textit{X: }}"
                + r"\,"
                + r"\enspace ".join(paragraph_crossrefs)
                + r"\par}"
            )
        paragraph_bits = []
        paragraph_textual_notes = []
        paragraph_crossrefs = []
        paragraph_study_notes = []

    for record in records:
        if record.book_name != current_book:
            flush()
            current_book = record.book_name
            current_chapter = None
            intro_row = book_intros.get(record.book_code)
            if book_intro_has_content(intro_row):
                lines.extend(render_latex_intro(intro_row))
            lines.append(r"\section*{" + latex_escape(record.book_name) + "}")
            lines.append(r"\markboth{" + latex_escape(record.book_name.upper()) + r"}{}")
        if record.chapter != current_chapter:
            flush()
            current_chapter = record.chapter
            chapter_label = chapter_heading(record.book_code, record.book_name, record.chapter)
            lines.append(r"\subsection*{" + latex_escape(chapter_label) + "}")
            lines.append(r"\markright{" + latex_escape(chapter_label.upper()) + r"}")
        if record.paragraph_start:
            flush()
        verse_text = r"{\color{tnaccent}\fontsize{6.9}{6.9}\selectfont\textsuperscript{" + str(record.verse) + r"}} " + latex_escape(record.text)
        paragraph_bits.append(verse_text)
        if not crossrefs_only:
            textual_item = format_textual_paragraph_item(record)
            if textual_item:
                paragraph_textual_notes.append(textual_item)
            study_item = format_study_paragraph_item(record)
            if study_item:
                paragraph_study_notes.append(study_item)
        crossref_item = format_crossref_paragraph_item(record, normal_crossrefs=normal_crossrefs)
        if crossref_item:
            paragraph_crossrefs.append(crossref_item)
    flush()
    if APPENDIX_MD.exists():
        appendix = APPENDIX_MD.read_text(encoding="utf-8")
        lines.append(r"\newpage")
        for raw_line in appendix.splitlines():
            line = raw_line.strip()
            if not line:
                lines.append("")
            elif line.startswith("## "):
                lines.append(r"\section*{" + latex_escape(line[3:]) + "}")
            elif line.startswith("### "):
                lines.append(r"\subsection*{" + latex_escape(line[4:]) + "}")
            elif line.startswith("|"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if cells and not all(cell.replace("-", "").strip() == "" for cell in cells):
                    lines.append(r"\noindent " + latex_escape(" | ".join(cells)) + r"\par")
            elif line.startswith("- "):
                lines.append(r"\noindent " + latex_escape(line[2:]) + r"\par")
            else:
                lines.append(r"\noindent " + latex_escape(line) + r"\par")
    if NAME_APPENDIX_MD.exists():
        appendix = NAME_APPENDIX_MD.read_text(encoding="utf-8")
        lines.append(r"\newpage")
        for raw_line in appendix.splitlines():
            line = raw_line.strip()
            if not line:
                lines.append("")
            elif line.startswith("## "):
                lines.append(r"\section*{" + latex_escape(line[3:]) + "}")
            elif line.startswith("### "):
                lines.append(r"\subsection*{" + latex_escape(line[4:]) + "}")
            elif line.startswith("|"):
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                if cells and not all(cell.replace("-", "").strip() == "" for cell in cells):
                    lines.append(r"\noindent " + latex_escape(" | ".join(cells)) + r"\par")
            elif line.startswith("- "):
                lines.append(r"\noindent " + latex_escape(line[2:]) + r"\par")
            else:
                lines.append(r"\noindent " + latex_escape(line) + r"\par")
    lines.append(r"\end{document}")
    return "\n".join(lines)


def build_overflow_report(records: List[VerseRecord]) -> Dict[str, object]:
    rows = []
    for record in records:
        note_text = " ".join(record.footnotes + record.study_notes)
        crossref_text = "; ".join(record.cross_references)
        crossref_count = len(record.cross_references)
        combined_load = len(record.text) + len(note_text) + len(crossref_text)
        rows.append(
            {
                "ref": record.ref,
                "source": record.source,
                "tier": verse_layout_tier(combined_load, crossref_count),
                "text_chars": len(record.text),
                "footnote_count": len(record.footnotes) + len(record.study_notes),
                "footnote_chars": len(note_text),
                "crossref_count": crossref_count,
                "crossref_chars": len(crossref_text),
                "combined_load": combined_load,
            }
        )

    def top_by(key: str, limit: int = 25) -> List[Dict[str, object]]:
        return nsmallest(limit, rows, key=lambda row: (-row[key], row["ref"]))

    margin_ref_exceeders = [
        row for row in rows
        if row["crossref_count"] > MAX_MARGIN_REFS_DISPLAY
    ]

    return {
        "top_footnote_char_verses": top_by("footnote_chars"),
        "top_crossref_count_verses": top_by("crossref_count"),
        "top_crossref_char_verses": top_by("crossref_chars"),
        "top_combined_load_verses": top_by("combined_load"),
        "margin_overflow_policy": {
            "max_margin_refs_display": MAX_MARGIN_REFS_DISPLAY,
            "margin_ref_group_size": MARGIN_REF_GROUP_SIZE,
            "heavy_crossref_threshold": HEAVY_CROSSREF_THRESHOLD,
            "extreme_crossref_threshold": EXTREME_CROSSREF_THRESHOLD,
            "extreme_combined_load_threshold": EXTREME_COMBINED_LOAD_THRESHOLD,
        },
        "tier_counts": {
            "normal": sum(1 for row in rows if row["tier"] == "normal"),
            "heavy": sum(1 for row in rows if row["tier"] == "heavy"),
            "extreme": sum(1 for row in rows if row["tier"] == "extreme"),
        },
        "verses_exceeding_margin_ref_cap": nsmallest(
            100,
            margin_ref_exceeders,
            key=lambda row: (-row["crossref_count"], row["ref"]),
        ),
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--crossrefs-only", action="store_true")
    parser.add_argument("--normal-crossrefs", action="store_true")
    args = parser.parse_args()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    records, diagnostics = merge_records()
    if args.crossrefs_only:
        records = trim_light_edition_records(records)
    if args.crossrefs_only and args.normal_crossrefs:
        output_prefix = OUTPUT_PREFIX_CROSSREFS_NORMAL
    elif args.crossrefs_only:
        output_prefix = OUTPUT_PREFIX_CROSSREFS_ONLY
    else:
        output_prefix = OUTPUT_PREFIX
    markdown = render_markdown(
        records,
        diagnostics,
        crossrefs_only=args.crossrefs_only,
        normal_crossrefs=args.normal_crossrefs,
    )
    md_path = OUTPUT / f"{output_prefix}.md"
    md_path.write_text(markdown, encoding="utf-8")
    json_path = OUTPUT / f"{output_prefix}_diagnostics.json"
    json_path.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False), encoding="utf-8")
    overflow_path = OUTPUT / f"{output_prefix}_overflow_report.json"
    overflow_path.write_text(json.dumps(build_overflow_report(records), indent=2, ensure_ascii=False), encoding="utf-8")
    tex_path = OUTPUT / f"{output_prefix}.tex"
    tex_path.write_text(
        render_latex(
            records,
            diagnostics,
            crossrefs_only=args.crossrefs_only,
            normal_crossrefs=args.normal_crossrefs,
        ),
        encoding="utf-8",
    )
    pdf_path = render_pdf_excerpt(records, md_path)
    summary = {
        "markdown": str(md_path),
        "diagnostics": str(json_path),
        "overflow_report": str(overflow_path),
        "latex": str(tex_path),
        "pdf_excerpt": str(pdf_path) if pdf_path else None,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
