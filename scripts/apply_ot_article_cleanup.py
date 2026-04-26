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
        re.compile(r"\bfor pasture of camels\b"),
        "for a pasture for camels",
    ),
    (
        re.compile(r"\bfor pasture of sheep\b"),
        "for a pasture for sheep",
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
    (re.compile(r"\b(upon|toward|before|from|to|with|through|against|in) Lord\b"), r"\1 the Lord"),
    (re.compile(r"\bthe(?: the)+\b"), "the"),
    (re.compile(r"\bThe(?: the)+\b"), "The"),
    (re.compile(r"\ba(?: a)+\b"), "a"),
    (re.compile(r"\bA(?: a)+\b"), "A"),
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
