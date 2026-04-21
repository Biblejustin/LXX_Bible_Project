#!/usr/bin/env python3
import argparse
import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "research" / "local" / "witness_review" / "logos_reading_list_export.csv"

DEFAULT_VERSIONS = [
    "NETS (Primary Texts)",
    "NET 2nd ed.",
    "LES",
    "LES2",
]

HEADING_RE = re.compile(
    r"^(?P<ref>(?:[1-4]\s+)?[A-Za-z][A-Za-z' .-]*\s+\d+:\d+(?:[–-]\d+)?)$"
)


def load_lines(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [line.strip() for line in text.splitlines()]


def is_heading(line: str) -> bool:
    if not line:
        return False
    if line.startswith("Exported from Logos"):
        return False
    return bool(HEADING_RE.match(line))


def clean_line(line: str) -> str:
    return " ".join(line.replace("\ufeff", "").split())


def parse_export(lines: list[str], versions: list[str]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows: list[dict[str, str]] = []
    issues: list[dict[str, str]] = []
    seen_rows: dict[str, dict[str, str]] = {}
    i = 0
    while i < len(lines):
        line = clean_line(lines[i])
        i += 1
        if not line or line == "Codex bible project":
            continue
        if not is_heading(line):
            continue

        ref = line
        blocks: list[str] = []
        while i < len(lines):
            nxt = clean_line(lines[i])
            if not nxt:
                i += 1
                continue
            if is_heading(nxt) or nxt.startswith("Exported from Logos"):
                break
            blocks.append(nxt)
            i += 1
            if len(blocks) == len(versions):
                break

        if len(blocks) != len(versions):
            issues.append(
                {
                    "ref": ref,
                    "issue": f"expected {len(versions)} version lines, found {len(blocks)}",
                }
            )
            continue

        row = {"ref": ref}
        for version, block in zip(versions, blocks):
            slug = (
                version.lower()
                .replace("(", "")
                .replace(")", "")
                .replace(".", "")
                .replace(" ", "_")
                .replace("-", "_")
            )
            row[slug] = block

        existing = seen_rows.get(ref)
        if existing is None:
            seen_rows[ref] = row
            rows.append(row)
            continue

        comparable_keys = [key for key in row if key != "ref"]
        if all(existing.get(key, "") == row.get(key, "") for key in comparable_keys):
            issues.append({"ref": ref, "issue": "duplicate_ref_identical_skipped"})
            continue

        issues.append({"ref": ref, "issue": "duplicate_ref_conflict_kept_first"})

    return rows, issues


def write_csv(path: Path, rows: list[dict[str, str]], versions: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["ref"]
    for version in versions:
        fieldnames.append(
            version.lower()
            .replace("(", "")
            .replace(")", "")
            .replace(".", "")
            .replace(" ", "_")
            .replace("-", "_")
        )
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Parse plain-text Logos reading-list export into per-ref witness rows.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--versions", nargs="+", default=DEFAULT_VERSIONS)
    args = parser.parse_args()

    lines = load_lines(args.input)
    rows, issues = parse_export(lines, args.versions)
    write_csv(args.output, rows, args.versions)

    print(
        json.dumps(
            {
                "input": args.input.as_posix(),
                "output": args.output.as_posix(),
                "versions": args.versions,
                "rows": len(rows),
                "issues": issues[:20],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
