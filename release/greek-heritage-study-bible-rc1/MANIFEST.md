# The Greek Heritage Study Bible RC1 Manifest

Release candidate: `greek-heritage-study-bible-rc1`

Date prepared: 2026-06-18

This package is a lightweight manifest for committed release artifacts for The Greek Heritage Study Bible. Large generated outputs remain in `output/` to avoid duplicating multi-megabyte files in git.

## Primary Reader Artifacts

- `output/the_greek_heritage_study_bible_translation_only.md`
- `output/the_greek_heritage_study_bible.md`
- `output/the_greek_heritage_study_bible_diagnostics.json`

## Logos Personal Book Artifacts

- `output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_reference_notes.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_proofreading.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_diagnostics.json`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_preview.md`
- `output/logos_greek_heritage/README.md`

## Separate Deuterocanon Artifacts

- `output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_logos_bible.docx`
- `output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_diagnostics.json`
- `output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_preview.md`
- `output/logos_deuterocanon/README.md`

## Print Proof Artifacts

- `output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof_diagnostics.json`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_pdf_headers.json`
- `output/print/README_lulu.md`
- `output/print/cover/ghsb_draft_lulu_jacket_cover_26_5x11_75.pdf`

## Release Verification Artifacts

- `output/release_hardening_report.md`
- `output/release_hardening_report.json`
- `output/release_hardening_samples.csv`

## Scope

- OT source: `data/raw/lxx_greek/ot_full.csv`
- NT source: `data/raw/tr_greek/nt_full.csv`
- Reader draft: Genesis through Revelation, 66 books.
- Logos DOCX: compile `output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx` in Logos Personal Books as resource type `Bible`.

## Checksums

See `CHECKSUMS.sha256`.

## Rebuild

```bash
make build-combined-logos
make build-deuterocanon-logos
make build-print-proof-lulu-pandoc-pdf
make release-combined
```
