# Fresh Translation NT Logos/Proofreading Files

Generated files:

- `fresh_translation_nt_tr_logos_bible.docx`: Logos Personal Book source. Compile as resource type `Bible`.
- `fresh_translation_nt_tr_reference_notes.docx`: Logos Personal Book source emitted for parity with the OT reference-bridge output. NT TR source rows already use standard NT milestones. Compile as resource type `Bible`.
- `fresh_translation_nt_tr_proofreading.docx`: clean proofreading/printing copy without Logos milestone or field syntax.
- `fresh_translation_nt_tr_diagnostics.json`: build counts and cross-reference/note diagnostics.
- `fresh_translation_nt_tr_preview.md`: quick preview sample for spot-checking.

Logos import:

1. Open Logos desktop.
2. Go to `Tools > Personal Books`.
3. Click `Add book`.
4. Set `Type` to `Bible`.
5. Add `fresh_translation_nt_tr_logos_bible.docx` as the body file.
6. Build the book.
7. If Logos exposes advanced datatype/index settings, keep the source milestones on `Bible`.

Reference-note bridge import:

`fresh_translation_nt_tr_reference_notes.docx` is emitted for parity with the OT build. NT TR source rows already use standard NT versification, so this bridge should normally match the main Logos source.

Verse numbering:

- OT Logos files preserve LXX source ordering and visible LXX verse numbers by design, including places where LXX chapter/verse order differs from standard English/MT order.

Scope:

- Source basis: Scrivener 1894 Textus Receptus Greek.
- Source text: `data/raw/tr_greek/nt_full.csv`, imported from byztxt/greektext-scrivener Scrivener 1894 Textus Receptus text-only files.
- Book preface pages: `data/book_intros_template.csv`. These are inserted before each book's chapter text in all generated DOCX files.
- Translation notes: reviewed rows from `data/research/translation_footnotes.csv` plus any local textual-note export entries matching NT references. OT-specific MT/LXX rows are ignored for this NT source.
- Name meanings: `data/proper_names.csv`, `data/proper_name_transliteration_notes.csv`, and `data/names_of_god.csv`. Proper-name notes and unambiguous multi-word divine-title notes are placed at the first exact occurrence per chapter. Ambiguous single-word divine-title notes remain source-reference anchored to avoid assigning the wrong source-language title from English alone.
- Name-meaning caution: many meanings are seeded from public-domain legacy sources such as Hitchcock's Bible Names Dictionary and are reader aids, not final etymological claims. Correct stronger lexical evidence should replace them as review continues.
- Literal phrase convention: phrases such as `sons of Israel` and `sons of men` usually preserve Greek son-language intentionally rather than smoothing by default.
- MT-only completeness insertion: LXX-numbered Jeremiah 40:14-26 supplies MT Jeremiah 33:14-26 in brackets. The footnote marks these verses as present in the MT, absent from the LXX text used here, not quoted in the NT, and included for completeness.
- 1 Kings ordering: Naboth vineyard material appears at LXX-numbered 1 Kings 20, while Ben-Hadad battle material appears at LXX-numbered 1 Kings 21. This follows the source order and is not treated as a missing chapter.
- Supplemental source notes: no NT supplemental source-note layer is currently enabled. TSK study-note text is intentionally excluded because it is too large for this Logos source. Greek vocabulary notes are excluded because Logos already provides lexical lookup layers. Proper-name and divine-title notes are integrated as name-meaning notes.
- Local textual-note export: generated from `data/research/textual_notes_export.html` when present. Note text is embedded into this Personal Book as local `Textual note` footnotes; no `logosres:` links or external Logos resource layer are emitted.
- Future work: NT literal revision is seeded from the public-domain UKJV alignment and still needs verse-by-verse TR Greek review.
- Place links: conservative Logos `BibleKnowledgebase` datatype links are added for unambiguous primary place labels found in the local Logos autocomplete database. These are clickable Factbook/place links; Personal Book source does not expose the same internal atlas-pin overlay used by Logos-edition Bibles.
- Cross-references: TSK primary set from `data/raw/TSK.zip`; OpenBible fallback from `data/raw/cross-references.zip` where TSK has no verse row. TSK catchwords are used as word/phrase anchors only when they exactly match the fresh translation; otherwise cross-references remain verse-anchored. Broad single-word catchword groups are thinned to same-book links or dropped to avoid loose thematic jumps. See root `NOTICE.md` for public-domain/CC-BY attribution details.
- Footnote numbering: one DOCX file with internal Word section metadata set to restart visible footnote numbering by `chapter`. Cross-reference footnotes use normal numeric Word footnote references because Logos 49 Personal Book import crashes while converting large DOCX files that use custom footnote marks.

Validation:

- The repo validates DOCX package/XML structure locally and checks that macOS can read the generated DOCX. Final Personal Book compilation still needs to be checked inside Logos after each source change.
