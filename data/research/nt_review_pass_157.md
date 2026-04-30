# NT Review Pass 157

Scope: Ephesians 2-3 focused queue rows after pass 156.

## Ephesians 2:14
- status: `revised`
- decision: Restore autos as "himself," use aorist "made/broke down," and remove inherited "between us."

## Ephesians 2:20
- status: `revised`
- decision: Preserve Christ Jesus word order and normalize "chief cornerstone."

## Ephesians 3:9
- status: `revised`
- decision: Render pantas as "all," tous aionas as "the ages," and apokekrymmenou as "hidden."

## Ephesians 3:12
- status: `revised`
- decision: Render dia tes pisteos autou as "through his faith."

## Ephesians 3:15
- status: `revised`
- decision: Render pasa patria as "every family" and keep heavens/earth explicit.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Ephesians 2:14,Ephesians 2:20,Ephesians 3:9,Ephesians 3:12,Ephesians 3:15'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
