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
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OT_SOURCE = DATA / "raw" / "lxx_greek" / "ot_full.csv"
PROPER_NAMES = DATA / "proper_names.csv"
NAMES_OF_GOD = DATA / "names_of_god.csv"
OUT_NOTES = DATA / "proper_name_transliteration_notes.csv"
OUT_COVERAGE_CSV = ROOT / "output" / "fresh_proper_name_note_coverage.csv"
OUT_COVERAGE_MD = ROOT / "output" / "fresh_proper_name_note_coverage.md"
OUT_DIAGNOSTICS = ROOT / "output" / "fresh_proper_name_note_coverage_diagnostics.json"

TOKEN_RE = re.compile(r"\b[A-ZĀĒĪŌŪ][A-Za-zĀĒĪŌŪāēīōū'-]+\b")

NAME_KINDS = {"Man", "Woman", "SupernaturalBeing", "PeopleGroup"}
PLACE_KINDS = {"City", "OtherPlace", "NaturalPlace", "ManMadePlace"}

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
}

MANUAL_PEOPLE_GROUP_FORMS = {
    "Levite",
    "Levites",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def normalize_token(token: str) -> str:
    if token.endswith("'s"):
        return token[:-2]
    return token


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
    for source_name, path in (("ot", OT_SOURCE),):
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
                entry = tokens.setdefault(
                    token,
                    {
                        "occurrences": 0,
                        "first_reference": ref,
                        "source": source_name,
                        "first_order": order,
                        "sample_refs": [],
                    },
                )
                entry["occurrences"] = int(entry["occurrences"]) + 1
                samples = entry["sample_refs"]
                if isinstance(samples, list) and ref not in samples and len(samples) < 8:
                    samples.append(ref)
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
    if token in MANUAL_TRANSLITERATED_FORMS:
        return "transliterated_form", "manual_high_frequency_lxx_form"
    primary = primary_kinds.get(token, set())
    any_match = any_kinds.get(token, set())
    primary_name = primary & NAME_KINDS
    primary_place = primary & PLACE_KINDS
    any_name = any_match & NAME_KINDS
    any_place = any_match & PLACE_KINDS
    if primary_place and not primary_name:
        return None, "place_primary_atlas_link"
    if primary_name:
        return note_kind_for_entity(primary_name), "logos_primary_entity"
    if any_name and not any_place:
        return note_kind_for_entity(any_name), "logos_alias_entity"
    if any(ch in token for ch in "ĀĒĪŌŪāēīōū"):
        return "transliterated_form", "macronized_source_form"
    return None, "not_classified"


def footnote_for(kind: str, reason: str) -> str:
    if kind == "person":
        return "Source text carries this as a personal name; retained as a proper noun rather than translated as ordinary vocabulary."
    if kind == "people_group":
        return "Ethnic or group proper noun; retained as a people-name rather than translated as ordinary vocabulary."
    if kind == "supernatural_being":
        return "Source text carries this as a divine or supernatural name/title; retained as a proper noun."
    if reason == "manual_high_frequency_lxx_form":
        return "High-frequency LXX-style proper noun form; retained here pending a context-by-context normalization decision."
    return "Transliterated source-form proper noun; retained here because a single conventional English equivalent is not yet assigned in this context."


def main() -> None:
    existing_labels = existing_note_labels()
    primary_kinds, any_kinds, logos_db = load_logos_entity_kinds()
    tokens, source_counts = gather_tokens()

    note_rows: list[dict[str, str]] = []
    coverage_rows: list[dict[str, str]] = []
    counts = Counter()

    for token, data in sorted(tokens.items(), key=lambda item: (int(item[1]["first_order"]), item[0])):
        if token in STOPWORDS or token in existing_labels:
            counts["skipped_existing_or_stopword"] += 1
            continue
        kind, reason = classify_token(token, primary_kinds=primary_kinds, any_kinds=any_kinds)
        if not kind:
            counts[f"skipped_{reason}"] += 1
            continue
        row = {
            "name": token,
            "kind": kind,
            "first_reference": str(data["first_reference"]),
            "source": str(data["source"]),
            "footnote": footnote_for(kind, reason),
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
        "- place names stay out of this supplemental file so Logos atlas/place links still work",
        "- this file covers remaining people names, people-group names, supernatural names, and LXX-style transliterated forms",
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
        "note_rows": len(note_rows),
        "source_counts": source_counts,
        "counts": dict(counts),
        "top_rows": top_rows[:20],
    }
    OUT_DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2))


if __name__ == "__main__":
    main()
