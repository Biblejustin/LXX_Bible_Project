# NT Review Pass 181

Scope: Hebrews 12-13 focused queue rows after pass 180.

## Hebrews 12:13
- status: `keep`
- decision: Retain the current straight-paths wording as direct.

## Hebrews 12:20
- status: `keep`
- decision: Retain the current commanded/mountain warning wording as direct.

## Hebrews 12:21
- status: `revised`
- decision: Render phantazomenon as "appearance," ekphobos as "terrified," and entromos as "trembling."

## Hebrews 12:26
- status: `keep`
- decision: Retain the current shook-earth/heaven wording as direct.

## Hebrews 12:27
- status: `revised`
- decision: Render deloi as "signifies," metathesin as "removal," and keep the shaken/not-shaken contrast explicit.

## Hebrews 12:29
- status: `keep`
- decision: Retain the current consuming-fire wording as direct.

## Hebrews 13:1
- status: `keep`
- decision: Retain the current brotherly-love wording as direct.

## Hebrews 13:11
- status: `revised`
- decision: Render zoun as "animals," ta hagia as "holy places," and exo tes paremboles as "outside the camp."

## Hebrews 13:14
- status: `revised`
- decision: Modernize word order while retaining "continuing city" and "one to come."

## Hebrews 13:15
- status: `revised`
- decision: Render di autou as "Through him," anapheromen as "let us offer," and homologounton as "confessing."

## Hebrews 13:16
- status: `revised`
- decision: Render eupoiias as "doing good" and koinonias as "sharing."

## Hebrews 13:18
- status: `revised`
- decision: Render pepoithamen as "we are persuaded" and anastrephesthai as "conduct ourselves."

## Hebrews 13:19
- status: `revised`
- decision: Render perissoteros as "more earnestly" and tachion as "sooner."

## Hebrews 13:25
- status: `keep`
- decision: Retain the current grace/Amen closing as direct.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Hebrews 12:13,Hebrews 12:20,Hebrews 12:21,Hebrews 12:26,Hebrews 12:27,Hebrews 12:29,Hebrews 13:1,Hebrews 13:11,Hebrews 13:14,Hebrews 13:15,Hebrews 13:16,Hebrews 13:18,Hebrews 13:19,Hebrews 13:25'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
