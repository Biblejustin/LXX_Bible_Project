#!/usr/bin/env python3
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "data" / "research"
LOCAL = RESEARCH / "local" / "witness_review"
LOGOS_SCAN_MERGED = RESEARCH / "local" / "logos_scan_merged" / "logos_resources_all.csv"
LOGOS_SCAN_SINGLE = RESEARCH / "local" / "logos_scan" / "logos_resources_all.csv"
NT_PARALLELS = RESEARCH / "nt_idiom_parallels.csv"

OUT_CSV = LOCAL / "nt_english_witness_observations.csv"
OUT_README = LOCAL / "nt_english_witness_observations_README.md"


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "order",
        "family",
        "nt_ref",
        "weight",
        "relevance",
        "note",
        "nt_greek",
        "literal_gloss",
        "lsb_resource",
        "esv_resource",
        "kjv_resource",
        "lsb_alignment",
        "esv_alignment",
        "kjv_alignment",
        "lsb_signal",
        "esv_signal",
        "kjv_signal",
        "consensus_recommendation",
        "reviewer_notes",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def logos_rows() -> list[dict[str, str]]:
    path = LOGOS_SCAN_MERGED if LOGOS_SCAN_MERGED.exists() else LOGOS_SCAN_SINGLE
    return load_csv(path)


def label(row: dict[str, str]) -> str:
    title = (row.get("title") or row.get("short_title") or row.get("resource_id") or "").strip()
    rid = (row.get("resource_id") or "").strip()
    return f"{title} [{rid}]".strip()


def first_exact(rows: list[dict[str, str]], *, title: str = "", resource_id: str = "") -> str:
    for row in rows:
        if title and (row.get("title") or "").strip() == title:
            return label(row)
        if resource_id and (row.get("resource_id") or "").strip() == resource_id:
            return label(row)
    return ""


def first_match(rows: list[dict[str, str]], patterns: list[str]) -> str:
    compiled = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    for row in rows:
        text = " | ".join([row.get("title", "") or "", row.get("short_title", "") or "", row.get("resource_id", "") or ""])
        if any(pattern.search(text) for pattern in compiled):
            return label(row)
    return ""


def resource_map() -> dict[str, str]:
    rows = logos_rows()
    return {
        "lsb_resource": first_exact(rows, title="Legacy Standard Bible") or first_match(rows, [r"legacy standard bible"]),
        "esv_resource": first_exact(rows, title="English Standard Version")
        or first_exact(rows, resource_id="LLS:1.0.710")
        or first_match(rows, [r"english standard version"]),
        "kjv_resource": first_exact(rows, title="King James Version")
        or first_exact(rows, resource_id="LLS:KJV1900")
        or first_match(rows, [r"king james version"]),
    }


def main() -> None:
    resources = resource_map()
    prior = {(row["family"], row["nt_ref"]): row for row in load_csv(OUT_CSV)}
    parallels = load_csv(NT_PARALLELS)

    out_rows: list[dict[str, str]] = []
    for index, row in enumerate(
        sorted(
            parallels,
            key=lambda item: (-int(item.get("weight") or 0), item.get("family", ""), item.get("nt_ref", "")),
        ),
        start=1,
    ):
        key = (row["family"], row["nt_ref"])
        existing = prior.get(key, {})
        out_rows.append(
            {
                "order": str(index),
                "family": row["family"],
                "nt_ref": row["nt_ref"],
                "weight": row.get("weight", ""),
                "relevance": row.get("relevance", ""),
                "note": row.get("note", ""),
                "nt_greek": row.get("nt_greek", ""),
                "literal_gloss": row.get("literal_gloss", ""),
                "lsb_resource": resources["lsb_resource"],
                "esv_resource": resources["esv_resource"],
                "kjv_resource": resources["kjv_resource"],
                "lsb_alignment": existing.get("lsb_alignment", ""),
                "esv_alignment": existing.get("esv_alignment", ""),
                "kjv_alignment": existing.get("kjv_alignment", ""),
                "lsb_signal": existing.get("lsb_signal", ""),
                "esv_signal": existing.get("esv_signal", ""),
                "kjv_signal": existing.get("kjv_signal", ""),
                "consensus_recommendation": existing.get("consensus_recommendation", ""),
                "reviewer_notes": existing.get("reviewer_notes", ""),
            }
        )

    write_csv(OUT_CSV, out_rows)
    OUT_README.write_text(
        "\n".join(
            [
                "# NT English Witness Observations",
                "",
                "Private file.",
                "Do not paste long copyrighted text here.",
                "Use short judgments only.",
                "",
                "Alignment values:",
                "- `supports_greek_family`",
                "- `softens_greek_family`",
                "- `mixed`",
                "- `not_checked` or blank",
                "",
                "Signal values:",
                "- `literal_support`",
                "- `smoothing`",
                "- `translation_tradition`",
                "- `unclear`",
                "- `no_issue`",
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
