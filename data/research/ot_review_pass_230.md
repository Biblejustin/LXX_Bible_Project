# OT Review Pass 230

Scope: Isaiah 17:1-14; 18:1-7.

Changes:
- Supplied English articles and predicate support for Damascus, Ephraim, Syrians, Jacob, harvest/ear/ravine, olive berries, people groups, harvest imagery, plunder/inheritance, Ethiopia rivers, nations/people, trumpet imagery, harvest branches, birds/beasts, and Zion-place phrases.
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 17-18 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
