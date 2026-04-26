# OT review pass 79

Scope: Continued conservative OT article cleanup after pass 78.

Changes:
- Normalized "of city", "of house", and "of temple" to include "the" in recurring prose formulas.
- Normalized "all assembly" and "all land" to "all the assembly" and "all the land".
- Left plural/genealogical house formulas such as "houses of fathers" untouched.

Verification:
- Re-ran `scripts/apply_ot_article_cleanup.py`.
- Added smoke assertions for city/house/temple and assembly/land article formulas.
- Ran `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q`.
