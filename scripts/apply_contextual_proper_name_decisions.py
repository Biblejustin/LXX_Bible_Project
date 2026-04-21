#!/usr/bin/env python3
import argparse
import csv
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
DECISIONS = ROOT / "data" / "research" / "contextual_proper_name_decisions.csv"

APPLY_STATUSES = {"apply", "revise-main-text"}


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def run_script(script_name: str) -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / script_name)], check=True)


def replace_token(text: str, current_form: str, preferred_form: str) -> tuple[str, int]:
    pattern = re.compile(rf"\b{re.escape(current_form)}\b")
    return pattern.subn(preferred_form, text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--rebuild-watch", action="store_true")
    parser.add_argument("--checkpoint", action="store_true")
    args = parser.parse_args()

    source_rows = load_csv(SOURCE)
    decision_rows = load_csv(DECISIONS)
    if not decision_rows:
        raise SystemExit(f"No contextual proper-name decisions found at {DECISIONS}")

    source_fieldnames = list(source_rows[0].keys()) if source_rows else []
    decision_fieldnames = list(decision_rows[0].keys())
    by_ref = {row["ref"]: row for row in source_rows}
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    considered_count = len([row for row in decision_rows if (row.get("status") or "").strip() in APPLY_STATUSES])

    applied: list[dict[str, str]] = []
    missing: list[dict[str, str]] = []

    for row in decision_rows:
        status = (row.get("status") or "").strip()
        if status not in APPLY_STATUSES:
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
            replaced = draft.replace(match_text, replacement_text)
        else:
            replaced, count = replace_token(draft, current_form, preferred_form)
        if count == 0:
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
            row["status"] = "done"
            notes = (row.get("notes") or "").strip()
            apply_note = f"applied {timestamp}"
            row["notes"] = f"{notes}; {apply_note}" if notes else apply_note

    if applied and not args.dry_run:
        write_csv(SOURCE, source_rows, source_fieldnames)
        write_csv(DECISIONS, decision_rows, decision_fieldnames)

    summary = {
        "timestamp": timestamp,
        "dry_run": args.dry_run,
        "decisions_considered": considered_count,
        "applied": applied,
        "missing": missing,
        "source": str(SOURCE),
        "decisions": str(DECISIONS),
    }
    print(json.dumps(summary, indent=2))

    if applied and not args.dry_run:
        if args.rebuild_watch:
            run_script("build_proper_name_watch.py")
        if args.checkpoint:
            run_script("run_priority_review_suite.py")


if __name__ == "__main__":
    main()
