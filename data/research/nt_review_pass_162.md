# NT Review Pass 162

Scope: Philippians 3-4 focused queue rows after pass 161.

## Philippians 3:2
- status: `revised`
- decision: Render katatome as "mutilation" rather than inherited "concision."

## Philippians 3:7
- status: `revised`
- decision: Render plural kerde as "gains," hegemai as "have counted," and dia ton Christon as "because of Christ."

## Philippians 3:12
- status: `revised`
- decision: Replace archaic "apprehend" wording with "lay hold" language and render the perfect passive as "have already been perfected."

## Philippians 3:14
- status: `revised`
- decision: Render skopon as "goal" and ano kleseos as "upward calling."

## Philippians 3:16
- status: `revised`
- decision: Keep TR wording for the same rule and same mind, while modernizing "whereto."

## Philippians 3:18
- status: `revised`
- decision: Tighten the clause around the many who walk as enemies of the cross of Christ.

## Philippians 3:19
- status: `keep`
- decision: Retain the current wording; it already preserves the destruction, belly, shame, and earthly-minded clauses clearly.

## Philippians 4:18
- status: `revised`
- decision: Render panta as "all things," para Epaphroditou as "from Epaphroditus," and osmen euodias as "an aroma of sweet smell."

## Philippians 4:19
- status: `revised`
- decision: Render plerosei as "shall fill," pasan chreian hymon as "every need of yours," and en Christo Iesou as "in Christ Jesus."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Philippians 3:2,Philippians 3:7,Philippians 3:12,Philippians 3:14,Philippians 3:16,Philippians 3:18,Philippians 3:19,Philippians 4:18,Philippians 4:19'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
