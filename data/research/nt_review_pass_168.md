# NT Review Pass 168

Scope: 1 Timothy 5-6 focused queue rows after pass 167, with two adjacent same-chapter corrections.

## 1 Timothy 5:2
- status: `keep`
- decision: Retain the current elder women, younger women, and purity wording as direct.

## 1 Timothy 5:4
- status: `revised`
- decision: Render ekgona as "grandchildren," idion oikon as "their own house," and amoibas apodidonai as "give recompense."

## 1 Timothy 5:5
- status: `revised`
- decision: Render ontos as "truly," memonomeni as "left alone," and the perfect elpiken as "has set her hope."

## 1 Timothy 5:6
- status: `revised`
- decision: Render spatalosa as "lives in self-indulgence" instead of the looser "lives in pleasure."

## 1 Timothy 5:7
- status: `revised`
- decision: Render paraggelle as "command" rather than the looser "give in charge."

## 1 Timothy 5:8
- status: `revised`
- decision: Render oikeion as "household" and apistou as "unbeliever."

## 1 Timothy 5:9
- status: `revised`
- decision: Render katalegestho as "be enrolled" and me elatton as "not less than."

## 1 Timothy 5:11
- status: `revised`
- decision: Render the younger widows command directly and katastreiniasosin as "grow wanton against Christ."

## 1 Timothy 5:13
- status: `revised`
- decision: Render hama as "at the same time," perierchomenai tas oikias as "going about the houses," and fluaroi as "gossips."

## 1 Timothy 5:14
- status: `revised`
- decision: Render oikodespotein as "rule the house" and loidorias charin as "for reproach."

## 1 Timothy 5:15
- status: `keep`
- decision: Retain the current turned aside after Satan wording as direct.

## 1 Timothy 5:19
- status: `revised`
- decision: Render the command as "Do not receive an accusation against an elder" and epi duo e trion martyron as "upon two or three witnesses."

## 1 Timothy 5:24
- status: `revised`
- decision: Render prodeloi as "manifest beforehand" and remove the awkward supplied "some men they."

## 1 Timothy 6:1
- status: `revised`
- decision: Correct despotas from "teachers" to "masters" and render didaskalia as "the teaching."

## 1 Timothy 6:5
- status: `revised`
- decision: Reverse the UKJV seed's sense so the phrase reads "supposing godliness to be gain."

## 1 Timothy 6:6
- status: `keep`
- decision: Retain the current godliness with contentment wording as direct.

## 1 Timothy 6:7
- status: `revised`
- decision: Render delon hoti as "it is clear that."

## 1 Timothy 6:10
- status: `revised`
- decision: Render the phrase as "a root of all the evils," oregomenoi as "reaching after," and odunais as "pains."

## 1 Timothy 6:17
- status: `revised`
- decision: Correct the generated "that they Do not" phrasing and render en to nyn aioni as "in the present age."

## 1 Timothy 6:18
- status: `revised`
- decision: Render eumetadotous as "ready to share" and koinonikous as "generous."

## 1 Timothy 6:19
- status: `revised`
- decision: Render eis to mellon as "for the future."

## 1 Timothy 6:20
- status: `revised`
- decision: Render parakatatheken as "the deposit" and pseudonymou gnoseos as "falsely named knowledge."

## 1 Timothy 6:21
- status: `revised`
- decision: Render estochesan as "missed the mark."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs '1 Timothy 5:2,1 Timothy 5:4,1 Timothy 5:5,1 Timothy 5:6,1 Timothy 5:7,1 Timothy 5:8,1 Timothy 5:9,1 Timothy 5:11,1 Timothy 5:13,1 Timothy 5:14,1 Timothy 5:15,1 Timothy 5:19,1 Timothy 5:24,1 Timothy 6:1,1 Timothy 6:5,1 Timothy 6:6,1 Timothy 6:7,1 Timothy 6:10,1 Timothy 6:17,1 Timothy 6:18,1 Timothy 6:19,1 Timothy 6:20,1 Timothy 6:21'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
