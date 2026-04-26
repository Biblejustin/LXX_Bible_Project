# OT review pass 76

Scope: Continued conservative English article cleanup after pass 75.

Changes:
- Normalized recurring sentence-start constructs: "And name of", "And ark of", "And queen of", "But word of", "But hand of", "For heart of", "And land of", and house-of-Israel formulas.
- Normalized remaining subject formulas such as "Voice of...", "Mouth of...", "River of God", "Mountain of God", "King of Babylon heard", "People of the land...", and "Remnant of Israel will...".
- Left genealogical headings such as "Sons of..." untouched because those are list headings, not prose article defects.

Verification:
- Re-ran `scripts/apply_ot_article_cleanup.py`.
- Added targeted smoke assertions for the new recurring patterns.
- Ran `pytest tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q`.
