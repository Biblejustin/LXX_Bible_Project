# OT Review Pass 98

Scope: additional non-vocative house, remnant, glory, ark, and law article cleanup after pass 97.

Changes:
- Normalized clear non-vocative `house of ...` phrases:
  - `dedicated/pulled down/Why was house of God` -> `the house of God`
  - `destroy/above house of David` -> `the house of David`
  - `like/avenged house of Ahab` -> `the house of Ahab`
  - selected `house of Israel/Judah/Jacob/Aaron` subject formulas -> article-normalized forms
- Normalized remnant formulas such as `remnant of Israel will`, `wipe out remnant of Israel`, and `receive remnant of Israel`.
- Normalized glory formulas such as `cloud of glory of the Lord`, `Let glory of the Lord`, `see glory of the Lord`, and `Blessed glory of the Lord`.
- Normalized `where ark of the Lord entered`, `book of law of Moses`, `hear law of God`, and `Remember law of Moses`.

Validation:
- `scripts/apply_ot_article_cleanup.py` updated 49 source rows, 9 decision rows, and 46 footnote rows.
- Targeted smoke test passed.
- Follow-up scan returned zero for pass 98 exact guards and double articles.
