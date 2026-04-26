# OT Review Pass 120

Scope: high-priority queue article cleanup in prayers, Daniel court narratives, Haggai, Hosea, and Amos.

Applied:
- 2 Chronicles 6:19: `Lord God` vocative -> `O Lord God`; `petition and prayer` -> `the petition and the prayer`.
- Nehemiah 1:5: `Please, Lord God of heaven` -> `Please, O Lord God of heaven`.
- Amos 5:15: `restore judgment in gates` -> `restore judgment in the gates`.
- Daniel 3:28: `command of the king` -> `the command of the king`.
- Daniel 4:22, 4:33, 4:34, 5:23: normalized `whole earth`, `house of the living God`, `sins of`, `herbs of the earth`, `the God of gods`, and `the kingdom` formulas.
- Haggai 2:9: `Latter glory` -> `The latter glory`; `greater than first` -> `greater than the first`.
- Hosea 4:6; 13:4: `the law of your God`; `all the army of heaven`.
- 2 Chronicles 36:5; Lamentations 4:13: `because of the sins of`.

Verification:
- `scripts/apply_ot_article_cleanup.py`
- `tests/test_smoke.py::test_common_lord_article_formulas_are_normalized`
