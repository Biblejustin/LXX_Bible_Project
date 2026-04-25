#!/usr/bin/env python3
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import ROOT, load_csv, replace_token, run_script, write_csv

SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
PRIVATE_DIR = ROOT / "data" / "research" / "local" / "proper_name_review"
PRIVATE_CSV = PRIVATE_DIR / "proper_name_candidates.csv"
SUMMARY_JSON = PRIVATE_DIR / "last_apply_summary.json"
SUMMARY_MD = PRIVATE_DIR / "last_apply_summary.md"

APPLY_STATUSES = {"revise-main-text", "apply"}


def build_summary(timestamp: str, changed: list[dict[str, str]], dry_run: bool) -> dict[str, object]:
    return {
        "timestamp": timestamp,
        "dry_run": dry_run,
        "decisions_considered": len(changed),
        "forms_changed": [
            {
                "current_form": row["current_form"],
                "preferred_form": row["preferred_form"],
                "rows_changed": row["rows_changed"],
                "refs_sample": row["refs_sample"],
            }
            for row in changed
        ],
        "source": str(SOURCE),
        "private_csv": str(PRIVATE_CSV),
    }


def write_summary_markdown(path: Path, summary: dict[str, object]) -> None:
    lines = [
        "# Proper Name Apply Summary",
        "",
        f"- timestamp: `{summary['timestamp']}`",
        f"- dry run: `{summary['dry_run']}`",
        f"- decisions considered: `{summary['decisions_considered']}`",
        "",
    ]
    for row in summary["forms_changed"]:
        lines.extend(
            [
                f"## {row['current_form']} -> {row['preferred_form']}",
                f"- rows changed: `{row['rows_changed']}`",
                f"- sample refs: {row['refs_sample'] or '[none]'}",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--forms", help='Comma-separated current forms, e.g. "Ierousalem,Roboam"')
    parser.add_argument("--rebuild-watch", action="store_true")
    parser.add_argument("--checkpoint", action="store_true")
    args = parser.parse_args()

    chosen_forms = None
    if args.forms:
        chosen_forms = {part.strip() for part in args.forms.split(",") if part.strip()}

    source_rows = load_csv(SOURCE)
    private_rows = load_csv(PRIVATE_CSV)
    if not private_rows:
        raise SystemExit("No proper-name candidate file found.")

    fieldnames = list(source_rows[0].keys()) if source_rows else []
    private_fieldnames = list(private_rows[0].keys())
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")

    changed_forms: list[dict[str, str]] = []
    for row in private_rows:
        current_form = (row.get("current_form") or "").strip()
        preferred_form = (row.get("preferred_form") or "").strip()
        status = (row.get("status") or "").strip()
        if not current_form or not preferred_form:
            continue
        if status not in APPLY_STATUSES:
            continue
        if chosen_forms and current_form not in chosen_forms:
            continue

        rows_changed = 0
        refs_sample: list[str] = []
        for source_row in source_rows:
            draft = source_row.get("draft_translation", "")
            replaced, count = replace_token(draft, current_form, preferred_form)
            if count:
                rows_changed += 1
                if len(refs_sample) < 8:
                    refs_sample.append(source_row.get("ref", ""))
                if not args.dry_run:
                    source_row["draft_translation"] = replaced

        changed_forms.append(
            {
                "current_form": current_form,
                "preferred_form": preferred_form,
                "rows_changed": str(rows_changed),
                "refs_sample": ", ".join(refs_sample),
            }
        )

        if not args.dry_run and rows_changed > 0:
            row["status"] = "done"
            notes = (row.get("notes") or "").strip()
            apply_note = f"applied {timestamp}"
            row["notes"] = f"{notes}; {apply_note}" if notes else apply_note

    if not args.dry_run and changed_forms:
        write_csv(SOURCE, source_rows, fieldnames)
        write_csv(PRIVATE_CSV, private_rows, private_fieldnames)

    summary = build_summary(timestamp, changed_forms, args.dry_run)
    SUMMARY_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_summary_markdown(SUMMARY_MD, summary)

    if changed_forms and not args.dry_run:
        if args.rebuild_watch:
            run_script("build_proper_name_watch.py")
        if args.checkpoint:
            run_script("run_priority_review_suite.py")

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
