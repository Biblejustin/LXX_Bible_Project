# OT Review Pass 236

Scope: Isaiah 28:1-15.

Changes:
- Supplied English articles and predicate support for crown/insolence and Ephraim drinker phrases, flower/glory/mountain language, wrath/force/earth wording, spirit-of-judgment language, priest/prophet/wine/drunkenness/vision phrases, message/weaned-one wording, hungry-one/rest phrasing, oracle-of-Lord-God language, direct-address wording, and covenant/storm/lie phrases.
- Kept Isaiah 28:16-29 for separate review because the cornerstone line is NT-quoted and should stay isolated.
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 28:1-15 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
