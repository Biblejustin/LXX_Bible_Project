# OT Review Pass 82

Focus: bare temple article cleanup.

Changes:
- Normalized remaining bare "before/from/toward/in/into temple" forms.
- Normalized "entered temple" to "entered the temple".
- Added smoke guards and reference assertions for 2 Chronicles 3:17; 4:7; 26:19; 29:17; Isaiah 66:6.

Verification:
- `scripts/apply_ot_article_cleanup.py` updated 8 source rows, 1 decision row, and 7 footnote rows.
- `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
