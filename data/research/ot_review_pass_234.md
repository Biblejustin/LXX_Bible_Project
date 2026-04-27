# OT Review Pass 234

Scope: Isaiah 25:1-12; 26:1-21.

Changes:
- Supplied English articles and predicate support for mound/city language, poor-people and oppressed-cities phrases, helper/shelter wording, nations/counsel language, reproach/rest/Moabite/threshing-floor phrases, height/refuge/ground language, strong-city/wall wording, gates/people language, heights/strong-cities phrasing, earth/dwellers wording, dead/tombs/dew/resurrection language, anger-of-Lord wording, and holy-place/dwellers/earth phrases.
- Clarified repeated Isaiah 25-26 vocatives as "O Lord" / "O Lord our God."
- Synced translation footnote triggers with the reviewed source wording.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 25-26 footnote-sync checks passed.
- `python3 -m pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
