# LXX Bible Project

Study Bible build pipeline for public-domain editions using:

- Brenton LXX Old Testament
- UKJV New Testament
- TSK cross-references
- lexical + name + intro-page apparatus

## Download PDF

- [Download current Brenton + UKJV PDF](output/Brenton_UKJV_study_bible_prototype.pdf)

## Why This Project

- Scripture received here as inerrant, word-for-word inspired in original writings.
- Edition gives deliberate weight to older Septuagintal and other early witnesses.
- Complete Greek biblical codices and earlier LXX fragments place major LXX witness history more than a millennium earlier than the standard complete Masoretic codex base used in many printed Hebrew Bibles.
- Dead Sea Scroll evidence shows earlier Hebrew textual plurality before medieval Masoretic stabilization.
- Many New Testament quotations align more closely with Septuagintal or other non-Masoretic forms than with later medieval Masoretic wording.
- This edition also pays special attention to passages where later textual standardization can affect christological, supernatural, or angelological readings, including texts such as Genesis 6.

## Current Outputs

- `output/Brenton_UKJV_study_bible_prototype.pdf`
- `output/Brenton_UKJV_study_bible_prototype.md`
- `output/Brenton_UKJV_study_bible_prototype.tex`
- `output/Brenton_UKJV_study_bible_prototype_diagnostics.json`
- `output/Brenton_UKJV_study_bible_prototype_overflow_report.json`

## Build

```bash
python3 scripts/build_study_bible.py
```

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

Scan local Logos library into ignored private outputs:

```bash
python3 scripts/scan_logos_library.py
```

This produces:

- `output/fresh_translation_genesis_1_3_pilot.md`
- `output/fresh_translation_genesis_1_3_pilot_diagnostics.json`

Private scanner output goes under:

- `data/research/local/logos_scan/`

## Data Sources in Repo

- `data/hebrew_top_vocab.csv`
- `data/greek_vocabulary.csv`
- `data/vocab_cleanup.csv`
- `data/preface_charts.md`
- `data/name_meanings_appendix.md`
- `data/proper_names.csv`
