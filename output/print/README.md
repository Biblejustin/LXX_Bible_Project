# Print Proof Files

Generated files:

- `the_greek_heritage_study_bible_print_proof.docx`: compact DOCX for inexpensive physical proofreading.
- `the_greek_heritage_study_bible_print_proof_diagnostics.json`: build counts and DOCX validation details.

Profile:

- Combined Genesis-Revelation text.
- OT source: LXX Greek source rows; NT source: Scrivener 1894 Textus Receptus Greek source rows.
- Compact two-column DOCX layout with narrow margins.
- Front matter includes an LXX-to-English numbering guide for major reader-facing divergences.
- Reviewed translation/textual notes included.
- Name-meaning notes are included only at their listed first/source occurrence to keep the physical proof shorter.
- Book preface pages excluded.
- Brenton/source supplemental notes excluded.
- Minimal cross-reference layer: TSK phrase-anchored references only, no OpenBible fallback, capped to one cross-reference footnote per verse and two references per footnote.

Counts:

- Verses: `30866`
- Translation/textual note footnotes: `4001`
- Name-meaning footnotes: `2816`
- Cross-reference footnotes: `12902`
- Cross-reference refs kept: `24110`
- Supplemental/Brenton footnotes: `0`

Rebuild:

```bash
make build-print-proof
```
