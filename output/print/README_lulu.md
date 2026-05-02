# Print Proof Files

Generated files:

- `the_greek_heritage_study_bible_lulu_print_proof.docx`: compact DOCX for inexpensive physical proofreading.
- `the_greek_heritage_study_bible_lulu_print_proof_diagnostics.json`: build counts and DOCX validation details.
- `the_greek_heritage_study_bible_lulu_print_proof.pdf`: Lulu-ready upload PDF.

Profile:

- Combined Genesis-Revelation text.
- OT source: LXX Greek source rows; NT source: Scrivener 1894 Textus Receptus Greek source rows.
- Compact single-column DOCX layout with Lulu-safe mirrored POD margins.
- Page size: US Letter 8.5 x 11 in.
- Margins: mirrored; inside 1.0 in; outside 0.75 in; top/bottom 0.5 in.
- Front matter includes an LXX-to-English numbering guide for major reader-facing divergences.
- Reviewed translation/textual notes included.
- Type profile: lulu_tight_leading_9_5pt.
- Print note label legend: T = translation note; Txt = textual note; MT/LXX = Masoretic/LXX difference; Heb = Hebrew divine title; Gk = Greek form or Greek LXX divine title; Tr = transliterated proper noun; Std = standard English equivalent; Src = source form; Nm = name meaning; Pn = personal name; Pl = place name; Ppl = people name; Div = divine or supernatural name; Eng = common English rendering.
- Name-meaning notes are included only at their listed first/source occurrence to keep the physical proof shorter.
- Book preface pages excluded for POD page-count limits.
- Brenton/source supplemental notes excluded.
- Generated TSK/OpenBible cross-reference footnotes are excluded from the physical proof; use the Logos/reference-note edition for dense cross-references.

Counts:

- Verses: `30866`
- Book preface pages: `0`
- Translation/textual note footnotes: `4001`
- Name-meaning footnotes: `2816`
- Cross-reference footnotes: `0`
- Cross-reference refs kept: `0`
- Supplemental/Brenton footnotes: `0`

Rebuild:

```bash
make build-print-proof-lulu-pdf
```
