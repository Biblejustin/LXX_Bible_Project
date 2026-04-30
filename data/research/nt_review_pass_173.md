# NT Review Pass 173

Scope: Hebrews 1-2 focused queue rows after pass 172.

## Hebrews 1:4
- status: `revised`
- decision: Render genomenos as "having become" and kekleronomiken as "has inherited."

## Hebrews 1:6
- status: `revised`
- decision: Render prototokon as "firstborn" and oikoumenin as "inhabited world."

## Hebrews 1:9
- status: `revised`
- decision: Render anomian as "lawlessness" and metochous as "companions."

## Hebrews 1:12
- status: `revised`
- decision: Render peribolaion as "mantle" and helixeis as "roll them up."

## Hebrews 2:6
- status: `revised`
- decision: Render diemartyrato de pou tis as "someone somewhere testified."

## Hebrews 2:8
- status: `revised`
- decision: Render the hupotasso chain consistently as "subjected" and "unsubjected."

## Hebrews 2:15
- status: `revised`
- decision: Render douleias as "slavery" and keep the all-their-life fear-of-death clause direct.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Hebrews 1:4,Hebrews 1:6,Hebrews 1:9,Hebrews 1:12,Hebrews 2:6,Hebrews 2:8,Hebrews 2:15'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
