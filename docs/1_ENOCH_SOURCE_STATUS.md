# 1 Enoch Source Status

1 Enoch is not currently part of the Greek deuterocanon source workspace.

## Current Local Source

- Local file: `data/raw/1_enoch_charles_1917.txt`
- Upstream: Project Gutenberg ebook 77935, `https://www.gutenberg.org/ebooks/77935`
- Text file checked: `https://www.gutenberg.org/cache/epub/77935/pg77935.txt`
- Verification date: 2026-05-22
- Status: public domain in the United States

This file is R. H. Charles's public-domain English translation, printed here as
historical witness material only. It is not a normalized Greek source row file.

The separate parser writes `data/raw/1_enoch/1_enoch_charles_witness.csv`,
`data/raw/1_enoch/source_manifest.json`, and
`output/enoch/1_enoch_witness_progress.md`. Use `make build-enoch-witness` to
refresh these witness artifacts.

The repo also now tracks `data/raw/1_enoch_charles_1912_djvu.txt`, the
public-domain Internet Archive OCR for R. H. Charles, *The Book of Enoch or
1 Enoch* (Oxford, 1912). This is a Greek-fragment audit source only. The OCR is
not source-grade Greek text until checked against page images or a cleaner
transcription.

## Textual Status

The local Charles/Oesterley introduction states that the full work survives in
Ethiopic, that the Ethiopic was translated from a Greek version, and that only
portions of that Greek version are extant. It also states that the work was
originally written in Hebrew or Aramaic, with Charles assigning some sections to
Aramaic and others to Hebrew, while noting that the exact Semitic source language
is difficult to decide.

The current book-intro row therefore treats 1 Enoch as ancient witness
literature related to Jude 14-15, not as a completed Greek deuterocanon
translation.

The Online Critical Pseudepigrapha introduction says its current 1 Enoch text
represents all extant Greek and Latin evidence, Aramaic fragments through
chapter 8, and one Ethiopic manuscript for the Book of Watchers and Parables.
That site is a comparison-source pointer for this workstream, not yet a
vendored source import.

The manifest records an OCP comparison inventory: Ethiopic Rylands Manuscript 23
(`p`), Greek fragments/witnesses including 7QEnoch, POxy2069, Chester Beatty
185, Vatican Greek 1809, Gizeh/Akhmim, Syncellus, and Jude 14-15, plus Aramaic
Qumran witnesses 4Q201-4Q212 and 4Q247.

OCP's copyright page distinguishes the words of extant manuscripts from the
tagged XML and reconstructed/eclectic texts. For this project, do not vendor OCP
tagging or reconstructed text unless the specific witness and usage terms are
checked first.

## Project Policy

Do not fold 1 Enoch into `data/raw/lxx_deuterocanon/deuterocanon_full.csv` unless
one of these exists:

- compatible Greek or Aramaic source rows for the material being translated, or
- a deliberately separate witness-appendix build that clearly labels Charles
  1917 as an English witness text rather than the translation base of the Greek
  Heritage Bible.

Until then, 1 Enoch belongs in source audit / appendix planning and the separate
witness workspace, not in the Greek deuterocanon Logos Bible output.

## Next Work

- Build a comparison layer against pinned Greek, Latin, Aramaic, and Ethiopic
  witness rows where public-domain or otherwise compatible source terms permit.
- Candidate public-domain Greek-fragment source: R. H. Charles, *The Book of
  Enoch or 1 Enoch* (Oxford, 1912), available through Internet Archive. The
  generated audit queue at
  `data/research/1_enoch_charles_1912_greek_ocr_audit.csv` flags 2,440
  Greek-heavy OCR lines for review, but those lines should not be treated as
  source-grade Greek rows without PDF/image verification or a cleaner
  transcription.
- Decide whether any printed appendix should use the full Charles witness or
  only the portions with extant Greek/Aramaic control.
- Keep Jude 14-15 and early Christian reception notes in the main Bible
  apparatus without implying that 1 Enoch is canonical Scripture in this edition.
