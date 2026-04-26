# OT review pass 81

Scope: Continued conservative OT article cleanup after pass 80.

Changes:
- Normalized remaining low-count formulas: "from presence of", "for work of", "with elders of", "over faithlessness of", "in gladness of", "in wandering of", "according to completion of", and "into height of".
- Added a specific "elders of land" -> "elders of the land" cleanup.
- Left idioms such as "in place of", "by way of", "on account of", and "to half of" unchanged.

Verification:
- Re-ran `scripts/apply_ot_article_cleanup.py`.
- Added smoke assertions for the new formulas.
- Ran `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q`.
