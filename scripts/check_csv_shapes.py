#!/usr/bin/env python3
"""Validate CSV row widths for source and review tables."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from fresh_bible.csv_shape import assert_csv_shapes


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PATHS = [
    ROOT / "data/raw/lxx_greek/ot_full.csv",
    ROOT / "data/raw/lxx_deuterocanon/deuterocanon_full.csv",
    ROOT / "data/raw/1_enoch/1_enoch_charles_witness.csv",
    ROOT / "data/raw/tr_greek/nt_full.csv",
    ROOT / "data/research/1_enoch_charles_1912_greek_ocr_audit.csv",
    ROOT / "data/research/1_enoch_charles_1912_greek_ocr_priority.csv",
    ROOT / "data/research/1_enoch_greek_fragment_ref_review.csv",
    ROOT / "data/research/1_enoch_witness_comparison_queue.csv",
    ROOT / "data/research/translation_footnotes.csv",
    ROOT / "data/research/translation_decisions.csv",
    ROOT / "data/research/reviewed_phrase_guards.csv",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="CSV paths to validate. Defaults to project review tables.")
    args = parser.parse_args()

    paths = [path if path.is_absolute() else ROOT / path for path in args.paths] if args.paths else DEFAULT_PATHS
    try:
        assert_csv_shapes(paths)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    print({"csv_shape_ok": len(paths)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
