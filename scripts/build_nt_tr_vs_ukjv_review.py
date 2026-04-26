#!/usr/bin/env python3
"""Build NT TR literal draft vs UKJV witness review outputs."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
DEFAULT_SOURCE = ROOT / "data" / "raw" / "tr_greek" / "nt_full.csv"
DEFAULT_REVIEW_CSV = OUTPUT / "fresh_nt_tr_vs_ukjv_review.csv"
DEFAULT_PRIORITY_CSV = OUTPUT / "fresh_nt_tr_vs_ukjv_priority_review.csv"
DEFAULT_PRIORITY_MD = OUTPUT / "fresh_nt_tr_vs_ukjv_priority_review.md"
DEFAULT_QUEUE_CSV = OUTPUT / "fresh_nt_tr_vs_ukjv_review_queue.csv"
DEFAULT_QUEUE_MD = OUTPUT / "fresh_nt_tr_vs_ukjv_review_queue.md"
DEFAULT_DIAGNOSTICS = OUTPUT / "fresh_nt_tr_vs_ukjv_review_diagnostics.json"
REVIEW_DIR = ROOT / "data" / "research"
RESOLVED_REVIEW_STATUSES = {"keep", "revised"}
STRONGS_MARKER_RE = re.compile(r"\([a-z]\.\s*[^)]+\)")
NON_COMPARE_WORD_RE = re.compile(r"[^a-z0-9\s]")
SPACE_RE = re.compile(r"\s+")
REVIEW_PASS_RE = re.compile(r"nt_review_pass_(\d+)\.md$")
BACKTICK_VALUE_RE = re.compile(r"`([^`]+)`")
COMPARISON_REPLACEMENTS = [
    ("all of you all", "you"),
    ("all of you", "you"),
    ("unto", "to"),
    ("thereunto", "to this"),
    ("hereunto", "to this"),
    ("whosoever", "whoever"),
    ("whatsoever", "whatever"),
    ("wherefore", "therefore"),
    ("henceforth", "from now on"),
    ("thenceforth", "from then on"),
    ("thence", "from there"),
    ("thither", "there"),
    ("offence", "offense"),
    ("saviour", "savior"),
    ("honour", "honor"),
    ("judaea", "judea"),
    ("enquire", "inquire"),
    ("enquired", "inquired"),
    ("enquiring", "inquiring"),
    ("whilst", "while"),
    ("he that", "the one who"),
    ("he which", "the one who"),
    ("which was", "who was"),
    ("which were", "who were"),
    ("which is", "who is"),
    ("which are", "who are"),
]
COMPARISON_REPLACEMENT_PATTERNS = [
    (re.compile(rf"\b{re.escape(old)}\b"), new)
    for old, new in COMPARISON_REPLACEMENTS
]

REVIEW_FIELDNAMES = [
    "ref",
    "book_code",
    "book_name",
    "chapter",
    "verse",
    "review_status",
    "importance",
    "priority_score",
    "themes",
    "keyword_hits",
    "same_normalized",
    "tr_literal_translation",
    "ukjv_translation",
    "review_notes",
    "latest_review_status",
    "latest_review_pass",
    "reasons",
    "decision",
]

THEME_TERMS = {
    "christology": [
        "jesus",
        "christ",
        "son of god",
        "son of man",
        "lord",
        "word",
        "only begotten",
        "firstborn",
        "king",
        "messiah",
    ],
    "soteriology": [
        "save",
        "saved",
        "salvation",
        "savior",
        "faith",
        "believe",
        "grace",
        "justify",
        "righteous",
        "righteousness",
        "forgive",
        "forgiveness",
        "redeem",
        "redemption",
        "blood",
        "cross",
        "resurrection",
        "raised",
    ],
    "spirit_church": [
        "spirit",
        "holy spirit",
        "assembly",
        "church",
        "baptize",
        "baptism",
        "apostle",
        "prophet",
        "elder",
        "overseer",
    ],
    "law_covenant": [
        "law",
        "commandment",
        "covenant",
        "scripture",
        "promise",
        "israel",
        "jew",
        "gentile",
        "circumcision",
    ],
    "judgment_afterlife": [
        "judgment",
        "judge",
        "wrath",
        "condemn",
        "hell",
        "gehenna",
        "hades",
        "tartarus",
        "death",
        "life eternal",
        "eternal life",
        "fire",
    ],
    "anthropology_ethics": [
        "flesh",
        "body",
        "soul",
        "heart",
        "sin",
        "repent",
        "love",
        "mercy",
        "peace",
        "hope",
        "slave",
        "servant",
        "sexual immorality",
    ],
    "textual_literal": [
        "amen",
        "truly",
        "good news",
        "gospel",
        "demon",
        "devil",
        "angel",
        "messenger",
        "son",
        "seed",
    ],
}

NOTE_WEIGHTS = {
    "manual TR literal override": 8,
    "rendered geenna as Gehenna": 8,
    "rendered hades as Hades": 8,
    "rendered tartaroo as Tartarus": 8,
    "rendered ekklesia as assembly": 7,
    "rendered doulos-family wording as slave": 6,
    "rendered euangelion as good news": 6,
    "kept huios as sons where Greek has sons of God": 6,
    "rendered amen formula directly": 5,
    "kept gar-linked amen formula as for truly": 5,
    "kept de-linked amen formula as but truly": 5,
    "normalized NT kurios as Lord": 4,
    "rendered daimonion as demon": 4,
    "rendered daimonizomai as demonized": 4,
}

STYLE_ONLY_NOTES = {
    "capitalized Passover",
    "cleaned forasmuch-as modernization artifact",
    "cleaned must-essentially source artifact",
    "fixed Father relative agreement",
    "fixed do-righteousness wording",
    "fixed earnest expectation artifact",
    "fixed clothing-down-to-foot artifact",
    "fixed question casing",
    "fixed sentence casing",
    "fixed sanctifies spelling",
    "fixed everything-whole artifact",
    "fixed brothers casing",
    "fixed became-rich artifact",
    "fixed does-corrupt agreement",
    "fixed duplicated think-not artifact",
    "fixed imperative casing",
    "fixed that-that wording",
    "fixed worldly typo",
    "fixed yours artifact",
    "modernized article before h-word",
    "modernized article before consonant sound",
    "modernized archaic directional unto",
    "modernized alms wording",
    "modernized any-man idiom",
    "modernized anything spelling",
    "modernized bare as bore",
    "modernized be-not clause",
    "modernized be-not imperative",
    "modernized be-not-afraid imperative",
    "modernized be-you imperative",
    "modernized be-you-not imperative",
    "modernized besought",
    "modernized because-that wording",
    "modernized behold",
    "modernized believe-not idiom",
    "modernized believes-not idiom",
    "modernized believed-not wording",
    "modernized brethren",
    "modernized brings-not wording",
    "modernized abides-not wording",
    "modernized can-not spelling",
    "modernized came-to-pass idiom",
    "modernized childbirth bring-forth idiom",
    "modernized coasts as borders",
    "modernized come-to-pass idiom",
    "modernized concupiscence",
    "modernized comes-not wording",
    "modernized conversation as conduct",
    "modernized counsellor spelling",
    "modernized craved",
    "modernized abode",
    "modernized brake as broke",
    "modernized divers",
    "modernized eat-not wording",
    "modernized eats-not wording",
    "modernized enter-not wording",
    "modernized everything spelling",
    "modernized enquired spelling",
    "modernized enquire spelling",
    "modernized enquiring spelling",
    "modernized dwells-not wording",
    "modernized forever spelling",
    "modernized fear-not imperative",
    "modernized fast-not wording",
    "modernized fell-not wording",
    "modernized forasmuch",
    "modernized from-thence idiom",
    "modernized go-you imperative",
    "modernized good-cheer idiom",
    "modernized garment where not contextually technical",
    "modernized held-his-peace idiom",
    "modernized held-their-peace idiom",
    "modernized hereby",
    "modernized hears-not wording",
    "modernized hear-not wording",
    "modernized hearken",
    "modernized he-that relative",
    "modernized henceforth",
    "modernized him-that relative",
    "modernized him-which relative",
    "modernized honour spelling",
    "modernized hold-your-peace idiom",
    "modernized how-says-you idiom",
    "modernized if-Christ-be idiom",
    "modernized if-be wording",
    "modernized if-there-be idiom",
    "modernized in-earth wording",
    "modernized inverted question",
    "modernized in-the-which wording",
    "modernized judge-not idiom",
    "modernized knew-not idiom",
    "modernized know-not idiom",
    "modernized know-you-not question",
    "modernized keeps-not wording",
    "modernized like-to wording",
    "modernized lo",
    "modernized labour spelling",
    "modernized loves-not wording",
    "modernized lived-not wording",
    "modernized meats",
    "modernized mine-own idiom",
    "modernized no-doubt wording",
    "modernized nay",
    "modernized neighbour spelling",
    "modernized nigh",
    "modernized no-man idiom",
    "modernized nowhere wording",
    "modernized offence spelling",
    "modernized overcharged wording",
    "modernized ought-as-anything idiom",
    "modernized palsy",
    "modernized personal which as who",
    "modernized personal relative wording",
    "modernized raiment",
    "modernized reclining-at-meal idiom",
    "modernized receives-not wording",
    "modernized regards-not wording",
    "modernized residual be wording",
    "modernized residual verb-not wording",
    "modernized repented-not wording",
    "modernized perished-not wording",
    "modernized prevailed-not wording",
    "modernized Sabbath-day wording",
    "modernized Sabbath-days wording",
    "modernized savour",
    "modernized says-not wording",
    "modernized see-not wording",
    "modernized sentence casing",
    "modernized sick-of wording",
    "modernized several wording",
    "modernized Saviour spelling",
    "modernized save-in idiom",
    "modernized sins-be-forgiven wording",
    "modernized suffer-as-allow wording",
    "modernized suffer-as-bear-with wording",
    "modernized suffer-as-permit wording",
    "modernized suffered-as-hindered wording",
    "modernized slain",
    "modernized slay",
    "modernized since-then-as wording",
    "modernized sin-not idiom",
    "modernized slew",
    "modernized such-an-one idiom",
    "modernized takes-not wording",
    "modernized take-no-thought idiom",
    "modernized take-thought idiom",
    "modernized them-that relative",
    "modernized them-which relative",
    "modernized there-be idiom",
    "modernized thereby",
    "modernized therefore",
    "modernized thereof",
    "modernized therein",
    "modernized abroad idiom",
    "modernized bade/bidden wording",
    "modernized charger as platter",
    "modernized cleave",
    "modernized exceeding modifier",
    "modernized every where spelling",
    "modernized fair-show idiom",
    "modernized feigned-words wording",
    "modernized fornicator",
    "modernized foes",
    "modernized he-it-is wording",
    "modernized heresies wording",
    "modernized hereof",
    "modernized herein",
    "modernized inverted clause",
    "modernized constrain wording",
    "modernized make-merchandise idiom",
    "modernized meet-as-fitting",
    "modernized mansions wording",
    "modernized minstrels",
    "modernized novice wording",
    "modernized sore modifier",
    "modernized seditions/heresies wording",
    "modernized subtlety",
    "modernized variance",
    "modernized vainglory",
    "modernized wantonness",
    "modernized whereby",
    "modernized whereof",
    "modernized wherein",
    "modernized wherewith",
    "modernized thence",
    "modernized they-that relative",
    "modernized they-which relative",
    "modernized think-not wording",
    "modernized today spelling",
    "modernized verily",
    "modernized was-come perfect",
    "modernized were-come perfect",
    "modernized went-not wording",
    "modernized we-be wording",
    "modernized what-will-you idiom",
    "modernized what-will-you question",
    "modernized will-you-that idiom",
    "modernized whilst",
    "modernized whatsoever",
    "modernized wherefore",
    "modernized where-to wording",
    "modernized whoremonger",
    "modernized whence",
    "modernized whosoever",
    "modernized whoso",
    "modernized worshipped spelling",
    "modernized wrestle-not wording",
    "modernized wrought",
    "modernized worldly-excess wording",
    "modernized waxed-rich idiom",
    "modernized waxed-strong idiom",
    "modernized you-that relative",
    "modernized yours before noun",
    "modernized yea",
    "rendered adelphoi-family wording as brothers",
    "rendered alalos as mute",
    "rendered didaskalos as teacher",
    "rendered eiper as if indeed",
    "rendered eige as if indeed",
    "rendered ean genetai as if it happens",
    "rendered enteuthen as from here",
    "rendered Greek coin term transliterally",
    "rendered general brings-forth as produces",
    "rendered kophos as mute",
    "rendered magoi as Magi",
    "rendered ochlos as crowd",
    "rendered phiale as bowl",
    "standardized NT proper-name English equivalent",
    "standardized Juda as Judah in tribe/land contexts",
    "standardized Jeremiah",
    "standardized Judea spelling",
    "translated sabaoth as hosts",
    "normalized NT kurios as Lord",
    "removed UKJV inline Strong-style lexical marker",
    "removed UKJV plural-expansion artifact",
}

STATUS_WEIGHTS = {
    "needs_focused_tr_review": 10,
    "tr_literal_manual": 8,
    "tr_literal_pass1": 4,
    "ukjv_witness_seed": 2,
}


def normalize_for_compare(text: str) -> str:
    text = text.lower()
    text = STRONGS_MARKER_RE.sub(" ", text)
    text = text.replace("'", "")
    text = NON_COMPARE_WORD_RE.sub(" ", text)
    text = SPACE_RE.sub(" ", text)
    for pattern, new in COMPARISON_REPLACEMENT_PATTERNS:
        text = pattern.sub(new, text)
    text = SPACE_RE.sub(" ", text)
    return text.strip()


NORMALIZED_THEME_TERMS = {
    theme: [
        (normalize_for_compare(term), term)
        for term in terms
        if normalize_for_compare(term)
    ]
    for theme, terms in THEME_TERMS.items()
}


def phrase_present(padded_normalized_text: str, normalized_phrase: str) -> bool:
    if not normalized_phrase:
        return False
    return f" {normalized_phrase} " in padded_normalized_text


def find_theme_hits(text: str) -> tuple[list[str], list[str]]:
    normalized_text = normalize_for_compare(text)
    padded_normalized_text = f" {normalized_text} "
    themes: list[str] = []
    hits: list[str] = []
    for theme, terms in NORMALIZED_THEME_TERMS.items():
        theme_hit = False
        for normalized_term, term in terms:
            if phrase_present(padded_normalized_text, normalized_term):
                theme_hit = True
                hits.append(f"{theme}:{term}")
        if theme_hit:
            themes.append(theme)
    return sorted(set(themes)), sorted(set(hits))


def note_matches(notes: str) -> list[str]:
    return [note for note in NOTE_WEIGHTS if note in notes]


def split_review_notes(notes: str) -> list[str]:
    return [note.strip() for note in notes.split(";") if note.strip()]


def review_pass_sort_key(path: Path) -> tuple[int, str]:
    match = REVIEW_PASS_RE.search(path.name)
    return (int(match.group(1)), path.name) if match else (0, path.name)


def load_latest_review_statuses() -> dict[str, dict[str, str]]:
    statuses: dict[str, dict[str, str]] = {}
    for path in sorted(REVIEW_DIR.glob("nt_review_pass_*.md"), key=review_pass_sort_key):
        ref = ""
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if line.startswith("## "):
                ref = line[3:].strip()
            elif ref and line.startswith("- status:"):
                match = BACKTICK_VALUE_RE.search(line)
                statuses[ref] = {
                    "status": match.group(1) if match else line.split(":", 1)[1].strip(),
                    "pass": path.name,
                }
    return statuses


def score_row(row: dict[str, str], latest_review_statuses: dict[str, dict[str, str]]) -> dict[str, str]:
    tr_text = row.get("draft_translation", "").strip()
    ukjv_text = row.get("ukjv_translation", "").strip()
    status = row.get("review_status", "").strip()
    notes = row.get("review_notes", "").strip()
    latest = latest_review_statuses.get(row.get("ref", ""), {})
    latest_status = latest.get("status", "")
    latest_pass = latest.get("pass", "")
    resolved = latest_status in RESOLVED_REVIEW_STATUSES
    tr_norm = normalize_for_compare(tr_text)
    ukjv_norm = normalize_for_compare(ukjv_text)
    same_normalized = bool(tr_norm and ukjv_norm and tr_norm == ukjv_norm)
    has_text_gap = not tr_text or not ukjv_text
    has_meaningful_difference = has_text_gap or not same_normalized

    themes, keyword_hits = find_theme_hits(f"{tr_text} {ukjv_text}")
    review_notes = split_review_notes(notes)
    matched_notes = note_matches(notes)
    style_only_difference = (
        bool(review_notes)
        and not has_text_gap
        and not same_normalized
        and all(note in STYLE_ONLY_NOTES for note in review_notes)
    )
    requires_review = has_text_gap or (has_meaningful_difference and not style_only_difference)
    score = 0
    reasons: list[str] = []

    if not tr_text:
        score += 12
        reasons.append("missing TR draft")
    if not ukjv_text:
        score += 8
        reasons.append("missing UKJV witness")
    if not same_normalized:
        score += 2
        reasons.append("TR draft differs from UKJV witness")
    elif tr_text and ukjv_text:
        reasons.append("TR draft matches UKJV witness")

    if style_only_difference:
        reasons.append("style-only modernization")

    if requires_review and status in STATUS_WEIGHTS:
        score += STATUS_WEIGHTS[status]
        reasons.append(f"status:{status}")

    if requires_review:
        for note in matched_notes:
            score += NOTE_WEIGHTS[note]
            reasons.append(note)

    if requires_review and keyword_hits:
        score += min(12, len(keyword_hits) * 2)
        reasons.append("theology/literal keyword hit")

    if resolved:
        importance = "none"
        reasons.append(f"resolved:{latest_status}")
    elif not requires_review:
        importance = "none"
    elif status == "needs_focused_tr_review" or score >= 18:
        importance = "high"
    elif score >= 10:
        importance = "medium"
    elif not same_normalized:
        importance = "low"
    else:
        importance = "none"

    if resolved:
        decision = f"resolved in {latest_pass}: {latest_status}"
    elif not requires_review:
        decision = "no meaningful UKJV difference"
    elif status == "needs_focused_tr_review":
        decision = "review Greek; UKJV witness not enough"
    elif matched_notes or keyword_hits:
        decision = "check TR literal choice against Greek, then keep or adjust"
    else:
        decision = "low-priority wording difference"

    return {
        "ref": row.get("ref", ""),
        "book_code": row.get("book_code", ""),
        "book_name": row.get("book_name", ""),
        "chapter": row.get("chapter", ""),
        "verse": row.get("verse", ""),
        "review_status": status,
        "importance": importance,
        "priority_score": str(score),
        "themes": "; ".join(themes),
        "keyword_hits": "; ".join(keyword_hits),
        "same_normalized": "yes" if same_normalized else "no",
        "tr_literal_translation": tr_text,
        "ukjv_translation": ukjv_text,
        "review_notes": notes,
        "latest_review_status": latest_status,
        "latest_review_pass": latest_pass,
        "reasons": "; ".join(dict.fromkeys(reasons)),
        "decision": decision,
    }


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REVIEW_FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in REVIEW_FIELDNAMES})


def priority_sort_key(row: dict[str, str]) -> tuple[int, str, int, int]:
    try:
        score = int(row.get("priority_score", "0"))
    except ValueError:
        score = 0
    try:
        chapter = int(row.get("chapter", "0"))
    except ValueError:
        chapter = 0
    try:
        verse = int(row.get("verse", "0"))
    except ValueError:
        verse = 0
    return (-score, row.get("book_code", ""), chapter, verse)


def write_markdown(path: Path, rows: list[dict[str, str]], *, limit: int, title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    limited = rows[:limit] if limit else rows
    lines = [
        f"# {title}",
        "",
        "Method: `draft_translation` = TR literal draft. `ukjv_translation` = UKJV witness only.",
        "Review target: meaningful or theologically relevant differences, not every style difference.",
        "",
        f"Rows shown: {len(limited)} of {len(rows)}",
        "",
    ]
    for index, row in enumerate(limited, start=1):
        lines.extend(
            [
                f"## {index}. {row['ref']} - {row['importance']} - score {row['priority_score']}",
                "",
                f"- TR draft: {row['tr_literal_translation']}",
                f"- UKJV witness: {row['ukjv_translation']}",
                f"- Themes: {row['themes'] or 'none'}",
                f"- Why: {row['reasons'] or 'none'}",
                f"- Latest review: {row.get('latest_review_status') or 'none'}",
                f"- Decision: {row['decision']}",
                "",
            ]
        )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--review-csv", type=Path, default=DEFAULT_REVIEW_CSV)
    parser.add_argument("--priority-csv", type=Path, default=DEFAULT_PRIORITY_CSV)
    parser.add_argument("--priority-md", type=Path, default=DEFAULT_PRIORITY_MD)
    parser.add_argument("--queue-csv", type=Path, default=DEFAULT_QUEUE_CSV)
    parser.add_argument("--queue-md", type=Path, default=DEFAULT_QUEUE_MD)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    parser.add_argument("--markdown-limit", type=int, default=300)
    args = parser.parse_args()

    source_rows = load_rows(args.source)
    latest_review_statuses = load_latest_review_statuses()
    review_rows = [score_row(row, latest_review_statuses) for row in source_rows]
    priority_rows = [
        row for row in review_rows if row["importance"] in {"high", "medium"}
    ]
    queue_rows = [
        row
        for row in priority_rows
        if row["latest_review_status"] not in RESOLVED_REVIEW_STATUSES
    ]
    priority_rows.sort(key=priority_sort_key)
    queue_rows.sort(key=priority_sort_key)

    write_csv(args.review_csv, review_rows)
    write_csv(args.priority_csv, priority_rows)
    write_csv(args.queue_csv, queue_rows)
    write_markdown(args.priority_md, priority_rows, limit=args.markdown_limit, title="NT TR Literal vs UKJV Priority Review")
    write_markdown(args.queue_md, queue_rows, limit=args.markdown_limit, title="NT TR Literal vs UKJV Review Queue")

    diagnostics = {
        "method": "TR literal draft is primary; UKJV is witness only.",
        "source": str(args.source),
        "rows": len(review_rows),
        "same_normalized": sum(1 for row in review_rows if row["same_normalized"] == "yes"),
        "different_normalized": sum(1 for row in review_rows if row["same_normalized"] == "no"),
        "priority_rows": len(priority_rows),
        "queue_rows": len(queue_rows),
        "status_counts": dict(Counter(row["review_status"] for row in review_rows)),
        "latest_review_status_counts": dict(
            Counter(row["latest_review_status"] or "unreviewed" for row in review_rows)
        ),
        "resolved_review_rows": sum(
            1 for row in review_rows if row["latest_review_status"] in RESOLVED_REVIEW_STATUSES
        ),
        "importance_counts": dict(Counter(row["importance"] for row in review_rows)),
        "theme_counts": dict(
            Counter(
                theme
                for row in review_rows
                for theme in row["themes"].split("; ")
                if theme
            )
        ),
        "outputs": {
            "review_csv": str(args.review_csv),
            "priority_csv": str(args.priority_csv),
            "priority_md": str(args.priority_md),
            "queue_csv": str(args.queue_csv),
            "queue_md": str(args.queue_md),
        },
    }
    args.diagnostics.parent.mkdir(parents=True, exist_ok=True)
    args.diagnostics.write_text(json.dumps(diagnostics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({key: diagnostics[key] for key in ["rows", "priority_rows", "queue_rows"]}, indent=2))


if __name__ == "__main__":
    main()
