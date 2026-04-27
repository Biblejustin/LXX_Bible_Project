# OT Review Pass 240

Scope: Isaiah 30:1-12.

Changes:
- Supplied English articles and predicate support for Egyptians wording, Pharaoh shelter/reproach language, people/nation phrases, wilderness vision imagery, lion/cub wording, book wording, disobedient-people clause, and prophets phrase.
- Synced stale Isaiah 30:4 translation-footnote trigger back to the source rendering "Zoan."
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 30:1-12 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
