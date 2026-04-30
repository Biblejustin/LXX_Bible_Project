# NT Review Pass 152

Scope: Galatians 2 focused queue rows after pass 151.

## Galatians 2:1
- status: `revised`
- decision: Replace inherited "fourteen years after" word order with "after fourteen years" and render symparalabon as taking Titus also with him.

## Galatians 2:3
- status: `revised`
- decision: Render oude as "not even" and keep the compelled-to-be-circumcised clause.

## Galatians 2:10
- status: `revised`
- decision: Remove inherited filler and render auto touto as "the very thing."

## Galatians 2:18
- status: `revised`
- decision: Use "things that I destroyed" and render synistemi as "establish" for the transgressor clause.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Galatians 2:1,Galatians 2:3,Galatians 2:10,Galatians 2:18'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
