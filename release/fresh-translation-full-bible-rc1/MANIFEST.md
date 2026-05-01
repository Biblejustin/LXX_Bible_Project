# Fresh Translation Full Bible RC1 Manifest

Release candidate: `fresh-translation-full-bible-rc1`

Date prepared: 2026-04-30

This package is a lightweight manifest for the committed full OT/NT release artifacts. Large generated outputs remain in `output/` to avoid duplicating multi-megabyte files in git.

## Primary Reader Artifacts

- `output/fresh_translation_full_bible_translation_only.md`
- `output/fresh_translation_full_bible.md`
- `output/fresh_translation_full_bible_diagnostics.json`

## Logos Personal Book Artifacts

- `output/logos_full/fresh_translation_full_bible_logos_bible.docx`
- `output/logos_full/fresh_translation_full_bible_reference_notes.docx`
- `output/logos_full/fresh_translation_full_bible_proofreading.docx`
- `output/logos_full/fresh_translation_full_bible_diagnostics.json`
- `output/logos_full/fresh_translation_full_bible_preview.md`
- `output/logos_full/README.md`

## Release Verification Artifacts

- `output/release_hardening_report.md`
- `output/release_hardening_report.json`
- `output/release_hardening_samples.csv`

## Scope

- OT source: `data/raw/lxx_greek/ot_full.csv`
- NT source: `data/raw/tr_greek/nt_full.csv`
- Combined reader draft: Genesis through Revelation, 66 books.
- Combined Logos DOCX: compile `output/logos_full/fresh_translation_full_bible_logos_bible.docx` in Logos Personal Books as resource type `Bible`.

## Checksums

See `CHECKSUMS.sha256`.

## Rebuild

```bash
make release-combined
```
