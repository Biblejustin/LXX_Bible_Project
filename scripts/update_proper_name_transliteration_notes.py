#!/usr/bin/env python3
"""Build the supplemental proper-name note layer from current Bible text.

This intentionally does not add place names to data/proper_names.csv, because
that file is also used to suppress Logos BibleKnowledgebase place links.
"""

from __future__ import annotations

import csv
import json
import re
import sqlite3
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OT_SOURCE = DATA / "raw" / "lxx_greek" / "ot_full.csv"
NT_SOURCE = DATA / "raw" / "tr_greek" / "nt_full.csv"
PROPER_NAMES = DATA / "proper_names.csv"
NAMES_OF_GOD = DATA / "names_of_god.csv"
UKJV_ZIP = DATA / "raw" / "SF_2009-01-20_ENG_UKJV_(UPDATED KING JAMES VERSION).zip"
HITCHCOCK_NAMES = DATA / "raw" / "hitchcock_bible_names.txt"
OUT_NOTES = DATA / "proper_name_transliteration_notes.csv"
OUT_COVERAGE_CSV = ROOT / "output" / "fresh_proper_name_note_coverage.csv"
OUT_COVERAGE_MD = ROOT / "output" / "fresh_proper_name_note_coverage.md"
OUT_DIAGNOSTICS = ROOT / "output" / "fresh_proper_name_note_coverage_diagnostics.json"

TOKEN_RE = re.compile(r"\b[A-ZĀĒĪŌŪ][A-Za-zĀĒĪŌŪāēīōū'-]+\b")
GREEK_TOKEN_RE = re.compile(r"[\u0370-\u03ff\u1f00-\u1fff\u0300-\u036f]+")
UKJV_NAME_RE = re.compile(r"\b[A-Z][A-Za-z'-]+\b")

NAME_KINDS = {"Man", "Woman", "SupernaturalBeing", "PeopleGroup"}
PLACE_KINDS = {"City", "OtherPlace", "NaturalPlace", "ManMadePlace"}

OT_UKJV_BOOK_MAP = {
    1: ("GEN", "Genesis"),
    2: ("EXO", "Exodus"),
    3: ("LEV", "Leviticus"),
    4: ("NUM", "Numbers"),
    5: ("DEU", "Deuteronomy"),
    6: ("JOS", "Joshua"),
    7: ("JDG", "Judges"),
    8: ("RUT", "Ruth"),
    9: ("1SA", "1 Samuel"),
    10: ("2SA", "2 Samuel"),
    11: ("1KI", "1 Kings"),
    12: ("2KI", "2 Kings"),
    13: ("1CH", "1 Chronicles"),
    14: ("2CH", "2 Chronicles"),
    15: ("EZR", "Ezra"),
    16: ("NEH", "Nehemiah"),
    17: ("EST", "Esther"),
    18: ("JOB", "Job"),
    19: ("PSA", "Psalms"),
    20: ("PRO", "Proverbs"),
    21: ("ECC", "Ecclesiastes"),
    22: ("SNG", "Song of Songs"),
    23: ("ISA", "Isaiah"),
    24: ("JER", "Jeremiah"),
    25: ("LAM", "Lamentations"),
    26: ("EZK", "Ezekiel"),
    27: ("DAN", "Daniel"),
    28: ("HOS", "Hosea"),
    29: ("JOL", "Joel"),
    30: ("AMO", "Amos"),
    31: ("OBA", "Obadiah"),
    32: ("JON", "Jonah"),
    33: ("MIC", "Micah"),
    34: ("NAM", "Nahum"),
    35: ("HAB", "Habakkuk"),
    36: ("ZEP", "Zephaniah"),
    37: ("HAG", "Haggai"),
    38: ("ZEC", "Zechariah"),
    39: ("MAL", "Malachi"),
}

GREEK_ROMANIZATION = {
    "α": "a",
    "β": "b",
    "γ": "g",
    "δ": "d",
    "ε": "e",
    "ζ": "z",
    "η": "e",
    "θ": "th",
    "ι": "i",
    "κ": "k",
    "λ": "l",
    "μ": "m",
    "ν": "n",
    "ξ": "x",
    "ο": "o",
    "π": "p",
    "ρ": "r",
    "σ": "s",
    "ς": "s",
    "τ": "t",
    "υ": "y",
    "φ": "ph",
    "χ": "ch",
    "ψ": "ps",
    "ω": "o",
}

STOPWORDS = {
    "A",
    "Against",
    "Alas",
    "All",
    "Almighty",
    "Also",
    "Amen",
    "An",
    "And",
    "Are",
    "As",
    "Ask",
    "At",
    "Awake",
    "Be",
    "Because",
    "Before",
    "Behold",
    "Better",
    "Bethel",
    "Bless",
    "Blessed",
    "Book",
    "Bring",
    "But",
    "By",
    "Call",
    "Choose",
    "City",
    "Come",
    "Command",
    "Concerning",
    "Cry",
    "Cursed",
    "Daughter",
    "Day",
    "Days",
    "Declare",
    "Deep",
    "Depart",
    "Desire",
    "Did",
    "Do",
    "Does",
    "Draw",
    "Drink",
    "Each",
    "Earth",
    "Eat",
    "Ecclesiastes",
    "Elders",
    "Enter",
    "Even",
    "Every",
    "Everyone",
    "Everything",
    "Evil",
    "Except",
    "False",
    "Far",
    "Father",
    "Fear",
    "Feast",
    "Fool",
    "Foolish",
    "For",
    "From",
    "Gather",
    "Gate",
    "Give",
    "Giving",
    "Glory",
    "Go",
    "God",
    "Good",
    "Great",
    "Guard",
    "Hades",
    "Hallelujah",
    "Has",
    "Have",
    "He",
    "Hear",
    "Heart",
    "Heaven",
    "Her",
    "His",
    "Holy",
    "Hope",
    "House",
    "How",
    "Howl",
    "I",
    "If",
    "In",
    "Incline",
    "Interlude",
    "Into",
    "Is",
    "It",
    "Its",
    "Judge",
    "Just",
    "Keep",
    "King",
    "Know",
    "Lawless",
    "Leave",
    "Lest",
    "Let",
    "Lift",
    "Like",
    "Lord",
    "Lord's",
    "Make",
    "Man",
    "Many",
    "Master",
    "Matters",
    "May",
    "Me",
    "Men",
    "Mighty",
    "Most",
    "Mount",
    "Mountains",
    "My",
    "Nation",
    "Nations",
    "No",
    "Nor",
    "Not",
    "Now",
    "Oath",
    "Of",
    "On",
    "One",
    "Only",
    "Open",
    "Or",
    "Oracle",
    "Our",
    "Out",
    "Over",
    "Ox",
    "Passover",
    "Pay",
    "People",
    "Place",
    "Praise",
    "Pray",
    "Prayer",
    "Prepare",
    "Psalm",
    "Red",
    "Rejoice",
    "Remember",
    "Rescue",
    "Return",
    "Righteous",
    "Righteousness",
    "Rise",
    "River",
    "Run",
    "Sabbath",
    "Sabbaths",
    "Sacrifice",
    "Salt",
    "Sanctify",
    "Save",
    "Say",
    "Sea",
    "Seek",
    "See",
    "Send",
    "Set",
    "Seven",
    "Shall",
    "She",
    "Since",
    "Sing",
    "Sit",
    "Six",
    "So",
    "Son",
    "Song",
    "Sons",
    "Speak",
    "Spirit",
    "Stand",
    "Stay",
    "Still",
    "Straight",
    "Strengthen",
    "Stretch",
    "Strike",
    "Sun",
    "Surely",
    "Sword",
    "Tell",
    "The",
    "Their",
    "Then",
    "There",
    "Therefore",
    "These",
    "They",
    "This",
    "Those",
    "Through",
    "Thus",
    "Time",
    "To",
    "Today",
    "Tomorrow",
    "Toward",
    "Truly",
    "Turn",
    "Two",
    "Ungodly",
    "Until",
    "Upon",
    "Us",
    "Valley",
    "Vision",
    "Voice",
    "Was",
    "Watch",
    "Water",
    "Way",
    "Ways",
    "We",
    "Well",
    "Were",
    "Whatever",
    "When",
    "Whenever",
    "Where",
    "While",
    "Who",
    "Whoever",
    "Whose",
    "Why",
    "Will",
    "Wisdom",
    "Wise",
    "With",
    "Woe",
    "Word",
    "Words",
    "You",
    "Young",
    "Your",
}

MANUAL_TRANSLITERATED_FORMS = {
    "Iou",
    "Ioudaioi",
    "Iosaphat",
    "Beniamin",
    "Galaad",
    "Ioas",
    "Ochozias",
    "Ader",
    "Chiram",
    "Galgala",
    "Gabaa",
    "Iessai",
    "Ionathan",
    "Sarouia",
    "Sychem",
    "Abessa",
    "Abia",
    "Bersabee",
    "Kaath",
    "Baasa",
    "Azarias",
    "Orna",
    "Rama",
    "Iodae",
    "Michaias",
    "Sisara",
    "Manasse",
    "Adraazar",
    "Anchous",
    "Achitophel",
    "Adonias",
    "Gedoliah",
    "Kis",
    "Moyses",
    "Assour",
    "Nabouthai",
    "Chebron",
    "Iabis",
    "Ioachas",
    "Ioram",
    "Kadesh",
    "Keila",
    "Melchol",
    "Samaias",
    "Sousa",
    "Amessias",
    "Eliphas",
    "Siba",
    "Achimaas",
    "Ambri",
    "Ana",
    "Arthasastha",
    "Gotholia",
    "Iezabel",
    "Jezrael",
    "Naiman",
    "Thaiman",
    "Thersa",
    "Abigaia",
    "Achia",
    "Adar",
    "Baithsamyis",
    "Giezi",
    "Iesou",
    "Phinees",
    "Sin",
    "Sabaoth",
    "Achaz",
    "Abiud",
    "Aminadab",
    "Booz",
    "Elisabeth",
    "Eliud",
    "Esrom",
    "Ezekias",
    "Gomorrha",
    "Jechonias",
    "Jeremy",
    "Joatham",
    "Josaphat",
    "Josias",
    "Juda",
    "Judaea",
    "Judas",
    "Manasses",
    "Naasson",
    "Noe",
    "Ozias",
    "Phares",
    "Salathiel",
    "Sion",
    "Sodoma",
    "Thamar",
    "Timotheus",
    "Zara",
    "Zorobabel",
}

MANUAL_PEOPLE_GROUP_FORMS = {
    "Levite",
    "Levites",
}

MANUAL_PLACE_FORMS = {
    "Bethleem",
    "Bethlehem",
    "Ephratha",
    "Ephratah",
}

EQUIVALENT_OVERRIDES = {
    "Abessa": "Abishai",
    "Abia": "Abijah",
    "Abigaia": "Abigail",
    "Achia": "Ahijah",
    "Achimaas": "Ahimaaz",
    "Achitophel": "Ahithophel",
    "Adonias": "Adonijah",
    "Adraazar": "Hadadezer",
    "Ader": "Hadad",
    "Akchō": "Acco",
    "Ambri": "Omri",
    "Anchous": "Achish",
    "Arthasastha": "Artaxerxes",
    "Assour": "Asshur",
    "Ausē": "Hoshea",
    "Azarias": "Azariah",
    "Baasa": "Baasha",
    "Baithsamyis": "Beth-shemesh",
    "Beniamin": "Benjamin",
    "Bēbai": "Bebai",
    "Belasōr": "Baal-hazor",
    "Bersabee": "Beersheba",
    "Bethleem": "Bethlehem",
    "Bethlehem": "Bethlehem",
    "Chebron": "Hebron",
    "Chiram": "Hiram",
    "Chōrēb": "Horeb",
    "Chousarsathōm": "Chushan-rishathaim",
    "Dōr": "Dor",
    "Eliphas": "Eliphaz",
    "Ephratha": "Ephrathah",
    "Ephratah": "Ephrathah",
    "Euphratēs": "Euphrates",
    "Gabaa": "Gibeah",
    "Galaad": "Gilead",
    "Galaaditēs": "Gileadites",
    "Galgala": "Gilgal",
    "Gedoliah": "Gedaliah",
    "Giezi": "Gehazi",
    "Gotholia": "Athaliah",
    "Gothoniēl": "Othniel",
    "Iabis": "Jabesh",
    "Iazēr": "Jazer",
    "Iessai": "Jesse",
    "Iezabel": "Jezebel",
    "Iōchabēd": "Ichabod",
    "Ioachas": "Jehoahaz",
    "Ioas": "Joash",
    "Iodae": "Jehoiada",
    "Ionathan": "Jonathan",
    "Iosaphat": "Jehoshaphat",
    "Iou": "Jehu",
    "Ioudaioi": "Jews",
    "Jephonnē": "Jephunneh",
    "Kaath": "Kohath",
    "Kerōe": "Iron",
    "Kis": "Kish",
    "Manasse": "Manasseh",
    "Melchol": "Michal",
    "Moyses": "Moses",
    "Nabouthai": "Naboth",
    "Naiman": "Naaman",
    "Nauē": "Nun",
    "Ochozias": "Ahaziah",
    "Orna": "Araunah",
    "Phadaēl": "Pedahel",
    "Phaltiēl": "Paltiel",
    "Phinees": "Phinehas",
    "Rama": "Ramah",
    "Sabaoth": "LORD of hosts",
    "Sabaōth": "LORD of hosts",
    "Salamiēl": "Shammua",
    "Samaias": "Shemaiah",
    "Sarouia": "Zeruiah",
    "Siba": "Ziba",
    "Sisara": "Sisera",
    "Sychem": "Shechem",
    "Thaiman": "Teman",
    "Thersa": "Tirzah",
    "Achaz": "Ahaz",
    "Abiud": "Abiud",
    "Aminadab": "Amminadab",
    "Booz": "Boaz",
    "Elisabeth": "Elizabeth",
    "Eliud": "Eliud",
    "Esrom": "Hezron",
    "Ezekias": "Hezekiah",
    "Gomorrha": "Gomorrah",
    "Jechonias": "Jeconiah",
    "Jeremy": "Jeremiah",
    "Joatham": "Jotham",
    "Josaphat": "Jehoshaphat",
    "Josias": "Josiah",
    "Juda": "Judah",
    "Judaea": "Judea",
    "Judas": "Judas",
    "Manasses": "Manasseh",
    "Naasson": "Nahshon",
    "Noe": "Noah",
    "Ozias": "Uzziah",
    "Phares": "Perez",
    "Salathiel": "Shealtiel",
    "Sion": "Zion",
    "Sodoma": "Sodom",
    "Thamar": "Tamar",
    "Timotheus": "Timothy",
    "Zara": "Zerah",
    "Zorobabel": "Zerubbabel",
}

EQUIVALENT_MEANING_OVERRIDES = {
    "Baal-hazor": "Baal's village; lord of the enclosure",
    "Beth-shemesh": "house of the sun",
    "Iron": "watchful; city-name meaning uncertain",
    "Jezreel": "God sows",
    "LORD of hosts": "Yahweh of armies; Lord of heavenly hosts",
    "Pedahel": "God has redeemed",
    "Jews": "People of Judah; Judeans",
    "Judea": "land of Judah",
}

CONTEXTUAL_FOOTNOTE_OVERRIDES = {
    "Juda": (
        "UKJV form: Juda. Standard English equivalent: Judah in land, tribe, and genealogy contexts; "
        "Mark 6:3 uses the same Greek form for Jesus' brother, normally rendered Judas or Jude. "
        "Source form: {source_form}.{greek_piece} Name meaning: {meaning}. Equivalent source: UKJV form plus manual context review."
    ),
    "Judas": (
        "UKJV form: Judas. Judas is the standard English form for the NT personal name; "
        "Matthew 1:2-3 uses the same Greek name-family in Judah's genealogy. "
        "Source form: {source_form}.{greek_piece} Name meaning: {meaning}. Equivalent source: UKJV form plus manual context review."
    ),
}

UKJV_EQUIVALENT_OVERRIDES = {
    "Bethshemesh": "Beth-shemesh",
    "Kadeshbarnea": "Kadesh-Barnea",
    "MeribahKadesh": "Meribah-kadesh",
    "Sichem": "Shechem",
}

MEANING_NAME_ALIASES = {
    "Acco": "Accho",
    "Aijalon": "Ajalon",
    "Beth-shemesh": "Bethshemesh",
    "Bethlehemite": "Bethlehem",
    "Ephrathah": "Ephratah",
    "Gileadites": "Gilead",
    "Hoshea": "Hosea",
    "Ichabod's": "Ichabod",
    "Joktheel": "Joktheel",
    "Jezreel": "Jezreel",
    "Paltiel": "Paltiel",
    "Pedahel": "Pedahel",
    "Phaltiel": "Paltiel",
    "Pirathonite": "Pirathon",
    "Shammua": "Shammuah",
    "Ahaz": "Achaz",
    "Amminadab": "Aminadab",
    "Boaz": "Booz",
    "Elizabeth": "Elisabeth",
    "Hezron": "Esrom",
    "Jeconiah": "Jechonias",
    "Jotham": "Joatham",
    "Judea": "Judaea",
    "Nahshon": "Naasson",
    "Perez": "Phares",
    "Shealtiel": "Salathiel",
    "Tamar": "Thamar",
    "Timothy": "Timotheus",
    "Uzziah": "Ozias",
    "Zerah": "Zara",
    "Zerubbabel": "Zorobabel",
}

UKJV_NAME_STOPWORDS = STOPWORDS | {
    "Ah",
    "Carry",
    "Come",
    "Current",
    "Is",
    "Should",
    "Thus",
    "Unto",
}


@dataclass(frozen=True)
class EquivalentInfo:
    equivalent: str
    meaning: str
    greek_form: str
    source_form: str
    witness: str
    confidence: str


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def normalize_token(token: str) -> str:
    if token.endswith("'s"):
        return token[:-2]
    return token


def normalize_lookup(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    stripped = stripped.replace("’", "'").replace("`", "'")
    return re.sub(r"[^a-z0-9]+", "", stripped.lower())


def lookup_variants(value: str) -> set[str]:
    variants = {normalize_lookup(value)}
    for _ in range(2):
        for variant in list(variants):
            if "j" in variant:
                variants.add(variant.replace("j", "i"))
            if "y" in variant:
                variants.add(variant.replace("y", "u"))
            if "ae" in variant:
                variants.add(variant.replace("ae", "ai"))
            if "ou" in variant:
                variants.add(variant.replace("ou", "u"))
    return {variant for variant in variants if variant}


def display_name(value: str) -> str:
    return re.sub(r"\s+\([^)]*\)$", "", value).strip()


def romanize_greek_token(token: str) -> str:
    normalized = unicodedata.normalize("NFD", token.lower())
    pieces: list[str] = []
    for char in normalized:
        if unicodedata.combining(char):
            continue
        pieces.append(GREEK_ROMANIZATION.get(char, char))
    return "".join(pieces)


def lookup_match_score(left: set[str], right: set[str]) -> float:
    best = 0.0
    for left_value in left:
        for right_value in right:
            score = SequenceMatcher(None, left_value, right_value).ratio()
            if left_value and right_value and left_value[0] == right_value[0]:
                score += 0.08
            if len(left_value) >= 4 and len(right_value) >= 4 and (left_value in right_value or right_value in left_value):
                score += 0.12
            best = max(best, score)
    return best


def parse_hitchcock_meanings(path: Path = HITCHCOCK_NAMES) -> dict[str, str]:
    if not path.exists():
        return {}
    meanings: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or "," not in line:
            continue
        name, meaning = line.split(",", 1)
        if not name or not meaning:
            continue
        key = normalize_lookup(name)
        if key and key not in meanings:
            meanings[key] = meaning.strip().rstrip(".")
    return meanings


def load_curated_meanings() -> dict[str, str]:
    meanings: dict[str, str] = {}
    for row in load_csv(PROPER_NAMES):
        name = row.get("name", "").strip()
        meaning = row.get("meaning", "").strip()
        if name and meaning:
            meanings[normalize_lookup(name)] = meaning
    return meanings


def meaning_for_name(name: str, curated: dict[str, str], hitchcock: dict[str, str]) -> str:
    base = display_name(name).rstrip("'s")
    override = EQUIVALENT_MEANING_OVERRIDES.get(name) or EQUIVALENT_MEANING_OVERRIDES.get(base)
    if override:
        return override
    candidates = [name, base, base.replace("-", ""), base.replace("-", " ")]
    alias = MEANING_NAME_ALIASES.get(base)
    if alias:
        candidates.append(alias)
    if base.endswith("ites") and len(base) > 5:
        candidates.append(base[:-4])
    if base.endswith("ite") and len(base) > 4:
        candidates.append(base[:-3])
    if base.endswith("ians") and len(base) > 5:
        candidates.append(base[:-4])
    if base.endswith("s") and len(base) > 3:
        candidates.append(base[:-1])
    for candidate in candidates:
        key = normalize_lookup(candidate)
        if key in curated:
            return curated[key]
        if key in hitchcock:
            return hitchcock[key]
    return "meaning uncertain/not securely attested in the consulted name dictionaries"


def parse_ukjv_ot(path: Path = UKJV_ZIP) -> dict[str, str]:
    if not path.exists():
        return {}
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read(zf.namelist()[0]))
    verses: dict[str, str] = {}
    for book in root.findall("BIBLEBOOK"):
        try:
            bnumber = int(book.attrib["bnumber"])
        except (KeyError, ValueError):
            continue
        mapped = OT_UKJV_BOOK_MAP.get(bnumber)
        if not mapped:
            continue
        _, book_name = mapped
        for chapter in book.findall("CHAPTER"):
            try:
                chapter_num = int(chapter.attrib["cnumber"])
            except (KeyError, ValueError):
                continue
            for verse in chapter.findall("VERS"):
                try:
                    verse_num = int(verse.attrib["vnumber"])
                except (KeyError, ValueError):
                    continue
                pieces: list[str] = []
                if verse.text:
                    pieces.append(verse.text)
                for child in verse:
                    if child.text:
                        pieces.append(child.text)
                    if child.tail:
                        pieces.append(child.tail)
                text = re.sub(r"\s+", " ", "".join(pieces)).strip()
                verses[f"{book_name} {chapter_num}:{verse_num}"] = text
    return verses


def load_logos_alias_primary() -> dict[str, set[str]]:
    db_path = choose_logos_autocomplete_db()
    if not db_path:
        return {}
    query = """
    SELECT l.LabelText, t.Reference, l.IsPrimary
    FROM Labels l
    JOIN Terms t ON t.TermId = l.TermId
    WHERE l.LanguageId = 1
      AND (t.Reference LIKE 'bk.#%' OR t.Reference LIKE 'bk.@%')
    """
    with sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True) as conn:
        rows = conn.execute(query).fetchall()
    labels_by_ref: dict[str, list[str]] = defaultdict(list)
    primary_by_ref: dict[str, list[str]] = defaultdict(list)
    for label, reference, is_primary in rows:
        labels_by_ref[reference].append(label)
        if is_primary:
            primary_by_ref[reference].append(label)
    alias_primary: dict[str, set[str]] = defaultdict(set)
    for reference, labels in labels_by_ref.items():
        primary_labels = primary_by_ref.get(reference)
        if not primary_labels:
            continue
        primary = min((display_name(label) for label in primary_labels), key=len)
        for label in labels:
            alias_primary[label].add(primary)
    return dict(alias_primary)


def ukjv_name_candidates(text: str) -> list[str]:
    candidates: list[str] = []
    for token in UKJV_NAME_RE.findall(text.replace("LORD", "Lord")):
        if token in UKJV_NAME_STOPWORDS:
            continue
        if token not in candidates:
            candidates.append(token)
    return candidates


def draft_name_candidates(text: str) -> list[str]:
    candidates: list[str] = []
    for token in TOKEN_RE.findall(text):
        normalized = normalize_token(token)
        if normalized in UKJV_NAME_STOPWORDS:
            continue
        if normalized not in candidates:
            candidates.append(normalized)
    return candidates


def normalize_equivalent_candidate(candidate: str, alias_primary: dict[str, set[str]]) -> str:
    candidate = display_name(candidate.rstrip("'s"))
    return UKJV_EQUIVALENT_OVERRIDES.get(candidate, candidate)


def find_greek_form(source_form: str, source_row: dict[str, str] | None) -> str:
    if not source_row:
        return ""
    best_score = 0.0
    best = ""
    targets = lookup_variants(source_form)
    for token in GREEK_TOKEN_RE.findall(source_row.get("greek_text", "")):
        greek_variants = lookup_variants(romanize_greek_token(token))
        score = lookup_match_score(targets, greek_variants)
        if score > best_score:
            best_score = score
            best = token
    return best if best_score >= 0.48 else ""


def resolve_equivalent(
    token: str,
    refs: list[str],
    *,
    source_rows_by_ref: dict[str, dict[str, str]],
    ukjv_by_ref: dict[str, str],
    alias_primary: dict[str, set[str]],
    curated_meanings: dict[str, str],
    hitchcock_meanings: dict[str, str],
) -> EquivalentInfo:
    source_form = token
    first_row = source_rows_by_ref.get(refs[0]) if refs else None
    greek_form = find_greek_form(token, first_row)
    override = EQUIVALENT_OVERRIDES.get(token)
    if override:
        return EquivalentInfo(
            equivalent=override,
            meaning=meaning_for_name(override, curated_meanings, hitchcock_meanings),
            greek_form=greek_form,
            source_form=source_form,
            witness="manual/standard English equivalent",
            confidence="manual",
        )

    for ref in refs:
        source_row = source_rows_by_ref.get(ref)
        if not source_row:
            continue
        draft_names = draft_name_candidates(source_row.get("draft_translation", ""))
        ukjv_names = ukjv_name_candidates(ukjv_by_ref.get(ref, ""))
        if token in draft_names and len(draft_names) == len(ukjv_names):
            equivalent = normalize_equivalent_candidate(ukjv_names[draft_names.index(token)], alias_primary)
            score = SequenceMatcher(None, normalize_lookup(token), normalize_lookup(equivalent)).ratio()
            if equivalent and score >= 0.50:
                return EquivalentInfo(
                    equivalent=equivalent,
                    meaning=meaning_for_name(equivalent, curated_meanings, hitchcock_meanings),
                    greek_form=greek_form,
                    source_form=source_form,
                    witness="UKJV same-reference name-order alignment",
                    confidence="aligned",
                )

    scored: list[tuple[float, str, str]] = []
    target = normalize_lookup(token)
    for ref in refs:
        for candidate in ukjv_name_candidates(ukjv_by_ref.get(ref, "")):
            primary_options = alias_primary.get(candidate, set())
            names = {candidate, *(display_name(option) for option in primary_options)}
            for name in names:
                score = SequenceMatcher(None, target, normalize_lookup(name)).ratio()
                scored.append((score, candidate, name))
    if scored:
        score, candidate, equivalent = max(scored, key=lambda item: item[0])
        if score >= 0.54:
            equivalent = normalize_equivalent_candidate(equivalent or candidate, alias_primary)
            return EquivalentInfo(
                equivalent=equivalent,
                meaning=meaning_for_name(equivalent, curated_meanings, hitchcock_meanings),
                greek_form=greek_form,
                source_form=source_form,
                witness="UKJV same-reference witness",
                confidence=f"{score:.2f}",
            )

    primary_options = alias_primary.get(token, set())
    if primary_options:
        equivalent = display_name(min(primary_options, key=len))
        return EquivalentInfo(
            equivalent=equivalent,
            meaning=meaning_for_name(equivalent, curated_meanings, hitchcock_meanings),
            greek_form=greek_form,
            source_form=source_form,
            witness="Logos Bible Knowledgebase alias",
            confidence="alias",
        )

    equivalent = token.replace("ē", "e").replace("ō", "o").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    return EquivalentInfo(
        equivalent=equivalent,
        meaning=meaning_for_name(equivalent, curated_meanings, hitchcock_meanings),
        greek_form=greek_form,
        source_form=source_form,
        witness="normalized source form",
        confidence="fallback",
    )


def existing_note_labels() -> set[str]:
    labels = {row["name"].strip() for row in load_csv(PROPER_NAMES) if row.get("name", "").strip()}
    for row in load_csv(NAMES_OF_GOD):
        for key in ("transliteration", "english_renderings"):
            value = row.get(key, "")
            for part in re.split(r"[;,]", value):
                part = part.strip()
                if part:
                    labels.add(part)
    return labels


def choose_logos_autocomplete_db() -> Path | None:
    data_root = Path.home() / "Library" / "Application Support" / "Logos4" / "Data"
    if not data_root.exists():
        return None
    candidates = sorted(data_root.glob("*/AutoComplete/AutoComplete.db"))
    if not candidates:
        return None
    return max(candidates, key=lambda path: path.stat().st_size)


def load_logos_entity_kinds() -> tuple[dict[str, set[str]], dict[str, set[str]], str | None]:
    db_path = choose_logos_autocomplete_db()
    if not db_path:
        return {}, {}, None
    primary: dict[str, set[str]] = defaultdict(set)
    any_label: dict[str, set[str]] = defaultdict(set)
    query = """
    SELECT l.LabelText, t.Reference, ik.IconKind, l.IsPrimary
    FROM Labels l
    JOIN Terms t ON t.TermId = l.TermId
    JOIN IconKinds ik ON ik.IconKindId = t.IconKindId
    WHERE l.LanguageId = 1
    """
    with sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True) as conn:
        rows = conn.execute(query).fetchall()
    for label, reference, icon_kind, is_primary in rows:
        if icon_kind in NAME_KINDS and reference.startswith("bk.#"):
            any_label[label].add(icon_kind)
            if is_primary:
                primary[label].add(icon_kind)
        elif icon_kind in PLACE_KINDS and reference.startswith("bk.@"):
            any_label[label].add(icon_kind)
            if is_primary:
                primary[label].add(icon_kind)
    return dict(primary), dict(any_label), str(db_path)


def gather_tokens() -> tuple[dict[str, dict[str, object]], dict[str, int]]:
    tokens: dict[str, dict[str, object]] = {}
    source_counts = Counter()
    order = 0
    for source_name, path in (("ot", OT_SOURCE), ("nt", NT_SOURCE)):
        if not path.exists():
            continue
        source_counts[f"{source_name}_rows"] = 0
        for row in load_csv(path):
            source_counts[f"{source_name}_rows"] += 1
            text = row.get("draft_translation", "")
            ref = row.get("ref", "")
            for match in TOKEN_RE.finditer(text):
                order += 1
                token = normalize_token(match.group(0))
                entry_key = f"{source_name}:{token}"
                entry = tokens.setdefault(
                    entry_key,
                    {
                        "name": token,
                        "occurrences": 0,
                        "first_reference": ref,
                        "source": source_name,
                        "first_order": order,
                        "sample_refs": [],
                        "refs": [],
                    },
                )
                entry["occurrences"] = int(entry["occurrences"]) + 1
                samples = entry["sample_refs"]
                if isinstance(samples, list) and ref not in samples and len(samples) < 8:
                    samples.append(ref)
                refs = entry["refs"]
                if isinstance(refs, list) and ref not in refs:
                    refs.append(ref)
    return tokens, dict(source_counts)


def note_kind_for_entity(kinds: set[str]) -> str:
    if "SupernaturalBeing" in kinds:
        return "supernatural_being"
    if "Man" in kinds or "Woman" in kinds:
        return "person"
    if "PeopleGroup" in kinds:
        return "people_group"
    return "transliterated_form"


def classify_token(
    token: str,
    *,
    primary_kinds: dict[str, set[str]],
    any_kinds: dict[str, set[str]],
) -> tuple[str | None, str]:
    if token in MANUAL_PEOPLE_GROUP_FORMS:
        return "people_group", "manual_high_frequency_people_group"
    if token in MANUAL_PLACE_FORMS:
        return "place", "manual_place_atlas_link_preserved"
    if token in MANUAL_TRANSLITERATED_FORMS:
        return "transliterated_form", "manual_high_frequency_source_form"
    primary = primary_kinds.get(token, set())
    any_match = any_kinds.get(token, set())
    primary_name = primary & NAME_KINDS
    primary_place = primary & PLACE_KINDS
    any_name = any_match & NAME_KINDS
    any_place = any_match & PLACE_KINDS
    if primary_place and not primary_name:
        return "place", "logos_primary_place_atlas_link_preserved"
    if primary_name:
        return note_kind_for_entity(primary_name), "logos_primary_entity"
    if any_place and not any_name:
        return "place", "logos_alias_place_atlas_link_preserved"
    if any_name and not any_place:
        return note_kind_for_entity(any_name), "logos_alias_entity"
    if any(ch in token for ch in "ĀĒĪŌŪāēīōū"):
        return "transliterated_form", "macronized_source_form"
    return None, "not_classified"


def footnote_for(kind: str, reason: str, equivalent: EquivalentInfo | None = None) -> str:
    if kind == "person":
        return "Source text carries this as a personal name; retained as a proper noun rather than translated as ordinary vocabulary."
    if kind == "people_group":
        return "Ethnic or group proper noun; retained as a people-name rather than translated as ordinary vocabulary."
    if kind == "supernatural_being":
        return "Source text carries this as a divine or supernatural name/title; retained as a proper noun."
    if kind == "place" and equivalent:
        greek_piece = f" Greek form: {equivalent.greek_form}." if equivalent.greek_form else ""
        equivalent_piece = (
            f" Standard English equivalent: {equivalent.equivalent}."
            if equivalent.equivalent != equivalent.source_form
            else ""
        )
        return (
            f"Place-name meaning: {equivalent.equivalent} — {equivalent.meaning}."
            f"{equivalent_piece} Source form: {equivalent.source_form}."
            f"{greek_piece} Equivalent source: {equivalent.witness}."
        )
    if equivalent:
        greek_piece = f" Greek form: {equivalent.greek_form}." if equivalent.greek_form else ""
        contextual_template = CONTEXTUAL_FOOTNOTE_OVERRIDES.get(equivalent.source_form)
        if contextual_template:
            return contextual_template.format(
                source_form=equivalent.source_form,
                greek_piece=greek_piece,
                meaning=equivalent.meaning,
            )
        return (
            f"Standard English equivalent: {equivalent.equivalent}. "
            f"Source form: {equivalent.source_form}."
            f"{greek_piece} "
            f"Name meaning: {equivalent.meaning}. "
            f"Equivalent source: {equivalent.witness}."
        )
    return "Transliterated source-form proper noun; standard equivalent review needed."


def main() -> None:
    existing_labels = existing_note_labels()
    primary_kinds, any_kinds, logos_db = load_logos_entity_kinds()
    alias_primary = load_logos_alias_primary()
    ukjv_by_ref = parse_ukjv_ot()
    for row in load_csv(NT_SOURCE):
        ref = row.get("ref", "")
        translation = row.get("ukjv_translation", "")
        if ref and translation:
            ukjv_by_ref[ref] = translation
    curated_meanings = load_curated_meanings()
    hitchcock_meanings = parse_hitchcock_meanings()
    tokens, source_counts = gather_tokens()
    source_rows_by_ref = {
        row.get("ref", ""): row
        for source_path in (OT_SOURCE, NT_SOURCE)
        for row in load_csv(source_path)
    }

    note_rows: list[dict[str, str]] = []
    coverage_rows: list[dict[str, str]] = []
    counts = Counter()

    for _, data in sorted(tokens.items(), key=lambda item: (int(item[1]["first_order"]), item[0])):
        token = str(data["name"])
        if token in STOPWORDS or token in existing_labels:
            counts["skipped_existing_or_stopword"] += 1
            continue
        kind, reason = classify_token(token, primary_kinds=primary_kinds, any_kinds=any_kinds)
        if not kind:
            counts[f"skipped_{reason}"] += 1
            continue
        equivalent = None
        if kind in {"place", "transliterated_form"}:
            refs = data.get("refs", [])
            equivalent = resolve_equivalent(
                token,
                refs if isinstance(refs, list) else [str(data["first_reference"])],
                source_rows_by_ref=source_rows_by_ref,
                ukjv_by_ref=ukjv_by_ref,
                alias_primary=alias_primary,
                curated_meanings=curated_meanings,
                hitchcock_meanings=hitchcock_meanings,
            )
            counts[f"equivalent_{equivalent.confidence.split('.')[0]}"] += 1
        row = {
            "name": token,
            "kind": kind,
            "first_reference": str(data["first_reference"]),
            "source": str(data["source"]),
            "english_equivalent": equivalent.equivalent if equivalent else "",
            "source_form": equivalent.source_form if equivalent else "",
            "greek_form": equivalent.greek_form if equivalent else "",
            "name_meaning": equivalent.meaning if equivalent else "",
            "equivalent_source": equivalent.witness if equivalent else "",
            "equivalent_confidence": equivalent.confidence if equivalent else "",
            "footnote": footnote_for(kind, reason, equivalent),
        }
        note_rows.append(row)
        coverage_rows.append(
            {
                **row,
                "occurrences": str(data["occurrences"]),
                "sample_refs": "; ".join(data["sample_refs"]),
                "reason": reason,
            }
        )
        counts[f"included_{kind}"] += 1

    fieldnames = ["name", "kind", "first_reference", "source", "footnote"]
    fieldnames = [
        "name",
        "kind",
        "first_reference",
        "source",
        "english_equivalent",
        "source_form",
        "greek_form",
        "name_meaning",
        "equivalent_source",
        "equivalent_confidence",
        "footnote",
    ]
    write_csv(OUT_NOTES, note_rows, fieldnames)
    write_csv(OUT_COVERAGE_CSV, coverage_rows, [*fieldnames, "occurrences", "sample_refs", "reason"])

    top_rows = sorted(coverage_rows, key=lambda row: (-int(row["occurrences"]), row["name"]))[:80]
    lines = [
        "# Proper Name Note Coverage",
        "",
        f"- supplemental note rows: `{len(note_rows)}`",
        f"- Logos autocomplete DB: `{logos_db or '[not found]'}`",
        "",
        "Policy:",
        "- existing meaning rows remain in `data/proper_names.csv`",
        "- place names stay out of `data/proper_names.csv`; supplemental place notes preserve Logos atlas/place links",
        "- transliterated-form rows now carry standard English equivalents, source/Greek form, and name meaning",
        "- this file covers remaining people names, people-group names, supernatural names, and source-text transliterated forms",
        "",
        "## Included Top Rows",
        "",
    ]
    for row in top_rows:
        lines.append(
            f"- `{row['name']}` ({row['kind']}, {row['occurrences']}x, first {row['first_reference']}) — {row['reason']}"
        )
    OUT_COVERAGE_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    diagnostics = {
        "notes": str(OUT_NOTES),
        "coverage_csv": str(OUT_COVERAGE_CSV),
        "coverage_md": str(OUT_COVERAGE_MD),
        "logos_db": logos_db,
        "ukjv_witness_rows": len(ukjv_by_ref),
        "hitchcock_meaning_rows": len(hitchcock_meanings),
        "note_rows": len(note_rows),
        "source_counts": source_counts,
        "counts": dict(counts),
        "top_rows": top_rows[:20],
    }
    OUT_DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2))


if __name__ == "__main__":
    main()
