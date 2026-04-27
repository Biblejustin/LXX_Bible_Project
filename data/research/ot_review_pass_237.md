# OT Review Pass 237

Scope: Isaiah 28:16-29.

Changes:
- Supplied English articles and predicate support for the cornerstone/believer line, storm/covenant/hope language, mountain-of-the-ungodly and bitterness phrases, completed-things wording, plowman/day/ground phrases, judgment-of-God language, black-cumin/wheel/wagon/cumin/rod wording, voice-of-bitterness language, and wonders wording.
- Preserved the NT-quoted cornerstone wording in Isaiah 28:16 while making the English article structure readable.
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 28:16-29 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
