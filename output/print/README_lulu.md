# Print Proof Files

Generated files:

- `the_greek_heritage_study_bible_lulu_print_proof.docx`: compact DOCX for inexpensive physical proofreading.
- `the_greek_heritage_study_bible_lulu_print_proof_diagnostics.json`: build counts and DOCX validation details.
- `the_greek_heritage_study_bible_lulu_print_proof_pandoc_pdf_headers.json`: active Pandoc PDF page-header diagnostics.
- `the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf`: active full-size Pandoc/XeLaTeX proof PDF with two-column footnotes.

Profile:

- Combined Genesis-Revelation text.
- OT source: LXX Greek source rows; NT source: Scrivener 1894 Textus Receptus Greek source rows.
- Compact single-column DOCX layout with Lulu-safe mirrored POD margins and run-in verse paragraphs.
- Page size: US Letter 8.5 x 11 in.
- Margins: mirrored; inside 0.75 in; outside 0.5 in; top/bottom 0.5 in.
- Front matter includes an LXX-to-English numbering guide for major reader-facing divergences.
- Reviewed translation/textual notes included.
- Type profile: docx_9_5pt; pandoc_pdf_8_75pt.
- Verse layout: chapter-continuous run-in paragraphs.
- Footnote layout: active Pandoc PDF uses two-column footnotes; TeX-side page-local note numbers; verse-number-keyed cross-references in red via manyfoot two-stream LaTeX; 7.5pt Latin text; 6.5pt complex-script text; 8.5pt note markers.
- Alternate PDF renderer: Pandoc/XeLaTeX is the active full-size print proof renderer; LibreOffice PDF output is disabled for print proof.
- Pericope headings: 2983 BSB-placement original headings included.
- Front preface pages discuss the purpose of the draft and rough translation methodology.
- Executive PDF profile abandoned; it did not save enough size versus Letter to justify maintaining.
- Lulu PDF build stamps page numbers and chapter/verse ranges into the top margin after pagination.
- Print note label legend: T = translation note; Txt = textual note; MT/LXX = Masoretic/LXX difference; Heb = Hebrew divine title; Gk = Greek form or Greek LXX divine title; Tr = transliterated proper noun; Std = standard English equivalent; Src = source form; Nm = name meaning; Pn = personal name; Pl = place name; Ppl = people name; Div = divine or supernatural name; Eng = common English rendering.
- Name-meaning notes are included only at their listed first/source occurrence to keep the physical proof shorter.
- Book preface pages included.
- Brenton/source supplemental notes excluded.
- Modest cross-reference layer: OpenBible.info verse-level cross-references, ranked by OpenBible vote count, capped per verse, and printed with abbreviated book names. Used by attribution under the OpenBible CC-BY dataset license.

Counts:

- Verses: `30866`
- Book preface pages: `66`
- Translation/textual note footnotes: `4035`
- Name-meaning footnotes: `2814`
- Cross-reference footnotes: `28809`
- Cross-reference refs kept: `213015`
- Supplemental/Brenton footnotes: `0`

Rebuild:

```bash
make build-print-proof-lulu-pandoc-pdf
```
