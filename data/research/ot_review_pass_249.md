# OT Review Pass 249

Scope: Isaiah 37.

Changes:
- Supplied English articles and predicate support for garments, elders/priests, Rabshakeh/living-God wording, words/envoys phrase, spirit/report/sword wording, king/Libnah phrase, Tirhakah/Ethiopians wording, kings/earth clause, gods/nations phrase, kings/city phrase, book/messengers phrase, cherubim/inhabited-world wording, words/living-God phrase, kings/inhabited-world phrase, fire/works phrase, kingdom/earth phrase, word/daughter/head wording, Lord/height/beauty/region phrase, bridge/waters phrase, nations/dwellers phrase, hands phrase, hook/bridle/way phrase, sign/remnant phrase, root phrase, left/saved participles, king/arrow/shield/palisade phrase, way phrase, and camp/morning/bodies phrase.
- Synced stale Isaiah 37 translation footnote triggers from Somnas/Lobna/Tharaka/Raphes/Thaimad/Arphad/Anag/Nasarach/Adramelech/Sarasar to the reviewed source forms Shebna/Libnah/Tirhakah/Rezeph/Theemath/Arpad/Hena/Nisroch/Adrammelech/Sharezer.
- Added decision rows and smoke guards for reviewed phrases.

Validation:
- CSV shape check passed for source, footnotes, and decisions.
- Targeted Isaiah 37 footnote-sync check passed.
- `python3 -m pytest tests/test_smoke.py::test_reviewed_ot_rendering_cleanup_stays_in_source_and_notes tests/test_smoke.py::test_common_lord_article_formulas_are_normalized -q` passed.
- `make checkpoint-ot` passed with no missing decisions; smoke passed 19 tests.
