#!/usr/bin/env python3
"""Audit rendered cross-reference targets against current OT/NT source rows."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "output" / "working" / "crossref_target_audit" / "broken_crossref_targets.csv"
DEFAULT_DIAGNOSTICS = ROOT / "output" / "working" / "crossref_target_audit" / "diagnostics.json"
DEFAULT_MAX_PRINT_REFS = 4

sys.path.insert(0, str(ROOT / "scripts"))
import build_fresh_logos_bible as builder  # noqa: E402
import build_print_proof_bible as print_builder  # noqa: E402


def load_combined_verses() -> list[builder.Verse]:
    return builder.load_verses(builder.DEFAULT_SOURCE) + builder.load_verses(builder.DEFAULT_NT_SOURCE)


def source_ref_set(verses: list[builder.Verse]) -> set[str]:
    return {builder.normalize_code_ref_code(builder.source_code_ref(verse)) for verse in verses}


def source_chapter_maxima(verses: list[builder.Verse]) -> dict[str, dict[int, int]]:
    maxima: dict[str, dict[int, int]] = {}
    for verse in verses:
        code, chapter, verse_num = builder.parse_code_ref(
            builder.normalize_code_ref_code(builder.source_code_ref(verse))
        ) or ("", 0, 0)
        if not code:
            continue
        book = builder.validation_code(code)
        maxima.setdefault(book, {})[chapter] = max(maxima.setdefault(book, {}).get(chapter, 0), verse_num)
    return maxima


def endpoint_code_ref(book_label: str, chapter: str, verse: str) -> str | None:
    return builder.code_ref_for_crossref_endpoint(book_label, chapter, verse)


def range_endpoints(ref: str) -> tuple[str, str] | None:
    normalized = builder.normalize_space(ref.strip())
    match = builder.CROSSREF_FULL_RANGE_RE.match(normalized)
    if match:
        start_book, start_chapter, start_verse, end_book, end_chapter, end_verse = match.groups()
        start_ref = endpoint_code_ref(start_book, start_chapter, start_verse)
        end_ref = endpoint_code_ref(end_book, end_chapter, end_verse)
        return (start_ref, end_ref) if start_ref and end_ref else None
    match = builder.CROSSREF_CHAPTER_RANGE_RE.match(normalized)
    if match:
        book, start_chapter, start_verse, end_chapter, end_verse = match.groups()
        start_ref = endpoint_code_ref(book, start_chapter, start_verse)
        end_ref = endpoint_code_ref(book, end_chapter, end_verse)
        return (start_ref, end_ref) if start_ref and end_ref else None
    match = builder.CROSSREF_SAME_CHAPTER_RANGE_RE.match(normalized)
    if match:
        book, chapter, start_verse, end_verse = match.groups()
        start_ref = endpoint_code_ref(book, chapter, start_verse)
        end_ref = endpoint_code_ref(book, chapter, end_verse)
        return (start_ref, end_ref) if start_ref and end_ref else None
    parsed = builder.parse_cross_reference(normalized)
    if not parsed:
        return None
    code, _label, chapter, verse, verse_end, _raw = parsed
    if verse is None:
        return None
    start_ref = f"{builder.validation_code(code)} {chapter}:{verse}"
    end_ref = f"{builder.validation_code(code)} {chapter}:{verse_end or verse}"
    return start_ref, end_ref


def expected_refs_between(
    start_ref: str,
    end_ref: str,
    chapter_maxima: dict[str, dict[int, int]],
) -> tuple[list[str], str]:
    start = builder.parse_code_ref(start_ref)
    end = builder.parse_code_ref(end_ref)
    if not start or not end:
        return [], "unparseable_endpoint"

    start_code, start_chapter, start_verse = start
    end_code, end_chapter, end_verse = end
    start_code = builder.validation_code(start_code)
    end_code = builder.validation_code(end_code)
    if start_code != end_code:
        return [start_ref, end_ref], "cross_book_range_not_expanded"

    chapters = chapter_maxima.get(start_code, {})
    if not chapters:
        return [], "unknown_book"
    if (end_chapter, end_verse) < (start_chapter, start_verse):
        return [], "range_reversed"

    refs: list[str] = []
    for chapter in range(start_chapter, end_chapter + 1):
        max_verse = chapters.get(chapter, 0)
        if max_verse <= 0:
            refs.append(f"{start_code} {chapter}:1")
            continue
        first_verse = start_verse if chapter == start_chapter else 1
        last_verse = end_verse if chapter == end_chapter else max_verse
        for verse in range(first_verse, last_verse + 1):
            refs.append(f"{start_code} {chapter}:{verse}")
    return refs, ""


def audit_target(
    ref: str,
    *,
    valid_refs: set[str],
    chapter_maxima: dict[str, dict[int, int]],
) -> tuple[list[dict[str, str]], Counter[str]]:
    counts: Counter[str] = Counter()
    endpoints = range_endpoints(ref)
    if not endpoints:
        return [{"issue": "unparseable_target", "normalized_ref": "", "missing_ref": "", "detail": ""}], counts

    start_ref, end_ref = endpoints
    normalized_start = builder.normalize_code_ref_code(start_ref)
    normalized_end = builder.normalize_code_ref_code(end_ref)
    issues: list[dict[str, str]] = []
    if normalized_start not in valid_refs:
        issues.append(
            {
                "issue": "missing_start_ref",
                "normalized_ref": normalized_start,
                "missing_ref": normalized_start,
                "detail": "",
            }
        )
    if normalized_end not in valid_refs:
        issues.append(
            {
                "issue": "missing_end_ref",
                "normalized_ref": normalized_end,
                "missing_ref": normalized_end,
                "detail": "",
            }
        )
    if issues:
        return issues, counts

    expected_refs, range_issue = expected_refs_between(normalized_start, normalized_end, chapter_maxima)
    if range_issue and range_issue != "cross_book_range_not_expanded":
        return [
            {
                "issue": range_issue,
                "normalized_ref": f"{normalized_start}-{normalized_end}",
                "missing_ref": "",
                "detail": "",
            }
        ], counts
    missing = [item for item in expected_refs if item not in valid_refs]
    if missing:
        # LXX numbering can skip verse numbers inside otherwise valid ranges.
        # A cross-reference range remains usable when both endpoints resolve.
        counts["internal_gap_ranges_accepted"] += 1
        counts["internal_gap_refs_skipped"] += len(missing)
    return [], counts


def audit_crossrefs(
    profile: str,
    crossrefs: dict[str, list[builder.CrossReferenceNote]],
    *,
    valid_refs: set[str],
    chapter_maxima: dict[str, dict[int, int]],
) -> tuple[list[dict[str, str]], Counter[str]]:
    rows: list[dict[str, str]] = []
    counts: Counter[str] = Counter()
    for source_ref, notes in sorted(crossrefs.items()):
        for note in notes:
            for target_ref in note.refs:
                counts["targets_checked"] += 1
                issues, target_counts = audit_target(
                    target_ref,
                    valid_refs=valid_refs,
                    chapter_maxima=chapter_maxima,
                )
                counts.update(target_counts)
                if not issues:
                    continue
                counts["broken_targets"] += 1
                for issue in issues:
                    rows.append(
                        {
                            "profile": profile,
                            "source_ref": source_ref,
                            "note_source": note.source,
                            "target_ref": target_ref,
                            **issue,
                        }
                    )
    return rows, counts


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "profile",
        "source_ref",
        "note_source",
        "target_ref",
        "issue",
        "normalized_ref",
        "missing_ref",
        "detail",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--diagnostics", type=Path, default=DEFAULT_DIAGNOSTICS)
    parser.add_argument("--max-print-refs", type=int, default=DEFAULT_MAX_PRINT_REFS)
    args = parser.parse_args()

    verses = load_combined_verses()
    valid_refs = source_ref_set(verses)
    chapter_maxima = source_chapter_maxima(verses)

    logos_crossrefs, logos_diag = builder.build_crossrefs_for_verses(verses, "combined", enabled=True)
    print_crossrefs, print_diag = print_builder.openbible_print_crossrefs(
        verses,
        max_refs_per_note=args.max_print_refs,
    )

    broken_rows: list[dict[str, str]] = []
    diagnostics: dict[str, object] = {
        "source_refs": len(valid_refs),
        "profiles": {},
    }
    for profile, crossrefs, diag in (
        ("logos_combined", logos_crossrefs, logos_diag),
        ("print_openbible_top_n", print_crossrefs, print_diag),
    ):
        rows, counts = audit_crossrefs(
            profile,
            crossrefs,
            valid_refs=valid_refs,
            chapter_maxima=chapter_maxima,
        )
        broken_rows.extend(rows)
        diagnostics["profiles"][profile] = {
            "verses_with_crossrefs": len(crossrefs),
            "targets_checked": counts["targets_checked"],
            "broken_targets": counts["broken_targets"],
            "internal_gap_ranges_accepted": counts["internal_gap_ranges_accepted"],
            "internal_gap_refs_skipped": counts["internal_gap_refs_skipped"],
            "source_diagnostics": diag,
        }

    diagnostics["broken_rows"] = len(broken_rows)
    diagnostics["output_csv"] = str(args.output)
    write_csv(args.output, broken_rows)
    args.diagnostics.parent.mkdir(parents=True, exist_ok=True)
    args.diagnostics.write_text(json.dumps(diagnostics, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
