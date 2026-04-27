# OT Review Pass 242

Scope: Isaiah 30:24-33.

Changes:
- Supplied English articles and predicate support for oxen/land/barley wording, mountain/hill water imagery, moon/sun/crushing/pain phrases, wrath/oracle/fire wording, ravine/neck/nations/face phrases, flute/God-of-Israel wording, glory/voice/arm/flame language, Assyrians/blow phrasing, hope/help wording, and deep-ravine/wrath comparison.
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 30:24-33 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
