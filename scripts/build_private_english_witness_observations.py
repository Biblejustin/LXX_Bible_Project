#!/usr/bin/env python3
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
LOCAL = ROOT / "data" / "research" / "local" / "witness_review"

CORE_CSV = OUTPUT / "fresh_human_review_core.csv"
PHASE1_CSV = OUTPUT / "fresh_human_review_phase1.csv"
NT_WATCH_CSV = OUTPUT / "fresh_human_review_nt_watch.csv"
MT_WATCH_CSV = OUTPUT / "fresh_human_review_mt_watch.csv"
MT_REVIEW_CSV = OUTPUT / "fresh_vs_mt_brenton_ot_review.csv"
RESOURCE_SHORTLIST = LOCAL / "resource_shortlist.csv"
OUT_CSV = LOCAL / "english_witness_observations.csv"
OUT_README = LOCAL / "english_witness_observations_README.md"


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "order",
        "ref",
        "priority_score",
        "importance",
        "gate_sources",
        "fresh_translation",
        "brenton_translation",
        "mt_translation",
        "les_resource",
        "nets_resource",
        "saas_resource",
        "les_alignment",
        "nets_alignment",
        "saas_alignment",
        "les_signal",
        "nets_signal",
        "saas_signal",
        "consensus_recommendation",
        "reviewer_notes",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def resource_map(path: Path) -> dict[str, str]:
    out = {"les_resource": "", "nets_resource": "", "saas_resource": ""}
    for row in load_csv(path):
        slot = (row.get("slot") or "").strip()
        title = (row.get("title") or row.get("short_title") or row.get("resource_id") or "").strip()
        rid = (row.get("resource_id") or "").strip()
        label = f"{title} [{rid}]".strip()
        if slot == "english_les" and not out["les_resource"]:
            out["les_resource"] = label
        elif slot == "english_nets" and not out["nets_resource"]:
            out["nets_resource"] = label
        elif slot == "english_saas" and not out["saas_resource"]:
            out["saas_resource"] = label
    return out


def mt_by_ref(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for row in load_csv(path):
        ref = (row.get("ref") or "").strip()
        if ref:
            out[ref] = row.get("mt_translation", "")
    return out


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


def main() -> None:
    rows = merged_review_rows()
    prior = {row["ref"]: row for row in load_csv(OUT_CSV)}
    mt_map = mt_by_ref(MT_REVIEW_CSV)
    resources = resource_map(RESOURCE_SHORTLIST)

    out_rows: list[dict[str, str]] = []
    for index, row in enumerate(
        sorted(rows, key=lambda item: (-int(item.get("priority_score") or 0), item["ref"])),
        start=1,
    ):
        ref = row["ref"]
        existing = prior.get(ref, {})
        out_rows.append(
            {
                "order": str(index),
                "ref": ref,
                "priority_score": row.get("priority_score", ""),
                "importance": row.get("importance", ""),
                "gate_sources": row.get("gate_sources", ""),
                "fresh_translation": row.get("fresh_translation", ""),
                "brenton_translation": row.get("brenton_translation", ""),
                "mt_translation": mt_map.get(ref, ""),
                "les_resource": resources["les_resource"],
                "nets_resource": resources["nets_resource"],
                "saas_resource": resources["saas_resource"],
                "les_alignment": existing.get("les_alignment", ""),
                "nets_alignment": existing.get("nets_alignment", ""),
                "saas_alignment": existing.get("saas_alignment", ""),
                "les_signal": existing.get("les_signal", ""),
                "nets_signal": existing.get("nets_signal", ""),
                "saas_signal": existing.get("saas_signal", ""),
                "consensus_recommendation": existing.get("consensus_recommendation", ""),
                "reviewer_notes": existing.get("reviewer_notes", ""),
            }
        )

    seeded_refs = {row["ref"] for row in out_rows}
    preserved_prior = []
    for row in load_csv(OUT_CSV):
        ref = (row.get("ref") or "").strip()
        if not ref or ref in seeded_refs:
            continue
        review_fields = [
            row.get("les_alignment", ""),
            row.get("nets_alignment", ""),
            row.get("saas_alignment", ""),
            row.get("les_signal", ""),
            row.get("nets_signal", ""),
            row.get("saas_signal", ""),
            row.get("consensus_recommendation", ""),
            row.get("reviewer_notes", ""),
        ]
        if any((value or "").strip() for value in review_fields):
            preserved_prior.append(dict(row))

    start = len(out_rows) + 1
    for index, row in enumerate(preserved_prior, start=start):
        row["order"] = str(index)
        out_rows.append(row)

    write_csv(OUT_CSV, out_rows)
    OUT_README.write_text(
        "\n".join(
            [
                "# English Witness Observations",
                "",
                "Private file.",
                "Do not paste long copyrighted text here.",
                "Use short notes only.",
                "",
                "Alignment values:",
                "- `agrees_fresh`",
                "- `agrees_brenton`",
                "- `agrees_mt`",
                "- `split_or_mixed`",
                "- `differs_all`",
                "- `not_checked` or blank",
                "",
                "Signal values:",
                "- `no_issue`",
                "- `smoothing_issue`",
                "- `idiom_support`",
                "- `textual_issue`",
                "- `mt_leaning`",
                "- `lxx_plus`",
                "- `verse_map`",
                "- `unclear`",
                "",
                "Consensus recommendation values:",
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
