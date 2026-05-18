# Architecture

This repository has two related pipelines:

- Fresh translation pipeline for OT LXX and NT TR source work.
- Legacy public-domain study-Bible prototype tooling.

The fresh translation pipeline is active. The legacy `scripts/build_study_bible.py`
path remains available, but new work should prefer the fresh translation scripts.

## Data Flow

```text
raw source archives/files
  -> import scripts
  -> normalized CSV workspaces
  -> review/decision scripts
  -> generated Markdown, DOCX, diagnostics, and release manifests
```

## Main Source Workspaces

| Path | Purpose |
| --- | --- |
| `data/raw/lxx_greek/ot_full.csv` | OT LXX fresh translation workspace |
| `data/raw/lxx_deuterocanon/deuterocanon_full.csv` | Separate LXX deuterocanon/additions Greek source workspace |
| `data/raw/tr_greek/nt_full.csv` | NT Scrivener TR fresh translation workspace with UKJV witness columns |
| `data/research/translation_decisions.csv` | Phrase and verse decisions used by the fresh output pipeline |
| `data/research/translation_footnotes.csv` | Public translation footnotes |
| `data/research/variant_notes.csv` | Selective textual notes |
| `data/proper_name_transliteration_notes.csv` | Generated proper-name and place-name note data |
| `data/research/nt_review_pass_*.md` | NT review audit notes |
| `data/research/ot_review_pass_*.md` | OT review audit notes |

## Core Scripts

| Script | Role |
| --- | --- |
| `scripts/import_ot_from_utf8_lxx.py` | Imports OT LXX source data into normalized CSV form |
| `scripts/import_lxx_deuterocanon_from_grclxx.py` | Imports the separate eBible GRCLXX deuterocanon/additions source workspace |
| `scripts/import_nt_from_scrivener.py` | Imports Scrivener TR NT source files |
| `scripts/apply_witness_decisions.py` | Applies reviewed OT translation decisions |
| `scripts/apply_nt_tr_literal_revision.py` | Applies reviewed NT TR literal-translation decisions |
| `scripts/build_fresh_translation.py` | Builds Markdown worksheet and translation-only outputs |
| `scripts/build_combined_fresh_translation.py` | Builds combined OT/NT worksheet, translation-only Markdown, and diagnostics |
| `scripts/build_fresh_logos_bible.py` | Builds Logos Personal Book DOCX outputs and diagnostics |
| `scripts/build_nt_tr_vs_ukjv_review.py` | Builds NT TR-vs-UKJV review queues |
| `scripts/run_book_checkpoint.py` | Rebuilds consolidated OT checkpoint outputs |
| `scripts/run_priority_review_suite.py` | Rebuilds OT review, hardening, and release reports |

## Output Policy

Generated outputs under `output/` are intentionally committed when they are part
of the review trail, release package, or Logos import workflow. Scratch outputs
belong under `output/working/`, which is ignored.

Do not add a broad `output/` ignore rule unless the project stops using generated
artifacts as auditable review evidence.

## Build Cache

`scripts/build_fresh_logos_bible.py` caches expensive ingest results under
`output/working/cache/`, including TSK cross-reference groups, OpenBible
cross-references, and Brenton USFM footnotes. Cache keys use source-file size and
mtime plus `INGEST_CACHE_VERSION`; bump that version when parser semantics
change. Cache state is intentionally omitted from generated diagnostics so
tracked outputs stay deterministic. Set `FRESH_BIBLE_DISABLE_CACHE=1` to force
uncached ingest.

`make build-nt-fast` is the ignored working-output loop for NT polish. It
keeps the same source/review steps, writes generated files under
`output/working/`, lowers DOCX compression, skips DOCX validation, and emits only
the Logos Bible-source DOCX. It is for iteration only; release artifacts still
come from `make build-nt`.

`make build-combined` refreshes the single-file OT/NT Markdown outputs from the
current OT LXX and NT TR source CSVs. `make build-fresh` runs `make build-ot`,
`make build-nt`, and `make build-combined` in order when all committed fresh
translation outputs should be synchronized.

## Print PDF Cross-References

The active Lulu/Pandoc print PDF uses two LaTeX footnote streams. Translation,
textual, divine-name, and name-meaning notes remain numeric. Cross-references are
split by `scripts/pandoc_split_xrefs.lua` and emitted through a separate
manyfoot stream keyed by the visible verse number in red. The verse-number label
is intentional: it is self-documenting on the page, avoids alphabetic rollover
problems on dense pages, and lets readers distinguish cross-references from
translation notes without relying on a post-PDF overlay.

`make import-deuterocanon` refreshes the separate deuterocanon/additions source
workspace from the pinned eBible GRCLXX archive plus the pinned public-domain
eBible Brenton Greek supplement for Prayer of Manasseh and true 2 Maccabees.
The primary GRCLXX import also includes Greek Ezra B / 2 Esdras as a broad-EO
appendix stream without touching `ot_full.csv`. `make build-deuterocanon` additionally writes
isolated review artifacts and a progress dashboard under `output/deuterocanon/`;
it passes
`--no-review-data` so the shared OT/NT note tables are not counted as
deuterocanon review material.
`make build-deuterocanon-book BOOK=Tobit` writes scoped working artifacts under
`output/working/deuterocanon_book/` for one-book review or polish loops.
`make validate-deuterocanon` rebuilds that separate workspace, runs script
compilation, CSV shape checks, `git diff --check`, and the focused
deuterocanon smoke test.

`make build-nt-book BOOK=Matthew` narrows that loop to one NT book and writes
ignored outputs under `output/working/nt_book/` and
`output/working/logos_nt_book/`. It still refreshes the generated NT source CSV
first so script-level wording changes are reflected before the scoped build.

## Fast Review Checkpoint

Daily translation review should use the scoped fast checkpoint, not aggregate
output rebuilds:

```bash
make review-ot-fast REFS="Isaiah 44:24-28" PASS=262 CHANGES="Reviewed final Isaiah 44 wording."
make review-nt-fast REFS="Matthew 1:1-5" PASS=120 CHANGES="Reviewed genealogy opening wording."
```

This path:

- syncs translation-comparison footnote triggers for the reviewed refs;
- adds full-verse reviewed phrase guards;
- checks CSV shape for source, footnotes, decisions, and guards;
- verifies footnote/source trigger sync for the reviewed refs;
- runs focused smoke tests;
- updates the review-pass validation block automatically.

It deliberately skips aggregate Markdown, Logos DOCX, and full diagnostics. Run
`make checkpoint-ot` for OT chapter/book boundaries and `make build-nt` before
NT release-facing commits that need generated output or Logos DOCX refreshes.
Run `make build-combined` after either testament changes when the single-file
OT/NT Markdown outputs need to be current, or `make build-fresh` when all
committed fresh outputs need a full refresh.

## Private Research Boundary

Private or copyrighted local material must stay in ignored paths:

- `data/private/`
- `data/raw/private/`
- `data/research/local/`

Public outputs should use original analysis, public-domain witnesses, or short
derived/paraphrased observations.

## Refactor Direction

`scripts/build_study_bible.py` is monolithic. If active work returns to that
legacy prototype, split it in stages:

1. Move data records into typed models.
2. Move source parsing into parser modules.
3. Move cross-reference and note processing into processors.
4. Move Markdown/LaTeX/PDF generation into renderers.
5. Add unit tests around each extracted module before changing behavior.

Do not do this refactor in the same branch as translation-text changes unless
the output diffs are intentionally reviewed.
