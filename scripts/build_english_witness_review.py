#!/usr/bin/env python3
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
LOCAL = ROOT / "data" / "research" / "local" / "witness_review"

OBSERVATIONS = LOCAL / "english_witness_observations.csv"
PRIORITY_CSV = OUTPUT / "fresh_vs_brenton_ot_priority_review.csv"

OUT_MD = OUTPUT / "fresh_ot_english_witness_review.md"
OUT_CSV = OUTPUT / "fresh_ot_english_witness_review.csv"
WATCH_MD = OUTPUT / "fresh_ot_english_witness_watch.md"
WATCH_CSV = OUTPUT / "fresh_ot_english_witness_watch.csv"
DIAGNOSTICS = OUTPUT / "fresh_ot_english_witness_review_diagnostics.json"

ALIGNMENT_FIELDS = ["les_alignment", "nets_alignment", "saas_alignment"]
SIGNAL_FIELDS = ["les_signal", "nets_signal", "saas_signal"]


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


def summarize_row(row: dict[str, str], priority_by_ref: dict[str, dict[str, str]]) -> dict[str, str] | None:
    checked_values = []
    for field in ALIGNMENT_FIELDS:
        value = (row.get(field) or "").strip()
        if value and value != "not_checked":
            checked_values.append(value)
    if not checked_values:
        return None

    signal_values = []
    for field in SIGNAL_FIELDS:
        value = (row.get(field) or "").strip()
        if value and value != "no_issue":
            signal_values.append(value)

    priority = priority_by_ref.get(row["ref"], {})
    fresh_support = sum(1 for value in checked_values if value == "agrees_fresh")
    brenton_support = sum(1 for value in checked_values if value == "agrees_brenton")
    mt_support = sum(1 for value in checked_values if value == "agrees_mt")
    differs_all = sum(1 for value in checked_values if value == "differs_all")
    split_or_mixed = sum(1 for value in checked_values if value == "split_or_mixed")
    recommendation = (row.get("consensus_recommendation") or "").strip()

    watch = False
    if recommendation in {"revise", "needs_logos", "defer"}:
        watch = True
    elif recommendation == "keep":
        watch = False
    else:
        if fresh_support == 0 and (brenton_support > 0 or mt_support > 0 or differs_all > 0):
            watch = True
        if differs_all > 0 or split_or_mixed > 0:
            watch = True
        if signal_values:
            watch = True

    return {
        "ref": row["ref"],
        "priority_score": priority.get("priority_score", row.get("priority_score", "")),
        "importance": priority.get("importance", row.get("importance", "")),
        "gate_sources": row.get("gate_sources", ""),
        "checked_witnesses": str(len(checked_values)),
        "fresh_support": str(fresh_support),
        "brenton_support": str(brenton_support),
        "mt_support": str(mt_support),
        "differs_all": str(differs_all),
        "split_or_mixed": str(split_or_mixed),
        "signals": ", ".join(sorted(dict.fromkeys(signal_values))),
        "recommendation": recommendation,
        "fresh_translation": priority.get("fresh_translation", row.get("fresh_translation", "")),
        "brenton_translation": priority.get("brenton_translation", row.get("brenton_translation", "")),
        "watch": "yes" if watch else "no",
    }


def build_md(title: str, rows: list[dict[str, str]]) -> str:
    lines = [f"# {title}", "", f"Rows: {len(rows)}", ""]
    for row in rows:
        lines.extend(
            [
                f"## {row['ref']}",
                f"- priority: `{row.get('priority_score', '0')}`",
                f"- importance: `{row.get('importance', 'none')}`",
                f"- checked witnesses: `{row.get('checked_witnesses', '0')}`",
                f"- fresh support: `{row.get('fresh_support', '0')}`",
                f"- brenton support: `{row.get('brenton_support', '0')}`",
                f"- mt support: `{row.get('mt_support', '0')}`",
                f"- differs all: `{row.get('differs_all', '0')}`",
                f"- split/mixed: `{row.get('split_or_mixed', '0')}`",
                f"- signals: {row.get('signals', '[none]') or '[none]'}",
                f"- recommendation: `{row.get('recommendation', '') or 'none'}`",
                f"- fresh: {row.get('fresh_translation', '[missing]')}",
                f"- brenton: {row.get('brenton_translation', '[missing]')}",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    observations = load_csv(OBSERVATIONS)
    priority_by_ref = {row["ref"]: row for row in load_csv(PRIORITY_CSV)}

    rows = []
    for row in observations:
        summarized = summarize_row(row, priority_by_ref)
        if summarized:
            rows.append(summarized)

    rows.sort(key=lambda row: (-int(row.get("priority_score") or 0), row["ref"]))
    watch_rows = [row for row in rows if row["watch"] == "yes"]

    fieldnames = [
        "ref",
        "priority_score",
        "importance",
        "gate_sources",
        "checked_witnesses",
        "fresh_support",
        "brenton_support",
        "mt_support",
        "differs_all",
        "split_or_mixed",
        "signals",
        "recommendation",
        "fresh_translation",
        "brenton_translation",
        "watch",
    ]
    write_csv(OUT_CSV, rows, fieldnames)
    write_csv(WATCH_CSV, watch_rows, fieldnames)
    OUT_MD.write_text(build_md("Fresh OT English Witness Review", rows), encoding="utf-8")
    WATCH_MD.write_text(build_md("Fresh OT English Witness Watch", watch_rows), encoding="utf-8")

    diagnostics = {
        "observations_path": str(OBSERVATIONS),
        "rows_with_checked_witnesses": len(rows),
        "watch_rows": len(watch_rows),
        "output_csv": str(OUT_CSV),
        "watch_csv": str(WATCH_CSV),
    }
    DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2))


if __name__ == "__main__":
    main()
