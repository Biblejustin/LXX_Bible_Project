# NT Review Pass 154

Scope: Galatians 4 focused queue rows after pass 153.

## Galatians 4:2
- status: `revised`
- decision: Render epitropous/oikonomous as "guardians and stewards" and make the implied heir explicit.

## Galatians 4:3
- status: `revised`
- decision: Render dedoulomenoi as "enslaved" and keep the elements-of-the-world clause.

## Galatians 4:16
- status: `revised`
- decision: Render hoste as "So then" and alētheuōn as "telling you the truth."

## Galatians 4:18
- status: `revised`
- decision: Replace archaic "zealously affected" with "be zealous" while keeping the good-thing phrase.

## Galatians 4:19
- status: `revised`
- decision: Use "for whom" and "is formed" for the birth-labor clause.

## Galatians 4:20
- status: `revised`
- decision: Replace "stand in doubt of you" with "am perplexed about you."

## Galatians 4:22
- status: `revised`
- decision: Harmonize paidiske wording as "bondwoman" and render ek as "from."

## Galatians 4:23
- status: `revised`
- decision: Render kata sarka as "according to flesh" and dia tes epangelias as "through promise."

## Galatians 4:26
- status: `revised`
- decision: Tighten "Jerusalem which is above" to "the Jerusalem above."

## Galatians 4:30
- status: `revised`
- decision: Replace "nevertheless" with "but," modernize the scripture question, and render kleronomese as "inherit."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Galatians 4:2,Galatians 4:3,Galatians 4:16,Galatians 4:18,Galatians 4:19,Galatians 4:20,Galatians 4:22,Galatians 4:23,Galatians 4:26,Galatians 4:30'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
