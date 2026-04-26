# OT Review Pass 87

Focus: idempotency and remaining ark/altar/people/house article cleanup.

Changes:
- Made remnant/house/city article rules idempotent to prevent repeated "the" on reruns.
- Added a general repeated-lowercase-article collapse.
- Normalized bare ark and altar phrases.
- Normalized sentence-start "people" forms.
- Normalized safe house phrases while leaving valid idioms such as "house to house".

Verification:
- `scripts/apply_ot_article_cleanup.py` updated 44 source rows, 31 decision rows, and 41 footnote rows; a follow-up house fix updated 1 source row, 3 decision rows, and 1 footnote row.
- `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- Follow-up scan found 0 doubled articles, 0 targeted bare house remnants, 0 bare ark remnants, 0 bare altar remnants, and 0 sentence-start bare people forms.
