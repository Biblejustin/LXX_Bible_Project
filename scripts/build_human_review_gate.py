#!/usr/bin/env python3
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"

PRIORITY_CSV = OUTPUT / "fresh_vs_brenton_ot_priority_review.csv"
MT_LEANING_CSV = OUTPUT / "fresh_mt_leaning_vs_brenton.csv"
NT_WATCH_CSV = OUTPUT / "fresh_human_review_nt_watch.csv"
NT_WATCH_MD = OUTPUT / "fresh_human_review_nt_watch.md"

CORE_CSV = OUTPUT / "fresh_human_review_core.csv"
CORE_MD = OUTPUT / "fresh_human_review_core.md"
PHASE1_CSV = OUTPUT / "fresh_human_review_phase1.csv"
PHASE1_MD = OUTPUT / "fresh_human_review_phase1.md"
MT_WATCH_CSV = OUTPUT / "fresh_human_review_mt_watch.csv"
MT_WATCH_MD = OUTPUT / "fresh_human_review_mt_watch.md"
DIAGNOSTICS = OUTPUT / "fresh_human_review_gate_diagnostics.json"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(["ref"])
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_md(title: str, rows: list[dict[str, str]], intro: list[str]) -> str:
    lines = [f"# {title}", "", *intro, "", f"Rows: {len(rows)}", ""]
    for row in rows:
        lines.extend(
            [
                f"## {row['ref']}",
                f"- priority: `{row.get('priority_score', '0')}`",
                f"- importance: `{row.get('importance', 'none')}`",
                f"- reason: {row.get('gate_reason', '[none]')}",
                f"- nt refs: {row.get('nt_parallel_refs', '[none]') or '[none]'}",
                f"- fresh: {row.get('fresh_translation', '[missing]')}",
                f"- brenton: {row.get('brenton_translation', '[missing]')}",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    priority_rows = load_csv(PRIORITY_CSV)
    mt_rows = load_csv(MT_LEANING_CSV)

    core_rows: list[dict[str, str]] = []
    phase1_rows: list[dict[str, str]] = []
    nt_watch_rows: list[dict[str, str]] = []
    for row in priority_rows:
        score = int(row.get("priority_score") or 0)
        decisions = int(row.get("decision_count") or 0)
        footnotes = int(row.get("footnote_count") or 0)
        nt_count = int(row.get("nt_parallel_count") or 0)
        importance = row.get("importance", "none")
        reasons: list[str] = []
        if score >= 12:
            reasons.append("score>=12")
        if importance == "high":
            reasons.append("importance=high")
        if decisions > 0:
            reasons.append(f"decisions={decisions}")
        if footnotes > 0:
            reasons.append(f"footnotes={footnotes}")
        if nt_count > 0:
            reasons.append(f"nt={nt_count}")
        if reasons:
            enriched = dict(row)
            enriched["gate_reason"] = "; ".join(reasons)
            core_rows.append(enriched)
        phase1_reasons: list[str] = []
        if score >= 16:
            phase1_reasons.append("score>=16")
        if importance == "high" and (decisions > 0 or footnotes > 0):
            phase1_reasons.append("high+tracked")
        if nt_count > 0 and score >= 14:
            phase1_reasons.append("nt+score>=14")
        if phase1_reasons:
            enriched = dict(row)
            enriched["gate_reason"] = "; ".join(phase1_reasons)
            phase1_rows.append(enriched)
        if nt_count > 0 and score >= 10:
            enriched = dict(row)
            enriched["gate_reason"] = f"nt={nt_count}; score={score}"
            nt_watch_rows.append(enriched)

    mt_watch_rows: list[dict[str, str]] = []
    for row in mt_rows:
        score = int(row.get("priority_score") or 0)
        if score < 12:
            continue
        enriched = dict(row)
        enriched["gate_reason"] = "mt-leaning score>=12"
        mt_watch_rows.append(enriched)

    core_rows.sort(key=lambda row: (-int(row.get("priority_score") or 0), row["ref"]))
    phase1_rows.sort(key=lambda row: (-int(row.get("priority_score") or 0), row["ref"]))
    mt_watch_rows.sort(key=lambda row: (-int(row.get("priority_score") or 0), row["ref"]))
    nt_watch_rows.sort(key=lambda row: (-int(row.get("priority_score") or 0), row["ref"]))

    write_csv(CORE_CSV, core_rows)
    write_csv(PHASE1_CSV, phase1_rows)
    write_csv(MT_WATCH_CSV, mt_watch_rows)
    write_csv(NT_WATCH_CSV, nt_watch_rows)

    CORE_MD.write_text(
        build_md(
            "Fresh OT Human Review Core",
            core_rows,
            [
                "Gate = score >= 12 OR importance high OR tracked decisions/footnotes.",
                "Use this instead of thousand-row outputs.",
            ],
        ),
        encoding="utf-8",
    )
    PHASE1_MD.write_text(
        build_md(
            "Fresh OT Human Review Phase 1",
            phase1_rows,
            [
                "Gate = score >= 16 OR high + tracked.",
                "Smallest first-pass queue.",
            ],
        ),
        encoding="utf-8",
    )
    MT_WATCH_MD.write_text(
        build_md(
            "Fresh OT MT-Leaning Watch",
            mt_watch_rows,
            [
                "Fresh closer to MT/UKJV than Brenton by threshold.",
                "Only rows with score >= 12 kept here.",
            ],
        ),
        encoding="utf-8",
    )
    NT_WATCH_MD.write_text(
        build_md(
            "Fresh OT NT Idiom Watch",
            nt_watch_rows,
            [
                "Rows in NT-linked Greek idiom families.",
                "Only rows with score >= 10 kept here.",
            ],
        ),
        encoding="utf-8",
    )

    diagnostics = {
        "priority_rows": len(priority_rows),
        "core_rows": len(core_rows),
        "phase1_rows": len(phase1_rows),
        "mt_watch_rows": len(mt_watch_rows),
        "nt_watch_rows": len(nt_watch_rows),
        "core_csv": str(CORE_CSV),
        "phase1_csv": str(PHASE1_CSV),
        "mt_watch_csv": str(MT_WATCH_CSV),
        "nt_watch_csv": str(NT_WATCH_CSV),
    }
    DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2))


if __name__ == "__main__":
    main()
