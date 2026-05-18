# The Greek Heritage Study Bible

Fresh translation workspace for Greek-to-English OT/NT polish behind The Greek
Heritage Study Bible, using:

- OT LXX Greek source rows and NT Scrivener 1894 Textus Receptus Greek source rows
- Logos-based lexical and apparatus review
- phrase-level decision tracking
- publishable footnote drafting

## Branch Focus

- Scripture received here as inerrant, word-for-word inspired in original writings.
- Fresh translation aims to work from Greek source text directly instead of reusing older English wording.
- Deuterocanonical LXX books are kept in a separate source workspace/output, not folded into this Protestant-canon branch.
- Local Logos resources serve as research tools, while private notes stay private.
- This branch keeps fresh-translation outputs first; inherited study-bible variants are outside the current polish scope.

## Reader Disclaimer And Review Request

The project author is not a biblical scholar or a Koine Greek expert. This
project receives the original manuscripts of Scripture as without error, but
this working translation is not without error. There definitely are mistakes in
this translation, its notes, and its generated outputs.

Your help and attention in finding those mistakes are greatly appreciated. Be a
Berean, as in Acts 17:11: receive the work with care, but diligently inspect the
text and source evidence to see whether these things are correct.

## Build Requirements

- Python 3.11+.
- Runtime scripts are standard-library first.
- Optional PDF excerpt support for `scripts/build_study_bible.py` uses
  `reportlab`; test tooling uses `pytest`.
- Install local dependencies with:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

The legacy LaTeX output is written as `.tex`; compiling it requires a Unicode
LaTeX toolchain such as TeX Live with `xelatex`, `fontspec`, `geometry`,
`titlesec`, `fancyhdr`, `multicol`, `xcolor`, `parskip`, `hyperref`, and
standard system fonts such as Baskerville and Times New Roman.

## Documentation

- Editorial method: `METHODOLOGY.md`
- Canon and numbering policy: `docs/CANON_POLICY.md`
- Architecture/data flow: `docs/ARCHITECTURE.md`
- CSV/data dictionary: `docs/DATA_DICTIONARY.md`
- Contributor guide: `CONTRIBUTING.md`
- Source provenance and checksums: `SOURCE_PROVENANCE.md`
- Rights and license notices: `NOTICE.md` and `LICENSE`
- Translation rules: `data/research/translation_rules.md`
- Reader-facing conventions: `data/editorial_conventions.md`

## Quick Start

```bash
python -m pip install -r requirements.txt
make test
make build-fresh
```

`make build-fresh` refreshes the OT outputs, NT outputs, Logos-facing files,
combined OT/NT Markdown files, combined Logos DOCX files, and combined release
manifest/checksums. To rebuild only part of that set:

```bash
make build-ot
make build-nt
make build-combined
make build-combined-logos
make build-print-proof
make build-deuterocanon
make build-deuterocanon-logos
make release-combined
```

For a compact physical proofreading copy, run:

```bash
make build-print-proof
```

That target writes a single-column DOCX under `output/print/` with the combined
fresh translation, reviewed translation notes, source-occurrence name meanings,
book prefaces, and an LXX-to-English numbering guide.
It excludes Brenton/source supplemental notes, OpenBible fallback cross-references,
generated TSK cross-reference footnotes, and TSK study-note text.
Print footnotes use compact labels such as `T`, `Txt`, `MT/LXX`, `Heb`, `Gk`,
`Tr`, `Std`, `Src`, `Nm`, `Pn`, `Pl`, `Ppl`, `Div`, and `Eng`; the print front
matter includes the legend.

For a Lulu/POD upload proof that stays under common 800-page limits, run:

```bash
make build-print-proof-lulu-pandoc-pdf
```

That target includes the compact front matter and book preface pages, then writes
a Letter-size Pandoc/XeLaTeX PDF under `output/print/`.

For fast NT iteration without touching committed release outputs:

```bash
make build-nt-fast
make build-nt-book BOOK=Matthew
```

That target writes ignored artifacts under `output/working/`, lowers DOCX ZIP
compression, skips DOCX validation, and emits only the Logos Bible-source DOCX.
Use `make build-nt-book` for one-book review loops. Use `make build-nt` before
publishing.

For fast text-review validation without rebuilding aggregate Markdown or DOCX:

```bash
make review-ot-fast REFS="Isaiah 44:24-28" PASS=262 CHANGES="Reviewed final Isaiah 44 wording."
make review-nt-fast REFS="Matthew 1:1-5" PASS=120 CHANGES="Reviewed genealogy opening wording."
```

Use the fast review targets while editing. Use `make checkpoint-ot` at
chapter/book boundaries or before release output refreshes. Use
`make build-combined` after OT or NT source/output edits when the single-file
reader draft should be refreshed.

For the separate LXX deuterocanon/additions workspace, run:

```bash
make import-deuterocanon
make build-deuterocanon
make build-deuterocanon-logos
make validate-deuterocanon
make build-deuterocanon-book BOOK=Tobit
```

That imports the pinned eBible GRCLXX USFM archive, plus the public-domain
eBible Brenton Greek supplement for Prayer of Manasseh and true 2 Maccabees, into
`data/raw/lxx_deuterocanon/deuterocanon_full.csv` and writes separate review
artifacts and a progress dashboard under ignored `output/deuterocanon/`. The existing
GRCLXX rows, Greek Ezra B / 2 Esdras, Prayer of Manasseh, Greek Esther
Additions, and true 2 Maccabees are drafted and have received a first polish
pass. Continued proofreading remains separate from the source import.
Importer reruns preserve existing draft translations when the reference and
Greek source text still match.
The deuterocanon worksheet uses `--no-review-data` so pre-existing OT/NT note
tables do not appear as if they belong to this separate workspace. Use
`build-deuterocanon-book` for ignored one-book working outputs while reviewing
or polishing a single book. Use `validate-deuterocanon` before handoff when
only this workstream needs a focused rebuild and smoke check.
`build-deuterocanon-logos` writes a separate Logos DOCX under
`output/logos_deuterocanon/`. The compact print-proof targets do not include
the deuterocanon/additions rows.

If `make` is unavailable, run the commands listed in `Makefile` directly.

## Project Map

- `data/raw/` = pinned source archives and normalized source workspaces.
- `data/research/` = decisions, notes, review passes, and audit tables.
- `scripts/` = import, review, build, and release-hardening tools.
- `tests/` = smoke tests for source shape, pinned artifacts, and DOCX validity.
- `output/` = committed review/output artifacts plus ignored scratch area.
- `docs/` = architecture and data-format documentation.
- `release/` = release-candidate manifests and checksums.

## Reproducibility Checks

```bash
python -m compileall -q scripts
pytest -q
```

CI runs the same smoke checks in `.github/workflows/smoke.yml`.

## Branch Strategy

`fresh-translation-pilot` is the active working branch for complete fresh OT/NT
polish from Greek source text. The OT work translates the normalized LXX Greek
source workspace; the NT work translates the Scrivener 1894 Textus Receptus
stream. Future public release branches should describe their source-text pairing
and output target in the branch name; default branch naming can be normalized
separately when the project is ready for broader contributors.

## Current Outputs

- `RELEASE_STATUS.md`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_logos_bible.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_reference_notes.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_preview.md`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_proofreading.docx`
- `output/logos_greek_heritage/the_greek_heritage_study_bible_diagnostics.json`
- `output/logos_greek_heritage/README.md`
- `output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_logos_bible.docx`
- `output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_preview.md`
- `output/logos_deuterocanon/the_greek_heritage_study_bible_deuterocanon_diagnostics.json`
- `output/logos_deuterocanon/README.md`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof.docx`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof_diagnostics.json`
- `output/print/the_greek_heritage_study_bible_lulu_print_proof_pandoc_pdf_headers.json`
- `output/print/README_lulu.md`
- `output/print/cover/ghsb_draft_lulu_jacket_cover_26_625x11_75.pdf`
- `release/fresh-translation-ot-rc1/MANIFEST.md`
- `release/greek-heritage-study-bible-rc1/MANIFEST.md`

Other review reports, size sweeps, renderer experiments, cache files, and
intermediate Markdown worksheets are build byproducts. They are ignored unless a
future release explicitly promotes them back to reader-facing artifacts.

## Fresh Translation Workspace

Fresh Greek-to-English workspace for completed OT and NT drafts. Current work
focuses on polish, notes, Logos outputs, and validation.

Tracked source and research tables:

- `data/raw/lxx_greek/ot_full.csv`
- `data/raw/tr_greek/nt_full.csv`
- `data/research/logos_notes.csv`
- `data/research/translation_decisions.csv`
- `data/research/translation_footnotes.csv`
- `data/research/variant_notes.csv`
- `data/research/translation_rules.md`
- `data/research/logos_translation_stack.json`

Safe local-only space:

- `data/research/local/`
- `data/private/`
- `data/raw/private/`

Build full fresh outputs:

```bash
make build-fresh
```

Build Logos/import and proofreading DOCX files:

```bash
make build-ot
make build-nt
```

Scoped day-to-day workflow:

```bash
python scripts/build_fresh_translation.py \
  --source data/raw/lxx_greek/ot_full.csv \
  --book Exodus \
  --chapter-start 32 \
  --chapter-end 34 \
  --skip-undrafted \
  --output output/working/exodus_32_34.md \
  --translation-only-output output/working/exodus_32_34_translation_only.md \
  --diagnostics output/working/exodus_32_34_diagnostics.json

python scripts/build_fresh_vs_brenton_compare.py \
  --source data/raw/lxx_greek/ot_full.csv \
  --book Exodus \
  --chapter-start 32 \
  --chapter-end 34 \
  --min-importance medium \
  --output output/working/exodus_32_34_compare.md \
  --csv-output output/working/exodus_32_34_compare.csv \
  --diagnostics output/working/exodus_32_34_compare_diagnostics.json
```

One-command scoped review pack:

```bash
python scripts/run_translation_review.py \
  --book Deuteronomy \
  --chapter-start 3 \
  --chapter-end 5 \
  --min-importance medium
```

This writes:

- `output/working/deuteronomy_3_5.md`
- `output/working/deuteronomy_3_5_translation_only.md`
- `output/working/deuteronomy_3_5_compare.md`
- `output/working/deuteronomy_3_5_compare.csv`

OT book-checkpoint rebuild:

```bash
python scripts/run_book_checkpoint.py
```

This enforces contextual proper-name decisions, syncs support notes, refreshes
proper-name note coverage, and rebuilds ignored checkpoint artifacts under
`output/`.

Priority-review suite:

```bash
python scripts/run_priority_review_suite.py
```

This rebuilds ignored review reports, queues, watchlists, and hardening samples
under `output/`, plus local-only witness observations under
`data/research/local/`.

Existing OT release-candidate package:

- `RELEASE_STATUS.md`
- `release/fresh-translation-ot-rc1/MANIFEST.md`
- `release/fresh-translation-ot-rc1/CHECKSUMS.sha256`
- `release/greek-heritage-study-bible-rc1/MANIFEST.md`
- `release/greek-heritage-study-bible-rc1/CHECKSUMS.sha256`

Private witness matrix:

```bash
python scripts/build_private_witness_matrix.py
```

Private English witness worksheet for NETS / LES / SAAS:

```bash
python scripts/build_private_english_witness_observations.py
```

This writes:

- `data/research/local/witness_review/english_witness_observations.csv`
- `data/research/local/witness_review/english_witness_observations_README.md`

Use short alignment notes only.
Do not store long copyrighted text.

Private NT English witness worksheet for LSB / ESV / KJV:

```bash
python scripts/build_private_nt_english_witness_observations.py
```

This writes:

- `data/research/local/witness_review/nt_english_witness_observations.csv`
- `data/research/local/witness_review/nt_english_witness_observations_README.md`

Use this to record whether NT English witnesses preserve or smooth the Greek idiom-family behind OT rows with NT reuse or NT-linked wording.
Do not store long copyrighted text.

Private Logos-local observation worksheet:

```bash
python scripts/build_private_logos_local_observations.py
```

This writes:

- `data/research/local/witness_review/logos_local_observations.csv`
- `data/research/local/witness_review/logos_local_observations_README.md`

Use short derived observations from local Logos tools such as Bible Word Study, Factbook, and local index/state inspection.
Do not store copyrighted book text.

Public Logos-local review summary:

```bash
python scripts/build_logos_local_review.py
```

This writes:

- ignored Logos-local review/watch artifacts under `output/`

Proper-name watch:

```bash
python scripts/build_proper_name_watch.py
```

This writes:

- `data/research/local/proper_name_review/proper_name_candidates.csv`

Use this for normalizing Greekized OT names toward familiar MT-based English forms, while keeping meaning notes in notes rather than main-text spellings.

Apply approved proper-name normalizations:

```bash
python scripts/apply_contextual_proper_name_decisions.py --dry-run
python scripts/apply_contextual_proper_name_decisions.py --summary-only
python scripts/apply_proper_name_decisions.py --dry-run
python scripts/apply_proper_name_decisions.py --rebuild-watch
python scripts/apply_proper_name_decisions.py --forms "Ierousalem,Roboam" --rebuild-watch
python scripts/apply_proper_name_decisions.py --checkpoint
```

Contextual decisions read:

- `data/research/contextual_proper_name_decisions.csv`

Bulk candidate decisions read:

- `data/research/local/proper_name_review/proper_name_candidates.csv`

And writes private summaries:

- `data/research/local/proper_name_review/last_apply_summary.json`
- `data/research/local/proper_name_review/last_apply_summary.md`

Apply witness decisions back into source:

```bash
python scripts/apply_witness_decisions.py --dry-run
python scripts/apply_witness_decisions.py --rebuild-scoped
```

This reads:

- `data/research/local/witness_review/ot_witness_matrix.csv`

And writes private summaries:

- `data/research/local/witness_review/last_apply_summary.json`
- `data/research/local/witness_review/last_apply_summary.md`

Optional:

- `--refs "Genesis 1:2,Exodus 20:24"` = apply only chosen rows
- `--checkpoint` = rebuild full OT outputs after apply

Recommended rhythm:

- polish OT source in `data/raw/lxx_greek/ot_full.csv`
- polish NT source in `data/raw/tr_greek/nt_full.csv`
- rebuild scoped working files while polishing
- refresh committed full outputs and Logos files before release-facing commits
- commit full outputs at coherent checkpoints, not every small wording pass

Scan local Logos library into ignored private outputs:

```bash
python scripts/scan_logos_library.py
```

This produces:

- `data/research/local/logos_scan/logos_resources_all.csv`
- `data/research/local/logos_scan/logos_translation_resources.csv`
- `data/research/local/logos_scan/logos_scan_summary.json`

Options:

```bash
# scan a specific Logos account
python scripts/scan_logos_library.py --account fuwvxxd2.2xq

# merge all Logos accounts into one union inventory
python scripts/scan_logos_library.py --all-accounts --output-dir data/research/local/logos_scan_merged
```

Merged output adds account metadata columns:

- `account`
- `account_ids`
- `account_count`
- `resource_locations`

Private scanner output goes under:

- `data/research/local/logos_scan/`

Local Logos state inspection:

```bash
# inspect one account
python scripts/inspect_logos_local_state.py --account fuwvxxd2.2xq

# inspect every account
python scripts/inspect_logos_local_state.py --all-accounts --output-dir data/research/local/logos_state_merged
```

This writes:

- `data/research/local/logos_state/accounts.csv`
- `data/research/local/logos_state/recent_history.csv`
- `data/research/local/logos_state/layout_panels.csv`
- `data/research/local/logos_state/file_signatures.csv`
- `data/research/local/logos_state/summary.json`

Local Logos index query:

```bash
python scripts/query_logos_local_index.py salvation --account fuwvxxd2.2xq
python scripts/query_logos_local_index.py σωτηρία --account fuwvxxd2.2xq
```

This queries:

- `AutoComplete.db` for terms, labels, descriptions, word senses, and entity references
- `milestones.db` for headword-to-resource matches
- `history.db` for recent matching search / factbook / word-study activity

## Data Sources in Repo

- `data/hebrew_top_vocab.csv`
- `data/greek_vocabulary.csv`
- `data/vocab_cleanup.csv`
- `data/preface_charts.md`
- `data/name_meanings_appendix.md`
- `data/proper_names.csv`
