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
- Reader-facing output: `output/fresh_translation_ot_full_translation_only.md`.
- Full worksheet output: `output/fresh_translation_ot_full.md`.

Current workspace note: the NT TR fresh draft is also complete in
`output/fresh_translation_nt_tr_full.md`,
`output/fresh_translation_nt_tr_translation_only.md`, and the `output/logos_nt/`
Logos files. This status file records the existing OT RC1 package only; a
combined OT/NT release package has not been cut.

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

Primary committed outputs:

- `output/fresh_translation_ot_full_translation_only.md`
- `output/fresh_translation_ot_full.md`
- `output/fresh_vs_brenton_ot_drafted.csv`
- `output/fresh_vs_brenton_ot_priority_review.csv`
- `output/fresh_human_review_core.csv`
- `output/fresh_human_review_phase1.csv`
- `output/release_hardening_report.md`
- `output/release_hardening_samples.csv`

## Known Limitations

- This is an OT release candidate, not a final typeset publication.
- The output is Markdown/CSV, not a formatted print or app edition.
- Brenton comparison coverage has known missing rows where the upstream Brenton source lacks a matched row; the fresh OT draft itself is complete.
- Private Logos/local research data remains under `data/research/local/` and is intentionally not part of the public release package.
- A final human editorial read-through is still recommended before public publication.

## Rebuild Commands

```bash
python3 scripts/run_book_checkpoint.py
python3 scripts/run_priority_review_suite.py
```

The priority suite now includes the release-hardening report.
