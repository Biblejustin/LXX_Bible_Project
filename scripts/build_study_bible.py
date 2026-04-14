#!/usr/bin/env python3
import csv
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
PREFACE_MD = ROOT / "data" / "preface_charts.md"
APPENDIX_MD = ROOT / "data" / "appendix_references.md"
NAME_APPENDIX_MD = ROOT / "data" / "name_meanings_appendix.md"
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
    "1ES", "MAN", "3MA", "4MA",
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

SUPERSCRIPTS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


@dataclass
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

    @property
    def ref(self) -> str:
        return f"{self.book_name} {self.chapter}:{self.verse}"


def normalize_space(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def strip_usfm_markup(text: str) -> str:
    text = re.sub(r"\\f\s+\+.*?\\f\*", "", text)
    text = re.sub(r"\\x\s+\+.*?\\x\*", "", text)
    text = re.sub(r"\\[a-z0-9*]+", " ", text)
    text = text.replace("~", " ")
    return normalize_space(text)


def extract_usfm_footnotes(text: str) -> List[str]:
    notes = []
    for raw in re.findall(r"\\f\s+\+(.*?)\\f\*", text):
        body = re.sub(r"\\fr\s+[^\\]+", "", raw)
        body = re.sub(r"\\fqa\s+", "", body)
        body = re.sub(r"\\ft\s+", "", body)
        body = re.sub(r"\\fk\s+", "", body)
        body = re.sub(r"\\fq\s+", "", body)
        body = re.sub(r"\\[a-z0-9*]+ ?", "", body)
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
                    m = re.match(r"\\id\s+([A-Z0-9]+)", line)
                    if m:
                        book_code = m.group(1)
                elif line.startswith("\\toc1 "):
                    book_name = line[6:].strip()
                elif line.startswith("\\mt1 ") and not book_name:
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
                    m = re.match(r"\\v\s+(\d+)\s+(.*)", line)
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
        book_code, book_name = UKJV_BOOK_MAP[bnumber]
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
    refs = [normalize_space(html.unescape(item)) for item in re.findall(r"<reference\b[^>]*>(.*?)</reference>", raw_text, flags=re.S)]
    refs = [item for item in refs if item]
    note_text = re.sub(r"<reference\b[^>]*>.*?</reference>", " ", raw_text, flags=re.S)
    note_text = re.sub(r"</?(hi|div|title|catchWord)\b[^>]*>", " ", note_text)
    note_text = re.sub(r"<lb\b[^>]*>", " ", note_text)
    note_text = re.sub(r"<[^>]+>", " ", note_text)
    note_text = normalize_space(html.unescape(note_text)).strip(" ;,")
    if note_text:
        note_text = re.sub(r"\s*;\s*", "; ", note_text)
        note_text = re.sub(r"\s*,\s*", ", ", note_text)
        note_text = re.sub(r"(?:,\s*){2,}", ", ", note_text)
        note_text = re.sub(r"(?:;\s*){2,}", "; ", note_text)
        note_text = re.sub(r"\b([A-Za-z]+)(?:\s+\1\b)+", r"\1", note_text)
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
                alpha_words = re.findall(r"[A-Za-z][A-Za-z'/-]*", note_text or "")
                if note_text and len(alpha_words) >= 5:
                    notes[verse_key].append(f"TSK note: {note_text}")

    cooked_crossrefs = {key: list(dict.fromkeys(values)) for key, values in crossrefs.items()}
    cooked_notes = {key: list(dict.fromkeys(values)) for key, values in notes.items()}
    diagnostics["status"] = "parsed"
    diagnostics["verses_with_refs"] = len(cooked_crossrefs)
    diagnostics["verses_with_notes"] = len(cooked_notes)
    diagnostics["total_crossrefs"] = sum(len(v) for v in cooked_crossrefs.values())
    return cooked_crossrefs, cooked_notes, diagnostics


def parse_openbible_ref(raw_ref: str) -> Optional[Tuple[str, int, int, str]]:
    match = re.match(r"([1-3]?[A-Za-z]+)\.(\d+)\.(\d+)$", raw_ref.strip())
    if not match:
        return None
    abbr, chapter, verse = match.groups()
    code = OPENBIBLE_BOOK_MAP.get(abbr)
    if not code:
        return None
    return code, int(chapter), int(verse), raw_ref.strip()


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
        cooked[key] = [f"{target} ({votes})" for votes, target in ranked[:limit_per_verse]]
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
    return parse_vocab_footnotes("Hebrew", "Hebrew background", [HEBREW_VOCAB_CSV, VOCAB_CLEANUP_CSV])


def parse_greek_vocab_footnotes() -> Dict[str, List[str]]:
    return parse_vocab_footnotes("Greek", "Greek background", [GREEK_VOCAB_CSV, VOCAB_CLEANUP_CSV])


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


def merge_records() -> Tuple[List[VerseRecord], Dict[str, object]]:
    brenton, brenton_diag = parse_brenton_usfm()
    ukjv, ukjv_diag = parse_ukjv_xml()
    kal_notes, kal_diag = parse_kalvesmaki()
    kal_html_notes, kal_html_diag = parse_kalvesmaki_html()
    tsk_crossrefs, tsk_notes, tsk_diag = parse_tsk_module()
    crossrefs, crossref_diag = parse_openbible_crossrefs()
    proper_name_notes = parse_proper_name_footnotes()
    names_of_god_notes = parse_names_of_god_footnotes()
    hebrew_vocab_notes = parse_hebrew_vocab_footnotes()
    greek_vocab_notes = parse_greek_vocab_footnotes()
    all_records = brenton + ukjv
    for record in all_records:
        key = (record.book_code, record.chapter, record.verse)
        if key in tsk_crossrefs:
            record.cross_references.extend(tsk_crossrefs[key])
        elif key in crossrefs:
            record.cross_references.extend(crossrefs[key])
        if key in tsk_notes:
            record.study_notes.extend(tsk_notes[key])
        if record.book_code in NT_BOOKS:
            notes = kal_html_notes.get(record.ref, []) or kal_notes.get(record.ref, [])
            if notes:
                record.study_notes.extend(notes)
        if record.ref in names_of_god_notes:
            record.footnotes.extend(names_of_god_notes[record.ref])
        if record.ref in proper_name_notes:
            record.footnotes.extend(proper_name_notes[record.ref])
        if record.ref in hebrew_vocab_notes:
            record.footnotes.extend(hebrew_vocab_notes[record.ref])
        if record.ref in greek_vocab_notes:
            record.footnotes.extend(greek_vocab_notes[record.ref])
    name_notes_added = sum(len(v) for v in proper_name_notes.values())
    all_records = sort_records(all_records)
    diagnostics = {
        "brenton": brenton_diag,
        "ukjv": ukjv_diag,
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


def render_markdown(records: List[VerseRecord], diagnostics: Dict[str, object]) -> str:
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
        if record.chapter != current_chapter:
            flush_paragraph()
            current_chapter = record.chapter
            lines.append(f"## {record.book_name} {record.chapter}")
            lines.append("")
        if record.paragraph_start:
            flush_paragraph()
        if record.section and (not lines or lines[-1] != f"*{record.section}*"):
            flush_paragraph()
            lines.append(f"*{record.section}*")
            lines.append("")
        paragraph_bits.append(f"{verse_number(record.verse)} {record.text}")
        for note in record.footnotes:
            paragraph_notes.append(f"{record.ref} Brenton note: {note}")
        for note in record.study_notes:
            paragraph_notes.append(f"{record.ref} {note}")
        if record.cross_references:
            paragraph_notes.append(f"{record.ref} Cross-refs: {'; '.join(record.cross_references)}")
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

    pdf_path = OUTPUT / "study_bible_prototype_excerpt.pdf"
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
            story.append(Paragraph(f"Chapter {record.chapter}", styles["ChapterTitle"]))
            if chapter_count > 8:
                break
        if record.paragraph_start:
            flush()
        para_parts.append(f"<super>{record.verse}</super> {record.text}")
        for note in record.footnotes:
            note_parts.append(f"{record.ref} Brenton note: {note}")
        for note in record.study_notes:
            note_parts.append(f"{record.ref} {note}")
    flush()
    doc.build(story)
    return pdf_path


def latex_escape(text: str) -> str:
    replacements = {
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
    return "".join(replacements.get(ch, ch) for ch in text)


def render_latex(records: List[VerseRecord], diagnostics: Dict[str, object]) -> str:
    lines = [
        r"\documentclass[11pt]{article}",
        r"\usepackage[margin=0.85in]{geometry}",
        r"\usepackage[T1]{fontenc}",
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage{parskip}",
        r"\usepackage{titlesec}",
        r"\titleformat{\section}{\Large\bfseries\centering}{}{0pt}{}",
        r"\titleformat{\subsection}{\large\bfseries}{}{0pt}{}",
        r"\begin{document}",
        r"\begin{center}\LARGE Public-Domain Study Bible Prototype\end{center}",
        r"\bigskip",
        r"\noindent\textbf{Data diagnostics:}",
        r"\begin{verbatim}",
        json.dumps(diagnostics, indent=2, ensure_ascii=False),
        r"\end{verbatim}",
    ]
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
            elif line.startswith("- "):
                lines.append(r"\noindent " + latex_escape(line[2:]) + r"\par")
            else:
                lines.append(r"\noindent " + latex_escape(line) + r"\par")
    current_book = None
    current_chapter = None
    paragraph_bits: List[str] = []
    paragraph_notes: List[str] = []

    def flush():
        nonlocal paragraph_bits, paragraph_notes
        if paragraph_bits:
            lines.append(r"\noindent " + " ".join(paragraph_bits) + r"\par")
        if paragraph_notes:
            lines.append(r"\begin{quote}\footnotesize")
            for note in paragraph_notes:
                lines.append(latex_escape(note) + r"\par")
            lines.append(r"\end{quote}")
        paragraph_bits = []
        paragraph_notes = []

    for record in records:
        if record.book_name != current_book:
            flush()
            current_book = record.book_name
            current_chapter = None
            lines.append(r"\section*{" + latex_escape(record.book_name) + "}")
        if record.chapter != current_chapter:
            flush()
            current_chapter = record.chapter
            lines.append(r"\subsection*{" + latex_escape(f"{record.book_name} {record.chapter}") + "}")
        if record.paragraph_start:
            flush()
        paragraph_bits.append(r"\textsuperscript{" + str(record.verse) + "} " + latex_escape(record.text))
        for note in record.footnotes:
            paragraph_notes.append(f"{record.ref} Brenton note: {note}")
        for note in record.study_notes:
            paragraph_notes.append(f"{record.ref} {note}")
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
            elif line.startswith("- "):
                lines.append(r"\noindent " + latex_escape(line[2:]) + r"\par")
            else:
                lines.append(r"\noindent " + latex_escape(line) + r"\par")
    lines.append(r"\end{document}")
    return "\n".join(lines)


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    records, diagnostics = merge_records()
    markdown = render_markdown(records, diagnostics)
    md_path = OUTPUT / "study_bible_prototype.md"
    md_path.write_text(markdown, encoding="utf-8")
    json_path = OUTPUT / "build_diagnostics.json"
    json_path.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False), encoding="utf-8")
    tex_path = OUTPUT / "study_bible_prototype.tex"
    tex_path.write_text(render_latex(records, diagnostics), encoding="utf-8")
    pdf_path = render_pdf_excerpt(records, md_path)
    summary = {
        "markdown": str(md_path),
        "diagnostics": str(json_path),
        "latex": str(tex_path),
        "pdf_excerpt": str(pdf_path) if pdf_path else None,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
