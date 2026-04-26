# OT Review Pass 84

Focus: remaining singular "son of man" article.

Changes:
- Normalized Job 35:8 from "to son of man" to "to a son of man".
- Added smoke guard for remaining "to son of man" forms.

Verification:
- `scripts/apply_ot_article_cleanup.py` updated 3 source rows, 1 decision row, and 3 footnote rows.
- `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
