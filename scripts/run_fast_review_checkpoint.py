#!/usr/bin/env python3
"""Fast scoped validation for translation-review chunks.

This is the day-to-day checkpoint. It intentionally avoids aggregate Markdown
and DOCX rebuilds; run `make checkpoint-ot` only at batch/release boundaries.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

from fresh_bible.csv_shape import assert_csv_shapes
import review_chunk_helper as helper


ROOT = Path(__file__).resolve().parents[1]
DECISIONS = ROOT / "data/research/translation_decisions.csv"


def csv_shape_check(paths: list[Path]) -> None:
    try:
        assert_csv_shapes(paths)
    except ValueError as error:
        raise SystemExit(f"CSV shape failure:\n{error}") from error


def run_pytest(testament: str) -> None:
    tests = [
        "tests/test_smoke.py::test_reviewed_phrase_guards_match_source",
        "tests/test_smoke.py::test_known_release_blocker_fixes_stay_fixed",
    ]
    if testament == "ot":
        tests.extend(
            [
                "tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes",
                "tests/test_smoke.py::test_common_lord_article_formulas_are_normalized",
            ]
        )
    subprocess.run([sys.executable, "-m", "pytest", *tests, "-q"], cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--testament", choices=["ot", "nt"], default="ot")
    parser.add_argument("--refs", required=True, help="Comma-separated refs or same-chapter ranges.")
    parser.add_argument("--sync-footnotes", action="store_true")
    parser.add_argument("--add-full-verse-guards", action="store_true")
    parser.add_argument("--guard-note", default="review chunk")
    parser.add_argument("--pass-id", type=int)
    parser.add_argument("--scope")
    parser.add_argument("--changes", default="Reviewed article and readability cleanup.")
    parser.add_argument("--skip-pytest", action="store_true")
    args = parser.parse_args()

    started = time.monotonic()
    refs = set(helper.expand_refs(args.refs))
    source_by_ref = helper.source_rows(args.testament)
    missing_refs = sorted(ref for ref in refs if ref not in source_by_ref)
    if missing_refs:
        raise SystemExit(f"Unknown refs: {', '.join(missing_refs)}")

    if args.sync_footnotes:
        print({"footnotes_synced": helper.sync_translation_footnotes(refs, source_by_ref)})
    if args.add_full_verse_guards:
        print({"guards_upserted": helper.upsert_full_verse_guards(args.testament, refs, source_by_ref, args.guard_note)})
    if args.pass_id is not None:
        scope = args.scope or args.refs
        print({"pass_file": str(helper.create_pass_file(args.testament, args.pass_id, scope, args.changes))})

    source_path = helper.OT_SOURCE if args.testament == "ot" else helper.NT_SOURCE
    csv_shape_check([source_path, helper.FOOTNOTES, DECISIONS, helper.GUARDS])
    print({"csv_shape_ok": True})

    helper.check_sync(refs, source_by_ref)
    print({"sync_ok": len(refs)})

    if not args.skip_pytest:
        run_pytest(args.testament)
        print({"focused_pytest_ok": True})

    elapsed = time.monotonic() - started
    if args.pass_id is not None:
        lines = [
            "Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.",
            f"`python scripts/run_fast_review_checkpoint.py --testament {args.testament} --refs '{args.refs}'` passed.",
        ]
        if not args.skip_pytest:
            lines.append("Focused smoke tests passed.")
        lines.append("Full aggregate/DOCX checkpoint intentionally deferred for batch boundary.")
        print({"validated_pass_file": str(helper.mark_pass_validated(args.testament, args.pass_id, lines))})

    print({"fast_checkpoint_seconds": round(elapsed, 2)})


if __name__ == "__main__":
    main()
