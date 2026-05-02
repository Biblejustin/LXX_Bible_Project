# LXX Deuterocanon Source Workspace

This directory is the separate workspace for deuterocanonical and Greek-addition
work. It is intentionally not part of `data/raw/lxx_greek/ot_full.csv` and does
not feed the current 66-book Greek Heritage Study Bible outputs.

Active files:

- `grclxx_usfm.zip` - pinned eBible GRCLXX Septuaginta USFM source archive.
- `deuterocanon_full.csv` - normalized Greek source rows for the separate
  deuterocanon/additions workstream.
- `source_manifest.json` - source URL, status, checksums, import policy, and
  import diagnostics.

Import command:

```bash
python scripts/import_lxx_deuterocanon_from_grclxx.py
```

Use `--refresh-source` only when intentionally re-pinning the upstream archive.
The `draft_translation` column is intentionally blank until fresh translation
work begins book by book. Any source-package descriptors or footnotes are
preserved in `syntax_notes`.
