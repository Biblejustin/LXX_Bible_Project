# OT Review Pass 252

Scope: Isaiah 40:1-17.

Changes:
- Supplied English articles and predicate support for paths-of-God phrase, crooked/rough wording, salvation-of-God phrase, glory/flower/grass phrase, grass/flower phrase, high-mountain/good-news participle, arm/wage/work phrase, shepherd/womb phrase, water/mountains/glens phrase, mind-of-Lord phrase, way-of-understanding phrase, nations/drop/bucket/scales phrase, Lebanon/animals/offering phrase, and nations phrase.
- Reordered Isaiah 40:9 high-mountain imperative for readable English without changing the reviewed source vocabulary.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 40:1-17 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
