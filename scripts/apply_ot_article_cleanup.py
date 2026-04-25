#!/usr/bin/env python3
"""Apply scoped English article cleanup to the OT draft.

This is intentionally conservative: it fixes repeated English artifacts around
divine-name formulas without trying to reliteralize the Greek source.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fresh_bible.pipeline_common import ROOT, load_csv, write_csv


OT_SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
DECISIONS = ROOT / "data" / "research" / "translation_decisions.csv"
FOOTNOTES = ROOT / "data" / "research" / "translation_footnotes.csv"

CONSTRUCT_NOUNS = (
    "word",
    "day",
    "way",
    "law",
    "hand",
    "face",
    "name",
    "fear",
    "wrath",
    "blessing",
)
CONSTRUCT_RE = re.compile(r"\b(" + "|".join(CONSTRUCT_NOUNS) + r") of the Lord\b")
PREVIOUS_WORD_RE = re.compile(r"[A-Za-z']+$")
CONSTRUCT_SKIP_PREVIOUS = {
    "a",
    "all",
    "an",
    "another",
    "each",
    "every",
    "good",
    "great",
    "hard",
    "her",
    "his",
    "holy",
    "its",
    "left",
    "living",
    "my",
    "no",
    "one",
    "our",
    "right",
    "same",
    "strong",
    "that",
    "the",
    "their",
    "this",
    "unmixed",
    "what",
    "which",
    "whole",
    "whose",
    "your",
}

BARE_LORD_VERBS = (
    "abhors",
    "add",
    "answer",
    "answers",
    "appointed",
    "at",
    "be",
    "begin",
    "brings",
    "broke",
    "building",
    "clothed",
    "concerning",
    "completed",
    "crushed",
    "created",
    "do",
    "doing",
    "examines",
    "finishes",
    "founded",
    "frees",
    "from",
    "fought",
    "fulfill",
    "give",
    "great",
    "guard",
    "hates",
    "had",
    "heals",
    "hear",
    "help",
    "helped",
    "instructed",
    "judges",
    "kind",
    "lifting",
    "looks",
    "knows",
    "left",
    "loves",
    "might",
    "near",
    "opposes",
    "ordered",
    "overthrew",
    "prepared",
    "received",
    "reigned",
    "reject",
    "remembered",
    "removed",
    "repays",
    "rescued",
    "saw",
    "say",
    "says",
    "scatters",
    "see",
    "seated",
    "sends",
    "shall",
    "showed",
    "shows",
    "sitting",
    "speak",
    "stirred",
    "straightens",
    "supports",
    "swears",
    "told",
    "turns",
    "utterly",
    "with",
)
BARE_LORD_RE = re.compile(
    r"(?<![Tt]he )(?<!my )(?<!your )(?<!our )(?<!his )(?<!their )(?<!good )\bLord "
    r"(?=(?:" + "|".join(BARE_LORD_VERBS) + r")\b)"
)
LORD_OBJECT_REPLACEMENTS = (
    (
        re.compile(r"\bGreat Lord and greatly praised\b"),
        "Great is the Lord and greatly praised",
    ),
    (
        re.compile(r"\bGreat Lord and greatly praiseworthy\b"),
        "Great is the Lord and greatly praiseworthy",
    ),
    (
        re.compile(r"\bServe Lord in fear\b"),
        "Serve the Lord in fear",
    ),
    (
        re.compile(r"\bLord his name\b"),
        "The Lord is his name",
    ),
    (
        re.compile(r"\bLord the good one make atonement concerning\b"),
        "May the good Lord make atonement concerning",
    ),
    (
        re.compile(r"\bthat hand of the Lord made\b"),
        "that the hand of the Lord made",
    ),
    (
        re.compile(r"\bBecause great day of the Lord is near\b"),
        "Because the great day of the Lord is near",
    ),
    (
        re.compile(r"\bEndure Lord and keep his way\b"),
        "Wait for the Lord and keep his way",
    ),
    (
        re.compile(r"\bhymn Lord\b"),
        "hymn the Lord",
    ),
    (
        re.compile(r"(?<![Tt]he )\bLord his God was with him\b"),
        "the Lord his God was with him",
    ),
    (
        re.compile(r"\bLord helper to me\b"),
        "The Lord is helper to me",
    ),
    (
        re.compile(r"\bLord righteous cut\b"),
        "The righteous Lord cut",
    ),
    (
        re.compile(r"\bLord guarding little ones\b"),
        "The Lord guards little ones",
    ),
    (
        re.compile(r"\bLord kind to all\b"),
        "The Lord is kind to all",
    ),
    (
        re.compile(r"\bUnless Lord build house\b"),
        "Unless the Lord builds a house",
    ),
    (
        re.compile(r"\bunless the Lord guard city\b"),
        "unless the Lord guards a city",
    ),
    (
        re.compile(r"\bMy strength and my hymn the Lord\b"),
        "The Lord is my strength and my hymn",
    ),
    (
        re.compile(r"\bLord righteous in all his ways\b"),
        "The Lord is righteous in all his ways",
    ),
    (
        re.compile(r"\bMay Lord establish\b"),
        "May the Lord establish",
    ),
    (
        re.compile(r"\bWill Lord accept\b"),
        "Will the Lord accept",
    ),
    (
        re.compile(r"\bIs Lord not in Zion\?"),
        "Is the Lord not in Zion?",
    ),
    (
        re.compile(r"\bIs not Lord among us\?"),
        "Is not the Lord among us?",
    ),
    (
        re.compile(r"\bDisciplining, Lord disciplined me\b"),
        "The Lord disciplined me with discipline",
    ),
    (
        re.compile(r"\bLord tears down houses\b"),
        "The Lord tears down houses",
    ),
    (
        re.compile(r"\bwhich Lord planted\b"),
        "which the Lord planted",
    ),
    (
        re.compile(r"\bLord of heaven has authority\b"),
        "the Lord of heaven has authority",
    ),
    (
        re.compile(r"\brelied on Lord saying\b"),
        "relied on the Lord saying",
    ),
    (
        re.compile(r"\bFor cloud was upon the tent by day\b"),
        "For the cloud was upon the tent by day",
    ),
    (
        re.compile(r'\bbefore all Israel in all their journeys\."'),
        "before all Israel in all their journeys.",
    ),
    (
        re.compile(r"\bthe name of the Lord great to you; place to you will be\b"),
        "the name of the Lord is great to you; a place for you will be",
    ),
    (
        re.compile(r"\bnor will vessel go through\b"),
        "nor will a vessel go through",
    ),
    (
        re.compile(r"\bAnd in first year of Cyrus\b"),
        "And in the first year of Cyrus",
    ),
    (
        re.compile(r"\bfrom mouth of (the Lord|Jeremiah)\b"),
        r"from the mouth of \1",
    ),
    (
        re.compile(r"\b([Ff]rom|[Bb]y) mouth of\b"),
        r"\1 the mouth of",
    ),
    (
        re.compile(r"\bby hand of\b"),
        "by the hand of",
    ),
    (
        re.compile(r"\b([Ii]n|[Ff]rom) days of\b"),
        r"\1 the days of",
    ),
    (
        re.compile(r"\b([Ii]n) land of\b"),
        r"\1 the land of",
    ),
    (
        re.compile(r"\b([Ff]rom|[Ii]nto|[Tt]o|[Oo]nto) land of\b"),
        r"\1 the land of",
    ),
    (
        re.compile(r"\b([Ff]rom|[Ii]nto|[Tt]o) land (which|that|where|about|concerning)\b"),
        r"\1 the land \2",
    ),
    (
        re.compile(r"\binto land dark and gloomy\b"),
        "into a dark and gloomy land",
    ),
    (
        re.compile(r"\binto land like your land\b"),
        "into a land like your land",
    ),
    (
        re.compile(r"\binto land whose bars\b"),
        "into a land whose bars",
    ),
    (
        re.compile(r"\b([Ff]rom|[Ii]nto|[Tt]o|[Ii]n) city of\b"),
        r"\1 the city of",
    ),
    (
        re.compile(r"\b([Ff]rom|[Ii]nto|[Tt]o|[Ii]n|[Oo]n) mountain of\b"),
        r"\1 the mountain of",
    ),
    (
        re.compile(r"\b([Ff]rom|[Tt]o|[Bb]efore) sons of\b"),
        r"\1 the sons of",
    ),
    (
        re.compile(r"\b([Ff]rom|[Tt]o) daughters of\b"),
        r"\1 the daughters of",
    ),
    (
        re.compile(r"\b([Ii]n) cities of\b"),
        r"\1 the cities of",
    ),
    (
        re.compile(r"\b([Ff]rom) all cities of\b"),
        r"\1 all the cities of",
    ),
    (
        re.compile(r"\b([Aa]gainst) cities of\b"),
        r"\1 the cities of",
    ),
    (
        re.compile(r"\b([Aa]gainst) inhabitants of\b"),
        r"\1 the inhabitants of",
    ),
    (
        re.compile(r"\b([Tt]o) king of\b"),
        r"\1 the king of",
    ),
    (
        re.compile(r"\b([Aa]gainst) king of\b"),
        r"\1 the king of",
    ),
    (
        re.compile(r"\b([Tt]o) queen of\b"),
        r"\1 the queen of",
    ),
    (
        re.compile(r"\b([Ff]rom) people of\b"),
        r"\1 the people of",
    ),
    (
        re.compile(r"\b([Ff]rom) peoples of\b"),
        r"\1 the peoples of",
    ),
    (
        re.compile(r"\b([Uu]pon) sons of\b"),
        r"\1 the sons of",
    ),
    (
        re.compile(r"\b([Oo]ver) sons of\b"),
        r"\1 the sons of",
    ),
    (
        re.compile(r"\b([Tt]o) all sons of\b"),
        r"\1 all the sons of",
    ),
    (
        re.compile(r"\b([Tt]o) all people of\b"),
        r"\1 all the people of",
    ),
    (
        re.compile(r"\b([Tt]o) all house of\b"),
        r"\1 all the house of",
    ),
    (
        re.compile(r"\b([Ii]n) valley of\b"),
        r"\1 the valley of",
    ),
    (
        re.compile(r"\b([Tt]o) man of God\b"),
        r"\1 the man of God",
    ),
    (
        re.compile(r"\b([Bb]efore|[Ff]rom|[Tt]oward|[Ii]n|[Ii]nto) temple of\b"),
        r"\1 the temple of",
    ),
    (
        re.compile(r"\b([Uu]pon|[Oo]n|[Bb]efore|[Tt]o) altar of\b"),
        r"\1 the altar of",
    ),
    (
        re.compile(r"\b([Bb]efore) ark of\b"),
        r"\1 the ark of",
    ),
    (
        re.compile(r"\b([Ff]rom) tribe of\b"),
        r"\1 the tribe of",
    ),
    (
        re.compile(r"\b([Bb]efore) face of\b"),
        r"\1 the face of",
    ),
    (
        re.compile(r"\b([Ii]n) house of the Lord\b"),
        r"\1 the house of the Lord",
    ),
    (
        re.compile(r"\bfrom man even to woman\b"),
        "from man to woman",
    ),
    (
        re.compile(r"\bWord of (the Lord|God)\b"),
        r"The word of \1",
    ),
    (
        re.compile(r"\bWords of the Lord\b"),
        "The words of the Lord",
    ),
    (
        re.compile(r"\b([Ii]n|[Ff]rom|[Ii]nto|[Tt]hrough|[Aa]mong) midst of\b"),
        r"\1 the midst of",
    ),
    (
        re.compile(r"\bGod in the midst of\b"),
        "God is in the midst of",
    ),
    (
        re.compile(r"\bbefore eyes of\b"),
        "before the eyes of",
    ),
    (
        re.compile(r"\b([Ff]rom) day when\b"),
        r"\1 the day when",
    ),
    (
        re.compile(r"\bfrom day they\b"),
        "from the day they",
    ),
    (
        re.compile(r"\b([Uu]ntil) day (he|of)\b"),
        r"\1 the day \2",
    ),
    (
        re.compile(r"\b([Oo]n) day (you|when|of|they|he|she|I)\b"),
        r"\1 the day \2",
    ),
    (
        re.compile(r"\b([Ii]n) day of\b"),
        r"\1 the day of",
    ),
    (
        re.compile(r"\b([Ii]n) time of\b"),
        r"\1 the time of",
    ),
    (
        re.compile(r"\bfrom beginning\b"),
        "from the beginning",
    ),
    (
        re.compile(r"\b(people|inhabitants|sons) of land\b"),
        r"\1 of the land",
    ),
    (
        re.compile(r"\bPeople of land\b"),
        "People of the land",
    ),
    (
        re.compile(r"\b([Tt]o|[Ii]nto|[Ff]rom|[Ii]n|[Bb]efore|[Aa]gainst|[Oo]ver|[Ff]or|[Cc]oncerning) house of\b"),
        r"\1 the house of",
    ),
    (
        re.compile(r"\b([Tt]o) (build|repair) house of\b"),
        r"\1 \2 the house of",
    ),
    (
        re.compile(r"\b([Uu]pon) house of\b"),
        r"\1 the house of",
    ),
    (
        re.compile(r"\b([Ii]nside) house of\b"),
        r"\1 the house of",
    ),
    (
        re.compile(r"\b([Ii]n) houses of\b"),
        r"\1 the houses of",
    ),
    (
        re.compile(r"\b([Bb]y|[Aa]ccording to) houses of\b"),
        r"\1 the houses of",
    ),
    (
        re.compile(r"\b([Ii]n) chambers of\b"),
        r"\1 the chambers of",
    ),
    (
        re.compile(r"\b([Oo]f) house of\b"),
        r"\1 the house of",
    ),
    (
        re.compile(r"\bhouse of king\b"),
        "house of the king",
    ),
    (
        re.compile(r"\b([Bb]y) river\b"),
        r"\1 the river",
    ),
    (
        re.compile(r"\b([Ii]n) heart of\b"),
        r"\1 the heart of",
    ),
    (
        re.compile(r"\bheart of sea\b"),
        "heart of the sea",
    ),
    (
        re.compile(r"\bset your heart as heart of god\b"),
        "set your heart as the heart of a god",
    ),
    (
        re.compile(r"\b([Ff]rom|[Oo]n|[Uu]pon) face of\b"),
        r"\1 the face of",
    ),
    (
        re.compile(r"\buncover face of\b"),
        "uncover the face of",
    ),
    (
        re.compile(r"\b([Oo]ver) face of\b"),
        r"\1 the face of",
    ),
    (
        re.compile(r"\bmake atonement to face of your God\b"),
        "make atonement before the face of your God",
    ),
    (
        re.compile(r"\b([Ii]n|[Ff]rom|[Tt]o|[Oo]n) wall of\b"),
        r"\1 the wall of",
    ),
    (
        re.compile(r"\bwidth of wall\b"),
        "width of the wall",
    ),
    (
        re.compile(r"\b([Uu]pon|[Oo]ver|[Oo]n) head of\b"),
        r"\1 the head of",
    ),
    (
        re.compile(r"\b([Oo]n|[Uu]pon|[Ii]n) seat of\b"),
        r"\1 the seat of",
    ),
    (
        re.compile(r"\b([Bb]efore|[Ff]rom|[Ii]n) tent of\b"),
        r"\1 the tent of",
    ),
    (
        re.compile(r"\b([Ii]n) eyes of\b"),
        r"\1 the eyes of",
    ),
    (
        re.compile(r"\b([Ii]n|[Ii]nto) ears of\b"),
        r"\1 the ears of",
    ),
    (
        re.compile(r"\b([Ff]rom) root of\b"),
        r"\1 the root of",
    ),
    (
        re.compile(r"\b([Tt]o|[Ff]rom) top of\b"),
        r"\1 the top of",
    ),
    (
        re.compile(r"\b([Aa]t|[Ff]rom) corner of\b"),
        r"\1 the corner of",
    ),
    (
        re.compile(r"\bcorner of house\b"),
        "corner of the house",
    ),
    (
        re.compile(r"\b([Ii]n|[Tt]hrough) middle of\b"),
        r"\1 the middle of",
    ),
    (
        re.compile(r"\bmiddle of tent\b"),
        "middle of the tent",
    ),
    (
        re.compile(r"\bmiddle of portion\b"),
        "middle of the portion",
    ),
    (
        re.compile(r"\b([Ff]rom|[Ii]n|[Aa]t) entrance of\b"),
        r"\1 the entrance of",
    ),
    (
        re.compile(r"\bentrance of new gate\b"),
        "entrance of the new gate",
    ),
    (
        re.compile(r"\bentrance of sea\b"),
        "entrance of the sea",
    ),
    (
        re.compile(r"\b([Tt]o|[Ff]rom) door of\b"),
        r"\1 the door of",
    ),
    (
        re.compile(r"\bdoor of furnace\b"),
        "door of the furnace",
    ),
    (
        re.compile(r"\b([Ff]rom|[Ii]n|[Ii]nto|[Oo]ver|[Aa]gainst) hand of\b"),
        r"\1 the hand of",
    ),
    (
        re.compile(r"\b([Ii]n|[Ii]nto|[Ff]rom|[Bb]y) hands of\b"),
        r"\1 the hands of",
    ),
    (
        re.compile(r"\b([Uu]pon|[Tt]o|[Ii]nto) heart of\b"),
        r"\1 the heart of",
    ),
    (
        re.compile(r"\b([Aa]t|[Bb]y|[Ff]rom|[Tt]o|[Tt]hrough|[Ii]n) gate of\b"),
        r"\1 the gate of",
    ),
    (
        re.compile(r"\bgate of city\b"),
        "gate of the city",
    ),
    (
        re.compile(r"\b([Ii]n|[Ff]rom|[Tt]o|[Ii]nto) court of\b"),
        r"\1 the court of",
    ),
    (
        re.compile(r"\b([Ii]n) courts of\b"),
        r"\1 the courts of",
    ),
    (
        re.compile(r"\bcourt of prison\b"),
        "court of the prison",
    ),
    (
        re.compile(r"\b([Oo]n|[Uu]pon) throne of\b"),
        r"\1 the throne of",
    ),
    (
        re.compile(r"\b([Ii]n|[Oo]n|[Tt]o|[Ii]nto) mouth of\b"),
        r"\1 the mouth of",
    ),
    (
        re.compile(r"\bmouth of den\b"),
        "mouth of the den",
    ),
    (
        re.compile(r"\bmouth of eater\b"),
        "mouth of the eater",
    ),
    (
        re.compile(r"\bto keep his commandments and his testimonies and his ordinances with all heart and with all soul\b"),
        "to keep his commandments and his testimonies and his ordinances with all his heart and with all his soul",
    ),
    (
        re.compile(r"\bto keep his commandments and his testimonies and his ordinances with all heart and with all soul, words of covenant\b"),
        "to keep his commandments and his testimonies and his ordinances with all his heart and with all his soul, words of covenant",
    ),
    (
        re.compile(r"\bwere playing before God with all strength\b"),
        "were playing before God with all their strength",
    ),
    (
        re.compile(r"\bturn toward you with all heart and all soul\b"),
        "turn toward you with all their heart and all their soul",
    ),
    (
        re.compile(r"\bwith all soul they swore and with all desire sought him\b"),
        "with all their soul they swore and with all their desire sought him",
    ),
    (
        re.compile(r"\bthe Lord stirred spirit of Cyrus\b"),
        "the Lord stirred the spirit of Cyrus",
    ),
    (
        re.compile(r"\ball kingdoms of earth\b"),
        "all kingdoms of the earth",
    ),
    (
        re.compile(r"\ball earth\b"),
        "all the earth",
    ),
    (
        re.compile(r"\bAll earth\b"),
        "All the earth",
    ),
    (
        re.compile(r"\btheir fall earth was shaken\b"),
        "their fall, earth was shaken",
    ),
    (
        re.compile(r"\b([Ff]rom) sound of\b"),
        r"\1 the sound of",
    ),
    (
        re.compile(r"\b([Aa]t) sound of\b"),
        r"\1 the sound of",
    ),
    (
        re.compile(r"\bheard in sea\b"),
        "heard in the sea",
    ),
    (
        re.compile(r"\bfrom breast\b"),
        "from the breast",
    ),
    (
        re.compile(r"\bfrom breasts of\b"),
        "from the breasts of",
    ),
    (
        re.compile(r"\b([Ff]rom) (seed|elders|voice|fruits|abundance|springs|captivity|multitude) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Tt]o) seed of\b"),
        r"\1 the seed of",
    ),
    (
        re.compile(r"\b([Ff]rom) (edge|rising|womb|belly|fat|fruit|wages|way|glory|east|possession) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ff]rom) (half tribe|mountains|brothers|borders|chiefs|country|depths|height) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ff]rom) (affliction|snare|produce|king|cities|islands|wrath|dust|mount|sight|men) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ff]rom) birds of\b"),
        r"\1 the birds of",
    ),
    (
        re.compile(r"\b([Ff]rom) all tribes of\b"),
        r"\1 all the tribes of",
    ),
    (
        re.compile(r"\b([Aa]t) threshing floor of\b"),
        r"\1 the threshing floor of",
    ),
    (
        re.compile(r"\bin upper court\b"),
        "in the upper court",
    ),
    (
        re.compile(r"\bin fire of\b"),
        "in the fire of",
    ),
    (
        re.compile(r"\b([Ii]n) (law|works|strength|gates|shelter|light|name|vision) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]n) (year|depth|hidden place|blood|tents|places) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]n) (holy things|clouds|uprightness|commandments|broad place|heat|pillar|path|counsel|mercy|shadow|depths|innocence) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]n) (acts|abundance|gathering|council|ways|womb|dark place|glory|prophets|paradise|desires|sons|scroll words) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\bin streets of\b"),
        "in the streets of",
    ),
    (
        re.compile(r"\b([Aa]t) (end|gates|completion|time|head) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]n) feast of\b"),
        r"\1 the feast of",
    ),
    (
        re.compile(r"\bin book of\b"),
        "in the book of",
    ),
    (
        re.compile(r"\bupon book of\b"),
        "upon the book of",
    ),
    (
        re.compile(r"\bin words of\b"),
        "in the words of",
    ),
    (
        re.compile(r"\bto words of\b"),
        "to the words of",
    ),
    (
        re.compile(r"\b([Tt]o) (voice|number|birds|beasts|remnant|forecourt|chiefs|prayer|counsel) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Tt]o) (bring up|carry) ark of\b"),
        r"\1 \2 the ark of",
    ),
    (
        re.compile(r"\b([Tt]o) (enter|strengthen) house of\b"),
        r"\1 \2 the house of",
    ),
    (
        re.compile(r"\b([Tt]o) turn kingdom of\b"),
        r"\1 turn the kingdom of",
    ),
    (
        re.compile(r"\b([Tt]o) (valley|ordinance|judgment|sins) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Tt]o) (men|abundance|elders|people|ruler|cities|generations|measures|length) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Tt]o) end of\b"),
        r"\1 the end of",
    ),
    (
        re.compile(r"\b([Tt]o) destroy race of\b"),
        r"\1 destroy the race of",
    ),
    (
        re.compile(r"\b([Tt]o) whom word of\b"),
        r"\1 whom the word of",
    ),
    (
        re.compile(r"\b([Tt]o) hear voice of\b"),
        r"\1 hear the voice of",
    ),
    (
        re.compile(r"\b([Tt]o) the all beasts of\b"),
        r"\1 all the beasts of",
    ),
    (
        re.compile(r"\b([Tt]o) all beasts of\b"),
        r"\1 all the beasts of",
    ),
    (
        re.compile(r"\b([Tt]o) (rulers|ends|servant|daughter) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Tt]o) celebrate feast of\b"),
        r"\1 celebrate the feast of",
    ),
    (
        re.compile(r"\b([Tt]o) all army of\b"),
        r"\1 all the army of",
    ),
    (
        re.compile(r"\b([Aa]t) voice of\b"),
        r"\1 the voice of",
    ),
    (
        re.compile(r"\b([Ww]ith) (sons|voice|words|weapons|instruments|beasts|rulers|house|servants|peoples|oil|strength|shame|assembly|fat) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ww]ith) (wounded|beauty|fullness|wife|vengeance) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ww]ith) (blood|blessing|produce|leaders|scarcity|water) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Aa]ccording to) (number|works|word|writing|counsel) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Aa]ccording to) (matter|abundance|likeness|anger|measures) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Aa]ccording to) purity of\b"),
        r"\1 the purity of",
    ),
    (
        re.compile(r"\b([Uu]pon) prayer of\b"),
        r"\1 the prayer of",
    ),
    (
        re.compile(r"\bin way of\b"),
        "in the way of",
    ),
    (
        re.compile(r"\bIn way of\b"),
        "In the way of",
    ),
    (
        re.compile(r"\bin ways of\b"),
        "in the ways of",
    ),
    (
        re.compile(r"\bin sight of\b"),
        "in the sight of",
    ),
    (
        re.compile(r"\b([Bb]y) spirit of\b"),
        r"\1 the spirit of",
    ),
    (
        re.compile(r"\b([Ff]rom) tower of\b"),
        r"\1 the tower of",
    ),
    (
        re.compile(r"\b([Oo]n) (land|tops) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Oo]n|[Uu]pon) (borders|road|house|ascent|beasts|way) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Oo]n) (breadth|corner|bank|furrows) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Oo]ver) men of\b"),
        r"\1 the men of",
    ),
    (
        re.compile(r"\b([Bb]y) sword of\b"),
        r"\1 the sword of",
    ),
    (
        re.compile(r"\b([Bb]y) (number|words) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Bb]y) (command|decree|name|king|strength|works) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Uu]pon) ways of\b"),
        r"\1 the ways of",
    ),
    (
        re.compile(r"\b([Uu]pon) (words|kingdom|bed|inhabitants) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Uu]nder) hand of\b"),
        r"\1 the hand of",
    ),
    (
        re.compile(r"\b([Uu]nder) yoke of\b"),
        r"\1 the yoke of",
    ),
    (
        re.compile(r"\b([Oo]ver) (works|treasuries|crushing|affairs) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Oo]ver) to souls of\b"),
        r"\1 to the souls of",
    ),
    (
        re.compile(r"\b([Ii]nto) (depth|chamber) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]nto) (depths|kingdom) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]nto) (holy|wilderness|torrent|treasury|pit|valley) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]nto) (cities|storerooms|foundations|bosom) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]n) kingdom of\b"),
        r"\1 the kingdom of",
    ),
    (
        re.compile(r"\b([Aa]gainst) kingdom of\b"),
        r"\1 the kingdom of",
    ),
    (
        re.compile(r"\b([Aa]gainst) land of\b"),
        r"\1 the land of",
    ),
    (
        re.compile(r"\b([Aa]gainst) sons of\b"),
        r"\1 the sons of",
    ),
    (
        re.compile(r"\b([Aa]fter) (end|death|wife) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Aa]fter) (thoughts|pleasures) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Bb]efore) king of\b"),
        r"\1 the king of",
    ),
    (
        re.compile(r"\b([Tt]hrough) broad place of\b"),
        r"\1 the broad place of",
    ),
    (
        re.compile(r"\b([Tt]hrough) generations of\b"),
        r"\1 the generations of",
    ),
    (
        re.compile(r"\b([Aa]t) right of\b"),
        r"\1 the right of",
    ),
    (
        re.compile(r"\b([Uu]pon) son of\b"),
        r"\1 the son of",
    ),
    (
        re.compile(r"\b([Oo]n|[Uu]pon) (walls|wings|heads) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Uu]pon) (wings|valley) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Tt]hrough) gates of\b"),
        r"\1 the gates of",
    ),
    (
        re.compile(r"\b([Tt]o) word of\b"),
        r"\1 the word of",
    ),
    (
        re.compile(r"\b([Ii]n) writing of\b"),
        r"\1 the writing of",
    ),
    (
        re.compile(r"\bin multitude of\b"),
        "in the multitude of",
    ),
    (
        re.compile(r"\bIn multitude of\b"),
        "In the multitude of",
    ),
    (
        re.compile(r"\bto multitude of\b"),
        "to the multitude of",
    ),
    (
        re.compile(r"\bby command of\b"),
        "by the command of",
    ),
    (
        re.compile(r"\baccording to command of\b"),
        "according to the command of",
    ),
    (
        re.compile(r"\bto command of\b"),
        "to the command of",
    ),
    (
        re.compile(r"\bin assembly of\b"),
        "in the assembly of",
    ),
    (
        re.compile(r"\bin plain of\b"),
        "in the plain of",
    ),
    (
        re.compile(r"\bat beginning of\b"),
        "at the beginning of",
    ),
    (
        re.compile(r"\bAt beginning of\b"),
        "At the beginning of",
    ),
    (
        re.compile(r"\bin reign of\b"),
        "in the reign of",
    ),
    (
        re.compile(r"\bon mountains of\b"),
        "on the mountains of",
    ),
    (
        re.compile(r"\bupon mountains of\b"),
        "upon the mountains of",
    ),
    (
        re.compile(r"\bUpon mountains of\b"),
        "Upon the mountains of",
    ),
    (
        re.compile(r"\bover land of\b"),
        "over the land of",
    ),
    (
        re.compile(r"\bupon land of\b"),
        "upon the land of",
    ),
    (
        re.compile(r"\bland of north\b"),
        "land of the north",
    ),
    (
        re.compile(r"\bland of life\b"),
        "land of the living",
    ),
    (
        re.compile(r"\bface of sword\b"),
        "face of the sword",
    ),
    (
        re.compile(r"\bWho measured water with hand and heaven with span, and who set all the earth by handful\? Who set mountains with scale and glens with balance\?"),
        "Who measured water with his hand and heaven with a span, and who set all the earth with a handful? Who set mountains with a scale and glens with a balance?",
    ),
    (
        re.compile(r"\bwith balance and with bag of deceitful weights\b"),
        "with a balance and with a bag of deceitful weights",
    ),
    (
        re.compile(r"\bbuild for him house in Jerusalem\b"),
        "build for him a house in Jerusalem",
    ),
    (
        re.compile(r"\bBlessed your men; blessed these servants\b"),
        "Blessed are your men; blessed are these servants",
    ),
    (
        re.compile(r"\bBlessed man (who|to whom|whose|whom|doing)\b"),
        r"Blessed is the man \1",
    ),
    (
        re.compile(r"\bBlessed man fearing Lord\b"),
        "Blessed is the man fearing the Lord",
    ),
    (
        re.compile(r"\bBlessed nation whose\b"),
        "Blessed is the nation whose",
    ),
    (
        re.compile(r"\bBlessed one (understanding|whom|coming)\b"),
        r"Blessed is the one \1",
    ),
    (
        re.compile(r"\bBlessed one having\b"),
        "Blessed is the one having",
    ),
    (
        re.compile(r"\bBlessed those\b"),
        "Blessed are those",
    ),
    (
        re.compile(r"\bBlessed people knowing\b"),
        "Blessed are the people knowing",
    ),
    (
        re.compile(r"\bBlessed you by Lord\b"),
        "Blessed are you by the Lord",
    ),
    (
        re.compile(r"\bBlessed who will\b"),
        "Blessed is the one who will",
    ),
    (
        re.compile(r"\bBlessed is one remaining\b"),
        "Blessed is the one remaining",
    ),
    (
        re.compile(r"\bBlessed whose helper God of Jacob\b"),
        "Blessed is he whose helper is the God of Jacob",
    ),
    (
        re.compile(r"\bBlessed God,"),
        "Blessed be God,",
    ),
    (
        re.compile(r"\bBlessed God\."),
        "Blessed be God.",
    ),
    (
        re.compile(r"\bBlessed be Lord\b"),
        "Blessed be the Lord",
    ),
    (
        re.compile(r"\bBlessed soul, every simple one; but hot-tempered man unseemly\."),
        "Every simple soul is blessed, but a hot-tempered man is unseemly.",
    ),
    (
        re.compile(r"\bBlessed are you, land whose king son of nobles\b"),
        "Blessed are you, land whose king is son of nobles",
    ),
    (
        re.compile(r"\b([Ee]nds?|[Ff]ace|[Ss]urface) of earth\b"),
        r"\1 of the earth",
    ),
    (
        re.compile(r"\b([Ff]rom|[Tt]o|[Aa]t) (end|ends|face|surface) of the earth\b"),
        r"\1 the \2 of the earth",
    ),
    (
        re.compile(r"\b([Ii]n) (first|second|third|fourth|eighth|twelfth) year\b"),
        r"\1 the \2 year",
    ),
    (
        re.compile(r"\b([Ii]n) (first|second|third|fourth|fifth|sixth|eighth|ninth|tenth|twelfth) month\b"),
        r"\1 the \2 month",
    ),
    (
        re.compile(r"\bof (first|second|third|fourth|fifth|sixth|eighth|ninth|tenth|twelfth) month\b"),
        r"of the \1 month",
    ),
    (
        re.compile(r"\bof month\b"),
        "of the month",
    ),
    (
        re.compile(r"\b([Oo]n|[Ff]rom) first day\b"),
        r"\1 the first day",
    ),
    (
        re.compile(r"\b([Oo]n) (first|fifth|tenth|thirteenth|fourteenth|fifteenth) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Aa]t) (forecourt|last) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Aa]t) doors of\b"),
        r"\1 the doors of",
    ),
    (
        re.compile(r"\b([Aa]t) water of\b"),
        r"\1 the water of",
    ),
    (
        re.compile(r"\b([Ii]n) (eighteenth|thirty-eighth) year of\b"),
        r"\1 the \2 year of",
    ),
    (
        re.compile(r"\b([Oo]n|[Uu]ntil) (eighth|sixteenth|last) day\b"),
        r"\1 the \2 day",
    ),
    (
        re.compile(r"\bholy your temple\b"),
        "holy is your temple",
    ),
    (
        re.compile(r"\bwithout Lord to war\b"),
        "without the Lord to war",
    ),
    (
        re.compile(r"\bfearing Lord hoped on Lord\b"),
        "fearing the Lord hoped on the Lord",
    ),
    (
        re.compile(r"\bI foresaw Lord before me\b"),
        "I foresaw the Lord before me",
    ),
    (
        re.compile(r"\bLord strong and mighty, Lord mighty in war\b"),
        "The Lord, strong and mighty; the Lord, mighty in war",
    ),
    (re.compile(r"\b(Seek|seek|Seeking|seeking|Sought|sought) Lord\b"), r"\1 the Lord"),
    (re.compile(r"\b(upon|toward|before|from|to|with|through|against|in) Lord\b"), r"\1 the Lord"),
)
DEDUPED_LORD_ARTICLE_RE = re.compile(r"\b([Tt])he [Tt]he Lord\b")


def _previous_word(text: str, index: int) -> str:
    match = PREVIOUS_WORD_RE.search(text[:index].rstrip())
    return match.group(0).lower() if match else ""


def _article_for_position(text: str, index: int) -> str:
    prefix = text[:index].rstrip()
    if not prefix or prefix[-1] in ".?!;:([":
        return "The"
    return "the"


def normalize_lord_articles(text: str) -> tuple[str, int]:
    changes = 0

    def construct_repl(match: re.Match[str]) -> str:
        nonlocal changes
        if _previous_word(text, match.start()) in CONSTRUCT_SKIP_PREVIOUS:
            return match.group(0)
        changes += 1
        return f"{_article_for_position(text, match.start())} {match.group(0)}"

    updated = CONSTRUCT_RE.sub(construct_repl, text)

    for pattern, replacement in LORD_OBJECT_REPLACEMENTS:
        updated, count = pattern.subn(replacement, updated)
        changes += count

    def bare_lord_repl(match: re.Match[str]) -> str:
        nonlocal changes
        changes += 1
        return f"{_article_for_position(updated, match.start())} Lord "

    updated = BARE_LORD_RE.sub(bare_lord_repl, updated)
    while True:
        updated, count = DEDUPED_LORD_ARTICLE_RE.subn(
            lambda match: f"{'T' if match.group(1) == 'T' else 't'}he Lord",
            updated,
        )
        changes += count
        if not count:
            break
    return updated, changes


def update_csv(path: Path, columns: tuple[str, ...]) -> int:
    rows = load_csv(path)
    updates = 0
    for row in rows:
        for column in columns:
            value = row.get(column, "")
            if not value:
                continue
            updated, count = normalize_lord_articles(value)
            if count and updated != value:
                row[column] = updated
                updates += count
    if updates:
        write_csv(path, rows, lineterminator="\n")
    return updates


def main() -> None:
    counts = {
        "source_updates": update_csv(OT_SOURCE, ("draft_translation",)),
        "decision_updates": update_csv(DECISIONS, ("chosen_rendering", "alternate_renderings")),
        "footnote_updates": update_csv(FOOTNOTES, ("trigger_phrase",)),
    }
    print(counts)


if __name__ == "__main__":
    main()
