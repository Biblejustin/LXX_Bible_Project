# NT Review Pass 169

Scope: 2 Timothy 1-2 focused queue rows after pass 168.

## 2 Timothy 1:3
- status: `keep`
- decision: Retain the current thank God, forefathers, pure conscience, and prayers wording as direct.

## 2 Timothy 1:4
- status: `revised`
- decision: Render epipothon as "longing" and memnimenos as "remembering."

## 2 Timothy 1:5
- status: `revised`
- decision: Render hypomnesin lambanon as "being reminded," keep sincere faith, and make the final clause explicit: "it is also in you."

## 2 Timothy 1:17
- status: `revised`
- decision: Render genomenos en Rome as "when he came to Rome" and remove unnecessary punctuation.

## 2 Timothy 2:2
- status: `revised`
- decision: Render par' emou as "from me" and parathou as "entrust."

## 2 Timothy 2:3
- status: `revised`
- decision: Render kakopatheson as "endure hardship" instead of the archaic "endure hardness."

## 2 Timothy 2:5
- status: `revised`
- decision: Replace "strive for masteries" with "competes" and retain the lawfully-crowned image.

## 2 Timothy 2:12
- status: `revised`
- decision: Render hypomenomen as "endure" instead of "suffer."

## 2 Timothy 2:18
- status: `revised`
- decision: Render estochesan as "missed the mark" and gegonenai as "has already happened."

## 2 Timothy 2:23
- status: `revised`
- decision: Render apaideutous as "uninstructed," paraitou as "refuse," and gennosin machas as "beget strifes."

## 2 Timothy 2:25
- status: `revised`
- decision: Render antidiatithemenous as "those who oppose" and mipote as "if perhaps."

## 2 Timothy 2:26
- status: `revised`
- decision: Render ananepsosin as "come to themselves" and preserve the captive/snare image.

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '2 Timothy 1:3,2 Timothy 1:4,2 Timothy 1:5,2 Timothy 1:17,2 Timothy 2:2,2 Timothy 2:3,2 Timothy 2:5,2 Timothy 2:12,2 Timothy 2:18,2 Timothy 2:23,2 Timothy 2:25,2 Timothy 2:26'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
