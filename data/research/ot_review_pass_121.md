# OT Review Pass 121

Scope: high-priority article cleanup in Malachi, Zechariah, Ecclesiastes, Ezekiel, Ezra, Habakkuk, Micah, and Proverbs.

Applied:
- Malachi 1:6; 2:7; 2:10: normalized `father`, `priest`, `law`, and covenant formulas.
- Zechariah 14:5: `ravine of my mountains` and `ravine of mountains` -> article-normalized forms.
- Ecclesiastes 11:5: `what way of spirit` and `womb of pregnant woman` -> readable article forms.
- Ezekiel 18:20; 33:12: normalized `soul`, `son`, `father`, `righteousness`, and `lawlessness` formulas.
- Ezra 5:3; 6:1; 6:3; 6:12; 7:21; 7:26: normalized decree and law formulas.
- Habakkuk 1:12: `Lord` vocative -> `O Lord`, with idempotent cleanup for repeated `O`.
- Micah 6:7; 7:6 and Proverbs 28:7: normalized womb, son, law, and father formulas.

Verification:
- `scripts/apply_ot_article_cleanup.py`
- `tests/test_smoke.py::test_common_lord_article_formulas_are_normalized`
