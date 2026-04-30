# Contributing

This project is text-sensitive. Small wording changes can affect translation,
notes, diagnostics, and generated Logos files.

## Before Editing

1. Read `METHODOLOGY.md`.
2. Check source provenance in `SOURCE_PROVENANCE.md`.
3. Use `docs/DATA_DICTIONARY.md` before editing CSV files.
4. Keep private or copyrighted research in ignored local paths.

## Text Accuracy Reports

Include:

- Reference, such as `Ruth 1:4`.
- Current wording.
- Proposed wording.
- Source-text reason.
- Witnesses consulted.
- Whether the change affects notes, names, cross-references, or versification.

Do not submit long excerpts from copyrighted works. Summarize the issue instead.

## Cross-Reference Suggestions

Include:

- Source verse.
- Suggested target verse.
- Reason for the link.
- Whether it is lexical, thematic, quoted/alluded, name/place, or theological.

Large cross-reference sets should stay filtered. The Logos Personal Book output
is intended to be readable, not an unbounded TSK dump.

## Build And Test

```bash
python -m pip install -r requirements.txt
python -m compileall -q scripts
pytest -q
```

Use `make test` if `make` is available.

## Generated Outputs

Generated outputs are committed when they are part of the audit trail or release
workflow. If a text change affects generated files, rebuild and commit the
matching diagnostics.

Scratch work belongs under `output/working/`.

## Pull Request Standard

Every PR should state:

- Scope of books/chapters changed.
- Source or review basis.
- Generated outputs rebuilt.
- Tests run.
- Known unresolved review rows.
