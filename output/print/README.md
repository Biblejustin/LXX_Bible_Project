# Print Proof Files

Generated files:

- `the_greek_heritage_study_bible_print_proof.docx`: compact DOCX for inexpensive physical proofreading.
- `the_greek_heritage_study_bible_print_proof_diagnostics.json`: build counts and DOCX validation details.

Profile:

- Combined Genesis-Revelation text.
- OT source: LXX Greek source rows; NT source: Scrivener 1894 Textus Receptus Greek source rows.
- Compact single-column DOCX layout with narrow margins.
- Page size: US Letter 8.5 x 11 in.
- Margins: top/bottom 0.5 in; left/right 0.375 in.
- Front matter includes an LXX-to-English numbering guide for major reader-facing divergences.
- Reviewed translation/textual notes included.
- Type profile: compact_9_5pt.
- Verse layout: one verse per paragraph.
- Footnote layout: active Pandoc PDF uses two-column footnotes; TeX-side page-local note numbers; green cross-reference letters; 7.5pt Latin text; 6.5pt complex-script text; 8.5pt note markers.
- Alternate PDF renderer: Pandoc/XeLaTeX is the active full-size print proof renderer; LibreOffice PDF output is disabled for print proof.
- Pericope headings: 2983 BSB-placement original headings included.
- Front preface pages discuss the purpose of the draft and rough translation methodology.
- Executive PDF profile abandoned; it did not save enough size versus Letter to justify maintaining.
- DOCX-only build does not stamp PDF page headers.
- Print note label legend: T = translation note; Txt = textual note; MT/LXX = Masoretic/LXX difference; Heb = Hebrew divine title; Gk = Greek form or Greek LXX divine title; Tr = transliterated proper noun; Std = standard English equivalent; Src = source form; Nm = name meaning; Pn = personal name; Pl = place name; Ppl = people name; Div = divine or supernatural name; Eng = common English rendering.
- Name-meaning notes are included only at their listed first/source occurrence to keep the physical proof shorter.
- Book preface pages included.
- Brenton/source supplemental notes excluded.
- Generated TSK/OpenBible cross-reference footnotes are excluded from the physical proof; use the Logos/reference-note edition for dense cross-references.

Counts:

- Verses: `30866`
- Book preface pages: `66`
- Translation/textual note footnotes: `3945`
- Name-meaning footnotes: `2812`
- Cross-reference footnotes: `0`
- Cross-reference refs kept: `0`
- Supplemental/Brenton footnotes: `0`

Rebuild:

```bash
make build-print-proof
```
