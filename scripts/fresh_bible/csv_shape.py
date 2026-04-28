"""CSV row-width validation helpers.

Manual review rows often contain prose. A bare comma in an unquoted field shifts
the row width and corrupts the table. These helpers make that failure explicit
and reusable across scripts, tests, and local pre-commit checks.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CsvShapeIssue:
    path: Path
    line_number: int
    expected_width: int
    actual_width: int
    row: list[str]


def csv_shape_issues(path: Path) -> list[CsvShapeIssue]:
    """Return rows whose parsed column count differs from the header width."""

    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        return [CsvShapeIssue(path, 1, 1, 0, [])]

    expected_width = len(rows[0])
    return [
        CsvShapeIssue(path, index + 1, expected_width, len(row), row)
        for index, row in enumerate(rows)
        if len(row) != expected_width
    ]


def format_csv_shape_issue(issue: CsvShapeIssue) -> str:
    sample = " | ".join(issue.row[: min(len(issue.row), 8)])
    if len(issue.row) > 8:
        sample += " | ..."
    return (
        f"{issue.path}: line {issue.line_number} has {issue.actual_width} columns; "
        f"expected {issue.expected_width}. Row: {sample}"
    )


def assert_csv_shapes(paths: list[Path]) -> None:
    issues: list[CsvShapeIssue] = []
    for path in paths:
        if path.exists():
            issues.extend(csv_shape_issues(path))

    if issues:
        detail = "\n".join(format_csv_shape_issue(issue) for issue in issues[:10])
        if len(issues) > 10:
            detail += f"\n... {len(issues) - 10} more CSV shape issues"
        raise ValueError(detail)
