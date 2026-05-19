# Print Edition Backlog

## Compact Greek-Driven Concordance

Build a separate concordance artifact for possible placement at the back of the paper Bible.

Constraints:

- Keep it separate from the main print proof for now.
- Target a useful but compact size, with an initial hard cap around 30 pages.
- Do not make it a simple surface-English word index.
- Drive entries from the underlying Greek lemma/source word where possible.
- When one Greek word is rendered by multiple English terms, create an English listing for each rendering.
- Each English listing should include the full verse list for that Greek word/rendering pair, subject to later page-budget trimming.

Open design questions:

- Which Greek terms are worth including under a 30-page cap.
- Whether entries should be limited to high-value theological, textual, and repeated vocabulary.
- Whether OT LXX and NT TR terms should be merged when the Greek lemma is the same, or marked by testament/source stream.
- Whether names, divine titles, and common particles should be excluded by default.
- Whether verse lists should use LXX numbering only, or also include familiar English/MT equivalents for major divergence points.

Implementation notes:

- Current verse source rows include Greek text, transliteration, literal gloss, syntax notes, and draft translation.
- Current verse source rows do not include Greek lemmas, morphology, or word-level Greek-to-English alignment.
- A useful concordance should therefore start from a curated term table rather than automatic surface-token grouping alone.
- Proposed term table fields: English heading, Greek lemma/source word, Greek forms to match, testament/source stream, priority, include/exclude flag, and compact note.
- The generator should emit a separate preview artifact first, then measure page count before any appendix is added to the main print proof.
- First pass should favor high-value theological and repeated vocabulary over exhaustive coverage.
