#!/usr/bin/env python3
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW_DIR = ROOT / "data" / "research"
SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
PRIORITY = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.csv"
OUT_CSV = ROOT / "output" / "fresh_vs_brenton_ot_final_unresolved.csv"
OUT_MD = ROOT / "output" / "fresh_vs_brenton_ot_final_unresolved.md"


def review_sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"ot_review_pass_(\d+)\.md$", path.name)
    return (int(match.group(1)), path.name) if match else (0, path.name)


def load_latest_statuses() -> dict[str, str]:
    statuses: dict[str, str] = {}
    for path in sorted(REVIEW_DIR.glob("ot_review_pass_*.md"), key=review_sort_key):
        ref = None
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if line.startswith("## "):
                ref = line[3:].strip()
            elif ref and line.startswith("- status:"):
                match = re.search(r"`([^`]+)`", line)
                statuses[ref] = match.group(1) if match else line.split(":", 1)[1].strip()
    return statuses


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    statuses = load_latest_statuses()
    src_rows = {row["ref"]: row for row in load_csv(SOURCE)}
    pri_rows = {row["ref"]: row for row in load_csv(PRIORITY)}

    rows: list[dict[str, str]] = []
    for ref, status in sorted(statuses.items()):
        if status != "keep-provisional":
            continue
        src = src_rows.get(ref, {})
        pri = pri_rows.get(ref, {})
        rows.append(
            {
                "ref": ref,
                "priority_score": pri.get("priority_score", ""),
                "importance": pri.get("importance", ""),
                "fresh_translation": src.get("draft_translation", ""),
                "greek_text": src.get("greek_text", ""),
                "brenton_translation": pri.get("brenton_translation", ""),
            }
        )

    rows.sort(key=lambda row: (-int(row["priority_score"] or 0), row["ref"]))

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["ref", "priority_score", "importance", "fresh_translation", "greek_text", "brenton_translation"],
        )
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Final Unresolved OT Review",
        "",
        f"Rows: {len(rows)}",
        "",
    ]
    for row in rows:
        lines.extend(
            [
                f"## {row['ref']}",
                f"- priority: `{row['priority_score']}`",
                f"- importance: `{row['importance']}`",
                f"- fresh: {row['fresh_translation']}",
                f"- brenton: {row['brenton_translation'] or '[missing]'}",
                "",
            ]
        )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(OUT_CSV)
    print(OUT_MD)


if __name__ == "__main__":
    main()
