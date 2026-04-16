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

## Current Outputs

- `output/fresh_translation_ot_full.md`
- `output/fresh_translation_ot_full_translation_only.md`
- `output/fresh_vs_brenton_ot_drafted.md`
- `output/fresh_vs_brenton_ot_priority_review.md`
- `output/fresh_vs_brenton_ot_theme_overview.md`

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

This rebuilds consolidated outputs:

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

Private scanner output goes under:

- `data/research/local/logos_scan/`

## Data Sources in Repo

- `data/hebrew_top_vocab.csv`
- `data/greek_vocabulary.csv`
- `data/vocab_cleanup.csv`
- `data/preface_charts.md`
- `data/name_meanings_appendix.md`
- `data/proper_names.csv`
