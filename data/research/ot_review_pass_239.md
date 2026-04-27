# OT Review Pass 239

Scope: Isaiah 29:13-24.

Changes:
- Supplied English articles and predicate support for the NT-quoted lips phrase, wisdom/understanding language, deep/secret-counsel participles, clay/potter/formed/work phrases, Carmel/forest wording, deaf/book/blind/darkness/gloom language, poor/hopeless phrases, word/stumbling-block/gates/righteous-one wording, face language, God-of-Israel wording, and grumblers/stammering-tongues phrases.
- Preserved Isaiah 29:13 wording close to the Greek while restoring "their lips."
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 29:13-24 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
