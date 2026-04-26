# LXX Bible Project

Fresh-translation pilot branch for Greek-to-English work using:

- Greek source text
- Logos-based lexical and apparatus review
- phrase-level decision tracking
- publishable footnote drafting

## Branch Focus

- Scripture received here as inerrant, word-for-word inspired in original writings.
- Fresh translation aims to work from Greek source text directly instead of reusing older English wording.
- Local Logos resources serve as research tools, while private notes stay private.
- This branch removes inherited study-bible output artifacts and keeps only fresh-translation outputs.

## Reader Disclaimer And Review Request

The project author is not a biblical scholar or a Koine Greek expert. This
project receives the original manuscripts of Scripture as without error, but
this working translation is not without error. There definitely are mistakes in
this translation, its notes, and its generated outputs.

Your help and attention in finding those mistakes are greatly appreciated. Be a
Berean, as in Acts 17:11: receive the work with care, but diligently inspect the
text and source evidence to see whether these things are correct.

## Build Requirements

- Python 3.11+.
- Runtime scripts are standard-library first.
- Optional PDF excerpt support for `scripts/build_study_bible.py` uses
  `reportlab`; test tooling uses `pytest`.
- Install local dependencies with:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

The legacy LaTeX output is written as `.tex`; compiling it requires a Unicode
LaTeX toolchain such as TeX Live with `xelatex`, `fontspec`, `geometry`,
`titlesec`, `fancyhdr`, `multicol`, `xcolor`, `parskip`, `hyperref`, and
standard system fonts such as Baskerville and Times New Roman.

## Documentation

- Editorial method: `METHODOLOGY.md`
- Architecture/data flow: `docs/ARCHITECTURE.md`
- CSV/data dictionary: `docs/DATA_DICTIONARY.md`
- Contributor guide: `CONTRIBUTING.md`
- Source provenance and checksums: `SOURCE_PROVENANCE.md`
- Rights and license notices: `NOTICE.md` and `LICENSE`
- Translation rules: `data/research/translation_rules.md`
- Reader-facing conventions: `data/editorial_conventions.md`

## Quick Start

```bash
python3 -m pip install -r requirements.txt
make test
make build-nt
```

For fast NT iteration without touching committed release outputs:

```bash
make build-nt-fast
```

That target writes ignored artifacts under `output/working/`, lowers DOCX ZIP
compression, and skips DOCX validation. Use `make build-nt` before publishing.

If `make` is unavailable, run the commands listed in `Makefile` directly.

## Project Map

- `data/raw/` = pinned source archives and normalized source workspaces.
- `data/research/` = decisions, notes, review passes, and audit tables.
- `scripts/` = import, review, build, and release-hardening tools.
- `tests/` = smoke tests for source shape, pinned artifacts, and DOCX validity.
- `output/` = committed review/output artifacts plus ignored scratch area.
- `docs/` = architecture and data-format documentation.
- `release/` = release-candidate manifests and checksums.

## Reproducibility Checks

```bash
python3 -m compileall -q scripts
pytest -q
```

CI runs the same smoke checks in `.github/workflows/smoke.yml`.

## Branch Strategy

`fresh-translation-pilot` is the active working branch for the new Greek-source
translation pipeline. Future public release branches should describe their
source-text pairing and output target in the branch name; default branch naming
can be normalized separately when the project is ready for broader contributors.

## Current Outputs

- `RELEASE_STATUS.md`
- `output/fresh_translation_ot_full.md`
- `output/fresh_translation_ot_full_translation_only.md`
- `output/fresh_translation_nt_tr_full.md`
- `output/fresh_translation_nt_tr_translation_only.md`
- `output/fresh_vs_brenton_ot_drafted.md`
- `output/fresh_vs_brenton_ot_priority_review.md`
- `output/fresh_nt_tr_vs_ukjv_priority_review.md`
- `output/fresh_vs_brenton_ot_theme_overview.md`
- `output/fresh_vs_mt_brenton_ot_review.md`
- `output/fresh_mt_leaning_vs_brenton.md`
- `output/fresh_human_review_phase1.md`
- `output/fresh_human_review_core.md`
- `output/release_hardening_report.md`
- `output/logos/fresh_translation_ot_logos_bible.docx`
- `output/logos/fresh_translation_ot_proofreading.docx`
- `output/logos/fresh_translation_ot_logos_bible_diagnostics.json`
- `output/logos_nt/fresh_translation_nt_tr_logos_bible.docx`
- `output/logos_nt/fresh_translation_nt_tr_proofreading.docx`
- `output/logos_nt/fresh_translation_nt_tr_diagnostics.json`
- `release/fresh-translation-ot-rc1/MANIFEST.md`

## Fresh Translation Pilot

Fresh Greek-to-English pilot workspace now scaffolded for a new translation that does not copy existing English versions.

Tracked research tables:

- `data/research/logos_notes.csv`
- `data/research/translation_decisions.csv`
- `data/research/translation_footnotes.csv`
- `data/research/variant_notes.csv`
- `data/research/translation_rules.md`
- `data/research/logos_translation_stack.json`
- `data/research/genesis_1_3_workflow.md`
- `data/raw/lxx_greek/genesis_1_3_pilot.csv`

Safe local-only space:

- `data/research/local/`
- `data/private/`
- `data/raw/private/`

Build pilot worksheet:

```bash
python3 scripts/build_fresh_translation.py
```

Build Logos/import and proofreading DOCX files:

```bash
python3 scripts/build_fresh_logos_bible.py
```

Scoped day-to-day workflow:

```bash
python3 scripts/build_fresh_translation.py \
  --source data/raw/lxx_greek/ot_full.csv \
  --book Exodus \
  --chapter-start 32 \
  --chapter-end 34 \
  --skip-undrafted \
  --output output/working/exodus_32_34.md \
  --translation-only-output output/working/exodus_32_34_translation_only.md \
  --diagnostics output/working/exodus_32_34_diagnostics.json

python3 scripts/build_fresh_vs_brenton_compare.py \
  --source data/raw/lxx_greek/ot_full.csv \
  --book Exodus \
  --chapter-start 32 \
  --chapter-end 34 \
  --min-importance medium \
  --output output/working/exodus_32_34_compare.md \
  --csv-output output/working/exodus_32_34_compare.csv \
  --diagnostics output/working/exodus_32_34_compare_diagnostics.json
```

One-command scoped review pack:

```bash
python3 scripts/run_translation_review.py \
  --book Deuteronomy \
  --chapter-start 3 \
  --chapter-end 5 \
  --min-importance medium
```

This writes:

- `output/working/deuteronomy_3_5.md`
- `output/working/deuteronomy_3_5_translation_only.md`
- `output/working/deuteronomy_3_5_compare.md`
- `output/working/deuteronomy_3_5_compare.csv`

Book-checkpoint rebuild:

```bash
python3 scripts/run_book_checkpoint.py
```

This enforces contextual proper-name decisions, syncs support notes, refreshes proper-name note coverage, and rebuilds consolidated outputs:

- `output/fresh_translation_ot_full.md`
- `output/fresh_translation_ot_full_translation_only.md`
- `output/fresh_vs_brenton_ot_drafted.md`
- `output/fresh_vs_brenton_ot_drafted.csv`

Priority-review suite:

```bash
python3 scripts/run_priority_review_suite.py
```

This rebuilds:

- `output/fresh_vs_brenton_ot_priority_review.md`
- `output/fresh_vs_brenton_ot_priority_top100.md`
- `output/priority_books/index.md`
- `output/fresh_vs_brenton_ot_theme_overview.md`
- `output/priority_themes/index.md`
- `output/fresh_vs_brenton_ot_review_queue.csv`
- `output/fresh_vs_brenton_ot_review_queue.md`
- `output/fresh_vs_brenton_ot_decision_queue.csv`
- `output/fresh_vs_brenton_ot_decision_queue.md`
- `output/fresh_vs_mt_brenton_ot_review.md`
- `output/fresh_same_as_mt_differs_from_brenton.md`
- `output/fresh_mt_leaning_vs_brenton.md`
- `output/fresh_differs_from_mt_and_brenton.md`
- `output/fresh_ot_idiom_consistency_review.md`
- `output/fresh_ot_idiom_consistency_outliers.md`
- `output/fresh_ot_nt_idiom_review.md`
- `output/fresh_ot_nt_idiom_outliers.md`
- `output/fresh_ot_crossref_clues.md`
- `output/fresh_ot_crossref_watch.md`
- `output/fresh_ot_logos_local_review.md`
- `output/fresh_ot_logos_local_watch.md`
- `data/research/local/witness_review/nt_english_witness_observations.csv`
- `data/research/local/witness_review/logos_local_observations.csv`
- `output/fresh_ot_english_witness_review.md`
- `output/fresh_ot_english_witness_watch.md`
- `output/fresh_ot_proper_name_watch.md`
- `output/fresh_human_review_phase1.md`
- `output/fresh_human_review_core.md`
- `output/fresh_human_review_mt_watch.md`
- `output/fresh_human_review_nt_watch.md`
- `output/release_hardening_report.md`
- `output/release_hardening_report.json`
- `output/release_hardening_samples.csv`

Release-candidate package:

- `RELEASE_STATUS.md`
- `release/fresh-translation-ot-rc1/MANIFEST.md`
- `release/fresh-translation-ot-rc1/CHECKSUMS.sha256`

Private witness matrix:

```bash
python3 scripts/build_private_witness_matrix.py
```

Private English witness worksheet for NETS / LES / SAAS:

```bash
python3 scripts/build_private_english_witness_observations.py
```

This writes:

- `data/research/local/witness_review/english_witness_observations.csv`
- `data/research/local/witness_review/english_witness_observations_README.md`

Use short alignment notes only.
Do not store long copyrighted text.

Private NT English witness worksheet for LSB / ESV / KJV:

```bash
python3 scripts/build_private_nt_english_witness_observations.py
```

This writes:

- `data/research/local/witness_review/nt_english_witness_observations.csv`
- `data/research/local/witness_review/nt_english_witness_observations_README.md`

Use this to record whether NT English witnesses preserve or smooth the Greek idiom-family behind OT rows with NT reuse or NT-linked wording.
Do not store long copyrighted text.

Private Logos-local observation worksheet:

```bash
python3 scripts/build_private_logos_local_observations.py
```

This writes:

- `data/research/local/witness_review/logos_local_observations.csv`
- `data/research/local/witness_review/logos_local_observations_README.md`

Use short derived observations from local Logos tools such as Bible Word Study, Factbook, and local index/state inspection.
Do not store copyrighted book text.

Public Logos-local review summary:

```bash
python3 scripts/build_logos_local_review.py
```

This writes:

- `output/fresh_ot_logos_local_review.md`
- `output/fresh_ot_logos_local_review.csv`
- `output/fresh_ot_logos_local_watch.md`
- `output/fresh_ot_logos_local_watch.csv`

Proper-name watch:

```bash
python3 scripts/build_proper_name_watch.py
```

This writes:

- `output/fresh_ot_proper_name_watch.md`
- `output/fresh_ot_proper_name_watch.csv`
- `data/research/local/proper_name_review/proper_name_candidates.csv`

Use this for normalizing Greekized OT names toward familiar MT-based English forms, while keeping meaning notes in notes rather than main-text spellings.

Apply approved proper-name normalizations:

```bash
python3 scripts/apply_contextual_proper_name_decisions.py --dry-run
python3 scripts/apply_contextual_proper_name_decisions.py --summary-only
python3 scripts/apply_proper_name_decisions.py --dry-run
python3 scripts/apply_proper_name_decisions.py --rebuild-watch
python3 scripts/apply_proper_name_decisions.py --forms "Ierousalem,Roboam" --rebuild-watch
python3 scripts/apply_proper_name_decisions.py --checkpoint
```

Contextual decisions read:

- `data/research/contextual_proper_name_decisions.csv`

Bulk candidate decisions read:

- `data/research/local/proper_name_review/proper_name_candidates.csv`

And writes private summaries:

- `data/research/local/proper_name_review/last_apply_summary.json`
- `data/research/local/proper_name_review/last_apply_summary.md`

Apply witness decisions back into source:

```bash
python3 scripts/apply_witness_decisions.py --dry-run
python3 scripts/apply_witness_decisions.py --rebuild-scoped
```

This reads:

- `data/research/local/witness_review/ot_witness_matrix.csv`

And writes private summaries:

- `data/research/local/witness_review/last_apply_summary.json`
- `data/research/local/witness_review/last_apply_summary.md`

Optional:

- `--refs "Genesis 1:2,Exodus 20:24"` = apply only chosen rows
- `--checkpoint` = rebuild full OT outputs after apply

Recommended rhythm:

- draft in `data/raw/lxx_greek/ot_full.csv`
- rebuild scoped working files while drafting
- rebuild full OT outputs only at book checkpoints
- commit full outputs at checkpoint, not every chapter

Scan local Logos library into ignored private outputs:

```bash
python3 scripts/scan_logos_library.py
```

This produces:

- `data/research/local/logos_scan/logos_resources_all.csv`
- `data/research/local/logos_scan/logos_translation_resources.csv`
- `data/research/local/logos_scan/logos_scan_summary.json`

Options:

```bash
# scan a specific Logos account
python3 scripts/scan_logos_library.py --account fuwvxxd2.2xq

# merge all Logos accounts into one union inventory
python3 scripts/scan_logos_library.py --all-accounts --output-dir data/research/local/logos_scan_merged
```

Merged output adds account metadata columns:

- `account`
- `account_ids`
- `account_count`
- `resource_locations`

Private scanner output goes under:

- `data/research/local/logos_scan/`

Local Logos state inspection:

```bash
# inspect one account
python3 scripts/inspect_logos_local_state.py --account fuwvxxd2.2xq

# inspect every account
python3 scripts/inspect_logos_local_state.py --all-accounts --output-dir data/research/local/logos_state_merged
```

This writes:

- `data/research/local/logos_state/accounts.csv`
- `data/research/local/logos_state/recent_history.csv`
- `data/research/local/logos_state/layout_panels.csv`
- `data/research/local/logos_state/file_signatures.csv`
- `data/research/local/logos_state/summary.json`

Local Logos index query:

```bash
python3 scripts/query_logos_local_index.py salvation --account fuwvxxd2.2xq
python3 scripts/query_logos_local_index.py σωτηρία --account fuwvxxd2.2xq
```

This queries:

- `AutoComplete.db` for terms, labels, descriptions, word senses, and entity references
- `milestones.db` for headword-to-resource matches
- `history.db` for recent matching search / factbook / word-study activity

## Data Sources in Repo

- `data/hebrew_top_vocab.csv`
- `data/greek_vocabulary.csv`
- `data/vocab_cleanup.csv`
- `data/preface_charts.md`
- `data/name_meanings_appendix.md`
- `data/proper_names.csv`
