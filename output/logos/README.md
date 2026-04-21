# Fresh Translation OT Logos/Proofreading Files

Generated files:

- `fresh_translation_ot_logos_bible_lxx.docx`: Logos Personal Book source. Compile as resource type `Bible`.
- `fresh_translation_ot_proofreading.docx`: clean proofreading/printing copy without Logos milestone or field syntax.
- `fresh_translation_ot_logos_bible_diagnostics.json`: build counts and cross-reference/note diagnostics.
- `fresh_translation_ot_logos_bible_preview.md`: quick preview sample for spot-checking.

Logos import:

1. Open Logos desktop.
2. Go to `Tools > Personal Books`.
3. Click `Add book`.
4. Set `Type` to `Bible`.
5. Add `fresh_translation_ot_logos_bible_lxx.docx` as the body file.
6. Build the book.
7. If Logos exposes advanced datatype/index settings, keep the source milestones on `BibleLXX2` / `Bible (LXX-S)`.

Scope:

- Source text: `data/raw/lxx_greek/ot_full.csv`.
- Translation notes: reviewed rows from `data/research/translation_footnotes.csv`.
- Excluded: generic Brenton comparison notes, name meanings, lexicon entries, vocabulary notes, names-of-God notes, and other Brenton package study notes.
- Cross-references: TSK primary set from `data/raw/TSK.zip`; OpenBible fallback from `data/raw/cross-references.zip` where TSK has no verse row. See root `NOTICE.md` for public-domain/CC-BY attribution details.

Known constraint:

- The repo can validate DOCX package/XML structure locally. This machine does not currently have LibreOffice installed, so visual rendering must be checked by opening the files in Word/Pages/Logos.
