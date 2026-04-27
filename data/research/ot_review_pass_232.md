# OT Review Pass 232

Scope: Isaiah 21:1-17; 22:1-25.

Changes:
- Supplied English articles and predicate support for wilderness/storm, Elamites/Persians, watchman/riders, Edom/Seir, Tema/Kedar, Zion valley, city/rulers/valleys, gates/houses/citadel/pool, Shebna, tomb/memorial/dwelling, robe/crown/stewardship, David glory, and Eliakim throne imagery.
- Synced translation footnote triggers with source wording, including existing drift on Edom/Idumea and Sobna/Shebna.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 21-22 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
