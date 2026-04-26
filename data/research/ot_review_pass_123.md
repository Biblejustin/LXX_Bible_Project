# OT Review Pass 123

Scope: release-hardening sample cleanup in wisdom books and prophets.

Applied:
- Proverbs 31:31; Ecclesiastes 1:1; Song of Solomon 4:14; 8:14: normalized article and comparison phrases.
- Jeremiah 1:1; Lamentations 3:35; Ezekiel 1:1; Daniel 6:20: normalized priest, judgment, year, heaven, and lions' den formulas.
- Hosea 14:10; Joel 2:17; Micah 4:12; Nahum 3:19: normalized ways/thought/threshing/nations and vocative `O Lord`.
- Habakkuk 1:1; 2:12: normalized `Habakkuk the prophet` and city-building article formulas.
- Haggai 1:1; Zechariah 1:1; Malachi 2:14: normalized royal-year, prophet/priest, and wife/covenant formulas.

Verification:
- `scripts/apply_ot_article_cleanup.py`
- `tests/test_smoke.py::test_common_lord_article_formulas_are_normalized`
