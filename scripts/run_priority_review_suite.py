#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_script(script_name: str) -> None:
    script_path = ROOT / "scripts" / script_name
    subprocess.run([sys.executable, str(script_path)], check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.parse_args()

    run_script("build_private_nt_english_witness_observations.py")
    run_script("build_private_logos_local_observations.py")
    run_script("build_private_english_witness_observations.py")
    run_script("apply_logos_reading_list_export.py")
    run_script("build_priority_diff_review.py")
    run_script("build_priority_book_reviews.py")
    run_script("build_priority_theme_reviews.py")
    run_script("build_priority_review_queue.py")
    run_script("build_decision_review_queue.py")
    run_script("build_remap_queue.py")
    run_script("build_mt_lxx_review.py")
    run_script("build_idiom_consistency_review.py")
    run_script("build_nt_idiom_review.py")
    run_script("build_crossref_clue_review.py")
    run_script("build_human_review_gate.py")
    run_script("build_logos_local_review.py")
    run_script("build_english_witness_review.py")
    run_script("build_proper_name_watch.py")
    run_script("build_release_hardening_report.py")

    print(
        json.dumps(
            {
                "priority_review": str(ROOT / "output" / "fresh_vs_brenton_ot_priority_review.md"),
                "priority_top100": str(ROOT / "output" / "fresh_vs_brenton_ot_priority_top100.md"),
                "theme_overview": str(ROOT / "output" / "fresh_vs_brenton_ot_theme_overview.md"),
                "theme_index": str(ROOT / "output" / "priority_themes" / "index.md"),
                "book_index": str(ROOT / "output" / "priority_books" / "index.md"),
                "review_queue": str(ROOT / "output" / "fresh_vs_brenton_ot_review_queue.csv"),
                "review_queue_readme": str(ROOT / "output" / "fresh_vs_brenton_ot_review_queue.md"),
                "decision_queue": str(ROOT / "output" / "fresh_vs_brenton_ot_decision_queue.csv"),
                "decision_queue_readme": str(ROOT / "output" / "fresh_vs_brenton_ot_decision_queue.md"),
                "remap_queue": str(ROOT / "output" / "fresh_vs_brenton_ot_remap_queue.csv"),
                "remap_queue_readme": str(ROOT / "output" / "fresh_vs_brenton_ot_remap_queue.md"),
                "mt_lxx_review": str(ROOT / "output" / "fresh_vs_mt_brenton_ot_review.md"),
                "mt_lxx_review_csv": str(ROOT / "output" / "fresh_vs_mt_brenton_ot_review.csv"),
                "idiom_consistency_review": str(ROOT / "output" / "fresh_ot_idiom_consistency_review.md"),
                "idiom_consistency_review_csv": str(ROOT / "output" / "fresh_ot_idiom_consistency_review.csv"),
                "idiom_consistency_outliers": str(ROOT / "output" / "fresh_ot_idiom_consistency_outliers.md"),
                "idiom_consistency_outliers_csv": str(ROOT / "output" / "fresh_ot_idiom_consistency_outliers.csv"),
                "nt_idiom_review": str(ROOT / "output" / "fresh_ot_nt_idiom_review.md"),
                "nt_idiom_review_csv": str(ROOT / "output" / "fresh_ot_nt_idiom_review.csv"),
                "nt_idiom_outliers": str(ROOT / "output" / "fresh_ot_nt_idiom_outliers.md"),
                "nt_idiom_outliers_csv": str(ROOT / "output" / "fresh_ot_nt_idiom_outliers.csv"),
                "nt_english_witness_observations": str(ROOT / "data" / "research" / "local" / "witness_review" / "nt_english_witness_observations.csv"),
                "crossref_clues": str(ROOT / "output" / "fresh_ot_crossref_clues.md"),
                "crossref_clues_csv": str(ROOT / "output" / "fresh_ot_crossref_clues.csv"),
                "crossref_watch": str(ROOT / "output" / "fresh_ot_crossref_watch.md"),
                "crossref_watch_csv": str(ROOT / "output" / "fresh_ot_crossref_watch.csv"),
                "logos_local_observations": str(ROOT / "data" / "research" / "local" / "witness_review" / "logos_local_observations.csv"),
                "logos_local_review": str(ROOT / "output" / "fresh_ot_logos_local_review.md"),
                "logos_local_review_csv": str(ROOT / "output" / "fresh_ot_logos_local_review.csv"),
                "logos_local_watch": str(ROOT / "output" / "fresh_ot_logos_local_watch.md"),
                "logos_local_watch_csv": str(ROOT / "output" / "fresh_ot_logos_local_watch.csv"),
                "english_witness_review": str(ROOT / "output" / "fresh_ot_english_witness_review.md"),
                "english_witness_review_csv": str(ROOT / "output" / "fresh_ot_english_witness_review.csv"),
                "english_witness_watch": str(ROOT / "output" / "fresh_ot_english_witness_watch.md"),
                "english_witness_watch_csv": str(ROOT / "output" / "fresh_ot_english_witness_watch.csv"),
                "same_as_mt": str(ROOT / "output" / "fresh_same_as_mt_differs_from_brenton.md"),
                "same_as_mt_csv": str(ROOT / "output" / "fresh_same_as_mt_differs_from_brenton.csv"),
                "mt_leaning": str(ROOT / "output" / "fresh_mt_leaning_vs_brenton.md"),
                "mt_leaning_csv": str(ROOT / "output" / "fresh_mt_leaning_vs_brenton.csv"),
                "differs_from_both": str(ROOT / "output" / "fresh_differs_from_mt_and_brenton.md"),
                "differs_from_both_csv": str(ROOT / "output" / "fresh_differs_from_mt_and_brenton.csv"),
                "human_review_core": str(ROOT / "output" / "fresh_human_review_core.md"),
                "human_review_phase1": str(ROOT / "output" / "fresh_human_review_phase1.md"),
                "human_review_mt_watch": str(ROOT / "output" / "fresh_human_review_mt_watch.md"),
                "human_review_nt_watch": str(ROOT / "output" / "fresh_human_review_nt_watch.md"),
                "proper_name_watch": str(ROOT / "output" / "fresh_ot_proper_name_watch.md"),
                "proper_name_watch_csv": str(ROOT / "output" / "fresh_ot_proper_name_watch.csv"),
                "release_hardening_report": str(ROOT / "output" / "release_hardening_report.md"),
                "release_hardening_report_json": str(ROOT / "output" / "release_hardening_report.json"),
                "release_hardening_samples": str(ROOT / "output" / "release_hardening_samples.csv"),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
