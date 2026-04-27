# OT Review Pass 246

Scope: Isaiah 34.

Changes:
- Supplied English articles and predicate support for earth/world/people wording, wrath/nations clause, mountains phrase, book/stars/vine/fig-tree imagery, people-of-destruction wording, sword/sacrifice phrasing, mighty/rams/bulls/land/blood wording, day/year clause, measuring-cord phrase, and hedgehog/earth phrase.
- Synced stale Isaiah 34 name forms in translation footnote triggers and source wording: Greek Idumea now renders as Edom, and Greek Bosor now renders as Bozrah.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 34 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
