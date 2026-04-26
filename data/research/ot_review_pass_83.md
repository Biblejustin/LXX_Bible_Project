# OT Review Pass 83

Focus: bare "build house" formulas.

Changes:
- Normalized temple/house construction formulas:
  - "build/building/built house of" -> "build/building/built the house of"
  - "build/building/built house for/to ..." -> "build/building/built a house for/to ..."
  - "build house, and I will take pleasure" -> "build the house, and I will take pleasure"
- Repaired an intermediate regex error that dropped the object after "for/to" in several rows.
- Added smoke guards for remaining "build house" forms.

Verification:
- `scripts/apply_ot_article_cleanup.py` left 0 `build house` remnants in `data/raw/lxx_greek/ot_full.csv`.
- `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
