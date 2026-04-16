#!/usr/bin/env python3
import csv
import json
from collections import defaultdict
from pathlib import Path

from build_idiom_consistency_review import FAMILIES


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "lxx_greek" / "ot_full.csv"
NT_PARALLELS = ROOT / "data" / "research" / "nt_idiom_parallels.csv"
IDIOM_REVIEW_CSV = ROOT / "output" / "fresh_ot_idiom_consistency_review.csv"
IDIOM_OUTLIERS_CSV = ROOT / "output" / "fresh_ot_idiom_consistency_outliers.csv"
NT_ENGLISH_OBSERVATIONS = ROOT / "data" / "research" / "local" / "witness_review" / "nt_english_witness_observations.csv"
OUTPUT = ROOT / "output"

REVIEW_MD = OUTPUT / "fresh_ot_nt_idiom_review.md"
REVIEW_CSV = OUTPUT / "fresh_ot_nt_idiom_review.csv"
OUTLIERS_MD = OUTPUT / "fresh_ot_nt_idiom_outliers.md"
OUTLIERS_CSV = OUTPUT / "fresh_ot_nt_idiom_outliers.csv"
DIAGNOSTICS = OUTPUT / "fresh_ot_nt_idiom_review_diagnostics.json"


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
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


def load_nt_parallels(path: Path) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in load_csv(path):
        grouped[row["family"]].append(row)
    return grouped


def load_nt_english_observations(path: Path) -> dict[tuple[str, str], dict[str, str]]:
    rows = load_csv(path)
    return {
        ((row.get("family") or "").strip(), (row.get("nt_ref") or "").strip()): row
        for row in rows
        if (row.get("family") or "").strip() and (row.get("nt_ref") or "").strip()
    }


def summarize_nt_english(family: str, nt_rows: list[dict[str, str]], nt_english: dict[tuple[str, str], dict[str, str]]) -> dict[str, str]:
    selected = [
        nt_english[(family, nt_row["nt_ref"])]
        for nt_row in nt_rows
        if (family, nt_row["nt_ref"]) in nt_english
    ]
    if not selected:
        return {
            "nt_english_checked": "0",
            "nt_english_support_family": "0",
            "nt_english_softens_family": "0",
            "nt_english_mixed": "0",
            "nt_english_signals": "",
            "nt_english_recommendation": "",
        }

    alignments = []
    signals = []
    recommendations = []
    for row in selected:
        for key in ("lsb_alignment", "esv_alignment", "kjv_alignment"):
            value = (row.get(key) or "").strip()
            if value and value != "not_checked":
                alignments.append(value)
        for key in ("lsb_signal", "esv_signal", "kjv_signal"):
            value = (row.get(key) or "").strip()
            if value and value != "no_issue":
                signals.append(value)
        recommendation = (row.get("consensus_recommendation") or "").strip()
        if recommendation:
            recommendations.append(recommendation)

    final_recommendation = ""
    for candidate in ("revise", "needs_logos", "defer", "keep"):
        if candidate in recommendations:
            final_recommendation = candidate
            break

    return {
        "nt_english_checked": str(len(alignments)),
        "nt_english_support_family": str(sum(1 for value in alignments if value == "supports_greek_family")),
        "nt_english_softens_family": str(sum(1 for value in alignments if value == "softens_greek_family")),
        "nt_english_mixed": str(sum(1 for value in alignments if value == "mixed")),
        "nt_english_signals": ", ".join(sorted(dict.fromkeys(signals))),
        "nt_english_recommendation": final_recommendation,
    }


def build_rows(
    idiom_rows: list[dict[str, str]],
    outlier_refs: set[str],
    nt_map: dict[str, list[dict[str, str]]],
    nt_english: dict[tuple[str, str], dict[str, str]],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    review_rows: list[dict[str, str]] = []
    outlier_rows: list[dict[str, str]] = []
    for row in idiom_rows:
        family = row["family"]
        nt_rows = nt_map.get(family, [])
        if not nt_rows:
            continue
        refs = "; ".join(item["nt_ref"] for item in nt_rows)
        greek = " || ".join(f"{item['nt_ref']}: {item['nt_greek']}" for item in nt_rows)
        gloss = " || ".join(f"{item['nt_ref']}: {item['literal_gloss']}" for item in nt_rows)
        notes = " || ".join(f"{item['nt_ref']}: {item['note']}" for item in nt_rows)
        weight = str(max(int(item["weight"]) for item in nt_rows))
        enriched = dict(row)
        enriched["nt_parallel_refs"] = refs
        enriched["nt_parallel_greek"] = greek
        enriched["nt_parallel_gloss"] = gloss
        enriched["nt_parallel_notes"] = notes
        enriched["nt_parallel_count"] = str(len(nt_rows))
        enriched["nt_parallel_weight"] = weight
        enriched.update(summarize_nt_english(family, nt_rows, nt_english))
        review_rows.append(enriched)
        if row["ref"] in outlier_refs:
            outlier_rows.append(enriched)
    review_rows.sort(key=lambda row: (row["family"], row["book_name"], int(row["chapter"]), int(row["verse"])))
    outlier_rows.sort(key=lambda row: (row["family"], row["book_name"], int(row["chapter"]), int(row["verse"])))
    return review_rows, outlier_rows


def build_markdown(title: str, rows: list[dict[str, str]]) -> str:
    lines = [f"# {title}", "", f"Rows: {len(rows)}", ""]
    for row in rows:
        lines.extend(
            [
                f"## {row['ref']}",
                f"- family: `{row['family']}`",
                f"- dominant bucket: `{row.get('dominant_bucket', '[none]')}`",
                f"- current bucket: `{row.get('bucket', '[none]')}`",
                f"- fresh: {row['fresh_translation']}",
                f"- NT refs: {row['nt_parallel_refs']}",
                f"- NT Greek: {row['nt_parallel_greek']}",
                f"- NT gloss: {row['nt_parallel_gloss']}",
                f"- NT English witnesses: checked `{row.get('nt_english_checked', '0')}`, support `{row.get('nt_english_support_family', '0')}`, soften `{row.get('nt_english_softens_family', '0')}`, mixed `{row.get('nt_english_mixed', '0')}`",
                f"- NT English recommendation: `{row.get('nt_english_recommendation', '') or 'none'}`",
                "",
            ]
        )
    return "\n".join(lines).strip() + "\n"


def main() -> None:
    idiom_rows = load_csv(IDIOM_REVIEW_CSV)
    outlier_refs = {row["ref"] for row in load_csv(IDIOM_OUTLIERS_CSV)}
    nt_map = load_nt_parallels(NT_PARALLELS)
    nt_english = load_nt_english_observations(NT_ENGLISH_OBSERVATIONS)

    review_rows, outlier_rows = build_rows(idiom_rows, outlier_refs, nt_map, nt_english)

    write_csv(REVIEW_CSV, review_rows)
    write_csv(OUTLIERS_CSV, outlier_rows)
    REVIEW_MD.write_text(build_markdown("Fresh OT NT Idiom Review", review_rows), encoding="utf-8")
    OUTLIERS_MD.write_text(build_markdown("Fresh OT NT Idiom Outliers", outlier_rows), encoding="utf-8")

    diagnostics = {
        "families_with_nt_parallels": sorted(nt_map.keys()),
        "review_rows": len(review_rows),
        "outlier_rows": len(outlier_rows),
        "rows_with_nt_english_observations": sum(1 for row in review_rows if row.get("nt_english_checked") not in {"", "0"}),
        "review_markdown": str(REVIEW_MD),
        "review_csv": str(REVIEW_CSV),
        "outliers_markdown": str(OUTLIERS_MD),
        "outliers_csv": str(OUTLIERS_CSV),
    }
    DIAGNOSTICS.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2))


if __name__ == "__main__":
    main()
