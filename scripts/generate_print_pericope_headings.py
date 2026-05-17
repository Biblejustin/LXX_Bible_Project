#!/usr/bin/env python3
"""Generate print pericope headings from public-domain BSB section locations.

The source locations come from Berean Standard Bible USFM section headings.
Heading wording is reworded from public-domain BSB headings, with this
project's draft verse text used for chapter fallback headings.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import zipfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BSB_USFM = ROOT / "data" / "raw" / "engbsb_usfm.zip"
DEFAULT_EXISTING = ROOT / "data" / "research" / "print_pericope_headings.csv"
DEFAULT_OUTPUT = DEFAULT_EXISTING
DEFAULT_DIAGNOSTICS = ROOT / "output" / "print" / "print_pericope_headings_diagnostics.json"
SOURCE_PATHS = [
    ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv",
    ROOT / "data" / "raw" / "tr_greek" / "nt_full.csv",
]

FIELDNAMES = ["ref", "heading", "source_basis", "status"]
BSB_PLACEMENT_BASIS = (
    "Original CC-BY editorial heading reworded from public-domain BSB heading; placement "
    "informed by public-domain BSB section-heading structure"
)
CHAPTER_FALLBACK_BASIS = (
    "Original CC-BY editorial heading from project draft text; chapter-start "
    "fallback for print chapter coverage"
)
GENERATED_BASIS_MARKERS = (
    "KJV paragraph structure",
    "BSB section-heading structure",
    "chapter-start fallback",
)

LEADING_SKIP_WORDS = {
    "and",
    "but",
    "for",
    "then",
    "therefore",
    "now",
    "so",
}
SMALL_TITLE_WORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "but",
    "by",
    "for",
    "from",
    "in",
    "into",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
}
TITLE_FIXES = {
    "God": "God",
    "Lord": "Lord",
    "Jesus": "Jesus",
    "Christ": "Christ",
    "Spirit": "Spirit",
    "Israel": "Israel",
    "Jerusalem": "Jerusalem",
    "David": "David",
    "Moses": "Moses",
    "Abraham": "Abraham",
    "Abram": "Abram",
    "Isaac": "Isaac",
    "Jacob": "Jacob",
    "Joseph": "Joseph",
    "LORD": "Lord",
}
BOOK_NAME_ALIASES = {
    "Song": "Song of Solomon",
}
SOURCE_HEADING_REPLACEMENTS = {
    "God Arraigns Adam and Eve": "God Calls Adam and Eve",
    "The Punishment of Mankind": "Judgment on Humanity",
}


def load_source_verses(paths: list[Path]) -> tuple[list[str], dict[str, str], dict[str, list[str]]]:
    order: list[str] = []
    text_by_ref: dict[str, str] = {}
    refs_by_chapter: dict[str, list[str]] = {}
    for path in paths:
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                draft = row.get("draft_translation", "").strip()
                if not draft:
                    continue
                ref = row["ref"].strip()
                order.append(ref)
                text_by_ref[ref] = draft
                chapter_key = f"{row['book_name'].strip()} {leading_int(row['chapter'])}"
                refs_by_chapter.setdefault(chapter_key, []).append(ref)
    return order, text_by_ref, refs_by_chapter


def leading_int(value: str) -> int:
    match = re.match(r"\d+", value.strip())
    if not match:
        raise ValueError(f"Cannot read integer label from {value!r}")
    return int(match.group(0))


def load_existing(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["ref"].strip(): row for row in csv.DictReader(handle) if row.get("ref", "").strip()}


def usfm_book_name(data: str) -> str | None:
    match = re.search(r"\\toc2\s+([^\n]+)", data)
    if match:
        name = match.group(1).strip()
        return BOOK_NAME_ALIASES.get(name, name)
    match = re.search(r"\\h\s+([^\n]+)", data)
    if not match:
        return None
    name = match.group(1).strip()
    return BOOK_NAME_ALIASES.get(name, name)


def bsb_section_heading_refs(path: Path, wanted_books: set[str]) -> tuple[dict[str, str], dict[str, object]]:
    refs: dict[str, str] = {}
    counts = Counter()
    tag_counts = Counter()
    with zipfile.ZipFile(path) as archive:
        for name in archive.namelist():
            if not name.endswith(".usfm") or name.startswith("00-"):
                continue
            data = archive.read(name).decode("utf-8", errors="ignore")
            book = usfm_book_name(data)
            if book not in wanted_books:
                continue
            counts["books_seen"] += 1
            chapter: int | None = None
            pending_headings: list[str] = []
            for raw_line in data.splitlines():
                line = raw_line.strip()
                if not line:
                    continue
                chapter_match = re.match(r"\\c\s+(\d+)", line)
                if chapter_match:
                    chapter = int(chapter_match.group(1))
                    pending_headings = []
                    continue
                section_match = re.match(r"\\(s\d?|ms\d?|mr)\s+(.+)", line)
                if section_match:
                    tag = section_match.group(1)
                    counts["section_heading_lines"] += 1
                    tag_counts[tag] += 1
                    pending_headings.append(section_match.group(2).strip())
                    continue
                verse_match = re.match(r"\\v\s+(\d+)", line)
                if verse_match and chapter is not None:
                    verse = int(verse_match.group(1))
                    if pending_headings:
                        refs[f"{book} {chapter}:{verse}"] = " / ".join(pending_headings)
                        counts["section_heading_refs"] += 1
                    pending_headings = []
    return refs, {**dict(counts), "section_heading_tags": dict(tag_counts)}


def clean_for_heading(value: str) -> str:
    value = re.sub(r"\[[^\]]+\]", "", value)
    value = re.sub(r"\s+", " ", value)
    value = value.strip(" \"'.,;:!?")
    value = re.sub(r"^(and it came to be that|and it happened that|it came to be that|it happened that)\s+", "", value, flags=re.I)
    value = re.sub(r"^(and it came to be|and it happened|it came to be|it happened)\s+", "", value, flags=re.I)
    changed = True
    while changed:
        changed = False
        for word in LEADING_SKIP_WORDS:
            prefix = word + " "
            if value.lower().startswith(prefix):
                value = value[len(prefix) :].lstrip()
                changed = True
    split = re.split(r"(?<=[.!?])\s+|[;:]", value, maxsplit=1)[0]
    comma_split = split.split(",", 1)[0]
    if 3 <= len(comma_split.split()) <= 8:
        split = comma_split
    return split.strip(" \"'.,;:!?")


def title_case_word(word: str, *, first: bool) -> str:
    bare = re.sub(r"[^A-Za-z]", "", word)
    if not first and bare.lower() in SMALL_TITLE_WORDS:
        return word.lower()
    if word.lower().endswith("'s") and len(word) > 2:
        return title_case_word(word[:-2], first=first) + "'s"
    lower = bare.lower()
    for fixed in TITLE_FIXES.values():
        if lower == fixed.lower():
            return re.sub(re.escape(bare), fixed, word, flags=re.I)
    if "'" in word:
        return "'".join(part[:1].upper() + part[1:].lower() for part in word.split("'"))
    if "-" in word:
        return "-".join(part[:1].upper() + part[1:].lower() for part in word.split("-"))
    return word[:1].upper() + word[1:].lower()


def title_case(value: str) -> str:
    words = value.split()
    return " ".join(title_case_word(word, first=index == 0) for index, word in enumerate(words))


def heading_from_text(text: str) -> str:
    clean = clean_for_heading(text)
    words = re.findall(r"[A-Za-z][A-Za-z'’-]*|\d+", clean)
    if not words:
        return "Text Continues"
    max_words = 7
    if len(words) > 7 and words[0].lower() in {"the", "lord", "god", "jesus", "paul", "moses"}:
        max_words = 6
    heading = title_case(" ".join(words[:max_words]))
    heading = heading.replace("Lord God", "Lord God")
    return heading[:80].rstrip()


def reword_source_heading(value: str) -> str:
    value = value.replace("’", "'")
    value = re.sub(r"\s+", " ", value).strip(" \"'.,;:!?")
    value = SOURCE_HEADING_REPLACEMENTS.get(value, value)
    if value.startswith("The ") and not value.startswith("The Lord"):
        value = value.removeprefix("The ")
    value = value.replace("LORD", "Lord")
    value = title_case(value)
    return value[:80].rstrip()


def chapter_key_from_ref(ref: str) -> str:
    book_chapter, _verse = ref.rsplit(":", 1)
    return book_chapter


def build_rows(
    *,
    existing: dict[str, dict[str, str]],
    order: list[str],
    text_by_ref: dict[str, str],
    refs_by_chapter: dict[str, list[str]],
    bsb_headings: dict[str, str],
) -> tuple[list[dict[str, str]], dict[str, object]]:
    order_index = {ref: index for index, ref in enumerate(order)}
    bsb_refs = set(bsb_headings)
    wanted_refs: set[str] = {ref for ref in bsb_refs if ref in text_by_ref}
    fallback_refs: set[str] = set()
    for refs in refs_by_chapter.values():
        if refs and not any(ref in wanted_refs for ref in refs):
            fallback_refs.add(refs[0])
    wanted_refs.update(fallback_refs)

    rows: list[dict[str, str]] = []
    counts = Counter()
    for ref in sorted(wanted_refs, key=lambda item: order_index.get(item, 10**9)):
        existing_basis = existing.get(ref, {}).get("source_basis", "")
        preserve_existing = ref in existing and not any(marker in existing_basis for marker in GENERATED_BASIS_MARKERS)
        if preserve_existing:
            row = dict(existing[ref])
            row["source_basis"] = row.get("source_basis") or BSB_PLACEMENT_BASIS
            row["status"] = row.get("status") or "active"
            counts["preserved_existing"] += 1
        else:
            heading = heading_from_text(text_by_ref[ref]) if ref in fallback_refs else reword_source_heading(bsb_headings[ref])
            row = {
                "ref": ref,
                "heading": heading,
                "source_basis": CHAPTER_FALLBACK_BASIS if ref in fallback_refs else BSB_PLACEMENT_BASIS,
                "status": "active",
            }
            counts["generated"] += 1
            if ref in fallback_refs:
                counts["chapter_fallback"] += 1
        rows.append({field: row.get(field, "") for field in FIELDNAMES})

    return rows, {
        **dict(counts),
        "rows": len(rows),
        "bsb_refs": len(bsb_refs),
        "bsb_refs_directly_mapped": len(bsb_refs & set(text_by_ref)),
        "bsb_refs_not_in_project_verses": len(bsb_refs - set(text_by_ref)),
        "chapters": len(refs_by_chapter),
        "chapters_with_heading": sum(
            1 for refs in refs_by_chapter.values() if any(ref in wanted_refs for ref in refs)
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bsb-usfm", type=Path, default=DEFAULT_BSB_USFM)
    parser.add_argument("--existing", type=Path, default=DEFAULT_EXISTING)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    args = parser.parse_args()

    order, text_by_ref, refs_by_chapter = load_source_verses(SOURCE_PATHS)
    wanted_books = {ref.rsplit(" ", 1)[0] for ref in text_by_ref}
    existing = load_existing(args.existing)
    bsb_headings, bsb_diag = bsb_section_heading_refs(args.bsb_usfm, wanted_books)
    rows, row_diag = build_rows(
        existing=existing,
        order=order,
        text_by_ref=text_by_ref,
        refs_by_chapter=refs_by_chapter,
        bsb_headings=bsb_headings,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    diagnostics = {
        "bsb_usfm": str(args.bsb_usfm),
        "output": str(args.output),
        "source_policy": "Berean Standard Bible public-domain section heading starts supply placement and semantic seed; output wording is project-normalized/reworded, with draft-text headings used for chapter fallbacks.",
        "bsb": bsb_diag,
        "rows": row_diag,
    }
    args.diagnostics.parent.mkdir(parents=True, exist_ok=True)
    args.diagnostics.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(diagnostics, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
