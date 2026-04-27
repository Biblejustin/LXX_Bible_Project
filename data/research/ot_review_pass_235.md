# OT Review Pass 235

Scope: Isaiah 27:1-13.

Changes:
- Supplied English articles and predicate support for sword/dragon/serpent imagery, vineyard/desire phrasing, strong-city and wall language, inhabited-world wording, harsh-spirit and anger-spirit phrasing, lawlessness/stones/altars/dust/forest language, abandoned-flock and pasture wording, maker/former participles, channel/river and sons-of-Israel phrases, and great-trumpet/Assyrians/holy-mountain language.
- Preserved the literal structure of difficult Isaiah 27 lines while making marked article phrases readable.
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 27 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
