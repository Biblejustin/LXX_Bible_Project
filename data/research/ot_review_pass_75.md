# OT Review Pass 75

Scope: continued sentence-subject article cleanup after pass 74.

Changes applied:
- Normalized narrative openers such as `And king of...` to `And the king of...`.
- Normalized Psalm/Proverb subject formulas: `Voice of the Lord`, `Fear of the Lord`, `Heart of...`, and `Lips of...`.
- Added article cleanup for `glory of the Lord filled house` and `remnant of Israel were`.

Verification:
- `python scripts/apply_ot_article_cleanup.py`
- `python -m pytest -q tests/test_smoke.py::test_common_lord_article_formulas_are_normalized`
