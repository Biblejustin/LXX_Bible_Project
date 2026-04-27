# OT Review Pass 248

Scope: Isaiah 36.

Changes:
- Supplied English articles and predicate support for Hezekiah dating phrase, fortified-cities phrase, force/conduit/pool wording, great-king phrase, battle-line phrase, trusting-ones phrase, bargain/lord/king wording, governor-face/Egyptians phrase, men-on-wall phrase, men-sitting-on-wall phrase, great-voice/words/great-king wording, king/vine/figs phrase, land phrase, gods/nations phrase, Hamath/Arpad/Sepharvaim gods phrase, gods/God-of-Jerusalem phrase, answered-word phrase, and Shebna/scribe/tunics phrase.
- Synced stale Isaiah 36 translation footnote triggers from Somnas to the existing standard source rendering Shebna, and from Arphad to Arpad.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 36 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
