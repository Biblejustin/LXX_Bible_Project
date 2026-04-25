"""Shared helpers for repo-local build scripts."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"

csv.field_size_limit(sys.maxsize)


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(
    path: Path,
    rows: list[dict[str, str]],
    fieldnames: list[str] | None = None,
    *,
    lineterminator: str | None = "\n",
) -> None:
    if not rows and fieldnames is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    output_fieldnames = fieldnames if fieldnames is not None else list(rows[0].keys())
    kwargs = {"fieldnames": output_fieldnames}
    if lineterminator is not None:
        kwargs["lineterminator"] = lineterminator
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, **kwargs)
        writer.writeheader()
        writer.writerows(rows)


def run_script(script_name: str) -> None:
    subprocess.run([sys.executable, str(SCRIPTS / script_name)], check=True, cwd=ROOT)


def run_cmd(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True, cwd=ROOT)


def count_csv_rows(path: Path) -> int:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def replace_token(text: str, current_form: str, preferred_form: str) -> tuple[str, int]:
    pattern = re.compile(rf"\b{re.escape(current_form)}\b")
    return pattern.subn(preferred_form, text)


def count_token(text: str, form: str) -> int:
    pattern = re.compile(rf"\b{re.escape(form)}\b")
    return len(pattern.findall(text))


def sample_rows(rows: list[dict[str, str]], limit: int) -> list[dict[str, str]]:
    return rows[:limit]
