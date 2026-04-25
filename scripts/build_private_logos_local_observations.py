#!/usr/bin/env python3
import csv
from pathlib import Path

from build_idiom_consistency_review import FAMILIES


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
RAW = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
LOCAL = ROOT / "data" / "research" / "local" / "witness_review"

CORE_CSV = OUTPUT / "fresh_human_review_core.csv"
PHASE1_CSV = OUTPUT / "fresh_human_review_phase1.csv"
NT_WATCH_CSV = OUTPUT / "fresh_human_review_nt_watch.csv"
MT_WATCH_CSV = OUTPUT / "fresh_human_review_mt_watch.csv"
OUT_CSV = LOCAL / "logos_local_observations.csv"
OUT_README = LOCAL / "logos_local_observations_README.md"

FIELDNAMES = [
    "order",
    "scope_type",
    "scope_key",
    "term",
    "matched_refs",
    "gate_sources",
    "source_tools",
    "signal_type",
    "observation_summary",
    "supports",
    "confidence",
    "recommendation",
    "reviewer_notes",
]

SEEDS = {
    ("family", "soteria-sacrifice-formula"): {
        "term": "soteria / soterion",
        "source_tools": "AutoComplete.db WordSense; Bible Word Study; Factbook; recent history",
        "signal_type": "lexical_support",
        "observation_summary": (
            "Local Logos word-sense and Bible Word Study cluster soteria around salvation/deliverance. "
            "Peace/well-being appears, but not as the dominant controlling sense."
        ),
        "supports": "salvation-shaped rendering",
        "confidence": "high",
        "recommendation": "keep",
        "reviewer_notes": "Derived from local Logos index/state inspection on 2026-04-16.",
    },
    ("ref", "Genesis 1:2"): {
        "term": "pneuma Theou / spirit",
        "source_tools": "AutoComplete.db WordSense; recent history; local index inspection",
        "signal_type": "lexical_support",
        "observation_summary": (
            "Local Logos word-sense index distinguishes spirit, Spirit of God, and soul/spirit crossover. "
            "That supports reading pneuma Theou here as Spirit, not mere wind."
        ),
        "supports": "Spirit of God rendering",
        "confidence": "medium",
        "recommendation": "keep",
        "reviewer_notes": "Derived from local Logos index/state inspection on 2026-04-16.",
    },
    ("ref", "Exodus 28:30"): {
        "term": "delosis / aletheia",
        "source_tools": "Bible Word Study; linked commentary snippets",
        "signal_type": "lexical_support",
        "observation_summary": (
            "Logos Bible Word Study keeps aletheia anchored at truth and shows delosis in disclosure or declaration "
            "language, while linked commentary snippets repeatedly treat the LXX wording as a semantic rendering of "
            "Urim and Thummim rather than a preserved transliteration."
        ),
        "supports": "Disclosure and Truth rendering",
        "confidence": "high",
        "recommendation": "keep",
        "reviewer_notes": "Derived from user-supplied Logos Bible Word Study screenshots on 2026-04-16.",
    },
    ("family", "into-living-soul-formula"): {
        "term": "psyche / soul",
        "source_tools": "AutoComplete.db WordSense; milestones/headwords; local index inspection",
        "signal_type": "lexical_support",
        "observation_summary": (
            "Local Logos word-sense index exposes soul as a primary sense and separately marks person/inner-person "
            "extensions. That supports keeping living soul visible where the formula is textually central."
        ),
        "supports": "living soul rendering",
        "confidence": "medium",
        "recommendation": "keep",
        "reviewer_notes": "Derived from local Logos index/state inspection on 2026-04-16.",
    },
}


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def merged_review_rows() -> list[dict[str, str]]:
    rows_by_ref: dict[str, dict[str, str]] = {}
    for source_name, path in [
        ("phase1", PHASE1_CSV),
        ("core", CORE_CSV),
        ("nt_watch", NT_WATCH_CSV),
        ("mt_watch", MT_WATCH_CSV),
    ]:
        for row in load_csv(path):
            ref = (row.get("ref") or "").strip()
            if not ref:
                continue
            existing = rows_by_ref.setdefault(ref, dict(row))
            gate_sources = {
                part.strip()
                for part in (existing.get("gate_sources") or "").split(",")
                if part.strip()
            }
            gate_sources.add(source_name)
            existing.update(row)
            existing["gate_sources"] = ", ".join(sorted(gate_sources))
    return list(rows_by_ref.values())


def load_source_by_ref(path: Path) -> dict[str, dict[str, str]]:
    return {row["ref"]: row for row in load_csv(path) if row.get("ref")}


def families_by_ref(source_by_ref: dict[str, dict[str, str]]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for ref, row in source_by_ref.items():
        greek = row.get("greek_text", "") or ""
        out[ref] = {family["name"] for family in FAMILIES if family["match"](greek)}
    return out


def main() -> None:
    review_rows = merged_review_rows()
    source_by_ref = load_source_by_ref(RAW)
    ref_families = families_by_ref(source_by_ref)
    prior = {
        ((row.get("scope_type") or "").strip(), (row.get("scope_key") or "").strip()): row
        for row in load_csv(OUT_CSV)
        if (row.get("scope_key") or "").strip()
    }

    out_rows: list[dict[str, str]] = []
    for index, (scope_type, scope_key) in enumerate(sorted(SEEDS), start=1):
        seed = SEEDS[(scope_type, scope_key)]
        if scope_type == "family":
            matching = [
                row
                for row in review_rows
                if scope_key in ref_families.get(row.get("ref", ""), set())
            ]
        else:
            matching = [row for row in review_rows if row.get("ref") == scope_key]
        if not matching:
            continue
        gate_sources = sorted(
            {
                part.strip()
                for row in matching
                for part in (row.get("gate_sources") or "").split(",")
                if part.strip()
            }
        )
        matched_refs = ", ".join(
            row["ref"]
            for row in sorted(matching, key=lambda item: (-int(item.get("priority_score") or 0), item["ref"]))[:12]
        )
        existing = prior.get((scope_type, scope_key), {})
        out_rows.append(
            {
                "order": str(index),
                "scope_type": scope_type,
                "scope_key": scope_key,
                "term": existing.get("term", seed["term"]),
                "matched_refs": matched_refs,
                "gate_sources": ", ".join(gate_sources),
                "source_tools": existing.get("source_tools", seed["source_tools"]),
                "signal_type": existing.get("signal_type", seed["signal_type"]),
                "observation_summary": existing.get("observation_summary", seed["observation_summary"]),
                "supports": existing.get("supports", seed["supports"]),
                "confidence": existing.get("confidence", seed["confidence"]),
                "recommendation": existing.get("recommendation", seed["recommendation"]),
                "reviewer_notes": existing.get("reviewer_notes", seed["reviewer_notes"]),
            }
        )

    write_csv(OUT_CSV, out_rows)
    OUT_README.write_text(
        "\n".join(
            [
                "# Logos Local Observations",
                "",
                "Private file.",
                "Use short derived notes only.",
                "Do not paste copyrighted book text.",
                "",
                "Scope types:",
                "- `family`",
                "- `ref`",
                "",
                "Signal types:",
                "- `lexical_support`",
                "- `idiom_support`",
                "- `textual_note`",
                "- `unclear`",
                "",
                "Recommendation values:",
                "- `keep`",
                "- `revise`",
                "- `needs_logos`",
                "- `defer`",
                "",
                f"Seed rows: {len(out_rows)}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    print(OUT_CSV)
    print(OUT_README)


if __name__ == "__main__":
    main()
