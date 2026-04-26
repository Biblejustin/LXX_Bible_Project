# OT Review Pass 125

Scope: high-priority idiom outlier grammar cleanup.

Applied:
- 2 Chronicles 6:33: normalized foreigner/all-peoples clause grammar while preserving the name-called-upon formula.
- Jeremiah 7:11: capitalized verse-opening question and supplied `a den of robbers`.
- Joel 3:5; Obadiah 1:17: normalized `Mount Zion` casing.
- Psalms 98:6: supplied article in `called on the Lord`.
- Habakkuk 3:19: supplied the implicit subject in the final high-places clause.

Verification:
- `scripts/apply_ot_article_cleanup.py`
- `tests/test_smoke.py::test_common_lord_article_formulas_are_normalized`
