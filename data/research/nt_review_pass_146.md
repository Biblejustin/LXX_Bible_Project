# NT TR Review Pass 146

Scope: 2 Corinthians 6-8 focused queue rows after pass 145.

## 2 Corinthians 6:4
- status: `revised`
- decision: Render sunistontes as "commending," diakonoi as "servants," and hupomone as "endurance."

## 2 Corinthians 6:10
- status: `keep`
- decision: Keep the current sorrowful/rejoicing and poor/enriching contrast. The wording matches the Greek closely enough.

## 2 Corinthians 7:6
- status: `revised`
- decision: Render all as "But," tapeinous as "the lowly," and parousia as "presence."

## 2 Corinthians 7:8
- status: `revised`
- decision: Render metamelomai as "regret" and keep the letter's grief as short-lived.

## 2 Corinthians 7:10
- status: `revised`
- decision: Render kata theon as "according to God" and ametameleton as "without regret."

## 2 Corinthians 7:16
- status: `keep`
- decision: Keep the current confidence wording. It is clear and matches en panti tharrou en humin.

## 2 Corinthians 8:13
- status: `revised`
- decision: Repair the verse split so the equality clause and present abundance phrase stay with the Greek row.

## 2 Corinthians 8:14
- status: `revised`
- decision: Remove duplicated prior-verse material and keep this row to their abundance answering your lack.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '2 Corinthians 6:4,2 Corinthians 6:10,2 Corinthians 7:6,2 Corinthians 7:8,2 Corinthians 7:10,2 Corinthians 7:16,2 Corinthians 8:13,2 Corinthians 8:14'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
