# NT Review Pass 199

Scope: Revelation 18 focused queue rows after pass 198.

## Revelation 18:1
- status: `revised`
- decision: Render exousia as "authority" and ephotisthe as "was illuminated."

## Revelation 18:7
- status: `revised`
- decision: Render estreniasen as "lived luxuriously," penthos as "mourning," and ou me ido as "shall by no means see."

## Revelation 18:10
- status: `revised`
- decision: Render ouai as "Woe" and keep the one-hour judgment clause direct.

## Revelation 18:12
- status: `revised`
- decision: Render gomon as "cargo," chalkos as "bronze," and modernize the vessel list.

## Revelation 18:13
- status: `revised`
- decision: Render thymiamata as "incense," myron as "myrrh," ktene as "cattle," redon as "wagons," and somaton as "bodies."

## Revelation 18:15
- status: `revised`
- decision: Render apo makrothen as "far off" and penthountes as "mourning."

## Revelation 18:16
- status: `revised`
- decision: Render ouai as "Woe" and kechrysomene as "adorned with gold."

## Revelation 18:17
- status: `revised`
- decision: Render eremothe as "was made desolate" and hoi ten thalassan ergazontai as "as many as work the sea."

Validation:
- Fast CSV shape check passed for source, footnotes, decisions, and reviewed phrase guards.
- `python3 scripts/run_fast_review_checkpoint.py --testament nt --refs 'Revelation 18:1,Revelation 18:7,Revelation 18:10,Revelation 18:12,Revelation 18:13,Revelation 18:15,Revelation 18:16,Revelation 18:17'` passed.
- Focused smoke tests passed.
- Full NT aggregate Markdown and Logos DOCX rebuild ran for the reviewed rows.
