# LXX Deuterocanon Source Workspace

This directory is the separate workspace for deuterocanonical and Greek-addition
work. It is intentionally not part of `data/raw/lxx_greek/ot_full.csv` and does
not feed the current 66-book Greek Heritage Study Bible outputs.

Active files:

- `grclxx_usfm.zip` - pinned eBible GRCLXX Septuaginta USFM source archive.
- `grcbrent_usfm.zip` - pinned public-domain eBible Brenton Greek Septuagint
  supplement used for Prayer of Manasseh and true 2 Maccabees.
- `deuterocanon_full.csv` - normalized Greek source rows for the separate
  deuterocanon/additions workstream; includes Greek Ezra B / 2 Esdras for
  broad-EO appendix coverage, and all imported rows are drafted.
- `source_manifest.json` - source URL, status, checksums, import policy, and
  import diagnostics.
- `../../../docs/DEUTEROCANON_MISSING_SOURCES.md` - checked source candidates and
  final supplemental-source choice for Prayer of Manasseh and 2 Maccabees.
- `../../../docs/DEUTEROCANON_PENDING_DECISIONS.md` - resolved decisions and
  remaining review notes for source scope and Greek Esther handling.

Common commands:

```bash
python scripts/import_lxx_deuterocanon_from_grclxx.py
make build-deuterocanon
make validate-deuterocanon
```

Use `--refresh-source` only when intentionally re-pinning the upstream archive.
The `draft_translation` column starts blank on first import; later importer
reruns preserve existing draft rows when the reference and Greek source text
still match. Use `--reset-drafts` only when intentionally rebuilding a blank
source workspace. Any source-package descriptors or footnotes are preserved in
`syntax_notes`.
