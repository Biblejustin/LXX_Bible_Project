# NT Review Pass 159

Scope: Ephesians 5-6 focused queue rows after pass 158.

## Ephesians 5:4
- status: `revised`
- decision: Replace archaic "convenient" with "fitting" and render eucharistia as "thanksgiving."

## Ephesians 5:11
- status: `revised`
- decision: Keep fellowship language and include kai before "reprove" as "even."

## Ephesians 5:12
- status: `revised`
- decision: Render ta kryphe ginomena as "the secret things being done" and aischron as "shameful."

## Ephesians 5:16
- status: `keep`
- decision: Keep "Redeeming the time"; it is literal and clear.

## Ephesians 5:21
- status: `revised`
- decision: Remove supplied "yourselves" and keep the fear-of-God phrase.

## Ephesians 5:30
- status: `keep`
- decision: Keep the body/flesh/bones wording because it matches the TR line.

## Ephesians 5:33
- status: `revised`
- decision: Render kath' hena hekastos as "each one" and keep reverence for phobetai.

## Ephesians 6:3
- status: `keep`
- decision: Keep the promise quote; it is clear and literal.

## Ephesians 6:14
- status: `revised`
- decision: Replace "girt about" with "having girded" and render endysamenoi as "having put on."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Ephesians 5:4,Ephesians 5:11,Ephesians 5:12,Ephesians 5:16,Ephesians 5:21,Ephesians 5:30,Ephesians 5:33,Ephesians 6:3,Ephesians 6:14'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
