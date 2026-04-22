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

STATUS_WEIGHTS = {
    "needs_focused_tr_review": 10,
    "tr_literal_manual": 8,
    "tr_literal_pass1": 4,
    "ukjv_witness_seed": 2,
}


def normalize_for_compare(text: str) -> str:
    text = text.lower()
    text = text.replace("'", "")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def phrase_present(normalized_text: str, phrase: str) -> bool:
    normalized_phrase = normalize_for_compare(phrase)
    if not normalized_phrase:
        return False
    return re.search(rf"\b{re.escape(normalized_phrase)}\b", normalized_text) is not None


def find_theme_hits(text: str) -> tuple[list[str], list[str]]:
    normalized_text = normalize_for_compare(text)
    themes: list[str] = []
    hits: list[str] = []
    for theme, terms in THEME_TERMS.items():
        theme_hit = False
        for term in terms:
            if phrase_present(normalized_text, term):
                theme_hit = True
                hits.append(f"{theme}:{term}")
        if theme_hit:
            themes.append(theme)
    return sorted(set(themes)), sorted(set(hits))


def note_matches(notes: str) -> list[str]:
    return [note for note in NOTE_WEIGHTS if note in notes]


def review_pass_sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"nt_review_pass_(\d+)\.md$", path.name)
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
                match = re.search(r"`([^`]+)`", line)
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

    themes, keyword_hits = find_theme_hits(f"{tr_text} {ukjv_text}")
    matched_notes = note_matches(notes)
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

    if status in STATUS_WEIGHTS:
        score += STATUS_WEIGHTS[status]
        reasons.append(f"status:{status}")

    for note in matched_notes:
        score += NOTE_WEIGHTS[note]
        reasons.append(note)

    if keyword_hits:
        score += min(12, len(keyword_hits) * 2)
        reasons.append("theology/literal keyword hit")

    requires_review = (
        not same_normalized
        or status == "needs_focused_tr_review"
        or not tr_text
        or not ukjv_text
    )

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
        if (
            row["latest_review_status"] not in RESOLVED_REVIEW_STATUSES
            and (row["importance"] == "high" or row["review_status"] == "needs_focused_tr_review")
        )
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
