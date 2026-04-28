#!/usr/bin/env python3
"""Update one CSV column safely from two-column TSV stdin.

Input rows must be:

    key<TAB>new value

Commas inside values are safe. The script rewrites only matching physical rows
and preserves all other rows byte-for-byte. Updated rows use LF so git's
whitespace check does not treat CRLF as trailing whitespace.
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
from pathlib import Path

from fresh_bible.csv_shape import assert_csv_shapes


ROOT = Path(__file__).resolve().parents[1]


def project_path(path: Path) -> Path:
    return path if path.is_absolute() else ROOT / path


def read_updates() -> dict[str, str]:
    updates: dict[str, str] = {}
    for index, row in enumerate(csv.reader(sys.stdin, delimiter="\t"), start=1):
        if not row or all(not cell.strip() for cell in row):
            continue
        if len(row) != 2:
            raise ValueError(f"stdin row {index}: expected 2 tab-separated columns, got {len(row)}")
        key, value = row
        key = key.strip()
        if not key:
            raise ValueError(f"stdin row {index}: key column is blank")
        updates[key] = value.strip()
    return updates


def strip_newline(line: str) -> tuple[str, str]:
    if line.endswith("\r\n"):
        return line[:-2], "\r\n"
    if line.endswith("\n"):
        return line[:-1], "\n"
    return line, ""


def render_row(row: list[str], lineterminator: str) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator=lineterminator)
    writer.writerow(row)
    return buffer.getvalue()


def update_file(path: Path, key_column: str, target_column: str, updates: dict[str, str]) -> int:
    lines = path.read_bytes().decode("utf-8").splitlines(keepends=True)
    if not lines:
        raise ValueError(f"{path} is empty")

    header_text, header_newline = strip_newline(lines[0])
    header = next(csv.reader([header_text]))
    try:
        key_index = header.index(key_column)
        target_index = header.index(target_column)
    except ValueError as error:
        raise ValueError(f"{path} missing required column: {error}") from error

    changed = 0
    seen: set[str] = set()
    out = [lines[0]]
    default_newline = header_newline or "\n"

    for line in lines[1:]:
        row_text, newline = strip_newline(line)
        row = next(csv.reader([row_text]))
        if len(row) == len(header) and row[key_index] in updates:
            key = row[key_index]
            seen.add(key)
            new_value = updates[key]
            if row[target_index] != new_value:
                row[target_index] = new_value
                out.append(render_row(row, "\n"))
                changed += 1
                continue
        out.append(line)

    missing = sorted(set(updates) - seen)
    if missing:
        preview = ", ".join(missing[:10])
        suffix = f" and {len(missing) - 10} more" if len(missing) > 10 else ""
        raise ValueError(f"{path} missing update keys: {preview}{suffix}")

    path.write_bytes("".join(out).encode("utf-8"))
    assert_csv_shapes([path])
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="CSV file to update. Relative paths resolve from repo root.")
    parser.add_argument("--key-column", default="ref", help="Column used to match TSV keys.")
    parser.add_argument("--target-column", default="draft_translation", help="Column to update.")
    parser.add_argument("--dry-run", action="store_true", help="Validate stdin and report matches without writing.")
    args = parser.parse_args()

    path = project_path(args.path)
    updates = read_updates()
    if args.dry_run:
        print({"update_csv_column_from_tsv_dry_run_ok": len(updates), "path": str(path)})
        return 0

    changed = update_file(path, args.key_column, args.target_column, updates)
    print({"updated_rows": changed, "path": str(path), "target_column": args.target_column})
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
