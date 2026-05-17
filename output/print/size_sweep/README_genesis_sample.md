# Print Proof Files

Generated files:

- `genesis_sample.docx`: compact DOCX for inexpensive physical proofreading.
- `genesis_sample_diagnostics.json`: build counts and DOCX validation details.
- `genesis_sample.pdf`: Lulu-ready upload PDF.
- `genesis_sample_pdf_headers.json`: PDF page-header diagnostics.
- `genesis_sample_pandoc.pdf`: optional Pandoc/XeLaTeX PDF with two-column footnotes.

Profile:

- Combined Genesis-Revelation text.
- OT source: LXX Greek source rows; NT source: Scrivener 1894 Textus Receptus Greek source rows.
- Compact single-column DOCX layout with Lulu-safe mirrored POD margins and run-in verse paragraphs.
- Page size: US Letter 8.5 x 11 in.
- Margins: mirrored; inside 0.75 in; outside 0.5 in; top/bottom 0.5 in.
- Front matter includes an LXX-to-English numbering guide for major reader-facing divergences.
- Reviewed translation/textual notes included.
- Type profile: lulu_tight_leading_9_5pt.
- Verse layout: chapter-continuous run-in paragraphs.
- Footnote layout: compact single-column PDF footnotes; 7.5pt Latin text; 6.5pt complex-script text; 8.5pt note markers; DOCX includes a Word-only two-column footnote hint.
- Alternate PDF renderer: Pandoc/XeLaTeX target renders two-column footnotes with per-page footnote numbering..
- Pericope headings: 31 original headings included.
- Lulu PDF build stamps page numbers and chapter/verse ranges into the top margin after pagination.
- Print note label legend: T = translation note; Txt = textual note; MT/LXX = Masoretic/LXX difference; Heb = Hebrew divine title; Gk = Greek form or Greek LXX divine title; Tr = transliterated proper noun; Std = standard English equivalent; Src = source form; Nm = name meaning; Pn = personal name; Pl = place name; Ppl = people name; Div = divine or supernatural name; Eng = common English rendering.
- Name-meaning notes are included only at their listed first/source occurrence to keep the physical proof shorter.
- Book preface pages excluded for POD page-count limits.
- Brenton/source supplemental notes excluded.
- Generated TSK/OpenBible cross-reference footnotes are excluded from the physical proof; use the Logos/reference-note edition for dense cross-references.

Counts:

- Verses: `1531`
- Book preface pages: `0`
- Translation/textual note footnotes: `183`
- Name-meaning footnotes: `426`
- Cross-reference footnotes: `0`
- Cross-reference refs kept: `0`
- Supplemental/Brenton footnotes: `0`

Rebuild:

```bash
make build-print-proof-lulu-pdf
```
