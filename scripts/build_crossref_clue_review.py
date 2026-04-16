#!/usr/bin/env python3
import csv
import json
import re
import xml.etree.ElementTree as ET
import zipfile
from collections import defaultdict
from pathlib import Path

from build_idiom_consistency_review import FAMILIES


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
RAW = DATA / "raw"
OUTPUT = ROOT / "output"

PRIORITY_CSV = OUTPUT / "fresh_vs_brenton_ot_priority_review.csv"
OT_SOURCE = RAW / "lxx_greek" / "ot_full.csv"
OPENBIBLE_ZIP = RAW / "cross-references.zip"
UKJV_ZIP = RAW / "SF_2009-01-20_ENG_UKJV_(UPDATED KING JAMES VERSION).zip"

REVIEW_MD = OUTPUT / "fresh_ot_crossref_clues.md"
REVIEW_CSV = OUTPUT / "fresh_ot_crossref_clues.csv"
WATCH_MD = OUTPUT / "fresh_ot_crossref_watch.md"
WATCH_CSV = OUTPUT / "fresh_ot_crossref_watch.csv"
DIAGNOSTICS = OUTPUT / "fresh_ot_crossref_clues_diagnostics.json"


OPENBIBLE_BOOK_MAP = {
    "Gen": "GEN", "Exod": "EXO", "Lev": "LEV", "Num": "NUM", "Deut": "DEU",
    "Josh": "JOS", "Judg": "JDG", "Ruth": "RUT", "1Sam": "1SA", "2Sam": "2SA",
    "1Kgs": "1KI", "2Kgs": "2KI", "1Chr": "1CH", "2Chr": "2CH", "Ezra": "EZR",
    "Neh": "NEH", "Esth": "EST", "Job": "JOB", "Ps": "PSA", "Prov": "PRO",
    "Eccl": "ECC", "Song": "SNG", "Isa": "ISA", "Jer": "JER", "Lam": "LAM",
    "Ezek": "EZK", "Dan": "DAN", "Hos": "HOS", "Joel": "JOL", "Amos": "AMO",
    "Obad": "OBA", "Jonah": "JON", "Mic": "MIC", "Nah": "NAM", "Hab": "HAB",
    "Zeph": "ZEP", "Hag": "HAG", "Zech": "ZEC", "Mal": "MAL", "Matt": "MAT",
    "Mark": "MRK", "Luke": "LUK", "John": "JHN", "Acts": "ACT", "Rom": "ROM",
    "1Cor": "1CO", "2Cor": "2CO", "Gal": "GAL", "Eph": "EPH", "Phil": "PHP",
    "Col": "COL", "1Thess": "1TH", "2Thess": "2TH", "1Tim": "1TI", "2Tim": "2TI",
    "Titus": "TIT", "Phlm": "PHM", "Heb": "HEB", "Jas": "JAS", "1Pet": "1PE",
    "2Pet": "2PE", "1John": "1JN", "2John": "2JN", "3John": "3JN", "Jude": "JUD",
    "Rev": "REV",
}

STANDARD_BOOK_NAMES = {
    "GEN": "Genesis", "EXO": "Exodus", "LEV": "Leviticus", "NUM": "Numbers", "DEU": "Deuteronomy",
    "JOS": "Joshua", "JDG": "Judges", "RUT": "Ruth", "1SA": "1 Samuel", "2SA": "2 Samuel",
    "1KI": "1 Kings", "2KI": "2 Kings", "1CH": "1 Chronicles", "2CH": "2 Chronicles", "EZR": "Ezra",
    "NEH": "Nehemiah", "EST": "Esther", "JOB": "Job", "PSA": "Psalms", "PRO": "Proverbs",
    "ECC": "Ecclesiastes", "SNG": "Song of Solomon", "ISA": "Isaiah", "JER": "Jeremiah",
    "LAM": "Lamentations", "EZK": "Ezekiel", "DAN": "Daniel", "HOS": "Hosea", "JOL": "Joel",
    "AMO": "Amos", "OBA": "Obadiah", "JON": "Jonah", "MIC": "Micah", "NAM": "Nahum",
    "HAB": "Habakkuk", "ZEP": "Zephaniah", "HAG": "Haggai", "ZEC": "Zechariah", "MAL": "Malachi",
    "MAT": "Matthew", "MRK": "Mark", "LUK": "Luke", "JHN": "John", "ACT": "Acts", "ROM": "Romans",
    "1CO": "1 Corinthians", "2CO": "2 Corinthians", "GAL": "Galatians", "EPH": "Ephesians",
    "PHP": "Philippians", "COL": "Colossians", "1TH": "1 Thessalonians", "2TH": "2 Thessalonians",
    "1TI": "1 Timothy", "2TI": "2 Timothy", "TIT": "Titus", "PHM": "Philemon", "HEB": "Hebrews",
    "JAS": "James", "1PE": "1 Peter", "2PE": "2 Peter", "1JN": "1 John", "2JN": "2 John",
    "3JN": "3 John", "JUD": "Jude", "REV": "Revelation",
}

UKJV_BOOK_MAP = {
    1: "Genesis", 2: "Exodus", 3: "Leviticus", 4: "Numbers", 5: "Deuteronomy", 6: "Joshua",
    7: "Judges", 8: "Ruth", 9: "1 Samuel", 10: "2 Samuel", 11: "1 Kings", 12: "2 Kings",
    13: "1 Chronicles", 14: "2 Chronicles", 15: "Ezra", 16: "Nehemiah", 17: "Esther",
    18: "Job", 19: "Psalms", 20: "Proverbs", 21: "Ecclesiastes", 22: "Song of Solomon",
    23: "Isaiah", 24: "Jeremiah", 25: "Lamentations", 26: "Ezekiel", 27: "Daniel",
    28: "Hosea", 29: "Joel", 30: "Amos", 31: "Obadiah", 32: "Jonah", 33: "Micah",
    34: "Nahum", 35: "Habakkuk", 36: "Zephaniah", 37: "Haggai", 38: "Zechariah",
    39: "Malachi", 40: "Matthew", 41: "Mark", 42: "Luke", 43: "John", 44: "Acts",
    45: "Romans", 46: "1 Corinthians", 47: "2 Corinthians", 48: "Galatians", 49: "Ephesians",
    50: "Philippians", 51: "Colossians", 52: "1 Thessalonians", 53: "2 Thessalonians",
    54: "1 Timothy", 55: "2 Timothy", 56: "Titus", 57: "Philemon", 58: "Hebrews",
    59: "James", 60: "1 Peter", 61: "2 Peter", 62: "1 John", 63: "2 John",
    64: "3 John", 65: "Jude", 66: "Revelation",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["ref"])
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_openbible_ref(raw_ref: str) -> tuple[str, int, int, str] | None:
    raw_ref = raw_ref.strip()
    if "-" in raw_ref:
        raw_ref = raw_ref.split("-", 1)[0]
    match = re.match(r"([1-3]?[A-Za-z]+)\.(\d+)\.(\d+)$", raw_ref)
    if not match:
        return None
    abbr, chapter, verse = match.groups()
    code = OPENBIBLE_BOOK_MAP.get(abbr)
    if not code:
        return None
    return code, int(chapter), int(verse), raw_ref


def load_openbible_crossrefs(limit_per_verse: int = 8, min_votes: int = 1) -> dict[str, list[dict[str, str]]]:
    refs: dict[str, list[tuple[int, str]]] = defaultdict(list)
    with zipfile.ZipFile(OPENBIBLE_ZIP) as zf:
        lines = zf.read("cross_references.txt").decode("utf-8", "replace").splitlines()
    for line in lines[1:]:
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        src, dst, votes_raw = parts
        parsed_src = parse_openbible_ref(src)
        if not parsed_src:
            continue
        try:
            votes = int(votes_raw)
        except ValueError:
            continue
        if votes < min_votes:
            continue
        src_ref = f"{STANDARD_BOOK_NAMES[parsed_src[0]]} {parsed_src[1]}:{parsed_src[2]}"
        refs[src_ref].append((votes, dst))
    cooked: dict[str, list[dict[str, str]]] = {}
    for ref, values in refs.items():
        ranked = sorted(values, key=lambda item: (-item[0], item[1]))[:limit_per_verse]
        cooked[ref] = [{"target_raw": target, "votes": str(votes)} for votes, target in ranked]
    return cooked


def build_ot_maps() -> tuple[dict[str, dict[str, str]], dict[str, set[str]]]:
    by_ref: dict[str, dict[str, str]] = {}
    families_by_ref: dict[str, set[str]] = {}
    for row in load_csv(OT_SOURCE):
        ref = row["ref"]
        by_ref[ref] = row
        greek = row.get("greek_text", "") or ""
        families_by_ref[ref] = {family["name"] for family in FAMILIES if family["match"](greek)}
    return by_ref, families_by_ref


def load_ukjv_map(needed_refs: set[str]) -> dict[str, str]:
    if not needed_refs:
        return {}
    result: dict[str, str] = {}
    with zipfile.ZipFile(UKJV_ZIP) as zf:
        xml_name = zf.namelist()[0]
        root = ET.fromstring(zf.read(xml_name))
    needed_by_book: dict[str, set[tuple[int, int]]] = defaultdict(set)
    for ref in needed_refs:
        book, cv = ref.rsplit(" ", 1)
        chapter, verse = cv.split(":")
        needed_by_book[book].add((int(chapter), int(verse)))
    for book in root.findall("BIBLEBOOK"):
        bnumber = int(book.attrib["bnumber"])
        book_name = UKJV_BOOK_MAP.get(bnumber)
        if book_name not in needed_by_book:
            continue
        wanted = needed_by_book[book_name]
        for chapter in book.findall("CHAPTER"):
            cnum = int(chapter.attrib["cnumber"])
            for verse in chapter.findall("VERS"):
                vnum = int(verse.attrib["vnumber"])
                if (cnum, vnum) not in wanted:
                    continue
                result[f"{book_name} {cnum}:{vnum}"] = normalize_space("".join(verse.itertext()))
    return result


def build_rows() -> tuple[list[dict[str, str]], list[dict[str, str]], dict[str, object]]:
    priority_rows = load_csv(PRIORITY_CSV)
    ot_by_ref, families_by_ref = build_ot_maps()
    crossrefs_by_ref = load_openbible_crossrefs()

    needed_nt_refs: set[str] = set()
    pending_targets: dict[str, list[dict[str, str]]] = defaultdict(list)

    for row in priority_rows:
        for target in crossrefs_by_ref.get(row["ref"], []):
            parsed = parse_openbible_ref(target["target_raw"])
            if not parsed:
                continue
            book_name = STANDARD_BOOK_NAMES[parsed[0]]
            target_ref = f"{book_name} {parsed[1]}:{parsed[2]}"
            enriched = dict(target)
            enriched["target_ref"] = target_ref
            enriched["target_book"] = book_name
            enriched["target_code"] = parsed[0]
            pending_targets[row["ref"]].append(enriched)
            if parsed[0] not in ot_by_ref and target_ref not in ot_by_ref:
                needed_nt_refs.add(target_ref)
            elif parsed[0].startswith(("MAT","MRK","LUK","JHN","ACT","ROM","1CO","2CO","GAL","EPH","PHP","COL","1TH","2TH","1TI","2TI","TIT","PHM","HEB","JAS","1PE","2PE","1JN","2JN","3JN","JUD","REV")):
                needed_nt_refs.add(target_ref)

    nt_map = load_ukjv_map(needed_nt_refs)

    review_rows: list[dict[str, str]] = []
    watch_rows: list[dict[str, str]] = []
    for row in priority_rows:
        ref = row["ref"]
        targets = pending_targets.get(ref, [])
        if not targets:
            continue
        source_families = families_by_ref.get(ref, set())
        ot_items: list[str] = []
        nt_items: list[str] = []
        shared_family_hits = 0
        top_vote = 0
        for target in targets:
            votes = int(target["votes"])
            top_vote = max(top_vote, votes)
            target_ref = target["target_ref"]
            target_book = target["target_book"]
            if target_ref in ot_by_ref:
                target_row = ot_by_ref[target_ref]
                target_text = target_row.get("draft_translation", "") or ""
                shared = sorted(source_families & families_by_ref.get(target_ref, set()))
                if shared:
                    shared_family_hits += 1
                shared_label = f" | shared-family={','.join(shared)}" if shared else ""
                ot_items.append(f"{target['target_raw']} ({votes}) -> {target_text}{shared_label}")
            elif target_ref in nt_map:
                nt_items.append(f"{target['target_raw']} ({votes}) -> {nt_map[target_ref]}")
        if not ot_items and not nt_items:
            continue
        review_row = {
            "ref": ref,
            "priority_score": row["priority_score"],
            "importance": row["importance"],
            "crossref_top_vote": str(top_vote),
            "crossref_ot_count": str(len(ot_items)),
            "crossref_nt_count": str(len(nt_items)),
            "crossref_shared_family_hits": str(shared_family_hits),
            "ot_crossrefs": " || ".join(ot_items[:4]),
            "nt_crossrefs": " || ".join(nt_items[:3]),
            "fresh_translation": row["fresh_translation"],
        }
        review_rows.append(review_row)
        if top_vote >= 20 or nt_items or shared_family_hits:
            watch_rows.append(review_row)

    review_rows.sort(key=lambda row: (-int(row["priority_score"]), row["ref"]))
    watch_rows.sort(key=lambda row: (-int(row["priority_score"]), -int(row["crossref_top_vote"]), row["ref"]))
    diagnostics = {
        "priority_rows": len(priority_rows),
        "rows_with_crossrefs": len(review_rows),
        "watch_rows": len(watch_rows),
    }
    return review_rows, watch_rows, diagnostics


def build_markdown(title: str, rows: list[dict[str, str]]) -> str:
    lines = [f"# {title}", "", f"Rows: {len(rows)}", ""]
    for row in rows:
        lines.extend(
            [
                f"## {row['ref']}",
                f"- score: {row['priority_score']}",
                f"- top vote: {row['crossref_top_vote']}",
                f"- OT crossrefs: {row['crossref_ot_count']}",
                f"- NT crossrefs: {row['crossref_nt_count']}",
                f"- shared-family hits: {row['crossref_shared_family_hits']}",
                f"- fresh: {row['fresh_translation']}",
            ]
        )
        if row["ot_crossrefs"]:
            lines.append(f"- OT clues: {row['ot_crossrefs']}")
        if row["nt_crossrefs"]:
            lines.append(f"- NT clues: {row['nt_crossrefs']}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    review_rows, watch_rows, diagnostics = build_rows()
    write_csv(REVIEW_CSV, review_rows)
    write_csv(WATCH_CSV, watch_rows)
    REVIEW_MD.write_text(build_markdown("Fresh OT Cross-Reference Clues", review_rows), encoding="utf-8")
    WATCH_MD.write_text(build_markdown("Fresh OT Cross-Reference Watch", watch_rows), encoding="utf-8")
    diagnostics.update(
        {
            "review_markdown": str(REVIEW_MD),
            "review_csv": str(REVIEW_CSV),
            "watch_markdown": str(WATCH_MD),
            "watch_csv": str(WATCH_CSV),
        }
    )
    DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2))


if __name__ == "__main__":
    main()
