# OT Review Pass 245

Scope: Isaiah 33.

Changes:
- Supplied English articles and predicate support for moth/garment imagery, nations phrase, heights phrase, wisdom/knowledge/piety clause, fear/covenant wording, Sharon/marsh phrase, strength/fire wording, nations/thorn phrase, far/near-ones phrase, ungodly/fire wording, way/body-part/judgment phrasing, cave/rock/water phrase, king/land wording, fear/scribes/counselors/counter phrase, despised-people/listener wording, city/rich-city/pegs phrase, ship/way clause, and sails/signal/lame-ones wording.
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 33 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
