# NT Review Pass 163

Scope: Colossians focused queue rows after pass 162.

## Colossians 1:15
- status: `revised`
- decision: Render pases ktiseos as "all creation" rather than inherited "every creature."

## Colossians 1:17
- status: `revised`
- decision: Render en auto as "in him" and synesteken as "hold together."

## Colossians 1:19
- status: `revised`
- decision: Remove supplied "Father" and keep the fullness clause explicit.

## Colossians 1:21
- status: `revised`
- decision: Modernize "sometime" to "once" and render the wicked works phrase as the sphere of alienation.

## Colossians 1:28
- status: `revised`
- decision: Render katangellomen as "proclaim," nouthetountes as "admonishing," and teleion as "complete."

## Colossians 2:3
- status: `revised`
- decision: Modernize "hid" to "hidden" while preserving the wisdom and knowledge treasures.

## Colossians 2:9
- status: `revised`
- decision: Render theotetos as "Deity" rather than inherited "Godhead."

## Colossians 2:14
- status: `revised`
- decision: Render the handwriting, ordinances, taking out of the midst, and the cross without the supplied "his."

## Colossians 2:15
- status: `revised`
- decision: Replace archaic "spoiled" with "stripped off" and render en parresia as a public show.

## Colossians 2:17
- status: `keep`
- decision: Retain the current shadow and body wording as already clear and close to the Greek.

## Colossians 2:22
- status: `revised`
- decision: Replace the inherited punctuation and "doctrines" wording with a clearer continuation of the parenthetical command list.

## Colossians 3:2
- status: `revised`
- decision: Render phroneite as "Mind" to match the Greek verb and local Philippians wording.

## Colossians 3:6
- status: `revised`
- decision: Replace "for which things' sake" with "because of these things" while retaining "children of disobedience" for consistency with Ephesians 5:6.

## Colossians 3:21
- status: `revised`
- decision: Remove supplied "to anger" and modernize the imperative.

## Colossians 4:2
- status: `revised`
- decision: Render proskartereite as "continue steadfastly" and "in it" rather than "in the same."

## Colossians 4:4
- status: `keep`
- decision: Retain the current manifest/speak wording as already direct.

## Colossians 4:14
- status: `keep`
- decision: Retain the current greeting wording as already clear.

## Colossians 4:18
- status: `revised`
- decision: Modernize "salutation" to "greeting" and smooth "the hand of me Paul" to "my hand, Paul."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Colossians 1:15,Colossians 1:17,Colossians 1:19,Colossians 1:21,Colossians 1:28,Colossians 2:3,Colossians 2:9,Colossians 2:14,Colossians 2:15,Colossians 2:17,Colossians 2:22,Colossians 3:2,Colossians 3:6,Colossians 3:21,Colossians 4:2,Colossians 4:4,Colossians 4:14,Colossians 4:18'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
