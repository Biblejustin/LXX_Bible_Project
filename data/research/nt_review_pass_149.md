# NT TR Review Pass 149

Scope: 2 Corinthians 11 focused queue rows after pass 148.

## 2 Corinthians 11:2
- status: `revised`
- decision: Render zeloo as "jealous," theou zelo as "God's jealousy," and hagnan as "pure."

## 2 Corinthians 11:13
- status: `revised`
- decision: Remove inherited article before "apostles of Christ" and keep pseudoapostoloi as "false apostles."

## 2 Corinthians 11:14
- status: `revised`
- decision: Replace "no marvel" with "no wonder" and keep the reflexive transformation.

## 2 Corinthians 11:15
- status: `revised`
- decision: Render diakonoi as "servants" and keep the reflexive transformation.

## 2 Corinthians 11:21
- status: `revised`
- decision: Tighten the dishonor/weakness clause and remove the inherited parenthetical break.

## 2 Corinthians 11:22
- status: `keep`
- decision: Keep the current Hebrews/Israelites/seed of Abraham sequence. It is clear and close.

## 2 Corinthians 11:24
- status: `revised`
- decision: Remove inverted word order and replace "save one" with "minus one."

## 2 Corinthians 11:25
- status: `revised`
- decision: Remove inherited inversions and render nuchthemeron in the deep as time spent there.

## 2 Corinthians 11:27
- status: `revised`
- decision: Replace "weariness and painfulness" with "labor and hardship."

## 2 Corinthians 11:32
- status: `revised`
- decision: Render ephrourrei as "guarded" and piasai as "seize."

## 2 Corinthians 11:33
- status: `revised`
- decision: Remove inherited inversion and keep the basket/window/wall sequence.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '2 Corinthians 11:2,2 Corinthians 11:13,2 Corinthians 11:14,2 Corinthians 11:15,2 Corinthians 11:21,2 Corinthians 11:22,2 Corinthians 11:24,2 Corinthians 11:25,2 Corinthians 11:27,2 Corinthians 11:32,2 Corinthians 11:33'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
