# OT Review Pass 250

Scope: Isaiah 38.

Changes:
- Supplied English articles and predicate support for time phrase, wall phrase, true-heart/pleasing-things phrase, sign phrase, shadow/stair-steps/sun wording, prayer heading, height/days/years phrase, salvation/earth/man phrase, remnant/tent/weaver-web phrase, day/night phrase, swallow/dove phrase, pain/soul phrase, dead/living participles, psaltery/days/life phrase, cake-of-figs phrase, and closing sign phrase.
- Reworked the stair-step sign sentence so the shadow and sun movement read as one coherent English sentence while preserving the Greek sequence.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 38 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
