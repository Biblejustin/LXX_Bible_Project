# Fresh Translation Pilot Worksheet

Pilot scope: Genesis 1-3

Method:
- Greek source text first
- Era-aware lexical research
- Phrase-level decision logging
- Variant-impact notes kept separate

Preferred Logos stack:
- base_text_primary | Genesis (Göttingen Septuagint I) | LLS:GSI01GE | Primary Greek base text for the Genesis pilot.
- base_text_fallback | Septuaginta | LXXSESB | Fallback portable Greek base when Göttingen navigation is slower.
- morphology_text | Septuagint with Logos Morphology | LLS:LOGOSLXX | Lemma and morphology support.
- lexicon_primary | Lexham Research Lexicon of the Septuagint | LLS:FBLXXLEX | Primary lexical range and semantic guidance.
- apparatus_primary | Septuaginta: Apparatus Criticus | LLS:LXXCAPP | Primary variant and textual evidence check.
- interlinear_primary | The Lexham Greek-English Interlinear Septuagint: Rahlfs Edition | LLS:LLXXI | Gloss orientation only; not source for final English wording.
- grammar_primary | Grammar of Septuagint Greek: Grammar | LLS:GRAMSPTGRK | Septuagint-specific syntax and idiom support.
- manuscript_check | Codex Sinaiticus: Septuagint and New Testament | LLS:CODEXSINAI | Manual manuscript spot-checks when variants matter.

# Chapter 1

## Genesis 1:1

Greek: Ἐν ἀρχῇ ἐποίησεν ὁ Θεὸς τὸν οὐρανὸν καὶ τὴν γῆν.
Transliteration: En arche epoiesen ho Theos ton ouranon kai ten gen.
Literal gloss: In beginning God made heaven and earth.
Syntax notes: Fronted temporal phrase. Aorist main verb. Paired direct objects form a cosmic merism.
Draft translation: At the beginning, God made heaven and earth.

Decision rows:
- greek_phrase: Ἐν ἀρχῇ | lemma: ἐν | ἀρχή | morphology: preposition + dative noun | chosen_rendering: at the beginning | alternate_renderings: in beginning; at first | rationale: Natural English for a fronted temporal opening phrase. | status: drafted
- greek_phrase: ἐποίησεν | lemma: ποιέω | morphology: aorist active indicative 3 singular | chosen_rendering: made | alternate_renderings: did; fashioned | rationale: Keeps the verb broad and direct without importing later technical wording. | status: drafted
- greek_phrase: τὸν οὐρανὸν καὶ τὴν γῆν | lemma: οὐρανός | γῆ | morphology: accusative singular objects | chosen_rendering: heaven and earth | alternate_renderings: the sky and the earth; sky and land | rationale: In this paired expression the phrase works as a cosmic merism, so heaven and earth carries the full range better. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: heaven and earth | footnote_text: The Greek phrase can function as a totality expression, referring to the whole ordered world rather than only the sky above and the soil below. | source_basis: lexical + idiom | status: drafted

Logos research:
- greek_phrase: τὸν οὐρανὸν καὶ τὴν γῆν | lemma: οὐρανός | γῆ | resource: LLS:FBLXXLEX | usage_note: Check whether the pair functions as a standard cosmic merism in LXX usage. | next_action: verify heaven vs sky

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:2

Greek: ἡ δὲ γῆ ἦν ἀόρατος καὶ ἀκατασκεύαστος, καὶ σκότος ἐπάνω τῆς ἀβύσσου, καὶ πνεῦμα Θεοῦ ἐπεφέρετο ἐπάνω τοῦ ὕδατος.
Transliteration: he de ge en aoratos kai akataskeuastos, kai skotos epano tes abyssou, kai pneuma Theou epephereto epano tou hydatos.
Literal gloss: But the earth was unseen and unformed, and darkness over the abyss, and a wind from God was moving over the water.
Syntax notes: De marks scene shift. Three linked clauses describe the world's condition. Imperfect epephereto presents ongoing motion. Pneuma remains semantically open but is rendered here with a meteorological sense.
Draft translation: Now the earth was unseen and unformed, darkness was over the abyss, and a wind from God was moving over the water.

Decision rows:
- greek_phrase: ἀόρατος καὶ ἀκατασκεύαστος | lemma: ἀόρατος | ἀκατασκεύαστος | morphology: nominative feminine singular adjectives | chosen_rendering: unseen and unformed | alternate_renderings: invisible and unprepared; unformed and unready | rationale: Preserves the double description and keeps the line concrete. | status: drafted
- greek_phrase: σκότος ἐπάνω τῆς ἀβύσσου | lemma: σκότος | ἐπάνω | ἄβυσσος | morphology: noun + preposition + genitive phrase | chosen_rendering: darkness was over the abyss | alternate_renderings: darkness lay over the abyss; darkness was over the deep | rationale: Abyss stays closer to abyssos while the clause remains plain and unforced. | status: drafted
- greek_phrase: πνεῦμα Θεοῦ ἐπεφέρετο | lemma: πνεῦμα | θεός | ἐπιφέρω | morphology: nominative noun + genitive noun + imperfect middle/passive 3 singular | chosen_rendering: a wind from God was moving | alternate_renderings: God's Spirit was moving; God's breath-wind moved | rationale: For a creation-scene first draft, wind keeps the meteorological force alive while leaving Spirit as a real alternate. | status: drafted
- greek_phrase: ἐπάνω τοῦ ὕδατος | lemma: ἐπάνω | ὕδωρ | morphology: preposition + genitive noun | chosen_rendering: over the water | alternate_renderings: above the waters | rationale: Greek uses singular hydatos as a mass noun here. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: a wind from God | footnote_text: Greek pneuma can mean wind, breath, or spirit. This draft keeps a meteorological sense in view, but the phrase remains open for further review. | source_basis: lexical + context | status: drafted

Logos research:
- greek_phrase: πνεῦμα Θεοῦ | lemma: πνεῦμα | θεός | resource: LLS:FBLXXLEX | usage_note: Check whether the immediate context pushes pneuma toward wind, breath, or Spirit. | next_action: verify wind vs Spirit

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Ambiguity around pneuma should stay open until apparatus and lexical review finish | decision: Keep wind wording provisional | status: pending

## Genesis 1:3

Greek: καὶ εἶπεν ὁ Θεός· γενηθήτω φῶς· καὶ ἐγένετο φῶς.
Transliteration: kai eipen ho Theos, genetheto phos, kai egeneto phos.
Literal gloss: And God said, let light come to be, and light came to be.
Syntax notes: The command uses aorist passive imperative as a jussive. The reply clause repeats ginomai for fulfillment.
Draft translation: And God said, 'Let light come to be.' And light came to be.

Decision rows:
- greek_phrase: καὶ εἶπεν ὁ Θεός | lemma: καί | λέγω | θεός | morphology: conjunction + aorist active indicative 3 singular + nominative noun | chosen_rendering: and God said | alternate_renderings: then God said | rationale: Keeps the repeated narrative cadence visible from clause to clause. | status: drafted
- greek_phrase: γενηθήτω φῶς | lemma: γίνομαι | φῶς | morphology: aorist passive imperative 3 singular + nominative noun | chosen_rendering: let light come to be | alternate_renderings: let there be light; let light be | rationale: Keeps the force of ginomai instead of flattening it into bare existence. | status: drafted
- greek_phrase: καὶ ἐγένετο φῶς | lemma: γίνομαι | φῶς | morphology: aorist middle indicative 3 singular + nominative noun | chosen_rendering: and light came to be | alternate_renderings: and there was light | rationale: Echoes the command verbally and keeps the narrative rhythm. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: come to be | footnote_text: The Greek verb is from ginomai, which often signals becoming or coming into being. This draft keeps that verbal echo in both command and fulfillment. | source_basis: verbal repetition + syntax | status: drafted

Logos research:
- greek_phrase: γενηθήτω φῶς | lemma: γίνομαι | φῶς | resource: LLS:LLXXI | usage_note: Check whether the interlinear and lexicon preserve a come-to-be nuance strong enough to keep in English. | next_action: verify come to be wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:4

Greek: καὶ εἶδεν ὁ Θεὸς τὸ φῶς, ὅτι καλόν· καὶ διεχώρισεν ὁ Θεὸς ἀνὰ μέσον τοῦ φωτὸς καὶ ἀνὰ μέσον τοῦ σκότους.
Transliteration: kai eiden ho Theos to phos, hoti kalon; kai diechorisen ho Theos ana meson tou photos kai ana meson tou skotous.
Literal gloss: And God saw the light, that it was good, and God separated between the light and between the darkness.
Syntax notes: The ὅτι clause gives God's evaluation of the light. Repeated ἀνὰ μέσον marks a formal act of division.
Draft translation: And God saw the light, that it was good. And God separated the light from the darkness.

Decision rows:
- greek_phrase: ὅτι καλόν | lemma: ὅτι | καλός | morphology: conjunction + nominative/adjective clause | chosen_rendering: that it was good | alternate_renderings: that it was fitting; that it was beautiful | rationale: Keeps the clause direct and leaves καλός broad enough to carry value beyond mere utility. | status: drafted
- greek_phrase: διεχώρισεν | lemma: διαχωρίζω | morphology: aorist active indicative 3 singular | chosen_rendering: separated | alternate_renderings: divided; marked off | rationale: Plain English fits the decisive act without losing force. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- greek_phrase: καλόν | lemma: καλός | resource: LLS:FBLXXLEX | usage_note: Check whether kalos in creation formulas leans toward good, fitting, beautiful, or some broader evaluative sense. | next_action: verify value nuance

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:5

Greek: καὶ ἐκάλεσεν ὁ Θεὸς τὸ φῶς ἡμέραν καὶ τὸ σκότος ἐκάλεσε νύκτα. καὶ ἐγένετο ἑσπέρα καὶ ἐγένετο πρωΐ, ἡμέρα μία.
Transliteration: kai ekalesen ho Theos to phos hemeran kai to skotos ekalese nykta. kai egeneto hespera kai egeneto proi, hemera mia.
Literal gloss: And God called the light day and the darkness he called night, and evening came and morning came, day one.
Syntax notes: Naming formula gives ordered functions. The closing line keeps the narrative refrain and uses the cardinal μία rather than an ordinal.
Draft translation: And God called the light Day, and the darkness he called Night. And evening came, and morning came: day one.

Decision rows:
- greek_phrase: ἐκάλεσεν ἡμέραν / νύκτα | lemma: καλέω | ἡμέρα | νύξ | morphology: aorist active indicative + accusative predicate objects | chosen_rendering: called Day / called Night | alternate_renderings: named Day / named Night | rationale: Keeps naming language visible and preserves the paired cadence. | status: drafted
- greek_phrase: ἡμέρα μία | lemma: ἡμέρα | εἷς | morphology: noun + cardinal adjective | chosen_rendering: day one | alternate_renderings: first day | rationale: Keeps the cardinal wording visible instead of smoothing immediately to an ordinal. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: day one | footnote_text: Greek uses a cardinal expression here, literally 'day one,' rather than the more expected ordinal 'first day.' The wording may mark the opening day as a distinct starting point. | source_basis: syntax + discourse | status: drafted

Logos research:
- greek_phrase: ἡμέρα μία | lemma: ἡμέρα | εἷς | resource: LLS:GRAMSPTGRK | usage_note: Check whether the cardinal expression here carries any discourse effect beyond simple counting. | next_action: verify day one wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Day-formula wording should stay open until apparatus review is complete | decision: Keep day one provisional | status: pending

## Genesis 1:6

Greek: Καὶ εἶπεν ὁ Θεός· γενηθήτω στερέωμα ἐν μέσῳ τοῦ ὕδατος καὶ ἔστω διαχωρίζον ἀνὰ μέσον ὕδατος καὶ ὕδατος. καὶ ἐγένετο οὕτως.
Transliteration: Kai eipen ho Theos, genetheto stereoma en meso tou hydatos kai esto diachorizon ana meson hydatos kai hydatos. kai egeneto houtos.
Literal gloss: And God said, let a firm span come to be in the middle of the water and let it be dividing between water and water, and it came to be so.
Syntax notes: Two linked jussives shape the command. στερέωμα carries a sense of something set firm, while διαχωρίζον presents ongoing separating function.
Draft translation: And God said, 'Let a firm span come to be in the middle of the water, and let it divide water from water.' And it came to be so.

Decision rows:
- greek_phrase: στερέωμα | lemma: στερέωμα | morphology: accusative singular noun | chosen_rendering: firm span | alternate_renderings: expanse; firmament; vault | rationale: Fresh English keeps the idea of something set firm without importing older church diction whole. | status: drafted
- greek_phrase: ἔστω διαχωρίζον | lemma: εἰμί | διαχωρίζω | morphology: present imperative + present participle | chosen_rendering: let it divide | alternate_renderings: let it be dividing; let it separate | rationale: Readable English keeps the functional force of the participle. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: firm span | footnote_text: Greek stereoma points to something fixed or made firm. 'Firm span' aims to preserve that sense without defaulting either to the older 'firmament' or to a purely empty 'expanse.' | source_basis: lexical + context | status: drafted

Logos research:
- greek_phrase: στερέωμα | lemma: στερέωμα | resource: LLS:FBLXXLEX | usage_note: Check whether stereoma in Septuagint usage suggests firmness, structure, vaulting, or spatial extension most strongly. | next_action: verify firm span wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Key cosmology term should remain open until apparatus and lexical review finish | decision: Keep firm span wording provisional | status: pending

## Genesis 1:7

Greek: καὶ ἐποίησεν ὁ Θεὸς τὸ στερέωμα, καὶ διεχώρισεν ὁ Θεὸς ἀνὰ μέσον τοῦ ὕδατος, ὃ ἦν ὑποκάτω τοῦ στερεώματος, καὶ ἀναμέσον τοῦ ὕδατος τοῦ ἐπάνω τοῦ στερεώματος.
Transliteration: kai epoiesen ho Theos to stereoma, kai diechorisen ho Theos ana meson tou hydatos, ho en hypokato tou stereomatos, kai ana meson tou hydatos tou epano tou stereomatos.
Literal gloss: And God made the firm span, and God separated between the water that was below the firm span and between the water above the firm span.
Syntax notes: The relative clause identifies the lower water first, then balances it with the upper water. The repeated noun keeps the structure explicit.
Draft translation: And God made the firm span, and God separated the water below the firm span from the water above the firm span.

Decision rows:
- greek_phrase: ὑποκάτω / ἐπάνω | lemma: ὑποκάτω | ἐπάνω | morphology: prepositional contrasts | chosen_rendering: below / above | alternate_renderings: under / over | rationale: Short pair preserves the spatial contrast cleanly. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- greek_phrase: ὕδωρ ... ὑποκάτω / ἐπάνω | lemma: ὕδωρ | ὑποκάτω | ἐπάνω | resource: LLS:GRAMSPTGRK | usage_note: Check how the repeated water phrases function rhetorically in Septuagint narrative style. | next_action: verify repeated water phrasing

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:8

Greek: καὶ ἐκάλεσεν ὁ Θεὸς τὸ στερέωμα οὐρανόν. καὶ εἶδεν ὁ Θεός, ὅτι καλόν, καὶ ἐγένετο ἑσπέρα καὶ ἐγένετο πρωΐ, ἡμέρα δευτέρα.
Transliteration: kai ekalesen ho Theos to stereoma ouranon. kai eiden ho Theos, hoti kalon, kai egeneto hespera kai egeneto proi, hemera deutera.
Literal gloss: And God called the firm span heaven, and God saw that it was good, and evening came and morning came, second day.
Syntax notes: The naming clause links στερέωμα with οὐρανός. Here the day formula shifts to an ordinal expression, δευτέρα.
Draft translation: And God called the firm span Heaven. And God saw that it was good. And evening came, and morning came: second day.

Decision rows:
- greek_phrase: οὐρανόν | lemma: οὐρανός | morphology: accusative singular noun | chosen_rendering: Heaven | alternate_renderings: sky | rationale: In this naming line Heaven better matches the world-ordering register already set in verse 1. | status: drafted
- greek_phrase: ἡμέρα δευτέρα | lemma: ἡμέρα | δεύτερος | morphology: noun + ordinal adjective | chosen_rendering: second day | alternate_renderings: day two | rationale: Greek shifts to an ordinal here, so English should show that shift. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- greek_phrase: οὐρανόν | lemma: οὐρανός | resource: LLS:FBLXXLEX | usage_note: Check whether the naming line favors heaven or sky in Greek cosmological usage. | next_action: verify Heaven wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Heaven vs sky naming should stay open until apparatus review is complete | decision: Keep Heaven wording provisional | status: pending

## Genesis 1:9

Greek: Καὶ εἶπεν ὁ Θεός· συναχθήτω τὸ ὕδωρ τὸ ὑποκάτω τοῦ οὐρανοῦ εἰς συναγωγὴν μίαν, καὶ ὀφθήτω ἡ ξηρά. καὶ ἐγένετο οὕτως. καὶ συνήχθη τὸ ὕδωρ τὸ ὑποκάτω τοῦ οὐρανοῦ εἰς τὰς συναγωγὰς αὐτῶν, καὶ ὤφθη ἡ ξηρά.
Transliteration: Kai eipen ho Theos, synachtheto to hydor to hypokato tou ouranou eis synagogen mian, kai ophtheto he xera. kai egeneto houtos. kai synechthe to hydor to hypokato tou ouranou eis tas synagogas auton, kai ophthe he xera.
Literal gloss: And God said, let the water below heaven be gathered into one gathering, and let the dry land appear, and it came to be so, and the water below heaven was gathered into their gatherings, and the dry land appeared.
Syntax notes: The command pairs gathered water with appearing dry land. The fulfillment restates the action with plural συναγωγαί, which may suggest gathered regions or collected bodies.
Draft translation: And God said, 'Let the water below Heaven be gathered into one gathering, and let the dry land appear.' And it came to be so. And the water below Heaven was gathered into collections, and the dry land appeared.

Decision rows:
- greek_phrase: συναγωγὴν μίαν | lemma: συναγωγή | εἷς | morphology: accusative noun phrase | chosen_rendering: one gathering | alternate_renderings: one place; one collection | rationale: Keeps the gathering image alive instead of flattening it into a generic place. | status: drafted
- greek_phrase: ὀφθήτω ἡ ξηρά | lemma: ὁράω | ξηρά | morphology: aorist passive imperative + nominative noun | chosen_rendering: let the dry land appear | alternate_renderings: let dry ground be seen | rationale: Keeps the emergence image visible. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: one gathering | footnote_text: Greek speaks of the waters being brought into 'one gathering,' which keeps the image of collected water in view more strongly than the smoother phrase 'one place.' | source_basis: lexical + imagery | status: drafted

Logos research:
- greek_phrase: συναγωγὴν μίαν / συναγωγὰς | lemma: συναγωγή | resource: LLS:FBLXXLEX | usage_note: Check whether the singular then plural gathering language carries a specific spatial nuance. | next_action: verify gathering wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Gathering language may shift with textual review | decision: Keep one gathering wording provisional | status: pending

## Genesis 1:10

Greek: καὶ ἐκάλεσεν ὁ Θεὸς τὴν ξηρὰν γῆν καὶ τὰ συστήματα τῶν ὑδάτων ἐκάλεσε θαλάσσας. καὶ εἶδεν ὁ Θεός, ὅτι καλόν.
Transliteration: kai ekalesen ho Theos ten xeran gen kai ta systemata ton hydaton ekalese thalassas. kai eiden ho Theos, hoti kalon.
Literal gloss: And God called the dry land earth and the gathered systems of the waters he called seas, and God saw that it was good.
Syntax notes: The paired naming formula continues. συστήματα suggests gathered groupings or formed bodies rather than undifferentiated water.
Draft translation: And God called the dry land Earth, and the gathered waters he called Seas. And God saw that it was good.

Decision rows:
- greek_phrase: τὴν ξηρὰν γῆν | lemma: ξηρός | γῆ | morphology: accusative adjective + noun | chosen_rendering: dry land | alternate_renderings: earth; dry ground | rationale: Dry land fits the named feature in context before Earth appears as the given name. | status: drafted
- greek_phrase: τὰ συστήματα τῶν ὑδάτων | lemma: σύστημα | ὕδωρ | morphology: accusative plural noun phrase | chosen_rendering: the gathered waters | alternate_renderings: the gathered systems of the waters; water-masses; collections of waters | rationale: Readable English compresses the phrase, while the footnote can preserve the fuller lexical picture. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: gathered waters | footnote_text: Greek literally refers to gathered formations or collected bodies of water. This draft shortens the phrase for readability while keeping the sense of ordered water-masses. | source_basis: lexical + imagery | status: drafted

Logos research:
- greek_phrase: συστήματα τῶν ὑδάτων | lemma: σύστημα | ὕδωρ | resource: LLS:FBLXXLEX | usage_note: Check whether systemata here should be rendered as gathered waters, basins, masses, or collections. | next_action: verify gathered waters wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Water-collection wording may shift with lexical and textual review | decision: Keep gathered waters wording provisional | status: pending

## Genesis 1:11

Greek: καὶ εἶπεν ὁ Θεός· βλαστησάτω ἡ γῆ βοτάνην χόρτου σπεῖρον σπέρμα κατὰ γένος καὶ καθ᾿ ὁμοιότητα, καὶ ξύλον κάρπιμον ποιοῦν καρπόν, οὗ τὸ σπέρμα αὐτοῦ ἐν αὐτῷ κατὰ γένος ἐπὶ τῆς γῆς. καὶ ἐγένετο οὕτως.
Transliteration: kai eipen ho Theos, blastesato he ge botanen chortou speiron sperma kata genos kai kath homoioteta, kai xylon karpimon poioun karpon, hou to sperma autou en auto kata genos epi tes ges. kai egeneto houtos.
Literal gloss: And God said, let the earth sprout grass-herb sowing seed according to kind and according to likeness, and fruit-bearing tree making fruit, whose seed of it is in it according to kind upon the earth, and it came to be so.
Syntax notes: The command stacks plant terms densely. κατὰ γένος and καθ᾿ ὁμοιότητα reinforce ordered reproduction and resemblance.
Draft translation: And God said, 'Let the earth sprout seed-bearing grass and herb according to kind and likeness, and fruit-bearing trees making fruit with their seed in them according to kind upon the earth.' And it came to be so.

Decision rows:
- greek_phrase: κατὰ γένος καὶ καθ᾿ ὁμοιότητα | lemma: γένος | ὁμοιότης | morphology: paired prepositional phrases | chosen_rendering: according to kind and likeness | alternate_renderings: according to kind and according to form; by kind and resemblance | rationale: Keeps both terms visible instead of collapsing the second into a duplicate. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: kind and likeness | footnote_text: The Greek command uses both 'kind' and 'likeness.' This draft keeps both terms visible because the pair may mark both reproductive grouping and recognizable form. | source_basis: lexical + discourse | status: drafted

Logos research:
- greek_phrase: κατὰ γένος καὶ καθ᾿ ὁμοιότητα | lemma: γένος | ὁμοιότης | resource: LLS:FBLXXLEX | usage_note: Check whether the double phrase marks distinct ideas in Septuagint creation language or functions as intensification. | next_action: verify kind and likeness wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Plant-order wording may shift with lexical review | decision: Keep kind and likeness wording provisional | status: pending

## Genesis 1:12

Greek: καὶ ἐξήνεγκεν ἡ γῆ βοτάνην χόρτου σπεῖρον σπέρμα κατὰ γένος καὶ καθ᾿ ὁμοιότητα, καὶ ξύλον κάρπιμον ποιοῦν καρπόν, οὗ τὸ σπέρμα αὐτοῦ ἐν αὐτῷ κατὰ γένος ἐπὶ τῆς γῆς. καὶ εἶδεν ὁ Θεός, ὅτι καλόν.
Transliteration: kai exenegken he ge botanen chortou speiron sperma kata genos kai kath homoioteta, kai xylon karpimon poioun karpon, hou to sperma autou en auto kata genos epi tes ges. kai eiden ho Theos, hoti kalon.
Literal gloss: And the earth brought forth grass-herb sowing seed according to kind and according to likeness, and fruit-bearing tree making fruit, whose seed of it is in it according to kind upon the earth, and God saw that it was good.
Syntax notes: The fulfillment closely echoes the command, highlighting ordered correspondence between word and result.
Draft translation: And the earth brought forth seed-bearing grass and herb according to kind and likeness, and fruit-bearing trees making fruit with their seed in them according to kind upon the earth. And God saw that it was good.

Decision rows:
- greek_phrase: ἐξήνεγκεν | lemma: ἐκφέρω | morphology: aorist active indicative 3 singular | chosen_rendering: brought forth | alternate_renderings: brought out; produced | rationale: Fits the earth-as-source imagery without sounding mechanical. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:13

Greek: καὶ ἐγένετο ἑσπέρα καὶ ἐγένετο πρωΐ, ἡμέρα τρίτη.
Transliteration: kai egeneto hespera kai egeneto proi, hemera trite.
Literal gloss: And evening came and morning came, third day.
Syntax notes: Refrain closes the day-unit with the same evening-morning sequence.
Draft translation: And evening came, and morning came: third day.

Decision rows:
- greek_phrase: ἡμέρα τρίτη | lemma: ἡμέρα | τρίτος | morphology: noun + ordinal adjective | chosen_rendering: third day | alternate_renderings: day three | rationale: Keeps the ordinal sequence explicit. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:14

Greek: Καὶ εἶπεν ὁ Θεός· γενηθήτωσαν φωστῆρες ἐν τῷ στερεώματι τοῦ οὐρανοῦ εἰς φαῦσιν ἐπὶ τῆς γῆς, τοῦ διαχωρίζειν ἀνὰ μέσον τῆς ἡμέρας καὶ ἀνὰ μέσον τῆς νυκτός· καὶ ἔστωσαν εἰς σημεῖα καὶ εἰς καιροὺς καὶ εἰς ἡμέρας καὶ εἰς ἐνιαυτούς·
Transliteration: Kai eipen ho Theos, genethethosan phosteres en to stereomati tou ouranou eis phausin epi tes ges, tou diachorizin ana meson tes hemeras kai ana meson tes nyktos; kai estosan eis semeia kai eis kairous kai eis hemeras kai eis eniautous;
Literal gloss: And God said, let light-bearers come to be in the firm span of heaven for shining upon the earth, for dividing between the day and between the night, and let them be for signs and for seasons and for days and for years.
Syntax notes: The infinitive τοῦ διαχωρίζειν states function. φωστῆρες are bearers or sources of light rather than light itself.
Draft translation: And God said, 'Let light-bearers come to be in the firm span of Heaven for shining on the earth, to divide day from night. And let them be for signs and for seasons and for days and for years.'

Decision rows:
- greek_phrase: φωστῆρες | lemma: φωστήρ | morphology: nominative plural noun | chosen_rendering: light-bearers | alternate_renderings: lights; luminaries | rationale: Fresh English preserves the sense of bodies that bear or give light. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: light-bearers | footnote_text: Greek does not simply say 'lights' here but uses a term for bodies that bear or give light. The wording points to heavenly lamps rather than to light as an abstract thing. | source_basis: lexical | status: drafted

Logos research:
- greek_phrase: φωστῆρες | lemma: φωστήρ | resource: LLS:FBLXXLEX | usage_note: Check whether phosteres in Septuagint Greek is best represented as lights, luminaries, or light-bearers. | next_action: verify light-bearers wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Cosmology-term wording may shift after lexical review | decision: Keep light-bearers wording provisional | status: pending

## Genesis 1:15

Greek: καὶ ἔστωσαν εἰς φαῦσιν ἐν τῷ στερεώματι τοῦ οὐρανοῦ, ὥστε φαίνειν ἐπὶ τῆς γῆς. καὶ ἐγένετο οὕτως.
Transliteration: kai estosan eis phausin en to stereomati tou ouranou, hoste phainein epi tes ges. kai egeneto houtos.
Literal gloss: And let them be for shining in the firm span of heaven, so as to shine upon the earth, and it came to be so.
Syntax notes: The ὥστε clause restates purpose with result-oriented force.
Draft translation: And let them be for shining in the firm span of Heaven so as to shine on the earth. And it came to be so.

Decision rows:
- greek_phrase: ὥστε φαίνειν | lemma: ὥστε | φαίνω | morphology: conjunction + present infinitive | chosen_rendering: so as to shine | alternate_renderings: to give light; to shine | rationale: Keeps the purpose-result nuance of the clause. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:16

Greek: καὶ ἐποίησεν ὁ Θεὸς τοὺς δύο φωστῆρας τοὺς μεγάλους, τὸν φωστῆρα τὸν μέγαν εἰς ἀρχὰς τῆς ἡμέρας καὶ τὸν φωστῆρα τὸν ἐλάσσω εἰς ἀρχὰς τῆς νυκτός, καὶ τοὺς ἀστέρας.
Transliteration: kai epoiesen ho Theos tous dyo phosteras tous megalous, ton phostera ton megan eis archas tes hemeras kai ton phostera ton elasso eis archas tes nyktos, kai tous asteras.
Literal gloss: And God made the two great light-bearers, the great light-bearer for the dominions of the day and the lesser light-bearer for the dominions of the night, and the stars.
Syntax notes: The repeated nouning is formal and emphatic. εἰς ἀρχὰς likely points to ruling functions or governing domains.
Draft translation: And God made the two great light-bearers, the greater light-bearer for the dominion of the day and the lesser light-bearer for the dominion of the night, and the stars.

Decision rows:
- greek_phrase: εἰς ἀρχὰς τῆς ἡμέρας / τῆς νυκτός | lemma: ἀρχή | morphology: prepositional domain phrases | chosen_rendering: for the dominion of the day / night | alternate_renderings: for rule over the day / night; for the beginnings of the day / night | rationale: Dominion keeps the governing sense alive while marking that the Greek uses a noun rather than a verb. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: dominion | footnote_text: Greek uses a noun built from the rule-family rather than a plain verb. 'Dominion' keeps that governing sense visible in the line. | source_basis: lexical + syntax | status: drafted

Logos research:
- greek_phrase: εἰς ἀρχὰς | lemma: ἀρχή | resource: LLS:FBLXXLEX | usage_note: Check whether this noun phrase leans toward rule, dominion, office, or beginning in this context. | next_action: verify dominion wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Governance wording may shift after lexical review of ἀρχὰς | decision: Keep dominion wording provisional | status: pending

## Genesis 1:17

Greek: καὶ ἔθετο αὐτοὺς ὁ Θεὸς ἐν τῷ στερεώματι τοῦ οὐρανοῦ, ὥστε φαίνειν ἐπὶ τῆς γῆς
Transliteration: kai etheto autous ho Theos en to stereomati tou ouranou, hoste phainein epi tes ges
Literal gloss: And God placed them in the firm span of heaven, so as to shine upon the earth.
Syntax notes: Placement matches the previously stated purpose.
Draft translation: And God placed them in the firm span of Heaven so as to shine on the earth.

Decision rows:
- greek_phrase: ἔθετο | lemma: τίθημι | morphology: aorist active indicative 3 singular | chosen_rendering: placed | alternate_renderings: set; positioned | rationale: Simple English fits the ordered-placement scene. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:18

Greek: καὶ ἄρχειν τῆς ἡμέρας καὶ τῆς νυκτὸς καὶ διαχωρίζειν ἀνὰ μέσον τοῦ φωτὸς καὶ ἀνὰ μέσον τοῦ σκότους. καὶ εἶδεν ὁ Θεός, ὅτι καλόν.
Transliteration: kai archein tes hemeras kai tes nyktos kai diachorizin ana meson tou photos kai ana meson tou skotous. kai eiden ho Theos, hoti kalon.
Literal gloss: And to rule the day and the night and to divide between the light and between the darkness, and God saw that it was good.
Syntax notes: Infinitives continue the functional purpose of the heavenly lights.
Draft translation: And they were to rule day and night and to divide light from darkness. And God saw that it was good.

Decision rows:
- greek_phrase: ἄρχειν | lemma: ἄρχω | morphology: present infinitive | chosen_rendering: rule | alternate_renderings: govern | rationale: Short verb matches the functional role of the lights. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:19

Greek: καὶ ἐγένετο ἑσπέρα καὶ ἐγένετο πρωΐ, ἡμέρα τετάρτη.
Transliteration: kai egeneto hespera kai egeneto proi, hemera tetarte.
Literal gloss: And evening came and morning came, fourth day.
Syntax notes: Day refrain continues without variation here beyond the ordinal.
Draft translation: And evening came, and morning came: fourth day.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:20

Greek: Καὶ εἶπεν ὁ Θεός· ἐξαγαγέτω τὰ ὕδατα ἑρπετὰ ψυχῶν ζωσῶν καὶ πετεινὰ πετόμενα ἐπὶ τῆς γῆς κατὰ τὸ στερέωμα τοῦ οὐρανοῦ. καὶ ἐγένετο οὕτως.
Transliteration: Kai eipen ho Theos, exagageto ta hydata herpeta psychon zōsōn kai peteina petomena epi tes ges kata to stereoma tou ouranou. kai egeneto houtos.
Literal gloss: And God said, let the waters bring forth crawling things of living souls and winged creatures flying over the earth across the firm span of heaven, and it came to be so.
Syntax notes: ἑρπετά can denote crawling or swarming creatures broadly. The line links waters and sky in a paired filling of created spaces.
Draft translation: And God said, 'Let the waters bring forth swarming living creatures and winged birds flying over the earth across the firm span of Heaven.' And it came to be so.

Decision rows:
- greek_phrase: ἑρπετὰ ψυχῶν ζωσῶν | lemma: ἑρπετόν | ψυχή | ζῶσα | morphology: accusative plural phrase | chosen_rendering: swarming living creatures | alternate_renderings: creeping living things; crawling creatures with life | rationale: Swarming catches broader life-in-motion better than a narrow reptile sense. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: swarming living creatures | footnote_text: The Greek phrase can cover more than reptiles in a narrow sense. This draft uses 'swarming' to keep the image broad and active. | source_basis: lexical + imagery | status: drafted

Logos research:
- greek_phrase: ἑρπετὰ ψυχῶν ζωσῶν | lemma: ἑρπετόν | ψυχή | ζωή | resource: LLS:FBLXXLEX | usage_note: Check whether herpeta here is broad swarming life or should be narrowed more specifically. | next_action: verify swarming wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Creature-category wording may shift with lexical review | decision: Keep swarming wording provisional | status: pending

## Genesis 1:21

Greek: καὶ ἐποίησεν ὁ Θεὸς τὰ κήτη τὰ μεγάλα καὶ πᾶσαν ψυχὴν ζῴων ἑρπετῶν, ἃ ἐξήγαγε τὰ ὕδατα κατὰ γένη αὐτῶν, καὶ πᾶν πετεινὸν πτερωτὸν κατὰ γένος. καὶ εἶδεν ὁ Θεός, ὅτι καλά.
Transliteration: kai epoiesen ho Theos ta kete ta megala kai pasan psychen zoon herpeton, ha exegage ta hydata kata gene auton, kai pan peteinon pteroton kata genos. kai eiden ho Theos, hoti kala.
Literal gloss: And God made the great sea-creatures and every living soul of creeping animals, which the waters brought forth according to their kinds, and every winged bird according to kind, and God saw that they were good.
Syntax notes: The verse expands the command with named groups. καλά is plural here, agreeing with the created things.
Draft translation: And God made the great sea-creatures and every living creature among the swarming things that the waters brought forth according to their kinds, and every winged bird according to kind. And God saw that they were good.

Decision rows:
- greek_phrase: κήτη τὰ μεγάλα | lemma: κῆτος | μέγας | morphology: accusative plural phrase | chosen_rendering: great sea-creatures | alternate_renderings: great sea monsters; great marine creatures | rationale: Sea-creatures stays broad without muting the scale. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- greek_phrase: κήτη τὰ μεγάλα | lemma: κῆτος | resource: LLS:FBLXXLEX | usage_note: Check range of ketos in LXX: sea-creature, monster, whale, or something broader. | next_action: verify sea-creatures wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Sea-creature wording may shift with lexical review | decision: Keep sea-creatures wording provisional | status: pending

## Genesis 1:22

Greek: καὶ εὐλόγησεν αὐτὰ ὁ Θεός, λέγων· αὐξάνεσθε καὶ πληθύνεσθε καὶ πληρώσατε τὰ ὕδατα ἐν ταῖς θαλάσσαις, καὶ τὰ πετεινὰ πληθυνέσθωσαν ἐπὶ τῆς γῆς.
Transliteration: kai eulogesen auta ho Theos, legōn; auxanesthe kai plethynesthe kai plerosate ta hydata en tais thalassais, kai ta peteina plethynesthosan epi tes ges.
Literal gloss: And God blessed them, saying, increase and multiply and fill the waters in the seas, and let the birds be multiplied upon the earth.
Syntax notes: Blessing speech introduces fecundity language that will recur later with humanity.
Draft translation: And God blessed them, saying, 'Increase and multiply and fill the waters in the seas, and let the birds multiply on the earth.'

Decision rows:
- greek_phrase: αὐξάνεσθε καὶ πληθύνεσθε | lemma: αὐξάνω | πληθύνω | morphology: present imperatives | chosen_rendering: increase and multiply | alternate_renderings: grow and multiply | rationale: Keeps the blessing formula recognizable. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:23

Greek: καὶ ἐγένετο ἑσπέρα καὶ ἐγένετο πρωΐ, ἡμέρα πέμπτη.
Transliteration: kai egeneto hespera kai egeneto proi, hemera pempte.
Literal gloss: And evening came and morning came, fifth day.
Syntax notes: Refrain closes the fifth day.
Draft translation: And evening came, and morning came: fifth day.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: No wording change yet | decision: Check LLS:LXXCAPP before locking final English | status: pending

## Genesis 1:24

Greek: Καὶ εἶπεν ὁ Θεός· ἐξαγαγέτω ἡ γῆ ψυχὴν ζῶσαν κατὰ γένος, τετράποδα καὶ ἑρπετὰ καὶ θηρία τῆς γῆς κατὰ γένος. καὶ ἐγένετο οὕτως.
Transliteration: Kai eipen ho Theos, exagageto he ge psychen zosan kata genos, tetrapoda kai herpeta kai theria tes ges kata genos. kai egeneto houtos.
Literal gloss: And God said, let the earth bring forth living soul according to kind, four-footed animals and creeping things and wild beasts of the earth according to kind, and it came to be so.
Syntax notes: The command moves to land animals in three grouped classes.
Draft translation: And God said, 'Let the earth bring forth living creatures according to kind: four-footed animals and creeping things and wild beasts of the earth according to kind.' And it came to be so.

Decision rows:
- greek_phrase: ψυχὴν ζῶσαν | lemma: ψυχή | ζῶσα | morphology: accusative singular collective phrase | chosen_rendering: living creatures | alternate_renderings: living being; living soul | rationale: Plural English reads naturally while preserving animate life. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- greek_phrase: ψυχὴν ζῶσαν | lemma: ψυχή | ζάω | resource: LLS:FBLXXLEX | usage_note: Check how often this phrase is treated as collective 'living creature' in Greek biblical usage. | next_action: verify living creatures wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Land-creature wording may shift with lexical review | decision: Keep living creatures wording provisional | status: pending

## Genesis 1:25

Greek: καὶ ἐποίησεν ὁ Θεὸς τὰ θηρία τῆς γῆς κατὰ γένος, καὶ τὰ κτήνη κατὰ γένος αὐτῶν καὶ πάντα τὰ ἑρπετὰ τῆς γῆς κατὰ γένος αὐτῶν. καὶ εἶδεν ὁ Θεός, ὅτι καλά.
Transliteration: kai epoiesen ho Theos ta theria tes ges kata genos, kai ta ktene kata genos auton kai panta ta herpeta tes ges kata genos auton. kai eiden ho Theos, hoti kala.
Literal gloss: And God made the wild beasts of the earth according to kind, and the cattle according to their kind, and all the creeping things of the earth according to their kind, and God saw that they were good.
Syntax notes: Fulfillment restates the land-animal triad with explicit categories.
Draft translation: And God made the wild beasts of the earth according to kind, and the livestock according to their kind, and every creeping thing of the earth according to its kind. And God saw that they were good.

Decision rows:
- greek_phrase: κτήνη | lemma: κτῆνος | morphology: accusative plural noun | chosen_rendering: livestock | alternate_renderings: cattle; domestic animals | rationale: Livestock fits modern English while keeping domesticated-animal sense. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Livestock wording may shift with lexical review | decision: Keep livestock wording provisional | status: pending

## Genesis 1:26

Greek: καὶ εἶπεν ὁ Θεός· ποιήσωμεν ἄνθρωπον κατ᾿ εἰκόνα ἡμετέραν καὶ καθ᾿ ὁμοίωσιν, καὶ ἀρχέτωσαν τῶν ἰχθύων τῆς θαλάσσης καὶ τῶν πετεινῶν τοῦ οὐρανοῦ καὶ τῶν κτηνῶν καὶ πάσης τῆς γῆς καὶ πάντων τῶν ἑρπετῶν τῶν ἑρπόντων ἐπὶ τῆς γῆς.
Transliteration: kai eipen ho Theos, poiēsōmen anthropon kat eikona hemeteran kai kath homoiōsin, kai archetōsan tōn ichthyōn tes thalasses kai tōn peteinōn tou ouranou kai tōn ktēnōn kai pases tes ges kai pantōn tōn herpetōn tōn herpontōn epi tes ges.
Literal gloss: And God said, let us make human according to our image and according to likeness, and let them rule the fish of the sea and the birds of heaven and the livestock and all the earth and all the creeping things creeping upon the earth.
Syntax notes: The verse shifts from singular ἄνθρωπον to plural rule language. εἰκών and ὁμοίωσις form a paired description rather than obvious synonyms.
Draft translation: And God said, 'Let us make humankind according to our image and according to likeness, and let them rule the fish of the sea and the birds of Heaven and the livestock and all the earth and every creeping thing that creeps on the earth.'

Decision rows:
- greek_phrase: ἄνθρωπον | lemma: ἄνθρωπος | morphology: accusative singular noun | chosen_rendering: humankind | alternate_renderings: human; the human | rationale: Collective English handles the verse's singular-to-plural shift best for now. | status: drafted
- greek_phrase: κατ᾿ εἰκόνα ἡμετέραν καὶ καθ᾿ ὁμοίωσιν | lemma: εἰκών | ὁμοίωσις | morphology: paired prepositional phrases | chosen_rendering: according to our image and according to likeness | alternate_renderings: in our image and likeness | rationale: Keeps both nouns audible instead of collapsing them too quickly. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: image and likeness | footnote_text: The Greek keeps both 'image' and 'likeness' rather than using only one term. This draft preserves the pair and leaves their exact relation open for later study. | source_basis: lexical + discourse | status: drafted

Logos research:
- greek_phrase: ἄνθρωπον / εἰκών / ὁμοίωσις | lemma: ἄνθρωπος | εἰκών | ὁμοίωσις | resource: LLS:FBLXXLEX | usage_note: Check singular-to-plural movement and relation between image and likeness in Genesis 1 Greek. | next_action: verify humankind image wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Anthropos and image-likeness wording remain open | decision: Keep humankind wording provisional | status: pending

## Genesis 1:27

Greek: καὶ ἐποίησεν ὁ Θεὸς τὸν ἄνθρωπον, κατ᾿ εἰκόνα Θεοῦ ἐποίησεν αὐτόν, ἄρσεν καὶ θῆλυ ἐποίησεν αὐτούς.
Transliteration: kai epoiesen ho Theos ton anthropon, kat eikona Theou epoiesen auton, arsen kai thely epoiesen autous.
Literal gloss: And God made the human, according to image of God he made him, male and female he made them.
Syntax notes: Singular and plural forms alternate within the verse. The line is tightly patterned and poetic.
Draft translation: And God made humankind; according to God's image he made it. Male and female he made them.

Decision rows:
- greek_phrase: ἄρσεν καὶ θῆλυ | lemma: ἄρσην | θῆλυ | morphology: paired predicates | chosen_rendering: male and female | alternate_renderings: man and woman | rationale: Closer to the paired sex terms used in the Greek line. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Singular-plural rendering may shift after close review | decision: Keep humankind wording provisional | status: pending

## Genesis 1:28

Greek: καὶ εὐλόγησεν αὐτοὺς ὁ Θεός, λέγων· αὐξάνεσθε καὶ πληθύνεσθε καὶ πληρώσατε τὴν γῆν καὶ κατακυριεύσατε αὐτῆς καὶ ἄρχετε τῶν ἰχθύων τῆς θαλάσσης καὶ τῶν πετεινῶν τοῦ οὐρανοῦ καὶ πάντων τῶν κτηνῶν καὶ πάσης τῆς γῆς καὶ πάντων τῶν ἑρπετῶν τῶν ἑρπόντων ἐπὶ τῆς γῆς.
Transliteration: kai eulogesen autous ho Theos, legōn; auxanesthe kai plethynesthe kai plerosate ten gen kai katakyrieusate autes kai archete tōn ichthyōn tes thalasses kai tōn peteinōn tou ouranou kai pantōn tōn ktēnōn kai pases tes ges kai pantōn tōn herpetōn tōn herpontōn epi tes ges.
Literal gloss: And God blessed them, saying, increase and multiply and fill the earth and subdue it and rule the fish of the sea and the birds of heaven and all the livestock and all the earth and all the creeping things creeping upon the earth.
Syntax notes: Blessing joins fecundity with dominion verbs. κατακυριεύσατε is stronger than simple rule.
Draft translation: And God blessed them, saying, 'Increase and multiply and fill the earth and subdue it, and rule the fish of the sea and the birds of Heaven and all the livestock and all the earth and every creeping thing that creeps on the earth.'

Decision rows:
- greek_phrase: κατακυριεύσατε | lemma: κατακυριεύω | morphology: aorist active imperative 2 plural | chosen_rendering: subdue | alternate_renderings: bring under rule; master | rationale: Subdue preserves the stronger force of the compound verb. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: subdue | footnote_text: The Greek verb is stronger than a gentle 'manage.' This wording keeps the force of bringing the earth under ordered human rule. | source_basis: lexical | status: drafted

Logos research:
- greek_phrase: κατακυριεύσατε | lemma: κατακυριεύω | resource: LLS:FBLXXLEX | usage_note: Check whether the verb carries dominion, subjection, or stronger conquest nuance in comparable Greek usage. | next_action: verify subdue wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Dominion verb wording may shift after lexical review | decision: Keep subdue wording provisional | status: pending

## Genesis 1:29

Greek: καὶ εἶπεν ὁ Θεός· ἰδοὺ δέδωκα ὑμῖν πάντα χόρτον σπόριμον σπεῖρον σπέρμα, ὅ ἐστιν ἐπάνω πάσης τῆς γῆς, καὶ πᾶν ξύλον, ὃ ἔχει ἐν ἑαυτῷ καρπὸν σπέρματος σπορίμου, ὑμῖν ἔσται εἰς βρῶσιν·
Transliteration: kai eipen ho Theos, idou dedōka hymin panta chorton sporimon speiron sperma, ho estin epanō pases tes ges, kai pan xylon, ho echei en heautō karpon spermatos sporimou, hymin estai eis brōsin;
Literal gloss: And God said, behold, I have given you every seed-bearing plant sowing seed, which is upon all the earth, and every tree that has in itself fruit of sowable seed, to you it shall be for food.
Syntax notes: δέδωκα presents the gift as granted. The line defines food sources by reproductive capacity.
Draft translation: And God said, 'Look, I have given you every seed-bearing plant that sows seed on all the earth, and every tree that has in itself fruit with seed for sowing. It will be food for you.'

Decision rows:
- greek_phrase: χόρτον σπόριμον σπεῖρον σπέρμα | lemma: χόρτος | σπόριμος | σπείρω | σπέρμα | morphology: stacked accusative phrase | chosen_rendering: seed-bearing plant that sows seed | alternate_renderings: every seed-bearing herb; every seeding plant | rationale: Keeps the reproductive wording foregrounded. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Food-gift wording may shift with lexical review | decision: Keep seed-bearing plant wording provisional | status: pending

## Genesis 1:30

Greek: καὶ πᾶσι τοῖς θηρίοις τῆς γῆς καὶ πᾶσι τοῖς πετεινοῖς τοῦ οὐρανοῦ καὶ παντὶ ἑρπετῷ ἕρποντι ἐπὶ τῆς γῆς, ὃ ἔχει ἐν ἑαυτῷ ψυχὴν ζωῆς, καὶ πάντα χόρτον χλωρὸν εἰς βρῶσιν. καὶ ἐγένετο οὕτως.
Transliteration: kai pasi tois theriois tes ges kai pasi tois peteinois tou ouranou kai panti herpetō herponti epi tes ges, ho echei en heautō psychen zōes, kai panta chorton chlōron eis brōsin. kai egeneto houtos.
Literal gloss: And to all the wild beasts of the earth and to all the birds of heaven and to every creeping thing creeping upon the earth, which has in itself soul of life, and every green plant for food, and it came to be so.
Syntax notes: The gift extends to animal life marked by ψυχὴ ζωῆς. The closing formula seals the command's fulfillment.
Draft translation: And to every wild beast of the earth and every bird of Heaven and every creeping thing that creeps on the earth, everything that has in itself living breath, I have given every green plant for food. And it came to be so.

Decision rows:
- greek_phrase: ψυχὴν ζωῆς | lemma: ψυχή | ζωή | morphology: accusative noun phrase | chosen_rendering: living breath | alternate_renderings: living soul; life-breath | rationale: Living breath keeps animate vitality visible without overly theological loading. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: living breath | footnote_text: Greek literally speaks of what has within itself the breath or life-principle of living existence. This draft keeps that animating sense in view. | source_basis: lexical + context | status: drafted

Logos research:
- greek_phrase: ψυχὴν ζωῆς | lemma: ψυχή | ζωή | resource: LLS:FBLXXLEX | usage_note: Check whether the phrase should be rendered life-breath, living soul, or animate life in this context. | next_action: verify living breath wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Animate-life wording may shift with lexical review | decision: Keep living breath wording provisional | status: pending

## Genesis 1:31

Greek: καὶ εἶδεν ὁ Θεὸς τὰ πάντα, ὅσα ἐποίησε, καὶ ἰδοὺ καλά λίαν. καὶ ἐγένετο ἑσπέρα καὶ ἐγένετο πρωΐ, ἡμέρα ἕκτη.
Transliteration: kai eiden ho Theos ta panta, hosa epoiese, kai idou kala lian. kai egeneto hespera kai egeneto proi, hemera hekte.
Literal gloss: And God saw all things, as many as he made, and behold, very good, and evening came and morning came, sixth day.
Syntax notes: The scope expands to all created things. λίαν intensifies the evaluation.
Draft translation: And God saw all that he had made, and look, it was very good. And evening came, and morning came: sixth day.

Decision rows:
- greek_phrase: καλά λίαν | lemma: καλός | λίαν | morphology: predicate adjective + adverb | chosen_rendering: very good | alternate_renderings: exceedingly good; very fitting | rationale: Simple English captures the climactic intensification. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: very good | footnote_text: Greek adds an intensifier, not merely 'good.' The line presents the completed whole as fully and emphatically good. | source_basis: syntax + discourse | status: drafted

Logos research:
- greek_phrase: καλά λίαν | lemma: καλός | λίαν | resource: LLS:GRAMSPTGRK | usage_note: Check whether lian here functions as simple intensifier or carries rhetorical climax in the creation sequence. | next_action: verify very good wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Climactic evaluation wording may shift with lexical review | decision: Keep very good wording provisional | status: pending

# Chapter 2

## Genesis 2:1

Greek: ΚΑΙ συνετελέσθησαν ὁ οὐρανὸς καὶ ἡ γῆ καὶ πᾶς ὁ κόσμος αὐτῶν.
Transliteration: kai synetelesthesan ho ouranos kai he ge kai pas ho kosmos auton.
Literal gloss: And heaven and earth and all their world-order were completed.
Syntax notes: Passive completion closes the creation sequence. κόσμος here denotes ordered arrangement or array.
Draft translation: And Heaven and Earth were completed, and all their ordered array.

Decision rows:
- greek_phrase: κόσμος | lemma: κόσμος | morphology: nominative singular noun | chosen_rendering: ordered array | alternate_renderings: world; ornament; order | rationale: Ordered array keeps the sense of an arranged totality without importing modern planet-language too quickly. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: ordered array | footnote_text: Greek kosmos can mean an ordered arrangement or adornment, not only 'world' in a modern sense. This draft keeps the idea of a completed, ordered whole. | source_basis: lexical + context | status: drafted

Logos research:
- greek_phrase: κόσμος | lemma: κόσμος | resource: LLS:FBLXXLEX | usage_note: Check whether kosmos here is best rendered world, adornment, order, or arranged whole in creation context. | next_action: verify ordered array wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Kosmos wording may shift with lexical review | decision: Keep ordered array wording provisional | status: pending

## Genesis 2:2

Greek: καὶ συνετέλεσεν ὁ Θεὸς ἐν τῇ ἡμέρᾳ τῇ ἕκτῃ τὰ ἔργα αὐτοῦ, ἃ ἐποίησε, καὶ κατέπαυσε τῇ ἡμέρᾳ τῇ ἑβδόμῃ ἀπὸ πάντων τῶν ἔργων αὐτοῦ, ὧν ἐποίησε.
Transliteration: kai synetelesen ho Theos en te hemera te hektē ta erga autou, ha epoiese, kai katepause te hemera te hebdomē apo pantōn tōn ergōn autou, hōn epoiese.
Literal gloss: And God completed on the sixth day his works, which he made, and he rested on the seventh day from all his works, which he made.
Syntax notes: The Greek here reads sixth day, not seventh day, for completion. κατέπαυσε gives cessation or rest from labor.
Draft translation: And God completed his works, the works he had made, on the sixth day, and he rested on the seventh day from all his works that he had made.

Decision rows:
- greek_phrase: ἐν τῇ ἡμέρᾳ τῇ ἕκτῃ | lemma: ἕκτος | morphology: prepositional time phrase | chosen_rendering: on the sixth day | alternate_renderings: on day six; in the sixth day | rationale: Keeps the Greek reading visible at a key textual point. | status: drafted
- greek_phrase: κατέπαυσε | lemma: καταπαύω | morphology: aorist active indicative 3 singular | chosen_rendering: rested | alternate_renderings: ceased; stopped | rationale: Rested is natural English, while the footnote can preserve cessation nuance if needed. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: sixth day | footnote_text: The Greek here says God completed his works on the sixth day and rested on the seventh. This differs from forms of the text that read 'seventh day' in the first clause. | source_basis: textual + lexical | status: drafted

Logos research:
- greek_phrase: ἕκτῃ / ἑβδόμῃ | lemma: ἕκτος | ἕβδομος | resource: LLS:LXXCAPP | usage_note: Check apparatus and notes on the sixth-day completion reading versus seventh-day forms. | next_action: verify sixth day reading

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: Greek line currently reads sixth day for completion | translation_impact: This verse likely needs direct apparatus review because the day-number reading affects translation and comparison with other text forms | decision: Keep sixth day wording provisional until apparatus checked | status: pending

## Genesis 2:3

Greek: καὶ εὐλόγησεν ὁ Θεὸς τὴν ἡμέραν τὴν ἑβδόμην καὶ ἡγίασεν αὐτήν· ὅτι ἐν αὐτῇ κατέπαυσεν ἀπὸ πάντων τῶν ἔργων αὐτοῦ, ὧν ἤρξατο ὁ Θεὸς ποιῆσαι.
Transliteration: kai eulogesen ho Theos ten hemeran ten hebdomēn kai hegiasen autēn; hoti en aute katepausen apo pantōn tōn ergōn autou, hōn ērxato ho Theos poiēsai.
Literal gloss: And God blessed the seventh day and made it holy, because in it he rested from all his works, which God began to make.
Syntax notes: The final clause is unusual and may point back to the whole creative undertaking as a begun work now brought to rest.
Draft translation: And God blessed the seventh day and made it holy, because on it he rested from all his works, the works God had begun to make.

Decision rows:
- greek_phrase: ἡγίασεν | lemma: ἁγιάζω | morphology: aorist active indicative 3 singular | chosen_rendering: made it holy | alternate_renderings: sanctified it; hallowed it | rationale: Plain English keeps the consecration idea readable. | status: drafted
- greek_phrase: ὧν ἤρξατο ὁ Θεὸς ποιῆσαι | lemma: ἄρχω | ποιέω | morphology: relative clause with complementary infinitive | chosen_rendering: the works God had begun to make | alternate_renderings: which God began to make | rationale: Keeps the odd final wording audible rather than smoothing it away. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: begun to make | footnote_text: The Greek closes with an unusual phrase, literally speaking of the works God 'began to make.' This draft keeps that odd ending visible rather than smoothing it away. | source_basis: syntax + discourse | status: drafted

Logos research:
- greek_phrase: ὧν ἤρξατο ὁ Θεὸς ποιῆσαι | lemma: ἄρχω | ποιέω | resource: LLS:GRAMSPTGRK | usage_note: Check how this closing phrase is treated in Septuagint Greek syntax and whether it implies begun-work now finished. | next_action: verify begun to make wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Final clause wording may shift after grammar review | decision: Keep begun to make wording provisional | status: pending

## Genesis 2:4

Greek: Αὕτη ἡ βίβλος γενέσεως οὐρανοῦ καὶ γῆς, ὅτε ἐγένετο· ᾗ ἡμέρᾳ ἐποίησε Κύριος ὁ Θεὸς τὸν οὐρανὸν καὶ τὴν γῆν
Transliteration: Haute he biblos geneseōs ouranou kai gēs, hote egeneto; hē hēmera epoiese Kyrios ho Theos ton ouranon kai tēn gēn
Literal gloss: This the book of genesis of heaven and earth, when it came to be; in the day Lord God made heaven and earth.
Syntax notes: The heading formula marks a new section. βίβλος γενέσεως may signal account, record, or origin-narrative.
Draft translation: This is the book of the genesis of Heaven and Earth, when they came to be, on the day the Lord God made Heaven and Earth.

Decision rows:
- greek_phrase: βίβλος γενέσεως | lemma: βίβλος | γένεσις | morphology: nominative heading phrase | chosen_rendering: the book of the genesis | alternate_renderings: the record of origins; the account of becoming | rationale: Keeps the heading's explicit genesis-language visible. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: book of the genesis | footnote_text: Greek literally says 'book of genesis' or 'book of becoming.' This draft keeps the heading's own wordplay visible rather than replacing it with a generic title. | source_basis: lexical + discourse | status: drafted

Logos research:
- greek_phrase: βίβλος γενέσεως | lemma: βίβλος | γένεσις | resource: LLS:FBLXXLEX | usage_note: Check how this heading formula functions in Greek Genesis and whether genesis here leans toward origins, generations, or becoming. | next_action: verify book of genesis wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Heading wording may shift with lexical review | decision: Keep book of genesis wording provisional | status: pending

## Genesis 2:5

Greek: καὶ πᾶν χλωρὸν ἀγροῦ πρὸ τοῦ γενέσθαι ἐπὶ τῆς γῆς καὶ πάντα χόρτον ἀγροῦ πρὸ τοῦ ἀνατεῖλαι· οὐ γὰρ ἔβρεξεν ὁ Θεὸς ἐπὶ τὴν γῆν, καὶ ἄνθρωπος οὐκ ἦν ἐργάζεσθαι αὐτήν·
Transliteration: kai pan chlōron agrou pro tou genesthai epi tes ges kai panta chorton agrou pro tou anateilai; ou gar ebrexen ho Theos epi tēn gēn, kai anthrōpos ouk ēn ergazesthai autēn;
Literal gloss: And every green thing of field before it came to be upon the earth and every grass of field before it sprang up; for God had not rained upon the earth, and human was not to work it.
Syntax notes: The verse layers pre-conditions before cultivated growth. The infinitive ἐργάζεσθαι states intended labor on the ground.
Draft translation: And every green thing of the field was there before it came to be on the earth, and every grass of the field before it sprang up; for God had not rained on the earth, and there was no human to work it.

Decision rows:
- greek_phrase: ἄνθρωπος οὐκ ἦν ἐργάζεσθαι αὐτήν | lemma: ἄνθρωπος | ἐργάζομαι | morphology: noun + infinitive clause | chosen_rendering: there was no human to work it | alternate_renderings: no one was there to cultivate it | rationale: Keeps the labor motif visible before the formed human appears. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Cultivation wording may shift with lexical review | decision: Keep work it wording provisional | status: pending

## Genesis 2:6

Greek: πηγὴ δὲ ἀνέβαινεν ἐκ τῆς γῆς καὶ ἐπότιζε πᾶν τὸ πρόσωπον τῆς γῆς.
Transliteration: pēgē de anebainen ek tēs gēs kai epotize pan to prosōpon tēs gēs.
Literal gloss: But a spring was rising from the earth and watering all the face of the earth.
Syntax notes: δὲ marks scene continuation. πρόσωπον τῆς γῆς is a surface-expression: face or whole surface of the ground.
Draft translation: But a spring was rising from the earth and watering the whole face of the ground.

Decision rows:
- greek_phrase: πηγή | lemma: πηγή | morphology: nominative singular noun | chosen_rendering: spring | alternate_renderings: mist; fountain; water source | rationale: Spring fits the rising-water image better than a vague mist for now. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: spring | footnote_text: Greek pege usually points to a spring or water source. This draft does not use 'mist' because the verse describes water rising and watering the ground. | source_basis: lexical + context | status: drafted

Logos research:
- greek_phrase: πηγή | lemma: πηγή | resource: LLS:FBLXXLEX | usage_note: Check whether pege in this verse can support spring, fountain, or mist; context may favor rising water source. | next_action: verify spring wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Water-source wording may shift with lexical review | decision: Keep spring wording provisional | status: pending

## Genesis 2:7

Greek: καὶ ἔπλασεν ὁ Θεὸς τὸν ἄνθρωπον, χοῦν ἀπὸ τῆς γῆς, καὶ ἐνεφύσησεν εἰς τὸ πρόσωπον αὐτοῦ πνοὴν ζωῆς, καὶ ἐγένετο ὁ ἄνθρωπος εἰς ψυχὴν ζῶσαν.
Transliteration: kai eplasen ho Theos ton anthrōpon, choun apo tēs gēs, kai enephysēsen eis to prosōpon autou pnoēn zōēs, kai egeneto ho anthrōpos eis psychēn zōsan.
Literal gloss: And God formed the human, dust from the earth, and breathed into his face breath of life, and the human became into a living being.
Syntax notes: πλάσσω gives shaping imagery. πνοὴ ζωῆς and ψυχὴ ζῶσα tightly link breath and animate life.
Draft translation: And God formed the human from dust of the earth and breathed into his face the breath of life, and the human became a living creature.

Decision rows:
- greek_phrase: ἔπλασεν | lemma: πλάσσω | morphology: aorist active indicative 3 singular | chosen_rendering: formed | alternate_renderings: fashioned; shaped | rationale: Formed keeps the hands-on shaping image clear. | status: drafted
- greek_phrase: πνοὴν ζωῆς | lemma: πνοή | ζωή | morphology: accusative noun phrase | chosen_rendering: the breath of life | alternate_renderings: breath of living; life-breath | rationale: Classic phrase but still direct and concrete. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: formed | footnote_text: The Greek verb suggests shaping or molding, not merely making in a general sense. The line narrows creation imagery from broad making to formed craftsmanship. | source_basis: lexical + imagery | status: drafted

Logos research:
- greek_phrase: πλάσσω / πνοὴ ζωῆς | lemma: πλάσσω | πνοή | ζωή | resource: LLS:FBLXXLEX | usage_note: Check shaping imagery and relation between breath-of-life phrase here and similar Greek expressions elsewhere. | next_action: verify formed breath wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Formation and breath wording may shift after lexical review | decision: Keep formed wording provisional | status: pending

## Genesis 2:8

Greek: Καὶ ἐφύτευσεν ὁ Θεὸς παράδεισον ἐν ᾿Εδὲμ κατὰ ἀνατολὰς καὶ ἔθετο ἐκεῖ τὸν ἄνθρωπον, ὃν ἔπλασε.
Transliteration: Kai ephyteusen ho Theos paradeison en Edem kata anatolas kai etheto ekei ton anthrōpon, hon eplase.
Literal gloss: And God planted a garden in Eden toward the east and placed there the human, whom he formed.
Syntax notes: παράδεισος is a planted park or garden-space. κατὰ ἀνατολάς marks eastward orientation.
Draft translation: And God planted a garden in Eden toward the east, and he placed there the human whom he formed.

Decision rows:
- greek_phrase: παράδεισον | lemma: παράδεισος | morphology: accusative singular noun | chosen_rendering: garden | alternate_renderings: park; paradise | rationale: Garden reads naturally while remaining open to richer park imagery in notes. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: garden | footnote_text: Greek paradeisos can denote a planted park or enclosed pleasure-garden. 'Garden' stays readable while leaving room for a fuller note later. | source_basis: lexical + context | status: drafted

Logos research:
- greek_phrase: παράδεισος | lemma: παράδεισος | resource: LLS:FBLXXLEX | usage_note: Check semantic range of paradeisos in Hellenistic Greek: garden, orchard-park, or enclosed pleasure-ground. | next_action: verify garden wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Paradeisos wording may shift with lexical review | decision: Keep garden wording provisional | status: pending

## Genesis 2:9

Greek: καὶ ἐξανέτειλεν ὁ Θεὸς ἔτι ἐκ τῆς γῆς πᾶν ξύλον ὡραῖον εἰς ὅρασιν καὶ καλὸν εἰς βρῶσιν καὶ τὸ ξύλον τῆς ζωῆς ἐν μέσῳ τοῦ παραδείσου καὶ τὸ ξύλον τοῦ εἰδέναι γνωστὸν καλοῦ καὶ πονηροῦ.
Transliteration: kai exaneteilen ho Theos eti ek tēs gēs pan xylon hōraion eis horasin kai kalon eis brōsin kai to xylon tēs zōēs en mesō tou paradeisou kai to xylon tou eidenai gnōston kalou kai ponērou.
Literal gloss: And God still caused to spring up from the earth every tree beautiful for sight and good for food, and the tree of life in the middle of the garden, and the tree of knowing the known of good and evil.
Syntax notes: The last tree phrase is syntactically odd in Greek. The line stresses both visual delight and nourishment.
Draft translation: And God still caused every tree to spring up from the earth, beautiful to look at and good for food, and the tree of life in the middle of the garden, and the tree of knowing good and evil.

Decision rows:
- greek_phrase: τὸ ξύλον τοῦ εἰδέναι γνωστὸν καλοῦ καὶ πονηροῦ | lemma: ξύλον | εἰδέναι | γνωστός | morphology: genitive + infinitive phrase | chosen_rendering: the tree of knowing good and evil | alternate_renderings: the tree of knowing what is known of good and evil | rationale: The Greek is odd, but this draft keeps the familiar core without pretending the syntax is simple. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: tree of knowing good and evil | footnote_text: The Greek wording is somewhat awkward here and may be more complex than the smoother English phrase suggests. This draft keeps the usual sense while marking the line for later review. | source_basis: syntax + lexical | status: drafted

Logos research:
- greek_phrase: τοῦ εἰδέναι γνωστὸν καλοῦ καὶ πονηροῦ | lemma: οἶδα | γνωστός | καλός | πονηρός | resource: LLS:GRAMSPTGRK | usage_note: Check syntax of the tree-of-knowing phrase; Greek wording seems less smooth than standard English tradition. | next_action: verify tree knowing wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Tree-of-knowing phrase may shift after grammar review | decision: Keep knowing good and evil wording provisional | status: pending

## Genesis 2:10

Greek: ποταμὸς δὲ ἐκπορεύεται ἐξ ᾿Εδὲμ ποτίζειν τὸν παράδεισον· ἐκεῖθεν ἀφορίζεται εἰς τέσσαρας ἀρχάς.
Transliteration: potamos de ekporeuetai ex Edem potizein ton paradeison; ekeithen aphorizetai eis tessaras archas.
Literal gloss: But a river goes out from Eden to water the garden; from there it is divided into four heads.
Syntax notes: Present verbs make the description vivid. ἀρχαί here are source-heads or branch-heads of the river system.
Draft translation: But a river goes out from Eden to water the garden; from there it is divided into four heads.

Decision rows:
- greek_phrase: εἰς τέσσαρας ἀρχάς | lemma: ἀρχή | morphology: prepositional phrase | chosen_rendering: into four heads | alternate_renderings: into four sources; into four branches | rationale: Heads is traditional and maps well to river-head language. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: four heads | footnote_text: Greek speaks of the river dividing into four 'heads,' a term used for source-points or chief branches. This draft keeps that concrete image. | source_basis: lexical + imagery | status: drafted

Logos research:
- greek_phrase: εἰς τέσσαρας ἀρχάς | lemma: ἀρχή | resource: LLS:FBLXXLEX | usage_note: Check whether the river phrase is best rendered heads, sources, or chief branches. | next_action: verify four heads wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: River-head wording may shift with lexical review | decision: Keep four heads wording provisional | status: pending

## Genesis 2:11

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:12

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:13

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:14

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:15

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:16

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:17

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:18

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:19

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:20

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:21

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:22

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:23

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:24

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:25

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

# Chapter 3

## Genesis 3:1

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:2

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:3

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:4

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:5

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:6

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:7

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:8

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:9

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:10

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:11

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:12

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:13

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:14

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:15

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:16

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:17

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:18

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:19

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:20

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:21

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:22

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:23

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:24

Greek: [TODO add Greek text]
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: [TODO]

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]
