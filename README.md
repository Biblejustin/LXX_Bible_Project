# LXX Bible Project

Study Bible build pipeline for public-domain editions using:

- Brenton LXX Old Testament
- UKJV New Testament
- TSK cross-references
- lexical + name + intro-page apparatus

## Download PDF

- [Download current Brenton + UKJV PDF](output/Brenton_UKJV_study_bible_prototype.pdf)

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
