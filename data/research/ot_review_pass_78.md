# OT review pass 78

Scope: Continued conservative OT article cleanup after pass 77.

Changes:
- Normalized "of king" -> "of the king" across recurring royal-office phrases.
- Normalized "of people" -> "of the people" where the English needed the article.
- Normalized "all people" -> "all the people" for recurring audience/assembly formulas.

Verification:
- Re-ran `scripts/apply_ot_article_cleanup.py`.
- Added smoke assertions for king/people article formulas.
- Ran `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q`.
