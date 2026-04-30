# NT Review Pass 175

Scope: Hebrews 5-6 focused queue rows after pass 174.

## Hebrews 5:1
- status: `revised`
- decision: Render kathistatai as "is appointed" and huper anthropon as "on behalf of men."

## Hebrews 5:8
- status: `revised`
- decision: Modernize the concession and render aph' hon as "from the things which."

## Hebrews 6:2
- status: `revised`
- decision: Render didachis as "teaching" and keep the genitive chain continuous with Hebrews 6:1.

## Hebrews 6:3
- status: `revised`
- decision: Modernize the word order and render epitrep as "permits."

## Hebrews 6:9
- status: `revised`
- decision: Render peri humon as "concerning you" and echomena sotirias as "things belonging to salvation."

## Hebrews 6:13
- status: `revised`
- decision: Render epangeilamenos as "promised" and keep the no-greater-oath logic direct.

## Hebrews 6:14
- status: `keep`
- decision: Retain the emphatic "blessing I will bless" and "multiplying I will multiply" wording because the Greek repeats both verbs.

## Hebrews 6:15
- status: `revised`
- decision: Render makrothumisas as "having patiently endured."

## Hebrews 6:18
- status: `revised`
- decision: Render ischuran paraklisin as "strong encouragement" and clarify the subject as "we who have fled for refuge."

## Hebrews 6:19
- status: `revised`
- decision: Render esoteron tou katapetasmatos as "the inner side of the veil."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Hebrews 5:1,Hebrews 5:8,Hebrews 6:2,Hebrews 6:3,Hebrews 6:9,Hebrews 6:13,Hebrews 6:14,Hebrews 6:15,Hebrews 6:18,Hebrews 6:19'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
