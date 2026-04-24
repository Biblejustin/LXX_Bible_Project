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
    "Children",
    "East",
    "Helper",
    "Passover",
    "Pay",
    "People",
    "Place",
    "Praise",
    "Pray",
    "Prayer",
    "Put",
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
    "Iosedek",
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
    "Adrazar",
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
    "Josedek",
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

MANUAL_CONTEXTUAL_TRANSLITERATED_NOTE_ROWS = [
    {
        "name": "Adraazar",
        "kind": "transliterated_form",
        "first_reference": "2 Samuel 8:3",
        "source": "ot",
        "english_equivalent": "Hadadezer",
        "source_form": "Adraazar",
        "greek_form": "αδρααζαρ",
        "name_meaning": "beauty of assistance",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Standard English equivalent: Hadadezer. Source form: Adraazar. Greek form: αδρααζαρ. Name meaning: beauty of assistance. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Adraazar",
        "kind": "transliterated_form",
        "first_reference": "2 Samuel 10:16",
        "source": "ot",
        "english_equivalent": "Hadarezer",
        "source_form": "Adraazar",
        "greek_form": "αδρααζαρ",
        "name_meaning": "beauty of assistance",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Standard English equivalent: Hadarezer. Source form: Adraazar. Greek form: αδρααζαρ. Name meaning: beauty of assistance. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Adrazar",
        "kind": "transliterated_form",
        "first_reference": "1 Kings 11:14",
        "source": "ot",
        "english_equivalent": "Hadadezer",
        "source_form": "Adrazar",
        "greek_form": "αδραζαρ",
        "name_meaning": "beauty of assistance",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Standard English equivalent: Hadadezer. Source form: Adrazar. Greek form: αδραζαρ. Name meaning: beauty of assistance. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Raab",
        "kind": "transliterated_form",
        "first_reference": "Joshua 19:28",
        "source": "ot",
        "english_equivalent": "Rehob",
        "source_form": "Raab",
        "greek_form": "ρααβ",
        "name_meaning": "breadth; space; extent",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Standard English equivalent: Rehob. Source form: Raab. Greek form: ρααβ. Name meaning: breadth; space; extent. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Raab",
        "kind": "transliterated_form",
        "first_reference": "Joshua 21:31",
        "source": "ot",
        "english_equivalent": "Rehob",
        "source_form": "Raab",
        "greek_form": "ρααβ",
        "name_meaning": "breadth; space; extent",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Standard English equivalent: Rehob. Source form: Raab. Greek form: ρααβ. Name meaning: breadth; space; extent. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Raab",
        "kind": "transliterated_form",
        "first_reference": "2 Samuel 8:3",
        "source": "ot",
        "english_equivalent": "Rehob",
        "source_form": "Raab",
        "greek_form": "ρααβ",
        "name_meaning": "breadth; space; extent",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Standard English equivalent: Rehob. Source form: Raab. Greek form: ρααβ. Name meaning: breadth; space; extent. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Souba",
        "kind": "place",
        "first_reference": "2 Samuel 8:3",
        "source": "ot",
        "english_equivalent": "Zobah",
        "source_form": "Souba",
        "greek_form": "σουβα",
        "name_meaning": "an army; warring",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Place-name meaning: Zobah — an army; warring. Standard English equivalent: Zobah. Source form: Souba. Greek form: σουβα. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Souba",
        "kind": "place",
        "first_reference": "2 Samuel 10:8",
        "source": "ot",
        "english_equivalent": "Zobah",
        "source_form": "Souba",
        "greek_form": "σουβα",
        "name_meaning": "an army; warring",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Place-name meaning: Zobah — an army; warring. Standard English equivalent: Zobah. Source form: Souba. Greek form: σουβα. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Souba",
        "kind": "place",
        "first_reference": "1 Kings 11:14",
        "source": "ot",
        "english_equivalent": "Zobah",
        "source_form": "Souba",
        "greek_form": "σουβα",
        "name_meaning": "an army; warring",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Place-name meaning: Zobah — an army; warring. Standard English equivalent: Zobah. Source form: Souba. Greek form: σουβα. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Souba",
        "kind": "place",
        "first_reference": "1 Kings 14:26",
        "source": "ot",
        "english_equivalent": "Zobah",
        "source_form": "Souba",
        "greek_form": "σουβα",
        "name_meaning": "an army; warring",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Place-name meaning: Zobah — an army; warring. Standard English equivalent: Zobah. Source form: Souba. Greek form: σουβα. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Souba",
        "kind": "place",
        "first_reference": "1 Chronicles 18:3",
        "source": "ot",
        "english_equivalent": "Zobah",
        "source_form": "Souba",
        "greek_form": "σουβα",
        "name_meaning": "an army; warring",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Place-name meaning: Zobah — an army; warring. Standard English equivalent: Zobah. Source form: Souba. Greek form: σουβα. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Souba",
        "kind": "place",
        "first_reference": "1 Chronicles 19:6",
        "source": "ot",
        "english_equivalent": "Zobah",
        "source_form": "Souba",
        "greek_form": "σουβα",
        "name_meaning": "an army; warring",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Place-name meaning: Zobah — an army; warring. Standard English equivalent: Zobah. Source form: Souba. Greek form: σουβα. Equivalent source: manual/standard English equivalent.",
    },
    {
        "name": "Soba",
        "kind": "place",
        "first_reference": "Psalms 59:2",
        "source": "ot",
        "english_equivalent": "Zobah",
        "source_form": "Soba",
        "greek_form": "σωβα",
        "name_meaning": "an army; warring",
        "equivalent_source": "manual/standard English equivalent",
        "equivalent_confidence": "manual",
        "footnote": "Place-name meaning: Zobah — an army; warring. Standard English equivalent: Zobah. Source form: Soba. Greek form: σωβα. Equivalent source: manual/standard English equivalent.",
    },
]

MANUAL_CONTEXTUAL_TRANSLITERATED_NOTE_SPECS = [
    ("Souba", "1 Kings 2:46", "ot", "Shisha"),
    ("Saba", "1 Kings 4:3", "ot", "Shisha"),
    ("Amman", "2 Samuel 2:24", "ot", "Ammah"),
    ("Amman", "2 Chronicles 36:5", "ot", "Ammon"),
    ("Abiesdri", "Daniel 1:11", "ot", "Melzar"),
    ("Bakcha", "1 Kings 4:12", "ot", "Baana"),
    ("Gaddi", "1 Chronicles 5:26", "ot", "Gadites"),
    ("Kades", "Joshua 19:37", "ot", "Kedesh"),
    ("Deblatha", "Ezekiel 6:14", "ot", "Diblath"),
    ("Thaimanites", "Job 6:19", "ot", "Tema"),
    ("Sabeans", "Job 6:19", "ot", "Sheba"),
    ("Aggai", "Isaiah 10:28", "ot", "Aiath"),
    ("Bathouel", "Joel 1:1", "ot", "Pethuel"),
    ("Deblathaim", "Numbers 33:46", "ot", "Almon-diblathaim"),
    ("Chetti", "2 Samuel 15:18", "ot", "Cherethites"),
    ("Ebelmaola", "1 Kings 4:12", "ot", "Abelmeholah"),
    ("Eliadae", "1 Kings 11:14", "ot", "Eliada"),
    ("Gaithan", "1 Kings 5:11", "ot", "Ethan"),
    ("Ioach", "1 Chronicles 6:6", "ot", "Joab"),
    ("Iethri", "1 Chronicles 6:6", "ot", "Jethri"),
    ("Iethrite", "1 Chronicles 11:40", "ot", "Ithrite"),
    ("Ioasar", "1 Chronicles 2:18", "ot", "Jesher"),
    ("Iothor", "1 Chronicles 2:17", "ot", "Jether"),
    ("Raōm", "1 Chronicles 7:12", "ot", "Ir"),
    ("Iesias", "1 Chronicles 24:21", "ot", "Isshiah"),
    ("Iesias", "Ezra 8:7", "ot", "Jeshaiah"),
    ("Mekedo", "1 Kings 4:12", "ot", "Megiddo"),
    ("Rhodians", "Ezekiel 27:15", "ot", "Dedan"),
    ("Raemmath", "1 Kings 11:14", "ot", "Ramah"),
    ("Souri", "1 Chronicles 25:3", "ot", "Zeri"),
    ("Mardochaios", "Ezra 2:2", "ot", "Mordecai"),
    ("Jephthae", "Judges 11:1", "ot", "Jephthah"),
    ("Mephibosthe", "2 Samuel 3:7", "ot", "Ishbosheth"),
    ("Mephibosthe", "2 Samuel 4:4", "ot", "Mephibosheth"),
    ("Ourias", "2 Samuel 11:3", "ot", "Uriah"),
    ("Ourias", "2 Kings 16:10", "ot", "Urijah"),
    ("Ornia", "1 Kings 4:5", "ot", "Azariah"),
    ("Iarim", "1 Chronicles 13:5", "ot", "Kirjathjearim"),
    ("Sior", "2 Kings 8:21", "ot", "Zair"),
    ("Idouia", "1 Chronicles 4:19", "ot", "Hodiah"),
    ("Nachem", "1 Chronicles 4:19", "ot", "Naham"),
    ("Esthemoe", "1 Chronicles 4:19", "ot", "Eshtemoa"),
    ("Semeion", "1 Chronicles 4:19", "ot", "Shimon"),
    ("Semeion", "1 Chronicles 4:20", "ot", "Shimon"),
    ("Rana", "1 Chronicles 4:20", "ot", "Rinnah"),
    ("Zoath", "1 Chronicles 4:20", "ot", "Zoheth"),
    ("Micha", "Nehemiah 10:12", "ot", "Micah"),
    ("Roob", "Nehemiah 10:12", "ot", "Rehob"),
    ("Judas", "Matthew 1:2", "nt", "Judah"),
    ("Phares", "Matthew 1:3", "nt", "Perez"),
    ("Zara", "Matthew 1:3", "nt", "Zerah"),
    ("Thamar", "Matthew 1:3", "nt", "Tamar"),
    ("Esrom", "Matthew 1:3", "nt", "Hezron"),
    ("Aminadab", "Matthew 1:4", "nt", "Amminadab"),
    ("Naasson", "Matthew 1:4", "nt", "Nahshon"),
    ("Booz", "Matthew 1:5", "nt", "Boaz"),
    ("Rachab", "Matthew 1:5", "nt", "Rahab"),
    ("Urias", "Matthew 1:6", "nt", "Uriah"),
    ("Roboam", "Matthew 1:7", "nt", "Rehoboam"),
    ("Abia", "Matthew 1:7", "nt", "Abijah"),
    ("Josaphat", "Matthew 1:8", "nt", "Jehoshaphat"),
    ("Ozias", "Matthew 1:8", "nt", "Uzziah"),
    ("Joatham", "Matthew 1:9", "nt", "Jotham"),
    ("Achaz", "Matthew 1:9", "nt", "Ahaz"),
    ("Ezekias", "Matthew 1:9", "nt", "Hezekiah"),
    ("Manasses", "Matthew 1:10", "nt", "Manasseh"),
    ("Josias", "Matthew 1:10", "nt", "Josiah"),
    ("Jechonias", "Matthew 1:11", "nt", "Jeconiah"),
    ("Salathiel", "Matthew 1:12", "nt", "Shealtiel"),
    ("Zorobabel", "Matthew 1:12", "nt", "Zerubbabel"),
    ("Juda", "Matthew 2:6", "nt", "Judah"),
    ("Zabulon", "Matthew 4:13", "nt", "Zebulun"),
    ("Nephthalim", "Matthew 4:13", "nt", "Naphtali"),
    ("Jonas", "Matthew 12:39", "nt", "Jonah"),
    ("Zacharias", "Matthew 23:35", "nt", "Zechariah"),
    ("Barachias", "Matthew 23:35", "nt", "Berechiah"),
    ("Noe", "Matthew 24:37", "nt", "Noah"),
    ("Juda", "Mark 6:3", "nt", "Judas"),
    ("Elisabeth", "Luke 1:5", "nt", "Elizabeth"),
    ("Thara", "Luke 3:34", "nt", "Terah"),
    ("Nachor", "Luke 3:34", "nt", "Nahor"),
    ("Saruch", "Luke 3:35", "nt", "Serug"),
    ("Ragau", "Luke 3:35", "nt", "Reu"),
    ("Phalec", "Luke 3:35", "nt", "Peleg"),
    ("Sala", "Luke 3:35", "nt", "Shelah"),
    ("Sem", "Luke 3:36", "nt", "Shem"),
    ("Mathusala", "Luke 3:37", "nt", "Methuselah"),
    ("Maleleel", "Luke 3:37", "nt", "Mahalaleel"),
    ("Sychem", "Acts 7:16", "nt", "Shechem"),
    ("Charran", "Acts 7:2", "nt", "Haran"),
    ("Madian", "Acts 7:29", "nt", "Midian"),
    ("Cis", "Acts 13:21", "nt", "Kish"),
    ("Timotheus", "Acts 16:1", "nt", "Timothy"),
    ("Rebecca", "Romans 9:10", "nt", "Rebekah"),
    ("Sabaoth", "Romans 9:29", "nt", "Lord of hosts"),
    ("Sodoma", "Romans 9:29", "nt", "Sodom"),
    ("Gomorrha", "Romans 9:29", "nt", "Gomorrah"),
    ("Sion", "Romans 9:33", "nt", "Zion"),
    ("Osee", "Romans 9:25", "nt", "Hosea"),
    ("Phebe", "Romans 16:1", "nt", "Phoebe"),
    ("Agar", "Galatians 4:24", "nt", "Hagar"),
    ("Marcus", "Colossians 4:10", "nt", "Mark"),
    ("Lucas", "Philemon 1:24", "nt", "Luke"),
    ("Sara", "Hebrews 11:11", "nt", "Sarah"),
    ("Gedeon", "Hebrews 11:32", "nt", "Gideon"),
    ("Jephthae", "Hebrews 11:32", "nt", "Jephthah"),
    ("Sabaoth", "James 5:4", "nt", "Lord of hosts"),
]

EQUIVALENT_OVERRIDES = {
    "BABYLON": "Babylon",
    "Abessa": "Abishai",
    "Abiesdri": "Ashpenaz",
    "Abia": "Abijah",
    "Abigaia": "Abigail",
    "Achia": "Ahijah",
    "Achimaas": "Ahimaaz",
    "Achitophel": "Ahithophel",
    "Ada": "Adah",
    "Adonias": "Adonijah",
    "Adraazar": "Hadadezer",
    "Adrazar": "Hadadezer",
    "Ader": "Hadad",
    "Aggai": "Ai",
    "Ammanites": "Ammonites",
    "Amorrites": "Amorites",
    "Akchō": "Acco",
    "Ambri": "Omri",
    "Anchous": "Achish",
    "Arthasastha": "Artaxerxes",
    "Assour": "Asshur",
    "Ausē": "Hoshea",
    "Azarias": "Azariah",
    "Baasa": "Baasha",
    "Baithsamyis": "Beth-shemesh",
    "Beeera": "Beerah",
    "Bathouel": "Bethuel",
    "Deblatha": "Riblah",
    "Deblathaim": "Beth-diblathaim",
    "Beniamin": "Benjamin",
    "Bēbai": "Bebai",
    "Belasōr": "Baal-hazor",
    "Bersabee": "Beersheba",
    "Bethleem": "Bethlehem",
    "Bethlehem": "Bethlehem",
    "GOD": "God",
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
    "Gesirite": "Geshurites",
    "Iabis": "Jabesh",
    "Iazēr": "Jazer",
    "Iessai": "Jesse",
    "Iezabel": "Jezebel",
    "Iōchabēd": "Ichabod",
    "Idumea": "Edom",
    "Idumean": "Edomite",
    "Idumeans": "Edomites",
    "Ioachas": "Jehoahaz",
    "Ioas": "Joash",
    "Iodae": "Jehoiada",
    "JESUS": "Jesus",
    "Ionathan": "Jonathan",
    "Iosaphat": "Jehoshaphat",
    "Iosedek": "Jozadak",
    "Iothor": "Ithra",
    "Iou": "Jehu",
    "Ioudaioi": "Jews",
    "Jephonnē": "Jephunneh",
    "Kades": "Kadesh",
    "Karmelite": "Carmelite",
    "Kaath": "Kohath",
    "Kerōe": "Iron",
    "Kis": "Kish",
    "Manasse": "Manasseh",
    "Melchol": "Michal",
    "Maachathi": "Maachathites",
    "Moyses": "Moses",
    "Nabouthai": "Naboth",
    "Naiman": "Naaman",
    "Nauē": "Nun",
    "Ochozias": "Ahaziah",
    "Orna": "Araunah",
    "Phadaēl": "Pedahel",
    "Phaloch": "Pul",
    "Phaltiēl": "Paltiel",
    "Phinees": "Phinehas",
    "Rama": "Ramah",
    "Horonin": "Beth-horon",
    "Rison": "Dishan",
    "Rhodians": "Dodanim",
    "Ros": "Rosh",
    "Rouben": "Reuben",
    "Roubenites": "Reubenites",
    "Sabaoth": "Lord of hosts",
    "Sabaōth": "Lord of hosts",
    "Saba": "Sheba",
    "Sala": "Shelah",
    "Assur": "Assyria",
    "Sarira": "Zereda",
    "Salamiēl": "Shammua",
    "Samaias": "Shemaiah",
    "Selmona": "Zalmonah",
    "Sarouia": "Zeruiah",
    "Siba": "Ziba",
    "Sisara": "Sisera",
    "Sychem": "Shechem",
    "Thaiman": "Teman",
    "Tanis": "Zoan",
    "Thersa": "Tirzah",
    "Thaglathfellasar": "Tilgathpilneser",
    "Thaglathphalnasar": "Tilgathpilneser",
    "Achaz": "Ahaz",
    "Abiud": "Abiud",
    "Aminadab": "Amminadab",
    "Agar": "Hagar",
    "Aser": "Asher",
    "Barachias": "Berechiah",
    "Booz": "Boaz",
    "Charran": "Haran",
    "Cis": "Kish",
    "Elisabeth": "Elizabeth",
    "Eliud": "Eliud",
    "Esrom": "Hezron",
    "Ezekias": "Hezekiah",
    "Gedeon": "Gideon",
    "Gomorrha": "Gomorrah",
    "Jechonias": "Jeconiah",
    "Jephthae": "Jephthah",
    "Jeremy": "Jeremiah",
    "Josedek": "Josedech",
    "Joatham": "Jotham",
    "Josaphat": "Jehoshaphat",
    "Josias": "Josiah",
    "Juda": "Judah",
    "Judaea": "Judea",
    "Judas": "Judas",
    "Lucas": "Luke",
    "Madian": "Midian",
    "Manasses": "Manasseh",
    "Marcus": "Mark",
    "Mathusala": "Methuselah",
    "Maleleel": "Mahalaleel",
    "NAZARETH": "Nazareth",
    "Naasson": "Nahshon",
    "Nachor": "Nahor",
    "Nephthalim": "Naphtali",
    "Noe": "Noah",
    "Osee": "Hosea",
    "Ozias": "Uzziah",
    "Phares": "Perez",
    "Phalec": "Peleg",
    "Phebe": "Phoebe",
    "Rachab": "Rahab",
    "Ragau": "Reu",
    "Rebecca": "Rebekah",
    "Roboam": "Rehoboam",
    "Salathiel": "Shealtiel",
    "Sara": "Sarah",
    "Saruch": "Serug",
    "Sion": "Zion",
    "Sodoma": "Sodom",
    "Thamar": "Tamar",
    "Thara": "Terah",
    "Timotheus": "Timothy",
    "Urias": "Uriah",
    "Zara": "Zerah",
    "Zabulon": "Zebulun",
    "Zaboucham": "Buz",
    "Zabdias": "Zebadiah",
    "Zaboulon": "Zebulun",
    "Zabouth": "Zabud",
    "Zabouthaithan": "Vaizatha",
    "Zacharias": "Zechariah",
    "Zacharia": "Zechariah",
    "Zorobabel": "Zerubbabel",
}

EQUIVALENT_MEANING_OVERRIDES = {
    "Adah": "an assembly",
    "Ai": "heap; ruin",
    "Aiath": "heap; ruin",
    "Ammah": "a cubit; mother-city; beginning",
    "Assyria": "country of Assur or Ashur",
    "Ashpenaz": "horse-nose; chief eunuch of Nebuchadnezzar",
    "Beerah": "a well; declaring",
    "Beth-diblathaim": "house of fig-cakes; house near Diblathaim",
    "Beth-eked": "house of shearing; shearing house",
    "Beth-horon": "house of wrath",
    "Bethuel": "filiation of God",
    "Carmelite": "circumcised lamb; harvest; full of ears of corn",
    "Diblath": "paste of dry figs",
    "Edom": "red; earthy; bloody",
    "Edomite": "red; earthy; bloody",
    "Edomites": "people of Edom; red",
    "Dishan": "a threshing",
    "Baal-hazor": "Baal's village; lord of the enclosure",
    "Baalzebub": "lord of flies",
    "BABYLON": "confusion; mixture",
    "Beth-shemesh": "house of the sun",
    "Cappadocia": "land of beautiful horses",
    "Damascus": "silent is the sackcloth weaver; traditional city-name meaning",
    "Iron": "watchful; alert",
    "Juda": "the praise of the Lord; confession",
    "Judaea": "land of Judah",
    "Judas": "the praise of the Lord; confession",
    "Jezreel": "God sows",
    "Hophni": "he that covers; my fist",
    "Huri": "their liberty; their whiteness; their hole",
    "Husham": "hastily; great haste",
    "Hathach": "good; well-disposed",
    "Julius": "downy; soft and tender hair",
    "LORD of hosts": "Yahweh of armies; Lord of heavenly hosts",
    "Jahdai": "Yah leads",
    "Jorkeam": "green people; grasslike folks",
    "Lord of hosts": "Yahweh of armies; Lord of heavenly hosts",
    "Kartan": "town; double city",
    "Lamech": "powerful; overthrower",
    "Maleleel": "praising God",
    "Melzar": "master of wine; chief butler; steward",
    "Matthan": "gifts; rains",
    "Michael": "Who is like God?",
    "Ithra": "abundance; excellence",
    "Jose": "raised; who pardons",
    "Joses": "raised; who pardons",
    "Nimrod": "rebellion; probably from an Assyrian source word",
    "Naashon": "that foretells; that conjectures",
    "Nahor": "hoarse; dry; hot",
    "Nahshon": "that foretells; that conjectures",
    "Nahum": "comforter; penitent",
    "Naum": "comforter; penitent",
    "Nereus": "water; sea",
    "Nephthalim": "that struggles or fights",
    "Nicolas": "victory of the people",
    "Naphtali": "that struggles or fights",
    "Nachor": "hoarse; dry; hot",
    "Paulus": "small; little",
    "Shelah": "that breaks; that unties; that undresses",
    "Pedahel": "God has redeemed",
    "Persis": "Persian woman",
    "Philippi": "city of Philip; horse-loving town",
    "Rachab": "broad; spacious",
    "Rama": "height; exalted place",
    "Ramathaimzophim": "the two watch-towers",
    "Ramah": "height; exalted place",
    "Rhodes": "rose island; rose",
    "Salathiel": "asked or lent of God",
    "Saron": "his plain; his song",
    "Shealtiel": "asked or lent of God",
    "Shimea": "that hears, or obeys; perdition",
    "Siloam": "sent",
    "Tilgathpilneser": "that binds or takes away captivity",
    "Tiras": "desire",
    "Zarah": "east; brightness",
    "Zerah": "east; brightness",
    "Zabud": "given; gift",
    "Zalmonah": "the shade; the sound of the number; his image",
    "Zoan": "motion",
    "Beelzebub": "lord of flies",
    "Jew": "praised one; one from Judah",
    "Jews": "People of Judah; Judeans",
    "Judea": "land of Judah",
    "Kedesh": "holy place; sanctuary",
    "Zereda": "ambush; change of dominion",
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
    "Bakcha": "Baana",
    "Bethshemesh": "Beth-shemesh",
    "Gaithan": "Ethan",
    "Ioasar": "Jesher",
    "Iethrite": "Ithrite",
    "Ithrites": "Ithrite",
    "Kadeshbarnea": "Kadesh-Barnea",
    "Mekedo": "Megiddo",
    "MeribahKadesh": "Meribah-kadesh",
    "Raemmath": "Ramah",
    "Sichem": "Shechem",
}

MEANING_NAME_ALIASES = {
    "Acco": "Accho",
    "Aijalon": "Ajalon",
    "Baana": "Baanah",
    "Beth-shemesh": "Bethshemesh",
    "Bethlehemite": "Bethlehem",
    "Ephrathah": "Ephratah",
    "Gileadites": "Gilead",
    "Hoshea": "Hosea",
    "Ichabod's": "Ichabod",
    "Ithrite": "Jether",
    "Ittai": "Ithai",
    "Joktheel": "Joktheel",
    "Jezreel": "Jezreel",
    "Jethri": "Jether",
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
    "Assyrians": "Assyria",
    "Assyrian": "Assyria",
    "Chaldeans": "Chaldea",
    "Chaldean": "Chaldea",
    "Syrians": "Syria",
    "Syrian": "Syria",
    "Philistines": "Philistine",
    "Phylistieim": "Philistine",
    "Gergesite": "Girgashite",
    "Girgashites": "Girgashite",
    "Ommaeans": "Emims",
    "Adullamite": "Adullam",
}

EQUIVALENT_OVERRIDES.update(
    {
        "Achamani": "Hachmoni",
        "Adonai": "Lord",
        "Adōnai": "Lord",
        "Anna": "Hannah",
        "Arama": "Ramah",
        "Caesar": "Caesar",
        "Chalanne": "Calneh",
        "Charoub": "Cherub",
        "Chasloniem": "Casluhim",
        "Chazad": "Chesed",
        "Chorraeans": "Horites",
        "Iebous": "Jebus",
        "Ierousa": "Jerusha",
        "Iesbakasa": "Joshbekashah",
        "Iesboam": "Jashobeam",
        "Iesebaal": "Jashobeam",
        "Iobel": "Jabal",
        "Iarim": "Harum",
        "Korite": "Korahite",
        "Mardochaios": "Mordecai",
        "Mephibosthe": "Mephibosheth",
        "Ornia": "Adonijah",
        "Ourias": "Uriah",
        "Phasga": "Pisgah",
        "Phaldes": "Pildash",
        "Phylistieim": "Philistines",
        "Ramathaimzophim": "Ramathaimzophim",
        "Raōm": "Ir",
        "Selei": "Shilhi",
        "Sior": "Zair",
        "Sharon": "Sharon",
        "Siphā": "Zophim",
        "Thekoue": "Kue",
        "Thekoim": "Tekoites",
        "Thema": "Thamah",
        "Syria": "Syria",
        "Thoke": "Tohu",
        "Nasib": "Zuph",
    }
)

EQUIVALENT_OVERRIDES.update(
    {
        "Alōēs": "Hallohesh",
        "Aphphousōth": "separate house",
        "Amaria": "Amariah",
        "Arabah": "Arabah",
        "Arōs": "Haruz",
        "Azotus": "Azotus (Ashdod)",
        "Azōtos": "Ashdod",
        "Babylon": "Babylon",
        "Baithōn": "Bethhoron",
        "Baithōr": "Baetheor",
        "Baniēlam": "Helem",
        "Basēza": "Meshezabeel",
        "Beōr": "Beor",
        "Borazē": "Bigtha",
        "Emēr": "Amon",
        "Eraēl": "Asarelah",
        "Gai-melē": "Valley of Salt",
        "Geththēm": "Getthaim",
        "Gōla": "Giloh",
        "Hebrew": "Hebrew",
        "Ieremeēl": "Jeroham",
        "Ieziēl": "Jeziel",
        "Iēssiou": "Isaiah",
        "Iēsoue": "Jehoshuah",
        "Iēsouni": "Jesiah",
        "Iōaa": "Joah",
        "Iōadae": "Joadas",
        "Ioach": "Joab",
        "Iōanou": "Johanan",
        "Iōazar": "Joezer",
        "Iōbab": "Jobab",
        "Iōdan": "Joadam",
        "Iōsadak": "Jehozadak",
        "Iōsia": "Jeshaiah",
        "Iodiēl": "Jediael",
        "Ioppē": "Joppa",
        "Iseriēl": "Jesharelah",
        "Isbakōm": "Isbacom",
        "Issiēr": "Jezer",
        "Jakephzēb": "winepress of Zeeb",
        "Kadēs": "Kadesh",
        "Magaphēs": "Magpiash",
        "Masemannē": "Mishmannah",
        "Massalēm": "Meshullam",
        "Mēēra": "Maharai",
        "Mesōzebel": "Meshezabeel",
        "Metabēchas": "Tibhath",
        "Mōabitans": "Moabites",
        "Myrsinōn": "Myrsinon",
        "Nēriou": "Nerias",
        "Nōbai": "Nebai",
        "Nōdab": "Nachon",
        "Osēe": "Hoshea",
        "Oza": "Uzza/Uzzah",
        "Ozriēl": "Azareel",
        "Parosōm": "Gershon",
        "Pheliēl": "Penuel",
        "Pharisee": "Pharisee",
        "Raassōn": "Rezin",
        "Roōllam": "Zaham",
        "Samaria": "Samaria",
        "Sēgōr": "So",
        "Sēlō": "Sallu",
        "Sellēs": "Laish",
        "Sousa": "Susa/Shushan",
        "Sōba": "Zobah",
        "Sōbēk": "Shobek",
        "Sōman": "Shunem",
        "Sōmēr": "Shomer",
        "Solōmōn": "Solomon",
        "Somorōn": "Zemaraim",
        "Sōpharphak": "Shephuphan",
        "Themmōn": "Kartan",
        "Thēsous": "Elishua",
        "Zechōra": "Zechora",
        "Zōsara": "Zeresh",
        "Ōr": "Hur",
        "Ōrōnēn": "Oronen",
    }
)

EQUIVALENT_MEANING_OVERRIDES.update(
    {
        "Adami-nekeb": "ruddy hollow; corrugated soil",
        "Adonai": "Lord; master",
        "Adōnai": "Lord; master",
        "Alexander": "defender/helper of men",
        "Alexandria": "city of Alexander; defender/helper of men",
        "Alexandrians": "people of Alexandria; city of Alexander",
        "Alphaeus": "learned; chief",
        "Amariah": "Yahweh has spoken; Yahweh has promised",
        "Amphipolis": "around the city",
        "Anakim": "descendants of Anak; long-necked/giant people",
        "Arabah": "plain; desert steppe",
        "Aram": "highness; highland",
        "Atharim": "places; tracks; route name",
        "Athenians": "people of Athens; city of Athena",
        "Athens": "city of Athena",
        "Azotus (Ashdod)": "stronghold; same city as Ashdod",
        "Babylon": "confusion; mixture",
        "Bamoth": "high places",
        "Basemath": "perfumed",
        "Bezalel": "in the shadow/protection of God",
        "Bosor": "burning; foolish; mad; variant form of Beor",
        "Caesar": "imperial title; associated with Latin caesus, cut",
        "Caesarea": "city of Caesar",
        "Children": "sons; children",
        "Christians": "followers of Christ, the anointed one",
        "Christian": "follower of Christ, the anointed one",
        "Cretans": "people of Crete",
        "Cyrenians": "people of Cyrene",
        "Damascenes": "people of Damascus",
        "Eloai": "my God",
        "Elōai": "my God",
        "Epaenetus": "praiseworthy",
        "Ephesian": "person of Ephesus; desirable",
        "Ephesians": "people of Ephesus; desirable",
        "Gazites": "people of Gaza; strong",
        "Gentiles": "nations; non-Jewish peoples",
        "Greece": "Greece; Hellenic land",
        "Greek": "Greek; Hellenic person",
        "Greeks": "Greek people; Hellenes",
        "Hebrew": "from Eber; one from beyond",
        "Helper": "helper; advocate; comforter",
        "Herodians": "party of Herod; son of a hero",
        "Holy Spirit": "holy breath/spirit",
        "Idumeans": "people of Idumea/Edom; red",
        "Ituraea": "land of Jetur; enclosed/guarded region",
        "Laodiceans": "people of Laodicea; just people",
        "Legion": "legion; a large military unit",
        "Levite": "person of Levi; joined/attached",
        "Levites": "people of Levi; joined/attached",
        "Libyans": "people of Libya",
        "Lycia": "wolf-land; Lycian region",
        "Magi": "wise men; learned astrologer-priests",
        "Macedonian": "person of Macedonia; high/tall one",
        "Macedonians": "people of Macedonia; high/tall ones",
        "Matthat": "gift",
        "Medes": "people of Media",
        "Miletus": "red; scarlet",
        "Nazarenes": "people connected with Nazareth; separated/crowned",
        "Nazirite": "separated/consecrated one",
        "Nazirites": "separated/consecrated ones",
        "Negeb": "south; dry land",
        "Oholiab": "father's tent",
        "Parthians": "people of Parthia",
        "Pharisee": "separated one; set apart",
        "Philippians": "people of Philippi; city of Philip",
        "Rameses": "Ra has fashioned/begotten him",
        "Salmone": "peaceable; perfect",
        "Samaria": "watch-mountain",
        "Samaritan": "person of Samaria; watch-mountain",
        "Samaritans": "people of Samaria; watch-mountain",
        "Scythians": "Scythian people; archer/nomad people",
        "Shelanite": "person of Shelah; breaking/letting loose",
        "Shelanites": "people of Shelah; breaking/letting loose",
        "Susa/Shushan": "lily",
        "Syria": "Aram/Syria; highland",
        "Syrian": "Aramean/Syrian; highland",
        "Syrians": "Arameans/Syrians; highland",
        "Thaddaeus": "praising/confessing",
        "Thessalonians": "people of Thessalonica; victory over Thessalians",
        "Tigris": "swift; rapid",
        "Trogyllium": "cave-like place",
        "Uzza/Uzzah": "strength",
        "Zimri": "my praise; my music",
    }
)

MEANING_NAME_ALIASES.update(
    {
        "Alphaeus": "Alpheus",
        "Arabian": "Arabia",
        "Arabians": "Arabia",
        "Babylonians": "Babylon",
        "Basemath": "Bashemath",
        "Bezalel": "Bezaleel",
        "Caiaphas": "Caiphas",
        "Corinthians": "Corinth",
        "Cyrenians": "Cyrene",
        "Egyptian": "Egypt",
        "Egyptians": "Egypt",
        "Epaenetus": "Epenetus",
        "Ephesian": "Ephesus",
        "Ephesians": "Ephesus",
        "Ethiopians": "Ethiopia",
        "Galatians": "Galatia",
        "Herodians": "Herod",
        "Idumeans": "Idumea",
        "Laodiceans": "Laodicea",
        "Levite": "Levi",
        "Levites": "Levi",
        "Macedonian": "Macedonia",
        "Macedonians": "Macedonia",
        "Matthat": "Matthan",
        "Medes": "Media",
        "Mushites": "Mushi",
        "Nazirite": "Nazarite",
        "Nazirites": "Nazarite",
        "Nethanel": "Nathanael",
        "Netophathite": "Netophah",
        "Netophathites": "Netophah",
        "Oholiab": "Aholiab",
        "Persian": "Persia",
        "Persians": "Persia",
        "Philippians": "Philippi",
        "Raphain": "Rehpaim",
        "Rephaim": "Rehpaim",
        "Samaritan": "Samaria",
        "Samaritans": "Samaria",
        "Shelanite": "Shelah",
        "Shelanites": "Shelah",
        "Sidonian": "Sidon",
        "Sidonians": "Sidon",
        "Thaddaeus": "Thaddeus",
        "Thessalonians": "Thessalonica",
        "Timaeus": "Timeus",
    }
)

EQUIVALENT_MEANING_OVERRIDES.update(
    {
        "Abida": "father of knowledge",
        "Adalia": "one that draws water; poverty; cloud; death",
        "Ahohi": "brotherly; my thorn or thistle",
        "Anan": "cloud; prophecy",
        "Armenia": "highland/Armenian land",
        "Asshur": "happy; walking/upright",
        "Atarothadar": "crowns of power",
        "Azal": "near; reserved",
        "Baanah": "in the answer; in affliction",
        "Baana": "in the answer; in affliction",
        "Baithon": "divisions",
        "Bariah": "in fellowship",
        "Bel": "lord; master",
        "Ben-Hur": "son of Hur; son of whiteness/nobility",
        "Bethjesimoth": "house of desolations",
        "Bethrehob": "house of spaciousness",
        "Bethshean": "house of rest/ivory; house of teeth",
        "Boscath": "in poverty",
        "Canneh": "established settlement",
        "Carchemish": "fortress/market of Chemosh; lamb withdrawn",
        "Chelkias": "Yahweh is my portion",
        "Cherub": "guardian being; blessing",
        "Cononiah": "Yahweh has established",
        "Dara": "pearl of wisdom; home of knowledge",
        "Enaim": "two springs; open place",
        "Gai-mele": "valley of salt; name meaning approximate",
        "Gedor": "wall; enclosure",
        "Ginnethon": "garden",
        "Goiim": "nations",
        "Hararites": "mountain people",
        "Hararite": "mountain person",
        "Hashmonah": "fertile/fat place",
        "Haziel": "God sees; vision of God",
        "Hezion": "vision; revelation",
        "Ieremeel": "God has mercy; God exalts",
        "Isshiah": "it is the Lord",
        "Ivvah": "iniquity; ruin",
        "Jahziel": "God sees",
        "Jehoaddah": "Yahweh has adorned; testimony of Yahweh",
        "Jehozadak": "Yahweh is righteous; justice of the Lord",
        "Jehiel": "God lives",
        "Jehoshabeath": "Yahweh has sworn",
        "Jeshaiah": "salvation of Yahweh",
        "Jezreelites": "people of Jezreel; God sows",
        "Jezreelite": "person of Jezreel; God sows",
        "Jephthah": "he opens",
        "Joiakim": "Yahweh raises/establishes",
        "Joshbekashah": "a hard seat; difficult dwelling",
        "Josedech": "Yahweh is righteous; justice of the Lord",
        "Jozadak": "Yahweh is righteous; justice of the Lord",
        "Kadesh": "holiness",
        "Kehelathah": "assembly; congregation",
        "Keilah": "fortress; citadel",
        "Korahite": "descendant of Korah; baldness; ice; frost",
        "Korahites": "descendants of Korah; baldness; ice; frost",
        "Kir-hareseth": "city of the sun; wall of burnt brick",
        "Kirjathjearim": "city of woods",
        "Kolaiah": "voice of Yahweh",
        "Kore": "caller; crier",
        "Kue": "Cilician region",
        "Lakum": "stopping place",
        "Lasha": "to call; to anoint",
        "Lodebar": "no pasture; no word",
        "Lord": "Lord; master",
        "Mahol": "dance; round dance",
        "Maoch": "oppression",
        "Matri": "rain; prison",
        "Matrites": "people of Matri; rain/prison",
        "Melchiel": "God is my king/counselor",
        "Michmash": "hidden; struck place",
        "Mithkah": "sweetness; pleasantness",
        "Moza": "going out; source",
        "Naaran": "young person; youth",
        "Nebajoth": "words; prophecies; buds",
        "Neco": "lame; beaten",
        "Urijah": "the Lord is my light or fire",
        "Nephtoah": "opening; open",
        "Ninevites": "people of Nineveh; dwelling of Ninus/fish-city",
        "Pashhur": "freedom; splendor",
        "Peleth": "special; separated",
        "Petra": "rock",
        "Pildash": "flame of fire",
        "Rapha": "healing; comfort",
        "Salu": "exalted; weighed",
        "Shaalim": "foxes; paths",
        "Shavsha": "noble; scribe-name form",
        "Shilonites": "people of Shiloh; peaceful/resting place",
        "Shiphmites": "people of Shepham; bare/smooth place",
        "Shocho": "defense; bough",
        "Shunammite": "person of Shunem; double resting place",
        "Siphmoth": "fruitful places",
        "Somer": "keeper; guard",
        "Tahapanes": "secret temptation",
        "Tahash": "that makes haste; that keeps silence",
        "Tahtim hodshi": "lower/new land",
        "Tekoites": "people of Tekoa; trumpet; confirmed",
        "Tekoah": "trumpet; confirmed",
        "Teresh": "strict; severe",
        "Thimnathah": "portion; allotment",
        "Tophel": "ruin; folly; without understanding",
        "Topheth": "drum; place of burning/betrayal",
        "Vaizatha": "sprinkling the chamber",
        "Zarethan": "tribulation; perplexity",
        "Zophim": "watchers",
        "Zuph": "watcher; honeycomb",
        "Asarelah": "upright toward God; God has turned",
        "Baetheor": "house; region-name form",
        "Bigtha": "given by fortune",
        "Getthaim": "winepress; place-name form",
        "Hallohesh": "the whisperer; the slanderer",
        "Isbacom": "empty/exhausted one; Ishbak-name family",
        "Jesharelah": "upright toward God",
        "Joadam": "Yahweh is people; name meaning approximate",
        "Joadas": "Yahweh knows",
        "Jehoshuah": "Yahweh saves",
        "Meshezabeel": "God rescues; God delivers",
        "Nerias": "lamp of Yahweh",
        "separate house": "separated/free dwelling",
        "So": "Egyptian royal name; meaning obscure",
        "Tibhath": "slaughter; security",
        "Valley of Salt": "valley of salt",
        "winepress of Zeeb": "winepress of Zeeb; Zeeb means wolf",
        "Zeri": "built; fashioned; balsam",
    }
)

EQUIVALENT_MEANING_OVERRIDES.update(
    {
        "Abiezrites": "descendants of Abiezer; father of help",
        "Aher": "another; following one",
        "Aloes": "aloes; fragrant spice",
        "Aphphousoth": "separated; exposed place",
        "Aridai": "lion-like",
        "Aridatha": "lion-like decree",
        "Arisai": "lion-like",
        "Aros": "flea; moth-fruit name-family",
        "Ashkelon": "weight; balance",
        "Aspatha": "horse-given",
        "Azarel": "help of God",
        "Aziel": "God is strength",
        "Baithor": "house; region-name form",
        "Banielam": "son or people of strength",
        "Baseza": "white; fair one",
        "Bimhal": "circumcised; hastened",
        "Boraze": "in strength; Boaz-name family",
        "Chusi": "Cushite; blackness",
        "Edna": "pleasure; delight",
        "Ela": "oak; terebinth",
        "Emer": "sheaf; handful",
        "Ephod": "priestly garment; covering",
        "Erael": "watcher of God",
        "Eth-kazin": "time/place of a prince",
        "Geththem": "winepress; place-name form",
        "Gilonite": "person of Giloh; he that rejoices; he that overturns",
        "Gola": "exile; passage/revolution name-family",
        "Gothoniel": "the hour of God",
        "Haziel": "God sees; vision of God",
        "Iessiou": "Jesse-name family; gift/being",
        "Iesouni": "Joshua/Jesus name-family; Yahweh saves",
        "Iesoue": "Joshua/Jesus name-family; Yahweh saves",
        "Ieziel": "sprinkling of God",
        "Iobab": "sorrowful; hated",
        "Iodan": "judgment; judge-name family",
        "Iodiel": "known by God; praise of God",
        "Ioadae": "Yahweh knows",
        "Ioanou": "John-name family; Yahweh is gracious",
        "Ioazar": "Yahweh has helped",
        "Ioaa": "Yahweh is brother; Yahweh is friend",
        "Ioppe": "beautiful",
        "Iosia": "Yahweh supports/heals; Josiah-name family",
        "Iosadak": "Yahweh is righteous",
        "Issier": "upright; prince of God name-family",
        "Isbakom": "empty/exhausted one; Ishbak-name family",
        "Jakephzeb": "he gathers; he collects",
        "Koz": "thorn; end",
        "Korhites": "descendants of Korah; bald/ice-name family",
        "Magaphes": "body/slaughter name-family",
        "Masemanne": "fatness; strength",
        "Massalem": "peaceable; perfect",
        "Meera": "bitter; disputing one",
        "Meshillemoth": "peaceable; repayment",
        "Meshullam": "friend; repaid; devoted",
        "Mesozebel": "Jezebel-name family; chaste/where is the prince",
        "Moabitans": "Moabites; from Moab, of his father",
        "Mount Seir": "mountain of Seir; hairy/rough",
        "Myrsinon": "myrtle place",
        "Osee": "salvation",
        "Ozriel": "God is my help/strength",
        "Oziel": "strength of God",
        "Parosom": "flea; moth-fruit name-family",
        "Pheliel": "God is wonderful; face/vision of God",
        "Piltai": "Yahweh delivers; my escape",
        "Raasson": "prince; delight",
        "Remmon": "pomegranate; elevation",
        "Roollam": "elevation; rolling",
        "Sarbacha": "royal official name",
        "Selo": "rock; strong place",
        "Selles": "prince; leader",
        "Segor": "little; small",
        "Shilonite": "person of Shiloh; peaceful/resting place",
        "Soba": "station; turning/captivity name-family",
        "Sobek": "made void; forsaken",
        "Soman": "strong; powerful",
        "Somoron": "watch-place; Samaria-name family",
        "Sopharphak": "scribe; numbering name",
        "Themmōn": "pomegranate/elevation name-family",
        "Themmon": "pomegranate/elevation name-family",
        "Thesous": "Jesus/Joshua name-family; Yahweh saves",
        "Tou": "living; declaring",
        "Valley of Rephaim": "valley of the Rephaim; giants/relaxed ones",
        "Zabdiel": "gift/endowment of God",
        "Zechora": "remembered; male name-family",
        "Zosara": "little/small name-family",
    }
)

MEANING_NAME_ALIASES.update(
    {
        "Abida": "Abidah",
        "Adalia": "Adaliah",
        "Ahohi": "Ahoah",
        "Amashsai": "Amashai",
        "Asshur": "Ashur",
        "Atarothadar": "Atarothaddar",
        "Azotos": "Azotus",
        "Baanah": "Baanah",
        "Becorath": "Bechorath",
        "Berechiah": "Berachiah",
        "Boscath": "Boskath",
        "Carchemish": "Charchemish",
        "Cononiah": "Coniah",
        "Eleasah": "Elasah",
        "Gedor": "Geder",
        "Ginnethon": "Ginnetho",
        "Habazziniah": "Habazinaiah",
        "Ivvah": "Ivah",
        "Jahziel": "Jahaziel",
        "Jehoaddah": "Jehoadah",
        "Jehiel": "Jeheiel",
        "Jeshuah": "Jeshua",
        "Joiakim": "Joakim",
        "Kades": "Kadesh",
        "Kehelathah": "Kehelahath",
        "Keilah": "Keiiah",
        "Kolaiah": "Kolariah",
        "Lasha": "Lashah",
        "Matri": "Matri",
        "Mithkah": "Mithcah",
        "Nebajoth": "Nebaioth",
        "Nephtoah": "Nephthoah",
        "Nobai": "Nebai",
        "Pashhur": "Pashur",
        "Rapha": "Raphah",
        "Salu": "Sallu",
        "Shocho": "Shochoh",
        "Somer": "Shomer",
        "Tahapanes": "Taphenes",
        "Tahash": "Thahash",
        "Thimnathah": "Timnath",
        "Topheth": "Tophet",
        "Zarethan": "Zaretan",
    }
)

MEANING_NAME_ALIASES.update(
    {
        "Ashkelon": "Askelon",
        "Gothoniel": "Othniel",
        "Jeiel": "Jeziel",
        "Mosollamos": "Meshullam",
        "Oziel": "Uzziel",
        "Phasga": "Pisgah",
        "Sachar": "Sacar",
        "Valley of Rephaim": "Rehpaim",
    }
)

EQUIVALENT_MEANING_OVERRIDES.update(
    {
        "Bani": "built; sons",
        "Emim": "terrors; formidable people",
        "Iseriel": "upright/prince of God",
        "Jeshaiah": "salvation of Yahweh",
        "Joiada": "Yahweh knows; knowledge of Yahweh",
        "Joktheel": "subdued by God",
        "Metabechas": "from Tebah/bronze-name family",
        "Neriou": "my lamp; my light",
        "Netophathites": "people of Netophah; dripping/distillation",
        "Oronen": "Horonaim-name family; double cave/place",
        "Ōronen": "Horonaim-name family; double cave/place",
        "Saraph": "burning one; fiery serpent",
        "Ōr": "light",
    }
)

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
    def is_alias_segment(value: str) -> bool:
        if value.lower().startswith("or "):
            value = value[3:].strip()
        parts = re.split(r"[- ]+", value)
        return bool(parts) and all(part and part[0].isupper() for part in parts)

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or "," not in line:
            continue
        parts = [part.strip() for part in line.split(",")]
        if len(parts) < 2 or not parts[0]:
            continue
        names = [parts[0]]
        meaning_parts = parts[1:]
        while meaning_parts:
            candidate = meaning_parts[0]
            if len(meaning_parts) == 1 or not is_alias_segment(candidate):
                break
            if candidate.lower().startswith("or "):
                candidate = candidate[3:].strip()
            names.append(candidate)
            meaning_parts = meaning_parts[1:]
        meaning = ", ".join(meaning_parts).strip().rstrip(".")
        if not meaning:
            continue
        for name in names:
            key = normalize_lookup(name)
            if key and key not in meanings:
                meanings[key] = meaning
    return meanings


def load_curated_meanings() -> dict[str, str]:
    meanings: dict[str, str] = {}
    for row in load_csv(PROPER_NAMES):
        name = row.get("name", "").strip()
        meaning = row.get("meaning", "").strip()
        if name and meaning:
            meanings[normalize_lookup(name)] = meaning
    return meanings


def resolve_alias_meaning(
    meaning: str,
    curated: dict[str, str],
    hitchcock: dict[str, str],
    seen: set[str] | None = None,
) -> str:
    raw = meaning.strip()
    match = re.match(r"^(?:the )?same as ([A-Za-z][A-Za-z' -]+?)(?:,.*)?$", raw, re.IGNORECASE)
    if not match:
        return raw
    alias = match.group(1).strip()
    alias_key = normalize_lookup(alias)
    if not alias_key:
        return raw
    if seen is None:
        seen = set()
    if alias_key in seen:
        return raw
    seen = seen | {alias_key}
    resolved = curated.get(alias_key) or hitchcock.get(alias_key)
    if not resolved or resolved.strip() == raw:
        return raw
    return resolve_alias_meaning(resolved, curated, hitchcock, seen)


def meaning_for_name(name: str, curated: dict[str, str], hitchcock: dict[str, str]) -> str:
    base = display_name(name)
    if base.endswith("'s"):
        base = base[:-2]
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
            return resolve_alias_meaning(curated[key], curated, hitchcock, {key})
        if key in hitchcock:
            return resolve_alias_meaning(hitchcock[key], curated, hitchcock, {key})
    return "meaning uncertain/not securely attested in the consulted name dictionaries"


def is_uncertain_meaning(meaning: str) -> bool:
    return meaning.startswith("meaning uncertain")


def best_meaning_for_name(
    equivalent: str,
    source_form: str,
    curated: dict[str, str],
    hitchcock: dict[str, str],
) -> str:
    meaning = meaning_for_name(equivalent, curated, hitchcock)
    if not is_uncertain_meaning(meaning):
        return meaning
    if source_form != equivalent:
        source_meaning = meaning_for_name(source_form, curated, hitchcock)
        if not is_uncertain_meaning(source_meaning):
            return source_meaning
    return meaning


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
    if candidate.endswith("'s"):
        candidate = candidate[:-2]
    candidate = display_name(candidate)
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
            meaning=best_meaning_for_name(override, source_form, curated_meanings, hitchcock_meanings),
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
                    meaning=best_meaning_for_name(equivalent, source_form, curated_meanings, hitchcock_meanings),
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
                meaning=best_meaning_for_name(equivalent, source_form, curated_meanings, hitchcock_meanings),
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
            meaning=best_meaning_for_name(equivalent, source_form, curated_meanings, hitchcock_meanings),
            greek_form=greek_form,
            source_form=source_form,
            witness="Logos Bible Knowledgebase alias",
            confidence="alias",
        )

    equivalent = token.replace("ē", "e").replace("ō", "o").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    return EquivalentInfo(
        equivalent=equivalent,
        meaning=best_meaning_for_name(equivalent, source_form, curated_meanings, hitchcock_meanings),
        greek_form=greek_form,
        source_form=source_form,
        witness="normalized source form",
        confidence="fallback",
    )


def source_for_reference(ref: str) -> str:
    if not ref:
        return ""
    book = ref.rsplit(" ", 1)[0]
    ot_books = {name for _, name in OT_UKJV_BOOK_MAP.values()}
    return "ot" if book in ot_books else "nt"


def existing_note_label_sources() -> dict[str, set[str]]:
    labels: dict[str, set[str]] = defaultdict(set)
    for row in load_csv(PROPER_NAMES):
        name = row.get("name", "").strip()
        if name:
            labels[name].add(source_for_reference(row.get("first_reference", "").strip()))
    for row in load_csv(NAMES_OF_GOD):
        source = source_for_reference(row.get("first_reference", "").strip())
        for key in ("transliteration", "english_renderings"):
            value = row.get(key, "")
            for part in re.split(r"[;,]", value):
                part = part.strip()
                if part:
                    labels[part].add(source)
    return dict(labels)


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
    if kind == "person" and equivalent:
        greek_piece = f" Greek form: {equivalent.greek_form}." if equivalent.greek_form else ""
        equivalent_piece = (
            f" Standard English equivalent: {equivalent.equivalent}."
            if equivalent.equivalent != equivalent.source_form
            else ""
        )
        return (
            f"Personal-name meaning: {equivalent.equivalent} — {equivalent.meaning}."
            f"{equivalent_piece} Source form: {equivalent.source_form}."
            f"{greek_piece} Equivalent source: {equivalent.witness}."
        )
    if kind == "people_group" and equivalent:
        greek_piece = f" Greek form: {equivalent.greek_form}." if equivalent.greek_form else ""
        equivalent_piece = (
            f" Standard English equivalent: {equivalent.equivalent}."
            if equivalent.equivalent != equivalent.source_form
            else ""
        )
        return (
            f"People-name meaning: {equivalent.equivalent} — {equivalent.meaning}."
            f"{equivalent_piece} Source form: {equivalent.source_form}."
            f"{greek_piece} Equivalent source: {equivalent.witness}."
        )
    if kind == "supernatural_being" and equivalent:
        greek_piece = f" Greek form: {equivalent.greek_form}." if equivalent.greek_form else ""
        equivalent_piece = (
            f" Standard English equivalent: {equivalent.equivalent}."
            if equivalent.equivalent != equivalent.source_form
            else ""
        )
        return (
            f"Divine/supernatural-name meaning: {equivalent.equivalent} — {equivalent.meaning}."
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


def should_include_unclassified(equivalent: EquivalentInfo) -> bool:
    if is_uncertain_meaning(equivalent.meaning):
        return False
    if equivalent.confidence in {"aligned", "manual", "alias", "direct"}:
        return True
    try:
        return float(equivalent.confidence) >= 0.78
    except ValueError:
        return False


def build_manual_contextual_note_row(
    spec: tuple[str, str, str, str],
    *,
    source_rows_by_ref: dict[str, dict[str, str]],
    curated_meanings: dict[str, str],
    hitchcock_meanings: dict[str, str],
) -> dict[str, str]:
    name, first_reference, source, english_equivalent = spec
    greek_form = find_greek_form(name, source_rows_by_ref.get(first_reference))
    equivalent = EquivalentInfo(
        equivalent=english_equivalent,
        meaning=best_meaning_for_name(english_equivalent, name, curated_meanings, hitchcock_meanings),
        greek_form=greek_form,
        source_form=name,
        witness="manual/standard English equivalent",
        confidence="manual",
    )
    footnote = footnote_for("transliterated_form", "manual contextual standard-equivalent note", equivalent)
    if name == "Judas" and english_equivalent == "Judah":
        greek_piece = f" Greek form: {greek_form}." if greek_form else ""
        footnote = (
            "Standard English equivalent in this genealogy context: Judah. "
            f"Source form: Judas.{greek_piece} "
            f"Name meaning: {equivalent.meaning}. "
            "Equivalent source: manual context review."
        )
    elif name == "Juda" and english_equivalent == "Judas":
        greek_piece = f" Greek form: {greek_form}." if greek_form else ""
        footnote = (
            "Standard English equivalent in this brother-of-Jesus context: Judas. "
            f"Source form: Juda.{greek_piece} "
            f"Name meaning: {equivalent.meaning}. "
            "Equivalent source: manual context review."
        )
    return {
        "name": name,
        "kind": "transliterated_form",
        "first_reference": first_reference,
        "source": source,
        "english_equivalent": english_equivalent,
        "source_form": name,
        "greek_form": greek_form,
        "name_meaning": equivalent.meaning,
        "equivalent_source": equivalent.witness,
        "equivalent_confidence": equivalent.confidence,
        "footnote": footnote,
    }


def main() -> None:
    existing_label_sources = existing_note_label_sources()
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
        source = str(data["source"])
        if token in STOPWORDS:
            counts["skipped_stopword"] += 1
            continue
        if source in existing_label_sources.get(token, set()):
            counts["skipped_existing_same_source"] += 1
            continue
        kind, reason = classify_token(token, primary_kinds=primary_kinds, any_kinds=any_kinds)
        equivalent = None
        refs = data.get("refs", [])
        ref_list = refs if isinstance(refs, list) else [str(data["first_reference"])]
        if kind in {"place", "transliterated_form"}:
            equivalent = resolve_equivalent(
                token,
                ref_list,
                source_rows_by_ref=source_rows_by_ref,
                ukjv_by_ref=ukjv_by_ref,
                alias_primary=alias_primary,
                curated_meanings=curated_meanings,
                hitchcock_meanings=hitchcock_meanings,
            )
            counts[f"equivalent_{equivalent.confidence.split('.')[0]}"] += 1
        elif kind:
            override = EQUIVALENT_OVERRIDES.get(token)
            if override:
                equivalent_name = override
                meaning = best_meaning_for_name(equivalent_name, token, curated_meanings, hitchcock_meanings)
                witness = "manual/standard English equivalent"
                confidence = "manual"
            else:
                direct_meaning = meaning_for_name(token, curated_meanings, hitchcock_meanings)
                primary_options = alias_primary.get(token, set()) if is_uncertain_meaning(direct_meaning) else set()
                if primary_options:
                    equivalent_name = normalize_equivalent_candidate(display_name(min(primary_options, key=len)), alias_primary)
                    meaning = best_meaning_for_name(equivalent_name, token, curated_meanings, hitchcock_meanings)
                    witness = "Logos Bible Knowledgebase alias"
                    confidence = "alias"
                else:
                    equivalent_name = token
                    meaning = direct_meaning
                    witness = "direct curated/Hitchcock lookup"
                    confidence = "direct"
            equivalent = EquivalentInfo(
                equivalent=equivalent_name,
                meaning=meaning,
                greek_form="",
                source_form=token,
                witness=witness,
                confidence=confidence,
            )
            counts[f"equivalent_{equivalent.confidence}"] += 1
        else:
            equivalent = resolve_equivalent(
                token,
                ref_list,
                source_rows_by_ref=source_rows_by_ref,
                ukjv_by_ref=ukjv_by_ref,
                alias_primary=alias_primary,
                curated_meanings=curated_meanings,
                hitchcock_meanings=hitchcock_meanings,
            )
            if not should_include_unclassified(equivalent):
                counts[f"skipped_{reason}"] += 1
                continue
            kind = "transliterated_form"
            counts[f"equivalent_{equivalent.confidence.split('.')[0]}"] += 1
            counts["included_unclassified_resolved_source_form"] += 1
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

    seen_note_keys = {
        (row["name"], row["first_reference"], row["english_equivalent"])
        for row in note_rows
    }
    equivalent_keys = {
        (row["first_reference"], row["source"], row["english_equivalent"]): idx
        for idx, row in enumerate(note_rows)
    }

    def add_manual_note_row(manual_row: dict[str, str]) -> None:
        note_key = (
            manual_row["name"],
            manual_row["first_reference"],
            manual_row["english_equivalent"],
        )
        equivalent_key = (
            manual_row["first_reference"],
            manual_row["source"],
            manual_row["english_equivalent"],
        )
        coverage_row = {
            **manual_row,
            "occurrences": "1",
            "sample_refs": manual_row["first_reference"],
            "reason": "manual contextual standard-equivalent note",
        }
        existing_idx = equivalent_keys.get(equivalent_key)
        if existing_idx is not None:
            note_rows[existing_idx] = dict(manual_row)
            coverage_rows[existing_idx] = coverage_row
            seen_note_keys.add(note_key)
            counts["included_manual_contextual_transliterated_note"] += 1
            return
        if note_key in seen_note_keys:
            return
        note_rows.append(dict(manual_row))
        coverage_rows.append(coverage_row)
        seen_note_keys.add(note_key)
        equivalent_keys[equivalent_key] = len(note_rows) - 1
        counts["included_manual_contextual_transliterated_note"] += 1

    for manual_row in MANUAL_CONTEXTUAL_TRANSLITERATED_NOTE_ROWS:
        add_manual_note_row(manual_row)

    for spec in MANUAL_CONTEXTUAL_TRANSLITERATED_NOTE_SPECS:
        manual_row = build_manual_contextual_note_row(
            spec,
            source_rows_by_ref=source_rows_by_ref,
            curated_meanings=curated_meanings,
            hitchcock_meanings=hitchcock_meanings,
        )
        add_manual_note_row(manual_row)

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
