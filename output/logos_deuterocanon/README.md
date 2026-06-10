# The Greek Heritage Study Bible Deuterocanon Logos/Proofreading Files

Generated files:

- `the_greek_heritage_study_bible_deuterocanon_logos_bible.docx`: Logos Personal Book source. Compile as resource type `Bible`.
- `the_greek_heritage_study_bible_deuterocanon_diagnostics.json`: build counts and cross-reference/note diagnostics.
- `the_greek_heritage_study_bible_deuterocanon_preview.md`: quick preview sample for spot-checking.

Logos import:

1. Open Logos desktop.
2. Go to `Tools > Personal Books`.
3. Click `Add book`.
4. Set `Type` to `Bible`.
5. Add `the_greek_heritage_study_bible_deuterocanon_logos_bible.docx` as the body file.
6. Build the book.
7. If Logos exposes advanced datatype/index settings, keep the source milestones on `Bible`.

Reference-note bridge import:

The default deuterocanon target emits a Logos-only DOCX. No MT-reference bridge is generated unless the full DOCX output set is requested explicitly.

Verse numbering:

- Deuterocanon Logos files preserve imported LXX source order and visible source verse labels, including suffix labels such as Greek Esther 1:1α. Hidden Logos milestones use the numeric base verse where suffix labels are present; unsupported Logos Bible datatype ranges are left as visible text without hidden milestones.
Key examples:

- Deuterocanon references follow imported source labels; suffix labels remain visible in the verse text.

Scope:

- Source basis: LXX deuterocanon/additions Greek source rows.
- Source text: `data/raw/lxx_deuterocanon/deuterocanon_full.csv`. Translation work is made from the separate LXX deuterocanon/additions Greek source rows, not from an English base.
- Book preface pages: `data/book_intros_template.csv`. These are inserted before each book's chapter text in all generated DOCX files.
- Translation notes: shared OT/NT translation-note tables are not applied to this separate deuterocanon Logos source.
- Name meanings: no deuterocanon name-meaning layer is enabled yet; proper-name notes can be added in a later deuterocanon note pass.
- Name-meaning caution: not applicable until a deuterocanon name-meaning layer is enabled.
- Literal phrase convention: phrases such as `sons of Israel` and `sons of men` usually preserve Greek son-language intentionally rather than smoothing by default.
- Greek Esther shape: `ESG` is the full Greek Esther import. `ESGA` remains available in the source workspace as an additions-only view for review; use the generated progress/worksheet files to audit that view.
- Greek Ezra B / 2 Esdras: `2ES` is Greek Ezra B from GRCLXX, not the Latin apocalypse commonly titled 2 Esdras / 4 Ezra in some English traditions. Its Logos Bible milestones are suppressed to avoid false links.
- Source row shape: plain embedded source verse labels are split into rows; bracketed source-text sections remain bracketed.
- Supplemental source notes: source descriptors are preserved in `syntax_notes` in the CSV workspace, but no supplemental footnote layer is emitted in this separate Logos source yet.
- Local textual-note export: generated from `data/research/textual_notes_export.html` when present. Note text is embedded into this Personal Book as local `Textual note` footnotes; no `logosres:` links or external Logos resource layer are emitted.
- Paper proof scope: this deuterocanon source is intentionally separate and is not included in the compact paper proofreading copy.
- Place links: disabled by default; generated DOCX keeps place names as plain text so Personal Book import remains stable.
- Cross-references: omitted because `--no-crossrefs` was used.
- Greek concordance: not included. Logos provides native dynamic concordance lookup, so this build relies on that capability instead of duplicating it as a static appendix. Print/deuterocanon proof outputs may include compact static concordance material for readers without Logos lookup tools.
- Footnote numbering: one DOCX file with internal Word section metadata set to restart visible footnote numbering by `chapter`. Cross-reference footnotes use normal numeric Word footnote references because Logos 49 Personal Book import crashes while converting large DOCX files that use custom footnote marks.

Validation:

- The repo validates DOCX package/XML structure locally and checks that macOS can read the generated DOCX. Final Personal Book compilation still needs to be checked inside Logos after each source change.
