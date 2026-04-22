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

REVIEW_COLUMNS = ["ukjv_translation", "review_status", "review_notes"]
STRONGS_MARKER_RE = re.compile(r"\s*\([a-z]\.\s*[^)]*\)")


def greek_has_stem(greek: str, *stems: str) -> bool:
    return any(re.search(rf"(?<!\S){re.escape(stem)}\w*", greek) for stem in stems)


def greek_has_token_part(greek: str, *parts: str) -> bool:
    return any(re.search(rf"(?<!\S)\w*{re.escape(part)}\w*", greek) for part in parts)


def greek_has_phrase(greek: str, phrase: str) -> bool:
    return re.search(rf"(?<!\S){re.escape(phrase)}(?!\S)", greek) is not None


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
    text = re.sub(r"\bA overseer\b", "An overseer", text)
    text = re.sub(r"\ba overseer\b", "an overseer", text)
    return text


def apply_general_revisions(text: str, notes: list[str]) -> str:
    cleaned, marker_count = STRONGS_MARKER_RE.subn("", text)
    if marker_count:
        notes.append("removed UKJV inline Strong-style lexical marker")
    text = cleaned

    phrase_replacements = [
        (r"\bsince as\b", "since", "cleaned forasmuch-as modernization artifact"),
        (r"\bmust essentially\b", "must", "cleaned must-essentially source artifact"),
        (r"\bto day\b", "today", "modernized today spelling"),
        (r"\bto morrow\b", "tomorrow", "modernized tomorrow spelling"),
        (r"\ban hungered\b", "hungry", "modernized an-hungered idiom"),
        (r"\bhungered\b", "was hungry", "modernized hungered idiom"),
        (r"\bbe you not\b", "do not be", "modernized be-you-not imperative"),
        (r"\bare come\b", "have come", "modernized are-come perfect"),
        (r"\bis come\b", "has come", "modernized is-come perfect"),
        (r"\bwas come\b", "had come", "modernized was-come perfect"),
        (r"\bwere come\b", "had come", "modernized were-come perfect"),
        (r"\bsat at meat\b", "reclined at table", "modernized reclining-at-meal idiom"),
        (r"\bsat with him at meat\b", "reclined with him at table", "modernized reclining-at-meal idiom"),
        (r"\bsat at food\b", "reclined at table", "modernized reclining-at-meal idiom"),
        (r"\bsat with him at food\b", "reclined with him at table", "modernized reclining-at-meal idiom"),
        (r"\bat food\b", "at table", "modernized at-food artifact"),
        (r"\bhe that\b", "the one who", "modernized he-that relative"),
        (r"\bhim that\b", "him who", "modernized him-that relative"),
        (r"\bthey that\b", "those who", "modernized they-that relative"),
        (r"\bthem that\b", "those who", "modernized them-that relative"),
        (r"\bit came to pass\b", "it happened", "modernized came-to-pass idiom"),
        (r"\bshall come to pass\b", "will happen", "modernized come-to-pass idiom"),
        (r"\bcame to pass\b", "happened", "modernized came-to-pass idiom"),
        (r"\bfear not\b", "do not fear", "modernized fear-not imperative"),
        (r"\bbe not afraid\b", "do not be afraid", "modernized be-not-afraid imperative"),
        (r"\bhold your peace\b", "be silent", "modernized hold-your-peace idiom"),
        (r"\bsuffer little children\b", "allow little children", "modernized suffer-little-children idiom"),
        (r"\bsabbath day\b", "Sabbath", "modernized Sabbath-day wording"),
        (r"\bthe receipt of custom\b", "the tax booth", "modernized tax-booth idiom"),
        (r"\breceipt of custom\b", "tax booth", "modernized tax-booth idiom"),
        (r"\bsea coast\b", "seashore", "modernized sea-coast idiom"),
        (r"\bgoodman of the house\b", "householder", "modernized goodman-of-house idiom"),
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
        ("nigh", "near", "modernized nigh"),
        ("besought", "begged", "modernized besought"),
        ("beseech", "beg", "modernized beseech"),
        ("beseeching", "begging", "modernized beseeching"),
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
        ("damsel", "girl", "modernized damsel"),
        ("maid", "girl", "modernized maid"),
        ("publicans", "tax collectors", "rendered telones as tax collector"),
        ("publican", "tax collector", "rendered telones as tax collector"),
        ("corn", "grain", "modernized corn as grain"),
        ("scrip", "bag", "modernized scrip"),
        ("staves", "staffs", "modernized staves"),
        ("coats", "tunics", "rendered chiton as tunic"),
        ("coat", "tunic", "rendered chiton as tunic"),
        ("meat", "food", "modernized meat as food"),
        ("kinsfolk", "relatives", "modernized kinsfolk"),
        ("kinsman", "relative", "modernized kinsman"),
        ("coasts", "borders", "modernized coasts as borders"),
        ("coast", "border", "modernized coast as border"),
        ("slew", "killed", "modernized slew"),
        ("slay", "kill", "modernized slay"),
        ("slain", "killed", "modernized slain"),
        ("conversation", "conduct", "modernized conversation as conduct"),
        ("concupiscence", "desire", "modernized concupiscence"),
        ("shew", "show", "modernized shew"),
        ("whore", "prostitute", "modernized porne wording"),
        ("whoremongers", "sexually immoral", "modernized pornos wording"),
        ("fornication", "sexual immorality", "modernized porneia wording"),
    ]
    for old, new, note in replacements:
        text = replace_word(text, old, new, note, notes)

    cleanup_replacements = [
        (r"\bsince as\b", "since", "cleaned forasmuch-as modernization artifact"),
        (r"\bold clothing\b", "old garment", "cleaned old-garment wording"),
        (r"\bnew clothing\b", "new garment", "cleaned new-garment wording"),
        (r"\bevery thing\b", "everything", "modernized everything spelling"),
        (r"\bany thing\b", "anything", "modernized anything spelling"),
        (r"\bbe you not\b", "do not be", "modernized be-you-not imperative"),
        (r"\ban house\b", "a house", "modernized article before h-word"),
        (r"\ban hard\b", "a hard", "modernized article before h-word"),
        (r"\ban holy\b", "a holy", "modernized article before h-word"),
        (r"\ban high\b", "a high", "modernized article before h-word"),
        (r"\ban hundred\b", "a hundred", "modernized article before h-word"),
    ]
    for pattern, replacement, note in cleanup_replacements:
        text = replace_literal(text, pattern, replacement, note, notes, flags=re.I)
    text = replace_literal(text, r"\bA overseer\b", "An overseer", "fixed article before overseer", notes)
    text = replace_literal(text, r"\ba overseer\b", "an overseer", "fixed article before overseer", notes)

    text = replace_literal(text, r"\bVerily,\s*verily\b", "truly, truly", "modernized verily", notes, flags=re.I)
    text = replace_literal(text, r"\bVerily\b", "truly", "modernized verily", notes, flags=re.I)
    text = replace_literal(text, r"\bbrings forth\b", "produces", "rendered general brings-forth as produces", notes)
    text = replace_literal(text, r"\bbring forth\b", "bear", "modernized childbirth bring-forth idiom", notes)
    text = replace_literal(text, r"\bbrought forth\b", "bore", "modernized childbirth bring-forth idiom", notes)
    text = replace_word(text, "whoso", "whoever", "modernized whoso", notes)
    text = replace_word(text, "bishoprick", "oversight", "rendered episkope as oversight", notes)
    text = replace_word_fixed(text, "passover", "Passover", "capitalized Passover", notes)
    text = replace_word(text, "no man", "no one", "modernized no-man idiom", notes)
    text = replace_word(text, "any man", "anyone", "modernized any-man idiom", notes)
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
    if greek_has_token_part(greek, "γεννησ", "γεννηθ", "γεννημ", "γεννα"):
        text = replace_literal(text, r"\bproduces\b", "fathered", "aligned gennao with fathered", notes)
    if greek_has_stem(greek, "διαθηκ"):
        text = replace_word(text, "testaments", "covenants", "rendered diatheke as covenant", notes)
        text = replace_word(text, "testament", "covenant", "rendered diatheke as covenant", notes)
    if greek_has_stem(greek, "αφεσ"):
        text = replace_word(text, "remission", "forgiveness", "rendered aphesis as forgiveness", notes)
    if greek_has_stem(greek, "αγι"):
        text = replace_word(text, "saints", "holy ones", "rendered hagioi as holy ones", notes)
        text = replace_word(text, "saint", "holy one", "rendered hagios as holy one", notes)
    if greek_has_stem(greek, "επισκοπ"):
        text = replace_literal(text, r"\boffice of a bishop\b", "oversight", "rendered episkope as oversight", notes, flags=re.I)
        text = replace_word(text, "bishops", "overseers", "rendered episkopos as overseer", notes)
        text = replace_word(text, "bishop", "overseer", "rendered episkopos as overseer", notes)
    if greek_has_stem(greek, "διακον"):
        text = replace_literal(text, r"\blet them use the office of a deacon\b", "let them serve", "rendered diakoneo as serve", notes, flags=re.I)
        text = replace_literal(text, r"\buse the office of a deacon\b", "serve", "rendered diakoneo as serve", notes, flags=re.I)
        text = replace_literal(text, r"\bused the office of a deacon\b", "served", "rendered diakoneo as serve", notes, flags=re.I)
        text = replace_word(text, "deacons", "servants", "rendered diakonos as servant", notes)
        text = replace_word(text, "deacon", "servant", "rendered diakonos as servant", notes)
    if greek_has_stem(greek, "πλοιο"):
        text = replace_word(text, "ships", "boats", "rendered ploion as boat", notes)
        text = replace_word(text, "ship", "boat", "rendered ploion as boat", notes)
    if greek_has_stem(greek, "ασκ"):
        text = replace_word(text, "bottles", "wineskins", "rendered askos as wineskin", notes)
        text = replace_word(text, "bottle", "wineskin", "rendered askos as wineskin", notes)
    if greek_has_stem(greek, "οχλ"):
        text = replace_word(text, "multitudes", "crowds", "rendered ochlos as crowd", notes)
        text = replace_word(text, "multitude", "crowd", "rendered ochlos as crowd", notes)
    if greek_has_stem(greek, "διδασκαλ"):
        text = replace_word(text, "masters", "teachers", "rendered didaskalos as teacher", notes)
        text = replace_word(text, "master", "teacher", "rendered didaskalos as teacher", notes)
    if greek_has_stem(greek, "κωφ"):
        text = replace_word(text, "dumb", "mute", "rendered kophos as mute", notes)
    if greek_has_stem(greek, "σκανδαλ"):
        text = replace_literal(text, r"\boffend you\b", "cause you to stumble", "rendered skandalizo as stumble", notes, flags=re.I)
        text = replace_literal(text, r"\boffend them\b", "cause them to stumble", "rendered skandalizo as stumble", notes, flags=re.I)
        text = replace_literal(text, r"\boffend him\b", "cause him to stumble", "rendered skandalizo as stumble", notes, flags=re.I)
        text = replace_word(text, "offences", "stumbling blocks", "rendered skandalon as stumbling block", notes)
        text = replace_word(text, "offense", "stumbling block", "rendered skandalon as stumbling block", notes)
        text = replace_word(text, "offence", "stumbling block", "rendered skandalon as stumbling block", notes)
        text = replace_word(text, "offended", "stumbled", "rendered skandalizo as stumble", notes)
    if greek_has_stem(greek, "αιων"):
        text = replace_literal(text, r"\bend of the world\b", "completion of the age", "rendered synteleia tou aionos as completion of the age", notes, flags=re.I)
        text = replace_literal(text, r"\bends of the world\b", "ends of the ages", "rendered aion as age", notes, flags=re.I)
        if greek_has_phrase(greek, "αιωνος τουτου") or greek_has_phrase(greek, "του αιωνος τουτου") or greek_has_phrase(greek, "τω αιωνι τουτω"):
            text = replace_literal(text, r"\bthis world\b", "this age", "rendered this aion as this age", notes, flags=re.I)
        if greek_has_phrase(greek, "αιωνι τω ερχομενω") or greek_has_phrase(greek, "αιωνι τω μελλοντι"):
            text = replace_literal(text, r"\bworld to come\b", "age to come", "rendered coming aion as age to come", notes, flags=re.I)
    return text


MANUAL_OVERRIDES = {
    "Matthew 1:1": "Book of the origin of Jesus Christ, son of David, son of Abraham.",
    "Matthew 1:18": "Now the birth of Jesus Christ was this way: after his mother Mary was betrothed to Joseph, before they came together, she was found having in womb from Holy Spirit.",
    "Mark 1:1": "Beginning of the good news of Jesus Christ, Son of God.",
    "Luke 1:1": "Since many took in hand to arrange an account concerning the matters fulfilled among us,",
    "John 1:1": "In the beginning was the Word, and the Word was with God, and the Word was God.",
    "John 1:2": "This one was in the beginning with God.",
    "John 1:3": "All things came to be through him, and apart from him not even one thing came to be that has come to be.",
    "John 1:4": "In him was life, and the life was the light of humans.",
    "John 1:5": "And the light shines in the darkness, and the darkness did not grasp it.",
    "John 1:14": "And the Word became flesh and tabernacled among us, and we beheld his glory, glory as of an only-begotten from Father, full of grace and truth.",
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
    fieldnames = [
        "ref",
        "book_code",
        "greek_text",
        "draft_translation",
        "ukjv_translation",
        "review_status",
        "review_notes",
    ]
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
        if not row.get("ukjv_translation"):
            row["ukjv_translation"] = original
        seed = row.get("ukjv_translation") or original
        working_row = dict(row)
        working_row["draft_translation"] = seed
        revised, notes, status = revise_row(working_row)
        row["draft_translation"] = revised
        row["review_status"] = status
        row["review_notes"] = "; ".join(notes)
        status_counts[status] += 1
        if revised != seed:
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
        "method": "TR literal draft is primary in draft_translation; UKJV is preserved only as ukjv_translation witness.",
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
