# NT Review Pass 158

Scope: Ephesians 4 focused queue rows after pass 157.

## Ephesians 4:6
- status: `revised`
- decision: Render epi panton as "over all" while keeping "in you all" from the TR line.

## Ephesians 4:9
- status: `revised`
- decision: Make the citation gloss explicit as "Now this, He ascended" and keep the descent clause.

## Ephesians 4:11
- status: `revised`
- decision: Restore autos as "he himself" and clarify the appositional gift list with "as."

## Ephesians 4:18
- status: `revised`
- decision: Render the participial opening directly and porosis as "hardness" rather than "blindness."

## Ephesians 4:27
- status: `keep`
- decision: Keep the current devil/place line; it is already literal and clear.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Ephesians 4:6,Ephesians 4:9,Ephesians 4:11,Ephesians 4:18,Ephesians 4:27'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
