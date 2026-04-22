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
        (r"\bhe which\b", "the one who", "modernized he-which relative"),
        (r"\bhim that\b", "him who", "modernized him-that relative"),
        (r"\bhim which\b", "him who", "modernized him-which relative"),
        (r"\bthey that\b", "those who", "modernized they-that relative"),
        (r"\bthey which\b", "those who", "modernized they-which relative"),
        (r"\bthem that\b", "those who", "modernized them-that relative"),
        (r"\bthem which\b", "those who", "modernized them-which relative"),
        (r"\bhe which\b", "the one who", "modernized he-which relative"),
        (r"\bit came to pass\b", "it happened", "modernized came-to-pass idiom"),
        (r"\bshall come to pass\b", "will happen", "modernized come-to-pass idiom"),
        (r"\bcame to pass\b", "happened", "modernized came-to-pass idiom"),
        (r"\bfear not\b", "do not fear", "modernized fear-not imperative"),
        (r"\bbe not afraid\b", "do not be afraid", "modernized be-not-afraid imperative"),
        (r"\bhold your peace\b", "be silent", "modernized hold-your-peace idiom"),
        (r"\bhold his peace\b", "be silent", "modernized hold-his-peace idiom"),
        (r"\bheld his peace\b", "was silent", "modernized held-his-peace idiom"),
        (r"\bhold their peace\b", "be silent", "modernized hold-their-peace idiom"),
        (r"\bheld their peace\b", "were silent", "modernized held-their-peace idiom"),
        (r"\bsuffer little children\b", "allow little children", "modernized suffer-little-children idiom"),
        (r"\bsabbath day\b", "Sabbath", "modernized Sabbath-day wording"),
        (r"\bthe receipt of custom\b", "the tax booth", "modernized tax-booth idiom"),
        (r"\breceipt of custom\b", "tax booth", "modernized tax-booth idiom"),
        (r"\bsea coast\b", "seashore", "modernized sea-coast idiom"),
        (r"\bgoodman of the house\b", "householder", "modernized goodman-of-house idiom"),
        (r"\bhas ought against\b", "has anything against", "modernized ought-as-anything idiom"),
        (r"\bhave ought against\b", "have anything against", "modernized ought-as-anything idiom"),
        (r"\bhad ought against\b", "had anything against", "modernized ought-as-anything idiom"),
        (r"\bwherewithal\b", "with what", "modernized wherewithal"),
        (r"\bwherewith\b", "with which", "modernized wherewith"),
        (r"\bwherein\b", "in which", "modernized wherein"),
        (r"\bwhereby\b", "by which", "modernized whereby"),
        (r"\bwist not\b", "did not know", "modernized wist-not idiom"),
        (r"\bknew not\b", "did not know", "modernized knew-not idiom"),
        (r"\bknow not\b", "do not know", "modernized know-not idiom"),
        (r"\bknows not\b", "does not know", "modernized knows-not idiom"),
        (r"\bbelieve not\b", "do not believe", "modernized believe-not idiom"),
        (r"\bbelieves not\b", "does not believe", "modernized believes-not idiom"),
        (r"\bfaint not\b", "do not faint", "modernized faint-not idiom"),
        (r"\btouch not\b", "do not touch", "modernized touch-not idiom"),
        (r"\btaste not\b", "do not taste", "modernized taste-not idiom"),
        (r"\bhandle not\b", "do not handle", "modernized handle-not idiom"),
        (r"\bgo not\b", "do not go", "modernized go-not idiom"),
        (r"\bsin not\b", "do not sin", "modernized sin-not idiom"),
        (r"\bjudge not\b", "do not judge", "modernized judge-not idiom"),
        (r"\bswear not\b", "do not swear", "modernized swear-not idiom"),
        (r"\bmarvel not\b", "do not marvel", "modernized marvel-not idiom"),
        (r"\bmine own\b", "my own", "modernized mine-own idiom"),
        (r"\bthine own\b", "your own", "modernized thine-own idiom"),
        (r"\byours ([A-Za-z])", r"your \1", "modernized yours before noun"),
        (r"\bearn expectation\b", "earnest expectation", "fixed earnest expectation artifact"),
        (r"\bthat that of\b", "than that of", "fixed than-that artifact"),
        (r"\bYou that destroys\b", "You who destroy", "modernized you-that relative"),
        (r"\byou that destroys\b", "you who destroy", "modernized you-that relative"),
        (r"\bpleaded them spitefully\b", "mistreated them", "fixed entreated-as-pleaded artifact"),
        (r"\bspitefully pleaded\b", "spitefully treated", "fixed entreated-as-pleaded artifact"),
        (r"\bpleaded him shamefully\b", "dishonored him", "fixed entreated-as-pleaded artifact"),
        (r"\bevil pleaded our fathers\b", "mistreated our fathers", "fixed entreated-as-pleaded artifact"),
        (r"\bcourteously pleaded Paul\b", "treated Paul kindly", "fixed entreated-as-pleaded artifact"),
        (r"\bshamefully pleaded\b", "shamefully treated", "fixed entreated-as-pleaded artifact"),
        (r"\bhow says you\b", "how do you say", "modernized how-says-you idiom"),
        (r"\bif he be\b", "if he is", "modernized if-he-be idiom"),
        (r"\bif Christ be\b", "if Christ is", "modernized if-Christ-be idiom"),
        (r"\bif there be\b", "if there is", "modernized if-there-be idiom"),
        (r"\bthere be no\b", "there is no", "modernized there-be idiom"),
        (r"\bthere be\b", "there is", "modernized there-be idiom"),
        (r"\bretore life in\b", "give life to", "rendered zoopoieo as gives life"),
        (r"\bretore life\b", "give life", "rendered zoopoieo as gives life"),
        (r"\breplenishes life to\b", "gives life to", "rendered zoopoieo as gives life"),
        (r"\breplenishes life\b", "gives life", "rendered zoopoieo as gives life"),
        (r"\bAnd you has he quickened, who were dead\b", "And you, being dead", "removed supplied quickened not present in verse"),
        (r"\bhas quickened us together with Christ\b", "he made us alive together with Christ", "rendered syzoopoieo as made alive together"),
        (r"\bhas he quickened together with him\b", "he made alive together with him", "rendered syzoopoieo as made alive together"),
        (r"\bnot quickened\b", "not made alive", "rendered zoopoieo as made alive"),
        (r"\bquickened by the Spirit\b", "made alive in spirit", "rendered zoopoieo as made alive"),
        (r"\ba just man and a holy\b", "a just and holy man", "fixed adjective-order artifact"),
        (r"\bGreet you one another\b", "Greet one another", "modernized greet-you imperative"),
        (r"\bwaxs old\b", "grows old", "fixed waxs-old artifact"),
        (r"\bWho now rejoice\b", "I now rejoice", "fixed first-person relative artifact"),
        (r"\bwaxed gross\b", "became dull", "modernized waxed-gross idiom"),
        (r"\bwaxed strong\b", "grew strong", "modernized waxed-strong idiom"),
        (r"\bwaxed a great tree\b", "became a great tree", "modernized waxed idiom"),
        (r"\bwaxed bold\b", "grew bold", "modernized waxed-bold idiom"),
        (r"\bwaxed valiant\b", "became valiant", "modernized waxed-valiant idiom"),
        (r"\bwaxed rich\b", "became rich", "modernized waxed-rich idiom"),
        (r"\bfrom thenceforth\b", "from then on", "modernized from-thenceforth idiom"),
        (r"\bfrom henceforth\b", "from now on", "modernized from-henceforth idiom"),
        (r"\bfrom thence\b", "from there", "modernized from-thence idiom"),
        (r"\bfrom hence\b", "from here", "modernized from-hence idiom"),
        (r"\bI know you not whence you are\b", "I do not know where you are from", "modernized know-not-whence idiom"),
        (r"\bWhence\b", "From where", "modernized whence"),
        (r"\bwhence\b", "from where", "modernized whence"),
        (r"\bno wise\b", "no way", "modernized no-wise idiom"),
        (r"\bin no way\b", "by no means", "aligned emphatic negation idiom"),
        (r"\bno more at all\b", "no longer", "modernized no-more-at-all idiom"),
        (r"\bin like manner\b", "likewise", "modernized like-manner idiom"),
        (r"\bwhereof\b", "of which", "modernized whereof"),
        (r"\bwhereon\b", "on which", "modernized whereon"),
        (r"\bthereof\b", "of it", "modernized thereof"),
        (r"\bthereby\b", "by it", "modernized thereby"),
        (r"\bhereby\b", "by this", "modernized hereby"),
        (r"\btherein\b", "in it", "modernized therein"),
        (r"\btherewith bless we\b", "with it we bless", "modernized therewith word order"),
        (r"\btherewith curse we\b", "with it we curse", "modernized therewith word order"),
        (r"\btherewith\b", "with it", "modernized therewith"),
        (r"\bwhich sleep\b", "who sleep", "modernized personal which as who"),
        (r"\bwhich sees\b", "who sees", "modernized personal which as who"),
        (r"\bwhich has an husband\b", "who has a husband", "modernized personal which as who"),
        (r"\bthem also who sleep\b", "those also who sleep", "modernized personal relative wording"),
        (r"\bthings which be not\b", "things that are not", "modernized things-which-be-not wording"),
        (r"\bFather also which\b", "Father also who", "modernized personal which as who"),
        (r"\bFather himself, which\b", "Father himself, who", "modernized personal which as who"),
        (r"\bSavior, which\b", "Savior, who", "modernized personal which as who"),
        (r"\bthe Father's will which has sent me\b", "the will of the Father who sent me", "fixed Father's-will relative wording"),
        (r"\bbaptized, which have received\b", "baptized, who have received", "modernized personal which as who"),
        (r"\bevery one which\b", "everyone who", "modernized every-one-which relative"),
        (r"\bany one which\b", "anyone who", "modernized any-one-which relative"),
        (r"\bsuch an one\b", "such a one", "modernized such-an-one idiom"),
        (r"\bfrom whence\b", "from where", "modernized from-whence idiom"),
        (r"\bfor ever\b", "forever", "modernized forever spelling"),
        (r"\bbe release from you\b", "be removed from you", "fixed be-release artifact"),
        (r"\bunder color as though\b", "under pretense as though", "modernized under-color idiom"),
        (r"\bWhich now of these\b", "Which of these", "modernized which-now idiom"),
        (r"\bLest lest by any means\b", "Lest by any means", "fixed duplicate lest artifact"),
        (r"\bafter they had were silent\b", "after they were silent", "fixed had-were artifact"),
        (r"\bto not a word\b", "not one word", "modernized answered-not wording"),
        (r"\bpins away\b", "pines away", "fixed pines-away spelling"),
        (r"\bBe not affrighted\b", "Do not be frightened", "modernized affrighted"),
        (r"\baffrighted\b", "frightened", "modernized affrighted"),
        (r"\bstrait gate\b", "narrow gate", "modernized strait-gate wording"),
        (r"\bin a strait between two\b", "pressed between two", "modernized in-a-strait idiom"),
        (r"\bby and by\b", "immediately", "modernized by-and-by idiom"),
        (r"\bhearkened\b", "listened", "modernized hearken"),
        (r"\bHearken\b", "Listen", "modernized hearken"),
        (r"\bhearken\b", "listen", "modernized hearken"),
        (r"\bwhere ever\b", "wherever", "modernized wherever spelling"),
        (r"\binsomuch that\b", "so that", "modernized insomuch-that idiom"),
        (r"\bEnter you in at\b", "Enter in through", "modernized enter-you-in idiom"),
        (r"\benter you into\b", "enter into", "modernized enter-you idiom"),
        (r"\bmany there is which go in thereat\b", "many are those who enter through it", "fixed many-there-is artifact"),
        (r"\bfew there is that find it\b", "few are those who find it", "fixed few-there-is artifact"),
        (r"\bBecause strait is the gate\b", "Because narrow is the gate", "modernized strait-gate wording"),
        (r"\bFrom where know you me\b", "How do you know me", "modernized whence-question idiom"),
        (r"\bwhich was crucified\b", "who was crucified", "modernized personal which as who"),
        (r"\ball that look it begin to mock\b", "all who see it begin to mock", "fixed look-it artifact"),
        (r"\bis not able to finish it\b", "cannot finish it", "modernized not-able wording"),
        (r"\byour Lord does come\b", "your Lord comes", "modernized does-come wording"),
        (r"\bcan not\b", "cannot", "modernized cannot spelling"),
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
        ("forbad", "forbade", "modernized forbad"),
        ("Jeremy", "Jeremiah", "standardized Jeremiah"),
        ("Judaea", "Judea", "standardized Judea spelling"),
        ("Rama", "Ramah", "standardized Ramah"),
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
        ("offence", "offense", "modernized offence spelling"),
        ("offences", "offenses", "modernized offence spelling"),
        ("Saviour", "Savior", "modernized Saviour spelling"),
        ("honours", "honors", "modernized honour spelling"),
        ("honoured", "honored", "modernized honour spelling"),
        ("honourable", "honorable", "modernized honour spelling"),
        ("honourably", "honorably", "modernized honour spelling"),
        ("honour", "honor", "modernized honour spelling"),
        ("labours", "labors", "modernized labour spelling"),
        ("laboured", "labored", "modernized labour spelling"),
        ("labouring", "laboring", "modernized labour spelling"),
        ("labourers", "laborers", "modernized labour spelling"),
        ("labourer", "laborer", "modernized labour spelling"),
        ("labour", "labor", "modernized labour spelling"),
        ("neighbours", "neighbors", "modernized neighbour spelling"),
        ("neighbour", "neighbor", "modernized neighbour spelling"),
        ("favours", "favors", "modernized favour spelling"),
        ("favoured", "favored", "modernized favour spelling"),
        ("favour", "favor", "modernized favour spelling"),
        ("marvelled", "marveled", "modernized marvelled spelling"),
        ("marvelling", "marveling", "modernized marvelling spelling"),
        ("marvellous", "marvelous", "modernized marvellous spelling"),
        ("clamour", "clamor", "modernized clamour spelling"),
        ("behaviour", "behavior", "modernized behaviour spelling"),
        ("colour", "color", "modernized colour spelling"),
        ("immoveable", "immovable", "modernized immoveable spelling"),
        ("unblameable", "blameless", "modernized unblameable"),
        ("irreproachable", "above reproach", "modernized irreproachable"),
        ("embodiment", "likeness", "rendered homoioma as likeness"),
        ("slew", "killed", "modernized slew"),
        ("slay", "kill", "modernized slay"),
        ("slain", "killed", "modernized slain"),
        ("bare", "bore", "modernized bare as bore"),
        ("brake", "broke", "modernized brake as broke"),
        ("durst", "dared", "modernized durst"),
        ("clave", "clung", "modernized clave"),
        ("abode", "remained", "modernized abode"),
        ("worshipped", "worshiped", "modernized worshipped spelling"),
        ("worshipping", "worshiping", "modernized worshipping spelling"),
        ("rumours", "rumors", "modernized rumours spelling"),
        ("recompence", "recompense", "modernized recompence spelling"),
        ("santifies", "sanctifies", "fixed sanctifies spelling"),
        ("wrought", "worked", "modernized wrought"),
        ("conversation", "conduct", "modernized conversation as conduct"),
        ("concupiscence", "desire", "modernized concupiscence"),
        ("shew", "show", "modernized shew"),
        ("victuals", "food", "modernized victuals"),
        ("fishes", "fish", "modernized fishes plural"),
        ("gainsayers", "opponents", "modernized gainsayers"),
        ("gainsaying", "contradiction", "modernized gainsaying"),
        ("gainsay", "contradict", "modernized gainsay"),
        ("meats", "foods", "modernized meats"),
        ("counsellors", "counselors", "modernized counsellor spelling"),
        ("counsellor", "counselor", "modernized counsellor spelling"),
        ("harlots", "prostitutes", "modernized porne wording"),
        ("harlot", "prostitute", "modernized porne wording"),
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
        (r"\bbe release from you\b", "be removed from you", "fixed be-release artifact"),
        (r"\bher which is release\b", "her who has been released", "fixed release participle artifact"),
        (r"\bher that is release from her husband\b", "her who has been released from her husband", "fixed release participle artifact"),
        (r"\binsomuch as\b", "so that", "modernized insomuch-as idiom"),
        (r"\bEnter you in at\b", "Enter in through", "modernized enter-you-in idiom"),
        (r"\ball that look it begin to mock\b", "all who see it begin to mock", "fixed look-it artifact"),
        (r"\bI know you not From where you are\b", "I do not know where you are from", "modernized know-not-whence idiom"),
        (r"\bI know you not from where you are\b", "I do not know where you are from", "modernized know-not-whence idiom"),
        (r"\bfrom From where\b", "from where", "fixed from-whence artifact"),
        (r"\bFrom From where\b", "From where", "fixed from-whence artifact"),
        (r"\btell From where\b", "tell from where", "fixed whence casing after tell"),
        (r"\bknow From where\b", "know from where", "fixed whence casing after know"),
        (r"\bknows From where\b", "knows from where", "fixed whence casing after knows"),
        (r"\band From where\b", "and from where", "fixed whence casing after and"),
        (r"\bAnd From where\b", "And from where", "fixed whence casing after and"),
        (r"\bSavior, which\b", "Savior, who", "modernized personal which as who"),
        (r"\bunder color as though\b", "under pretense as though", "modernized under-color idiom"),
        (
            r"\b(God|Father|Lord|Christ|Jesus|Son|man|men|woman|women|child|children|people|priest|priests|scribe|scribes|Pharisee|Pharisees|disciple|disciples|angel|angels|prophet|prophets) which\b",
            r"\1 who",
            "modernized personal which as who",
        ),
        (
            r"\b(God|Father|Lord|Christ|Jesus|Son|man|men|woman|women|child|children|people|priest|priests|scribe|scribes|Pharisee|Pharisees|disciple|disciples|angel|angels|prophet|prophets), which\b",
            r"\1, who",
            "modernized personal which as who",
        ),
        (r"\brighteousness of God who is\b", "righteousness of God which is", "fixed non-person relative after righteousness"),
        (r"\blove of God, who is\b", "love of God, which is", "fixed non-person relative after love"),
        (r"\bgrace of God who is\b", "grace of God which is", "fixed non-person relative after grace"),
        (r"\bgrace of God who was\b", "grace of God which was", "fixed non-person relative after grace"),
        (r"\bspirit of man who is\b", "spirit of man which is", "fixed non-person relative after spirit of man"),
        (r"\bbegged him who he\b", "begged him that he", "fixed him-that relative artifact"),
        (r"\bdesired him who he\b", "desired him that he", "fixed him-that relative artifact"),
        (r"\bdesiring him who he\b", "desiring him that he", "fixed him-that relative artifact"),
        (r"\bcharged him who he\b", "charged him that he", "fixed him-that relative artifact"),
        (r"\bprayed him who he\b", "asked him that he", "fixed prayed-him relative artifact"),
        (r"\baccused to him who he\b", "accused to him that he", "fixed him-that relative artifact"),
        (r"\bseen him who he was blind\b", "seen him when he was blind", "fixed seen-him relative artifact"),
        (r"\btears him who he foams again\b", "tears him so that he foams again", "fixed him-that relative artifact"),
        (r"\bJudas, which betrayed\b", "Judas, who betrayed", "modernized personal which as who"),
        (r"\bJudas, which had betrayed\b", "Judas, who had betrayed", "modernized personal which as who"),
        (r"\bJudas, which was guide\b", "Judas, who became guide", "modernized personal which as who"),
        (r"\bwhich shall fulfill all my will\b", "who shall fulfill all my will", "modernized personal which as who"),
        (r"\bword of God, and which had not worshiped\b", "word of God, and those who had not worshiped", "fixed Revelation relative artifact"),
        (r"\bby this know you the Spirit\b", "By this you know the Spirit", "fixed know-you word order"),
        (r"\bhad sexual contact with her not till she had bore\b", "did not know her until she had borne", "fixed borne grammar"),
        (
            r"\bThen immediately they departed from him who should have examined him\b",
            "Then immediately those who were about to examine him departed from him",
            "fixed Acts 22:29 relative artifact",
        ),
        (r"\bdispensation of God who is given\b", "dispensation of God which is given", "fixed non-person relative after dispensation"),
        (r"\bassembly of God, who he has purchased\b", "assembly of God, which he has purchased", "fixed non-person relative after assembly"),
        (r"\bpeople who he foreknew\b", "people whom he foreknew", "fixed whom relative after people"),
        (r"\bwitness of God who he has testified\b", "witness of God which he has testified", "fixed non-person relative after witness"),
        (
            r"\bcharged those who they should tell no one: but the more he charged them, so much the more a great deal they published it\b",
            "charged them that they should tell no one: but the more he charged them, so much the more they proclaimed it",
            "fixed Mark 7:36 relative artifact",
        ),
        (r"\bcharged those who they should\b", "charged them that they should", "fixed charged-them relative artifact"),
        (r"\bcommanded those who they should\b", "commanded them that they should", "fixed commanded-them relative artifact"),
        (r"\bsee Jesus who he was\b", "see who Jesus was", "fixed Luke 19:3 word order"),
        (r"\bcried the more a great deal\b", "cried out much more", "fixed cried-more artifact"),
        (r"\bbruising him hardly departs from him\b", "with difficulty departs from him, bruising him", "fixed hardly-departs word order"),
        (r"\bsat down to food\b", "reclined at table", "modernized reclining-at-meal idiom"),
        (r"\bWhat\? do you not know\b", "Or do you not know", "fixed rhetorical question wording"),
        (r"\bcondemn not\b", "do not condemn", "modernized condemn-not idiom"),
        (r"\bTake you him\b", "Take him yourselves", "fixed take-you-him imperative"),
        (r"\bin the which\b", "in which", "modernized in-the-which wording"),
        (r"\bDo you not know your own selves\b", "Do you not know yourselves", "modernized own-selves wording"),
        (r"\bThese things write I to you\b", "I write these things to you", "modernized write-I word order"),
        (r"\bthese things write I to you\b", "I write these things to you", "modernized write-I word order"),
        (r"\bThis day is salvation come\b", "Today salvation has come", "modernized salvation-has-come wording"),
        (r"\bwhich was since the law\b", "which came after the law", "fixed Hebrews 7:28 temporal wording"),
        (r"\bfor evermore\b", "forevermore", "modernized forevermore spelling"),
        (r"\bif lest by any means\b", "if perhaps", "fixed if-lest artifact"),
        (r"\bsave Jesus only\b", "except Jesus only", "modernized save-as-except wording"),
        (r"\bsave Jesus Christ\b", "except Jesus Christ", "modernized save-as-except wording"),
        (r"\bfor my sake and the good news's\b", "for my sake and the good news", "fixed good-news possessive artifact"),
        (r"\? do you not know\b", "? Do you not know", "fixed question sentence casing"),
        (r"\bbe you not\b", "do not be", "modernized be-you-not imperative"),
        (r"\ban house\b", "a house", "modernized article before h-word"),
        (r"\ban hard\b", "a hard", "modernized article before h-word"),
        (r"\ban holy\b", "a holy", "modernized article before h-word"),
        (r"\ban high\b", "a high", "modernized article before h-word"),
        (r"\ban harlot\b", "a harlot", "modernized article before h-word"),
        (r"\ban heart\b", "a heart", "modernized article before h-word"),
        (r"\ban hymn\b", "a hymn", "modernized article before h-word"),
        (r"\ban hundred\b", "a hundred", "modernized article before h-word"),
        (r"\ban prostitute\b", "a prostitute", "fixed article before prostitute"),
    ]
    for pattern, replacement, note in cleanup_replacements:
        text = replace_literal(text, pattern, replacement, note, notes, flags=re.I)
    text = replace_literal(text, r"\bso that that field\b", "so that field", "cleaned so-that-that wording", notes)
    text = replace_literal(text, r"^from where\b", "From where", "fixed sentence-initial whence casing", notes)
    text = replace_literal(text, r"\bcome they not behind\b", "are they not from here", "rendered enteuthen question as from here", notes)
    text = replace_literal(text, r"\bI know you not\b", "I do not know you", "modernized know-you-not idiom", notes)
    text = replace_literal(text, r"\bKnow you not\b", "Do you not know", "modernized know-you-not question", notes)
    text = replace_literal(text, r"\bknow you not\b", "do you not know", "modernized know-you-not question", notes)
    text = replace_literal(text, r"\bSpeak you not\b", "Do you not speak", "modernized speak-you-not question", notes)
    text = replace_literal(text, r"\byour's\b", "yours", "modernized possessive pronoun spelling", notes)
    text = replace_literal(text, r"\bour's\b", "ours", "modernized possessive pronoun spelling", notes)
    text = replace_literal(text, r"\btheir's\b", "theirs", "modernized possessive pronoun spelling", notes)
    text = replace_literal(text, r"\bmine account\b", "my account", "modernized mine-account wording", notes)
    text = replace_literal(text, r"\bearn heed\b", "earnest heed", "fixed earnest-heed artifact", notes)
    text = replace_literal(text, r"\bsay ought to you\b", "say anything to you", "modernized ought-as-anything idiom", notes)
    text = replace_literal(text, r"\bdo ought for\b", "do anything for", "modernized ought-as-anything idiom", notes)
    text = replace_literal(text, r"\bsaw ought\b", "saw anything", "modernized ought-as-anything idiom", notes)
    text = replace_literal(text, r"\bbrought him ought to eat\b", "brought him anything to eat", "modernized ought-as-anything idiom", notes)
    text = replace_literal(text, r"\bhad ought to accuse\b", "had anything to accuse", "modernized ought-as-anything idiom", notes)
    text = replace_literal(text, r"\bowes you ought\b", "owes you anything", "modernized ought-as-anything idiom", notes)
    text = replace_literal(text, r"\bbe you ware also\b", "beware of him also", "modernized be-ware idiom", notes)
    text = replace_literal(text, r"\bware no clothes\b", "wore no clothes", "modernized ware as wore", notes)
    text = replace_literal(text, r"\bvery chiefest\b", "foremost", "modernized chiefest", notes)
    text = replace_literal(text, r"\bchiefest\b", "foremost", "modernized chiefest", notes)
    text = replace_literal(text, r"\bovermuch\b", "excessive", "modernized overmuch", notes)
    text = replace_literal(text, r"\bOf whom beware of him also\b", "Beware of him also", "fixed be-ware artifact", notes)
    text = replace_literal(
        text,
        r"\bneither said any of those who ought of the things which he possessed was his own\b",
        "neither did any of them say that anything of the things which he possessed was his own",
        "modernized ought-as-anything idiom",
        notes,
    )
    text = replace_literal(text, r"\bwith him who day\b", "with him that day", "fixed him-that-day artifact", notes)
    text = replace_literal(text, r"\bFor the which cause\b", "For this reason", "modernized for-which-cause idiom", notes)
    text = replace_literal(text, r"\bFor which cause\b", "For this reason", "modernized for-which-cause idiom", notes)
    text = replace_literal(text, r"\bfor which cause\b", "for this reason", "modernized for-which-cause idiom", notes)
    text = replace_literal(text, r"\bto him who he may find\b", "to him that he may find", "fixed him-that relative artifact", notes)
    text = replace_literal(text, r"\bthat that day should\b", "that the day should", "fixed that-that-day artifact", notes)
    text = replace_literal(text, r"\ban hill\b", "a hill", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban herd\b", "a herd", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban hundredfold\b", "a hundredfold", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban householder\b", "a householder", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban stumbling\b", "a stumbling", "modernized article before consonant sound", notes)
    text = replace_literal(text, r"\ban hook\b", "a hook", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban nations man\b", "a man of the nations", "fixed nations-man article artifact", notes)
    text = replace_literal(text, r"\bhad an barrier in his speech\b", "had a speech impediment", "modernized speech-impediment wording", notes)
    text = replace_literal(text, r"\ban hedge\b", "a hedge", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban horn\b", "a horn", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban husband\b", "a husband", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban hair\b", "a hair", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban honeycomb\b", "a honeycomb", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban haven\b", "a haven", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban Hebrew\b", "a Hebrew", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban holyday\b", "a holy day", "modernized holy day spelling", notes)
    text = replace_literal(text, r"\ban helmet\b", "a helmet", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban heretic\b", "a heretic", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban heifer\b", "a heifer", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban heavenly\b", "a heavenly", "modernized article before h-word", notes)
    text = replace_literal(text, r"\ban half\b", "a half", "modernized article before h-word", notes)
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
    text = replace_literal(text, r"\bputs away\b", "releases", "aligned apoluo with release", notes)
    text = replace_literal(text, r"\bput away\b", "release", "aligned apoluo with release", notes)
    text = replace_literal(text, r"\bbe release from you\b", "be removed from you", "fixed be-release artifact", notes, flags=re.I)
    text = replace_literal(text, r"\bher which is release\b", "her who has been released", "fixed release participle artifact", notes, flags=re.I)
    text = replace_literal(text, r"\bher that is release from her husband\b", "her who has been released from her husband", "fixed release participle artifact", notes, flags=re.I)
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
        text = replace_word(text, "bond", "slave", "rendered doulos-family wording as slave", notes)
    if "ευαγγελ" in greek or "ευηγγελ" in greek:
        text = replace_word(text, "gospel", "good news", "rendered euangelion as good news", notes)
    if greek_has_stem(greek, "μαγ"):
        text = replace_literal(text, r"\bwise men\b", "Magi", "rendered magoi as Magi", notes, flags=re.I)
    if greek_has_stem(greek, "εθν"):
        text = replace_word_fixed(text, "Gentiles", "nations", "rendered ethne as nations", notes)
        text = replace_word_fixed(text, "Gentile", "nation", "rendered ethnos as nation", notes)
        text = replace_word(text, "heathen", "nations", "rendered ethne as nations", notes)
    if greek_has_stem(greek, "σκυθ"):
        text = replace_word(text, "Savages", "Scythian", "rendered Skythes as Scythian", notes)
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
    if greek_has_phrase(greek, "ειπερ"):
        text = replace_literal(text, r"\bIf so be that\b", "If indeed", "rendered eiper as if indeed", notes)
        text = replace_literal(text, r"\bif so be that\b", "if indeed", "rendered eiper as if indeed", notes)
    if greek_has_phrase(greek, "ειγε"):
        text = replace_literal(text, r"\bIf so be that\b", "If indeed", "rendered eige as if indeed", notes)
        text = replace_literal(text, r"\bif so be that\b", "if indeed", "rendered eige as if indeed", notes)
    if greek_has_phrase(greek, "εαν γενηται"):
        text = replace_literal(
            text,
            r"\bAnd if so be that he find it\b",
            "And if it happens that he finds it",
            "rendered ean genetai as if it happens",
            notes,
        )
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
        text = replace_literal(text, r"\bminister of sin\b", "servant of sin", "rendered diakonos as servant", notes, flags=re.I)
        text = replace_literal(text, r"\bminister the same\b", "serve the same", "rendered diakoneo as serve", notes, flags=re.I)
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
    if greek_has_stem(greek, "αλαλ"):
        text = replace_word(text, "dumb", "mute", "rendered alalos as mute", notes)
    if greek_has_stem(greek, "αφων"):
        text = replace_word(text, "dumb", "voiceless", "rendered aphonos as voiceless", notes)
    if greek_has_stem(greek, "σιωπ"):
        text = replace_word(text, "dumb", "silent", "rendered siopao as silent", notes)
    if greek_has_stem(greek, "ομολογ"):
        text = replace_word(text, "profession", "confession", "rendered homologia as confession", notes)
    if greek_has_stem(greek, "φιαλ"):
        text = replace_word(text, "vials", "bowls", "rendered phiale as bowl", notes)
        text = replace_word(text, "vial", "bowl", "rendered phiale as bowl", notes)
    if greek_has_stem(greek, "ζωντ") or greek_has_stem(greek, "ζωσι"):
        text = replace_literal(text, r"\bquick and dead\b", "living and dead", "rendered living/dead idiom", notes, flags=re.I)
    if greek_has_phrase(greek, "μη γενοιτο"):
        text = replace_literal(text, r"\bGod forbid\b", "may it not be", "rendered me genoito directly", notes, flags=re.I)
        text = replace_literal(text, r"^may it not be\b", "May it not be", "rendered me genoito directly", notes)
        text = replace_literal(text, r"([.!?]\s+)may it not be\b", r"\1May it not be", "rendered me genoito directly", notes)
    if greek_has_stem(greek, "παρεσιν"):
        text = replace_literal(text, r"\bremission of sins that are past\b", "passing over of sins that had happened before", "rendered paresis as passing over", notes, flags=re.I)
    if greek_has_stem(greek, "κρι"):
        text = replace_word(text, "damnation", "judgment", "rendered krima/krisis as judgment", notes)
    if greek_has_stem(greek, "απωλει"):
        text = replace_word(text, "perdition", "destruction", "rendered apoleia as destruction", notes)
    if greek_has_stem(greek, "σπλαγχν"):
        text = replace_literal(text, r"\bbowels of compassion\b", "compassion", "rendered splanchna compassion idiom", notes, flags=re.I)
        text = replace_literal(text, r"\bin the bowels of Jesus Christ\b", "in the deep affection of Jesus Christ", "rendered splanchna affection idiom", notes, flags=re.I)
        text = replace_literal(text, r"\bbowels and mercies\b", "deep affections and mercies", "rendered splanchna affection idiom", notes, flags=re.I)
        text = replace_literal(text, r"\binward parts and mercies\b", "deep affections and mercies", "rendered splanchna affection idiom", notes, flags=re.I)
        text = replace_word(text, "bowels", "inward parts", "rendered splanchna as inward parts", notes)
    if greek_has_stem(greek, "πτυ"):
        text = replace_word(text, "fan", "winnowing fork", "rendered ptuon as winnowing fork", notes)
    if greek_has_stem(greek, "αλων"):
        text = replace_literal(text, r"\bthoroughly purge his floor\b", "thoroughly cleanse his threshing floor", "rendered halon as threshing floor", notes, flags=re.I)
        text = replace_literal(text, r"\bpurge his floor\b", "cleanse his threshing floor", "rendered halon as threshing floor", notes, flags=re.I)
    if greek_has_stem(greek, "αποθηκ"):
        text = replace_word(text, "garner", "storehouse", "rendered apotheke as storehouse", notes)
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
    if greek_has_stem(greek, "αιωνι"):
        text = replace_word(text, "everlasting", "eternal", "rendered aionios as eternal", notes)
    if greek_has_stem(greek, "εντευθεν"):
        text = replace_literal(text, r"\bfrom behind\b", "from here", "rendered enteuthen as from here", notes, flags=re.I)
    if greek_has_stem(greek, "επιχορηγ"):
        text = replace_word(text, "ministered", "supplied", "rendered epichoregeo as supply", notes)
        text = replace_word(text, "ministers", "supplies", "rendered epichoregeo as supply", notes)
        text = replace_word(text, "minister", "supply", "rendered epichoregeo as supply", notes)
    if greek_has_stem(greek, "αξι") and greek_has_stem(greek, "μετανοι"):
        text = replace_literal(text, r"\bmeet for repentance\b", "worthy of repentance", "rendered axios as worthy", notes, flags=re.I)
    return text


def apply_final_cleanups(text: str, notes: list[str]) -> str:
    final_replacements = [
        (r"\ban stumbling block\b", "a stumbling block", "modernized article before consonant sound"),
        (r"\ban nations man\b", "a man of the nations", "fixed nations-man article artifact"),
        (r"\ban habitation\b", "a habitation", "modernized article before h-word"),
        (r"\bwhich also waited for the kingdom\b", "who also waited for the kingdom", "modernized personal which as who"),
        (r"\bcraved the body\b", "asked for the body", "modernized craved"),
        (r"\bcast out into the draught\b", "cast out into the latrine", "rendered draught as latrine"),
        (r"\bgoes out into the draught\b", "goes out into the latrine", "rendered draught as latrine"),
        (r"\bnets for a draught\b", "nets for a catch", "rendered draught as catch"),
        (r"\bat the draught of the fish\b", "at the catch of fish", "rendered draught as catch"),
        (r"\bGet you behind me\b", "Get behind me", "modernized get-you imperative"),
        (r"\btaste not the things that be of God\b", "do not mind the things that are of God", "rendered phroneo as mind"),
        (r"\btaste not the things that be of men\b", "do not mind the things that are of men", "rendered phroneo as mind"),
        (r"\bthings that be of God\b", "things that are of God", "modernized things-that-be wording"),
        (r"\bthings that be of men\b", "things that are of men", "modernized things-that-be wording"),
        (r"\bthose that be of men\b", "those that are of men", "modernized things-that-be wording"),
        (r"\bthose who be in Judea\b", "those who are in Judea", "modernized who-be wording"),
        (r"\bTo all that be in Rome\b", "To all who are in Rome", "modernized all-that-be wording"),
        (r"\bthe powers that be\b", "the powers that exist", "modernized powers-that-be wording"),
        (r"\bGet you behind, Satan\b", "Get behind me, Satan", "modernized get-you imperative"),
        (r"\bDo not you yet understand\b", "Do you not yet understand", "modernized inverted question"),
        (r"\bDo not you fear God\b", "Do you not fear God", "modernized inverted question"),
        (r"\bdo not you judge\b", "do you not judge", "modernized inverted question"),
        (r"\bdo not you yield\b", "do not yield", "modernized do-not-you imperative"),
        (r"\bdo not your alms\b", "do not do your charitable giving", "modernized alms wording"),
        (r"\bdo not you after their works\b", "do not do according to their works", "modernized do-not-you wording"),
        (r"\bGo you therefore\b", "Go therefore", "modernized go-you imperative"),
        (r"\bGo you into\b", "Go into", "modernized go-you imperative"),
        (r"\bGo you also\b", "Go also", "modernized go-you imperative"),
        (r"\bgo you and learn\b", "go and learn", "modernized go-you imperative"),
        (r"\bgo you to the sea\b", "go to the sea", "modernized go-you imperative"),
        (r"\bgo you out\b", "go out", "modernized go-you imperative"),
        (r"\bgo you rather\b", "go rather", "modernized go-you imperative"),
        (r"\bgo you not therefore\b", "do not go therefore", "modernized go-you-not imperative"),
        (r"\bWhom say you that I am\b", "Who do you say that I am", "modernized inverted question"),
        (r"\bwhom say you that I am\b", "who do you say that I am", "modernized inverted question"),
        (r"\bSay you, His disciples\b", "Say, His disciples", "modernized say-you imperative"),
        (r"\bsay you that the Lord\b", "say that the Lord", "modernized say-you imperative"),
        (r"\bsay you to the householder\b", "say to the householder", "modernized say-you imperative"),
        (r"\bSay you of him\b", "Do you say of him", "modernized inverted question"),
        (r"\bWhat think you\?", "What do you think?", "modernized inverted question"),
        (r"\bwhat think you\?", "what do you think?", "modernized inverted question"),
        (r"\bWhat think you of Christ\b", "What do you think of Christ", "modernized inverted question"),
        (r"\bThink you that\b", "Do you think that", "modernized inverted question"),
        (r"\bthink you that\b", "do you think that", "modernized inverted question"),
        (r"\bTherefore think you evil\b", "Why do you think evil", "modernized inverted question"),
        (r"\bHow think you\?", "What do you think?", "modernized inverted question"),
        (r"\bWhich of these three, think you,\b", "Which of these three, do you think,", "modernized inverted question"),
        (r"\bWhom think you that I am\b", "Who do you think that I am", "modernized inverted question"),
        (r"\bWhat will you that I shall do to you\b", "What do you want me to do for you", "modernized what-will-you idiom"),
        (r"\bWhat will you that I should do to you\b", "What do you want me to do for you", "modernized what-will-you idiom"),
        (r"\bWhere will you that we prepare\b", "Where do you want us to prepare", "modernized where-will-you idiom"),
        (r"\bWhere will you that we go and prepare\b", "Where do you want us to go and prepare", "modernized where-will-you idiom"),
        (r"\bWill you that I release\b", "Do you want me to release", "modernized will-you-that idiom"),
        (r"\bWhom will you that I release\b", "Whom do you want me to release", "modernized will-you-that idiom"),
        (r"\bWhether of the two will you that I release\b", "Which of the two do you want me to release", "modernized will-you-that idiom"),
        (r"\bPray you therefore the Lord\b", "Pray therefore to the Lord", "modernized pray-you imperative"),
        (r"\bpray you therefore the Lord\b", "pray therefore to the Lord", "modernized pray-you imperative"),
        (r"\bpray you that your flight\b", "pray that your flight", "modernized pray-you imperative"),
        (r"\bI pray you, come\b", "I ask you, come", "modernized I-pray-you wording"),
        (r"\bI pray you have me excused\b", "I ask you, have me excused", "modernized I-pray-you wording"),
        (r"\bI pray you therefore\b", "I ask you therefore", "modernized I-pray-you wording"),
        (r"\bI pray you, of whom\b", "I ask you, of whom", "modernized I-pray-you wording"),
        (r"\bI pray you that you would hear us\b", "I ask you that you would hear us", "modernized I-pray-you wording"),
        (r"\bI pray you to take some food\b", "I ask you to take some food", "modernized I-pray-you wording"),
        (r"\bAfter this manner therefore pray you\b", "Therefore pray this way", "modernized pray-you imperative"),
        (r"\bPray you to the Lord\b", "Pray to the Lord", "modernized pray-you imperative"),
        (r"\bwe pray you in Christ's position\b", "we plead with you in Christ's place", "modernized pray-you wording"),
        (r"\bTake no thought for\b", "Do not be anxious for", "modernized take-no-thought idiom"),
        (r"\btake no thought for\b", "do not be anxious for", "modernized take-no-thought idiom"),
        (r"\btake you thought for\b", "are you anxious for", "modernized take-you-thought idiom"),
        (r"\btaking thought\b", "being anxious", "modernized taking-thought idiom"),
        (r"\bBut Who do you say\b", "But who do you say", "fixed question casing"),
        (r"\bOur Father who are in heaven\b", "Our Father who is in heaven", "fixed Father relative agreement"),
        (r"\bthey toil not\b", "they do not toil", "modernized toil-not wording"),
        (r"\bthey spin not\b", "they do not spin", "modernized spin-not wording"),
        (r"\byour flight be not in the winter\b", "your flight not be in the winter", "modernized be-not clause"),
        (r"\bWhat think you, Simon\b", "What do you think, Simon", "modernized inverted question"),
        (r"\bWhat think you, that\b", "What do you think, that", "modernized inverted question"),
        (r"\bTake that your is\b", "Take what is yours", "fixed yours artifact"),
        (r"\byour is the kingdom\b", "yours is the kingdom", "fixed yours artifact"),
        (r"\bnot yet full come\b", "not yet fully come", "modernized full-come idiom"),
        (r"\bAnd presently the fig tree\b", "And immediately the fig tree", "modernized presently"),
        (r"\bshall presently give me\b", "shall immediately give me", "modernized presently"),
        (r"\bhope to send presently\b", "hope to send soon", "modernized presently"),
        (r"\bJesus prevented him\b", "Jesus anticipated him", "modernized prevented-as-anticipated"),
        (r"\bWhat means this\?", "What does this mean?", "modernized what-means-this question"),
        (r"\bwill you that we command\b", "do you want us to command", "modernized will-you-that idiom"),
        (r"\bwill you therefore that I release\b", "do you therefore want me to release", "modernized will-you-that idiom"),
        (r"\bWhat will you then that I shall do\b", "What then do you want me to do", "modernized what-will-you idiom"),
        (r"\bwhat will you have me to do\b", "what do you want me to do", "modernized what-will-you idiom"),
        (r"\bWill you be made whole\b", "Do you want to be made whole", "modernized will-you question"),
        (r"\bWhat will you\?", "What do you want?", "modernized what-will-you question"),
        (r"\bBe you therefore\b", "Be therefore", "modernized be-you imperative"),
        (r"\bbe you therefore\b", "be therefore", "modernized be-you imperative"),
        (r"\bbe you there until\b", "stay there until", "modernized be-you imperative"),
        (r"\bbe you clean\b", "be clean", "modernized be-you imperative"),
        (r"\bBe you removed\b", "Be removed", "modernized be-you imperative"),
        (r"\bbe you cast\b", "be cast", "modernized be-you imperative"),
        (r"\bBe you plucked up\b", "Be plucked up", "modernized be-you imperative"),
        (r"\bbe you planted\b", "be planted", "modernized be-you imperative"),
        (r"\bbe you called\b", "be called", "modernized be-you imperative"),
        (r"\bbe you also ready\b", "be also ready", "modernized be-you imperative"),
        (r"\bbe you sure\b", "be sure", "modernized be-you imperative"),
        (r"\bbe you of doubtful mind\b", "be of doubtful mind", "modernized be-you imperative"),
        (r"\bbe you transformed\b", "be transformed", "modernized be-you imperative"),
        (r"\bbe you followers\b", "be followers", "modernized be-you imperative"),
        (r"\bbe you idolaters\b", "be idolaters", "modernized be-you imperative"),
        (r"\bbe you children\b", "be children", "modernized be-you imperative"),
        (r"\bbe you steadfast\b", "be steadfast", "modernized be-you imperative"),
        (r"\bbe you reconciled\b", "be reconciled", "modernized be-you imperative"),
        (r"\bbe you also enlarged\b", "be also enlarged", "modernized be-you imperative"),
        (r"\bbe you separate\b", "be separate", "modernized be-you imperative"),
        (r"\bbe you kind\b", "be kind", "modernized be-you imperative"),
        (r"\bbe you thankful\b", "be thankful", "modernized be-you imperative"),
        (r"\bbe you an example\b", "be an example", "modernized be-you imperative"),
        (r"\bbe you partaker\b", "be partaker", "modernized be-you imperative"),
        (r"\bbe you doers\b", "be doers", "modernized be-you imperative"),
        (r"\bbe you warmed\b", "be warmed", "modernized be-you imperative"),
        (r"\bbe you holy\b", "be holy", "modernized be-you imperative"),
        (r"\bbe you all of one mind\b", "be all of one mind", "modernized be-you imperative"),
        (r"\bbe you faithful\b", "be faithful", "modernized be-you imperative"),
        (r"\bBlessed be you poor\b", "Blessed are you poor", "modernized blessed-be-you wording"),
        (r"\bBe not you therefore like\b", "Do not therefore be like", "modernized be-not-you imperative"),
        (r"\bBe not you therefore partakers\b", "Do not therefore be partakers", "modernized be-not-you imperative"),
        (r"\bBe not you therefore ashamed\b", "Do not therefore be ashamed", "modernized be-not-you imperative"),
        (r"\bbe not you called\b", "do not be called", "modernized be-not-you imperative"),
        (r"\bbe not you the slaves\b", "do not be slaves", "modernized be-not-you imperative"),
        (r"\bBe not high-minded\b", "Do not be high-minded", "modernized be-not imperative"),
        (r"\bBe not wise\b", "Do not be wise", "modernized be-not imperative"),
        (r"\bBe not overcome\b", "Do not be overcome", "modernized be-not imperative"),
        (r"\bBe not deceived\b", "Do not be deceived", "modernized be-not imperative"),
        (r"\bBe not forgetful\b", "Do not be forgetful", "modernized be-not imperative"),
        (r"\bBe not carried about\b", "Do not be carried about", "modernized be-not imperative"),
        (r"\bbe not terrified\b", "do not be terrified", "modernized be-not imperative"),
        (r"\band be not faithless\b", "and do not be faithless", "modernized be-not imperative"),
        (r"\bAnd be not conformed\b", "And do not be conformed", "modernized be-not imperative"),
        (r"\band be not conformed\b", "and do not be conformed", "modernized be-not imperative"),
        (r"\bbe not children\b", "do not be children", "modernized be-not imperative"),
        (r"\band be not entangled\b", "and do not be entangled", "modernized be-not imperative"),
        (r"\bAnd be not drunk\b", "And do not be drunk", "modernized be-not imperative"),
        (r"\bbe not bitter\b", "do not be bitter", "modernized be-not imperative"),
        (r"\bbe not weary\b", "do not be weary", "modernized be-not imperative"),
        (r"\bbe not ignorant\b", "do not be ignorant", "modernized be-not imperative"),
        (r"\bBe not you\b", "Do not be", "modernized be-not-you imperative"),
        (r"\bbe not, as\b", "do not be, as", "modernized be-not imperative"),
        (r"\bresist not evil\b", "do not resist evil", "modernized resist-not wording"),
        (r"\bforgive not men\b", "do not forgive men", "modernized forgive-not wording"),
        (r"\bforgive not every one\b", "do not forgive every one", "modernized forgive-not wording"),
        (r"\blittle ones which believe\b", "little ones who believe", "modernized personal which as who"),
        (r"\bJews which believed\b", "Jews who believed", "modernized personal which as who"),
        (r"\bthey of the circumcision which believed\b", "those of the circumcision who believed", "modernized personal which as who"),
        (r"\bthere are which believe\b", "there are who believe", "modernized personal which as who"),
        (r"\bnations which believe\b", "nations that believe", "modernized nations relative as that"),
        (r"\bTo you therefore which believe\b", "To you therefore who believe", "modernized personal which as who"),
        (r"\belders, which had come to him\b", "elders, who had come to him", "modernized personal which as who"),
        (r"\bPharisees and doctors of the law sitting by, which had come\b", "Pharisees and doctors of the law sitting by, who had come", "modernized personal which as who"),
        (r"\bit is better for him who a millstone were hanged about his neck\b", "it is better for him if a millstone were hung around his neck", "fixed millstone relative artifact"),
        (r"\bit were better for him who a millstone were hanged about his neck\b", "it would be better for him if a millstone were hung around his neck", "fixed millstone relative artifact"),
        (r"^do not judge\b", "Do not judge", "fixed sentence casing"),
        (r"\bDo not therefore be like to them\b", "Do not therefore be like them", "modernized like-to wording"),
        (r"\bBe therefore perfect\b", "Therefore be perfect", "modernized be-therefore order"),
        (r"\bBe you also over five cities\b", "Be over five cities also", "modernized be-you imperative"),
        (r"\bBe you come out\b", "Have you come out", "modernized be-you question"),
        (r"\bBe you angry\b", "Be angry", "modernized be-you imperative"),
        (r"\bBe you also patient\b", "Be also patient", "modernized be-you imperative"),
        (r"\bIf so be you have tasted\b", "If indeed you have tasted", "modernized if-so-be wording"),
        (r"\bif it be you\b", "if it is you", "modernized if-it-be wording"),
        (r"\byou be not troubled\b", "you are not troubled", "modernized be-not clause"),
        (r"\byou be not deceived\b", "you are not deceived", "modernized be-not clause"),
        (r"\byou be not judged\b", "you not be judged", "modernized be-not clause"),
        (r"\bwho be disobedient\b", "who are disobedient", "modernized who-be wording"),
        (r"\bevil communications corrupt good manners\b", "evil company corrupts good morals", "modernized communications-good-manners idiom"),
        (r"\bWhat\? do you not know\b", "Or do you not know", "fixed rhetorical question wording"),
        (r"\bDo you not know your own selves\b", "Do you not know yourselves", "modernized own-selves wording"),
        (r"\bfor my sake,? and the good news's\b", "for my sake and the good news", "fixed good-news possessive artifact"),
        (r"\bfor the good news's sake\b", "for the sake of the good news", "fixed good-news possessive artifact"),
        (r"\bhad sexual contact with her not till she had bore\b", "did not know her until she had borne", "fixed borne grammar"),
        (r"\bjust man and a holy\b", "just and holy man", "fixed adjective-order artifact"),
        (r"\bentreated them spitefully\b", "mistreated them", "rendered hybrizo as mistreat"),
        (r"\bwhich were his friends\b", "who were his friends", "modernized personal which as who"),
        (r"\badventure himself\b", "venture himself", "modernized adventure-as-venture"),
        (r"\bover the which\b", "over which", "modernized over-the-which wording"),
        (r"\bassembly of God, who he has purchased\b", "assembly of God, which he has purchased", "fixed non-person relative after assembly"),
        (r"\bgraven by are and man's device\b", "engraved by art and man's device", "fixed graven-by-art typo"),
        (r"\bthe more part\b", "most", "modernized more-part idiom"),
        (r"\bthat you not be judged\b", "that you may not be judged", "fixed negative subjunctive wording"),
        (r"\bSince then as\b", "Since then", "modernized since-then-as wording"),
        (r"\bsince then as\b", "since then", "modernized since-then-as wording"),
        (r"\bbecause that\b", "because", "modernized because-that wording"),
        (r"\bof which you have heard\b", "concerning which you have heard", "aligned peri relative wording"),
        (r"\bdoes not righteousness\b", "does not do righteousness", "fixed do-righteousness wording"),
        (r"\bmade a man everything whole\b", "made a man entirely whole", "fixed everything-whole artifact"),
        (r"\bWhom Do you want\b", "Whom do you want", "fixed question casing"),
        (r"\bdo not fear you\b", "do not fear", "modernized fear-not imperative"),
        (r"\bon the sabbath days\b", "on the Sabbath", "modernized Sabbath-days wording"),
        (r"\bBrothers which are\b", "Brothers who are", "modernized personal which as who"),
        (r"\bbrothers which are\b", "brothers who are", "modernized personal which as who"),
        (r"\bwhich also bears fruit\b", "who also bears fruit", "modernized personal which as who"),
        (r"\bclothed with a clothing down to the foot\b", "clothed with a garment reaching to the feet", "fixed clothing-down-to-foot artifact"),
        (r"\bThe Brothers who are\b", "The brothers who are", "fixed brothers casing"),
        (r"\bbrothers, Has not God\b", "brothers, has not God", "fixed question casing"),
        (r"\bsaying, be silent\b", "saying, Be silent", "fixed imperative casing"),
        (r"\bor to do evil\? to save life\b", "or to do evil? To save life", "fixed question casing"),
        (r"\brepented not\b", "did not repent", "modernized repented-not wording"),
        (r"\bperished not\b", "did not perish", "modernized perished-not wording"),
        (r"\bbelieved not\b", "did not believe", "modernized believed-not wording"),
        (r"\bwe wrestle not against\b", "we do not wrestle against", "modernized wrestle-not wording"),
        (r"\bare became rich\b", "became rich", "fixed became-rich artifact"),
        (r"\bAnd think not to say\b", "And do not think to say", "modernized think-not wording"),
        (r"\bThink not that\b", "Do not think that", "modernized think-not wording"),
        (r"\bthink not that\b", "do not think that", "modernized think-not wording"),
        (r"\bI I think not not\b", "I do not think so", "fixed duplicated think-not artifact"),
        (r"\bin such an hour as you think not\b", "at an hour you do not expect", "modernized think-not wording"),
        (r"\bat an hour when you think not\b", "at an hour when you do not expect", "modernized think-not wording"),
        (r"\bFear them not therefore\b", "Do not fear them therefore", "modernized fear-not imperative"),
        (r"\bFear you not therefore\b", "Do not fear therefore", "modernized fear-not imperative"),
        (r"\bbrings not forth\b", "does not bring forth", "modernized brings-not wording"),
        (r"\bfell not\b", "did not fall", "modernized fell-not wording"),
        (r"\bfast not\b", "do not fast", "modernized fast-not wording"),
        (r"\btakes not\b", "does not take", "modernized takes-not wording"),
        (r"\bseeing see not\b", "seeing do not see", "modernized see-not wording"),
        (r"\bhearing they hear not\b", "hearing they do not hear", "modernized hear-not wording"),
        (r"\band went not\b", "and did not go", "modernized went-not wording"),
        (r"\bJesus went not with\b", "Jesus did not go with", "modernized went-not wording"),
        (r"\bthey themselves went not into\b", "they themselves did not go into", "modernized went-not wording"),
        (r"\bwhich went not astray\b", "that did not go astray", "modernized went-not wording"),
        (r"\byou enter not into temptation\b", "you not enter into temptation", "modernized enter-not wording"),
        (r"\beat not\b", "do not eat", "modernized eat-not wording"),
        (r"\bprevailed not\b", "did not prevail", "modernized prevailed-not wording"),
        (r"\blived not again\b", "did not live again", "modernized lived-not wording"),
        (r"\bdoes corrupt\b", "corrupt", "fixed does-corrupt agreement"),
        (r"\bare dead which sought\b", "are dead who sought", "modernized personal which as who"),
        (r"\byour sins be forgiven you\b", "your sins are forgiven you", "modernized sins-be-forgiven wording"),
        (r"\bwhen you do alms\b", "when you do charitable giving", "modernized alms wording"),
        (r"\bthat that deceiver said\b", "that this deceiver said", "fixed that-that wording"),
        (r"\bthat that disciple should not die\b", "that disciple would not die", "fixed that-that wording"),
        (r"\bin earth\b", "on earth", "modernized in-earth wording"),
        (r"\bif the house be worthy\b", "if the house is worthy", "modernized if-be wording"),
        (r"\bif it be not worthy\b", "if it is not worthy", "modernized if-be wording"),
        (r"\bbe not darkness\b", "not be darkness", "modernized be-not clause"),
        (r"\bIf you then be not able\b", "If then you are not able", "modernized be-not clause"),
        (r"\bif you be not that Christ\b", "if you are not the Christ", "modernized if-be wording"),
        (r"\bWe be not born\b", "We were not born", "modernized we-be wording"),
        (r"\bthough he be not far\b", "though he is not far", "modernized be-not clause"),
        (r"\bthat I be not wearisome\b", "that I may not be wearisome", "modernized be-not clause"),
        (r"\bthough they be not circumcised\b", "though they are not circumcised", "modernized be-not clause"),
        (r"\bIf I be not an apostle\b", "If I am not an apostle", "modernized if-be wording"),
        (r"\bif the woman be not covered\b", "if the woman is not covered", "modernized be-not clause"),
        (r"\bthat the ministry be not blamed\b", "that the ministry not be blamed", "modernized be-not clause"),
        (r"\bthat you be not consumed\b", "that you not be consumed", "modernized be-not clause"),
        (r"\bsays not the law\b", "does not the law say", "modernized says-not question"),
        (r"\bHe says not,", "He does not say,", "modernized says-not wording"),
        (r"\bsays not,", "does not say,", "modernized says-not wording"),
        (r"\bloves me not\b", "does not love me", "modernized loves-not wording"),
        (r"\bloves not\b", "does not love", "modernized loves-not wording"),
        (r"\bcomes not\b", "does not come", "modernized comes-not wording"),
        (r"\bhears not\b", "does not hear", "modernized hears-not wording"),
        (r"\breceives not\b", "does not receive", "modernized receives-not wording"),
        (r"\bkeeps not\b", "does not keep", "modernized keeps-not wording"),
        (r"\bdwells not\b", "does not dwell", "modernized dwells-not wording"),
        (r"\babides not\b", "does not abide", "modernized abides-not wording"),
        (r"\bregards not\b", "does not regard", "modernized regards-not wording"),
        (r"\beats not\b", "does not eat", "modernized eats-not wording"),
    ]
    for pattern, replacement, note in final_replacements:
        text = replace_literal(text, pattern, replacement, note, notes, flags=re.I)
    case_sensitive_replacements = [
        (r"\bWhom Do\b", "Whom do", "fixed question casing"),
        (r"\bto The brothers\b", "to the brothers", "fixed brothers casing"),
        (r"\band The brothers\b", "and the brothers", "fixed brothers casing"),
        (r"\ball The brothers\b", "all the brothers", "fixed brothers casing"),
        (r"\bSalute The brothers\b", "Salute the brothers", "fixed brothers casing"),
        (r"\bThe brothers who are\b", "the brothers who are", "fixed brothers casing"),
    ]
    for pattern, replacement, note in case_sensitive_replacements:
        text = replace_literal(text, pattern, replacement, note, notes)
    text = replace_literal(
        text,
        r"\b(holy ones|servants|Jews|apostles|brothers|elders|nations) which\b",
        r"\1 who",
        "modernized personal which as who",
        notes,
    )
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
    "Romans 3:25": "whom God set forth as propitiation through faith in his blood, for a display of his righteousness because of the passing over of the sins that had happened before, in the forbearance of God;",
    "Romans 3:31": "Do we then make void the law through faith? May it not be. Rather, we establish the law.",
    "Romans 7:7": "What then shall we say? Is the law sin? May it not be. But I did not know sin except through the law: for I had not known desire, unless the law had said, You shall not covet.",
    "Galatians 4:4": "But when the fullness of the time had come, God sent forth his Son, having come from a woman, having come under law,",
    "Hebrews 9:16": "For where a will is, the death of the one who made it must be established.",
    "Hebrews 9:17": "For a will is firm when people are dead, since it never has force while the one who made it lives.",
    "Hebrews 9:18": "Therefore neither was the first covenant inaugurated without blood.",
    "Philippians 2:1": "If therefore there is any consolation in Christ, if any comfort of love, if any fellowship of the Spirit, if any deep affections and mercies,",
    "1 John 5:1": "Everyone who believes that Jesus is the Christ has been born of God: and everyone who loves the one who fathered loves also the one begotten from him.",
    "Galatians 2:17": "But if, while seeking to be justified in Christ, we ourselves also were found sinners, then is Christ a servant of sin? May it not be.",
    "2 Corinthians 9:10": "Now may the one who supplies seed to the sower and bread for food supply and multiply your seed sown, and increase the fruits of your righteousness;",
    "1 Corinthians 9:2": "If I am not an apostle to others, yet indeed I am to you: for you are the seal of my apostleship in the Lord.",
    "Philippians 1:8": "For God is my witness, how I long for you all in the deep affection of Jesus Christ.",
    "1 Timothy 1:4": "nor to give heed to myths and endless genealogies, which produce disputes rather than godly edification which is in faith.",
    "1 Peter 4:10": "As each received a gift, serve it to one another, as good stewards of the manifold grace of God.",
    "1 Peter 5:13": "She who is in Babylon, elect together with you, greets you; and Marcus my son.",
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
    text = apply_final_cleanups(text, notes)
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
