# OT Review Pass 257

Scope: Isaiah 42:14-25.

Changes:
- Supplied English articles and predicate support for birthing-woman simile, marshes clause, darkness/crooked-things phrase, trusting/carved/molten participles, deaf/blind participles, blind/ruling participle phrase, ears phrase, justified/magnify phrase, snare/storerooms/rescuing/saying phrase, coming-things phrase, spoiling participle phrase, and anger/burning/soul phrase.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 42:14-25 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
