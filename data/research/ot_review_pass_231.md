# OT Review Pass 231

Scope: Isaiah 19:1-25; 20:1-6.

Changes:
- Supplied English articles and predicate support for Egypt, Egyptians, river/sea imagery, textile work, Zoan/Memphis rulers, wandering spirit, Jews/Egyptians, altar/sign/savior-man, Assyrians, and Isaiah sign-act phrases.
- Synced translation footnote triggers with source wording, including existing drift on Zoan/Tanis and Sargon/Arna.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 19-20 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
