#!/usr/bin/env python3
import argparse
import csv
import json
import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
MATRIX = ROOT / "data" / "research" / "local" / "witness_review" / "ot_witness_matrix.csv"
SUMMARY_JSON = ROOT / "data" / "research" / "local" / "witness_review" / "last_apply_summary.json"
SUMMARY_MD = ROOT / "data" / "research" / "local" / "witness_review" / "last_apply_summary.md"
SCRIPTS = ROOT / "scripts"

EXTRA_MATRIX_FIELDS = [
    "apply_status",
    "applied_at",
]


def load_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def parse_refs(raw: str | None) -> set[str]:
    if not raw:
        return set()
    return {part.strip() for part in raw.split(",") if part.strip()}


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, cwd=ROOT)


def build_scope_commands(changed_refs: list[str], min_importance: str) -> list[list[str]]:
    groups: dict[str, list[int]] = defaultdict(list)
    for ref in changed_refs:
        book, chapter = ref.rsplit(" ", 1)
        groups[book].append(int(chapter.split(":")[0]))

    commands = []
    for book in sorted(groups):
        chapters = sorted(set(groups[book]))
        commands.append(
            [
                sys.executable,
                str(SCRIPTS / "run_translation_review.py"),
                "--book",
                book,
                "--chapter-start",
                str(min(chapters)),
                "--chapter-end",
                str(max(chapters)),
                "--min-importance",
                min_importance,
            ]
        )
    return commands


def write_summary(summary: dict) -> None:
    SUMMARY_JSON.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    lines = [
        "# Witness Apply Summary",
        "",
        f"- timestamp: `{summary['timestamp']}`",
        f"- source_rows_changed: `{summary['source_rows_changed']}`",
        f"- matrix_rows_with_decisions: `{summary['matrix_rows_with_decisions']}`",
        f"- matrix_rows_applied: `{summary['matrix_rows_applied']}`",
        f"- matrix_rows_already_matching: `{summary['matrix_rows_already_matching']}`",
        f"- refs_in_run: `{len(summary['refs'])}`",
        "",
        "## Refs",
    ]
    for ref in summary["refs"]:
        lines.append(f"- `{ref}`")
    if summary["scope_commands"]:
        lines += [
            "",
            "## Suggested Scoped Review",
        ]
        for cmd in summary["scope_commands"]:
            lines.append(f"- `{cmd}`")
    SUMMARY_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matrix", default=str(MATRIX))
    parser.add_argument("--source", default=str(SOURCE))
    parser.add_argument("--refs", help="Comma-separated refs to limit apply scope")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--rebuild-scoped", action="store_true")
    parser.add_argument("--checkpoint", action="store_true")
    parser.add_argument("--min-importance", choices=["none", "low", "medium", "high"], default="medium")
    args = parser.parse_args()

    matrix_path = Path(args.matrix)
    source_path = Path(args.source)
    selected_refs = parse_refs(args.refs)
    timestamp = datetime.now().astimezone().replace(microsecond=0).isoformat()

    matrix_rows, matrix_fields = load_csv(matrix_path)
    source_rows, source_fields = load_csv(source_path)
    source_by_ref = {row["ref"]: row for row in source_rows}

    for field in EXTRA_MATRIX_FIELDS:
        if field not in matrix_fields:
            matrix_fields.append(field)
    for row in matrix_rows:
        for field in EXTRA_MATRIX_FIELDS:
            row.setdefault(field, "")

    changed_refs: list[str] = []
    matrix_rows_with_decisions = 0
    matrix_rows_applied = 0
    matrix_rows_already_matching = 0

    for row in matrix_rows:
        ref = row["ref"].strip()
        final_decision = row.get("final_decision", "").strip()
        if selected_refs and ref not in selected_refs:
            continue
        if not final_decision:
            continue

        matrix_rows_with_decisions += 1
        source_row = source_by_ref.get(ref)
        if not source_row:
            row["apply_status"] = "missing-source-ref"
            row["applied_at"] = timestamp
            continue

        current = source_row.get("draft_translation", "").strip()
        if current == final_decision:
            row["apply_status"] = "already-matches"
            row["applied_at"] = timestamp
            matrix_rows_already_matching += 1
            changed_refs.append(ref)
            continue

        row["apply_status"] = "applied" if not args.dry_run else "dry-run"
        row["applied_at"] = timestamp
        matrix_rows_applied += 1
        changed_refs.append(ref)
        if not args.dry_run:
            source_row["draft_translation"] = final_decision

    changed_refs = sorted(set(changed_refs))
    scope_commands = [
        " ".join(cmd)
        for cmd in build_scope_commands(changed_refs, args.min_importance)
    ]

    if not args.dry_run:
        write_csv(source_path, source_rows, source_fields)
        write_csv(matrix_path, matrix_rows, matrix_fields)

    summary = {
        "timestamp": timestamp,
        "dry_run": args.dry_run,
        "matrix_rows_with_decisions": matrix_rows_with_decisions,
        "matrix_rows_applied": matrix_rows_applied,
        "matrix_rows_already_matching": matrix_rows_already_matching,
        "source_rows_changed": matrix_rows_applied,
        "refs": changed_refs,
        "scope_commands": scope_commands,
        "performed_scoped_rebuild": False,
        "performed_checkpoint": False,
    }
    if matrix_rows_with_decisions == 0:
        summary["warning"] = "No rows have final_decision yet."
    elif matrix_rows_applied == 0:
        summary["warning"] = "No source rows changed."
    write_summary(summary)

    if not args.dry_run and args.rebuild_scoped and matrix_rows_applied > 0:
        for cmd in build_scope_commands(changed_refs, args.min_importance):
            run(cmd)
        summary["performed_scoped_rebuild"] = True

    if not args.dry_run and args.checkpoint and matrix_rows_applied > 0:
        run([sys.executable, str(SCRIPTS / "run_book_checkpoint.py")])
        summary["performed_checkpoint"] = True

    write_summary(summary)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
