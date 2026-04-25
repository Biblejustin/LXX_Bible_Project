#!/usr/bin/env python3
import csv
import json
from collections import defaultdict
from pathlib import Path

from build_idiom_consistency_review import FAMILIES


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
OUTPUT = ROOT / "output"
LOCAL = ROOT / "data" / "research" / "local" / "witness_review"

OBSERVATIONS = LOCAL / "logos_local_observations.csv"
PRIORITY_CSV = OUTPUT / "fresh_vs_brenton_ot_priority_review.csv"
OUT_MD = OUTPUT / "fresh_ot_logos_local_review.md"
OUT_CSV = OUTPUT / "fresh_ot_logos_local_review.csv"
WATCH_MD = OUTPUT / "fresh_ot_logos_local_watch.md"
WATCH_CSV = OUTPUT / "fresh_ot_logos_local_watch.csv"
DIAGNOSTICS = OUTPUT / "fresh_ot_logos_local_review_diagnostics.json"


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def load_source_by_ref(path: Path) -> dict[str, dict[str, str]]:
    return {row["ref"]: row for row in load_csv(path) if row.get("ref")}


def families_by_ref(source_by_ref: dict[str, dict[str, str]]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for ref, row in source_by_ref.items():
        greek = row.get("greek_text", "") or ""
        out[ref] = {family["name"] for family in FAMILIES if family["match"](greek)}
    return out


def load_observation_map(path: Path) -> dict[str, dict[str, list[dict[str, str]]]]:
    out = {"ref": defaultdict(list), "family": defaultdict(list)}
    for row in load_csv(path):
        scope_type = (row.get("scope_type") or "").strip()
        scope_key = (row.get("scope_key") or "").strip()
        if scope_type in out and scope_key:
            out[scope_type][scope_key].append(row)
    return out


def summarize_row(
    priority_row: dict[str, str],
    observation_map: dict[str, dict[str, list[dict[str, str]]]],
    ref_families: dict[str, set[str]],
) -> dict[str, str] | None:
    matched = []
    ref = priority_row["ref"]
    matched.extend(observation_map["ref"].get(ref, []))
    for family_name in ref_families.get(ref, set()):
        matched.extend(observation_map["family"].get(family_name, []))
    if not matched:
        return None

    sources = sorted({row.get("source_tools", "").strip() for row in matched if row.get("source_tools", "").strip()})
    signals = sorted({row.get("signal_type", "").strip() for row in matched if row.get("signal_type", "").strip()})
    supports = sorted({row.get("supports", "").strip() for row in matched if row.get("supports", "").strip()})
    scopes = sorted({row.get("scope_key", "").strip() for row in matched if row.get("scope_key", "").strip()})
    summaries = [row.get("observation_summary", "").strip() for row in matched if row.get("observation_summary", "").strip()]
    recommendations = [row.get("recommendation", "").strip() for row in matched if row.get("recommendation", "").strip()]
    confidences = [row.get("confidence", "").strip() for row in matched if row.get("confidence", "").strip()]

    recommendation = ""
    for candidate in ("revise", "needs_logos", "defer", "keep"):
        if candidate in recommendations:
            recommendation = candidate
            break

    confidence = ""
    for candidate in ("high", "medium", "low"):
        if candidate in confidences:
            confidence = candidate
            break

    watch = recommendation in {"revise", "needs_logos", "defer"} or "unclear" in signals

    return {
        "ref": ref,
        "priority_score": priority_row.get("priority_score", ""),
        "importance": priority_row.get("importance", ""),
        "checked": str(len(matched)),
        "scopes": ", ".join(scopes),
        "signals": ", ".join(signals),
        "supports": ", ".join(supports),
        "recommendation": recommendation,
        "confidence": confidence,
        "source_tools": " | ".join(sources),
        "observation_summary": " | ".join(dict.fromkeys(summaries)),
        "fresh_translation": priority_row.get("fresh_translation", ""),
        "brenton_translation": priority_row.get("brenton_translation", ""),
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
                f"- checked: `{row.get('checked', '0')}`",
                f"- scopes: {row.get('scopes', '[none]') or '[none]'}",
                f"- signals: {row.get('signals', '[none]') or '[none]'}",
                f"- supports: {row.get('supports', '[none]') or '[none]'}",
                f"- recommendation: `{row.get('recommendation', '') or 'none'}`",
                f"- confidence: `{row.get('confidence', '') or 'none'}`",
                f"- tools: {row.get('source_tools', '[none]') or '[none]'}",
                f"- summary: {row.get('observation_summary', '[none]') or '[none]'}",
                f"- fresh: {row.get('fresh_translation', '[missing]')}",
                f"- brenton: {row.get('brenton_translation', '[missing]')}",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    source_by_ref = load_source_by_ref(RAW)
    ref_families = families_by_ref(source_by_ref)
    observation_map = load_observation_map(OBSERVATIONS)
    priority_rows = load_csv(PRIORITY_CSV)

    rows = []
    for priority_row in priority_rows:
        summarized = summarize_row(priority_row, observation_map, ref_families)
        if summarized:
            rows.append(summarized)

    rows.sort(key=lambda row: (-int(row.get("priority_score") or 0), row["ref"]))
    watch_rows = [row for row in rows if row["watch"] == "yes"]

    fieldnames = [
        "ref",
        "priority_score",
        "importance",
        "checked",
        "scopes",
        "signals",
        "supports",
        "recommendation",
        "confidence",
        "source_tools",
        "observation_summary",
        "fresh_translation",
        "brenton_translation",
        "watch",
    ]
    write_csv(OUT_CSV, rows, fieldnames)
    write_csv(WATCH_CSV, watch_rows, fieldnames)
    OUT_MD.write_text(build_md("Fresh OT Logos Local Review", rows), encoding="utf-8")
    WATCH_MD.write_text(build_md("Fresh OT Logos Local Watch", watch_rows), encoding="utf-8")

    diagnostics = {
        "observations_path": str(OBSERVATIONS),
        "rows_with_logos_local_signal": len(rows),
        "watch_rows": len(watch_rows),
        "output_csv": str(OUT_CSV),
        "watch_csv": str(WATCH_CSV),
    }
    DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2))


if __name__ == "__main__":
    main()
