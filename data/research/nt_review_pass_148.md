# NT TR Review Pass 148

Scope: 2 Corinthians 10 focused queue rows after pass 147.

## 2 Corinthians 10:1
- status: `revised`
- decision: Render kata prosopon as "in person" and tapeinos as "lowly," removing inherited "base" wording.

## 2 Corinthians 10:3
- status: `revised`
- decision: Render kata sarka as "according to flesh" and strateuometha as "wage war."

## 2 Corinthians 10:4
- status: `revised`
- decision: Render sarkika as "fleshly" and close the broken "strong holds" spelling.

## 2 Corinthians 10:5
- status: `revised`
- decision: Render logismous as "reasonings" and aichmalotizontes as taking every thought captive.

## 2 Corinthians 10:6
- status: `revised`
- decision: Render ekdikesai as "avenge" and plerothe as "completed."

## 2 Corinthians 10:9
- status: `keep`
- decision: Keep "terrify you by letters." It matches ekphobein humas dia ton epistolon clearly enough.

## 2 Corinthians 10:12
- status: `revised`
- decision: Replace inherited "make ourselves of the number" and render ou syniousin as "do not understand."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '2 Corinthians 10:1,2 Corinthians 10:3,2 Corinthians 10:4,2 Corinthians 10:5,2 Corinthians 10:6,2 Corinthians 10:9,2 Corinthians 10:12'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
