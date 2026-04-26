# OT Review Pass 119

Scope: article/vocative cleanup in high-signal divine-title and prayer formulas.

Applied:
- 2 Samuel 7:25: `Lord Almighty` vocative -> `O Lord Almighty`.
- 1 Chronicles 16:35: `God of our salvation` vocative -> `O God of our salvation`; `from nations` -> `from the nations`.
- 1 Chronicles 17:24: opening vocative -> `O Lord, Lord Almighty`.
- 2 Chronicles 6:20: `to hear prayer which` -> `to hear the prayer which`.
- Psalms 67:20; 84:5: normalized `God of our salvations` subject/vocative formulas.
- Psalms 105:47: `Lord our God` vocative -> `O Lord our God`; `from nations` -> `from the nations`.
- Jeremiah 15:16; Zechariah 1:12: `Lord Almighty` vocatives -> `O Lord Almighty`.
- Zechariah 12:10: `spirit of grace and compassion` -> `a spirit of grace and compassion`.

Deferred:
- Broad `from nations` cleanup. Too many contexts use different Greek constructions and need per-reference review.
- Full translation-style review of `salvations` plural. Current pass preserves LXX plural where present.

Verification:
- `scripts/apply_ot_article_cleanup.py`
- `tests/test_smoke.py::test_common_lord_article_formulas_are_normalized`
