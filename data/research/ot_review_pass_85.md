# OT Review Pass 85

Focus: lowercase city article cleanup.

Changes:
- Normalized lowercase city phrases such as "came into city", "from city", "in city", "to city", and "city will be taken".
- Preserved capitalized proper-title forms such as "City of David" by using case-sensitive lowercase rules.
- Added smoke guards for remaining lowercase city forms.

Verification:
- `scripts/apply_ot_article_cleanup.py` updated 38 source rows, 21 decision rows, and 39 footnote rows.
- `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- Follow-up scan found 0 remaining lowercase city article remnants.
