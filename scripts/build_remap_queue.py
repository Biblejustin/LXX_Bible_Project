#!/usr/bin/env python3
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW_DIR = ROOT / "data" / "research"
OT_SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
PRIORITY_CSV = ROOT / "output" / "fresh_vs_brenton_ot_priority_review.csv"
OUT_CSV = ROOT / "output" / "fresh_vs_brenton_ot_remap_queue.csv"
OUT_MD = ROOT / "output" / "fresh_vs_brenton_ot_remap_queue.md"


def review_pass_sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"ot_review_pass_(\d+)\.md$", path.name)
    if not match:
        return (0, path.name)
    return (int(match.group(1)), path.name)


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_review_passes() -> dict[str, dict[str, str]]:
    merged: dict[str, dict[str, str]] = {}
    for path in sorted(REVIEW_DIR.glob("ot_review_pass_*.md"), key=review_pass_sort_key):
        current_ref = None
        current: dict[str, str] = {}
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if line.startswith("## "):
                current_ref = line[3:].strip()
                current = {"ref": current_ref, "review_pass": path.name}
                merged[current_ref] = current
            elif current_ref and line.startswith("- status:"):
                match = re.search(r"`([^`]+)`", line)
                current["status"] = match.group(1) if match else ""
            elif current_ref and line.startswith("- focus:"):
                current["focus"] = line.split(":", 1)[1].strip()
            elif current_ref and line.startswith("- reason:"):
                current["reason"] = line.split(":", 1)[1].strip()
        merged.update({k: v for k, v in list(merged.items()) if v.get("status") == "needs-remap"})
    return {ref: row for ref, row in merged.items() if row.get("status") == "needs-remap"}


def main() -> None:
    remap_rows = parse_review_passes()
    ot_rows = {row["ref"]: row for row in load_csv(OT_SOURCE)}
    priority_rows = {row["ref"]: row for row in load_csv(PRIORITY_CSV)} if PRIORITY_CSV.exists() else {}

    rows: list[dict[str, str]] = []
    for order, ref in enumerate(sorted(remap_rows), start=1):
        meta = remap_rows[ref]
        ot = ot_rows.get(ref, {})
        pr = priority_rows.get(ref, {})
        rows.append(
            {
                "order": str(order),
                "ref": ref,
                "review_pass": meta.get("review_pass", ""),
                "priority_score": pr.get("priority_score", ""),
                "importance": pr.get("importance", ""),
                "reason": meta.get("reason", ""),
                "focus": meta.get("focus", ""),
                "greek_text": ot.get("greek_text", ""),
                "draft_translation": ot.get("draft_translation", ""),
                "remap_status": "pending",
                "remap_notes": "",
            }
        )

    fieldnames = [
        "order",
        "ref",
        "review_pass",
        "priority_score",
        "importance",
        "reason",
        "focus",
        "greek_text",
        "draft_translation",
        "remap_status",
        "remap_notes",
    ]

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# OT Remap Queue",
        "",
        f"Rows: {len(rows)}",
        "",
        "Use CSV for edits.",
        "",
    ]
    for row in rows:
        lines.extend(
            [
                f"## {row['ref']}",
                f"- pass: `{row['review_pass']}`",
                f"- priority: `{row['priority_score'] or 'n/a'}`",
                f"- reason: {row['reason']}",
                "",
            ]
        )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(OUT_CSV)
    print(OUT_MD)


if __name__ == "__main__":
    main()
