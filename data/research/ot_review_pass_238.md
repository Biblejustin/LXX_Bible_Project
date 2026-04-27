# OT Review Pass 238

Scope: Isaiah 29:1-12.

Changes:
- Supplied English articles and predicate support for Ariel strength/wealth wording, palisade language, earth/ground phrases, dust-from-wheel imagery, visitation/voice/storm/flame phrases, wealth-of-nations wording, sleep/dream/thirsty-man language, spirit-of-stupor wording, sealed-book language, and literate/illiterate man phrases.
- Kept Isaiah 29:13 and following for separate review because Isaiah 29:13 is NT-quoted.
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 29:1-12 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
