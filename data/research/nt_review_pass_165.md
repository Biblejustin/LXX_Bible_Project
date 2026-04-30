# NT Review Pass 165

Scope: 2 Thessalonians focused queue rows after pass 164.

## 2 Thessalonians 2:7
- status: `revised`
- decision: Replace archaic "lets will let" with restraining language and render ek mesou as "out of the midst."

## 2 Thessalonians 2:9
- status: `revised`
- decision: Render kata as "according to" and terasin pseudous as "wonders of falsehood."

## 2 Thessalonians 2:11
- status: `revised`
- decision: Replace "for this cause" with "because of this" and render energeian planes as "a working of error."

## 2 Thessalonians 3:2
- status: `revised`
- decision: Keep "unreasonable" for atopon, render poneron as "evil," and preserve the article in "the faith."

## 2 Thessalonians 3:10
- status: `revised`
- decision: Render ei tis as "if anyone," ou thelei as "is not willing," and the imperative as "let him eat."

## 2 Thessalonians 3:11
- status: `revised`
- decision: Modernize "some which" and preserve the working/busybodies contrast.

## 2 Thessalonians 3:15
- status: `revised`
- decision: Render hegeisthe as "regard" and modernize the negative imperative.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '2 Thessalonians 2:7,2 Thessalonians 2:9,2 Thessalonians 2:11,2 Thessalonians 3:2,2 Thessalonians 3:10,2 Thessalonians 3:11,2 Thessalonians 3:15'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
