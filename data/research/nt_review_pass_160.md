# NT Review Pass 160

Scope: Philippians 1 focused queue rows after pass 159.

## Philippians 1:3
- status: `revised`
- decision: Render epi pase te mneia as "at every remembrance."

## Philippians 1:4
- status: `revised`
- decision: Remove inherited inversion and keep the repeated prayer phrase visible.

## Philippians 1:13
- status: `revised`
- decision: Render genesthai as "became," praitorio as praetorium, and tois loipois pasin as "all the rest."

## Philippians 1:15
- status: `revised`
- decision: Render dia as "through" and keep both envy/strife and good will.

## Philippians 1:16
- status: `revised`
- decision: Replace ungrammatical inherited singular with a plural subject and render eritheia as selfish ambition.

## Philippians 1:21
- status: `revised`
- decision: Remove the "In order to me" artifact and restore the simple to-live/to-die clause.

## Philippians 1:24
- status: `revised`
- decision: Render de as "But" and epimenein as "remain."

## Philippians 1:25
- status: `revised`
- decision: Render prokope as "progress" and keep joy tied to the faith.

## Philippians 1:26
- status: `revised`
- decision: Render kauchema as "boasting" and parousia as "presence."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Philippians 1:3,Philippians 1:4,Philippians 1:13,Philippians 1:15,Philippians 1:16,Philippians 1:21,Philippians 1:24,Philippians 1:25,Philippians 1:26'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
