# Fresh Translation OT RC1 Manifest

Release candidate: `fresh-translation-ot-rc1`

Date prepared: 2026-04-30

This package is a lightweight manifest for the committed release artifacts. Large generated outputs remain in `output/` to avoid duplicating multi-megabyte files in git.

## Primary Reader Artifacts

- `output/fresh_translation_ot_full_translation_only.md`
- `output/fresh_translation_ot_full.md`

## Comparison And Review Artifacts

- `output/fresh_vs_brenton_ot_drafted.csv`
- `output/fresh_vs_brenton_ot_drafted.md`
- `output/fresh_vs_brenton_ot_priority_review.csv`
- `output/fresh_vs_brenton_ot_priority_review.md`
- `output/fresh_vs_mt_brenton_ot_review.csv`
- `output/fresh_vs_mt_brenton_ot_review.md`
- `output/fresh_human_review_core.csv`
- `output/fresh_human_review_core.md`
- `output/fresh_human_review_phase1.csv`
- `output/fresh_human_review_phase1.md`

## Release Verification Artifacts

- `output/release_hardening_report.md`
- `output/release_hardening_report.json`
- `output/release_hardening_samples.csv`

## Watch Queues Expected Empty

- `output/fresh_ot_crossref_watch.csv`
- `output/fresh_ot_english_witness_watch.csv`
- `output/fresh_human_review_mt_watch.csv`
- `output/fresh_human_review_nt_watch.csv`
- `output/fresh_ot_logos_local_watch.csv`
- `output/fresh_ot_proper_name_watch.csv`
- `output/fresh_vs_brenton_ot_remap_queue.csv`
- `output/fresh_vs_brenton_ot_final_unresolved.csv`

## Checksums

See `CHECKSUMS.sha256`.

## Rebuild

```bash
python3 scripts/run_book_checkpoint.py
python3 scripts/run_priority_review_suite.py
```
