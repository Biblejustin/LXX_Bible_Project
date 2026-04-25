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
