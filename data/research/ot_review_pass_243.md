# OT Review Pass 243

Scope: Isaiah 31.

Changes:
- Supplied English articles and predicate support for the woe/trusting construction, houses of evil men, Egyptian/horses/helpers clauses, lion/prey/mountains/multitude imagery, flying-birds wording, counseling-ones phrase, handmade-things material phrase, sword/young-men wording, and trench/rock/fleeing-one/household phrases.
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 31 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
