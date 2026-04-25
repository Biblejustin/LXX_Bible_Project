#!/usr/bin/env python3
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline_common import ROOT, count_token, load_csv, replace_token, run_script, sample_rows, write_csv

SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
DECISIONS = ROOT / "data" / "research" / "contextual_proper_name_decisions.csv"

ENFORCE_STATUSES = {"apply", "revise-main-text", "done"}
STATUS_MARK_DONE = {"apply", "revise-main-text"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--rebuild-watch", action="store_true")
    parser.add_argument("--checkpoint", action="store_true")
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Print counts and samples instead of full decision lists.",
    )
    args = parser.parse_args()

    source_rows = load_csv(SOURCE)
    decision_rows = load_csv(DECISIONS)
    if not decision_rows:
        raise SystemExit(f"No contextual proper-name decisions found at {DECISIONS}")

    source_fieldnames = list(source_rows[0].keys()) if source_rows else []
    decision_fieldnames = list(decision_rows[0].keys())
    by_ref = {row["ref"]: row for row in source_rows}
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    considered_count = len(
        [row for row in decision_rows if (row.get("status") or "").strip().lower() in ENFORCE_STATUSES]
    )

    applied: list[dict[str, str]] = []
    already_applied: list[dict[str, str]] = []
    missing: list[dict[str, str]] = []
    decision_rows_changed = False

    for row in decision_rows:
        status = (row.get("status") or "").strip().lower()
        if status not in ENFORCE_STATUSES:
            continue
        ref = (row.get("ref") or "").strip()
        current_form = (row.get("current_form") or "").strip()
        preferred_form = (row.get("preferred_form") or "").strip()
        match_text = (row.get("match_text") or "").strip()
        replacement_text = (row.get("replacement_text") or "").strip()
        source_row = by_ref.get(ref)
        if not source_row or not current_form or not preferred_form:
            missing.append({"ref": ref, "current_form": current_form, "reason": "missing source row or form"})
            continue

        draft = source_row.get("draft_translation", "")
        if match_text and replacement_text:
            count = draft.count(match_text)
            if count:
                replaced = draft.replace(match_text, replacement_text)
            elif replacement_text in draft or count_token(draft, preferred_form):
                already_applied.append(
                    {"ref": ref, "current_form": current_form, "preferred_form": preferred_form}
                )
                if status in STATUS_MARK_DONE and not args.dry_run:
                    row["status"] = "done"
                    notes = (row.get("notes") or "").strip()
                    verify_note = f"verified {timestamp}"
                    row["notes"] = f"{notes}; {verify_note}" if notes else verify_note
                    decision_rows_changed = True
                continue
            else:
                replaced = draft
        else:
            replaced, count = replace_token(draft, current_form, preferred_form)
        if count == 0:
            if count_token(draft, preferred_form):
                already_applied.append(
                    {"ref": ref, "current_form": current_form, "preferred_form": preferred_form}
                )
                if status in STATUS_MARK_DONE and not args.dry_run:
                    row["status"] = "done"
                    notes = (row.get("notes") or "").strip()
                    verify_note = f"verified {timestamp}"
                    row["notes"] = f"{notes}; {verify_note}" if notes else verify_note
                    decision_rows_changed = True
                continue
            missing.append({"ref": ref, "current_form": current_form, "reason": "form not found"})
            continue
        applied.append(
            {
                "ref": ref,
                "current_form": current_form,
                "preferred_form": preferred_form,
                "count": str(count),
            }
        )
        if not args.dry_run:
            source_row["draft_translation"] = replaced
            if status in STATUS_MARK_DONE:
                row["status"] = "done"
                notes = (row.get("notes") or "").strip()
                apply_note = f"applied {timestamp}"
                row["notes"] = f"{notes}; {apply_note}" if notes else apply_note
                decision_rows_changed = True

    if applied and not args.dry_run:
        write_csv(SOURCE, source_rows, source_fieldnames)
    if decision_rows_changed and not args.dry_run:
        write_csv(DECISIONS, decision_rows, decision_fieldnames)

    summary = {
        "timestamp": timestamp,
        "dry_run": args.dry_run,
        "decisions_considered": considered_count,
        "applied_count": len(applied),
        "already_applied_count": len(already_applied),
        "missing_count": len(missing),
        "applied": applied,
        "already_applied": already_applied,
        "missing": missing,
        "source": str(SOURCE),
        "decisions": str(DECISIONS),
    }
    if args.summary_only:
        summary["applied"] = sample_rows(applied, 10)
        summary["already_applied"] = sample_rows(already_applied, 10)
        summary["missing"] = sample_rows(missing, 20)
    print(json.dumps(summary, indent=2))

    if applied and not args.dry_run:
        if args.rebuild_watch:
            run_script("build_proper_name_watch.py")
        if args.checkpoint:
            run_script("run_priority_review_suite.py")


if __name__ == "__main__":
    main()
