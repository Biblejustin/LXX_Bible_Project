# OT Review Pass 73

Scope: article cleanup for repeated construct phrases surfaced in the 1 Samuel and 1 Chronicles review sweep.

Changes applied:
- Added "the" in scoped phrases such as "from the end of the land", "into the tribe of Levi", "from the hill of Benjamin", "to bring the ark of God", and "from there the ark of God".
- Added 1 Chronicles service/temple phrases such as "for the ark of God", "for the cities of our God", "for the nails of doors", "for the fine flour of offering", "for the remaining sons of Levi", "For the divisions of gates", and "over the cleansing of all holy things".
- Added remaining scoped formulas including "after the gods of the peoples", "at the hearing of the ear", "from the families of the half tribe", "to the borders of the sons of Manasseh", and "into the cave of Adullam".

Verification:
- `python scripts/apply_ot_article_cleanup.py`
- `python -m pytest -q tests/test_smoke.py::test_common_lord_article_formulas_are_normalized`
