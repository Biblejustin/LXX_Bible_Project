# OT Review Pass 217: Song of Solomon 3 articles

Scope: Song of Solomon 3:2-5 and 3:7-11.

Changes:
- Supplied English articles and predicate/object support for markets/squares, soul-love relative clauses, powers/strengths, mighty men, sword/night, Solomon/litter, and crown phrases.
- Kept Song of Solomon 3:1 unchanged in the translation because it already uses "the one my soul loved"; updated its decision note to match that wording.
- Left Song of Solomon 3:6 and 3:10 unchanged because current wording is readable for this article-focused pass.

Validation:
- CSV shape check passed for `ot_full.csv`, `translation_decisions.csv`, and `translation_footnotes.csv`.
- `python3 -m pytest -q tests/test_smoke.py` passed: 19 tests.
- `make checkpoint-ot` passed with no missing decisions.
- `make build-ot-review` passed.
