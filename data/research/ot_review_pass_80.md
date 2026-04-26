# OT review pass 80

Scope: Continued conservative OT article cleanup after pass 79.

Changes:
- Normalized low-risk preposition formulas: "from breath of", "in wilderness of", "at dedication of", "at mouth of", "according to ways of", "by gates of", "for wall of", and "for throne of".
- Skipped idioms such as "in place of", "by way of", "in front of", and "on account of".

Verification:
- Re-ran `scripts/apply_ot_article_cleanup.py`.
- Added smoke assertions for the new preposition/article formulas.
- Ran `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q`.
