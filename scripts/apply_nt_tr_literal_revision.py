#!/usr/bin/env python3
"""Apply a first full-NT TR literal revision pass to the imported source CSV."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "data" / "raw" / "tr_greek" / "nt_full.csv"
DEFAULT_REPORT = ROOT / "output" / "nt_tr_literal_revision_pass1_diagnostics.json"
DEFAULT_REVIEW_QUEUE = ROOT / "output" / "nt_tr_literal_revision_review_queue.csv"

REVIEW_COLUMNS = ["review_status", "review_notes"]
STRONGS_MARKER_RE = re.compile(r"\s*\([a-z]\.\s*[^)]*\)")


def load_rows(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def write_rows(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    for column in REVIEW_COLUMNS:
        if column not in fieldnames:
            fieldnames.append(column)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def replace_literal(
    text: str,
    pattern: str,
    replacement: str,
    note: str,
    notes: list[str],
    *,
    flags: int = 0,
) -> str:
    new_text, count = re.subn(pattern, replacement, text, flags=flags)
    if count:
        notes.append(note)
    return new_text


def replace_word(text: str, old: str, new: str, note: str, notes: list[str]) -> str:
    pattern = rf"\b{re.escape(old)}\b"

    def repl(match: re.Match[str]) -> str:
        value = match.group(0)
        if value.isupper():
            return new.upper()
        if value[0].isupper():
            return new[:1].upper() + new[1:]
        return new

    new_text, count = re.subn(pattern, repl, text, flags=re.I)
    if count:
        notes.append(note)
    return new_text


def replace_word_fixed(text: str, old: str, new: str, note: str, notes: list[str]) -> str:
    pattern = rf"\b{re.escape(old)}\b"
    new_text, count = re.subn(pattern, new, text, flags=re.I)
    if count:
        notes.append(note)
    return new_text


def clean_spacing(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s+([,.;:?!])", r"\1", text)
    text = re.sub(r"([.!?])([A-Z])", r"\1 \2", text)
    return text


def apply_general_revisions(text: str, notes: list[str]) -> str:
    cleaned, marker_count = STRONGS_MARKER_RE.subn("", text)
    if marker_count:
        notes.append("removed UKJV inline Strong-style lexical marker")
    text = cleaned

    phrase_replacements = [
        (r"\bfrom thenceforth\b", "from then on", "modernized from-thenceforth idiom"),
        (r"\bfrom henceforth\b", "from now on", "modernized from-henceforth idiom"),
        (r"\bfrom thence\b", "from there", "modernized from-thence idiom"),
        (r"\bfrom hence\b", "from here", "modernized from-hence idiom"),
        (r"\bno wise\b", "no way", "modernized no-wise idiom"),
        (r"\bin no way\b", "by no means", "aligned emphatic negation idiom"),
        (r"\bno more at all\b", "no longer", "modernized no-more-at-all idiom"),
        (r"\bin like manner\b", "likewise", "modernized like-manner idiom"),
    ]
    for pattern, replacement, note in phrase_replacements:
        text = replace_literal(text, pattern, replacement, note, notes, flags=re.I)

    replacements = [
        ("all of you", "you", "removed UKJV plural-expansion artifact"),
        ("unto", "to", "modernized archaic directional unto"),
        ("thereunto", "to this", "modernized thereunto"),
        ("hereunto", "to this", "modernized hereunto"),
        ("whosoever", "whoever", "modernized whosoever"),
        ("whatsoever", "whatever", "modernized whatsoever"),
        ("wherefore", "therefore", "modernized wherefore"),
        ("henceforth", "from now on", "modernized henceforth"),
        ("thenceforth", "from then on", "modernized thenceforth"),
        ("thence", "from there", "modernized thence"),
        ("thither", "there", "modernized thither"),
        ("hither", "here", "modernized hither"),
        ("behold", "look", "modernized behold"),
        ("brethren", "brothers", "rendered adelphoi-family wording as brothers"),
        ("raiment", "clothing", "modernized raiment"),
        ("garment", "clothing", "modernized garment where not contextually technical"),
        ("garments", "clothes", "modernized garments where not contextually technical"),
        ("divers", "various", "modernized divers"),
        ("sundry", "various", "modernized sundry"),
        ("forasmuch", "since", "modernized forasmuch"),
        ("straightway", "immediately", "modernized straightway"),
        ("forthwith", "immediately", "modernized forthwith"),
        ("yea", "yes", "modernized yea"),
        ("nay", "no", "modernized nay"),
        ("lo", "look", "modernized lo"),
        ("savour", "taste", "modernized savour"),
        ("palsy", "paralysis", "modernized palsy"),
        ("lunatic", "moonstruck", "literalized seleniazomai"),
        ("hewn", "cut", "modernized hewn"),
        ("trodden", "trampled", "modernized trodden"),
        ("fowls", "birds", "modernized fowls"),
        ("whore", "prostitute", "modernized porne wording"),
        ("whoremongers", "sexually immoral", "modernized pornos wording"),
        ("fornication", "sexual immorality", "modernized porneia wording"),
    ]
    for old, new, note in replacements:
        text = replace_word(text, old, new, note, notes)

    text = replace_literal(text, r"\bVerily,\s*verily\b", "truly, truly", "modernized verily", notes, flags=re.I)
    text = replace_literal(text, r"\bVerily\b", "truly", "modernized verily", notes, flags=re.I)
    text = replace_literal(text, r"\bbrings forth\b", "fathered", "aligned genealogy egennesen with fathered", notes)
    text = replace_literal(text, r"\bbring forth\b", "bear", "modernized childbirth bring-forth idiom", notes)
    text = replace_literal(text, r"\bbrought forth\b", "bore", "modernized childbirth bring-forth idiom", notes)
    text = replace_literal(text, r"\bwas minded to\b", "resolved to", "modernized was-minded idiom", notes)
    text = replace_literal(text, r"\bput her away\b", "release her", "aligned apoluo with release", notes)
    text = replace_literal(text, r"\bput away\b", "release", "aligned apoluo with release", notes)
    text = replace_literal(text, r"\bmake a public example\b", "expose publicly", "literalized paradeigmatizo wording", notes)
    return text


def apply_greek_triggered_revisions(row: dict[str, str], text: str, notes: list[str]) -> str:
    greek = row.get("greek_text", "")
    if "γεενν" in greek:
        text = replace_literal(text, r"\bhell fire\b", "Gehenna of fire", "rendered geenna as Gehenna", notes)
        text = replace_word(text, "hell", "Gehenna", "rendered geenna as Gehenna", notes)
    if re.search(r"\bαδ(ης|ην|ου|η)\b", greek):
        text = replace_word_fixed(text, "hell", "Hades", "rendered hades as Hades", notes)
    if "ταρταρ" in greek:
        text = replace_word(text, "hell", "Tartarus", "rendered tartaroo as Tartarus", notes)
    if "δαιμον" in greek:
        text = replace_literal(text, r"\bpossessed with devils\b", "demonized", "rendered daimonizomai as demonized", notes)
        text = replace_literal(text, r"\bpossessed by devils\b", "demonized", "rendered daimonizomai as demonized", notes)
        text = replace_word(text, "devils", "demons", "rendered daimonion as demon", notes)
        if "διαβολ" not in greek:
            text = replace_word(text, "devil", "demon", "rendered daimonion as demon", notes)
    if "εκκλησι" in greek:
        text = replace_word(text, "churches", "assemblies", "rendered ekklesia as assembly", notes)
        text = replace_word(text, "church", "assembly", "rendered ekklesia as assembly", notes)
    if "δουλ" in greek:
        text = replace_word(text, "servants", "slaves", "rendered doulos-family wording as slave", notes)
        text = replace_word(text, "servant", "slave", "rendered doulos-family wording as slave", notes)
    if "ευαγγελ" in greek or "ευηγγελ" in greek:
        text = replace_word(text, "gospel", "good news", "rendered euangelion as good news", notes)
    if "υιοι θεου" in greek or "υιους θεου" in greek:
        text = replace_literal(text, r"\bchildren of God\b", "sons of God", "kept huios as sons where Greek has sons of God", notes)
    if "αμην" in greek:
        text = replace_literal(text, r"\btruly,\s*truly,\s*I say\b", "Amen, amen, I say", "rendered amen formula directly", notes, flags=re.I)
        text = replace_literal(text, r"\btruly,\s*truly\b", "Amen, amen", "rendered amen formula directly", notes, flags=re.I)
        text = replace_literal(text, r"\btruly I say\b", "Amen, I say", "rendered amen formula directly", notes, flags=re.I)
        text = replace_literal(text, r"\bAmen I say\b", "Amen, I say", "normalized amen formula punctuation", notes)
        text = replace_literal(text, r"\bAmen,\s*Amen\b", "Amen, amen", "normalized amen formula casing", notes)
        if re.search(r"\bαμην\s+γαρ\s+λεγω\b", greek):
            text = replace_literal(text, r"\bFor Amen,\s*I say\b", "For truly I say", "kept gar-linked amen formula as for truly", notes)
            text = replace_literal(text, r"\bfor Amen,\s*I say\b", "for truly I say", "kept gar-linked amen formula as for truly", notes)
        if re.search(r"\bαμην\s+δε\s+λεγω\b", greek):
            text = replace_literal(text, r"\band Amen,\s*I say\b", "but truly I say", "kept de-linked amen formula as but truly", notes)
            text = replace_literal(text, r"\bAnd Amen,\s*I say\b", "But truly I say", "kept de-linked amen formula as but truly", notes)
            text = replace_literal(text, r"\bBut Amen,\s*I say\b", "But truly I say", "kept de-linked amen formula as but truly", notes)
    if "κυρι" in greek:
        text = replace_word_fixed(text, "LORD", "Lord", "normalized NT kurios as Lord", notes)
    return text


MANUAL_OVERRIDES = {
    "Matthew 1:1": "Book of the origin of Jesus Christ, son of David, son of Abraham.",
    "Matthew 1:18": "Now the birth of Jesus Christ was this way: after his mother Mary was betrothed to Joseph, before they came together, she was found having in womb from Holy Spirit.",
    "Mark 1:1": "Beginning of the good news of Jesus Christ, Son of God.",
    "Luke 1:1": "Since many took in hand to arrange an account concerning the matters fulfilled among us,",
    "John 1:1": "In beginning was the Word, and the Word was with God, and the Word was God.",
    "John 1:2": "This one was in beginning with God.",
    "John 1:3": "All things came to be through him, and apart from him not even one thing came to be that has come to be.",
    "John 1:4": "In him was life, and the life was the light of humans.",
    "John 1:5": "And the light shines in the darkness, and the darkness did not grasp it.",
    "Romans 1:1": "Paul, slave of Jesus Christ, called apostle, set apart for God's good news,",
    "Romans 1:2": "which he promised beforehand through his prophets in holy Scriptures,",
    "Romans 1:3": "concerning his Son, who came from David's seed according to flesh,",
    "Romans 1:4": "who was marked out Son of God in power according to Spirit of holiness by resurrection of dead ones: Jesus Christ our Lord,",
    "Revelation 1:1": "Revelation of Jesus Christ, which God gave him to show his slaves what must happen quickly; and he signified it, sending through his angel to his slave John,",
}


def revise_row(row: dict[str, str]) -> tuple[str, list[str], str]:
    ref = row.get("ref", "")
    if ref in MANUAL_OVERRIDES:
        return MANUAL_OVERRIDES[ref], ["manual TR literal override"], "tr_literal_manual"

    notes: list[str] = []
    text = row.get("draft_translation", "")
    text = apply_general_revisions(text, notes)
    text = apply_greek_triggered_revisions(row, text, notes)
    text = clean_spacing(text)
    if notes:
        return text, sorted(set(notes)), "tr_literal_pass1"
    return text, ["UKJV seed retained; needs focused Greek review"], "needs_focused_tr_review"


def write_review_queue(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["ref", "book_code", "greek_text", "draft_translation", "review_status", "review_notes"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            if row.get("review_status") != "needs_focused_tr_review":
                continue
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--review-queue", type=Path, default=DEFAULT_REVIEW_QUEUE)
    args = parser.parse_args()

    rows, fieldnames = load_rows(args.source)
    status_counts: Counter[str] = Counter()
    rule_counts: Counter[str] = Counter()
    changed_by_book: Counter[str] = Counter()
    examples: dict[str, list[dict[str, str]]] = defaultdict(list)

    for row in rows:
        original = row.get("draft_translation", "")
        revised, notes, status = revise_row(row)
        row["draft_translation"] = revised
        row["review_status"] = status
        row["review_notes"] = "; ".join(notes)
        status_counts[status] += 1
        if revised != original:
            changed_by_book[row.get("book_code", "")] += 1
        for note in notes:
            rule_counts[note] += 1
            if len(examples[note]) < 3:
                examples[note].append(
                    {
                        "ref": row.get("ref", ""),
                        "book_code": row.get("book_code", ""),
                        "draft_translation": revised,
                    }
                )

    write_rows(args.source, rows, fieldnames)
    write_review_queue(args.review_queue, rows)
    diagnostics = {
        "source": str(args.source),
        "rows": len(rows),
        "status_counts": dict(status_counts),
        "changed_by_book": dict(changed_by_book),
        "rule_counts": dict(rule_counts),
        "review_queue": str(args.review_queue),
        "review_queue_rows": status_counts.get("needs_focused_tr_review", 0),
        "examples": examples,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: diagnostics[k] for k in ["rows", "status_counts", "review_queue_rows"]}, indent=2))


if __name__ == "__main__":
    main()
