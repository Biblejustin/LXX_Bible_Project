# NT Review Pass 180

Scope: Hebrews 11:20-40 focused queue rows after pass 179, plus adjacent Hebrews 11:22 and 11:27.

## Hebrews 11:20
- status: `keep`
- decision: Retain the current Isaac blessing wording as direct.

## Hebrews 11:22
- status: `revised`
- decision: Render teleuton as "when dying" and exodou as "exodus."

## Hebrews 11:23
- status: `revised`
- decision: Render ekrubi as "was hidden," hupo ton pateron as "by his parents," asteion as "beautiful," and diatagma as "decree."

## Hebrews 11:25
- status: `revised`
- decision: Render proskairon as "temporary" and apolausin as "enjoyment."

## Hebrews 11:27
- status: `revised`
- decision: Render katelipen as "left" and keep the invisible-one clause direct.

## Hebrews 11:29
- status: `revised`
- decision: Render hos dia xiras as "as through dry land" and katepothisan as "were swallowed."

## Hebrews 11:30
- status: `revised`
- decision: Render kuklothenta as "having been encircled."

## Hebrews 11:35
- status: `revised`
- decision: Render ex anastaseos as "by resurrection" and apolutrosin as "release."

## Hebrews 11:38
- status: `revised`
- decision: Remove supplied parenthetical punctuation and render opais as "holes."

## Hebrews 11:40
- status: `revised`
- decision: Render peri humon as "concerning us" and move "without us" to the end for clarity.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Hebrews 11:20,Hebrews 11:22,Hebrews 11:23,Hebrews 11:25,Hebrews 11:27,Hebrews 11:29,Hebrews 11:30,Hebrews 11:35,Hebrews 11:38,Hebrews 11:40'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
