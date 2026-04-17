#!/usr/bin/env python3
import argparse
import csv
import json
import re
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / "data" / "research" / "local" / "witness_review"

EXPORT_CSV = LOCAL / "logos_reading_list_export.csv"
OBSERVATIONS_CSV = LOCAL / "english_witness_observations.csv"
ALIGNMENT_REVIEW_CSV = LOCAL / "logos_reading_list_alignment_review.csv"
DIAGNOSTICS_JSON = LOCAL / "logos_reading_list_alignment_diagnostics.json"

ALIGNMENT_FIELDS = {
    "nets_alignment": "nets_primary_texts",
    "les_alignment": "les",
}
SIGNAL_FIELDS = {
    "nets_signal": "nets_primary_texts",
    "les_signal": "les",
}


def load_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def normalize(text: str) -> str:
    text = (text or "").lower()
    text = text.replace("’", "").replace("'", "")
    text = text.replace("“", " ").replace("”", " ").replace("–", "-")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def similarity_metrics(left: str, right: str) -> dict[str, float]:
    left_norm = normalize(left)
    right_norm = normalize(right)
    left_tokens = set(left_norm.split())
    right_tokens = set(right_norm.split())
    if not left_tokens or not right_tokens:
        return {
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "sequence": 0.0,
            "combo": 0.0,
        }
    overlap = len(left_tokens & right_tokens)
    precision = overlap / len(left_tokens)
    recall = overlap / len(right_tokens)
    f1 = (2 * precision * recall / (precision + recall)) if precision + recall else 0.0
    sequence = SequenceMatcher(None, left_norm, right_norm).ratio()
    combo = 0.75 * f1 + 0.25 * sequence
    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "sequence": sequence,
        "combo": combo,
    }


def classify_alignment(witness_text: str, observation_row: dict[str, str]) -> tuple[str, str, dict[str, dict[str, float]]]:
    candidates = {
        "agrees_fresh": observation_row.get("fresh_translation", ""),
        "agrees_brenton": observation_row.get("brenton_translation", ""),
        "agrees_mt": observation_row.get("mt_translation", ""),
    }
    metrics = {
        label: similarity_metrics(witness_text, target)
        for label, target in candidates.items()
        if (target or "").strip()
    }
    if not metrics:
        return "", "", {}

    ranked = sorted(metrics.items(), key=lambda item: item[1]["combo"], reverse=True)
    best_label, best = ranked[0]
    second_combo = ranked[1][1]["combo"] if len(ranked) > 1 else 0.0
    fresh_metrics = metrics.get("agrees_fresh", {"precision": 0.0, "recall": 0.0, "combo": 0.0})

    if len(metrics) == 1:
        if best["combo"] >= 0.70:
            alignment = best_label
        else:
            alignment = ""
    elif best["combo"] < 0.56:
        alignment = "differs_all"
    elif best["combo"] - second_combo < 0.04:
        alignment = "split_or_mixed"
    elif best_label == "agrees_fresh" and best["recall"] < 0.45:
        alignment = "split_or_mixed"
    elif best_label in {"agrees_brenton", "agrees_mt"} and best["recall"] < 0.45 and best["precision"] < 0.80:
        alignment = "split_or_mixed"
    else:
        alignment = best_label

    if not alignment:
        signal = ""
    elif alignment == "agrees_fresh":
        signal = "no_issue"
    elif alignment == "agrees_mt":
        signal = "mt_leaning"
    elif alignment == "agrees_brenton":
        if fresh_metrics["precision"] >= 0.85 and fresh_metrics["recall"] <= 0.25:
            signal = "lxx_plus"
        else:
            signal = "smoothing_issue"
    else:
        if fresh_metrics["precision"] >= 0.85 and fresh_metrics["recall"] <= 0.25:
            signal = "lxx_plus"
        else:
            signal = "unclear"

    return alignment, signal, metrics


def consensus_for_row(row: dict[str, str]) -> str:
    alignments = []
    for field in ("les_alignment", "nets_alignment", "saas_alignment"):
        value = (row.get(field) or "").strip()
        if value and value != "not_checked":
            alignments.append(value)
    if len(alignments) < 2:
        return ""

    fresh = sum(1 for value in alignments if value == "agrees_fresh")
    brenton = sum(1 for value in alignments if value == "agrees_brenton")
    mt = sum(1 for value in alignments if value == "agrees_mt")
    differs = sum(1 for value in alignments if value == "differs_all")
    split = sum(1 for value in alignments if value == "split_or_mixed")

    if fresh >= 2 and brenton == 0 and mt == 0 and differs == 0:
        return "keep"
    if fresh >= 2 and differs == 0 and split <= 1 and brenton + mt == 0:
        return "keep"
    if fresh == 0 and brenton + mt >= 2:
        return "needs_logos"
    if differs >= 2 or split >= 2:
        return "needs_logos"
    if brenton + mt >= 2 and fresh <= 1:
        return "needs_logos"
    return ""


def add_note(existing: str, note: str) -> str:
    existing = (existing or "").strip()
    if not existing:
        return note
    if note in existing:
        return existing
    return f"{existing}; {note}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply parsed Logos reading-list export to english witness observations.")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    export_rows = load_rows(EXPORT_CSV)
    observation_rows = load_rows(OBSERVATIONS_CSV)
    export_by_ref = {row["ref"]: row for row in export_rows if row.get("ref")}

    review_rows: list[dict[str, str]] = []
    updated_rows = 0
    imported_field_updates = 0
    matched_refs = 0
    unmatched_refs = sorted(ref for ref in export_by_ref if ref not in {row["ref"] for row in observation_rows})
    consensus_counter: Counter[str] = Counter()

    for row in observation_rows:
        export_row = export_by_ref.get(row["ref"])
        if not export_row:
            continue
        matched_refs += 1
        changed = False
        review_row = {"ref": row["ref"]}

        for alignment_field, export_field in ALIGNMENT_FIELDS.items():
            signal_field = alignment_field.replace("_alignment", "_signal")
            witness_text = (export_row.get(export_field) or "").strip()
            if not witness_text:
                review_row[alignment_field] = ""
                review_row[signal_field] = ""
                review_row[f"{alignment_field}_best"] = ""
                continue

            alignment, signal, metrics = classify_alignment(witness_text, row)
            if args.overwrite or not (row.get(alignment_field) or "").strip():
                row[alignment_field] = alignment
                changed = True
                imported_field_updates += 1
            if args.overwrite or not (row.get(signal_field) or "").strip():
                row[signal_field] = signal
                changed = True
                imported_field_updates += 1

            best_label = ""
            best_combo = 0.0
            if metrics:
                best_label, best_combo = max(
                    ((label, values["combo"]) for label, values in metrics.items()),
                    key=lambda item: item[1],
                )
            review_row[alignment_field] = alignment
            review_row[signal_field] = signal
            review_row[f"{alignment_field}_best"] = f"{best_label}:{best_combo:.3f}" if best_label else ""
            for label, values in metrics.items():
                prefix = alignment_field.replace("_alignment", "")
                review_row[f"{prefix}_{label}_combo"] = f"{values['combo']:.3f}"
                review_row[f"{prefix}_{label}_recall"] = f"{values['recall']:.3f}"

        new_consensus = consensus_for_row(row)
        if new_consensus:
            consensus_counter[new_consensus] += 1
            if args.overwrite or not (row.get("consensus_recommendation") or "").strip():
                row["consensus_recommendation"] = new_consensus
                changed = True
        review_row["consensus_recommendation"] = new_consensus

        if changed:
            row["reviewer_notes"] = add_note(row.get("reviewer_notes", ""), "auto_import=logos_reading_list_export")
            updated_rows += 1
        review_rows.append(review_row)

    fieldnames = list(observation_rows[0].keys()) if observation_rows else []
    if observation_rows:
        write_rows(OBSERVATIONS_CSV, observation_rows, fieldnames)

    review_fieldnames = [
        "ref",
        "nets_alignment",
        "nets_signal",
        "nets_alignment_best",
        "nets_agrees_fresh_combo",
        "nets_agrees_brenton_combo",
        "nets_agrees_mt_combo",
        "nets_agrees_fresh_recall",
        "les_alignment",
        "les_signal",
        "les_alignment_best",
        "les_agrees_fresh_combo",
        "les_agrees_brenton_combo",
        "les_agrees_mt_combo",
        "les_agrees_fresh_recall",
        "consensus_recommendation",
    ]
    write_rows(ALIGNMENT_REVIEW_CSV, review_rows, review_fieldnames)

    diagnostics = {
        "export_csv": str(EXPORT_CSV),
        "observations_csv": str(OBSERVATIONS_CSV),
        "alignment_review_csv": str(ALIGNMENT_REVIEW_CSV),
        "export_rows": len(export_rows),
        "unique_export_refs": len(export_by_ref),
        "matched_observation_refs": matched_refs,
        "unmatched_export_refs": len(unmatched_refs),
        "updated_rows": updated_rows,
        "updated_fields": imported_field_updates,
        "consensus_counts": dict(consensus_counter),
        "unmatched_export_ref_examples": unmatched_refs[:20],
    }
    DIAGNOSTICS_JSON.write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print(json.dumps(diagnostics, indent=2))


if __name__ == "__main__":
    main()
