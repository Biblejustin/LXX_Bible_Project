# OT Review Pass 244

Scope: Isaiah 32.

Changes:
- Supplied English articles and possessive/predicate support for righteous-king wording, man/river/land phrase, ears phrase, weak-ones/stammering-tongues wording, fool/thirsty-souls wording, counsel/humble/words phrase, godly-men phrase, year/vintage/seed wording, loins/breasts/field/vine language, rich-city phrase, abandoned-houses/villages/joy wording, spirit/forest phrase, hail/forests wording, and ox/donkey phrase.
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 32 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
