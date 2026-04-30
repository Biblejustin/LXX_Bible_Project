# NT Review Pass 161

Scope: Philippians 2 focused queue rows after pass 160.

## Philippians 2:4
- status: `revised`
- decision: Render hekastos as "each" and remove inherited "every man."

## Philippians 2:5
- status: `revised`
- decision: Restore gar as "For" and keep the Christ Jesus clause.

## Philippians 2:6
- status: `revised`
- decision: Replace the "robbery" idiom with a more direct rendering of harpagmos as "a thing to be seized."

## Philippians 2:14
- status: `revised`
- decision: Render goggysmon as grumblings and dialogismon as reasonings.

## Philippians 2:21
- status: `revised`
- decision: Restore Christ Jesus word order and make "things" explicit on both sides.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Philippians 2:4,Philippians 2:5,Philippians 2:6,Philippians 2:14,Philippians 2:21'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
