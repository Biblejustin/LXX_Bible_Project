# NT Review Pass 194

Scope: Revelation 9 focused queue rows after pass 193.

## Revelation 9:2
- status: `revised`
- decision: Render phrear tes abyssou as "pit of the abyss" and ek tou kapnou as "from the smoke."

## Revelation 9:5
- status: `revised`
- decision: Preserve the divine-passive wording and render paise as "strikes."

## Revelation 9:6
- status: `revised`
- decision: Retain the death-seeking sequence with modern word order.

## Revelation 9:8
- status: `revised`
- decision: Render trichas gynaikon as "women's hair" and leonton as "lions' teeth."

## Revelation 9:9
- status: `revised`
- decision: Remove supplied "as it were" and render polemon as "war."

## Revelation 9:11
- status: `revised`
- decision: Render abyssos as "abyss" and simplify the Hebrew/Greek name clauses.

## Revelation 9:13
- status: `revised`
- decision: Render phonen mian as "one voice" and remove the supplied relative clause.

## Revelation 9:16
- status: `revised`
- decision: Render strateumaton tou hippikou as "armies of the cavalry" and duo myriades myriadon as "two myriads of myriads."

## Revelation 9:18
- status: `revised`
- decision: Render to triton ton anthropon as "the third of men" and ekporeuomenou as "proceeded."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Revelation 9:2,Revelation 9:5,Revelation 9:6,Revelation 9:8,Revelation 9:9,Revelation 9:11,Revelation 9:13,Revelation 9:16,Revelation 9:18'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
