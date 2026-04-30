# NT Review Pass 179

Scope: Hebrews 11:1-18 focused queue rows after pass 178.

## Hebrews 11:1
- status: `keep`
- decision: Retain the current substance/evidence wording as direct and familiar.

## Hebrews 11:2
- status: `revised`
- decision: Render emarturithisan as "obtained testimony."

## Hebrews 11:5
- status: `revised`
- decision: Render tou mi idein thanaton as "so that he should not see death" and memarturitai as "had testimony."

## Hebrews 11:7
- status: `revised`
- decision: Render peri ton midepo blepomenon as "concerning things not yet seen" and dia his as "through which."

## Hebrews 11:8
- status: `revised`
- decision: Render kaloumenos as "when called" and imellen lambanein as "was about to receive."

## Hebrews 11:9
- status: `revised`
- decision: Render allotrian as "foreign land" and sugklironomon as "co-heirs."

## Hebrews 11:10
- status: `revised`
- decision: Render exedecheto as "waited for."

## Hebrews 11:12
- status: `revised`
- decision: Render egenithisan as "were begotten" and smooth the one-as-good-as-dead clause.

## Hebrews 11:13
- status: `revised`
- decision: Render kata pistin as "according to faith" and aspasamenoi as "greeted them."

## Hebrews 11:18
- status: `revised`
- decision: Correct pros hon from "Of whom" to "to whom."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Hebrews 11:1,Hebrews 11:2,Hebrews 11:5,Hebrews 11:7,Hebrews 11:8,Hebrews 11:9,Hebrews 11:10,Hebrews 11:12,Hebrews 11:13,Hebrews 11:18'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
