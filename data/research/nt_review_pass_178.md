# NT Review Pass 178

Scope: Hebrews 10 focused queue rows after pass 177.

## Hebrews 10:3
- status: `revised`
- decision: Remove supplied "sacrifices" and render en autais as "in them."

## Hebrews 10:4
- status: `revised`
- decision: Tighten the infinitive clause: blood of bulls and goats cannot take away sins.

## Hebrews 10:6
- status: `revised`
- decision: Render peri hamartias as "offerings for sin."

## Hebrews 10:11
- status: `revised`
- decision: Modernize "oftentimes" to "often."

## Hebrews 10:17
- status: `revised`
- decision: Render anomion as "lawless deeds."

## Hebrews 10:20
- status: `revised`
- decision: Render enekainisen as "inaugurated" and keep prosphaton as "new."

## Hebrews 10:22
- status: `revised`
- decision: Render the singular soma as "body" and keep the sprinkled/washed clauses direct.

## Hebrews 10:26
- status: `revised`
- decision: Render hekousios as "willingly" and remove the supplied "after that we have."

## Hebrews 10:27
- status: `revised`
- decision: Render ekdochi as "expectation" and puros zilos as "fiery zeal."

## Hebrews 10:31
- status: `keep`
- decision: Retain the current living God wording as direct.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Hebrews 10:3,Hebrews 10:4,Hebrews 10:6,Hebrews 10:11,Hebrews 10:17,Hebrews 10:20,Hebrews 10:22,Hebrews 10:26,Hebrews 10:27,Hebrews 10:31'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
