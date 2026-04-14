# LXX_UKJV_bible

Study Bible build pipeline for a public-domain edition using:

- Brenton LXX Old Testament
- UKJV New Testament
- Extensive cross-reference and lexical footnote infrastructure

## Current Outputs

- `output/study_bible_prototype.md`
- `output/study_bible_prototype.tex`
- `output/build_diagnostics.json`

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
