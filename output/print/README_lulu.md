# Print Proof Files

Generated files:

- `the_greek_heritage_study_bible_lulu_print_proof.docx`: compact DOCX for inexpensive physical proofreading.
- `the_greek_heritage_study_bible_lulu_print_proof_diagnostics.json`: build counts and DOCX validation details.
- `the_greek_heritage_study_bible_lulu_print_proof.pdf`: Lulu-ready upload PDF.
- `the_greek_heritage_study_bible_lulu_print_proof_pdf_headers.json`: PDF page-header diagnostics.
- `the_greek_heritage_study_bible_lulu_print_proof_pandoc.pdf`: optional Pandoc/XeLaTeX PDF with two-column footnotes.

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
- Footnote layout: compact single-column PDF footnotes; 7.5pt Latin text; 6.5pt complex-script text; 8.5pt note markers; DOCX includes a Word-only two-column footnote hint.
- Alternate PDF renderer: Pandoc/XeLaTeX target renders two-column footnotes; PDF stamping resets visible blue note numbers by page because TeX-side per-page reset exceeds XeTeX capacity.
- Pericope headings: 3040 BSB-placement original headings included.
- Front preface pages discuss the purpose of the draft and rough translation methodology.
- Executive PDF profile abandoned; it did not save enough size versus Letter to justify maintaining.
- Lulu PDF build stamps page numbers and chapter/verse ranges into the top margin after pagination.
- Print note label legend: T = translation note; Txt = textual note; MT/LXX = Masoretic/LXX difference; Heb = Hebrew divine title; Gk = Greek form or Greek LXX divine title; Tr = transliterated proper noun; Std = standard English equivalent; Src = source form; Nm = name meaning; Pn = personal name; Pl = place name; Ppl = people name; Div = divine or supernatural name; Eng = common English rendering.
- Name-meaning notes are included only at their listed first/source occurrence to keep the physical proof shorter.
- Book preface pages included.
- Brenton/source supplemental notes excluded.
- Generated TSK/OpenBible cross-reference footnotes are excluded from the physical proof; use the Logos/reference-note edition for dense cross-references.

Counts:

- Verses: `30866`
- Book preface pages: `66`
- Translation/textual note footnotes: `4001`
- Name-meaning footnotes: `2816`
- Cross-reference footnotes: `27820`
- Cross-reference refs kept: `104121`
- Supplemental/Brenton footnotes: `0`

Rebuild:

```bash
make build-print-proof-lulu-pdf
make build-print-proof-lulu-pandoc-pdf
```
