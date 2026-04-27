# OT Review Pass 251

Scope: Isaiah 39.

Changes:
- Supplied English articles and predicate support for heard-that clause, house/vessels/treasury phrase, far-land phrase, things/house/treasures phrase, days/house-things phrase, king/Babylonians phrase, and word-of-Lord predicate.
- Synced Isaiah 39:1 translation footnote trigger to the reviewed source form Babylon.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 39 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
