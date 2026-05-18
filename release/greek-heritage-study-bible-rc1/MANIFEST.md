# The Greek Heritage Study Bible RC1 Manifest

Release candidate: `greek-heritage-study-bible-rc1`

Date prepared: 2026-05-18

This package is a lightweight manifest for committed reader-facing artifacts for The Greek Heritage Study Bible. Iterative review reports, queue files, renderer scratch files, and size sweeps are reproducible build byproducts and are not tracked.

## Primary Reader Artifacts

- `output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_reference_notes.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_proofreading.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_diagnostics.json`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_preview.md`
- `output/logos_greek_heritage/README.md`
- `output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_logos_bible.docx`
- `output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_diagnostics.json`
- `output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_preview.md`
- `output/logos_deuterocanon/README.md`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof.docx`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof_diagnostics.json`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_pdf_headers.json`
- `output/print/README_lulu.md`
- `output/print/cover/ghsb_draft_lulu_jacket_cover_26_625x11_75.pdf`

## Scope

- OT source: `data/raw/lxx_greek/ot_full.csv`
- NT source: `data/raw/tr_greek/nt_full.csv`
- Reader draft: Genesis through Revelation, 66 books, plus separate LXX deuterocanon Logos workstream.
- Logos DOCX: compile `output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx` in Logos Personal Books as resource type `Bible`.
- Print proof: use `output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf` for the current full-size proof.

## Checksums

See `CHECKSUMS.sha256`.

## Rebuild

```bash
make build-combined-logos
make build-deuterocanon-logos
make build-print-proof-lulu-pandoc-pdf
```
