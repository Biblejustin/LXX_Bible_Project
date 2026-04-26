# OT Review Pass 86

Focus: lowercase land article cleanup.

Changes:
- Normalized lowercase land phrases such as "dwelling in land", "death in land", "reigned over land", "came into land", and "cover land".
- Used scoped indefinite forms where needed, such as "a land not theirs" and "a land thrown open".
- Normalized Job 42:17 to "dwelt in the land of Uz".
- Added smoke guards for remaining lowercase land forms and double-land articles.

Verification:
- `scripts/apply_ot_article_cleanup.py` updated 72 source rows, 18 decision rows, and 72 footnote rows; a follow-up dedupe run updated 5 source rows, 1 decision row, and 5 footnote rows.
- `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- Follow-up scan found 0 lowercase land article remnants and 0 doubled land articles.
