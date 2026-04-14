# LXX Bible Project

Study Bible build pipeline for public-domain editions using:

- LXX2012 Old Testament
- UKJV New Testament
- TSK cross-references
- lexical + name + intro-page apparatus

## Download PDF

- [Download current LXX2012 + UKJV PDF](output/LXX2012_UKJV_study_bible_prototype.pdf)

## Current Outputs

- `output/LXX2012_UKJV_study_bible_prototype.pdf`
- `output/LXX2012_UKJV_study_bible_prototype.md`
- `output/LXX2012_UKJV_study_bible_prototype.tex`
- `output/LXX2012_UKJV_study_bible_prototype_diagnostics.json`
- `output/LXX2012_UKJV_study_bible_prototype_overflow_report.json`

## Build

```bash
python3 scripts/build_study_bible.py --ot-source lxx2012
```

## Data Sources in Repo

- `data/hebrew_top_vocab.csv`
- `data/greek_vocabulary.csv`
- `data/vocab_cleanup.csv`
- `data/preface_charts.md`
- `data/name_meanings_appendix.md`
- `data/proper_names.csv`
