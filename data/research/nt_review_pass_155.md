# NT Review Pass 155

Scope: Galatians 5-6 focused queue rows after pass 154.

## Galatians 5:3
- status: `revised`
- decision: Render de as "And," modernize "that is circumcised" to "who is circumcised," and keep the debtor clause.

## Galatians 5:9
- status: `keep`
- decision: Keep the leaven proverb; it is already literal and clear.

## Galatians 5:12
- status: `revised`
- decision: Render anastatountes as "unsettle" and preserve the cutting-off force of apokopsontai.

## Galatians 5:23
- status: `revised`
- decision: Replace the inherited "wilful restrain" error with "self-control."

## Galatians 5:26
- status: `revised`
- decision: Render kenodoxoi as "vain-glorious" and keep the reciprocal participles.

## Galatians 6:3
- status: `revised`
- decision: Use "anyone" for tis and tighten the being-nothing clause.

## Galatians 6:4
- status: `revised`
- decision: Render hekastos as "each one" and kauchema as "boasting."

## Galatians 6:5
- status: `revised`
- decision: Render phortion as "load" to distinguish it from the burdens in 6:2.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Galatians 5:3,Galatians 5:9,Galatians 5:12,Galatians 5:23,Galatians 5:26,Galatians 6:3,Galatians 6:4,Galatians 6:5'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
