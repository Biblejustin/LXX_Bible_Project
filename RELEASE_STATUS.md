# Release Status

Release candidate: `fresh-translation-ot-rc1`

Date prepared: 2026-04-30

Branch: `fresh-translation-pilot`

## Verdict

`PASS`: release-hardening checks found no blocking issues.

## Scope

- Fresh OT translation output from Genesis through Malachi.
- Greek source rows: `22,909`.
- Drafted translation rows: `22,909`.
- Book coverage: `39 / 39` books complete.
- Reader-facing committed outputs: current Logos DOCX files and current Lulu
  print-proof files.

Current workspace note: the NT TR fresh draft is complete in the source rows.
Combined Logos DOCX files are generated under `output/logos_greek_heritage/`.
The separate deuterocanon Logos DOCX is generated under
`output/logos_deuterocanon/`. The active print proof is generated under
`output/print/`. The combined OT/NT release package is cut at
`release/greek-heritage-study-bible-rc1/`.

## Verification Counts

- Raw OT rows: `22,909`.
- Drafted compare rows: `22,909`.
- Raw duplicate refs: `0`.
- Drafted duplicate refs: `0`.
- Missing draft translations: `0`.
- Watch/remap/final-unresolved rows: `0`.
- Active generated-output markers: `0`.
- Blocking text artifacts: `0`.
- Priority rows open: `0`.
- Deterministic sample audit rows: `117`.
- Deterministic sample artifact hits: `0`.

## Release Artifacts

The release package manifest is in:

- `release/fresh-translation-ot-rc1/MANIFEST.md`
- `release/fresh-translation-ot-rc1/CHECKSUMS.sha256`
- `release/greek-heritage-study-bible-rc1/MANIFEST.md`
- `release/greek-heritage-study-bible-rc1/CHECKSUMS.sha256`

Primary committed outputs:

- `output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_reference_notes.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_proofreading.docx`
- `output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_logos_bible.docx`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof.docx`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf`
- `output/print/cover/ghsb_draft_lulu_jacket_cover_26_625x11_75.pdf`

## Known Limitations

- This is an OT release candidate, not a final typeset publication.
- The compact print proof is a proofreading DOCX, not a final typeset print edition.
- `data/research/variant_notes.csv` has `0` non-blocking pending
  apparatus rows.
- Brenton comparison coverage has known missing rows where the upstream Brenton source lacks a matched row; the fresh OT draft itself is complete.
- Private Logos/local research data remains under `data/research/local/` and is intentionally not part of the public release package.
- A final human editorial read-through is still recommended before public publication.

## Rebuild Commands

```bash
python scripts/run_book_checkpoint.py
python scripts/run_priority_review_suite.py
make release-combined
```

The priority suite now includes the release-hardening report.
