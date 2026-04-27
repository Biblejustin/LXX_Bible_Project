# OT Review Pass 225

Scope: Isaiah 7:2-25; 8:1-23.

Changes:
- Supplied English articles for named-location phrases, sign/oracle phrases, and geographic phrases.
- Clarified Isaiah 7:14 as "have a child in the womb" to express the Greek have-in-womb idiom without dropping womb language.
- Smoothed difficult literal fragments in Isaiah 7:17, 8:10, 8:15, and 8:16 while preserving source relationships.
- Synced matching translation footnotes and added decision rows for each reviewed phrase.

Validation:
- CSV shape check passed for OT source, translation footnotes, and translation decisions.
- Targeted Isaiah string, footnote-sync, and decision-coverage checks passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke 19 tests.
