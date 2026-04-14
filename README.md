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

## Data Sources in Repo

- `data/hebrew_top_vocab.csv`
- `data/greek_vocabulary.csv`
- `data/vocab_cleanup.csv`
- `data/preface_charts.md`
- `data/name_meanings_appendix.md`
- `data/proper_names.csv`
