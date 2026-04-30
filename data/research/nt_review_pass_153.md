# NT Review Pass 153

Scope: Galatians 3 focused queue rows after pass 152.

## Galatians 3:6
- status: `revised`
- decision: Match Romans 4 reckoning language and render kathos as "Just as."

## Galatians 3:10
- status: `revised`
- decision: Render ex ergon nomou as "from works of law," use "under a curse," and modernize the quoted curse.

## Galatians 3:12
- status: `revised`
- decision: Render ek pisteos as "from faith" and modernize the quoted "man who does them" clause.

## Galatians 3:13
- status: `revised`
- decision: Render the aorist as "redeemed" and genomenos as "having become" while modernizing the tree quote.

## Galatians 3:18
- status: `revised`
- decision: Render ek nomou/ex epangelias as "from law/from promise" and kecharistai as graciously granted.

## Galatians 3:20
- status: `revised`
- decision: Remove the repeated inserted "mediator" and keep the one/God contrast concise.

## Galatians 3:25
- status: `revised`
- decision: Replace inherited "after that faith has come" with clearer "after faith came."

## Galatians 3:27
- status: `keep`
- decision: Keep the current baptized-into-Christ wording; it is clear and close.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Galatians 3:6,Galatians 3:10,Galatians 3:12,Galatians 3:13,Galatians 3:18,Galatians 3:20,Galatians 3:25,Galatians 3:27'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
