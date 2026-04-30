# NT TR Review Pass 147

Scope: 2 Corinthians 8-9 focused queue rows after pass 146.

## 2 Corinthians 8:22
- status: `revised`
- decision: Remove inherited "oftentimes" and "which I have" wording; keep dokimazo/spoudaios as proved/diligent.

## 2 Corinthians 9:2
- status: `revised`
- decision: Render prothumian as "readiness," Macedosin as "Macedonians," and tous pleionas as "the majority."

## 2 Corinthians 9:7
- status: `revised`
- decision: Render hekastos as "each one" and ek lupes as "from sorrow" rather than "grudgingly."

## 2 Corinthians 9:14
- status: `revised`
- decision: Repair the inherited relative-clause break and render huperballousan charin as "surpassing grace."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '2 Corinthians 8:22,2 Corinthians 9:2,2 Corinthians 9:7,2 Corinthians 9:14'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
