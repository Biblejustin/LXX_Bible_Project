# OT Review Pass 96

Scope: conservative article cleanup for recurring bare construct phrases after pass 95.

Changes:
- Normalized Proverbs gate formulas: `beside gates of` -> `beside the gates of`.
- Normalized Song of Solomon field formula: `strengths of field` -> `strengths of the field`.
- Normalized isolated construct phrases:
  - `in vineyards of wine` -> `in the vineyards of wine`
  - `In region of Jordan king cast them in thickness of earth` -> `In the region of Jordan the king cast them in the thickness of the earth`
  - `with force of mighty warriors` -> `with a force of mighty warriors`
  - `concerning houses of this city` -> `concerning the houses of this city`
  - `in fury of wrath` -> `in a fury of wrath`
  - `for pasture of camels/sheep` -> `for a pasture for camels/sheep`
  - `from line of sons of Israel` -> `from the line of the sons of Israel`
- Normalized Daniel commander formulas with needed subject/object articles.

Validation:
- `scripts/apply_ot_article_cleanup.py` updated 21 source rows, 1 decision row, and 20 footnote rows.
- Targeted smoke test passed.
- Follow-up scan returned zero for pass 96 exact guards and double articles.
