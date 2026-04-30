# NT Review Pass 184

Scope: 1 Peter 1-2 focused queue rows after pass 183.

## 1 Peter 1:4
- status: `revised`
- decision: Render aphtharton, amianton, and amaranton as "incorruptible," "undefiled," and "unfading," with "heavens" plural.

## 1 Peter 1:9
- status: `revised`
- decision: Remove supplied "even" and retain "salvation of your souls."

## 1 Peter 1:14
- status: `revised`
- decision: Render tekna hypakoes as "children of obedience" and epithymiais as "desires."

## 1 Peter 1:19
- status: `revised`
- decision: Render amomou and aspilou as "without blemish" and "without spot."

## 1 Peter 2:10
- status: `revised`
- decision: Modernize the relative clauses and retain the mercy contrast.

## 1 Peter 2:11
- status: `revised`
- decision: Render agapetoi as "Beloved," parakalo as "exhort," and epithymion as "desires."

## 1 Peter 2:18
- status: `revised`
- decision: Render oiketai as "Household servants" and en panti phobo as "in all fear."

## 1 Peter 2:19
- status: `revised`
- decision: Render touto gar charis as "For this is grace" and adikos as "unjustly."

## 1 Peter 2:22
- status: `revised`
- decision: Render dolos as "deceit."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '1 Peter 1:4,1 Peter 1:9,1 Peter 1:14,1 Peter 1:19,1 Peter 2:10,1 Peter 2:11,1 Peter 2:18,1 Peter 2:19,1 Peter 2:22'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
