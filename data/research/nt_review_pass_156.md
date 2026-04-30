# NT Review Pass 156

Scope: Ephesians 1 focused queue rows after pass 155.

## Ephesians 1:10
- status: `revised`
- decision: Render oikonomia as dispensation, anakephalaiosasthai as "sum up," and keep the heavens/earth pairing explicit.

## Ephesians 1:11
- status: `revised`
- decision: Replace "predestinated" with "predestined" and remove inherited "own" from the counsel-of-will clause.

## Ephesians 1:12
- status: `revised`
- decision: Render proelpikotas as "first hoped" rather than "first trusted."

## Ephesians 1:16
- status: `revised`
- decision: Replace inherited "Cease not" inversion with "I do not cease."

## Ephesians 1:19
- status: `revised`
- decision: Render hyperballon megethos as "surpassing greatness" and keep might/strength distinct.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Ephesians 1:10,Ephesians 1:11,Ephesians 1:12,Ephesians 1:16,Ephesians 1:19'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
