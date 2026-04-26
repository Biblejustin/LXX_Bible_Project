# OT review pass 77

Scope: Continued conservative OT prose cleanup after pass 76.

Changes:
- Normalized lowercase royal title before proper names: "king David/Solomon/etc." -> "King David/Solomon/etc."
- Normalized bare royal subject formulas such as "And king said/commanded", "Because king hopes", "But king will", and "Then king issued" to include "the king".
- Left genealogy/list "Sons of..." headings untouched.

Verification:
- Re-ran `scripts/apply_ot_article_cleanup.py`.
- Added targeted smoke assertions for royal-title and royal-subject formulas.
- Ran `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q`.
