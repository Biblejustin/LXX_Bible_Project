#!/usr/bin/env python3
"""Append review CSV rows safely from tab-separated stdin.

Use this for manual review rows instead of pasting comma-separated rows into a
CSV file. Tabs separate fields; commas inside prose are written with proper CSV
quoting by Python's csv module.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from fresh_bible.csv_shape import assert_csv_shapes


ROOT = Path(__file__).resolve().parents[1]


def project_path(path: Path) -> Path:
    return path if path.is_absolute() else ROOT / path


def read_header(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        try:
            return next(csv.reader(handle))
        except StopIteration as error:
            raise ValueError(f"{path} is empty; expected a header row") from error


def read_tsv_rows() -> list[list[str]]:
    rows: list[list[str]] = []
    for row in csv.reader(sys.stdin, delimiter="\t"):
        if not row or all(not cell.strip() for cell in row):
            continue
        rows.append([cell.strip() for cell in row])
    return rows


def validate_rows(path: Path, header: list[str], rows: list[list[str]]) -> None:
    expected_width = len(header)
    bad_rows = [(index, row) for index, row in enumerate(rows, start=1) if len(row) != expected_width]
    if not bad_rows:
        return

    details = []
    for index, row in bad_rows[:5]:
        sample = " | ".join(row[: min(len(row), 8)])
        if len(row) > 8:
            sample += " | ..."
        details.append(f"stdin row {index}: {len(row)} columns; expected {expected_width}. Row: {sample}")
    if len(bad_rows) > 5:
        details.append(f"... {len(bad_rows) - 5} more bad stdin rows")
    raise ValueError(
        f"Refusing to append malformed rows to {path}.\n"
        f"Use tabs between fields. Commas inside fields are safe.\n"
        + "\n".join(details)
    )


def append_rows(path: Path, rows: list[list[str]]) -> None:
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerows(rows)
    assert_csv_shapes([path])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="CSV file to append to. Relative paths resolve from repo root.")
    parser.add_argument("--dry-run", action="store_true", help="Validate stdin rows without appending.")
    args = parser.parse_args()

    path = project_path(args.path)
    header = read_header(path)
    rows = read_tsv_rows()
    validate_rows(path, header, rows)

    if args.dry_run:
        print({"append_review_csv_rows_dry_run_ok": len(rows), "path": str(path)})
        return 0

    append_rows(path, rows)
    print({"appended_rows": len(rows), "path": str(path)})
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
