# NT Review Pass 185

Scope: 1 Peter 3-5 focused queue rows after pass 184.

## 1 Peter 3:3
- status: `revised`
- decision: Render kosmos as "adornment" and keep the outward-adornment items direct.

## 1 Peter 3:11
- status: `revised`
- decision: Render ekklina as "turn away."

## 1 Peter 4:2
- status: `revised`
- decision: Render epiloipon chronon as "remaining time" and epithymiais as "desires."

## 1 Peter 4:9
- status: `revised`
- decision: Render philoxenoi as "Be hospitable" and gongysmon as "grumblings."

## 1 Peter 4:15
- status: `revised`
- decision: Render allotrioepiskopos as "meddler in others' matters."

## 1 Peter 4:18
- status: `revised`
- decision: Render molis as "with difficulty."

## 1 Peter 5:3
- status: `revised`
- decision: Render katakyrieuontes as "lording it over" and ton kleron as "the allotted portions."

## 1 Peter 5:6
- status: `keep`
- decision: Retain the current humble/mighty-hand wording as direct.

## 1 Peter 5:7
- status: `revised`
- decision: Render merimnan as "anxiety."

## 1 Peter 5:8
- status: `revised`
- decision: Render gregoresate as "watch" and keep the roaring-lion image direct.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '1 Peter 3:3,1 Peter 3:11,1 Peter 4:2,1 Peter 4:9,1 Peter 4:15,1 Peter 4:18,1 Peter 5:3,1 Peter 5:6,1 Peter 5:7,1 Peter 5:8'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
