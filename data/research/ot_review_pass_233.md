# OT Review Pass 233

Scope: Isaiah 23:1-18; 24:1-23.

Changes:
- Supplied English articles and predicate support for Tyre/Carthage/Kittim imagery, island dwellers, sea/trader/harvest language, Chaldeans/Assyrians, prostitute-song and marketplace phrases, inhabited-world judgment, social-role comparisons, law/covenant language, land/earth phrases, glory/islands/sea wording, and pit/snare/stronghold imagery.
- Clarified Isaiah 24:15 as vocative: "O Lord, the God of Israel."
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 23-24 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
