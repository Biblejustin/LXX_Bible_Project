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
    r"(?<![Tt]he )(?<!my )(?<!your )(?<!our )(?<!his )(?<!their )(?<!good )(?<!great )\bLord "
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
        re.compile(r"\bis breath of life\b"),
        "is the breath of life",
    ),
    (
        re.compile(r"\bis spirit of life\b"),
        "is the spirit of life",
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
        re.compile(r"\bVoice of the Lord upon waters\b"),
        "The voice of the Lord is upon waters",
    ),
    (
        re.compile(r"\bVoice of the Lord in strength\b"),
        "The voice of the Lord is in strength",
    ),
    (
        re.compile(r"\bThe voice of the Lord in strength\b"),
        "The voice of the Lord is in strength",
    ),
    (
        re.compile(r"\bVoice of the Lord\b"),
        "The voice of the Lord",
    ),
    (
        re.compile(r"\bVoice of exultation and salvation\b"),
        "The voice of exultation and salvation",
    ),
    (
        re.compile(r"\bvoice of rejoicing and voice of gladness, voice of bridegroom and voice of bride\b"),
        "the voice of rejoicing and the voice of gladness, the voice of bridegroom and the voice of bride",
    ),
    (
        re.compile(r"\bvoice of joy and voice of gladness, voice of bridegroom and voice of bride\b"),
        "the voice of joy and the voice of gladness, the voice of bridegroom and the voice of bride",
    ),
    (
        re.compile(r"^voice of gladness and voice of joy, voice of bridegroom and voice of bride, voice of those saying\b"),
        "The voice of gladness and the voice of joy, the voice of bridegroom and the voice of bride, the voice of those saying",
    ),
    (
        re.compile(r"\bSound of\b"),
        "The sound of",
    ),
    (
        re.compile(r"\bpursuing horse and jolting chariot\b"),
        "a pursuing horse and a jolting chariot",
    ),
    (
        re.compile(r"\band sound of\b"),
        "and the sound of",
    ),
    (
        re.compile(r"\bsound of lions\b"),
        "the sound of lions",
    ),
    (
        re.compile(r"\bvoice of the Lord in magnificence\b"),
        "the voice of the Lord is in magnificence",
    ),
    (
        re.compile(r"\bFear of the Lord pure\b"),
        "The fear of the Lord is pure",
    ),
    (
        re.compile(r"\bFear of the Lord\b"),
        "The fear of the Lord",
    ),
    (
        re.compile(r"\bBeginning of wisdom the fear of the Lord\b"),
        "The beginning of wisdom is the fear of the Lord",
    ),
    (
        re.compile(r"\bWorks of his hands\b"),
        "The works of his hands",
    ),
    (
        re.compile(r"\bHeart of\b"),
        "The heart of",
    ),
    (
        re.compile(r"\bLips of\b"),
        "The lips of",
    ),
    (
        re.compile(r"\bright hand of the Lord\b"),
        "the right hand of the Lord",
    ),
    (
        re.compile(r"\bRight hand of the Lord\b"),
        "The right hand of the Lord",
    ),
    (
        re.compile(r"\bdid mighty deed\b"),
        "did a mighty deed",
    ),
    (
        re.compile(r"\bHand of choice ones will rule easily\b"),
        "The hand of choice ones will rule easily",
    ),
    (
        re.compile(r"\bAnd spirit of God clothed Azariah\b"),
        "And the Spirit of God clothed Azariah",
    ),
    (
        re.compile(r"\bAnd Spirit of God will rest upon him, spirit of wisdom\b"),
        "And the Spirit of God will rest upon him, a spirit of wisdom",
    ),
    (
        re.compile(r"\bin Spirit of God\b"),
        "in the Spirit of God",
    ),
    (
        re.compile(r"\babove people and said\b"),
        "above the people and said",
    ),
    (
        re.compile(r"\btransgress commandments of the Lord\b"),
        "transgress the commandments of the Lord",
    ),
    (
        re.compile(r"\bBecause you forsake Lord, he will forsake you\b"),
        "Because you forsake the Lord, he will forsake you",
    ),
    (
        re.compile(r"(?<!the )\bglory of the Lord filled house\b"),
        "the glory of the Lord filled the house",
    ),
    (
        re.compile(r"(?<!the )\bremnant of Israel were\b"),
        "the remnant of Israel were",
    ),
    (
        re.compile(r"(?<!the )\bhouse of the Lord was full of glory\b"),
        "the house of the Lord was full of glory",
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
        re.compile(r"\b([Ff]rom|[Ii]nto|[Tt]o|[Oo]nto|[Tt]oward) land of\b"),
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
        re.compile(r"\b([Ff]or|[Cc]oncerning) sons of\b"),
        r"\1 the sons of",
    ),
    (
        re.compile(r"\b([Tt]o) son of man\b"),
        r"\1 a son of man",
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
        re.compile(r"\b([Bb]efore|[Ff]rom|[Tt]oward|[Ii]n|[Ii]nto) temple\b"),
        r"\1 the temple",
    ),
    (
        re.compile(r"\b([Ee]ntered) temple\b"),
        r"\1 the temple",
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
        re.compile(r"\bin ark of\b"),
        "in the ark of",
    ),
    (
        re.compile(r"\b([Ff]rom) tribe of\b"),
        r"\1 the tribe of",
    ),
    (
        re.compile(r"\b([Ii]nto) tribe of\b"),
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
        re.compile(r"\b(build(?:ing)?|built) house of\b"),
        r"\1 the house of",
    ),
    (
        re.compile(r"\b(build(?:ing)?|built) house that\b"),
        r"\1 the house that",
    ),
    (
        re.compile(r"\b(build(?:ing)?|built) house (for|to) (God|the Lord|my name|his name|your holy name|himself|herself|you)\b"),
        r"\1 a house \2 \3",
    ),
    (
        re.compile(r"\b(build(?:ing)?|built) house to the name\b"),
        r"\1 a house to the name",
    ),
    (
        re.compile(r"\band house for his kingdom\b"),
        "and a house for his kingdom",
    ),
    (
        re.compile(r"\bpassing through city from city in\b"),
        "passing from one city to another in",
    ),
    (
        re.compile(r"\bin city and province\b"),
        "in each city and province",
    ),
    (
        re.compile(r"\b(from|into|in|to|through) city\b"),
        r"\1 the city",
    ),
    (
        re.compile(r"\bcame into city\b"),
        "came into the city",
    ),
    (
        re.compile(r"\bentered city\b"),
        "entered the city",
    ),
    (
        re.compile(r"\bopposite city\b"),
        "opposite the city",
    ),
    (
        re.compile(r"\bhappen to city\b"),
        "happen to the city",
    ),
    (
        re.compile(r"\badorn city\b"),
        "adorn the city",
    ),
    (
        re.compile(r"(?<!the )\bcity will be taken\b"),
        "the city will be taken",
    ),
    (
        re.compile(r"\bdwelt in land Uz\b"),
        "dwelt in the land of Uz",
    ),
    (
        re.compile(r"\bin land desert and trackless and waterless\b"),
        "in a desert and trackless and waterless land",
    ),
    (
        re.compile(r"\bin land not (theirs|yours)\b"),
        r"in a land not \1",
    ),
    (
        re.compile(r"\bin land you did not know\b"),
        "in a land you did not know",
    ),
    (
        re.compile(r"\bto land you did not know\b"),
        "to a land you did not know",
    ),
    (
        re.compile(r"\bupon land where\b"),
        "upon a land where",
    ),
    (
        re.compile(r"\bon land where\b"),
        "on a land where",
    ),
    (
        re.compile(r"\bagainst land thrown open\b"),
        "against a land thrown open",
    ),
    (
        re.compile(r"\binto land turned back from sword\b"),
        "into a land turned back from sword",
    ),
    (
        re.compile(r"\bin whole land of Babylon\b"),
        "in the whole land of Babylon",
    ),
    (
        re.compile(r"\btogether with freewill of\b"),
        "together with the freewill offering of",
    ),
    (
        re.compile(r"\bwhole land\b"),
        "the whole land",
    ),
    (
        re.compile(r"\bWhole land\b"),
        "The whole land",
    ),
    (
        re.compile(r"\ball the whole land\b"),
        "all the land",
    ),
    (
        re.compile(r"\ball the(?: the)? whole land\b"),
        "all the land",
    ),
    (
        re.compile(r"\b(in|on|upon|over|from|to|into|through|against) land\b"),
        r"\1 the land",
    ),
    (
        re.compile(r"\bdwelling in land\b"),
        "dwelling in the land",
    ),
    (
        re.compile(r"\bdwell in land\b"),
        "dwell in the land",
    ),
    (
        re.compile(r"\bdwell on land\b"),
        "dwell on the land",
    ),
    (
        re.compile(r"\bdwelling on land\b"),
        "dwelling on the land",
    ),
    (
        re.compile(r"\bdwell upon land\b"),
        "dwell upon the land",
    ),
    (
        re.compile(r"\bdwelling upon land\b"),
        "dwelling upon the land",
    ),
    (
        re.compile(r"\breigned over land\b"),
        "reigned over the land",
    ),
    (
        re.compile(r"\bimposed tribute on land\b"),
        "imposed tribute on the land",
    ),
    (
        re.compile(r"\bcame into land\b"),
        "came into the land",
    ),
    (
        re.compile(r"\bcame up against land\b"),
        "came up against the land",
    ),
    (
        re.compile(r"\bcover land\b"),
        "cover the land",
    ),
    (
        re.compile(r"\bcovering land\b"),
        "covering the land",
    ),
    (
        re.compile(r"\bland will be poor\b"),
        "the land will be poor",
    ),
    (
        re.compile(r"\bcurse will eat land\b"),
        "curse will eat the land",
    ),
    (
        re.compile(r"\bFlowers appeared in land\b"),
        "Flowers appeared in the land",
    ),
    (
        re.compile(r"\bLand with ruin will be ruined and with plunder will be plundered\b"),
        "The land will be ruined with ruin and plundered with plunder",
    ),
    (
        re.compile(r"\bthe(?: the)+ land\b"),
        "the land",
    ),
    (
        re.compile(r"\bWith arrow and bow they will enter there\b"),
        "With an arrow and bow they will enter there",
    ),
    (
        re.compile(r"\bwill be wasteland and thorn\b"),
        "will be a wasteland and thorn",
    ),
    (
        re.compile(r"\bcities of Judah will be built\b"),
        "the cities of Judah will be built",
    ),
    (
        re.compile(r"\ball foundations of earth will be shaken\b"),
        "all foundations of the earth will be shaken",
    ),
    (
        re.compile(r"\bBut light of ungodly will be quenched\b"),
        "But the light of the ungodly will be quenched",
    ),
    (
        re.compile(r"\bcalled city of righteousness\b"),
        "called the city of righteousness",
    ),
    (
        re.compile(r"\bcalled City of Righteousness\b"),
        "called the City of Righteousness",
    ),
    (
        re.compile(r"\bspeaking language of Canaan\b"),
        "speaking the language of Canaan",
    ),
    (
        re.compile(r"\bman supported in trustworthy place will be shaken, and he will fall, and glory upon him will be removed\b"),
        "the man supported in a trustworthy place will be shaken, and he will fall, and the glory upon him will be removed",
    ),
    (
        re.compile(r"\bfrom streets of Jerusalem\b"),
        "from the streets of Jerusalem",
    ),
    (
        re.compile(r"\byet full end I will not make\b"),
        "yet I will not make a full end",
    ),
    (
        re.compile(r"\bbut make no full end\b"),
        "but do not make a full end",
    ),
    (
        re.compile(r"\bI will not make you into full end\b"),
        "I will not make a full end of you",
    ),
    (
        re.compile(r"\bwill be desolation\b"),
        "will be a desolation",
    ),
    (
        re.compile(r"\bbecause no man lays it to heart\b"),
        "because no one lays it to heart",
    ),
    (
        re.compile(r"\bland behind them was made desolate from anyone passing through or returning\b"),
        "the land behind them will be made desolate, with no one passing through or returning",
    ),
    (
        re.compile(r"\bbecame lion\b"),
        "became a lion",
    ),
    (
        re.compile(r"\bbecame reproach\b"),
        "became a reproach",
    ),
    (
        re.compile(r"\bfor all beasts of field\b"),
        "for all beasts of the field",
    ),
    (
        re.compile(r"\bMerchants from nations hissed\b"),
        "Merchants from the nations hissed",
    ),
    (
        re.compile(r"\ball knowing you among nations\b"),
        "all knowing you among the nations",
    ),
    (
        re.compile(r"\bwill be God to family of Israel\b"),
        "will be God to the family of Israel",
    ),
    (
        re.compile(r"\bnumber of sons of Israel was like sand of sea\b"),
        "the number of the sons of Israel was like the sand of the sea",
    ),
    (
        re.compile(r"\bthan sand of seashore\b"),
        "than the sand of the seashore",
    ),
    (
        re.compile(r"\blike sand of seas\b"),
        "like the sand of the seas",
    ),
    (
        re.compile(r"\bpeople Israel become as sand of sea, remnant of them\b"),
        "the people Israel become as the sand of the sea, the remnant of them",
    ),
    (
        re.compile(r"\bbeyond sand of sea\b"),
        "beyond the sand of the sea",
    ),
    (
        re.compile(r"\bagainst mother of young man misery\b"),
        "against the mother of a young man, misery",
    ),
    (
        re.compile(r"\bthey will be called sons of living God\b"),
        "they will be called sons of the living God",
    ),
    (
        re.compile(r"\bmy house will be called house of prayer\b"),
        "my house will be called a house of prayer",
    ),
    (
        re.compile(r"\byou will be called city of the Lord, Zion of Holy One of Israel\b"),
        "you will be called the city of the Lord, Zion of the Holy One of Israel",
    ),
    (
        re.compile(r"\bJerusalem will be called city of truth and mountain of the Lord Almighty, holy mountain\b"),
        "Jerusalem will be called the city of truth and the mountain of the Lord Almighty, a holy mountain",
    ),
    (
        re.compile(r"\bthey will be called border of lawlessness and people against whom\b"),
        "they will be called the border of lawlessness and a people against whom",
    ),
    (
        re.compile(r"\bYou will eat strength of nations\b"),
        "You will eat the strength of nations",
    ),
    (
        re.compile(r"(?<!the )\bstrength of nations\b"),
        "the strength of nations",
    ),
    (
        re.compile(r"\band one rescuing you, he God of Israel, will be called God of all the earth\b"),
        "and the one rescuing you, the God of Israel, will be called the God of all the earth",
    ),
    (
        re.compile(r"\bthe Lord, one rescuing you, Holy One of Israel\b"),
        "the Lord, the one rescuing you, the Holy One of Israel",
    ),
    (
        re.compile(r"\bI am the Lord, one rescuing you and upholding strength of Jacob\b"),
        "I am the Lord, the one rescuing you and upholding the strength of Jacob",
    ),
    (
        re.compile(r"\bsaid the Lord, one rescuing you\b"),
        "said the Lord, the one rescuing you",
    ),
    (
        re.compile(r"\bto find way in which you should walk\b"),
        "to find the way in which you should walk",
    ),
    (
        re.compile(r"\b([Tt]he Lord) stirred spirit of the king of Medes\b"),
        r"\1 stirred the spirit of the king of Medes",
    ),
    (
        re.compile(r"\bbeside gates of\b"),
        "beside the gates of",
    ),
    (
        re.compile(r"\bstrengths of field\b"),
        "strengths of the field",
    ),
    (
        re.compile(r"\bin vineyards of wine\b"),
        "in the vineyards of wine",
    ),
    (
        re.compile(r"\bIn region of Jordan king cast them in thickness of earth\b"),
        "In the region of Jordan the king cast them in the thickness of the earth",
    ),
    (
        re.compile(r"\bwith force of mighty warriors\b"),
        "with a force of mighty warriors",
    ),
    (
        re.compile(r"\bconcerning houses of this city\b"),
        "concerning the houses of this city",
    ),
    (
        re.compile(r"\bin fury of wrath\b"),
        "in a fury of wrath",
    ),
    (
        re.compile(r"\bestablish forever, Lord Almighty, God of Israel\b"),
        "establish forever, O Lord Almighty, God of Israel",
    ),
    (
        re.compile(r"\bLet them say, Lord, Lord Almighty, God of Israel\b"),
        "Let them say, O Lord, Lord Almighty, God of Israel",
    ),
    (
        re.compile(r"\byour name is called upon me, Lord Almighty\b"),
        "your name is called upon me, O Lord Almighty",
    ),
    (
        re.compile(r"\bsaid, Lord Almighty, how long\b"),
        "said, O Lord Almighty, how long",
    ),
    (
        re.compile(r"\bSave us, God of our salvation, and deliver us from nations\b"),
        "Save us, O God of our salvation, and deliver us from the nations",
    ),
    (
        re.compile(r"\bGod of our salvations will make straight way for us\b"),
        "the God of our salvations will make a straight way for us",
    ),
    (
        re.compile(r"; The God of our salvations will make a straight way for us\b"),
        "; the God of our salvations will make a straight way for us",
    ),
    (
        re.compile(r"\bTurn us back, God of our salvations\b"),
        "Turn us back, O God of our salvations",
    ),
    (
        re.compile(r"\bSave us, Lord our God, and gather us from nations\b"),
        "Save us, O Lord our God, and gather us from the nations",
    ),
    (
        re.compile(r"\bto hear prayer which your servant prays\b"),
        "to hear the prayer which your servant prays",
    ),
    (
        re.compile(r"\bLord God, to hear petition and prayer which your servant prays\b"),
        "O Lord God, to hear the petition and the prayer which your servant prays",
    ),
    (
        re.compile(r"\bJerusalem spirit of grace and compassion\b"),
        "Jerusalem a spirit of grace and compassion",
    ),
    (
        re.compile(r"\bfor pasture of camels\b"),
        "for a pasture for camels",
    ),
    (
        re.compile(r"\bfor pasture of sheep\b"),
        "for a pasture for sheep",
    ),
    (
        re.compile(r"\bPlease, Lord God of heaven\b"),
        "Please, O Lord God of heaven",
    ),
    (
        re.compile(r"\brestore judgment in gates\b"),
        "restore judgment in the gates",
    ),
    (
        re.compile(r"\bset aside command of the king\b"),
        "set aside the command of the king",
    ),
    (
        re.compile(r"\bface of whole earth\b"),
        "face of the whole earth",
    ),
    (
        re.compile(r"\blaid waste house of living God because of sins\b"),
        "laid waste the house of the living God because of the sins",
    ),
    (
        re.compile(r"\bhouse of living God\b"),
        "house of the living God",
    ),
    (
        re.compile(r"\bbless living God\b"),
        "bless the living God",
    ),
    (
        re.compile(r"\bbecause of sins of\b"),
        "because of the sins of",
    ),
    (
        re.compile(r"\bfrom herbs of the earth\b"),
        "from the herbs of the earth",
    ),
    (
        re.compile(r"\btime of my release came\b"),
        "the time of my release came",
    ),
    (
        re.compile(r"\bkingdom of your nation is restored\b"),
        "the kingdom of your nation is restored",
    ),
    (
        re.compile(r"\bto God of gods, the great one\b"),
        "to the God of gods, the great one",
    ),
    (
        re.compile(r"\bLatter glory of this house\b"),
        "The latter glory of this house",
    ),
    (
        re.compile(r"\bgreater than first\b"),
        "greater than the first",
    ),
    (
        re.compile(r"\byou forgot law of your God\b"),
        "you forgot the law of your God",
    ),
    (
        re.compile(r"\bcreated all army of heaven\b"),
        "created all the army of heaven",
    ),
    (
        re.compile(r"\ball army of heaven\b"),
        "all the army of heaven",
    ),
    (
        re.compile(r"\bA son honors father\b"),
        "A son honors a father",
    ),
    (
        re.compile(r"\bUnderstanding son keeps law\b"),
        "An understanding son keeps the law",
    ),
    (
        re.compile(r"\bBecause son dishonors\b"),
        "Because a son dishonors",
    ),
    (
        re.compile(r"\bdishonors father\b"),
        "dishonors his father",
    ),
    (
        re.compile(r"\bIf I am father\b"),
        "If I am a father",
    ),
    (
        re.compile(r"\bBecause lips of priest will guard knowledge, and law they will seek\b"),
        "Because the lips of a priest will guard knowledge, and the law they will seek",
    ),
    (
        re.compile(r"\bAnd ravine of my mountains\b"),
        "And the ravine of my mountains",
    ),
    (
        re.compile(r"\band ravine of mountains\b"),
        "and the ravine of mountains",
    ),
    (
        re.compile(r"\bwhat way of spirit\b"),
        "what the way of spirit is",
    ),
    (
        re.compile(r"\bas bones in the womb of pregnant woman\b"),
        "as bones in the womb of a pregnant woman",
    ),
    (
        re.compile(r"\bAnd soul sinning will die\b"),
        "And the soul sinning will die",
    ),
    (
        re.compile(r"\bbut son will not bear injustice of his father, nor father bear injustice of his son\b"),
        "but a son will not bear the injustice of his father, nor a father bear the injustice of his son",
    ),
    (
        re.compile(r"\bRighteousness of righteous one will be upon him, and lawlessness of lawless one will be upon him\b"),
        "The righteousness of a righteous one will be upon him, and the lawlessness of a lawless one will be upon him",
    ),
    (
        re.compile(r"\bRighteousness of righteous one\b"),
        "The righteousness of a righteous one",
    ),
    (
        re.compile(r"\blawlessness of impious one\b"),
        "the lawlessness of an impious one",
    ),
    (
        re.compile(r"\bCyrus the king set decree\b"),
        "Cyrus the king set a decree",
    ),
    (
        re.compile(r"\bset decree for you\b"),
        "set a decree for you",
    ),
    (
        re.compile(r"\bKing Darius set decree\b"),
        "King Darius set a decree",
    ),
    (
        re.compile(r"\bI, Darius, set decree\b"),
        "I, Darius, set a decree",
    ),
    (
        re.compile(r"\bset decree to all treasuries\b"),
        "set a decree to all the treasuries",
    ),
    (
        re.compile(r"\bnot doing law of your God and law of the king\b"),
        "not doing the law of your God and the law of the king",
    ),
    (
        re.compile(r"\bAre you not from the beginning, Lord my God\b"),
        "Are you not from the beginning, O Lord my God",
    ),
    (
        re.compile(r"(?<!O )\bLord, you appointed him for judgment\b"),
        "O Lord, you appointed him for judgment",
    ),
    (
        re.compile(r"\b(?:O ){2,}Lord, you appointed him for judgment\b"),
        "O Lord, you appointed him for judgment",
    ),
    (
        re.compile(r"\bprofane covenant of your fathers\b"),
        "profane the covenant of your fathers",
    ),
    (
        re.compile(r"\bfruit of my womb for sin of my soul\b"),
        "the fruit of my womb for the sin of my soul",
    ),
    (
        re.compile(r"\bWords of Nehemiah son of Hachaliah\b"),
        "The words of Nehemiah son of Hachaliah",
    ),
    (
        re.compile(r"\bin month Chisleu, twentieth year\b"),
        "in the month of Chisleu, in the twentieth year",
    ),
    (
        re.compile(r"\bGates of Jerusalem shall not be opened\b"),
        "The gates of Jerusalem shall not be opened",
    ),
    (
        re.compile(r"(?<!the )(?<!The )\binhabitants of Jerusalem\b"),
        "the inhabitants of Jerusalem",
    ),
    (
        re.compile(r"\bwith face to ground\b"),
        "with his face to the ground",
    ),
    (
        re.compile(r"\brose early in morning\b"),
        "rose early in the morning",
    ),
    (
        re.compile(r"\beveryone understanding to hear\b"),
        "everyone who could understand what they heard",
    ),
    (
        re.compile(r"\band gift of the wood-bearers at appointed times from years and in the firstfruits\b"),
        "and the gift of the wood-bearers at appointed times, year by year, and in the firstfruits",
    ),
    (
        re.compile(r"\bRemember me, our God, for goodness\b"),
        "Remember me, O our God, for goodness",
    ),
    (
        re.compile(r"\bWill you keep ancient path\b"),
        "Will you keep the ancient path",
    ),
    (
        re.compile(r"\bWrath of the king messenger of death, but wise man\b"),
        "The wrath of the king is a messenger of death, but a wise man",
    ),
    (
        re.compile(r"\bbe praised in gates\b"),
        "be praised in the gates",
    ),
    (
        re.compile(r"\bWords of Ecclesiastes\b"),
        "The words of Ecclesiastes",
    ),
    (
        re.compile(r"\bwith all woods of Lebanon\b"),
        "with all the woods of Lebanon",
    ),
    (
        re.compile(r"\bwith all first perfumes\b"),
        "with all the first perfumes",
    ),
    (
        re.compile(r"\blike gazelle or fawn of deer\b"),
        "like a gazelle or a fawn of deer",
    ),
    (
        re.compile(r"\bfrom priests dwelling in Anathoth\b"),
        "from the priests dwelling in Anathoth",
    ),
    (
        re.compile(r"\bjudgment of man before the face of Most High\b"),
        "the judgment of a man before the face of the Most High",
    ),
    (
        re.compile(r"\bin thirtieth year\b"),
        "in the thirtieth year",
    ),
    (
        re.compile(r"\band heavens were opened\b"),
        "and the heavens were opened",
    ),
    (
        re.compile(r"\bstood at the mouth of lions' den\b"),
        "stood at the mouth of the lions' den",
    ),
    (
        re.compile(r"\bBecause ways of the Lord are straight\b"),
        "Because the ways of the Lord are straight",
    ),
    (
        re.compile(r"\bBetween base of altar\b"),
        "Between the base of the altar",
    ),
    (
        re.compile(r"\bSpare, Lord, your people\b"),
        "Spare, O Lord, your people",
    ),
    (
        re.compile(r"\bto reproach for nations\b"),
        "to reproach for the nations",
    ),
    (
        re.compile(r"\bsay among nations\b"),
        "say among the nations",
    ),
    (
        re.compile(r"\bdid not know thought of the Lord\b"),
        "did not know the thought of the Lord",
    ),
    (
        re.compile(r"\blike sheaves of threshing floor\b"),
        "like sheaves of the threshing floor",
    ),
    (
        re.compile(r"\bwill clap hands over you\b"),
        "will clap their hands over you",
    ),
    (
        re.compile(r"\bHabakkuk prophet\b"),
        "Habakkuk the prophet",
    ),
    (
        re.compile(r"\bone building city in bloods and preparing city\b"),
        "one building a city in bloods and preparing a city",
    ),
    (
        re.compile(r"\bIn the second year of Darius king\b"),
        "In the second year of Darius the king",
    ),
    (
        re.compile(r"\bby the hand of Haggai prophet\b"),
        "by the hand of Haggai the prophet",
    ),
    (
        re.compile(r"\bthe great priest\b"),
        "the high priest",
    ),
    (
        re.compile(r"\bIn the eighth month of second year of Darius\b"),
        "In the eighth month of the second year of Darius",
    ),
    (
        re.compile(r"\bbetween you and wife of your youth\b"),
        "between you and the wife of your youth",
    ),
    (
        re.compile(r"\band wife of your covenant\b"),
        "and the wife of your covenant",
    ),
    (
        re.compile(r"\bfrom Syriac book\b"),
        "from the Syriac book",
    ),
    (
        re.compile(r"\bTaking Arabian wife\b"),
        "Taking an Arabian wife",
    ),
    (
        re.compile(r"\bhe fathered son whose name\b"),
        "he fathered a son whose name",
    ),
    (
        re.compile(r"\bone of sons of Esau\b"),
        "one of the sons of Esau",
    ),
    (
        re.compile(r"\bfrom mother Bozrah\b"),
        "from his mother Bozrah",
    ),
    (
        re.compile(r"\bking of sons of Esau from Temanites\b"),
        "king of the sons of Esau from the Temanites",
    ),
    (
        re.compile(r"\btyrant of Sauchites\b"),
        "tyrant of the Sauchites",
    ),
    (
        re.compile(r"\bking of Naamathites\b"),
        "king of the Naamathites",
    ),
    (
        re.compile(r"\bsee limbs of men\b"),
        "see the limbs of the men",
    ),
    (
        re.compile(r"\bwill be spectacle to all flesh\b"),
        "will be a spectacle to all flesh",
    ),
    (
        re.compile(r"\bAnd ration for him was given\b"),
        "And the ration for him was given",
    ),
    (
        re.compile(r"\bWords of Amos\b"),
        "The words of Amos",
    ),
    (
        re.compile(r"\bVision of Obadiah\b"),
        "The vision of Obadiah",
    ),
    (
        re.compile(r"\bmessage to nations\b"),
        "message to the nations",
    ),
    (
        re.compile(r"\binherit mount of Esau\b"),
        "inherit the mount of Esau",
    ),
    (
        re.compile(r"\binherit mount of Ephraim\b"),
        "inherit the mount of Ephraim",
    ),
    (
        re.compile(r"\bplain of Samaria\b"),
        "the plain of Samaria",
    ),
    (
        re.compile(r"\bfrom mount Zion\b"),
        "from Mount Zion",
    ),
    (
        re.compile(r"\bavenge mount of Esau\b"),
        "avenge the mount of Esau",
    ),
    (
        re.compile(r"\band kingdom will belong\b"),
        "and the kingdom will belong",
    ),
    (
        re.compile(r"\bNineveh, great city\b"),
        "Nineveh, the great city",
    ),
    (
        re.compile(r"\bbecause cry of its evil\b"),
        "because the cry of its evil",
    ),
    (
        re.compile(r"\baccording to former proclamation\b"),
        "according to the former proclamation",
    ),
    (
        re.compile(r"\bBook of vision of Nahum\b"),
        "Book of the vision of Nahum",
    ),
    (
        re.compile(r"\bMoab will be as Sodom and sons of Ammon as Gomorrah\b"),
        "Moab will be as Sodom and the sons of Ammon as Gomorrah",
    ),
    (
        re.compile(r"\blike heap of threshing-floor\b"),
        "like a heap of the threshing-floor",
    ),
    (
        re.compile(r"\bremnant of my people will plunder them, and remnant of my nation will inherit them\b"),
        "the remnant of my people will plunder them, and the remnant of my nation will inherit them",
    ),
    (
        re.compile(r"\bfor boast among all peoples of earth\b"),
        "for a boast among all the peoples of the earth",
    ),
    (
        re.compile(r"\bthere will no longer be Canaanite\b"),
        "there will no longer be a Canaanite",
    ),
    (
        re.compile(r"\bwhatever foreigner calls upon you for\b"),
        "whatever a foreigner calls upon you for",
    ),
    (
        re.compile(r"\bso that all peoples of earth may know\b"),
        "so that all the peoples of the earth may know",
    ),
    (
        re.compile(r"\bfear you as your people Israel and know\b"),
        "fear you as your people Israel do, and know",
    ),
    (
        re.compile(r"\bhas my house over which my name has been called become den of robbers\b"),
        "Has my house over which my name has been called become a den of robbers",
    ),
    (
        re.compile(r"\bon mount Zion\b"),
        "on Mount Zion",
    ),
    (
        re.compile(r"\bcalled on Lord\b"),
        "called on the Lord",
    ),
    (
        re.compile(r"\bUpon heights set me, to conquer in his song\b"),
        "He mounts me upon heights, to conquer in his song",
    ),
    (
        re.compile(r"\bProverbs of Solomon\b"),
        "The Proverbs of Solomon",
    ),
    (
        re.compile(r"\bSong of songs, which is Solomon's\b"),
        "The Song of Songs, which is Solomon's",
    ),
    (
        re.compile(r"\bVision which Isaiah\b"),
        "The vision which Isaiah",
    ),
    (
        re.compile(r"\bbecause great is day of Jezreel\b"),
        "because great is the day of Jezreel",
    ),
    (
        re.compile(r"\bin last days\b"),
        "in the last days",
    ),
    (
        re.compile(r"\bIn last days\b"),
        "In the last days",
    ),
    (
        re.compile(r"\bAlleluia\. In Israel going out from Egypt, the house of Jacob from barbarous people\b"),
        "Alleluia. When Israel went out from Egypt, the house of Jacob from a barbarous people",
    ),
    (
        re.compile(r"\bhe their helper and defender\b"),
        "he is their helper and defender",
    ),
    (
        re.compile(r"\bO Lord, I your servant, I your servant\b"),
        "O Lord, I am your servant, I am your servant",
    ),
    (
        re.compile(r"\bwhole day it my meditation\b"),
        "the whole day it is my meditation",
    ),
    (
        re.compile(r"\bI your servant; make me understand\b"),
        "I am your servant; make me understand",
    ),
    (
        re.compile(r"\bBut I your servant did not see\b"),
        "But I, your servant, did not see",
    ),
    (
        re.compile(r"\bbecause I your servant\b"),
        "because I am your servant",
    ),
    (
        re.compile(r"\bbecause you my firm place and refuge\b"),
        "because you are my firm place and refuge",
    ),
    (
        re.compile(r"\bBecause you my endurance\b"),
        "Because you are my endurance",
    ),
    (
        re.compile(r"\byou my protector\b"),
        "you are my protector",
    ),
    (
        re.compile(r"\bBut we your people and sheep of your pasture\b"),
        "But we are your people and sheep of your pasture",
    ),
    (
        re.compile(r"\bThose trusting in the Lord like Mount Zion\b"),
        "Those trusting in the Lord are like Mount Zion",
    ),
    (
        re.compile(r"\bBlessed all fearing Lord\b"),
        "Blessed are all fearing the Lord",
    ),
    (
        re.compile(r"\bOut of depths I cried\b"),
        "Out of the depths I cried",
    ),
    (
        re.compile(r"\bLord, my heart not exalted\b"),
        "Lord, my heart is not exalted",
    ),
    (
        re.compile(r"\bwhat good or what pleasant\b"),
        "what is good or what is pleasant",
    ),
    (
        re.compile(r"\bBecause in the last days mountain of the Lord and the house of God\b"),
        "Because in the last days the mountain of the Lord and the house of God",
    ),
    (
        re.compile(r"\bwhat he will do upon whole earth\b"),
        "what he will do upon the whole earth",
    ),
    (
        re.compile(r"\bwhat kings of Assyrians did to whole earth\b"),
        "what the kings of the Assyrians did to the whole earth",
    ),
    (
        re.compile(r"\bWill plowman plow whole earth all day\b"),
        "Will a plowman plow the whole earth all day",
    ),
    (
        re.compile(r"\ball beasts of whole earth\b"),
        "all beasts of the whole earth",
    ),
    (
        re.compile(r"\bIn joy of whole earth\b"),
        "In the joy of the whole earth",
    ),
    (
        re.compile(r"\bthe house of Jacob in snare\b"),
        "the house of Jacob is in a snare",
    ),
    (
        re.compile(r"\bthe house of Joseph flame, and house of Esau stubble\b"),
        "the house of Joseph a flame, and the house of Esau stubble",
    ),
    (
        re.compile(r"\bHas spirit of the Lord been provoked\b"),
        "Has the spirit of the Lord been provoked",
    ),
    (
        re.compile(r"\blike lion among beasts of the forest and like lion-cub among flocks of sheep\b"),
        "like a lion among beasts of the forest and like a lion-cub among flocks of sheep",
    ),
    (
        re.compile(r"\blike lion ready for hunt and like lion-cub dwelling\b"),
        "like a lion ready for the hunt and like a lion-cub dwelling",
    ),
    (
        re.compile(r"\blike lion\b"),
        "like a lion",
    ),
    (
        re.compile(r"\bas lion\b"),
        "as a lion",
    ),
    (
        re.compile(r"\bas beast\b"),
        "as a beast",
    ),
    (
        re.compile(r"\bfrom the face of great sword\b"),
        "from the face of the great sword",
    ),
    (
        re.compile(r"\blike sparrow\b"),
        "like a sparrow",
    ),
    (
        re.compile(r"\blike bird\b"),
        "like a bird",
    ),
    (
        re.compile(r"\blike dog\b"),
        "like a dog",
    ),
    (
        re.compile(r"\blike gazelle\b"),
        "like a gazelle",
    ),
    (
        re.compile(r"\blike calf\b"),
        "like a calf",
    ),
    (
        re.compile(r"\blike dove\b"),
        "like a dove",
    ),
    (
        re.compile(r"\blike horse through\b"),
        "like a horse through",
    ),
    (
        re.compile(r"\blike bear\b"),
        "like a bear",
    ),
    (
        re.compile(r"\bLike bear\b"),
        "Like a bear",
    ),
    (
        re.compile(r"\bas deer\b"),
        "as a deer",
    ),
    (
        re.compile(r"\blike eagle([.,])"),
        r"like an eagle\1",
    ),
    (
        re.compile(r"\blike eagle (he|against|eager)\b"),
        r"like an eagle \1",
    ),
    (
        re.compile(r"\bsoar high like eagle\b"),
        "soar high like an eagle",
    ),
    (
        re.compile(r"\bwiden your widowhood like eagle\b"),
        "widen your widowhood like an eagle",
    ),
    (
        re.compile(r"\bas young man dwelling with virgin\b"),
        "as a young man dwelling with a virgin",
    ),
    (
        re.compile(r"\bas bridegroom rejoices over bride\b"),
        "as a bridegroom rejoices over a bride",
    ),
    (
        re.compile(r"\bas ruler\b"),
        "as a ruler",
    ),
    (
        re.compile(r"\bas leader\b"),
        "as a leader",
    ),
    (
        re.compile(r"\bas prophet\b"),
        "as a prophet",
    ),
    (
        re.compile(r"\blike drunkard\b"),
        "like a drunkard",
    ),
    (
        re.compile(r"\blike tree\b"),
        "like a tree",
    ),
    (
        re.compile(r"\blike spider\b"),
        "like a spider",
    ),
    (
        re.compile(r"\blike moth\b"),
        "like a moth",
    ),
    (
        re.compile(r"\blike giant\b"),
        "like a giant",
    ),
    (
        re.compile(r"\blike wineskin\b"),
        "like a wineskin",
    ),
    (
        re.compile(r"\blike wheel within wheel\b"),
        "like a wheel within a wheel",
    ),
    (
        re.compile(r"\blike wheel\b"),
        "like a wheel",
    ),
    (
        re.compile(r"\bas wheel within wheel\b"),
        "as a wheel within a wheel",
    ),
    (
        re.compile(r"\blike storm\b"),
        "like a storm",
    ),
    (
        re.compile(r"\blike torrent\b"),
        "like a torrent",
    ),
    (
        re.compile(r"\blike river of peace\b"),
        "like a river of peace",
    ),
    (
        re.compile(r"\blike garment\b"),
        "like a garment",
    ),
    (
        re.compile(r"\blike cloak\b"),
        "like a cloak",
    ),
    (
        re.compile(r"\blike skin-bag\b"),
        "like a skin-bag",
    ),
    (
        re.compile(r"\blike cloud\b"),
        "like a cloud",
    ),
    (
        re.compile(r"\blike river\b"),
        "like a river",
    ),
    (
        re.compile(r"\blike wave\b"),
        "like a wave",
    ),
    (
        re.compile(r"\bas woman\b"),
        "as a woman",
    ),
    (
        re.compile(r"\blike dead man\b"),
        "like a dead man",
    ),
    (
        re.compile(r"\blike ruined vessel\b"),
        "like a ruined vessel",
    ),
    (
        re.compile(r"\bas house of sacrifice\b"),
        "as a house of sacrifice",
    ),
    (
        re.compile(r"\bas of woman\b"),
        "as of a woman",
    ),
    (
        re.compile(r"\bas fleeing gazelle\b"),
        "as a fleeing gazelle",
    ),
    (
        re.compile(r"\bas with weapon of favor\b"),
        "as with a weapon of favor",
    ),
    (
        re.compile(r"\bas flame burns\b"),
        "as a flame burns",
    ),
    (
        re.compile(r"\bas flame\b"),
        "as a flame",
    ),
    (
        re.compile(r"\bAct like man\b"),
        "Act like a man",
    ),
    (
        re.compile(r"\bact like man\b"),
        "act like a man",
    ),
    (
        re.compile(r"\blike birthing woman\b"),
        "like a birthing woman",
    ),
    (
        re.compile(r"\blike son of man\b"),
        "like a son of man",
    ),
    (
        re.compile(r"\blike sleeping man\b"),
        "like a sleeping man",
    ),
    (
        re.compile(r"\blike broken man\b"),
        "like a broken man",
    ),
    (
        re.compile(r"\blike wounded man\b"),
        "like a wounded man",
    ),
    (
        re.compile(r"\blike man\b"),
        "like a man",
    ),
    (
        re.compile(r"\blike desert\b"),
        "like a desert",
    ),
    (
        re.compile(r"\blike morning star\b"),
        "like a morning star",
    ),
    (
        re.compile(r"\blike morning cloud\b"),
        "like a morning cloud",
    ),
    (
        re.compile(r"\blike fruitful\b"),
        "like a fruitful",
    ),
    (
        re.compile(r"\blike vine\b"),
        "like a vine",
    ),
    (
        re.compile(r"\blike blossom\b"),
        "like a blossom",
    ),
    (
        re.compile(r"\blike bad traveler\b"),
        "like a bad traveler",
    ),
    (
        re.compile(r"\blike bad runner\b"),
        "like a bad runner",
    ),
    (
        re.compile(r"\blike good runner\b"),
        "like a good runner",
    ),
    (
        re.compile(r"\blike fountain\b"),
        "like a fountain",
    ),
    (
        re.compile(r"\bLike sound of\b"),
        "Like the sound of",
    ),
    (
        re.compile(r"\blike sound of\b"),
        "like the sound of",
    ),
    (
        re.compile(r"\blike voice of\b"),
        "like the voice of",
    ),
    (
        re.compile(r"\blike oven\b"),
        "like an oven",
    ),
    (
        re.compile(r"\blike bronze pot\b"),
        "like a bronze pot",
    ),
    (
        re.compile(r"\blike perfume-vessel\b"),
        "like a perfume-vessel",
    ),
    (
        re.compile(r"\blike shadow\b"),
        "like a shadow",
    ),
    (
        re.compile(r"\bLike flower\b"),
        "Like a flower",
    ),
    (
        re.compile(r"\blike flower\b"),
        "like a flower",
    ),
    (
        re.compile(r"\blike sword\b"),
        "like a sword",
    ),
    (
        re.compile(r"\blike stone cube\b"),
        "like a stone cube",
    ),
    (
        re.compile(r"\blike beam of\b"),
        "like a beam of",
    ),
    (
        re.compile(r"\blike heap of\b"),
        "like a heap of",
    ),
    (
        re.compile(r"\blike ripe threshing-floor\b"),
        "like a ripe threshing-floor",
    ),
    (
        re.compile(r"\blike hired man\b"),
        "like a hired man",
    ),
    (
        re.compile(r"\blike furnace\b"),
        "like a furnace",
    ),
    (
        re.compile(r"\blike deaf man\b"),
        "like a deaf man",
    ),
    (
        re.compile(r"\blike deaf asp\b"),
        "like a deaf asp",
    ),
    (
        re.compile(r"\blike flock\b"),
        "like a flock",
    ),
    (
        re.compile(r"\blike palm tree\b"),
        "like a palm tree",
    ),
    (
        re.compile(r"\blike cedar\b"),
        "like a cedar",
    ),
    (
        re.compile(r"\blike herd of\b"),
        "like a herd of",
    ),
    (
        re.compile(r"\bas piece of\b"),
        "as a piece of",
    ),
    (
        re.compile(r"\bas seal\b"),
        "as a seal",
    ),
    (
        re.compile(r"\bas tent\b"),
        "as a tent",
    ),
    (
        re.compile(r"\bas city\b"),
        "as a city",
    ),
    (
        re.compile(r"\blike oak\b"),
        "like an oak",
    ),
    (
        re.compile(r"\bas flying bird\b"),
        "as a flying bird",
    ),
    (
        re.compile(r"\bas enemy\b"),
        "as an enemy",
    ),
    (
        re.compile(r"\blike field\b"),
        "like a field",
    ),
    (
        re.compile(r"\bas shepherd\b"),
        "as a shepherd",
    ),
    (
        re.compile(r"\blike flame of fire\b"),
        "like a flame of fire",
    ),
    (
        re.compile(r"\bas sound of\b"),
        "as the sound of",
    ),
    (
        re.compile(r"\bas watchman\b"),
        "as a watchman",
    ),
    (
        re.compile(r"\bas iron wall\b"),
        "as an iron wall",
    ),
    (
        re.compile(r"\blike dead of\b"),
        "like the dead of",
    ),
    (
        re.compile(r"\blike passing shadow\b"),
        "like a passing shadow",
    ),
    (
        re.compile(r"\blike passing flower\b"),
        "like a passing flower",
    ),
    (
        re.compile(r"\blike roaring of lion\b"),
        "like the roaring of a lion",
    ),
    (
        re.compile(r"\blike force of God\b"),
        "like the force of God",
    ),
    (
        re.compile(r"\blike breaking of waters\b"),
        "like the breaking of waters",
    ),
    (
        re.compile(r"\blike name of\b"),
        "like the name of",
    ),
    (
        re.compile(r"\blike rim of cup\b"),
        "like the rim of a cup",
    ),
    (
        re.compile(r"\blike funeral of\b"),
        "like the funeral of",
    ),
    (
        re.compile(r"\bas leper\b"),
        "as a leper",
    ),
    (
        re.compile(r"\bas stumbling-block\b"),
        "as a stumbling-block",
    ),
    (
        re.compile(r"\bas laughingstock\b"),
        "as a laughingstock",
    ),
    (
        re.compile(r"\bLike appearance of\b"),
        "Like the appearance of",
    ),
    (
        re.compile(r"\blike appearance of\b"),
        "like the appearance of",
    ),
    (
        re.compile(r"\bas appearance of\b"),
        "as the appearance of",
    ),
    (
        re.compile(r"\blike sight of\b"),
        "like the sight of",
    ),
    (
        re.compile(r"\blike work of\b"),
        "like the work of",
    ),
    (
        re.compile(r"\blike likeness of\b"),
        "like the likeness of",
    ),
    (
        re.compile(r"\blike fish of the great sea\b"),
        "like the fish of the great sea",
    ),
    (
        re.compile(r"\blike fish of the sea\b"),
        "like the fish of the sea",
    ),
    (
        re.compile(r"\bas eyes of servants\b"),
        "as the eyes of servants",
    ),
    (
        re.compile(r"\bas eyes of maidservant\b"),
        "as the eyes of a maidservant",
    ),
    (
        re.compile(r"\bI was eye of blind\b"),
        "I was the eye of the blind",
    ),
    (
        re.compile(r"\band foot of lame\b"),
        "and foot of the lame",
    ),
    (
        re.compile(r"\blike the appearance of sapphire stone\b"),
        "like the appearance of a sapphire stone",
    ),
    (
        re.compile(r"\bLike the appearance of sapphire stone\b"),
        "Like the appearance of a sapphire stone",
    ),
    (
        re.compile(r"\blike the appearance of carbuncle stone\b"),
        "like the appearance of a carbuncle stone",
    ),
    (
        re.compile(r"\bas the appearance of man\b"),
        "as the appearance of a man",
    ),
    (
        re.compile(r"\bLike the appearance of bow when it is in cloud\b"),
        "Like the appearance of a bow when it is in a cloud",
    ),
    (
        re.compile(r"\bThis was appearance of likeness of\b"),
        "This was the appearance of the likeness of",
    ),
    (
        re.compile(r"\bheard voice speaking\b"),
        "heard a voice speaking",
    ),
    (
        re.compile(r"\bheard voice of\b"),
        "heard the voice of",
    ),
    (
        re.compile(r"\bhear sound of\b"),
        "hear the sound of",
    ),
    (
        re.compile(r"\bheard sound of\b"),
        "heard the sound of",
    ),
    (
        re.compile(r"\bendure sound of\b"),
        "endure the sound of",
    ),
    (
        re.compile(r", sound of festival-keepers\b"),
        ", the sound of festival-keepers",
    ),
    (
        re.compile(r", sound of its waves\b"),
        ", the sound of its waves",
    ),
    (
        re.compile(r"\bset sound of\b"),
        "set the sound of",
    ),
    (
        re.compile(r"\bWith sound of\b"),
        "With the sound of",
    ),
    (
        re.compile(r", sound of his wheels\b"),
        ", the sound of his wheels",
    ),
    (
        re.compile(r"\bby sound of\b"),
        "by the sound of",
    ),
    (
        re.compile(r"\bbecause of sound of\b"),
        "because of the sound of",
    ),
    (
        re.compile(r"\bRemove from me sound of\b"),
        "Remove from me the sound of",
    ),
    (
        re.compile(r"\bto sound of instruments\b"),
        "to the sound of instruments",
    ),
    (
        re.compile(r"\bhates sound of security\b"),
        "hates the sound of security",
    ),
    (
        re.compile(r"\b([Tt]o|[Bb]efore|[Ww]ith|[Ff]rom|[Aa]gainst|[Ff]or) king\b"),
        r"\1 the king",
    ),
    (
        re.compile(r"\band king of\b"),
        "and the king of",
    ),
    (
        re.compile(r"\band king were\b"),
        "and the king were",
    ),
    (
        re.compile(r"\band king put\b"),
        "and the king put",
    ),
    (
        re.compile(r"\bGod and king\b"),
        "God and the king",
    ),
    (
        re.compile(r"\bpeople and king\b"),
        "people and the king",
    ),
    (
        re.compile(r"\bson, and king\b"),
        "son, and the king",
    ),
    (
        re.compile(r"\bbecause king desired\b"),
        "because the king desired",
    ),
    (
        re.compile(r"\band king speaking publicly\b"),
        "and a king speaking publicly",
    ),
    (
        re.compile(r"\band king asked\b"),
        "and the king asked",
    ),
    (
        re.compile(r"\band king honored\b"),
        "and the king honored",
    ),
    (
        re.compile(r"\band king sealed\b"),
        "and the king sealed",
    ),
    (
        re.compile(r"\bthat king might\b"),
        "that the king might",
    ),
    (
        re.compile(r"\bthat king did not\b"),
        "that the king did not",
    ),
    (
        re.compile(r"\banswered king saying\b"),
        "answered the king saying",
    ),
    (
        re.compile(r"\bbecause mouth of sinner and mouth of deceitful one\b"),
        "because the mouth of sinner and the mouth of deceitful one",
    ),
    (
        re.compile(r"\bSpirit of fear of God\b"),
        "The spirit of fear of God",
    ),
    (
        re.compile(r"\bAnd spirit of Egyptians\b"),
        "And the spirit of Egyptians",
    ),
    (
        re.compile(r"\bSpirit of the Lord on me\b"),
        "The Spirit of the Lord on me",
    ),
    (
        re.compile(r"\bSpirit of fullness\b"),
        "The spirit of fullness",
    ),
    (
        re.compile(r"\bAnd spirit of the Lord fell\b"),
        "And the Spirit of the Lord fell",
    ),
    (
        re.compile(r"\bbut word of our God remains\b"),
        "but the word of our God remains",
    ),
    (
        re.compile(r"\bGlory of God hides word\b"),
        "The glory of God hides a word",
    ),
    (
        re.compile(r"\bGlory of Lebanon\b"),
        "The glory of Lebanon",
    ),
    (
        re.compile(r"\bCity of your holy one became\b"),
        "The city of your holy one became",
    ),
    (
        re.compile(r"\bAnd city came into siege\b"),
        "And the city came into siege",
    ),
    (
        re.compile(r"\bAnd city was broken through\b"),
        "And the city was broken through",
    ),
    (
        re.compile(r"\bLand mourned\b"),
        "The land mourned",
    ),
    (
        re.compile(r"\bAnd land acted lawlessly\b"),
        "And the land acted lawlessly",
    ),
    (
        re.compile(r"\bAnd land will be watered\b"),
        "And the land will be watered",
    ),
    (
        re.compile(r"\band land that was desolated\b"),
        "and the land that was desolated",
    ),
    (
        re.compile(r"\bAnd land will mourn\b"),
        "And the land will mourn",
    ),
    (
        re.compile(r"\bPeople will fall\b"),
        "The people will fall",
    ),
    (
        re.compile(r"\bPeople walking in darkness\b"),
        "The people walking in darkness",
    ),
    (
        re.compile(r"\bPeople and cattle clothed themselves\b"),
        "The people and cattle clothed themselves",
    ),
    (
        re.compile(r"\bBirth-pangs of death\b"),
        "The birth-pangs of death",
    ),
    (
        re.compile(r"\bPangs of death\b"),
        "The pangs of death",
    ),
    (
        re.compile(r"\bPangs of Hades\b"),
        "The pangs of Hades",
    ),
    (
        re.compile(r"\bKings of earth\b"),
        "The kings of earth",
    ),
    (
        re.compile(r"\bThe kings of earth\b"),
        "The kings of the earth",
    ),
    (
        re.compile(r"\bSwords of enemy\b"),
        "The swords of enemy",
    ),
    (
        re.compile(r"\bThe swords of enemy\b"),
        "The swords of the enemy",
    ),
    (
        re.compile(r"\bDesire of poor men\b"),
        "The desire of poor men",
    ),
    (
        re.compile(r"\bDesire of his soul\b"),
        "The desire of his soul",
    ),
    (
        re.compile(r"\bDesire of righteous\b"),
        "The desire of righteous",
    ),
    (
        re.compile(r"\bThe desire of righteous\b"),
        "The desire of the righteous",
    ),
    (
        re.compile(r"\bLaw of the Lord blameless\b"),
        "The law of the Lord is blameless",
    ),
    (
        re.compile(r"\btestimony of the Lord faithful\b"),
        "the testimony of the Lord is faithful",
    ),
    (
        re.compile(r"\bOrdinances of the Lord straight\b"),
        "The ordinances of the Lord are straight",
    ),
    (
        re.compile(r"\bcommand of the Lord radiant\b"),
        "the command of the Lord is radiant",
    ),
    (
        re.compile(r"\bEyes of the Lord upon\b"),
        "The eyes of the Lord are upon",
    ),
    (
        re.compile(r"\bEyes of the Lord preserve\b"),
        "The eyes of the Lord preserve",
    ),
    (
        re.compile(r"\bDeath of sinners evil\b"),
        "The death of sinners is evil",
    ),
    (
        re.compile(r"\bWords of his mouth\b"),
        "The words of his mouth",
    ),
    (
        re.compile(r"\bLaw of his God in his heart\b"),
        "The law of his God is in his heart",
    ),
    (
        re.compile(r"\bSacrifice of praise\b"),
        "A sacrifice of praise",
    ),
    (
        re.compile(r"\bWords of lawless men\b"),
        "The words of lawless men",
    ),
    (
        re.compile(r"\bKings of Tarshish\b"),
        "The kings of Tarshish",
    ),
    (
        re.compile(r"\bTrees of the plain\b"),
        "The trees of the plain",
    ),
    (
        re.compile(r"\bIdols of nations\b"),
        "The idols of nations",
    ),
    (
        re.compile(r"\bHeaven of heaven belongs\b"),
        "The heaven of heaven belongs",
    ),
    (
        re.compile(r"\bCup of salvation\b"),
        "The cup of salvation",
    ),
    (
        re.compile(r"\bWay of truth\b"),
        "The way of truth",
    ),
    (
        re.compile(r"\bWay of your commandments\b"),
        "The way of your commandments",
    ),
    (
        re.compile(r"\bRopes of sinners\b"),
        "The ropes of sinners",
    ),
    (
        re.compile(r"\bDisclosure of your words\b"),
        "The disclosure of your words",
    ),
    (
        re.compile(r"\bStreams of waters\b"),
        "The streams of waters",
    ),
    (
        re.compile(r"\bBeginning of your words truth\b"),
        "The beginning of your words is truth",
    ),
    (
        re.compile(r"\bLabors of your fruits\b"),
        "The labors of your fruits",
    ),
    (
        re.compile(r"\bDaughter of Babylon\b"),
        "The daughter of Babylon",
    ),
    (
        re.compile(r"\bHead of their encirclement\b"),
        "The head of their encirclement",
    ),
    (
        re.compile(r"\bEyes of all hope in you\b"),
        "The eyes of all hope in you",
    ),
    (
        re.compile(r"\bPraise of the Lord my mouth\b"),
        "The praise of the Lord my mouth",
    ),
    (
        re.compile(r"\bExaltations of God\b"),
        "The exaltations of God",
    ),
    (
        re.compile(r"\bBeginning of wisdom fear of God\b"),
        "The beginning of wisdom is fear of God",
    ),
    (
        re.compile(r"\bBeginning of the word of the Lord\b"),
        "The beginning of the word of the Lord",
    ),
    (
        re.compile(r"\bWorks of righteous\b"),
        "The works of righteous",
    ),
    (
        re.compile(r"\bThe works of righteous\b"),
        "The works of the righteous",
    ),
    (
        re.compile(r"\bWords of ungodly\b"),
        "The words of ungodly",
    ),
    (
        re.compile(r"\bThe words of ungodly\b"),
        "The words of the ungodly",
    ),
    (
        re.compile(r"\bLaw of wise fountain of life\b"),
        "The law of wise is a fountain of life",
    ),
    (
        re.compile(r"\bThe law of wise is a fountain of life\b"),
        "The law of the wise is a fountain of life",
    ),
    (
        re.compile(r"\bBeginning of good way ="),
        "The beginning of a good way =",
    ),
    (
        re.compile(r"\bWay of righteousness\b"),
        "The way of righteousness",
    ),
    (
        re.compile(r"\bWay of evil\b"),
        "The way of evil",
    ),
    (
        re.compile(r"\bWords of whisperers\b"),
        "The words of whisperers",
    ),
    (
        re.compile(r"\bEyes of wise man\b"),
        "The eyes of a wise man",
    ),
    (
        re.compile(r"\bWords of mouth of wise\b"),
        "The words of the mouth of wise",
    ),
    (
        re.compile(r"\bThe words of the mouth of wise\b"),
        "The words of the mouth of the wise",
    ),
    (
        re.compile(r"\bBeginning of words of his mouth ="),
        "The beginning of the words of his mouth =",
    ),
    (
        re.compile(r"\bDaughter of Zion\b"),
        "The daughter of Zion",
    ),
    (
        re.compile(r"\bWay of godly\b"),
        "The way of godly",
    ),
    (
        re.compile(r"\bThe way of godly\b"),
        "The way of the godly",
    ),
    (
        re.compile(r"\bDaughter of my people\b"),
        "The daughter of my people",
    ),
    (
        re.compile(r"\bDaughter of Egypt\b"),
        "The daughter of Egypt",
    ),
    (
        re.compile(r"\bWords of sons of Jonadab\b"),
        "The words of sons of Jonadab",
    ),
    (
        re.compile(r"\bKings of earth did not\b"),
        "The kings of earth did not",
    ),
    (
        re.compile(r"\bThe kings of earth did not\b"),
        "The kings of the earth did not",
    ),
    (
        re.compile(r"\bLaw of truth\b"),
        "The law of truth",
    ),
    (
        re.compile(r"\bSacrifice of Judah\b"),
        "The sacrifice of Judah",
    ),
    (
        re.compile(r"\bBlessing of one perishing came upon me, and mouth of widow blessed me\b"),
        "The blessing of one perishing came upon me, and the mouth of the widow blessed me",
    ),
    (
        re.compile(r"\bCurse of God in the houses of ungodly\b"),
        "The curse of God in the houses of the ungodly",
    ),
    (
        re.compile(r"\bdwellings of righteous are blessed\b"),
        "dwellings of the righteous are blessed",
    ),
    (
        re.compile(r"\bBlessing of the Lord upon the head of righteous\b"),
        "The blessing of the Lord upon the head of the righteous",
    ),
    (
        re.compile(r"\bMemory of righteous with praises\b"),
        "The memory of the righteous with praises",
    ),
    (
        re.compile(r"\bname of ungodly is quenched\b"),
        "the name of the ungodly is quenched",
    ),
    (
        re.compile(r"\bFountain of life in the hand of righteous\b"),
        "A fountain of life is in the hand of the righteous",
    ),
    (
        re.compile(r"\bRighteousness of blameless cuts straight ways\b"),
        "The righteousness of the blameless cuts straight ways",
    ),
    (
        re.compile(r"\bRighteousness of upright rescues them\b"),
        "The righteousness of the upright rescues them",
    ),
    (
        re.compile(r"\bWisdom of shrewd will know their ways\b"),
        "The wisdom of the shrewd will know their ways",
    ),
    (
        re.compile(r"\bbut folly of fools in wandering\b"),
        "but the folly of fools is in wandering",
    ),
    (
        re.compile(r"\bCommand of the Lord fountain of life\b"),
        "The command of the Lord is a fountain of life",
    ),
    (
        re.compile(r"\bFear of God discipline and wisdom\b"),
        "The fear of God is discipline and wisdom",
    ),
    (
        re.compile(r"\bLight of the Lord = breath of men\b"),
        "The light of the Lord = the breath of men",
    ),
    (
        re.compile(r"\bJoy of righteous = doing judgment\b"),
        "The joy of the righteous = doing judgment",
    ),
    (
        re.compile(r"\bJoy of our heart ceased\b"),
        "The joy of our heart ceased",
    ),
    (
        re.compile(r"\bTongue of wise knows good things\b"),
        "The tongue of the wise knows good things",
    ),
    (
        re.compile(r"\bmouth of fools will announce evils\b"),
        "the mouth of fools will announce evils",
    ),
    (
        re.compile(r"\bFace of understanding man belongs to wise one\b"),
        "The face of an understanding man belongs to a wise one",
    ),
    (
        re.compile(r"\beyes of fool to the ends of the earth\b"),
        "the eyes of a fool to the ends of the earth",
    ),
    (
        re.compile(r"\bTongue of nursing child clung\b"),
        "The tongue of a nursing child clung",
    ),
    (
        re.compile(r"\bHands of compassionate women cooked their children\b"),
        "The hands of compassionate women cooked their children",
    ),
    (
        re.compile(r"\bFace of the Lord is their portion\b"),
        "The face of the Lord is their portion",
    ),
    (
        re.compile(r"\bFoot of man will not pass through it\b"),
        "The foot of a man will not pass through it",
    ),
    (
        re.compile(r"\bThe foot of man will not pass through it\b"),
        "The foot of a man will not pass through it",
    ),
    (
        re.compile(r"\bfoot of beast will not pass through it\b"),
        "the foot of a beast will not pass through it",
    ),
    (
        re.compile(r"\bFace of man toward the palm\b"),
        "The face of a man toward the palm",
    ),
    (
        re.compile(r"\bface of lion toward the palm\b"),
        "the face of a lion toward the palm",
    ),
    (
        re.compile(r"\bHands of Zerubbabel founded this house\b"),
        "The hands of Zerubbabel founded this house",
    ),
    (
        re.compile(r"\bRulers of peoples gathered with God of Abraham\b"),
        "The rulers of peoples gathered with the God of Abraham",
    ),
    (
        re.compile(r"\bmighty ones of earth belong to God\b"),
        "the mighty ones of the earth belong to God",
    ),
    (
        re.compile(r"\bEnemies of the Lord lied to him\b"),
        "The enemies of the Lord lied to him",
    ),
    (
        re.compile(r"\bHouses of lawless will owe cleansing\b"),
        "The houses of the lawless will owe cleansing",
    ),
    (
        re.compile(r"\bhouses of righteous acceptable\b"),
        "houses of the righteous are acceptable",
    ),
    (
        re.compile(r"\bHouses of ungodly will vanish\b"),
        "The houses of the ungodly will vanish",
    ),
    (
        re.compile(r"\bPrinces of Zoan failed, and princes of Memphis\b"),
        "The princes of Zoan failed, and the princes of Memphis",
    ),
    (
        re.compile(r"\bRulers of Judah became\b"),
        "The rulers of Judah became",
    ),
    (
        re.compile(r"\brighteous with ungodly\b"),
        "the righteous with the ungodly",
    ),
    (
        re.compile(
            r"\b(hope|overthrow|gift|dwelling|hands|counsel|eyes|life|witness|gladness|vengeance) of ungodly(?! (?:man|men))\b"
        ),
        r"\1 of the ungodly",
    ),
    (
        re.compile(r"\bcounsel of the ungodly men\b"),
        "counsel of ungodly men",
    ),
    (
        re.compile(r"\boverthrow of the ungodly men\b"),
        "overthrow of ungodly men",
    ),
    (
        re.compile(r"\b(afflictions|salvation) of righteous ones\b"),
        r"\1 of the righteous ones",
    ),
    (
        re.compile(r"\bhorns of righteous one\b"),
        "horns of the righteous one",
    ),
    (
        re.compile(r"\bsoul of righteous man\b"),
        "soul of a righteous man",
    ),
    (
        re.compile(r"\blot of righteous\b"),
        "lot of the righteous",
    ),
    (
        re.compile(r"\bcry of poor upon\b"),
        "cry of the poor upon",
    ),
    (
        re.compile(r"\bcounsel of poor man\b"),
        "counsel of a poor man",
    ),
    (
        re.compile(r"\bpetition of poor man\b"),
        "petition of a poor man",
    ),
    (
        re.compile(r"\bjudgment of poor one and justice of needy\b"),
        "judgment of a poor one and justice of the needy",
    ),
    (
        re.compile(r"\bSinner provoked Lord\b"),
        "The sinner provoked the Lord",
    ),
    (
        re.compile(r"\bLawless man says\b"),
        "The lawless man says",
    ),
    (
        re.compile(r"\bSinner will watch righteous man\b"),
        "The sinner will watch a righteous man",
    ),
    (
        re.compile(r"\bSinner borrows and will not repay, but righteous man\b"),
        "The sinner borrows and will not repay, but a righteous man",
    ),
    (
        re.compile(r"\bSinner watches righteous man\b"),
        "The sinner watches a righteous man",
    ),
    (
        re.compile(r"\bFool said in his heart\b"),
        "The fool said in his heart",
    ),
    (
        re.compile(r"\bRighteous one will rejoice\b"),
        "The righteous one will rejoice",
    ),
    (
        re.compile(r"\bRighteous one will flower\b"),
        "The righteous one will flower",
    ),
    (
        re.compile(r"\bSinner will see and be angry\b"),
        "The sinner will see and be angry",
    ),
    (
        re.compile(r"\bWise son gladdens father, but foolish son\b"),
        "A wise son gladdens a father, but a foolish son",
    ),
    (
        re.compile(r"\bUngodly one does unjust works\b"),
        "An ungodly one does unjust works",
    ),
    (
        re.compile(r"\bFool same day announces\b"),
        "A fool the same day announces",
    ),
    (
        re.compile(r"\bWise man, fearing,"),
        "A wise man, fearing,",
    ),
    (
        re.compile(r"\bbut fool, trusting himself, mixes with lawless man\b"),
        "but a fool, trusting himself, mixes with a lawless man",
    ),
    (
        re.compile(r"\bFool sneers discipline of father\b"),
        "A fool sneers at the discipline of a father",
    ),
    (
        re.compile(r"\bLawless man tests friends\b"),
        "A lawless man tests friends",
    ),
    (
        re.compile(r"\bWise servant calms anger of man\b"),
        "A wise servant calms the anger of a man",
    ),
    (
        re.compile(r"\bRighteous man accuses himself\b"),
        "A righteous man accuses himself",
    ),
    (
        re.compile(r"\bWise king winnows ungodly\b"),
        "A wise king winnows the ungodly",
    ),
    (
        re.compile(r"\bLawless man = purging-scrap for righteous\b"),
        "A lawless man = purging-scrap for the righteous",
    ),
    (
        re.compile(r"\bWise man scaled strong cities\b"),
        "A wise man scaled strong cities",
    ),
    (
        re.compile(r"\bUngodly man stands shameless\b"),
        "An ungodly man stands shameless",
    ),
    (
        re.compile(r"\bFool dies in sins\b"),
        "A fool dies in sins",
    ),
    (
        re.compile(r"\bWise man will judge nations\b"),
        "A wise man will judge nations",
    ),
    (
        re.compile(r"\bFool folded his hands\b"),
        "A fool folded his hands",
    ),
    (
        re.compile(r"\bFool was given\b"),
        "A fool was given",
    ),
    (
        re.compile(r"\bjudgments of the Lord true\b"),
        "judgments of the Lord are true",
    ),
    (
        re.compile(r"\bthe word of the Lord straight\b"),
        "the word of the Lord is straight",
    ),
    (
        re.compile(r"\bThe word of the Lord straight\b"),
        "The word of the Lord is straight",
    ),
    (
        re.compile(r"\bsalvation of man vain\b"),
        "salvation of man is vain",
    ),
    (
        re.compile(r"\bPrecious before the Lord death of his holy ones\b"),
        "Precious before the Lord is the death of his holy ones",
    ),
    (
        re.compile(r"\bThe ways of righteous like shining light\b"),
        "The ways of the righteous are like shining light",
    ),
    (
        re.compile(r"\bThe memory of the righteous with praises\b"),
        "The memory of the righteous is with praises",
    ),
    (
        re.compile(r"\bdesire of righteous acceptable\b"),
        "the desire of the righteous is acceptable",
    ),
    (
        re.compile(r"\bThe desire of the righteous altogether good\b"),
        "The desire of the righteous is altogether good",
    ),
    (
        re.compile(r"\bThe fear of the Lord fortress of holy one\b"),
        "The fear of the Lord is a fortress of a holy one",
    ),
    (
        re.compile(r"\bThe mouth of righteous drips wisdom\b"),
        "The mouth of the righteous drips wisdom",
    ),
    (
        re.compile(r"\bThe words of the ungodly deceitful\b"),
        "The words of the ungodly are deceitful",
    ),
    (
        re.compile(r"\bHearts of righteous meditate faithfulness\b"),
        "The hearts of the righteous meditate faithfulness",
    ),
    (
        re.compile(r"\bThe ways of righteous men acceptable to the Lord\b"),
        "The ways of righteous men are acceptable to the Lord",
    ),
    (
        re.compile(r"\bGod far from ungodly\b"),
        "God is far from the ungodly",
    ),
    (
        re.compile(r"\bbut prayers of righteous he hears\b"),
        "but prayers of the righteous he hears",
    ),
    (
        re.compile(r"\bWays of Hades her house\b"),
        "The ways of Hades are her house",
    ),
    (
        re.compile(r"\bWays of fools right before themselves\b"),
        "The ways of fools are right before themselves",
    ),
    (
        re.compile(r"\bWays of idle paved with thorns\b"),
        "The ways of the idle are paved with thorns",
    ),
    (
        re.compile(r"\bWays of mindless man lacking sense\b"),
        "The ways of a mindless man lack sense",
    ),
    (
        re.compile(r"\bWays of life thoughts of understanding\b"),
        "The ways of life are thoughts of understanding",
    ),
    (
        re.compile(r"\bcounsel of holy ones understanding\b"),
        "the counsel of holy ones is understanding",
    ),
    (
        re.compile(r"\bbut tongue of unjust will perish\b"),
        "but the tongue of the unjust will perish",
    ),
    (
        re.compile(r"\bbut mouth of upright will rescue them\b"),
        "but the mouth of the upright will rescue them",
    ),
    (
        re.compile(r"\bIn every place eyes of the Lord watch\b"),
        "In every place the eyes of the Lord watch",
    ),
    (
        re.compile(r"\bAll the time eyes of evil ones expect evils\b"),
        "All the time the eyes of evil ones expect evils",
    ),
    (
        re.compile(r"\bThe way of evil and foot of lawless man perish\b"),
        "The way of evil and the foot of a lawless man perish",
    ),
    (
        re.compile(r"\band way of godly prepared\b"),
        "and the way of the godly is prepared",
    ),
    (
        re.compile(r"\bSee how righteous man perished\b"),
        "See how a righteous man perished",
    ),
    (
        re.compile(r"\bbecause from the face of injustice righteous man is taken away\b"),
        "because from the face of injustice a righteous man is taken away",
    ),
    (
        re.compile(r"\bWrath of anger will be sent upon him\b"),
        "The wrath of anger will be sent upon him",
    ),
    (
        re.compile(r"\bPebbles of torrent were sweet to him\b"),
        "The pebbles of a torrent were sweet to him",
    ),
    (
        re.compile(r"\bPillars of heaven were spread out\b"),
        "The pillars of heaven were spread out",
    ),
    (
        re.compile(r"\bDrops of rain are counted for him\b"),
        "The drops of rain are counted for him",
    ),
    (
        re.compile(r"\bSoul of ungodly will not be pitied\b"),
        "The soul of the ungodly will not be pitied",
    ),
    (
        re.compile(r"\bToil of fools will weary them\b"),
        "The toil of fools will weary them",
    ),
    (
        re.compile(r"\bDwellers of rock will rejoice\b"),
        "The dwellers of rock will rejoice",
    ),
    (
        re.compile(r"\bFace of prostitute became yours\b"),
        "The face of a prostitute became yours",
    ),
    (
        re.compile(r"\bDays of vengeance have come; days of your repayment have come\b"),
        "The days of vengeance have come; the days of your repayment have come",
    ),
    (
        re.compile(r"\bGates of rivers were opened\b"),
        "The gates of rivers were opened",
    ),
    (
        re.compile(r"\bAnd wings of cheroubim were twenty cubits\b"),
        "And the wings of cheroubim were twenty cubits",
    ),
    (
        re.compile(r"\bAnd wings of cheroubim spread out were twenty cubits\b"),
        "And the wings of cheroubim spread out were twenty cubits",
    ),
    (
        re.compile(r"\bBecause many of assembly had not sanctified themselves\b"),
        "Because many of the assembly had not sanctified themselves",
    ),
    (
        re.compile(r"\bFor wrath of anger is unrestrainable\b"),
        "For the wrath of anger is unrestrainable",
    ),
    (
        re.compile(r"\bto defile wife of man\b"),
        "to defile the wife of a man",
    ),
    (
        re.compile(r"\bAnd fountains of waters were seen\b"),
        "And the fountains of waters were seen",
    ),
    (
        re.compile(r"\band foundations of inhabited world were uncovered\b"),
        "and the foundations of the inhabited world were uncovered",
    ),
    (
        re.compile(r"\bThere workers of lawlessness fell\b"),
        "There the workers of lawlessness fell",
    ),
    (
        re.compile(r"\bFrom the Lord steps of man are directed straight\b"),
        "From the Lord the steps of a man are directed straight",
    ),
    (
        re.compile(r"\bFrom the Lord steps of man are made straight\b"),
        "From the Lord the steps of a man are made straight",
    ),
    (
        re.compile(r"\bThe ways of ungodly will perish\b"),
        "The ways of the ungodly will perish",
    ),
    (
        re.compile(r"\bThe ways of ungodly abomination to the Lord\b"),
        "The ways of the ungodly are an abomination to the Lord",
    ),
    (
        re.compile(r"\bBut the ways of ungodly dark\b"),
        "But the ways of the ungodly are dark",
    ),
    (
        re.compile(r"\bAnd wealth of ungodly will be\b"),
        "And the wealth of the ungodly will be",
    ),
    (
        re.compile(r"\bbut wealth of ungodly stored up for righteous\b"),
        "but the wealth of the ungodly is stored up for the righteous",
    ),
    (
        re.compile(r"\bGladness of drums ceased, insolence and wealth of ungodly ceased, voice of lyre ceased\b"),
        "The gladness of drums ceased, insolence and the wealth of the ungodly ceased, the voice of the lyre ceased",
    ),
    (
        re.compile(r"\bAnd light of moon will be as light of sun, and light of sun will be sevenfold\b"),
        "And the light of moon will be as the light of sun, and the light of sun will be sevenfold",
    ),
    (
        re.compile(r"\bin day when the Lord heals\b"),
        "in the day when the Lord heals",
    ),
    (
        re.compile(r"\bAnd works of righteousness will be peace\b"),
        "And the works of righteousness will be peace",
    ),
    (
        re.compile(r"\bSeed of disobedient became for destruction\b"),
        "The seed of the disobedient became for destruction",
    ),
    (
        re.compile(r"\bThen eyes of blind will be opened and ears of deaf will hear\b"),
        "Then the eyes of the blind will be opened and ears of the deaf will hear",
    ),
    (
        re.compile(r"\bBecause customs of nations are vain\b"),
        "Because the customs of nations are vain",
    ),
    (
        re.compile(r"\bThe foot of man will not pass through it, and the foot of beast will not pass through it\b"),
        "The foot of a man will not pass through it, and the foot of a beast will not pass through it",
    ),
    (
        re.compile(r"\bAnd altars of laughter will be destroyed, and rites of Israel will be laid waste\b"),
        "And the altars of laughter will be destroyed, and the rites of Israel will be laid waste",
    ),
    (
        re.compile(r"\bAnd tract of sea will belong to the remnant\b"),
        "And the tract of sea will belong to the remnant",
    ),
    (
        re.compile(r"\bYou prisoners of congregation will sit\b"),
        "You prisoners of the congregation will sit",
    ),
    (
        re.compile(r"\bAnd gathering of peoples will encircle you\b"),
        "And a gathering of peoples will encircle you",
    ),
    (
        re.compile(r"\bWise in heart will receive commands\b"),
        "The wise in heart will receive commands",
    ),
    (
        re.compile(r"\bbut wise listens to counsels\b"),
        "but a wise one listens to counsels",
    ),
    (
        re.compile(r"\bknow that Lord of all hearts knows\b"),
        "know that the Lord of all hearts knows",
    ),
    (
        re.compile(r"\bAnd dwellers in this island will say\b"),
        "And the dwellers in this island will say",
    ),
    (
        re.compile(r"\bAnd those from west will fear the name of the Lord\b"),
        "And those from the west will fear the name of the Lord",
    ),
    (
        re.compile(r"\band those from sunrise his glorious name\b"),
        "and those from the sunrise his glorious name",
    ),
    (
        re.compile(r"\bVoice from lips was heard\b"),
        "A voice from lips was heard",
    ),
    (
        re.compile(r"\bAnd remnants of peace will cease\b"),
        "And the remnants of peace will cease",
    ),
    (
        re.compile(r"\bAnd reproach of nations will no longer be heard against you\b"),
        "And the reproach of nations will no longer be heard against you",
    ),
    (
        re.compile(r"\bArrogance of your heart lifted you up\b"),
        "The arrogance of your heart lifted you up",
    ),
    (
        re.compile(r"\bAnd seers of dreams will be put to shame\b"),
        "And the seers of dreams will be put to shame",
    ),
    (
        re.compile(r"\bwith them was book of the law\b"),
        "with them was the book of the law",
    ),
    (
        re.compile(r"\bfound book of the law\b"),
        "found the book of the law",
    ),
    (
        re.compile(r"\bbring book of the law\b"),
        "bring the book of the law",
    ),
    (
        re.compile(r"\btoward book of the law\b"),
        "toward the book of the law",
    ),
    (
        re.compile(r"\bwhen king heard words of law\b"),
        "when the king heard the words of the law",
    ),
    (
        re.compile(r"\ball words of the law\b"),
        "all the words of the law",
    ),
    (
        re.compile(r"\bI found book of law\b"),
        "I found the book of the law",
    ),
    (
        re.compile(r"\bgave book to\b"),
        "gave the book to",
    ),
    (
        re.compile(r"\btaught people\b"),
        "taught the people",
    ),
    (
        re.compile(r"\bpraising king\b"),
        "praising the king",
    ),
    (
        re.compile(r"\bentered to king\b"),
        "entered to the king",
    ),
    (
        re.compile(r"\bannounced to king all words\b"),
        "announced to the king all the words",
    ),
    (
        re.compile(r"\bwhen king heard\b"),
        "when the king heard",
    ),
    (
        re.compile(r"\bheard words of the law\b"),
        "heard the words of the law",
    ),
    (
        re.compile(r"\bwords of the Lord refined\b"),
        "the words of the Lord refined",
    ),
    (
        re.compile(r"\bprovoked words of God\b"),
        "provoked the words of God",
    ),
    (
        re.compile(r"\bAll words of God\b"),
        "All the words of God",
    ),
    (
        re.compile(r"\bwords of wise\b"),
        "words of the wise",
    ),
    (
        re.compile(r"\ball words of the Lord\b"),
        "all the words of the Lord",
    ),
    (
        re.compile(r"\bread in the scroll words of the Lord\b"),
        "read in the scroll the words of the Lord",
    ),
    (
        re.compile(r"\bhear words of the Lord\b"),
        "hear the words of the Lord",
    ),
    (
        re.compile(r"\blike woman\b"),
        "like a woman",
    ),
    (
        re.compile(r"\blike vessel\b"),
        "like a vessel",
    ),
    (
        re.compile(r"\blike hammer\b"),
        "like a hammer",
    ),
    (
        re.compile(r"\blike arrow\b"),
        "like an arrow",
    ),
    (
        re.compile(r"\blike dragon\b"),
        "like a dragon",
    ),
    (
        re.compile(r"\blike adversary\b"),
        "like an adversary",
    ),
    (
        re.compile(r"\blike enemy\b"),
        "like an enemy",
    ),
    (
        re.compile(r"\blike barber's razor\b"),
        "like a barber's razor",
    ),
    (
        re.compile(r"\blike barber’s razor\b"),
        "like a barber's razor",
    ),
    (
        re.compile(r"\blike bride\b"),
        "like a bride",
    ),
    (
        re.compile(r"\blike firebrand\b"),
        "like a firebrand",
    ),
    (
        re.compile(r"\blike torch\b"),
        "like a torch",
    ),
    (
        re.compile(r"\blike angel\b"),
        "like an angel",
    ),
    (
        re.compile(r"\bvine will give its fruit, land will give its produce\b"),
        "the vine will give its fruit, the land will give its produce",
    ),
    (
        re.compile(r"\bFast of fourth and fast of fifth and fast of seventh and fast of tenth\b"),
        "The fast of the fourth and the fast of the fifth and the fast of the seventh and the fast of the tenth",
    ),
    (
        re.compile(r"\bforming spirit of human\b"),
        "forming the spirit of a human",
    ),
    (
        re.compile(r"\bfrom line of sons of Israel\b"),
        "from the line of the sons of Israel",
    ),
    (
        re.compile(r"\bwith commander of the king\b"),
        "with the commander of the king",
    ),
    (
        re.compile(r"^And commander of the king\b"),
        "And the commander of the king",
    ),
    (
        re.compile(r"\bbehold, commander of Greeks\b"),
        "behold, the commander of Greeks",
    ),
    (
        re.compile(r"\bone of first rulers\b"),
        "one of the first rulers",
    ),
    (
        re.compile(r"\bking of Assyrians\b"),
        "king of the Assyrians",
    ),
    (
        re.compile(r"\bking of Persians\b"),
        "king of the Persians",
    ),
    (
        re.compile(r"\bking of north\b"),
        "king of the north",
    ),
    (
        re.compile(r"\bas house of Ahab\b"),
        "as the house of Ahab",
    ),
    (
        re.compile(r"\blet house of David\b"),
        "let the house of David",
    ),
    (
        re.compile(r"\blike house of David\b"),
        "like the house of David",
    ),
    (
        re.compile(r"\band house of David like house of God\b"),
        "and the house of David like the house of God",
    ),
    (
        re.compile(r"\bgathered house of Judah\b"),
        "gathered the house of Judah",
    ),
    (
        re.compile(r"\bhouse of Jacob will inherit\b"),
        "the house of Jacob will inherit",
    ),
    (
        re.compile(r"\bIn Israel going out from Egypt, house of Jacob\b"),
        "In Israel going out from Egypt, the house of Jacob",
    ),
    (
        re.compile(r"(?<!the )\bark of God\b"),
        "the ark of God",
    ),
    (
        re.compile(r"\bthe ark of covenant\b"),
        "the ark of the covenant",
    ),
    (
        re.compile(r"(?<!the )\bark of covenant\b"),
        "the ark of the covenant",
    ),
    (
        re.compile(r"\bof law of God\b"),
        "of the law of God",
    ),
    (
        re.compile(r"\bto law of God\b"),
        "to the law of God",
    ),
    (
        re.compile(r"\bfrom law of God\b"),
        "from the law of God",
    ),
    (
        re.compile(r"\bheed law of God\b"),
        "heed the law of God",
    ),
    (
        re.compile(r"\b(pursuing|recount|surround you and|beneath) glory of God\b"),
        r"\1 the glory of God",
    ),
    (
        re.compile(r"\band glory of God will\b"),
        "and the glory of God will",
    ),
    (
        re.compile(r"(?<![Tt]he )\bglory of God of Israel\b"),
        "the glory of God of Israel",
    ),
    (
        re.compile(r"\bglory of God of Israel was\b"),
        "the glory of God of Israel was",
    ),
    (
        re.compile(r"\bBehold, glory of God of Israel\b"),
        "Behold, the glory of God of Israel",
    ),
    (
        re.compile(r"\bgladdens heart of man\b"),
        "gladdens the heart of man",
    ),
    (
        re.compile(r"\bbread strengthens heart of man\b"),
        "bread strengthens the heart of man",
    ),
    (
        re.compile(r"\bto brighten face with oil\b"),
        "to brighten the face with oil",
    ),
    (
        re.compile(r"\bglorify remnant of Israel\b"),
        "glorify the remnant of Israel",
    ),
    (
        re.compile(r"\btoward mountains of Israel\b"),
        "toward the mountains of Israel",
    ),
    (
        re.compile(r"\bover mountains of Israel\b"),
        "over the mountains of Israel",
    ),
    (
        re.compile(r"\bto mountains of Israel\b"),
        "to the mountains of Israel",
    ),
    (
        re.compile(r"\bin sound of trumpet\b"),
        "with the sound of a trumpet",
    ),
    (
        re.compile(r"(?<!the )\bmouth of ungodly\b"),
        "the mouth of the ungodly",
    ),
    (
        re.compile(r"(?<!the )\bcamp of Philistines\b"),
        "the camp of the Philistines",
    ),
    (
        re.compile(r"\bcharges of tent of testimony\b"),
        "charges of the tent of testimony",
    ),
    (
        re.compile(r"\bcharges of sons of Aaron\b"),
        "charges of the sons of Aaron",
    ),
    (
        re.compile(r"\bdedicated house of God\b"),
        "dedicated the house of God",
    ),
    (
        re.compile(r"\bdestroy house of David\b"),
        "destroy the house of David",
    ),
    (
        re.compile(r"\blike house of Ahab\b"),
        "like the house of Ahab",
    ),
    (
        re.compile(r"\bavenged house of Ahab\b"),
        "avenged the house of Ahab",
    ),
    (
        re.compile(r"\bpulled down house of God\b"),
        "pulled down the house of God",
    ),
    (
        re.compile(r"\bhonored the people and house of God\b"),
        "honored the people and the house of God",
    ),
    (
        re.compile(r"\bopposite house of God\b"),
        "opposite the house of God",
    ),
    (
        re.compile(r"\babove house of David\b"),
        "above the house of David",
    ),
    (
        re.compile(r"\bWhy was house of God forsaken\b"),
        "Why was the house of God forsaken",
    ),
    (
        re.compile(r"\bas far as house of God\b"),
        "as far as the house of God",
    ),
    (
        re.compile(r"\bhe blessed house of Israel\b"),
        "he blessed the house of Israel",
    ),
    (
        re.compile(r"\bhe blessed house of Aaron\b"),
        "he blessed the house of Aaron",
    ),
    (
        re.compile(r"\bLet house of Israel say\b"),
        "Let the house of Israel say",
    ),
    (
        re.compile(r"\bLet house of Aaron say\b"),
        "Let the house of Aaron say",
    ),
    (
        re.compile(r"\bhouse of God will be manifest\b"),
        "the house of God will be manifest",
    ),
    (
        re.compile(r"\bhouse of Jacob in snare\b"),
        "the house of Jacob in snare",
    ),
    (
        re.compile(r"\bhouse of Judah will come\b"),
        "the house of Judah will come",
    ),
    (
        re.compile(r"\bso house of Israel proved faithless\b"),
        "so the house of Israel proved faithless",
    ),
    (
        re.compile(r"\bBecause in faithlessness house of Israel and house of Judah\b"),
        "Because in faithlessness the house of Israel and the house of Judah",
    ),
    (
        re.compile(r"\band house of Judah broke\b"),
        "and the house of Judah broke",
    ),
    (
        re.compile(r"\bof the house of Israel and house of Judah\b"),
        "of the house of Israel and the house of Judah",
    ),
    (
        re.compile(r"\bbrought up house of Israel\b"),
        "brought up the house of Israel",
    ),
    (
        re.compile(r"\bremnant of Israel will\b"),
        "the remnant of Israel will",
    ),
    (
        re.compile(r"\bpeople, remnant of Israel\b"),
        "people, the remnant of Israel",
    ),
    (
        re.compile(r"\band remnant of Judah perish\b"),
        "and the remnant of Judah perish",
    ),
    (
        re.compile(r"\bwipe out remnant of Israel\b"),
        "wipe out the remnant of Israel",
    ),
    (
        re.compile(r"\bbringing remnant of Israel to an end\b"),
        "bringing the remnant of Israel to an end",
    ),
    (
        re.compile(r"\breceive remnant of Israel\b"),
        "receive the remnant of Israel",
    ),
    (
        re.compile(r"\bcloud of glory of the Lord\b"),
        "cloud of the glory of the Lord",
    ),
    (
        re.compile(r"\band glory of the Lord upon\b"),
        "and the glory of the Lord upon",
    ),
    (
        re.compile(r"\bLet glory of the Lord\b"),
        "Let the glory of the Lord",
    ),
    (
        re.compile(r"\bbecause great glory of the Lord\b"),
        "because great is the glory of the Lord",
    ),
    (
        re.compile(r"\beclipse of glory of Jacob\b"),
        "eclipse of the glory of Jacob",
    ),
    (
        re.compile(r"\bsee glory of the Lord\b"),
        "see the glory of the Lord",
    ),
    (
        re.compile(r"\band glory of the Lord has risen\b"),
        "and the glory of the Lord has risen",
    ),
    (
        re.compile(r"\bearth glory of Israel\b"),
        "earth the glory of Israel",
    ),
    (
        re.compile(r"\bof likeness of glory of the Lord\b"),
        "of likeness of the glory of the Lord",
    ),
    (
        re.compile(r"\bBlessed glory of the Lord\b"),
        "Blessed be the glory of the Lord",
    ),
    (
        re.compile(r"\bthere glory of the Lord stood\b"),
        "there the glory of the Lord stood",
    ),
    (
        re.compile(r"\bthere was glory of the Lord\b"),
        "there was the glory of the Lord",
    ),
    (
        re.compile(r"\bbrightness of glory of the Lord\b"),
        "brightness of the glory of the Lord",
    ),
    (
        re.compile(r"\bfull of glory of the Lord\b"),
        "full of the glory of the Lord",
    ),
    (
        re.compile(r"\bknow glory of the Lord\b"),
        "know the glory of the Lord",
    ),
    (
        re.compile(r"\bwhere ark of the Lord entered\b"),
        "where the ark of the Lord entered",
    ),
    (
        re.compile(r"\bbook of law of Moses\b"),
        "book of the law of Moses",
    ),
    (
        re.compile(r"\bhear law of God\b"),
        "hear the law of God",
    ),
    (
        re.compile(r"\bRemember law of Moses\b"),
        "Remember the law of Moses",
    ),
    (
        re.compile(r"\bthis is City of David\b"),
        "this is the City of David",
    ),
    (
        re.compile(r"\bcalled it City of David\b"),
        "called it the City of David",
    ),
    (
        re.compile(r"\b(to|into|in|from|as far as|beside|with|of|toward|outside) City of David\b"),
        r"\1 the City of David",
    ),
    (
        re.compile(r"\b(upper outlet of water of Gihon and directed them down toward south of|supporting-wall of|wall outside) City of David\b"),
        r"\1 the City of David",
    ),
    (
        re.compile(r"\b(over|by|after|strike) tribes of Israel\b"),
        r"\1 the tribes of Israel",
    ),
    (
        re.compile(r"\bmade tribes of Israel dwell\b"),
        "made the tribes of Israel dwell",
    ),
    (
        re.compile(r"\band tribes of Israel attached\b"),
        "and the tribes of Israel attached",
    ),
    (
        re.compile(r"\b([Ii]n|until|was) (?:the )?([a-z-]+) year of reign of\b"),
        r"\1 the \2 year of the reign of",
    ),
    (
        re.compile(r"\b(in) (?:the )?([a-z-]+) year of reign of\b"),
        r"\1 the \2 year of the reign of",
    ),
    (
        re.compile(r"\b([Ff]rom|out of|enter|entered|strike|destroy|midst of|wilderness of|make|give|gave him) land of Egypt\b"),
        r"\1 the land of Egypt",
    ),
    (
        re.compile(r"\b(?<!the )land of Egypt\b"),
        "the land of Egypt",
    ),
    (
        re.compile(r"\b([Hh]ear|hearing|heard|hears) sound of trumpet\b"),
        r"\1 the sound of a trumpet",
    ),
    (
        re.compile(r"\bhearing sound of trumpets\b"),
        "hearing the sound of trumpets",
    ),
    (
        re.compile(r"\bwith sound of trumpet\b"),
        "with the sound of a trumpet",
    ),
    (
        re.compile(r"\b(voice|Voice) of trumpet\b"),
        r"\1 of a trumpet",
    ),
    (
        re.compile(r"\bworks of hands of men\b"),
        "works of the hands of men",
    ),
    (
        re.compile(r"\bweakens hands of men fighting\b"),
        "weakens the hands of men fighting",
    ),
    (
        re.compile(r"\bIn good heart of man\b"),
        "In the good heart of man",
    ),
    (
        re.compile(r"\bLet heart of man\b"),
        "Let the heart of man",
    ),
    (
        re.compile(r"\bBefore crushing heart of man\b"),
        "Before crushing the heart of man",
    ),
    (
        re.compile(r"\brestore heart of father to son and heart of man\b"),
        "restore the heart of father to son and the heart of man",
    ),
    (
        re.compile(r"(?<!the )\bspirit of life\b"),
        "the spirit of life",
    ),
    (
        re.compile(r"(?<!the )\btrees of forest\b"),
        "trees of the forest",
    ),
    (
        re.compile(r"(?<!the )\btent of testimony\b"),
        "the tent of testimony",
    ),
    (
        re.compile(r"\bas good hand of God\b"),
        "as the good hand of God",
    ),
    (
        re.compile(r"\bof hand of God\b"),
        "of the hand of God",
    ),
    (
        re.compile(r"(?<!the )\bgates of Jerusalem\b"),
        "the gates of Jerusalem",
    ),
    (
        re.compile(r"(?<!the )\bgates of death\b"),
        "the gates of death",
    ),
    (
        re.compile(r"\bway of righteous men\b"),
        "the way of righteous men",
    ),
    (
        re.compile(r"\bway of ungodly men\b"),
        "the way of ungodly men",
    ),
    (
        re.compile(r"\bway of ungodly\b"),
        "the way of ungodly",
    ),
    (
        re.compile(r"\bWhy does way of ungodly\b"),
        "Why does the way of ungodly",
    ),
    (
        re.compile(r"\bFor ways of man\b"),
        "For the ways of man",
    ),
    (
        re.compile(r"\breproving ways of man\b"),
        "reproving the ways of man",
    ),
    (
        re.compile(r"\band ways of man\b"),
        "and the ways of man",
    ),
    (
        re.compile(r"\bgrows tree of life\b"),
        "grows the tree of life",
    ),
    (
        re.compile(r"\bgood desire tree of life\b"),
        "good desire is a tree of life",
    ),
    (
        re.compile(r"\bHealing tongue tree of life\b"),
        "A healing tongue is a tree of life",
    ),
    (
        re.compile(r"\bas days of tree of life\b"),
        "as days of the tree of life",
    ),
    (
        re.compile(r"(?<!the )\bday of Sabbaths\b"),
        "the day of Sabbaths",
    ),
    (
        re.compile(r"\bjudge city of bloods\b"),
        "judge the city of bloods",
    ),
    (
        re.compile(r"\bmountains of Israel will be desolated\b"),
        "the mountains of Israel will be desolated",
    ),
    (
        re.compile(r"\blest house of Joseph\b"),
        "lest the house of Joseph",
    ),
    (
        re.compile(r"\bhouse of Joseph flame\b"),
        "the house of Joseph flame",
    ),
    (
        re.compile(r"\band house of Joseph I will\b"),
        "and the house of Joseph I will",
    ),
    (
        re.compile(r"\bfruit of womb\b"),
        "fruit of the womb",
    ),
    (
        re.compile(r"\bgive land of Canaan\b"),
        "give the land of Canaan",
    ),
    (
        re.compile(r"\b([Mm]ay) name of God\b"),
        r"\1 the name of God",
    ),
    (
        re.compile(r"\bpraise name of God\b"),
        "praise the name of God",
    ),
    (
        re.compile(r"\bgladden city of God\b"),
        "gladden the city of God",
    ),
    (
        re.compile(r"\bwater of sea\b"),
        "the water of the sea",
    ),
    (
        re.compile(r"\bwhole house of Judah\b"),
        "the whole house of Judah",
    ),
    (
        re.compile(r"\bwhole house of Israel\b"),
        "the whole house of Israel",
    ),
    (
        re.compile(r"\bthe house of Israel and house of Judah\b"),
        "the house of Israel and the house of Judah",
    ),
    (
        re.compile(r"\bPerhaps house of Judah\b"),
        "Perhaps the house of Judah",
    ),
    (
        re.compile(r"\bJerusalem and house of Judah\b"),
        "Jerusalem and the house of Judah",
    ),
    (
        re.compile(r"\bhis flock, house of Judah\b"),
        "his flock, the house of Judah",
    ),
    (
        re.compile(r"\bwords of truth are\b"),
        "the words of truth are",
    ),
    (
        re.compile(r"\banswering words of truth\b"),
        "answering the words of truth",
    ),
    (
        re.compile(r"\buprightness, words of truth\b"),
        "uprightness, the words of truth",
    ),
    (
        re.compile(r"\bwas City of Letters\b"),
        "was the City of Letters",
    ),
    (
        re.compile(r"\band City of Letters\b"),
        "and the City of Letters",
    ),
    (
        re.compile(r"\bwas City of Arba\b"),
        "was the City of Arba",
    ),
    (
        re.compile(r"\band City of Arba\b"),
        "and the City of Arba",
    ),
    (
        re.compile(r"\babove Gate of Ephraim\b"),
        "above the Gate of Ephraim",
    ),
    (
        re.compile(r"\b(in|until) (?:the )?([a-z-]+) year of kingdom of\b"),
        r"\1 the \2 year of the kingdom of",
    ),
    (
        re.compile(r"\bRemember days of old\b"),
        "Remember the days of old",
    ),
    (
        re.compile(r"\bremembered days of old\b"),
        "remembered the days of old",
    ),
    (
        re.compile(r"\bJericho, city of palms\b"),
        "Jericho, the city of palms",
    ),
    (
        re.compile(r"\bpatriarchs of tribes of Israel\b"),
        "patriarchs of the tribes of Israel",
    ),
    (
        re.compile(r"\b(went through|attacked|upon|make|give desolate) cities of Judah\b"),
        r"\1 the cities of Judah",
    ),
    (
        re.compile(r"\band cities of Judah I will\b"),
        "and the cities of Judah I will",
    ),
    (
        re.compile(r"\bAnd cities of Judah\b"),
        "And the cities of Judah",
    ),
    (
        re.compile(r"\bknow heart of sons of men\b"),
        "know the heart of sons of men",
    ),
    (
        re.compile(r"\bright hand of poor man\b"),
        "the right hand of a poor man",
    ),
    (
        re.compile(r"\bright hand right hand of injustice\b"),
        "right hand, the right hand of injustice",
    ),
    (
        re.compile(r"\bWays of ungodly\b"),
        "The ways of ungodly",
    ),
    (
        re.compile(r"\bBut ways of ungodly\b"),
        "But the ways of ungodly",
    ),
    (
        re.compile(r"\bWays of righteous\b"),
        "The ways of righteous",
    ),
    (
        re.compile(r"\bguards ways of righteous life\b"),
        "guards the ways of righteous life",
    ),
    (
        re.compile(r"\bWords of wise\b"),
        "The words of wise",
    ),
    (
        re.compile(r"\bheight of men will\b"),
        "the height of men will",
    ),
    (
        re.compile(r"\bsee way of Egypt\b"),
        "see the way of Egypt",
    ),
    (
        re.compile(r"\breported to him words of Rabshakeh\b"),
        "reported to him the words of Rabshakeh",
    ),
    (
        re.compile(r"\btear apart strength of kings\b"),
        "tear apart the strength of kings",
    ),
    (
        re.compile(r"\bfor army of heaven\b"),
        "for the army of heaven",
    ),
    (
        re.compile(r"\bDo not hear words of prophets\b"),
        "Do not hear the words of prophets",
    ),
    (
        re.compile(r"\bmake land of Babylon\b"),
        "make the land of Babylon",
    ),
    (
        re.compile(r"\bgive them land of Israel\b"),
        "give them the land of Israel",
    ),
    (
        re.compile(r"\bbecause of blood of humans\b"),
        "because of the blood of humans",
    ),
    (
        re.compile(r"\bAnd heart of weak ones\b"),
        "And the heart of weak ones",
    ),
    (
        re.compile(r"\bAnd hand of man\b"),
        "And the hand of man",
    ),
    (
        re.compile(r"\bAnd gate of inner court faced gate of north\b"),
        "And the gate of the inner court faced the gate of the north",
    ),
    (
        re.compile(r"\bby way of gate between\b"),
        "by way of the gate between",
    ),
    (
        re.compile(r"\bby way of gate of the court\b"),
        "by way of the gate of the court",
    ),
    (
        re.compile(r"\bfor remnant of his inheritance\b"),
        "for the remnant of his inheritance",
    ),
    (
        re.compile(r"\bbefore remnant of this people\b"),
        "before the remnant of this people",
    ),
    (
        re.compile(r"\bAnd sons of the (exile|singers)\b"),
        r"And the sons of the \1",
    ),
    (
        re.compile(r"\bAnd export of horses\b"),
        "And the export of horses",
    ),
    (
        re.compile(r"\bAnd anger of the Lord\b"),
        "And the anger of the Lord",
    ),
    (
        re.compile(r"\bAnd arrogance of Israel\b"),
        "And the arrogance of Israel",
    ),
    (
        re.compile(r"\bAnd eyes of God\b"),
        "And the eyes of God",
    ),
    (
        re.compile(r"\bAnd force of (Pharaoh|Chaldeans|the king of Babylon)\b"),
        r"And the force of \1",
    ),
    (
        re.compile(r"\bAnd he burned house of the Lord\b"),
        "And he burned the house of the Lord",
    ),
    (
        re.compile(r"\band house of the king\b"),
        "and the house of the king",
    ),
    (
        re.compile(r"\ball houses of the city\b"),
        "all the houses of the city",
    ),
    (
        re.compile(r"\bAnd he measured (width|length) of\b"),
        r"And he measured the \1 of",
    ),
    (
        re.compile(r"\bAnd one of seraphim\b"),
        "And one of the seraphim",
    ),
    (
        re.compile(r"\bbroke down wall of Jerusalem\b"),
        "broke down the wall of Jerusalem",
    ),
    (
        re.compile(r"\band city was quiet\b"),
        "and the city was quiet",
    ),
    (
        re.compile(r"\bentered house of\b"),
        "entered the house of",
    ),
    (
        re.compile(r"\bsaw wisdom of Solomon and house which he built\b"),
        "saw the wisdom of Solomon and the house which he built",
    ),
    (
        re.compile(r"\bheard name of Solomon\b"),
        "heard the name of Solomon",
    ),
    (
        re.compile(r"\bthen answer was sent\b"),
        "then an answer was sent",
    ),
    (
        re.compile(r"\bfrom undertaking of his heart\b"),
        "from the undertaking of his heart",
    ),
    (
        re.compile(r"\bestablishes undertaking of his heart\b"),
        "establishes the undertaking of his heart",
    ),
    (
        re.compile(r"\baccording to blow of Midian\b"),
        "according to the blow of Midian",
    ),
    (
        re.compile(r"\bin way by sea\b"),
        "in the way by sea",
    ),
    (
        re.compile(r"\bin way toward Egypt\b"),
        "in the way toward Egypt",
    ),
    (
        re.compile(r"(?<!the )\bshadow of death\b"),
        "the shadow of death",
    ),
    (
        re.compile(r"\bbeasts of earth\b"),
        "beasts of the earth",
    ),
    (
        re.compile(r"\bface of field\b"),
        "face of the field",
    ),
    (
        re.compile(r"\bcloud filled house\b"),
        "cloud filled the house",
    ),
    (
        re.compile(r"\band court was filled\b"),
        "and the court was filled",
    ),
    (
        re.compile(r"\bstood upon mountain opposite\b"),
        "stood upon the mountain opposite",
    ),
    (
        re.compile(r"\bAnd all elders of Israel\b"),
        "And all the elders of Israel",
    ),
    (
        re.compile(r"\ball Levites took ark\b"),
        "all the Levites took the ark",
    ),
    (
        re.compile(r"\bAnd all leaders of force\b"),
        "And all the leaders of the force",
    ),
    (
        re.compile(r"\bin field\b"),
        "in the field",
    ),
    (
        re.compile(r"\bthat king of Babylon\b"),
        "that the king of Babylon",
    ),
    (
        re.compile(r"\bAnd dead bodies of\b"),
        "And the dead bodies of",
    ),
    (
        re.compile(r"\bbe example upon\b"),
        "be an example upon",
    ),
    (
        re.compile(r"\bAnd eyes of Zedekiah\b"),
        "And the eyes of Zedekiah",
    ),
    (
        re.compile(r"\band king of Babylon led\b"),
        "and the king of Babylon led",
    ),
    (
        re.compile(r"\bAnd the name of wife of Abishur\b"),
        "And the name of the wife of Abishur",
    ),
    (
        re.compile(r"\band name of their sister\b"),
        "and the name of their sister",
    ),
    (
        re.compile(r"\bholy is place where\b"),
        "holy is the place where",
    ),
    (
        re.compile(r"\bAnd all men of Judah and Benjamin\b"),
        "And all the men of Judah and Benjamin",
    ),
    (
        re.compile(r"\bbring ark of our God\b"),
        "bring the ark of our God",
    ),
    (
        re.compile(r"\bserved as priest in place of him\b"),
        "served as priest in his place",
    ),
    (
        re.compile(r"\b(reigned|reign|would reign|who will stand) in place of him\b"),
        r"\1 in his place",
    ),
    (
        re.compile(r"\bWho will give my death in place of you\? I, in place of you\b"),
        "Who will give my death instead of you? I, instead of you",
    ),
    (
        re.compile(r"\bmade bronze arms in place of them\b"),
        "made bronze arms in their place",
    ),
    (
        re.compile(r"\bput satraps in place of them\b"),
        "put satraps in their place",
    ),
    (
        re.compile(r"\bmake in place of them iron yokes\b"),
        "make iron yokes in their place",
    ),
    (
        re.compile(r"\bin place of every firstborn\b"),
        "instead of every firstborn",
    ),
    (
        re.compile(r"\bbeasts of field\b"),
        "beasts of the field",
    ),
    (
        re.compile(r"\ball beasts of the field\b"),
        "all the beasts of the field",
    ),
    (
        re.compile(r"\bfish of sea\b"),
        "fish of the sea",
    ),
    (
        re.compile(r"\breptiles of earth\b"),
        "reptiles of the earth",
    ),
    (
        re.compile(r"\bcreeping things creeping on earth\b"),
        "creeping things creeping on the earth",
    ),
    (
        re.compile(r"\bin wilderness\b"),
        "in the wilderness",
    ),
    (
        re.compile(r"\bIn wilderness\b"),
        "In the wilderness",
    ),
    (
        re.compile(r"\bfrom wilderness\b"),
        "from the wilderness",
    ),
    (
        re.compile(r"\binto wilderness\b"),
        "into the wilderness",
    ),
    (
        re.compile(r"\bto wilderness\b"),
        "to the wilderness",
    ),
    (
        re.compile(r"\bof wilderness\b"),
        "of the wilderness",
    ),
    (
        re.compile(r"\bin plain\b"),
        "in the plain",
    ),
    (
        re.compile(r"\bIn plain\b"),
        "In the plain",
    ),
    (
        re.compile(r"\binto plain\b"),
        "into the plain",
    ),
    (
        re.compile(r"\bfrom plain\b"),
        "from the plain",
    ),
    (
        re.compile(r"\bof plain\b"),
        "of the plain",
    ),
    (
        re.compile(r"\bin forest\b"),
        "in the forest",
    ),
    (
        re.compile(r"\bIn forest\b"),
        "In the forest",
    ),
    (
        re.compile(r"\bfrom forest\b"),
        "from the forest",
    ),
    (
        re.compile(r"\bto forest\b"),
        "to the forest",
    ),
    (
        re.compile(r"\bof forest\b"),
        "of the forest",
    ),
    (
        re.compile(r"\b(to|upon|from|in|into|of|by) river\b"),
        r"\1 the river",
    ),
    (
        re.compile(r"\bLet not king speak thus\b"),
        "Let not the king speak thus",
    ),
    (
        re.compile(r"\bexcept king of Israel only\b"),
        "except the king of Israel only",
    ),
    (
        re.compile(r"\bwhom king of Babylon appointed\b"),
        "whom the king of Babylon appointed",
    ),
    (
        re.compile(r"\band name of (?=(?:his|her|their|the|[A-Z]))"),
        "and the name of ",
    ),
    (
        re.compile(r"\bAnd name of (?=(?:his|her|their|the|[A-Z]))"),
        "And the name of ",
    ),
    (
        re.compile(r"\bCall name of Pharaoh\b"),
        "Call the name of Pharaoh",
    ),
    (
        re.compile(r"\bLet name of the great the Lord\b"),
        "Let the name of the great Lord",
    ),
    (
        re.compile(r"\bLet the name of the great the Lord\b"),
        "Let the name of the great Lord",
    ),
    (
        re.compile(r"\bpraise name of your boasting\b"),
        "praise the name of your boasting",
    ),
    (
        re.compile(r"\bbless name of your glory\b"),
        "bless the name of your glory",
    ),
    (
        re.compile(r"\bprofane name of their God\b"),
        "profane the name of their God",
    ),
    (
        re.compile(r"\bname of Israel will\b"),
        "the name of Israel will",
    ),
    (
        re.compile(r"\bthey made delightful land into destruction\b"),
        "they made the delightful land into destruction",
    ),
    (
        re.compile(r"\bsmell of perfume and light of lamp\b"),
        "the smell of perfume and the light of a lamp",
    ),
    (
        re.compile(r"\bbefore ark\b"),
        "before the ark",
    ),
    (
        re.compile(r"\bin ark\b"),
        "in the ark",
    ),
    (
        re.compile(r"\bbefore altar\b"),
        "before the altar",
    ),
    (
        re.compile(r"\bon altar\b"),
        "on the altar",
    ),
    (
        re.compile(r"\bupon altar\b"),
        "upon the altar",
    ),
    (
        re.compile(r"\bto altar\b"),
        "to the altar",
    ),
    (
        re.compile(r"\bfrom altar\b"),
        "from the altar",
    ),
    (
        re.compile(r"^(And|But|Because|For|Then) people\b"),
        r"\1 the people",
    ),
    (
        re.compile(r"^people\b"),
        "The people",
    ),
    (
        re.compile(r"\bdwelt in house from\b"),
        "dwelt in a house from",
    ),
    (
        re.compile(r"\bshut house so as not to enter\b"),
        "shut a house so as not to enter",
    ),
    (
        re.compile(r"\bbefore house\b"),
        "before the house",
    ),
    (
        re.compile(r"\bupon house\b"),
        "upon the house",
    ),
    (
        re.compile(r"\binto house which\b"),
        "into the house which",
    ),
    (
        re.compile(r"\binto house\b"),
        "into the house",
    ),
    (
        re.compile(r"\binto house,\b"),
        "into the house,",
    ),
    (
        re.compile(r"\bstrengthen house\b"),
        "strengthen the house",
    ),
    (
        re.compile(r"\bholy ark in house\b"),
        "holy ark in the house",
    ),
    (
        re.compile(r"\bstand in house\b"),
        "stand in the house",
    ),
    (
        re.compile(r"\bsolitary ones in house\b"),
        "solitary ones in a house",
    ),
    (
        re.compile(r"\bbarren woman in house\b"),
        "barren woman in a house",
    ),
    (
        re.compile(r"\bin house her feet\b"),
        "in the house her feet",
    ),
    (
        re.compile(r"\bfoods to house\b"),
        "foods to the house",
    ),
    (
        re.compile(r"\bthose in house\b"),
        "those in the house",
    ),
    (
        re.compile(r"\bset it in house\b"),
        "set it in a house",
    ),
    (
        re.compile(r"\bin house (over|on) which\b"),
        r"in the house \1 which",
    ),
    (
        re.compile(r"\bfrom house where\b"),
        "from the house where",
    ),
    (
        re.compile(r"\binside house\b"),
        "inside the house",
    ),
    (
        re.compile(r"\bsat in house\b"),
        "sat in the house",
    ),
    (
        re.compile(r"\bfrom house and settled\b"),
        "from the house and settled",
    ),
    (
        re.compile(r"\bbrought into house\b"),
        "brought into the house",
    ),
    (
        re.compile(r"\bbuild house, and I will take pleasure\b"),
        "build the house, and I will take pleasure",
    ),
    (
        re.compile(r"\bwill not build house\b"),
        "will not build a house",
    ),
    (
        re.compile(r"\bshall not build house\b"),
        "shall not build a house",
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
        re.compile(r"\b([Ff]rom) end of\b"),
        r"\1 the end of",
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
        re.compile(r"\b([Ff]rom) hill of\b"),
        r"\1 the hill of",
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
        re.compile(r"\b([Ff]rom) (half tribe|mountains|brothers|borders|chiefs|country|depths|height|families) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ff]rom) (affliction|snare|produce|king|cities|islands|wrath|dust|mount|sight|men) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ff]rom) breath of\b"),
        r"\1 the breath of",
    ),
    (
        re.compile(r"\b([Ff]rom) presence of\b"),
        r"\1 the presence of",
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
        re.compile(r"\b([Ii]n) wilderness of\b"),
        r"\1 the wilderness of",
    ),
    (
        re.compile(r"\b([Ii]n) (gladness|wandering) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]n) anger of\b"),
        r"\1 the anger of",
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
        re.compile(r"\b([Tt]o) bring ark of\b"),
        r"\1 bring the ark of",
    ),
    (
        re.compile(r"\b([Tt]o) (enter|strengthen) house of\b"),
        r"\1 \2 the house of",
    ),
    (
        re.compile(r"\b([Tt]o) bless house of\b"),
        r"\1 bless the house of",
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
        re.compile(r"\b([Tt]o) borders of sons of\b"),
        r"\1 the borders of the sons of",
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
        re.compile(r"\b([Tt]o) give inheritance of\b"),
        r"\1 give the inheritance of",
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
        re.compile(r"\b([Ff]or) (sacrifice|service|day|mouth|command|life|seed|time|light|people|salvation|bread|works) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ff]or) (wall|throne) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ff]or) work of\b"),
        r"\1 the work of",
    ),
    (
        re.compile(r"\b([Ff]or) sake of\b"),
        r"\1 the sake of",
    ),
    (
        re.compile(r"\b([Ff]or) (length|authority|words|days|rest) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ff]or) (ark|cities|nails|fine flour) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ff]or) remaining sons of\b"),
        r"\1 the remaining sons of",
    ),
    (
        re.compile(r"\bFor divisions of\b"),
        "For the divisions of",
    ),
    (
        re.compile(r"\b([Ff]or) half tribe of\b"),
        r"\1 the half tribe of",
    ),
    (
        re.compile(r"\b([Cc]oncerning) (words|favor) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Tt]o) drink water of\b"),
        r"\1 drink the water of",
    ),
    (
        re.compile(r"\b([Aa]t) voice of\b"),
        r"\1 the voice of",
    ),
    (
        re.compile(r"\b([Aa]t) dedication of\b"),
        r"\1 the dedication of",
    ),
    (
        re.compile(r"\b([Aa]t) mouth of\b"),
        r"\1 the mouth of",
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
        re.compile(r"\b([Ww]ith) elders of\b"),
        r"\1 the elders of",
    ),
    (
        re.compile(r"\belders of land\b"),
        "elders of the land",
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
        re.compile(r"\b([Aa]ccording to) ways of\b"),
        r"\1 the ways of",
    ),
    (
        re.compile(r"\b([Aa]ccording to) completion of\b"),
        r"\1 the completion of",
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
        re.compile(r"\b([Oo]n) servants of\b"),
        r"\1 the servants of",
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
        re.compile(r"\b([Bb]y) word of\b"),
        r"\1 the word of",
    ),
    (
        re.compile(r"\b([Bb]y) gates of\b"),
        r"\1 the gates of",
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
        re.compile(r"\b([Tt]oward) hands of\b"),
        r"\1 the hands of",
    ),
    (
        re.compile(r"\bkeeping charge of\b"),
        "keeping the charge of",
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
        re.compile(r"\b([Oo]ver) cleansing of\b"),
        r"\1 the cleansing of",
    ),
    (
        re.compile(r"\b([Oo]ver) faithlessness of\b"),
        r"\1 the faithlessness of",
    ),
    (
        re.compile(r"\b([Oo]ver) to souls of\b"),
        r"\1 to the souls of",
    ),
    (
        re.compile(r"\b([Oo]ver) third part of\b"),
        r"\1 the third part of",
    ),
    (
        re.compile(r"\b([Ii]nto) (depth|chamber|treasury-room) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]nto) cave of\b"),
        r"\1 the cave of",
    ),
    (
        re.compile(r"\b([Ii]nto) (depths|kingdom) of\b"),
        r"\1 the \2 of",
    ),
    (
        re.compile(r"\b([Ii]nto) height of\b"),
        r"\1 the height of",
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
        re.compile(r"\b([Ff]rom) there ark of\b"),
        r"\1 there the ark of",
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
        re.compile(r"\bking ([A-Z][A-Za-z-]+)"),
        r"King \1",
    ),
    (
        re.compile(r"\bthe King ([A-Z][A-Za-z-]+)"),
        r"King \1",
    ),
    (
        re.compile(r"\b([Aa]nd|[Bb]ut|[Bb]ecause|[Tt]hen) king (?=(?:said|commanded|answered|sent|went|came|stood|sat|swore|spoke|cried|removed|made|turned|rejoice|hopes|will|did|does|shall|was|heard|saw|gave|took|called|issued)\b)"),
        r"\1 the king ",
    ),
    (
        re.compile(r"\b([Aa]nd|[Bb]ecause) king and\b"),
        r"\1 the king and",
    ),
    (
        re.compile(r"\b([Bb]ecause) king of\b"),
        r"\1 the king of",
    ),
    (
        re.compile(r"\bof king\b"),
        "of the king",
    ),
    (
        re.compile(r"\bof people\b"),
        "of the people",
    ),
    (
        re.compile(r"\bof city\b"),
        "of the city",
    ),
    (
        re.compile(r"\bof house\b"),
        "of the house",
    ),
    (
        re.compile(r"\bof temple\b"),
        "of the temple",
    ),
    (
        re.compile(r"\b([Aa]ll) people\b"),
        r"\1 the people",
    ),
    (
        re.compile(r"\b([Aa]ll) assembly\b"),
        r"\1 the assembly",
    ),
    (
        re.compile(r"\b([Aa]ll) land\b"),
        r"\1 the land",
    ),
    (
        re.compile(r"\bAnd rest of\b"),
        "And the rest of",
    ),
    (
        re.compile(r"\bAnd beside border of\b"),
        "And beside the border of",
    ),
    (
        re.compile(r"\bAnd servants of\b"),
        "And the servants of",
    ),
    (
        re.compile(r"\bAnd angel of\b"),
        "And the angel of",
    ),
    (
        re.compile(r"\bAnd men of\b"),
        "And the men of",
    ),
    (
        re.compile(r"\bAnd people of\b"),
        "And the people of",
    ),
    (
        re.compile(r"\bAnd all people of\b"),
        "And all the people of",
    ),
    (
        re.compile(r"\bAnd king of\b"),
        "And the king of",
    ),
    (
        re.compile(r"\bAnd queen of\b"),
        "And the queen of",
    ),
    (
        re.compile(r"\bAnd name of\b"),
        "And the name of",
    ),
    (
        re.compile(r"\bAnd ark of\b"),
        "And the ark of",
    ),
    (
        re.compile(r"\bAnd word of\b"),
        "And the word of",
    ),
    (
        re.compile(r"\bBut word of\b"),
        "But the word of",
    ),
    (
        re.compile(r"\bBut hand of\b"),
        "But the hand of",
    ),
    (
        re.compile(r"\bFor heart of\b"),
        "For the heart of",
    ),
    (
        re.compile(r"\bAnd land of\b"),
        "And the land of",
    ),
    (
        re.compile(r"\bAnd house of Israel\b"),
        "And the house of Israel",
    ),
    (
        re.compile(r"\bBut house of Israel\b"),
        "But the house of Israel",
    ),
    (
        re.compile(r"\bHouse of (Israel|Aaron|Levi|Jacob|Joseph)\b"),
        r"The house of \1",
    ),
    (
        re.compile(r"\bBecause voice of\b"),
        "Because the voice of",
    ),
    (
        re.compile(r"\bVoice of (your|many|one|ones|my|cry|report|fear|criers|daughter)\b"),
        r"The voice of \1",
    ),
    (
        re.compile(r"\bMouth of\b"),
        "The mouth of",
    ),
    (
        re.compile(r"\bHand of our God\b"),
        "The hand of our God",
    ),
    (
        re.compile(r"\bRiver of God\b"),
        "The river of God",
    ),
    (
        re.compile(r"\bMountain of God\b"),
        "The mountain of God",
    ),
    (
        re.compile(r"\bKing of Babylon heard\b"),
        "The king of Babylon heard",
    ),
    (
        re.compile(r"\bPeople of the land, oppressing\b"),
        "The people of the land, oppressing",
    ),
    (
        re.compile(r"\bRemnant of Israel will\b"),
        "The remnant of Israel will",
    ),
    (
        re.compile(r"\bAnd rulers of\b"),
        "And the rulers of",
    ),
    (
        re.compile(r"\bAnd remnant of\b"),
        "And the remnant of",
    ),
    (
        re.compile(r"\bAnd glory of\b"),
        "And the glory of",
    ),
    (
        re.compile(r"\bBecause of multitude of\b"),
        "Because of the multitude of",
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
        re.compile(r"\b([Aa]fter) gods of\b"),
        r"\1 the gods of",
    ),
    (
        re.compile(r"\b([Aa]t) hearing of\b"),
        r"\1 the hearing of",
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
        re.compile(r"\bby Lord\b"),
        "by the Lord",
    ),
    (
        re.compile(r"\bfears Lord\b"),
        "fears the Lord",
    ),
    (
        re.compile(r"\bhear voice of his servant\b"),
        "hear the voice of his servant",
    ),
    (
        re.compile(r"\bname of the city is\b"),
        "the name of the city is",
    ),
    (
        re.compile(r"\band land will be cleansed\b"),
        "and the land will be cleansed",
    ),
    (
        re.compile(r"(?<!a )\bhouse of refuge\b"),
        "a house of refuge",
    ),
    (
        re.compile(r"\bhouse of kingdom\b"),
        "house of the kingdom",
    ),
    (
        re.compile(r"\bhouse of lawless one\b"),
        "house of a lawless one",
    ),
    (
        re.compile(r"\benter house of thief\b"),
        "enter the house of the thief",
    ),
    (
        re.compile(r"\band house of one swearing falsely\b"),
        "and the house of the one swearing falsely",
    ),
    (
        re.compile(r"\bThe heart of wise\b"),
        "The heart of the wise",
    ),
    (
        re.compile(r"\bThe heart of fool\b"),
        "The heart of a fool",
    ),
    (
        re.compile(r"\band heart of fools\b"),
        "and the heart of fools",
    ),
    (
        re.compile(r"\bbut heart of fools\b"),
        "but the heart of fools",
    ),
    (
        re.compile(r"\band heart of rulers\b"),
        "and the heart of the rulers",
    ),
    (
        re.compile(r"\bheart of the king will perish\b"),
        "the heart of the king will perish",
    ),
    (
        re.compile(r"\bvoice of weeping and voice of cry\b"),
        "the voice of weeping and the voice of cry",
    ),
    (
        re.compile(r"\bsaid to Levites\b"),
        "said to the Levites",
    ),
    (
        re.compile(r"\brulers of Levites\b"),
        "rulers of the Levites",
    ),
    (
        re.compile(r"\bcontributed to Levites\b"),
        "contributed to the Levites",
    ),
    (
        re.compile(r"\bplaced holy ark\b"),
        "placed the holy ark",
    ),
    (
        re.compile(r"\bKing said\b"),
        "The king said",
    ),
    (
        re.compile(r"\bbuilt, The king said\b"),
        "built, and the king said",
    ),
    (
        re.compile(r"\bcarry anything on shoulders\b"),
        "carry anything on your shoulders",
    ),
    (
        re.compile(r"\bfor continual whole burnt offering\b"),
        "for the continual whole burnt offering",
    ),
    (
        re.compile(r"\band words I put\b"),
        "and the words I put",
    ),
    (
        re.compile(r"\bGreat his rule\b"),
        "Great is his rule",
    ),
    (
        re.compile(r"\bZeal of the Lord of hosts\b"),
        "The zeal of the Lord of hosts",
    ),
    (
        re.compile(r"\bso that remnant of men and all nations upon whom my name was called upon them may seek\b"),
        "so that the remnant of men and all nations upon whom my name has been called may seek",
    ),
    (
        re.compile(r"\bbring third through fire\b"),
        "bring the third through fire",
    ),
    (
        re.compile(r"\bhe will say, the Lord is my God\b"),
        "he will say, The Lord is my God",
    ),
    (
        re.compile(r"\bthis one is God of gods\b"),
        "this one is the God of gods",
    ),
    (
        re.compile(r"\bhe is God of gods\b"),
        "he is the God of gods",
    ),
    (
        re.compile(r"\byour God is God of gods\b"),
        "your God is the God of gods",
    ),
    (
        re.compile(r"\bGod of heaven will set up\b"),
        "the God of heaven will set up",
    ),
    (
        re.compile(r"\bGod of heaven has authority\b"),
        "the God of heaven has authority",
    ),
    (
        re.compile(r"\bGod of heaven did in me\b"),
        "the God of heaven did in me",
    ),
    (
        re.compile(r"\bagainst God of gods\b"),
        "against the God of gods",
    ),
    (
        re.compile(r"\bservants of God of gods\b"),
        "servants of the God of gods",
    ),
    (
        re.compile(r"\bservants of God of heaven and earth\b"),
        "servants of the God of heaven and earth",
    ),
    (
        re.compile(r"\bprovoked God of heaven\b"),
        "provoked the God of heaven",
    ),
    (
        re.compile(r"\bbefore God of heaven\b"),
        "before the God of heaven",
    ),
    (
        re.compile(r"\bprayed to God of heaven\b"),
        "prayed to the God of heaven",
    ),
    (
        re.compile(r"\bprayed to God of gods\b"),
        "prayed to the God of gods",
    ),
    (
        re.compile(r"\bserve God of heaven\b"),
        "serve the God of heaven",
    ),
    (
        re.compile(r"\bspeaks against God of heaven\b"),
        "speaks against the God of heaven",
    ),
    (
        re.compile(r"\bto God of heaven\b"),
        "to the God of heaven",
    ),
    (
        re.compile(r"\bof God of heaven\b"),
        "of the God of heaven",
    ),
    (
        re.compile(r"\bGod of heaven, he will\b"),
        "The God of heaven, he will",
    ),
    (
        re.compile(r"\bGod of gods, Lord, spoke\b"),
        "The God of gods, the Lord, spoke",
    ),
    (
        re.compile(r"\bGod of gods will be seen\b"),
        "the God of gods will be seen",
    ),
    (
        re.compile(r"\bGive thanks to God of gods\b"),
        "Give thanks to the God of gods",
    ),
    (
        re.compile(r"\bGive thanks to God of heaven\b"),
        "Give thanks to the God of heaven",
    ),
    (
        re.compile(r"\bin the shelter of God of heaven\b"),
        "in the shelter of the God of heaven",
    ),
    (
        re.compile(r"\bremoving kingdom from kings\b"),
        "removing a kingdom from kings",
    ),
    (
        re.compile(r"\bAll days of my kingdom\b"),
        "All the days of my kingdom",
    ),
    (
        re.compile(r"\bas sweet smell to the Lord\b"),
        "as a sweet smell to the Lord",
    ),
    (
        re.compile(r"\boffer sacrifice and offering\b"),
        "offer a sacrifice and an offering",
    ),
    (
        re.compile(r"\bsound of shout of joy\b"),
        "the sound of a shout of joy",
    ),
    (
        re.compile(r"\bsound of wings\b"),
        "the sound of wings",
    ),
    (
        re.compile(r"\bsound of harmony\b"),
        "the sound of harmony",
    ),
    (
        re.compile(r"\bsound of cry\b"),
        "the sound of a cry",
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
        re.compile(r"\bmother, that you bore me, man being judged\b"),
        "mother, that you bore me, a man being judged",
    ),
    (
        re.compile(r"\bbecause no man from his seed will grow, sitting\b"),
        "because no man from his seed will grow up to sit",
    ),
    (
        re.compile(r"\bwhen chiefs of\b"),
        "when the chiefs of",
    ),
    (
        re.compile(r"\bBlessed are you, land whose king son of nobles\b"),
        "Blessed are you, land whose king is son of nobles",
    ),
    (
        re.compile(r"\bStrength of the enemies was crushed\b"),
        "The strength of the enemies was crushed",
    ),
    (
        re.compile(r"\bBeauties of the wilderness will grow fat, and hills will gird\b"),
        "The beauties of the wilderness will grow fat, and the hills will gird",
    ),
    (
        re.compile(r"\bQuarter of you will be consumed\b"),
        "A quarter of you will be consumed",
    ),
    (
        re.compile(r"\band quarter of you finished\b"),
        "and a quarter of you finished",
    ),
    (
        re.compile(r"\band quarter I will scatter\b"),
        "and a quarter I will scatter",
    ),
    (
        re.compile(r"\band quarter will fall\b"),
        "and a quarter will fall",
    ),
    (
        re.compile(r"\bWise will inherit glory, but ungodly exalt dishonor\b"),
        "The wise will inherit glory, but the ungodly exalt dishonor",
    ),
    (
        re.compile(r"\bWise hide perception, but mouth of rash approaches ruin\b"),
        "The wise hide perception, but the mouth of the rash approaches ruin",
    ),
    (
        re.compile(r"\bWise women of her princesses answered\b"),
        "The wise women of her princesses answered",
    ),
    (
        re.compile(r"\bWise men were ashamed\b"),
        "The wise men were ashamed",
    ),
    (
        re.compile(r"\bBecause thought of man will confess to you, and remnant of thought will celebrate feast to you\b"),
        "Because the thought of man will confess to you, and the remnant of thought will celebrate feast to you",
    ),
    (
        re.compile(r"\bthe Lord of hosts will be crown of hope, woven thing of glory\b"),
        "the Lord of hosts will be a crown of hope, a woven thing of glory",
    ),
    (
        re.compile(r"\bSo then will be end of all who forget Lord, for hope of the ungodly\b"),
        "So then will be the end of all who forget the Lord, for the hope of the ungodly",
    ),
    (
        re.compile(r"\bGood ones will be inhabitants of earth\b"),
        "Good ones will be inhabitants of the earth",
    ),
    (
        re.compile(r"\bstraight ones will settle in earth\b"),
        "straight ones will settle in the earth",
    ),
    (
        re.compile(r"\bit will be camp of sirens and courtyard of ostriches\b"),
        "it will be a camp of sirens and a courtyard of ostriches",
    ),
    (
        re.compile(r"\bthere will be spring of water\b"),
        "there will be a spring of water",
    ),
    (
        re.compile(r"\bThere joy of birds, camp of reed and marsh\b"),
        "There will be joy of birds, a camp of reed and marsh",
    ),
    (
        re.compile(r"\bYou will be crown of beauty\b"),
        "You will be a crown of beauty",
    ),
    (
        re.compile(r"\bCrete will be pasture of flocks and sheepfold\b"),
        "Crete will be a pasture of flocks and a sheepfold",
    ),
    (
        re.compile(r"\bThis will be sin of Egypt and sin of all nations\b"),
        "This will be the sin of Egypt and the sin of all nations",
    ),
    (
        re.compile(r"\bThis is house of the Lord God, and this is altar\b"),
        "This is the house of the Lord God, and this is the altar",
    ),
    (
        re.compile(r"\bthis is place of those not knowing Lord\b"),
        "this is the place of those not knowing the Lord",
    ),
    (
        re.compile(r"\bThis is portion of ungodly man from the Lord\b"),
        "This is the portion of an ungodly man from the Lord",
    ),
    (
        re.compile(r"\bwhat is place of darkness\b"),
        "what is the place of darkness",
    ),
    (
        re.compile(r"\bit is gift of God\b"),
        "it is a gift of God",
    ),
    (
        re.compile(r"\bNear is day of Moab\b"),
        "Near is the day of Moab",
    ),
    (
        re.compile(r"\bThat day is day of wrath\b"),
        "That day is a day of wrath",
    ),
    (
        re.compile(r"\bhe is messenger of the Lord Almighty\b"),
        "he is a messenger of the Lord Almighty",
    ),
    (
        re.compile(r"\bwas man of war\b"),
        "was a man of war",
    ),
    (
        re.compile(r"\bthere was oversized man\b"),
        "there was an oversized man",
    ),
    (
        re.compile(r"\bhe was descendant of giants\b"),
        "he was a descendant of giants",
    ),
    (
        re.compile(r"\bthere was prophet of the Lord there\b"),
        "there was a prophet of the Lord there",
    ),
    (
        re.compile(r"\bFor righteous and blameless man became object of mockery\b"),
        "For a righteous and blameless man became an object of mockery",
    ),
    (
        re.compile(r"\bStone which builders rejected, this became head of corner\b"),
        "The stone which builders rejected, this became the head of the corner",
    ),
    (
        re.compile(r"\bit became torment of their injustices\b"),
        "it became a torment of their injustices",
    ),
    (
        re.compile(r"\bthis will be downfall of horses\b"),
        "this will be the downfall of horses",
    ),
    (
        re.compile(r"\bwhich is city of Scythians\b"),
        "which is a city of Scythians",
    ),
    (
        re.compile(r"\bShe is mother of Onam\b"),
        "She is the mother of Onam",
    ),
    (
        re.compile(r"\bin which is covenant of the Lord\b"),
        "in which is the covenant of the Lord",
    ),
    (
        re.compile(r"\bIt is king of Israel\b"),
        "It is the king of Israel",
    ),
    (
        re.compile(r"\bHe is son of Jehoshaphat\b"),
        "He is a son of Jehoshaphat",
    ),
    (
        re.compile(r"\bthis is copy of decree\b"),
        "this is a copy of the decree",
    ),
    (
        re.compile(r"\bin his hand is soul of every living thing\b"),
        "in his hand is the soul of every living thing",
    ),
    (
        re.compile(r"\bWhere is house of ruler\b"),
        "Where is the house of a ruler",
    ),
    (
        re.compile(r"\bwhere is shelter of tents of ungodly men\b"),
        "where is the shelter of tents of ungodly men",
    ),
    (
        re.compile(r"\bWho is father of rain\b"),
        "Who is the father of rain",
    ),
    (
        re.compile(r"\bOr is arm of yours against the Lord\b"),
        "Or is your arm against the Lord",
    ),
    (
        re.compile(r"\bit is king of all things in waters\b"),
        "it is the king of all things in waters",
    ),
    (
        re.compile(r"\bwhere is wrath of one afflicting you\b"),
        "where is the wrath of one afflicting you",
    ),
    (
        re.compile(r"\bWhere is your zeal and strength\? Where is multitude of your mercy\b"),
        "Where is your zeal and strength? Where is the multitude of your mercy",
    ),
    (
        re.compile(r"\bis portion of Jacob\b"),
        "is the portion of Jacob",
    ),
    (
        re.compile(r"\bit is land of carved images\b"),
        "it is a land of carved images",
    ),
    (
        re.compile(r"\bthere is day of calling of defenders\b"),
        "there is a day of calling of defenders",
    ),
    (
        re.compile(r"\bThis is law of the house\b"),
        "This is the law of the house",
    ),
    (
        re.compile(r"\bThis is height of the altar\b"),
        "This is the height of the altar",
    ),
    (
        re.compile(r"\bThis is interpretation of the writing\b"),
        "This is the interpretation of the writing",
    ),
    (
        re.compile(r"\bis king of Medes and Persians\b"),
        "is the king of Medes and Persians",
    ),
    (
        re.compile(r"\bis king of Greeks\b"),
        "is the king of Greeks",
    ),
    (
        re.compile(r"\bis first king\b"),
        "is the first king",
    ),
    (
        re.compile(r"\bWhen then is completion of these wonders\b"),
        "When then is the completion of these wonders",
    ),
    (
        re.compile(r"\bwhat is solution of this word\b"),
        "what is the solution of this word",
    ),
    (
        re.compile(r"\bit is sanctuary of the king and house of the kingdom\b"),
        "it is the sanctuary of the king and the house of the kingdom",
    ),
    (
        re.compile(r"\bWhat is impiety of Jacob\? Is it not Samaria\? And what is sin of the house of Judah\b"),
        "What is the impiety of Jacob? Is it not Samaria? And what is the sin of the house of Judah",
    ),
    (
        re.compile(r"\bWhere is dwelling of lions\b"),
        "Where is the dwelling of lions",
    ),
    (
        re.compile(r"\bHe was priest of God Most High\b"),
        "He was a priest of God Most High",
    ),
    (
        re.compile(r"\bTimnah was concubine of Eliphaz\b"),
        "Timnah was a concubine of Eliphaz",
    ),
    (
        re.compile(r"\bAnd it was days of wheat harvest\b"),
        "And it was the days of wheat harvest",
    ),
    (
        re.compile(r"\bhe was chief of a band\b"),
        "he was the chief of a band",
    ),
    (
        re.compile(r"\bHe was ruler of the Reubenites\b"),
        "He was the ruler of the Reubenites",
    ),
    (
        re.compile(r"\bZechariah son of Meshelemiah was gatekeeper\b"),
        "Zechariah son of Meshelemiah was the gatekeeper",
    ),
    (
        re.compile(r"\bthis was number of mighty men of David\b"),
        "this was the number of mighty men of David",
    ),
    (
        re.compile(r"\bAsaph from the beginning was chief of the singers\b"),
        "Asaph from the beginning was the chief of the singers",
    ),
    (
        re.compile(r"\bthis was lawlessness of Sodom your sister\b"),
        "this was the lawlessness of Sodom your sister",
    ),
    (
        re.compile(r"\bThey became grass of field and green herb, grass of rooftops\b"),
        "They became grass of the field and green herb, grass of the rooftops",
    ),
    (
        re.compile(r"\bThis is beginning of the Lord's creation\b"),
        "This is the beginning of the Lord's creation",
    ),
    (
        re.compile(r"\bwhose king is son of nobles\b"),
        "whose king is a son of nobles",
    ),
    (
        re.compile(r"\bfor time and times and half a time is completion of release-hands\b"),
        "for time and times and half a time is the completion of release-hands",
    ),
    (
        re.compile(r"\bShe is beginning of sin to the daughter of Zion\b"),
        "She is the beginning of sin to the daughter of Zion",
    ),
    (
        re.compile(r"\bAnd Joseph was ruler of the land\b"),
        "And Joseph was the ruler of the land",
    ),
    (
        re.compile(r"\bWisdom built a house for and set seven pillars under it\b"),
        "Wisdom built a house for herself and set seven pillars under it",
    ),
    (
        re.compile(r"\bWisdom good with inheritance\b"),
        "Wisdom is good with inheritance",
    ),
    (
        re.compile(r"\bWisdom good above weapons of war\b"),
        "Wisdom is good above weapons of war",
    ),
    (
        re.compile(r"\bDeath and life in the hand of tongue\b"),
        "Death and life are in the hand of the tongue",
    ),
    (
        re.compile(r"\bFolly of man ruins his ways\b"),
        "The folly of a man ruins his ways",
    ),
    (
        re.compile(r"\bGlory to man to turn from insults\b"),
        "Glory to a man to turn from insults",
    ),
    (
        re.compile(r"\bFolly fastened to the heart of youth\b"),
        "Folly is fastened to the heart of youth",
    ),
    (
        re.compile(r"\bWisdom will help wise above ten rulers\b"),
        "Wisdom will help the wise above ten rulers",
    ),
    (
        re.compile(r"\bWisdom and good understanding at the gates of wise\b"),
        "Wisdom and good understanding are at the gates of the wise",
    ),
    (
        re.compile(r"\bLawless men set city on fire\b"),
        "Lawless men set a city on fire",
    ),
    (
        re.compile(r"\bFear and pit and snare upon you\b"),
        "Fear and pit and snare are upon you",
    ),
    (
        re.compile(r"\bGood ones will be inhabitants of the earth, and innocent ones remain in it, for straight ones will settle in the earth and holy ones remain in it\b"),
        "The good ones will inhabit the earth, and the innocent ones remain in it, for the straight ones will settle in the earth and the holy ones remain in it",
    ),
    (
        re.compile(r"\bFor Hebronites, Ioudias was chief of the Hebronites by their generations, by fathers\. In fortieth year of his reign they were sought out, and mighty man was found among them in Jaazer of Gilead\b"),
        "For the Hebronites, Ioudias was the chief of the Hebronites by their generations, by fathers. In the fortieth year of his reign they were sought out, and a mighty man was found among them in Jaazer of Gilead",
    ),
    (
        re.compile(r"\bGod will come from Teman, and Holy One from overshadowing wooded mountain\. Pause\. His excellence covered heavens, and earth was full of his praise\b"),
        "God will come from Teman, and the Holy One from overshadowing wooded mountain. Pause. His excellence covered the heavens, and the earth was full of his praise",
    ),
    (
        re.compile(r"\bwith lyre, Holy One of Israel\b"),
        "with lyre, O Holy One of Israel",
    ),
    (
        re.compile(r"\bYou abandoned Lord and provoked Holy One of Israel\b"),
        "You abandoned the Lord and provoked the Holy One of Israel",
    ),
    (
        re.compile(r"(?<!O )(?<!my )(?<!your )(?<![Tt]he )\bHoly One\b"),
        "the Holy One",
    ),
    (
        re.compile(r"\bThey became grass of the field and green herb, grass of the rooftops and trampling before standing grain\b"),
        "They became like grass of the field and green herb, like grass of the rooftops and trampling before standing grain",
    ),
    (
        re.compile(r"\bGlory to a man to turn from insults\b"),
        "It is glory for a man to turn from insults",
    ),
    (
        re.compile(r"\bFolly is fastened to the heart of youth, but rod and discipline far from him\b"),
        "Folly is fastened to the heart of youth, but the rod and discipline are far from him",
    ),
    (
        re.compile(r"\bWisdom is good with inheritance, and surplus to those seeing sun\b"),
        "Wisdom is good with inheritance, and surplus to those seeing the sun",
    ),
    (
        re.compile(r"\bRighteous are you, Lord, because I will speak in defense to you; yet I will speak judgments to you: Why does the (?:the )?way of ungodly prosper\? All dealing faithlessly in the acts of faithlessness flourished\b"),
        "You are righteous, Lord, because I will speak in defense to you; yet I will speak judgments to you: Why does the way of the ungodly prosper? All who deal faithlessly in the acts of faithlessness flourished",
    ),
    (
        re.compile(r"\bRighteous is the Lord, because I embittered his mouth\b"),
        "The Lord is righteous, because I embittered his mouth",
    ),
    (
        re.compile(r"\bLawless and sinners will be shattered together\b"),
        "The lawless and sinners will be shattered together",
    ),
    (
        re.compile(r"\bFear and pit and snare are upon you, dwellers on earth\b"),
        "Fear and pit and snare are upon you, dwellers on the earth",
    ),
    (
        re.compile(r"\bRighteousness guards innocent, but sin makes ungodly base\b"),
        "Righteousness guards the innocent, but sin makes the ungodly base",
    ),
    (
        re.compile(r"\bLight for the righteous always, but light of ungodly is quenched\. Deceitful souls wander in sins, but righteous show compassion and mercy\b"),
        "There is light for the righteous always, but the light of the ungodly is quenched. Deceitful souls wander in sins, but the righteous show compassion and mercy",
    ),
    (
        re.compile(r"\bRighteousness exalts nation, but sins diminish tribes\b"),
        "Righteousness exalts a nation, but sins diminish tribes",
    ),
    (
        re.compile(r"\bFear casts down sluggards\b"),
        "Fear casts down the sluggards",
    ),
    (
        re.compile(r"\bFear God, son, and the king, and do not disobey either of them\b"),
        "My son, fear God and the king, and do not disobey either of them",
    ),
    (
        re.compile(r"\ball kings of earth were seeking face of Solomon\b"),
        "all kings of the earth were seeking the face of Solomon",
    ),
    (
        re.compile(r"\bkings of earth\b"),
        "kings of the earth",
    ),
    (
        re.compile(r"\ball nations of earth\b"),
        "all nations of the earth",
    ),
    (
        re.compile(r"\bFor earth is given into the hands\b"),
        "For the earth is given into the hands",
    ),
    (
        re.compile(r"\bearth is house for every mortal\b"),
        "the earth is a house for every mortal",
    ),
    (
        re.compile(r"\bword of the Lord heavens were made firm\b"),
        "word of the Lord the heavens were made firm",
    ),
    (
        re.compile(r"\bfoundations? of earth\b"),
        lambda match: f"{match.group(0).split()[0]} of the earth",
    ),
    (
        re.compile(r"\bupon host of heaven and upon kings of the earth\b"),
        "upon the host of heaven and upon kings of the earth",
    ),
    (
        re.compile(r"\bif foundation of the earth\b"),
        "if the foundation of the earth",
    ),
    (
        re.compile(r"\bLord in his holy temple; Lord, his throne in heaven\b"),
        "The Lord is in his holy temple; the Lord's throne is in heaven",
    ),
    (
        re.compile(r"\bLord in his anger will trouble them\b"),
        "The Lord in his anger will trouble them",
    ),
    (
        re.compile(r"\bWorship Lord in his holy court\b"),
        "Worship the Lord in his holy court",
    ),
    (
        re.compile(r"\bFaithful Lord in his words and holy in all his works\b"),
        "Faithful is the Lord in his words and holy in all his works",
    ),
    (
        re.compile(r"\bearth shook, and heaven was shaken\b"),
        "the earth shook, and heaven was shaken",
    ),
    (
        re.compile(r"\bupon earth\?"),
        "upon the earth?",
    ),
    (
        re.compile(r"\bdust of earth\b"),
        "dust of the earth",
    ),
    (
        re.compile(r"\bbut earth he gave\b"),
        "but the earth he gave",
    ),
    (
        re.compile(r"\bcrushing of daughter of my kin\b"),
        "crushing of the daughter of my kin",
    ),
    (
        re.compile(r"\bfrom heads of father-houses\b"),
        "from the heads of father-houses",
    ),
    (
        re.compile(r"\bforecourt of gate of the house\b"),
        "forecourt of the gate of the house",
    ),
    (
        re.compile(r"\bporch of gate\b"),
        "porch of the gate",
    ),
    (
        re.compile(r"\bthrone of kingdom of the Lord\b"),
        "throne of the kingdom of the Lord",
    ),
    (
        re.compile(r"\bpattern which he had in his spirit of courts of the house\b"),
        "pattern which he had in his spirit of the courts of the house",
    ),
    (
        re.compile(r"\bmade house of holy of holies\b"),
        "made the house of the holy of holies",
    ),
    (
        re.compile(r"\bfor judgment of the Lord\b"),
        "for the judgment of the Lord",
    ),
    (
        re.compile(r"\bnot in tombs of kings\b"),
        "not in the tombs of kings",
    ),
    (
        re.compile(r"\baccording to covenant of the law of the Lord\b"),
        "according to the covenant of the law of the Lord",
    ),
    (
        re.compile(r"\baccording to abominations of nations\b"),
        "according to the abominations of nations",
    ),
    (
        re.compile(r"\bgods of nations of earth\b"),
        "gods of the nations of the earth",
    ),
    (
        re.compile(r"\bcommanders of force of the king\b"),
        "commanders of the force of the king",
    ),
    (
        re.compile(r"\brulers of earth\b"),
        "rulers of the earth",
    ),
    (
        re.compile(r"\bunder sun\b"),
        "under the sun",
    ),
    (
        re.compile(r"(?<![Tt]he )\bdaughter of my people\b"),
        "the daughter of my people",
    ),
    (
        re.compile(r"(?<![Tt]he )\bheads of father-houses\b"),
        "the heads of father-houses",
    ),
    (
        re.compile(r"\bchiefs of houses of fathers\b"),
        "chiefs of the houses of fathers",
    ),
    (
        re.compile(r"\bchiefs of father-houses of priests\b"),
        "chiefs of the father-houses of priests",
    ),
    (
        re.compile(r"\bhouse of tombs of my fathers\b"),
        "house of the tombs of my fathers",
    ),
    (
        re.compile(r"\bcity of tombs of my fathers\b"),
        "city of the tombs of my fathers",
    ),
    (
        re.compile(r"\bof words of the king\b"),
        "of the words of the king",
    ),
    (
        re.compile(r"(?<![Tt]he )\bpeoples of the land\b"),
        "the peoples of the land",
    ),
    (
        re.compile(r"\bjudgments of your righteousness\b"),
        "the judgments of your righteousness",
    ),
    (
        re.compile(r"\bfrom day of your fall\b"),
        "from the day of your fall",
    ),
    (
        re.compile(r"\bLords anger\b"),
        "Lord's anger",
    ),
    (
        re.compile(r"\bfrom strength of your hand\b"),
        "from the strength of your hand",
    ),
    (
        re.compile(r"\bby multitude of his strength\b"),
        "by the multitude of his strength",
    ),
    (
        re.compile(r"\ball multitude of his strength\b"),
        "all the multitude of his strength",
    ),
    (
        re.compile(r"\bbreath of spirit of your wrath\b"),
        "breath of the spirit of your wrath",
    ),
    (
        re.compile(r"\bunder the sun, number of days\b"),
        "under the sun, the number of days",
    ),
    (
        re.compile(r"\bin life, number of days\b"),
        "in life, the number of days",
    ),
    (
        re.compile(r"\bfor number of days\b"),
        "for the number of days",
    ),
    (
        re.compile(r"\bwith sun and before moon\b"),
        "with the sun and before the moon",
    ),
    (
        re.compile(r"\bSeven times in day\b"),
        "Seven times a day",
    ),
    (
        re.compile(r"\bin day when\b"),
        "on the day when",
    ),
    (
        re.compile(r"\bin day I\b"),
        "on the day I",
    ),
    (
        re.compile(r"\bin day that\b"),
        "on the day that",
    ),
    (
        re.compile(r"\bin day he gives lot\b"),
        "on the day he gives lot",
    ),
    (
        re.compile(r"\bin day and in night\b"),
        "by day and by night",
    ),
    (
        re.compile(r"\bas in day on Midian\b"),
        "as on the day of Midian",
    ),
    (
        re.compile(
            r"\brace not to swift, nor war to strong, and indeed not bread to wise, and indeed not wealth to understanding\b"
        ),
        "the race is not to the swift, nor war to the strong, and indeed not bread to the wise, and indeed not wealth to those with understanding",
    ),
    (
        re.compile(r"\bStrength of lion, voice of lioness\b"),
        "The strength of a lion, the voice of a lioness",
    ),
    (
        re.compile(r"\bGod went up in shout, Lord in voice of a trumpet\b"),
        "God went up with a shout, the Lord with the voice of a trumpet",
    ),
    (
        re.compile(r"\bvoice of turtledove was heard\b"),
        "the voice of a turtledove was heard",
    ),
    (
        re.compile(r"\bThe voice of cry from the city, voice from the temple, voice of the Lord\b"),
        "The voice of a cry from the city, a voice from the temple, the voice of the Lord",
    ),
    (
        re.compile(r"\bBehold, voice of cry of daughter of my people\b"),
        "Behold, the voice of the cry of the daughter of my people",
    ),
    (
        re.compile(r"\b(?:hear|heard|hears|hearing) voice of\b"),
        lambda match: f"{match.group(0).rsplit(' ', 2)[0]} the voice of",
    ),
    (
        re.compile(r"\bobey voice of\b"),
        "obey the voice of",
    ),
    (
        re.compile(r"\bby voice of\b"),
        "by the voice of",
    ),
    (
        re.compile(r"\bWhether good or evil, voice of the Lord\b"),
        "Whether good or evil, the voice of the Lord",
    ),
    (
        re.compile(r"\bThis one is father of the Moabites\b"),
        "This one is the father of the Moabites",
    ),
    (
        re.compile(r"\bThis one is father of the Ammonites\b"),
        "This one is the father of the Ammonites",
    ),
    (
        re.compile(r"\bhe is father of Jesse, father of David\b"),
        "he is the father of Jesse, the father of David",
    ),
    (
        re.compile(r"\bhe is king of glory\b"),
        "he is the king of glory",
    ),
    (
        re.compile(r"\bhe is the King of Glory\b"),
        "he is the king of glory",
    ),
    (
        re.compile(r"\bHe was father of those dwelling in tents\b"),
        "He was the father of those dwelling in tents",
    ),
    (
        re.compile(r"\bHam was father of Canaan\b"),
        "Ham was the father of Canaan",
    ),
    (
        re.compile(r"\bthen I was servant of your father and now again and now I am your servant\b"),
        "then I was your father's servant, and now again I am your servant",
    ),
    (
        re.compile(r"\bAnd there became sons of Belah\b"),
        "And the sons of Belah were",
    ),
    (
        re.compile(r"\ball Edomites became servants of David\b"),
        "all Edomites became David's servants",
    ),
    (
        re.compile(r"\bthey will be portions of foxes\b"),
        "they will be portions for foxes",
    ),
    (
        re.compile(r"\bthere will be folds of flocks and valley of Achor for the rest of herds\b"),
        "there will be folds for flocks and the valley of Achor for the rest of herds",
    ),
    (
        re.compile(r"\bhouse of Israel was ashamed of Bethel\b"),
        "the house of Israel was ashamed of Bethel",
    ),
    (
        re.compile(r"\buntil time of completion of war\b"),
        "until the time of the completion of war",
    ),
    (
        re.compile(r"\buntil time of completion it will be warred by war\b"),
        "until the time of completion it will be warred by war",
    ),
    (
        re.compile(r"\buntil time of completion\b"),
        "until the time of completion",
    ),
    (
        re.compile(r"\bLight turned to darkness for you\b"),
        "The light turned to darkness for you",
    ),
    (
        re.compile(r"\bRighteous men seeing laughed\b"),
        "Righteous men saw and laughed",
    ),
    (
        re.compile(r"\bWisdom hymns in exits\b"),
        "Wisdom is hymned in exits",
    ),
    (
        re.compile(r"\bRighteous escapes from trap\b"),
        "A righteous one escapes from a trap",
    ),
    (
        re.compile(r"\bJoy lingers for righteous\b"),
        "Joy lingers for the righteous",
    ),
    (
        re.compile(r"\bRighteous forever will not give way\b"),
        "The righteous forever will not give way",
    ),
    (
        re.compile(r"\bRighteous pities souls of his cattle\b"),
        "A righteous one pities the souls of his cattle",
    ),
    (
        re.compile(r"\bRighteous openly displays faith\b"),
        "A righteous one openly displays faith",
    ),
    (
        re.compile(r"\bRighteous hates unjust word\b"),
        "A righteous one hates an unjust word",
    ),
    (
        re.compile(r"\bLight for righteous always\b"),
        "Light for the righteous always",
    ),
    (
        re.compile(r"\bRighteous son is born for life\b"),
        "A righteous son is born for life",
    ),
    (
        re.compile(r"\bUngodly is carried about in destruction\b"),
        "An ungodly one is carried about in destruction",
    ),
    (
        re.compile(r"\bbut ungodly will not inhabit earth\b"),
        "but the ungodly will not inhabit the earth",
    ),
    (
        re.compile(r"\bUngodly all day desires evil desires\b"),
        "An ungodly one all day desires evil desires",
    ),
    (
        re.compile(r"\bUngodly flees with none pursuing\b"),
        "An ungodly one flees with none pursuing",
    ),
    (
        re.compile(r"\bDeath swallowed after growing strong\b"),
        "Death was swallowed after growing strong",
    ),
    (
        re.compile(r"\bLawless one failed and proud one perished\b"),
        "The lawless one failed and the proud one perished",
    ),
    (
        re.compile(r"\bLawless in Zion departed\b"),
        "The lawless in Zion departed",
    ),
    (
        re.compile(r"\bThere will be joy of birds\b"),
        "There will be the joy of birds",
    ),
    (
        re.compile(r"\bwhere was hope of help for him\b"),
        "where there was hope of help for him",
    ),
    (
        re.compile(r"\bI was father of weak men\b"),
        "I was a father to weak men",
    ),
    (
        re.compile(r"\bThis one was father of Ziph\b"),
        "This one was the father of Ziph",
    ),
    (
        re.compile(r"\bMaon was father of Bethzur\b"),
        "Maon was the father of Bethzur",
    ),
    (
        re.compile(r"\bThis one was father of Eshton\b"),
        "This one was the father of Eshton",
    ),
    (
        re.compile(r"\bDeath is rest to a man\b"),
        "Death is rest for a man",
    ),
    (
        re.compile(r"\buntil moon is removed\b"),
        "until the moon is removed",
    ),
    (
        re.compile(r"\bset his footsteps in way\b"),
        "set his footsteps in the way",
    ),
    (
        re.compile(r"\bLight arose for righteous one, and for straight in heart gladness\b"),
        "Light arose for a righteous one, and gladness for the straight in heart",
    ),
    (
        re.compile(r"\bGlory and wealth in his house\b"),
        "Glory and wealth are in his house",
    ),
    (
        re.compile(r"\bRighteous ones cried out\b"),
        "The righteous cried out",
    ),
    (
        re.compile(r"\bRighteous will instruct me\b"),
        "A righteous one will instruct me",
    ),
    (
        re.compile(r"\boil of sinner may it not fatten\b"),
        "oil of a sinner may it not fatten",
    ),
    (
        re.compile(r"\bRighteous lips acceptable to the king\b"),
        "Righteous lips are acceptable to the king",
    ),
    (
        re.compile(r"\bRighteous will make many years in wealth\b"),
        "A righteous one will make many years in wealth",
    ),
    (
        re.compile(r"\bRighteous eating fills his soul\b"),
        "A righteous one eats and fills his soul",
    ),
    (
        re.compile(r"\bRighteous understands hearts of ungodly\b"),
        "A righteous one understands hearts of ungodly",
    ),
    (
        re.compile(r"\bRighteous father rears well\b"),
        "A righteous father rears well",
    ),
    (
        re.compile(r"\bRighteous king raises up land\b"),
        "A righteous king raises up a land",
    ),
    (
        re.compile(r"\bRighteous knows how to judge poor men\b"),
        "A righteous one knows how to judge poor men",
    ),
    (
        re.compile(r"\bsinner one will destroy much good\b"),
        "one sinner will destroy much good",
    ),
    (
        re.compile(r"\bFear and anger became to us\b"),
        "Fear and anger came upon us",
    ),
    (
        re.compile(r"\bEphraim surrounded me with lie and house of Israel with impieties, and now Judah knew them before God, and holy people will be called of God\b"),
        "Ephraim surrounded me with falsehood, and the house of Israel and Judah with impieties; but now God knows them, and they will be called God's holy people",
    ),
    (
        re.compile(r"\btrusting on them\b"),
        "trusting in them",
    ),
    (
        re.compile(r"\bhe was brother to her father and that he was son of Rebekah\b"),
        "he was a relative of her father and that he was son of Rebekah",
    ),
    (
        re.compile(r"\bso was standing of brightness around\b"),
        "so was the appearance of brightness around",
    ),
    (
        re.compile(r"\bUngodly is one saying to the king, You act lawlessly, and Most Ungodly One to rulers\b"),
        "He is ungodly who says to the king, You act lawlessly, and Most Ungodly One to rulers",
    ),
    (
        re.compile(r"\bWise and understanding men they call evil, but sweet in speech will hear more\b"),
        "Men call the wise and understanding evil, but those sweet in speech will hear more",
    ),
    (
        re.compile(r"\bJoy and gladness were consumed from Moab, and wine was upon your vats\. Morning they did not tread, nor evening\. They did not make shouting\b"),
        "Joy and gladness were utterly swept from the land of Moab, and though wine was in your presses, in the morning they did not tread it, nor in the evening did they raise the cry of joy",
    ),
    (
        re.compile(r"\bhe was son of Rebekah\b"),
        "he was the son of Rebekah",
    ),
    (
        re.compile(r"\bAmasa was son of a man\b"),
        "Amasa was the son of a man",
    ),
    (
        re.compile(r"\bthis one was son of Isabia\b"),
        "this one was the son of Isabia",
    ),
    (
        re.compile(r"\bAnd overseer of the Levites was son of Bani\b"),
        "And the overseer of the Levites was the son of Bani",
    ),
    (
        re.compile(r"\bhe himself was son of Zerah\b"),
        "he himself was the son of Zerah",
    ),
    (
        re.compile(r"\bhe was chief of three\b"),
        "he was chief of the three",
    ),
    (
        re.compile(r"\bIoudias was chief of Hebronites\b"),
        "Ioudias was chief of the Hebronites",
    ),
    (
        re.compile(r"\bAhithophel was counselor of the king\b"),
        "Ahithophel was counselor to the king",
    ),
    (
        re.compile(r"\bCushi was first friend of the king\b"),
        "Cushi was the first friend of the king",
    ),
    (
        re.compile(r"\bwho was overseer of men of war\b"),
        "who was overseer over the men of war",
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
        re.compile(r"\b([Ii]n) (seventh|ninth|thirty-ninth) year of\b"),
        r"\1 the \2 year of",
    ),
    (
        re.compile(r"\b([Oo]n|[Uu]ntil) (eighth|sixteenth|last|twenty-fourth) day\b"),
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
    (re.compile(r"\b(upon|on|at|toward|before|from|to|with|through|against|in) Lord\b"), r"\1 the Lord"),
    (re.compile(r"\bthe(?: [Tt]he)+\b"), "the"),
    (re.compile(r"\bThe(?: [Tt]he)+\b"), "The"),
    (re.compile(r"\ba(?: a)+\b"), "a"),
    (re.compile(r"\bA(?: a)+\b"), "A"),
)
DEDUPED_LORD_ARTICLE_RE = re.compile(r"\b([Tt])he [Tt]he Lord\b")
COPULA_EXACT_REPLACEMENTS = (
    ("And this to you = sign:", "And this is a sign to you:"),
    ("And this to you = sign from", "And this is a sign to you from"),
    ("This = sign that", "This is a sign that"),
    ("because this = whole man", "because this is the whole man"),
    ("I = flower of field, lily of valleys", "I am a flower of the field, a lily of the valleys"),
    ("and he whole = desire", "and he is wholly desirable"),
    ("This my beloved", "This is my beloved"),
    ("This my dear one", "this is my dear one"),
    ("I = God", "I am God"),
    ("You = my witnesses", "You are my witnesses"),
    ("I = witness", "I am a witness"),
    ("All flesh = grass", "All flesh is grass"),
    ("Holy = God dwelling in heights", "The Holy One is God dwelling in heights"),
    ("Day of affliction and reproach and rebuke and anger = today", "Today is a day of affliction and reproach and rebuke and anger"),
    ("in horses = very great multitude", "in horses, a very great multitude"),
)
COPULA_PLURAL_LEFTS = (
    "children's children",
    "egyptians",
    "honeycombs",
    "its wings",
    "the words",
    "their works",
    "treasures",
    "your shoots",
)
COPULA_MARKER_RE = re.compile(r" = ")


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

    for source, replacement in COPULA_EXACT_REPLACEMENTS:
        updated, count = updated.replace(source, replacement), updated.count(source)
        changes += count

    while " = " in updated:
        index = updated.index(" = ")
        prefix = updated[:index].rstrip()
        left_segment = re.split(r"[.;:?!]", prefix)[-1].strip().lower()
        copula = "are" if left_segment.startswith(COPULA_PLURAL_LEFTS) else "is"
        updated = f"{updated[:index]} {copula} {updated[index + 3:]}"
        changes += 1

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
