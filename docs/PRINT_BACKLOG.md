# Print Edition Backlog

## Compact Greek-Driven Concordance

Build a separate concordance artifact for possible placement at the back of the paper Bible.

Constraints:

- Keep it separate from the main print proof for now.
- Target a useful but compact size, with an initial hard cap around 30 pages.
- Do not make it a simple surface-English word index.
- Drive entries from the underlying Greek lemma/source word where possible.
- When one Greek word is rendered by multiple English terms, create an English listing for each visible rendering.
- Keep the printed listing compact: rank references, cap each visible rendering, and omit filler notices about skipped references.

Open design questions:

- Which additional Greek terms are worth adding without pushing the broad preview past the 30-page cap.
- Whether the broad preview should continue suppressing low-value "other rendering" buckets or show a few of them in a later reference-only edition.
- Whether OT LXX and NT TR terms should be merged when the Greek lemma is the same, or marked by testament/source stream.
- Whether names, divine titles, and common particles should be excluded by default.
- Whether verse lists should use LXX numbering only, or also include familiar English/MT equivalents for major divergence points.

Implementation notes:

- Current verse source rows include Greek text, transliteration, literal gloss, syntax notes, and draft translation.
- Current verse source rows do not include Greek lemmas, morphology, or word-level Greek-to-English alignment.
- A useful concordance should therefore start from a curated term table rather than automatic surface-token grouping alone.
- Current compact seed table: `data/research/greek_concordance_terms.csv`.
- Current broad curated term list: `scripts/build_greek_concordance_preview.py` (`BROAD_TERMS`).
- Current generator: `make build-concordance-preview` for the small preview, or `make build-concordance-broad-preview` for the broader print candidate.
- Current broad preview artifact: `output/concordance/the_greek_heritage_study_bible_greek_concordance_broad_preview.md`.
- Current broad diagnostics: `output/concordance/the_greek_heritage_study_bible_greek_concordance_broad_preview_diagnostics.json`.
- The broad candidate includes high-frequency core terms but keeps them usable through per-rendering caps and reference ranking rather than full verse lists.
- The broad candidate suppresses "other rendering" buckets and omitted-reference notices to avoid filler in the printed appendix.
- Current broad preview status: 363 configured terms, 362 rendered terms, about 13,500 words, and an estimated 29.9 pages at 450 words per page.
- Current reference style uses print book abbreviations such as `Jer`, `Matt`, and `Rev`.
