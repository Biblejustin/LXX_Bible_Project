# Textus Receptus Greek NT Source

Source: Scrivener 1894 Textus Receptus text-only files from byztxt/greektext-scrivener.

- Upstream: <https://github.com/byztxt/greektext-scrivener>
- Pinned commit: `6049a43b135ed870f843b83eb6a04764fc796678`
- License notice from upstream README: `Public Domain. Copy freely.`
- Imported CSV: `data/raw/tr_greek/nt_full.csv`
- Source manifest: `data/raw/tr_greek/source_manifest.json`

Import notes:

- Upstream files use an ASCII Greek encoding. The importer preserves that source string in `transliteration` and converts it to unaccented Unicode Greek in `greek_text`.
- Downloaded SCV files are normalized to LF line endings with trailing source-line whitespace trimmed.
- `ukjv_translation` preserves the public-domain UKJV as a witness column.
- `draft_translation` is a working TR literal draft after `scripts/apply_nt_tr_literal_revision.py`; UKJV should be checked against it, not used as final wording.
- `literal_gloss` and `syntax_notes` are intentionally blank until verse-level TR review fills them.

Import counts:

- Rows: 7957
- Books: 27
- UKJV witness rows: 7957
- Missing UKJV seed rows: 0
