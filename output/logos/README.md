# Fresh Translation OT Logos/Proofreading Files

Generated files:

- `fresh_translation_ot_logos_bible.docx`: Logos Personal Book source. Compile as resource type `Bible`.
- `fresh_translation_ot_logos_bible_mt_notes.docx`: Logos Personal Book source with verse milestones remapped to standard English/MT references so existing reference-anchored Logos notes from MT-based Bibles can show. Compile as resource type `Bible`.
- `fresh_translation_ot_proofreading.docx`: clean proofreading/printing copy without Logos milestone or field syntax.
- `fresh_translation_ot_logos_bible_diagnostics.json`: build counts and cross-reference/note diagnostics.
- `fresh_translation_ot_logos_bible_preview.md`: quick preview sample for spot-checking.

Logos import:

1. Open Logos desktop.
2. Go to `Tools > Personal Books`.
3. Click `Add book`.
4. Set `Type` to `Bible`.
5. Add `fresh_translation_ot_logos_bible.docx` as the body file.
6. Build the book.
7. If Logos exposes advanced datatype/index settings, keep the source milestones on `Bible`.

MT-note bridge import:

Use `fresh_translation_ot_logos_bible_mt_notes.docx` instead of `fresh_translation_ot_logos_bible.docx` when the goal is to surface notes already anchored to standard MT/English Bible references. The visible verse numbers remain from the LXX source rows, but hidden milestones are remapped to standard Bible references where a reliable mapping is available.

Verse numbering:

- OT Logos files preserve LXX source ordering and visible LXX verse numbers by design, including places where LXX chapter/verse order differs from standard English/MT order.

Scope:

- Source basis: LXX Greek.
- Source text: `data/raw/lxx_greek/ot_full.csv`.
- Book preface pages: `data/book_intros_template.csv`. These are inserted before each book's chapter text in all generated DOCX files.
- Translation notes: reviewed rows from `data/research/translation_footnotes.csv`. Generic MT/LXX difference rows are skipped unless `data/research/translation_decisions.csv` supports a concrete local detail, such as a substantive number/unit difference. Those concrete rows are labeled `MT/LXX note`.
- Name meanings: `data/proper_names.csv`, `data/proper_name_transliteration_notes.csv`, and `data/names_of_god.csv`. Proper-name notes and unambiguous multi-word divine-title notes are placed at the first exact occurrence per chapter. Ambiguous single-word divine-title notes remain source-reference anchored to avoid assigning the wrong source-language title from English alone.
- Name-meaning caution: many meanings are seeded from public-domain legacy sources such as Hitchcock's Bible Names Dictionary and are reader aids, not final etymological claims. Correct stronger lexical evidence should replace them as review continues.
- Literal phrase convention: phrases such as `sons of Israel` and `sons of men` usually preserve Greek son-language intentionally rather than smoothing by default.
- MT-only completeness insertion: LXX-numbered Jeremiah 40:14-26 supplies MT Jeremiah 33:14-26 in brackets. The footnote marks these verses as present in the MT, absent from the LXX text used here, not quoted in the NT, and included for completeness.
- 1 Kings ordering: Naboth vineyard material appears at LXX-numbered 1 Kings 20, while Ben-Hadad battle material appears at LXX-numbered 1 Kings 21. This follows the source order and is not treated as a missing chapter.
- Supplemental Brenton notes: Brenton USFM footnotes are included. TSK study-note text is intentionally excluded because it is too large for this Logos source. Hebrew and Greek vocabulary notes are excluded because Logos already provides lexical lookup layers. Proper-name and divine-title notes are integrated as name-meaning notes.
- Local textual-note export: generated from `data/research/textual_notes_export.html` when present. Note text is embedded into this Personal Book as local `Textual note` footnotes; no `logosres:` links or external Logos resource layer are emitted.
- Future work: deuterocanonical/apocrypha intro rows exist, but current source text does not yet include these books: Tobit, Judith, Wisdom, Sirach, Baruch, Letter of Jeremiah, Susanna, Bel and the Dragon, 1 Maccabees, 2 Maccabees, 1 Esdras, Prayer of Manasseh, 3 Maccabees, 4 Maccabees, 1 Enoch.
- Place links: disabled by default; generated DOCX keeps place names as plain text so Personal Book import remains stable.
- Cross-references: TSK primary set from `data/raw/TSK.zip`; OpenBible fallback from `data/raw/cross-references.zip` where TSK has no verse row. TSK catchwords are used as word/phrase anchors only when they exactly match the fresh translation; otherwise cross-references remain verse-anchored. Broad single-word catchword groups are thinned to same-book links or dropped to avoid loose thematic jumps. See root `NOTICE.md` for public-domain/CC-BY attribution details.
- Footnote numbering: one DOCX file with internal Word section metadata set to restart visible footnote numbering by `chapter`. Cross-reference footnotes use normal numeric Word footnote references because Logos 49 Personal Book import crashes while converting large DOCX files that use custom footnote marks.

Validation:

- The repo validates DOCX package/XML structure locally and checks that macOS can read the generated DOCX. Final Personal Book compilation still needs to be checked inside Logos after each source change.
