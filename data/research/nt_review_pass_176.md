# NT Review Pass 176

Scope: Hebrews 7-8 focused queue rows after pass 175.

## Hebrews 7:1
- status: `revised`
- decision: Capitalize the title "Most High God" and keep the Melchisedec wording.

## Hebrews 7:7
- status: `revised`
- decision: Render choris pasis antilogias as "without any dispute" and elatton as "lesser."

## Hebrews 7:8
- status: `revised`
- decision: Render apothniskontes anthropoi as "dying men" and avoid the supplied plural object after receives.

## Hebrews 7:9
- status: `revised`
- decision: Render hos epos eipein as "so to speak" and dia Abraam as "through Abraham."

## Hebrews 7:10
- status: `revised`
- decision: Modernize "yet" to "still."

## Hebrews 7:11
- status: `revised`
- decision: Render dia as "through," epi auti as "upon it," and kata as "according to" in both order clauses.

## Hebrews 7:12
- status: `revised`
- decision: Render metatithemenis as "when ... is changed" and ginetai as "takes place."

## Hebrews 7:16
- status: `revised`
- decision: Render gegonen as "has become," sarkikis as "fleshly," and akatalutou as "indestructible."

## Hebrews 7:20
- status: `revised`
- decision: Remove supplied "he was made priest" and render horkomosias as "oath-taking."

## Hebrews 7:24
- status: `revised`
- decision: Render dia to menein auton eis ton aiona as "because he remains forever."

## Hebrews 7:27
- status: `revised`
- decision: Render ephapax as "once for all" and the participle as "having offered up himself."

## Hebrews 8:4
- status: `revised`
- decision: Modernize "should not" to "would not" and render onton as "there being."

## Hebrews 8:6
- status: `revised`
- decision: Render teutuchen as "has obtained" and nenomothetetai as "has been enacted."

## Hebrews 8:7
- status: `revised`
- decision: Remove supplied "covenant" and render deuteras as "a second."

## Hebrews 8:12
- status: `revised`
- decision: Render anomion as "lawless deeds."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Hebrews 7:1,Hebrews 7:7,Hebrews 7:8,Hebrews 7:9,Hebrews 7:10,Hebrews 7:11,Hebrews 7:12,Hebrews 7:16,Hebrews 7:20,Hebrews 7:24,Hebrews 7:27,Hebrews 8:4,Hebrews 8:6,Hebrews 8:7,Hebrews 8:12'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
