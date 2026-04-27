# OT Review Pass 247

Scope: Isaiah 35.

Changes:
- Supplied English articles and predicate support for wilderness/lily wording, deserts/glory/honor/height phrase, loosened-hands phrase, ears/deaf phrase, lame-one/tongue/ravine/land wording, dry-place/thirsty-land wording, way/unclean/scattered phrases, lion/evil-beasts wording, and eternal-gladness clause.
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 35 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
