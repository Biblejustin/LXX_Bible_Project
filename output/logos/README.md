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

Scope:

- Source text: `data/raw/lxx_greek/ot_full.csv`.
- Translation notes: reviewed rows from `data/research/translation_footnotes.csv`. Notes that explicitly mention Masoretic/MT/Hebrew-aligned textual divergence are labeled `MT/LXX note` in the footnotes.
- Name meanings: `data/proper_names.csv` and `data/names_of_god.csv`. Proper-name notes and unambiguous multi-word divine-title notes are placed at the first exact occurrence per chapter. Ambiguous single-word divine-title notes remain source-reference anchored to avoid assigning the wrong source-language title from English alone.
- Supplemental Brenton-package notes: Brenton USFM footnotes, TSK study-note text, and Hebrew/Greek vocabulary notes. Proper-name and divine-title notes are not duplicated here because they are already integrated as name-meaning notes.
- Lexham Textual Notes links: generated from `/Users/justinscaggs/Desktop/The Lexham Textual Notes on the Bible.html` when present. Links use `logosres:lexcontxtntbbl;ref=Bible.<ref.ly-code>` and require a Logos license for `The Lexham Textual Notes on the Bible`.
- Cross-references: TSK primary set from `data/raw/TSK.zip`; OpenBible fallback from `data/raw/cross-references.zip` where TSK has no verse row. TSK catchwords are used as word/phrase anchors when they exactly match the fresh translation; otherwise cross-references remain verse-anchored. See root `NOTICE.md` for public-domain/CC-BY attribution details.
- Footnote numbering: one DOCX file with internal Word section metadata set to restart visible footnote numbering by `chapter`.

Validation:

- The repo validates DOCX package/XML structure locally and checks that macOS can read the generated DOCX. Final Personal Book compilation still needs to be checked inside Logos after each source change.
