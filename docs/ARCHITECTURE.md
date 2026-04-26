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
| `data/raw/tr_greek/nt_full.csv` | NT Scrivener TR fresh translation workspace with UKJV witness columns |
| `data/research/translation_decisions.csv` | Phrase and verse decisions used by the OT pipeline |
| `data/research/translation_footnotes.csv` | Public translation footnotes |
| `data/research/variant_notes.csv` | Selective textual notes |
| `data/proper_name_transliteration_notes.csv` | Generated proper-name and place-name note data |
| `data/research/nt_review_pass_*.md` | NT review audit notes |
| `data/research/ot_review_pass_*.md` | OT review audit notes |

## Core Scripts

| Script | Role |
| --- | --- |
| `scripts/import_ot_from_utf8_lxx.py` | Imports OT LXX source data into normalized CSV form |
| `scripts/import_nt_from_scrivener.py` | Imports Scrivener TR NT source files |
| `scripts/apply_witness_decisions.py` | Applies reviewed OT translation decisions |
| `scripts/apply_nt_tr_literal_revision.py` | Applies reviewed NT TR literal-translation decisions |
| `scripts/build_fresh_translation.py` | Builds Markdown worksheet and translation-only outputs |
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

`make build-nt-fast` is the ignored working-output loop for NT development. It
keeps the same source/review steps, writes generated files under
`output/working/`, lowers DOCX compression, skips DOCX validation, and emits only
the Logos Bible-source DOCX. It is for iteration only; release artifacts still
come from `make build-nt`.

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
