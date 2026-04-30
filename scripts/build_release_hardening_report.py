#!/usr/bin/env python3
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUT = ROOT / "output"
RESEARCH = DATA / "research"
RAW_OT = DATA / "raw" / "lxx_greek" / "ot_full.csv"
TRANSLATION_DECISIONS = RESEARCH / "translation_decisions.csv"
DRAFTED_CSV = OUTPUT / "fresh_vs_brenton_ot_drafted.csv"
REPORT_MD = OUTPUT / "release_hardening_report.md"
REPORT_JSON = OUTPUT / "release_hardening_report.json"
SAMPLES_CSV = OUTPUT / "release_hardening_samples.csv"

WATCH_QUEUE_PATHS = [
    OUTPUT / "fresh_ot_crossref_watch.csv",
    OUTPUT / "fresh_ot_english_witness_watch.csv",
    OUTPUT / "fresh_human_review_mt_watch.csv",
    OUTPUT / "fresh_human_review_nt_watch.csv",
    OUTPUT / "fresh_ot_logos_local_watch.csv",
    OUTPUT / "fresh_ot_proper_name_watch.csv",
    OUTPUT / "fresh_vs_brenton_ot_remap_queue.csv",
    OUTPUT / "fresh_vs_brenton_ot_final_unresolved.csv",
]

REQUIRED_OUTPUTS = [
    OUTPUT / "fresh_translation_ot_full.md",
    OUTPUT / "fresh_translation_ot_full_translation_only.md",
    OUTPUT / "fresh_translation_ot_full_diagnostics.json",
    OUTPUT / "fresh_vs_brenton_ot_drafted.csv",
    OUTPUT / "fresh_vs_brenton_ot_drafted.md",
    OUTPUT / "fresh_vs_brenton_ot_drafted_diagnostics.json",
    OUTPUT / "fresh_vs_brenton_ot_priority_review.csv",
    OUTPUT / "fresh_vs_brenton_ot_priority_review.md",
    OUTPUT / "fresh_human_review_core.csv",
    OUTPUT / "fresh_human_review_phase1.csv",
]

ACTIVE_MARKER_FIELDS = [
    "watch",
    "needs_followup",
    "review_status",
    "latest_review_status",
    "recommendation",
    "consensus_recommendation",
    "nt_english_recommendation",
    "english_witness_recommendation",
    "logos_local_recommendation",
]
ACTIVE_MARKER_VALUES = {"yes", "pending", "needs_logos", "revise", "defer", "needs-review", "needs_review"}

BLOCKING_PATTERNS = {
    "todo_marker": re.compile(r"\b(?:TODO|XXX)\b|\?\?\?|\[TODO", re.IGNORECASE),
    "ellipsis": re.compile(r"\.\.\.|…"),
    "double_period": re.compile(r"\.\s*\."),
    "double_comma": re.compile(r",\s*,"),
    "double_space": re.compile(r" {2,}"),
    "space_before_punctuation": re.compile(r"\s+[,.!?;:]"),
    "replacement_character": re.compile("\ufffd"),
}
REPEATED_WORD_RE = re.compile(r"\b([A-Za-z]+)\s+\1\b", re.IGNORECASE)
REPEATED_WORD_ALLOWLIST = {"that", "her", "thousand"}


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def review_pass_sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"ot_review_pass_(\d+)\.md$", path.name)
    return (int(match.group(1)), path.name) if match else (0, path.name)


def latest_review_statuses() -> dict[str, dict[str, str]]:
    statuses: dict[str, dict[str, str]] = {}
    for path in sorted(RESEARCH.glob("ot_review_pass_*.md"), key=review_pass_sort_key):
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


def row_count_and_duplicates(path: Path) -> dict[str, object]:
    rows = load_csv(path)
    refs = [row.get("ref", "") for row in rows if row.get("ref")]
    duplicates = sorted(ref for ref, count in Counter(refs).items() if count > 1)
    missing_drafts = [
        row.get("ref", "")
        for row in rows
        if "draft_translation" in row and not (row.get("draft_translation") or "").strip()
    ]
    return {
        "path": str(path),
        "rows": len(rows),
        "duplicate_refs": len(duplicates),
        "duplicate_ref_examples": duplicates[:20],
        "missing_draft_translations": len(missing_drafts),
        "missing_draft_examples": missing_drafts[:20],
    }


def book_coverage(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for row in rows:
        book = row.get("book_name", "")
        if not book:
            continue
        counts[book][1] += 1
        if (row.get("draft_translation") or "").strip():
            counts[book][0] += 1
    return [
        {"book_name": book, "drafted": str(done), "total": str(total), "complete": "yes" if done == total else "no"}
        for book, (done, total) in counts.items()
    ]


def watch_queue_counts() -> list[dict[str, str]]:
    rows = []
    for path in WATCH_QUEUE_PATHS:
        rows.append(
            {
                "path": str(path.relative_to(ROOT)),
                "rows": str(len(load_csv(path))),
                "exists": "yes" if path.exists() else "no",
            }
        )
    return rows


def active_marker_hits() -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for path in sorted(OUTPUT.glob("*.csv")):
        rows = load_csv(path)
        if not rows:
            continue
        for field in ACTIVE_MARKER_FIELDS:
            if field not in rows[0]:
                continue
            counts = Counter((row.get(field) or "") for row in rows)
            for value in sorted(ACTIVE_MARKER_VALUES):
                if counts[value]:
                    hits.append(
                        {
                            "path": str(path.relative_to(ROOT)),
                            "field": field,
                            "value": value,
                            "count": str(counts[value]),
                        }
                    )
    return hits


def reviewed_repeated_word_allowlist(rows: list[dict[str, str]]) -> set[tuple[str, str]]:
    allowed: set[tuple[str, str]] = set()
    for row in rows:
        if row.get("status", "").strip().casefold() != "reviewed":
            continue
        rendering = row.get("chosen_rendering", "")
        match = REPEATED_WORD_RE.search(rendering)
        if match:
            allowed.add((row.get("ref", ""), match.group(1).casefold()))
    return allowed


def repeated_word_candidate(text: str, ref: str, reviewed_allowlist: set[tuple[str, str]]) -> str:
    match = REPEATED_WORD_RE.search(text)
    if not match:
        return ""
    word = match.group(1)
    word_key = word.casefold()
    if word_key in REPEATED_WORD_ALLOWLIST or (ref, word_key) in reviewed_allowlist:
        return ""
    return word


def scan_translation_text(
    rows: list[dict[str, str]],
    reviewed_repeated_words: set[tuple[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    blocking_hits: list[dict[str, str]] = []
    repeated_word_candidates: list[dict[str, str]] = []
    for row in rows:
        ref = row.get("ref", "")
        text = row.get("draft_translation", "")
        for name, pattern in BLOCKING_PATTERNS.items():
            match = pattern.search(text)
            if match:
                blocking_hits.append(
                    {
                        "ref": ref,
                        "check": name,
                        "match": match.group(0),
                        "text": text,
                    }
                )
        repeated_word = repeated_word_candidate(text, ref, reviewed_repeated_words)
        if repeated_word:
            repeated_word_candidates.append(
                {
                    "ref": ref,
                    "word": repeated_word,
                    "text": text,
                }
            )
    return blocking_hits, repeated_word_candidates


def deterministic_samples(
    rows: list[dict[str, str]],
    reviewed_repeated_words: set[tuple[str, str]],
) -> list[dict[str, str]]:
    by_book: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_book[row.get("book_name", "")].append(row)

    samples: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for book, book_rows in by_book.items():
        if not book:
            continue
        indexes = [0, len(book_rows) // 2, len(book_rows) - 1]
        for label, index in zip(["first", "middle", "last"], indexes):
            row = book_rows[index]
            key = (book, row["ref"])
            if key in seen:
                continue
            seen.add(key)
            text = row.get("draft_translation", "")
            hit_names = [
                name
                for name, pattern in BLOCKING_PATTERNS.items()
                if pattern.search(text)
            ]
            repeated_word = repeated_word_candidate(text, row["ref"], reviewed_repeated_words)
            samples.append(
                {
                    "book_name": book,
                    "sample_slot": label,
                    "ref": row["ref"],
                    "artifact_checks": ", ".join(hit_names),
                    "repeated_word_candidate": repeated_word,
                    "translation": text,
                }
            )
    return samples


def build_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Release Hardening Report",
        "",
        "Purpose: final automated release-readiness checks for the fresh OT translation output.",
        "",
        "## Summary",
    ]
    for item in report["summary"]:
        lines.append(f"- {item['name']}: `{item['value']}`")

    lines.extend(["", "## Watch Queues"])
    for row in report["watch_queues"]:
        lines.append(f"- `{row['path']}`: `{row['rows']}` rows")

    lines.extend(["", "## Artifact Scan"])
    lines.append(f"- blocking text artifacts: `{len(report['blocking_text_artifacts'])}`")
    lines.append(f"- repeated-word candidates: `{len(report['repeated_word_candidates'])}`")
    if report["repeated_word_candidates"]:
        lines.append("- repeated-word candidates are non-blocking; inspect before changing because Hebrew/Greek-style repetition can be intentional.")
        for row in report["repeated_word_candidates"][:12]:
            lines.append(f"- candidate `{row['word']}` at `{row['ref']}`: {row['text']}")

    lines.extend(["", "## Review Coverage"])
    lines.append(f"- latest reviewed refs: `{report['review_status_total']}`")
    for status, count in report["review_status_counts"].items():
        lines.append(f"- `{status}`: `{count}`")
    lines.append(f"- priority rows still open: `{report['priority_open_count']}`")

    lines.extend(["", "## Sample Audit"])
    lines.append(f"- deterministic per-book samples written to `{SAMPLES_CSV.relative_to(ROOT)}`")
    lines.append(f"- sampled rows: `{report['sample_rows']}`")
    lines.append(f"- sample artifact hits: `{report['sample_artifact_hits']}`")

    lines.extend(["", "## Required Outputs"])
    for row in report["required_outputs"]:
        lines.append(f"- `{row['path']}`: `{row['exists']}`")

    lines.extend(["", "## Verdict"])
    lines.append(report["verdict"])
    return "\n".join(lines) + "\n"


def main() -> None:
    raw_rows = load_csv(RAW_OT)
    drafted_rows = load_csv(DRAFTED_CSV)
    decisions = load_csv(TRANSLATION_DECISIONS)
    statuses = latest_review_statuses()
    priority_rows = load_csv(OUTPUT / "fresh_vs_brenton_ot_priority_review.csv")

    raw_counts = row_count_and_duplicates(RAW_OT)
    drafted_counts = row_count_and_duplicates(DRAFTED_CSV)
    queues = watch_queue_counts()
    active_hits = active_marker_hits()
    reviewed_repeated_words = reviewed_repeated_word_allowlist(decisions)
    blocking_hits, repeated_word_candidates = scan_translation_text(raw_rows, reviewed_repeated_words)
    samples = deterministic_samples(raw_rows, reviewed_repeated_words)
    sample_artifact_hits = sum(1 for row in samples if row["artifact_checks"] or row["repeated_word_candidate"])

    resolved_statuses = {"keep", "revised"}
    priority_open = [
        row["ref"]
        for row in priority_rows
        if statuses.get(row["ref"], {}).get("status") not in resolved_statuses
    ]
    status_counts = Counter(item["status"] for item in statuses.values())
    required_outputs = [
        {"path": str(path.relative_to(ROOT)), "exists": "yes" if path.exists() and path.stat().st_size else "no"}
        for path in REQUIRED_OUTPUTS
    ]

    blocking_conditions = [
        raw_counts["duplicate_refs"],
        raw_counts["missing_draft_translations"],
        drafted_counts["duplicate_refs"],
        sum(int(row["rows"]) for row in queues),
        len(active_hits),
        len(blocking_hits),
        len(priority_open),
        sum(1 for row in required_outputs if row["exists"] != "yes"),
    ]
    verdict = (
        "PASS: release-hardening checks found no blocking issues."
        if not any(blocking_conditions)
        else "BLOCKED: release-hardening checks found one or more blocking issues."
    )

    report = {
        "summary": [
            {"name": "raw OT rows", "value": str(raw_counts["rows"])},
            {"name": "drafted compare rows", "value": str(drafted_counts["rows"])},
            {"name": "raw duplicate refs", "value": str(raw_counts["duplicate_refs"])},
            {"name": "drafted duplicate refs", "value": str(drafted_counts["duplicate_refs"])},
            {"name": "missing draft translations", "value": str(raw_counts["missing_draft_translations"])},
            {"name": "watch/remap/final-unresolved rows", "value": str(sum(int(row["rows"]) for row in queues))},
            {"name": "active generated-output markers", "value": str(len(active_hits))},
            {"name": "blocking text artifacts", "value": str(len(blocking_hits))},
            {"name": "priority rows open", "value": str(len(priority_open))},
        ],
        "raw_counts": raw_counts,
        "drafted_counts": drafted_counts,
        "book_coverage": book_coverage(raw_rows),
        "watch_queues": queues,
        "active_marker_hits": active_hits,
        "blocking_text_artifacts": blocking_hits,
        "repeated_word_candidates": repeated_word_candidates,
        "review_status_total": len(statuses),
        "review_status_counts": dict(sorted(status_counts.items())),
        "priority_open_count": len(priority_open),
        "priority_open_examples": priority_open[:20],
        "sample_rows": len(samples),
        "sample_artifact_hits": sample_artifact_hits,
        "required_outputs": required_outputs,
        "verdict": verdict,
    }

    write_csv(
        SAMPLES_CSV,
        samples,
        ["book_name", "sample_slot", "ref", "artifact_checks", "repeated_word_candidate", "translation"],
    )
    REPORT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    REPORT_MD.write_text(build_markdown(report), encoding="utf-8")
    print(json.dumps({"report": str(REPORT_MD), "json": str(REPORT_JSON), "samples": str(SAMPLES_CSV), "verdict": verdict}, indent=2))


if __name__ == "__main__":
    main()
