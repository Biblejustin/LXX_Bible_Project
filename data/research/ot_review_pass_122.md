# OT Review Pass 122

Scope: sample-visible reader cleanup from release-hardening samples and priority book samples.

Applied:
- Nehemiah 1:1: `Words of Nehemiah` -> `The words of Nehemiah`; `in month Chisleu, twentieth year` -> `in the month of Chisleu, in the twentieth year`.
- Nehemiah 7:3: `Gates of Jerusalem` -> `The gates of Jerusalem`; added article before `inhabitants of Jerusalem`.
- Nehemiah 8:2: `everyone understanding to hear` -> `everyone who could understand what they heard`.
- Nehemiah 13:31: normalized wood-bearer gift wording and vocative `O our God`.
- 2 Chronicles 20:18, 20:20: normalized `face to ground`, `inhabitants of Jerusalem`, and `in morning`.
- Job 22:15: `ancient path` -> `the ancient path`.
- Proverbs 16:14: `Wrath of the king messenger` -> `The wrath of the king is a messenger`; `wise man` -> `a wise man`.

Verification:
- `scripts/apply_ot_article_cleanup.py`
- `tests/test_smoke.py::test_common_lord_article_formulas_are_normalized`
