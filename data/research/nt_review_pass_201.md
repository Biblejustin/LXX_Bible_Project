# NT Review Pass 201

Scope: Revelation 21-22 focused queue rows after pass 200.

## Revelation 21:1
- status: `revised`
- decision: Render parelthen as "had passed away" and keep the sea clause as "the sea is no more."

## Revelation 21:2
- status: `revised`
- decision: Keep the holy city bride image direct with "adorned for her husband."

## Revelation 21:12
- status: `revised`
- decision: Render participial opening as "having" and huion Israel as "sons of Israel."

## Revelation 21:13
- status: `revised`
- decision: Render apo with the directional "From" in each gate clause.

## Revelation 21:14
- status: `revised`
- decision: Keep the twelve foundations and apostles wording.

## Revelation 21:16
- status: `revised`
- decision: Render tetragonos as "square" and stadion wording as "stadia."

## Revelation 21:19
- status: `revised`
- decision: Render kekosmemeni as "adorned" and simplify the precious-stone list.

## Revelation 21:20
- status: `revised`
- decision: Use direct stone names, including sardius and chrysoprase.

## Revelation 21:25
- status: `revised`
- decision: Keep ou me as "shall by no means" and render the final clause as "night shall not be there."

## Revelation 22:1
- status: `revised`
- decision: Render lampron as "bright" and keep the water-of-life phrase.

## Revelation 22:4
- status: `revised`
- decision: Render epi as "on" for the name on their foreheads.

## Revelation 22:13
- status: `revised`
- decision: Render to Alpha kai to Omega as "the Alpha and the Omega."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Revelation 21:1,Revelation 21:2,Revelation 21:12,Revelation 21:13,Revelation 21:14,Revelation 21:16,Revelation 21:19,Revelation 21:20,Revelation 21:25,Revelation 22:1,Revelation 22:4,Revelation 22:13'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
