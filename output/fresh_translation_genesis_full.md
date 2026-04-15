# Fresh Translation Worksheet

Scope: Genesis 1-50

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

Greek: ὄνομα τῷ ἑνὶ Φισῶν· οὗτος ὁ κυκλῶν πᾶσαν τὴν γῆν Εὐιλάτ, ἐκεῖ οὗ ἐστι τὸ χρυσίον·
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: The name of the first is Pishon; this is the one that circles all the land of Havilah, where the gold is.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:12

Greek: τὸ δὲ χρυσίον τῆς γῆς ἐκείνης καλόν· καὶ ἐκεῖ ἐστιν ὁ ἄνθραξ καὶ ὁ λίθος ὁ πράσινος.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the gold of that land is good; and there too are the carbuncle and the green stone.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:13

Greek: καὶ ὄνομα τῷ ποταμῷ τῷ δευτέρῳ Γεῶν· οὗτος ὁ κυκλῶν πᾶσαν τὴν γῆν Αἰθιοπίας.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the name of the second river is Gihon; this is the one that circles all the land of Ethiopia.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:14

Greek: καὶ ὁ ποταμὸς ὁ τρίτος Τίγρις· οὗτος ὁ προπορευόμενος κατέναντι ᾿Ασσυρίων. ὁ δὲ ποταμὸς ὁ τέταρτος Εὐφράτης.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the third river is Tigris; this is the one that goes opposite the Assyrians. And the fourth river is Euphrates.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:15

Greek: Καὶ ἔλαβε Κύριος ὁ Θεὸς τὸν ἄνθρωπον, ὃν ἔπλασε, καὶ ἔθετο αὐτὸν ἐν τῷ παραδείσῳ τῆς τρυφῆς, ἐργάζεσθαι αὐτὸν καὶ φυλάσσειν.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord God took the human whom he had formed and placed him in the garden of delight, to work it and to keep it.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:16

Greek: καὶ ἐνετείλατο Κύριος ὁ Θεὸς τῷ ᾿Αδὰμ λέγων· ἀπὸ παντὸς ξύλου τοῦ ἐν τῷ παραδείσῳ βρώσει φαγῇ,
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord God commanded Adam, saying that from every tree in the garden he might surely eat,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:17

Greek: ἀπὸ δὲ τοῦ ξύλου τοῦ γινώσκειν καλὸν καὶ πονηρόν, οὐ φάγεσθε ἀπ᾿ αὐτοῦ· ᾗ δ᾿ ἂν ἡμέρᾳ φάγητε ἀπ᾿ αὐτοῦ, θανάτῳ ἀποθανεῖσθε.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: but from the tree of knowing good and evil, he was not to eat from it; on the day he ate from it, he would certainly die.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:18

Greek: Καὶ εἶπε Κύριος ὁ Θεός· οὐ καλὸν εἶναι τὸν ἄνθρωπον μόνον· ποιήσωμεν αὐτῷ βοηθὸν κατ᾿ αὐτόν.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord God said, 'It is not good for the human to be alone. Let us make for him a helper corresponding to him.'

Decision rows:
- greek_phrase: βοηθὸν κατ᾿ αὐτόν | lemma: βοηθός | κατά | morphology: accusative phrase | chosen_rendering: a helper corresponding to him | alternate_renderings: a helper fit for him; a helper matching him | rationale: Corresponding keeps the relational sense without flattening it into mere utility. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: helper corresponding to him | footnote_text: Greek does not merely say 'helper' but adds language of correspondence or counterpart. This draft aims to preserve mutual fit rather than infer lesser status. | source_basis: lexical + context | status: drafted

Logos research:
- greek_phrase: βοηθὸν κατ᾿ αὐτόν | lemma: βοηθός | κατά | resource: LLS:FBLXXLEX | usage_note: Check whether the phrase points to correspondence, likeness, equality, or simple suitability in Septuagint Greek. | next_action: verify helper corresponding wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Helper phrase wording may shift with lexical review | decision: Keep helper corresponding wording provisional | status: pending

## Genesis 2:19

Greek: καὶ ἔπλασεν ὁ Θεὸς ἔτι ἐκ τῆς γῆς πάντα τὰ θηρία τοῦ ἀγροῦ καὶ πάντα τὰ πετεινὰ τοῦ οὐρανοῦ καὶ ἤγαγεν αὐτὰ πρὸς τὸν ᾿Αδάμ, ἰδεῖν τί καλέσει αὐτά. καὶ πᾶν ὃ ἐὰν ἐκάλεσεν αὐτὸ ᾿Αδὰμ ψυχὴν ζῶσαν, τοῦτο ὄνομα αὐτῷ.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God still formed from the earth all the beasts of the field and all the birds of Heaven, and brought them to Adam to see what he would call them. And whatever Adam called each living creature, that was its name.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:20

Greek: καὶ ἐκάλεσεν ᾿Αδὰμ ὀνόματα πᾶσι τοῖς κτήνεσι καὶ πᾶσι τοῖς πετεινοῖς τοῦ οὐρανοῦ καὶ πᾶσι τοῖς θηρίοις τοῦ ἀγροῦ· τῷ δὲ ᾿Αδὰμ οὐχ εὑρέθη βοηθὸς ὅμοιος αὐτῷ.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Adam gave names to all the livestock and to all the birds of Heaven and to all the beasts of the field. But for Adam no helper like him was found.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:21

Greek: καὶ ἐπέβαλεν ὁ Θεὸς ἔκστασιν ἐπὶ τὸν ᾿Αδάμ, καὶ ὕπνωσε· καὶ ἔλαβε μίαν τῶν πλευρῶν αὐτοῦ καὶ ἀνεπλήρωσε σάρκα ἀντ᾿ αὐτῆς.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God cast an ecstasy on Adam, and he slept; and he took one of his sides and filled flesh in its place.

Decision rows:
- greek_phrase: ἔκστασιν / πλευρῶν | lemma: ἔκστασις | πλευρά | morphology: accusative noun + genitive plural | chosen_rendering: ecstasy / sides | alternate_renderings: deep sleep / ribs | rationale: This draft keeps the Greek's stronger trance-language and the broader side-image alive for now. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: ecstasy | footnote_text: Greek says God cast an ekstasis on Adam, a stronger term than ordinary sleep. This draft keeps the trance-like force of the line open for readers. | source_basis: lexical + imagery | status: drafted

Logos research:
- greek_phrase: ἔκστασιν / πλευρά | lemma: ἔκστασις | πλευρά | resource: LLS:FBLXXLEX | usage_note: Check whether ekstasis here should remain trance/ecstasy language and whether pleura is better side than rib. | next_action: verify ecstasy side wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Ekstasis and side/rib wording may shift after lexical review | decision: Keep ecstasy side wording provisional | status: pending

## Genesis 2:22

Greek: καὶ ᾠκοδόμησεν ὁ Θεὸς τὴν πλευράν, ἣν ἔλαβεν ἀπὸ τοῦ ᾿Αδάμ, εἰς γυναῖκα καὶ ἤγαγεν αὐτὴν πρὸς τὸν ᾿Αδάμ.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God built the side that he had taken from Adam into a woman and brought her to Adam.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:23

Greek: καὶ εἶπεν ᾿Αδάμ· τοῦτο νῦν ὀστοῦν ἐκ τῶν ὀστέων μου καὶ σὰρξ ἐκ τῆς σαρκός μου· αὕτη κληθήσεται γυνή, ὅτι ἐκ τοῦ ἀνδρὸς αὐτῆς ἐλήφθη αὕτη·
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Adam said, 'This now is bone from my bones and flesh from my flesh. She shall be called woman, because she was taken from her man.'

Decision rows:
- greek_phrase: γυνή / ἀνήρ | lemma: γυνή | ἀνήρ | morphology: paired nouns | chosen_rendering: woman / man | alternate_renderings: wife / husband | rationale: This draft keeps the wordplay visible, even though the Greek phrase remains slightly awkward in English. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: woman / man | footnote_text: The Greek wording preserves a close relation between the terms for woman and man. This draft keeps the pair audible even though the English remains somewhat strained. | source_basis: lexical + discourse | status: drafted

Logos research:
- greek_phrase: γυνή / ἀνήρ | lemma: γυνή | ἀνήρ | resource: LLS:GRAMSPTGRK | usage_note: Check how the Greek preserves or reshapes the man/woman wordplay in this line. | next_action: verify woman man wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Wordplay wording may shift after grammar review | decision: Keep woman/man wording provisional | status: pending

## Genesis 2:24

Greek: ἕνεκεν τούτου καταλείψει ἄνθρωπος τὸν πατέρα αὐτοῦ καὶ τὴν μητέρα καὶ προσκολληθήσεται πρὸς τὴν γυναῖκα αὐτοῦ, καὶ ἔσονται οἱ δύο εἰς σάρκα μίαν.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Because of this, a man will leave his father and his mother and be joined to his wife, and the two will become one flesh.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 2:25

Greek: καὶ ἦσαν οἱ δύο γυμνοί, ὅ τε ᾿Αδὰμ καὶ ἡ γυνὴ αὐτοῦ, καὶ οὐκ ᾐσχύνοντο.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the two were naked, Adam and his wife, and they were not ashamed.

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

Greek: Οδὲ ὄφις ἦν φρονιμώτατος πάντων τῶν θηρίων τῶν ἐπὶ τῆς γῆς, ὧν ἐποίησε Κύριος ὁ Θεός. καὶ εἶπεν ὁ ὄφις τῇ γυναικί· τί ὅτι εἶπεν ὁ Θεός, οὐ μὴ φάγητε ἀπὸ παντὸς ξύλου τοῦ παραδείσου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now the serpent was the most prudent of all the beasts on the earth that the Lord God had made. And the serpent said to the woman, 'Why is it that God said, "You shall not eat from every tree of the garden"?'

Decision rows:
- greek_phrase: φρονιμώτατος | lemma: φρόνιμος | morphology: superlative adjective | chosen_rendering: the most prudent | alternate_renderings: the most shrewd; the most crafty | rationale: Prudent keeps the intelligence sense without forcing a fully negative reading too early. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: most prudent | footnote_text: Greek phronimos can suggest practical intelligence, shrewdness, or craft. This draft keeps the serpent's mental sharpness in view without locking the term into one moral shade. | source_basis: lexical | status: drafted

Logos research:
- greek_phrase: φρονιμώτατος | lemma: φρόνιμος | resource: LLS:FBLXXLEX | usage_note: Check whether phronimos here leans prudent, shrewd, intelligent, or crafty in comparable Greek usage. | next_action: verify prudent wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Serpent adjective wording may shift with lexical review | decision: Keep prudent wording provisional | status: pending

## Genesis 3:2

Greek: καὶ εἶπεν ἡ γυνὴ τῷ ὄφει· ἀπὸ καρποῦ τοῦ ξύλου τοῦ παραδείσου φαγούμεθα,
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the woman said to the serpent that they would eat from the fruit of the trees of the garden,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:3

Greek: ἀπὸ δὲ τοῦ καρποῦ τοῦ ξύλου, ὅ ἐστιν ἐν μέσῳ τοῦ παραδείσου, εἶπεν ὁ Θεός, οὐ φάγεσθε ἀπ᾿ αὐτοῦ, οὐ δὲ μὴ ἅψησθε αὐτοῦ, ἵνα μὴ ἀποθάνητε.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: but from the fruit of the tree that is in the middle of the garden, God had said they should not eat from it, nor indeed touch it, lest they die.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:4

Greek: καὶ εἶπεν ὁ ὄφις τῇ γυναικί· οὐ θανάτῳ ἀποθανεῖσθε·
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the serpent said to the woman that they would certainly not die.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:5

Greek: ᾔδει γὰρ ὁ Θεός, ὅτι ᾗ ἂν ἡμέρᾳ φάγητε ἀπ᾿ αὐτοῦ, διανοιχθήσονται ὑμῶν οἱ ὀφθαλμοὶ καὶ ἔσεσθε ὡς θεοί, γινώσκοντες καλὸν καὶ πονηρόν.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: For God knew that on the day you eat from it, your eyes will be opened and you will be like gods, knowing good and evil.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:6

Greek: καὶ εἶδεν ἡ γυνή, ὅτι καλὸν τὸ ξύλον εἰς βρῶσιν καὶ ὅτι ἀρεστὸν τοῖς ὀφθαλμοῖς ἰδεῖν καὶ ὡραῖόν ἐστι τοῦ κατανοῆσαι, καὶ λαβοῦσα ἀπὸ τοῦ καρποῦ αὐτοῦ ἔφαγε· καὶ ἔδωκε καὶ τῷ ἀνδρὶ αὐτῆς μετ᾿ αὐτῆς, καὶ ἔφαγον.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the woman saw that the tree was good for food and pleasing to the eyes to look at, and that it was beautiful for understanding. And taking from its fruit, she ate; and she gave also to her husband with her, and they ate.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:7

Greek: καὶ διηνοίχθησαν οἱ ὀφθαλμοὶ τῶν δύο, καὶ ἔγνωσαν ὅτι γυμνοὶ ἦσαν, καὶ ἔρραψαν φύλλα συκῆς καὶ ἐποίησαν ἑαυτοῖς περιζώματα.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the eyes of the two were opened, and they knew that they were naked, and they sewed fig leaves together and made loincloths for themselves.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:8

Greek: Καὶ ἤκουσαν τῆς φωνῆς Κυρίου τοῦ Θεοῦ περιπατοῦντος ἐν τῷ παραδείσῳ τὸ δειλινόν, καὶ ἐκρύβησαν ὅ τε ᾿Αδὰμ καὶ ἡ γυνὴ αὐτοῦ ἀπὸ προσώπου Κυρίου τοῦ Θεοῦ ἐν μέσῳ τοῦ ξύλου τοῦ παραδείσου.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they heard the sound of the Lord God walking in the garden at evening, and Adam and his wife hid themselves from the face of the Lord God among the trees of the garden.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:9

Greek: καὶ ἐκάλεσε Κύριος ὁ Θεὸς τὸν ᾿Αδὰμ καὶ εἶπεν αὐτῷ· ᾿Αδάμ, ποῦ εἶ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord God called Adam and said to him, 'Adam, where are you?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:10

Greek: καὶ εἶπεν αὐτῷ· τῆς φωνῆς σου ἤκουσα περιπατοῦντος ἐν τῷ παραδείσῳ καὶ ἐφοβήθην, ὅτι γυμνός εἰμι, καὶ ἐκρύβην.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said to him, 'I heard your sound as you were walking in the garden, and I was afraid because I am naked, and I hid myself.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:11

Greek: καὶ εἶπεν αὐτῷ ὁ Θεός· τίς ἀνήγγειλέ σοι ὅτι γυμνὸς εἶ, εἰ μὴ ἀπὸ τοῦ ξύλου, οὗ ἐνετειλάμην σοι τούτου μόνου μὴ φαγεῖν, ἀπ᾿ αὐτοῦ ἔφαγες
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God said to him, 'Who told you that you are naked, unless you have eaten from the tree from which alone I commanded you not to eat?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:12

Greek: καὶ εἶπεν ὁ ᾿Αδάμ· ἡ γυνή, ἣν ἔδωκας μετ᾿ ἐμοῦ, αὕτη μοι ἔδωκεν ἀπὸ τοῦ ξύλου, καὶ ἔφαγον.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Adam said, 'The woman whom you gave with me, she gave me from the tree, and I ate.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:13

Greek: καὶ εἶπε Κύριος ὁ Θεὸς τῇ γυναικί· τί τοῦτο ἐποίησας; καὶ εἶπεν ἡ γυνή· ὁ ὄφις ἠπάτησέ με, καὶ ἔφαγον.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord God said to the woman, 'What is this you have done?' And the woman said, 'The serpent deceived me, and I ate.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:14

Greek: καὶ εἶπε Κύριος ὁ Θεὸς τῷ ὄφει· ὅτι ἐποίησας τοῦτο, ἐπικατάρατος σὺ ἀπὸ πάντων τῶν κτηνῶν καὶ ἀπὸ πάντων τῶν θηρίων τῶν ἐπὶ τῆς γῆς· ἐπὶ τῷ στήθει σου καὶ τῇ κοιλίᾳ πορεύσῃ καὶ γῆν φαγῇ πάσας τὰς ἡμέρας τῆς ζωῆς σου.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord God said to the serpent that because you did this, you are cursed above all livestock and above all the beasts on the earth. On your chest and your belly you will go, and earth you will eat all the days of your life.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:15

Greek: καὶ ἔχθραν θήσω ἀνὰ μέσον σοῦ καὶ ἀνὰ μέσον τῆς γυναικὸς καὶ ἀνὰ μέσον τοῦ σπέρματός σου καὶ ἀνὰ μέσον τοῦ σπέρματος αὐτῆς· αὐτός σου τηρήσει κεφαλήν, καὶ σὺ τηρήσεις αὐτοῦ πτέρναν.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he would put enmity between you and the woman, and between your seed and her seed. He will watch your head, and you will watch his heel.

Decision rows:
- greek_phrase: τηρήσει κεφαλήν / πτέρναν | lemma: τηρέω | κεφαλή | πτέρνα | morphology: future verb + objects | chosen_rendering: watch your head / watch his heel | alternate_renderings: strike your head / strike his heel; keep your head / keep his heel | rationale: The Greek verb is not the usual verb for crushing, so the draft keeps a more cautious rendering pending further review. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: watch your head | footnote_text: The Greek verb here is not the common verb for crush or strike. This draft keeps a more cautious wording until fuller lexical and textual review is complete. | source_basis: lexical + textual | status: drafted

Logos research:
- greek_phrase: τηρέω | lemma: τηρέω | resource: LLS:FBLXXLEX | usage_note: Check semantic range of tereo here and whether stronger hostile sense is warranted in this context. | next_action: verify watch head heel wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Head/heel verb wording likely needs close lexical review | decision: Keep watch wording provisional | status: pending

## Genesis 3:16

Greek: καὶ τῇ γυναικὶ εἶπε· πληθύνων πληθυνῶ τὰς λύπας σου καὶ τὸν στεναγμόν σου· ἐν λύπαις τέξῃ τέκνα, καὶ πρὸς τὸν ἄνδρα σου ἡ ἀποστροφή σου, καὶ αὐτός σου κυριεύσει.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And to the woman he said that multiplying he would multiply your pains and your groaning. In pains you will bear children, and your turning will be toward your husband, and he will rule over you.

Decision rows:
- greek_phrase: ἡ ἀποστροφή σου | lemma: ἀποστροφή | morphology: nominative singular noun | chosen_rendering: your turning | alternate_renderings: your desire; your return | rationale: Turning stays closest to the Greek noun and avoids importing later traditional wording too quickly. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: your turning | footnote_text: Greek uses a noun of turning or orientation here, not the later traditional wording 'desire.' This draft keeps the directional sense visible. | source_basis: lexical + context | status: drafted

Logos research:
- greek_phrase: ἀποστροφή | lemma: ἀποστροφή | resource: LLS:FBLXXLEX | usage_note: Check whether apostrophe here means turning, return, dependence, or desire-like orientation. | next_action: verify turning wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Turning/desire wording may shift with lexical review | decision: Keep turning wording provisional | status: pending

## Genesis 3:17

Greek: τῷ δὲ ᾿Αδὰμ εἶπεν· ὅτι ἤκουσας τῆς φωνῆς τῆς γυναικός σου καὶ ἔφαγες ἀπὸ τοῦ ξύλου, οὗ ἐνετειλάμην σοι τούτου μόνου μὴ φαγεῖν, ἀπ᾿ αὐτοῦ ἔφαγες, ἐπικατάρατος ἡ γῆ ἐν τοῖς ἔργοις σου· ἐν λύπαις φαγῇ αὐτὴν πάσας τὰς ἡμέρας τῆς ζωῆς σου·
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And to Adam he said that because you listened to the voice of your wife and ate from the tree from which alone he commanded you not to eat, the ground is cursed in your works. In pains you will eat from it all the days of your life.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:18

Greek: ἀκάνθας καὶ τριβόλους ἀνατελεῖ σοι, καὶ φαγῇ τὸν χόρτον τοῦ ἀγροῦ.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: It will bring forth thorns and thistles for you, and you will eat the grass of the field.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:19

Greek: ἐν ἱδρῶτι τοῦ προσώπου σου φαγῇ τὸν ἄρτον σου, ἕως τοῦ ἀποστρέψαι σε εἰς τὴν γῆν, ἐξ ἧς ἐλήφθης, ὅτι γῆ εἶ καὶ εἰς γῆν ἀπελεύσῃ·
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: By the sweat of your face you will eat your bread, until you return to the earth from which you were taken; because earth you are, and to earth you will depart.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:20

Greek: καὶ ἐκάλεσεν ᾿Αδὰμ τὸ ὄνομα τῆς γυναικὸς αὐτοῦ Ζωή, ὅτι αὕτη μήτηρ πάντων τῶν ζώντων.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Adam called the name of his wife Life, because she is the mother of all the living.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:21

Greek: Καὶ ἐποίησε Κύριος ὁ Θεὸς τῷ ᾿Αδὰμ καὶ τῇ γυναικὶ αὐτοῦ χιτῶνας δερματίνους καὶ ἐνέδυσεν αὐτούς.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord God made skin tunics for Adam and for his wife, and clothed them.

Decision rows:
- greek_phrase: χιτῶνας δερματίνους | lemma: χιτών | δερμάτινος | morphology: accusative plural phrase | chosen_rendering: skin tunics | alternate_renderings: garments of skin; leather tunics | rationale: Skin tunics is plain, concrete, and close to the Greek image. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: skin tunics | footnote_text: The phrase is concrete and bodily. This draft avoids softer wording like 'clothes' so the image stays stark and material. | source_basis: lexical + imagery | status: drafted

Logos research:
- greek_phrase: χιτῶνας δερματίνους | lemma: χιτών | δερμάτινος | resource: LLS:FBLXXLEX | usage_note: Check whether dermatinous should remain skin/leather and whether chiton here needs tunic, tunics, or garments. | next_action: verify skin tunics wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Skin tunics wording may shift with lexical review | decision: Keep skin tunics wording provisional | status: pending

## Genesis 3:22

Greek: καὶ εἶπεν ὁ Θεός· ἰδοὺ ᾿Αδὰμ γέγονεν ὡς εἷς ἐξ ἡμῶν, τοῦ γινώσκειν καλὸν καὶ πονηρόν· καὶ νῦν μή ποτε ἐκτείνῃ τὴν χεῖρα αὐτοῦ καὶ λάβῃ ἀπὸ τοῦ ξύλου τῆς ζωῆς καὶ φάγῃ καὶ ζήσεται εἰς τὸν αἰῶνα.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God said, 'Look, Adam has become like one of us, to know good and evil. And now, lest perhaps he stretch out his hand and take from the tree of life and eat and live forever.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:23

Greek: καὶ ἐξαπέστειλεν αὐτὸν Κύριος ὁ Θεὸς ἐκ τοῦ παραδείσου τῆς τρυφῆς ἐργάζεσθαι τὴν γῆν, ἐξ ἧς ἐλήφθη.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord God sent him out from the garden of delight to work the earth from which he had been taken.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Genesis 3:24

Greek: καὶ ἐξέβαλε τὸν ᾿Αδὰμ καὶ κατῴκισεν αὐτὸν ἀπέναντι τοῦ παραδείσου τῆς τρυφῆς καὶ ἔταξε τὰ Χερουβὶμ καὶ τὴν φλογίνην ρομφαίαν τὴν στρεφομένην φυλάσσειν τὴν ὁδὸν τοῦ ξύλου τῆς ζωῆς.
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he cast Adam out and settled him opposite the garden of delight, and he stationed the Cherubim and the flaming turning sword to guard the way of the tree of life.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

# Chapter 4

## Genesis 4:1

Greek: ΑΔΑΜ δὲ ἔγνω Εὔαν τὴν γυναῖκα αὐτοῦ, καὶ συλλαβοῦσα ἔτεκε τὸν Κάϊν καὶ εἶπεν· ἐκτησάμην ἄνθρωπον διά τοῦ Θεοῦ.
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

## Genesis 4:2

Greek: καὶ προσέθηκε τεκεῖν τὸ ἀδελφὸν αὐτοῦ, τὸν ῎Αβελ. καὶ ἐγένετο ῎Αβελ ποιμὴν προβάτων, Κάϊν δὲ ἦν ἐργαζόμενος τὴν γῆν.
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

## Genesis 4:3

Greek: καὶ ἐγένετο μεθ᾿ ἡμέρας ἤνεγκε Κάϊν ἀπὸ τῶν καρπῶν τῆς γῆς θυσίαν τῷ Κυρίῳ,
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

## Genesis 4:4

Greek: καὶ ῎Αβελ ἤνεγκε καὶ αὐτὸς ἀπὸ τῶν πρωτοτόκων τῶν προβάτων αὐτοῦ καὶ ἀπὸ τῶν στεάτων αὐτῶν. καὶ ἐπεῖδεν ὁ Θεὸς ἐπί ῎Αβελ καὶ ἐπὶ τοῖς δώροις αὐτοῦ,
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

## Genesis 4:5

Greek: ἐπὶ δὲ Κάϊν καὶ ἐπὶ ταῖς θυσίαις αὐτοῦ οὐ προσέσχε. καὶ ἐλυπήθη Κάϊν λίαν, καὶ συνέπεσε τῷ προσώπῳ αὐτοῦ.
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

## Genesis 4:6

Greek: καὶ εἶπε Κύριος ὁ Θεὸς τῷ Κάϊν· ἵνα τί περίλυπος ἐγένου, καὶ ἵνα τί συνέπεσε τὸ πρόσωπόν σου
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

## Genesis 4:7

Greek: οὐκ ἐὰν ὀρθῶς προσενέγκῃς, ὀρθῶς δὲ μὴ διέλῃς, ἥμαρτες; ἡσύχασον· πρὸς σὲ ἡ ἀποστροφὴ αὐτοῦ, καὶ σὺ ἄρξεις αὐτοῦ.
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

## Genesis 4:8

Greek: καὶ εἶπε Κάϊν πρὸς ῎Αβελ τὸν ἀδελφὸν αὐτοῦ· διέλθωμεν εἰς τὸ πεδίον. καὶ ἐγένετο ἐν τῷ εἶναι αὐτοὺς ἐν τῷ πεδίῳ, ἀνέστη Κάϊν ἐπὶ ῎Αβελ τὸν ἀδελφὸν αὐτοῦ καὶ ἀπέκτεινεν αὐτόν.
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

## Genesis 4:9

Greek: καὶ εἶπε Κύριος ὁ Θεὸς πρὸς Κάϊν· ποῦ ἔστιν ῎Αβελ ὁ ἀδελφός σου; καὶ εἶπεν· οὐ γινώσκω· μὴ φύλαξ τοῦ ἀδελφοῦ μου εἰμὶ ἐγώ
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

## Genesis 4:10

Greek: καί εἶπε Κύριος· τί πεποίηκας; φωνὴ αἵματος τοῦ ἀδελφοῦ σου βοᾷ πρός με ἐκ τῆς γῆς.
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

## Genesis 4:11

Greek: καὶ νῦν ἐπικατάρατος σὺ ἀπὸ τῆς γῆς, ἣ ἔχανε τὸ στόμα αὐτῆς δέξασθαι τὸ αἷμα τοῦ ἀδελφοῦ σου ἐκ τῆς χειρός σου·
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

## Genesis 4:12

Greek: ὅτε ἐργᾷ τὴν γῆν, καὶ οὐ προσθήσει τὴν ἰσχὺν αὐτῆς δοῦναί σοι· στένων καὶ τρέμων ἔσῃ ἐπὶ τῆς γῆς.
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

## Genesis 4:13

Greek: καὶ εἶπε Κάϊν πρὸς Κύριον τὸν Θεόν· μείζων ἡ αἰτία μου τοῦ ἀφεθῆναί με·
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

## Genesis 4:14

Greek: εἰ ἐκβάλλεις με σήμερον ἀπὸ προσώπου τῆς γῆς καὶ ἀπὸ τοῦ προσώπου σου κρυβήσομαι, καὶ ἔσομαι στένων καὶ τρέμων ἐπὶ τῆς γῆς, καὶ ἔσται πᾶς ὁ εὑρίσκων με, ἀποκτενεῖ με.
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

## Genesis 4:15

Greek: καὶ εἶπεν αὐτῷ Κύριος ὁ Θεός· οὐχ οὕτως, πᾶς ὁ ἀποκτείνας Κάϊν ἑπτὰ ἐκδικούμενα παραλύσει. καὶ ἔθετο Κύριος ὁ Θεὸς σημεῖον τῷ Κάϊν τοῦ μὴ ἀνελεῖν αὐτὸν πάντα τὸν εὑρίσκοντα αὐτόν.
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

## Genesis 4:16

Greek: ἐξῆλθε δὲ Κάϊν ἀπὸ προσώπου τοῦ Θεοῦ καὶ ᾤκησεν ἐν γῇ Ναὶδ κατέναντι ᾿Εδέμ.
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

## Genesis 4:17

Greek: Καὶ ἔγνω Κάϊν τὴν γυναῖκα αὐτοῦ, καὶ συλλαβοῦσα ἔτεκε τὸν ᾿Ενώχ. καὶ ἦν οἰκοδομῶν πόλιν καὶ ἐπωνόμασε τὴν πόλιν ἐπὶ τῷ ὀνόματι τοῦ υἱοῦ αὐτοῦ, ᾿Ενώχ.
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

## Genesis 4:18

Greek: ἐγεννήθη δὲ τῷ ᾿Ενὼχ Γαϊδάδ, καὶ Γαϊδὰδ ἐγέννησε τὸν Μαλελεήλ, καὶ Μαλελεὴλ ἐγέννησε τὸν Μαθουσάλα, καὶ Μαθουσάλα ἐγέννησε τὸν Λάμεχ.
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

## Genesis 4:19

Greek: καὶ ἔλαβεν ἑαυτῷ Λάμεχ δύο γυναῖκας, ὄνομα τῇ μιᾷ ᾿Αδά, καὶ ὄνομα τῇ δευτέρᾳ Σελλά.
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

## Genesis 4:20

Greek: καὶ ἔτεκεν ᾿Αδὰ τὸν ᾿Ιωβήλ· οὗτος ἦν πατὴρ οἰκούντων ἐν σκηναῖς κτηνοτροφων.
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

## Genesis 4:21

Greek: καὶ ὄνομα τῷ ἀδελφῷ αὐτοῦ ᾿Ιουβάλ· οὗτος ἦν ὁ καταδείξας ψαλτήριον καὶ κιθάραν.
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

## Genesis 4:22

Greek: Σελλὰ δὲ καὶ αὐτὴ ἔτεκε τὸν Θόβελ, καὶ ἦν σφυροκόπος χαλκεὺς χαλκοῦ καὶ σιδήρου· ἀδελφὴ δὲ Θόβελ Νοεμά.
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

## Genesis 4:23

Greek: εἶπε δὲ Λάμεχ ταῖς ἑαυτοῦ γυναιξίν· ᾿Αδὰ καὶ Σελλά, ἀκούσατέ μου τῆς φωνῆς, γυναῖκες Λάμεχ, ἐνωτίσασθέ μου τοὺς λόγους, ὅτι ἄνδρα ἀπέκτεινα εἰς τραῦμα ἐμοὶ καὶ νεανίσκον εἰς μώλωπα ἐμοί·
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

## Genesis 4:24

Greek: ὅτι ἑπτάκις ἐκδεδίκηται ἐκ Κάϊν, ἐκ δὲ Λάμεχ ἑβδομηκοντάκις ἑπτά.
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

## Genesis 4:25

Greek: ῎Εγνω δὲ ᾿Αδὰμ Εὔαν τὴν γυναῖκα αὐτοῦ, καὶ συλλαβοῦσα ἔτεκεν υἱόν, καὶ ἐπωνόμασε τὸ ὄνομα αὐτοῦ Σήθ, λέγουσα· ἐξανέστησε γάρ μοι ὁ Θεὸς σπέρμα ἕτερον ἀντὶ ῎Αβελ, ὃν ἀπέκτεινε Κάϊν.
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

## Genesis 4:26

Greek: καὶ τῷ Σὴθ ἐγένετο υἱός, ἐπωνόμασε δὲ τὸ ὄνομα αὐτοῦ ᾿Ενώς· οὗτος ἤλπισεν ἐπικαλεῖσθα τὸ ὄνομα Κυρίου τοῦ Θεοῦ.
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

# Chapter 5

## Genesis 5:1

Greek: ΑΥΤΗ ἡ βίβλος γενέσεως ἀνθρώπων· ᾗ ἡμέρᾳ ἐποίησεν ὁ Θεὸς τὸν ᾿Αδάμ, κατ᾿ εἰκόνα Θεοῦ ἐποίησεν αὐτόν·
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

## Genesis 5:2

Greek: ἄρσεν καὶ θῆλυ ἐποίησεν αὐτοὺς καὶ εὐλόγησεν αὐτούς· καὶ ἐπωνόμασε τὸ ὄνομα αὐτοῦ ᾿Αδάμ, ᾗ ἡμέρᾳ ἐποίησεν αὐτούς·
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

## Genesis 5:3

Greek: ἔζησε δὲ ᾿Αδὰμ τριάκοντα καὶ διακόσια ἔτη, καὶ ἐγέννησε κατὰ τὴν ἰδέαν αὐτοῦ καὶ κατὰ τὴν εἰκόνα αὐτοῦ καὶ ἐπωνόμασε τὸ ὄνομα αὐτοῦ Σήθ.
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

## Genesis 5:4

Greek: ἐγένοντο δὲ αἱ ἡμέραι τοῦ ᾿Αδάμ, ἃς ἔζησε μετά τὸ γεννῆσαι αὐτὸν τὸν Σήθ, ἔτη ἑπτακόσια, καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας.
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

## Genesis 5:5

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέραι ᾿Αδάμ, ἃς ἔζησε, τριάκοντα καὶ ἐννακόσια ἔτη, καὶ ἀπέθανεν.
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

## Genesis 5:6

Greek: ῎Εζησε δὲ Σὴθ πέντε καὶ διακόσια ἔτη καὶ ἐγέννησε τὸν ᾿Ενώς.
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

## Genesis 5:7

Greek: καὶ ἔζησε Σὴθ μετὰ τὸ γεννῆσαι αὐτὸν τὸν ᾿Ενὼς ἑπτὰ ἔτη καὶ ἑπτακόσια καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας.
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

## Genesis 5:8

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέραι Σὴθ δώδεκα καὶ ἐννακόσια ἔτη, καὶ ἀπέθανε.
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

## Genesis 5:9

Greek: Καὶ ἔζησεν ᾿Ενὼς ἔτη ἑκατὸν ἐνενήκοντα καὶ ἐγέννησε τὸν Καϊνᾶν.
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

## Genesis 5:10

Greek: καὶ ἔζησεν ᾿Ενὼς μετὰ τὸ γεννῆσαι αὐτὸν τὸν Καϊνᾶν πεντεκαίδεκα ἔτη καὶ ἑπτακόσια καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας.
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

## Genesis 5:11

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέραι ᾿Ενὼς πέντε ἔτη καὶ ἐννακόσια, καὶ ἀπέθανε.
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

## Genesis 5:12

Greek: Καὶ ἔζησε Καϊνᾶν ἑβδομήκοντα καὶ ἑκατὸν ἔτη, καὶ ἐγέννησε τὸν Μαλελεήλ.
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

## Genesis 5:13

Greek: καὶ ἔζησε Καϊνᾶν μετὰ τὸ γεννῆσαι αὐτὸν τὸν Μαλελεὴλ τεσσαράκοντα καὶ ἑπτακόσια ἔτη καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας.
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

## Genesis 5:14

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέρα Καϊνᾶν δέκα ἔτη καὶ ἐννακόσια, καὶ ἀπέθανε.
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

## Genesis 5:15

Greek: Καὶ ἔζησε Μαλελεὴλ πέντε καὶ ἑξήκοντα καὶ ἑκατὸν ἔτη καὶ ἐγέννησε τὸν ᾿Ιάρεδ.
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

## Genesis 5:16

Greek: καὶ ἔζησε Μαλελεὴλ μετὰ τὸ γεννῆσαι αὐτὸν τὸν ᾿Ιάρεδ ἔτη τριάκοντα καὶ ἑπτακόσια καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας.
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

## Genesis 5:17

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέραι Μαλελεήλ, ἔτη πέντε καὶ ἐνενήκοντα καὶ ὀκτακόσια, καὶ ἀπέθανε.
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

## Genesis 5:18

Greek: Καὶ ἔζησεν ᾿Ιάρεδ δύο καὶ ἑξήκοντα ἔτη καὶ ἑκατὸν καὶ ἐγέννησε τὸν ᾿Ενώχ.
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

## Genesis 5:19

Greek: καὶ ἔζησεν ᾿Ιάρεδ μετὰ τὸ γεννῆσαι αὐτὸν τὸν ᾿Ενὼχ ὀκτακόσια ἔτη καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας.
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

## Genesis 5:20

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέραι ᾿Ιάρεδ δύο καὶ ἑξήκοντα καὶ ἐννακόσια ἔτη, καὶ ἀπέθανε.
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

## Genesis 5:21

Greek: Καὶ ἔζησεν ᾿Ενὼχ πέντε καὶ ἑξήκοντα καὶ ἑκατὸν ἔτη καὶ ἐγέννησε τὸν Μαθουσάλα.
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

## Genesis 5:22

Greek: εὐηρέστησε δὲ ᾿Ενὼχ τῷ Θεῷ μετὰ τὸ γεννῆσαι αὐτὸν τὸν Μαθουσάλα διακόσια ἔτη καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας.
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

## Genesis 5:23

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέραι ᾿Ενὼχ πέντε καὶ ἑξήκοντα καὶ τριακόσια ἔτη.
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

## Genesis 5:24

Greek: καὶ εὐηρέστησεν ᾿Ενὼχ τῷ Θεῷ καὶ οὐχ εὑρίσκετο, ὅτι μετέθηκεν αὐτὸν ὁ Θεός.
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

## Genesis 5:25

Greek: Καὶ ἔζησε Μαθουσάλα ἑπτὰ ἔτη καὶ ἑξήκοντα καὶ ἑκατὸν καὶ ἐγέννησε τὸν Λάμεχ.
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

## Genesis 5:26

Greek: καὶ ἔζησε Μαθουσάλα μετὰ τὸ γεννῆσαι αὐτὸν τὸν Λάμεχ δύο καὶ ὀκτακόσια ἔτη καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας.
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

## Genesis 5:27

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέραι Μαθουσάλα, ἃς ἔζησεν, ἐννέα καὶ ἑξήκοντα καὶ ἐννακόσια ἔτη, καὶ ἀπέθανε.
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

## Genesis 5:28

Greek: Καὶ ἔζησε Λάμεχ ὀκτὼ καὶ ὀγδοήκοντα καὶ ἑκατὸν ἔτη καὶ ἐγέννησεν υἱόν.
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

## Genesis 5:29

Greek: καὶ ἐπωνόμασε τὸ ὄνομα αὐτοῦ Νῶε λέγων· οὗτος διαναπαύσει ἡμᾶς ἀπό τῶν ἔργων ἡμῶν καὶ ἀπὸ τῶν λυπῶν τῶν χειρῶν ἡμῶν καὶ ἀπὸ τῆς γῆς, ἧς κατηράσατο Κύριος ὁ Θεός.
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

## Genesis 5:30

Greek: καὶ ἔζησε Λάμεχ μετὰ τὸ γεννῆσαι αὐτὸν τὸν Νῶε πεντακόσια καὶ ἑξήκοντα καὶ πέντε ἔτη καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας.
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

## Genesis 5:31

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέραι Λάμεχ ἑπτακόσια καὶ πεντήκοντα τρία ἔτη, καὶ ἀπέθανε.
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

## Genesis 5:32

Greek: Καὶ ἦν Νῶε ἐτῶν πεντακοσίων καὶ ἐγέννησε τρεῖς υἱούς, τὸν Σήμ, τὸν Χάμ, καὶ τὸν ᾿Ιάφεθ.
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

# Chapter 6

## Genesis 6:1

Greek: ΚΑΙ ἐγένετο ἡνίκα ἤρξαντο οἱ ἄνθρωποι πολλοὶ γίνεσθαι ἐπὶ τῆς γῆς, καὶ θυγατέρες ἐγεννήθησαν αὐτοῖς.
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

## Genesis 6:2

Greek: ἰδόντες δὲ οἱ υἱοὶ τοῦ Θεοῦ τὰς θυγατέρας τῶν ἀνθρώπων ὅτι καλαί εἰσιν, ἔλαβον ἑαυτοῖς γυναῖκας ἀπὸ πασῶν, ὧν ἐξελέξαντο.
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

## Genesis 6:3

Greek: καὶ εἶπε Κύριος ὁ Θεός· οὐ μὴ καταμείνῃ τὸ πνεῦμά μου ἐν τοῖς ἀνθρώποις τούτοις εἰς τὸν αἰῶνα διὰ τὸ εἶναι αὐτοὺς σάρκας, ἔσονται δὲ αἱ ἡμέραι αὐτῶν ἑκατὸν εἴκοσιν ἔτη.
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

## Genesis 6:4

Greek: οἱ δὲ γίγαντες ἦσαν ἐπὶ τῆς γῆς ἐν ταῖς ἡμέραις ἐκείναις· καὶ μετ᾿ ἐκεῖνο, ὡς ἂν εἰσεπορεύοντο οἱ υἱοὶ τοῦ Θεοῦ πρὸς τὰς θυγατέρας τῶν ἀνθρώπων, καὶ ἐγεννῶσαν ἑαυτοῖς· ἐκεῖνοι ἦσαν οἱ γίγαντες οἱ ἀπ᾿ αἰῶνος, οἱ ἄνθρωποι οἱ ὀνομαστοί.
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

## Genesis 6:5

Greek: ᾿Ιδὼν δὲ Κύριος ὁ Θεός, ὅτι ἐπληθύνθησαν αἱ κακίαι τῶν ἀνθρώπων ἐπὶ τῆς γῆς καὶ πᾶς τις διανοεῖται ἐν τῇ καρδίᾳ αὐτοῦ ἐπιμελῶς ἐπὶ τὰ πονηρὰ πάσας τὰς ἡμέρας,
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

## Genesis 6:6

Greek: καὶ ἐνεθυμήθη ὁ Θεὸς ὅτι ἐποίησε τὸν ἄνθρωπον ἐπὶ τῆς γῆς, καὶ διενοήθη.
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

## Genesis 6:7

Greek: καὶ εἶπεν ὁ Θεός· ἀπαλείψω τὸν ἄνθρωπον, ὃν ἐποίησα ἀπὸ προσώπου τῆς γῆς, ἀπὸ ἀνθρώπου ἕως κτήνους καὶ ἀπό ἑρπετῶν ἕως πετεινῶν τοῦ οὐρανοῦ, ὅτι μετεμελήθην ὅτι ἐποίησα αὐτούς.
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

## Genesis 6:8

Greek: Νῶε δὲ εὗρε χάριν ἐναντίον Κυρίου τοῦ Θεοῦ.
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

## Genesis 6:9

Greek: Αὗται δὲ αἱ γενέσεις Νῶε· Νῶε ἄνθρωπος δίκαιος, τέλειος ὢν ἐν τῇ γενεᾷ αὐτοῦ· τῷ Θεῷ εὐηρέστησε Νῶε.
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

## Genesis 6:10

Greek: ἐγέννησε δὲ Νῶε τρεῖς υἱούς, τὸν Σήμ, τὸν Χάμ, τὸν ᾿Ιάφεθ.
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

## Genesis 6:11

Greek: ἐφθάρη δὲ ἡ γῆ ἐναντίον τοῦ Θεοῦ, καὶ ἐπλήσθη ἡ γῆ ἀδικίας.
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

## Genesis 6:12

Greek: καὶ εἶδε Κύριος ὁ Θεὸς τὴν γῆν, καὶ ἦν κατεφθαρμένη, ὅτι κατέφθειρε πᾶσα σὰρξ τὴν ὁδὸν αὐτοῦ ἐπὶ τῆς γῆς.
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

## Genesis 6:13

Greek: καὶ εἶπε Κύριος ὁ Θεὸς τῷ Νῶε· καιρὸς παντὸς ἀνθρώπου ἥκει ἐναντίον μου, ὅτι ἐπλήσθη ἡ γῆ ἀδικίας ἀπ᾿ αὐτῶν, καὶ ἰδοὺ ἐγὼ καταφθείρω αὐτοὺς καὶ τὴν γῆν.
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

## Genesis 6:14

Greek: ποίησον οὖν σεαυτῷ κιβωτὸν ἐκ ξύλων τετραγώνων· νοσσιὰς ποιήσεις τὴν κιβωτὸν καὶ ἀσφαλτώσεις αὐτὴν ἔσωθεν καὶ ἔξωθεν τῇ ἀσφάλτῳ.
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

## Genesis 6:15

Greek: καὶ οὕτω ποιήσεις τὴν κιβωτόν· τριακοσίων πήχεων τὸ μῆκος τῆς κιβωτοῦ καὶ πεντήκοντα πήχεων τὸ πλάτος καὶ τριάκοντα πήχεων τὸ ὕψος αὐτῆς·
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

## Genesis 6:16

Greek: ἐπισυνάγων ποιήσεις τὴν κιβωτὸν καὶ εἰς πῆχυν συντελέσεις αὐτὴν ἄνωθεν· τὴν δὲ θύραν τῆς κιβωτοῦ ποιήσεις ἐκ πλαγίων· κατάγαια διώροφα καὶ τριώροφα ποιήσεις αὐτήν.
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

## Genesis 6:17

Greek: ἐγὼ δὲ ἰδοὺ ἐπάγω τὸν κατακλυσμόν, ὕδωρ ἐπὶ τὴν γῆν καταφθεῖραι πᾶσαν σάρκα, ἐν ᾗ ἐστι πνεῦμα ζωῆς, ὑποκάτω τοῦ οὐρανοῦ· καὶ ὅσα ἐὰν ᾖ ἐπὶ τῆς γῆς, τελευτήσει.
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

## Genesis 6:18

Greek: καὶ στήσω τὴν διαθήκην μου μετὰ σοῦ· εἰσελεύσῃ δὲ εἰς τὴν κιβωτὸν σὺ καὶ οἱ υἱοί σου καὶ ἡ γυνή σου καὶ αἱ γυναῖκες τῶν υἱῶν σου μετὰ σοῦ.
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

## Genesis 6:19

Greek: καὶ ἀπὸ πάντων τῶν κτηνῶν καὶ ἀπὸ πάντων τῶν ἑρπετῶν καὶ ἀπὸ πάντων τῶν θηρίων καὶ ἀπὸ πάσης σαρκός, δύο δύο ἀπὸ πάντων εἰσάξεις εἰς τὴν κιβωτόν, ἵνα τρέφῃς μετὰ σεαυτοῦ· ἄρσεν καὶ θῆλυ ἔσονται.
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

## Genesis 6:20

Greek: ἀπὸ πάντων τῶν ὀρνέων τῶν πετεινῶν κατὰ γένος, καὶ ἀπὸ πάντων τῶν κτηνῶν κατὰ γένος καὶ ἀπὸ πάντων τῶν ἑρπετῶν τῶν ἑρπόντων ἐπὶ τῆς γῆς κατὰ γένος αὐτῶν, δύο δύο ἀπὸ πάντων εἰσελεύσονται πρὸς σὲ τρέφεσθαι μετὰ σοῦ, ἄρσεν καὶ θῆλυ.
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

## Genesis 6:21

Greek: σὺ δὲ λήψῃ σεαυτῷ ἀπὸ πάντων τῶν βρωμάτων, ἃ ἔδεσθε, καὶ συνάξεις πρὸς σεαυτόν, καὶ ἔσται σοι καὶ ἐκείνοις φαγεῖν.
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

## Genesis 6:22

Greek: καὶ ἐποίησε Νῶε πάντα, ὅσα ἐνετείλατο αὐτῷ Κύριος ὁ Θεός, οὕτως ἐποίησε.
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

# Chapter 7

## Genesis 7:1

Greek: ΚΑΙ εἶπε Κύριος ὁ Θεὸς πρὸς Νῶε· εἴσελθε σὺ καὶ πᾶς ὁ οἶκός σου εἰς τὴν κιβωτόν, ὅτι σὲ εἶδον δίκαιον ἐναντίον μου ἐν τῇ γενεᾷ ταύτῃ.
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

## Genesis 7:2

Greek: ἀπὸ δὲ τῶν κτηνῶν τῶν καθαρῶν εἰσάγαγε πρὸς σὲ ἑπτὰ ἑπτά, ἄρσεν καὶ θῆλυ, ἀπὸ δὲ τῶν κτηνῶν τῶν μὴ καθαρῶν δύο δύο, ἄρσεν καὶ θῆλυ,
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

## Genesis 7:3

Greek: καὶ ἀπὸ τῶν πετεινῶν τοῦ οὐρανοῦ τῶν καθαρῶν ἑπτὰ ἑπτά, ἄρσεν καὶ θῆλυ, καὶ ἀπὸ πάντων τῶν πετεινῶν τῶν μὴ καθαρῶν δύο δύο, ἄρσεν καὶ θῆλυ, διαθρέψαι σπέρμα ἐπί πᾶσαν τὴν γῆν.
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

## Genesis 7:4

Greek: ἔτι γὰρ ἡμερῶν ἑπτὰ ἐγὼ ἐπάγω ὑετὸν ἐπὶ τὴν γῆν τεσσαράκοντα ἡμέρας καὶ τεσσαράκοντα νύκτας καὶ ἐξαλείψω πᾶν τὸ ἀνάστημα, ὃ ἐποίησα, ἀπὸ προσώπου πάσης τῆς γῆς.
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

## Genesis 7:5

Greek: καὶ ἐποίησε Νῶε πάντα, ὅσα ἐνετείλατο αὐτῷ Κύριος ὁ Θεός.
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

## Genesis 7:6

Greek: Νῶε δὲ ἦν ἐτῶν ἑξακοσίων, καὶ ὁ κατακλυσμὸς τοῦ ὕδατος ἐγένετο ἐπὶ τῆς γῆς.
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

## Genesis 7:7

Greek: εἰσῆλθε δὲ Νῶε καὶ οἱ υἱοὶ αὐτοῦ καὶ ἡ γυνὴ αὐτοῦ καὶ αἱ γυναῖκες τῶν υἱῶν αὐτοῦ μετ᾿ αὐτοῦ εἰς τὴν κιβωτὸν διὰ τὸ ὕδωρ τοῦ κατατακλυσμοῦ.
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

## Genesis 7:8

Greek: καὶ ἀπὸ τῶν πετεινῶν τῶν καθαρῶν καὶ ἀπὸ τῶν πετεινῶν τῶν μὴ καθαρῶν καὶ ἀπὸ τῶν κτηνῶν τῶν καθαρῶν καὶ ἀπὸ τῶν κτηνῶν τῶν μὴ καθαρῶν καὶ ἀπὸ πάντων τῶν ἑρπόντων ἐπὶ τῆς γῆς
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

## Genesis 7:9

Greek: δύο δύο εἰσῆλθον πρὸς Νῶε εἰς τὴν κιβωτόν, ἄρσεν καὶ θῆλυ, καθὰ ἐνετείλατο ὁ Θεὸς τῷ Νῶε.
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

## Genesis 7:10

Greek: καὶ ἐγένετο μετὰ τὰς ἑπτὰ ἡμέρας καὶ τὸ ὕδωρ τοῦ κατακλυσμοῦ ἐγένετο ἐπὶ τῆς γῆς.
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

## Genesis 7:11

Greek: ἐν τῷ ἑξακοσιοστῷ ἔτει ἐν τῇ ζωῇ τοῦ Νῶε, τοῦ δευτέρου μηνός, ἑβδόμῃ καὶ εἰκάδι τοῦ μηνός, τῇ ἡμέρᾳ ταύτῃ ἐρράγησαν πᾶσαι αἱ πηγαὶ τῆς ἀβύσσου, καὶ οἱ καταρράκται τοῦ οὐρανοῦ ἠνεῴχθησαν.
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

## Genesis 7:12

Greek: καὶ ἐγένετο ὑετὸς ἐπὶ τῆς γῆς τεσσαράκοντα ἡμέρας καὶ τεσσαράκοντα νύκτας.
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

## Genesis 7:13

Greek: ἐν τῇ ἡμέρᾳ ταύτῃ εἰσῆλθε Νῶε, Σήμ, Χάμ, ᾿Ιάφεθ, οἱ υἱοὶ Νῶε, καὶ ἡ γυνὴ Νῶε καὶ αἱ τρεῖς γυναῖκες τῶν υἱῶν αὐτοῦ μετ᾿ αὐτοῦ εἰς τὴν κιβωτόν.
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

## Genesis 7:14

Greek: καὶ πάντα τὰ θηρία κατὰ γένος καὶ πάντα τὰ κτήνη κατὰ γένος καὶ πᾶν ἑρπετὸν κινούμενον ἐπὶ τῆς γῆς κατὰ γένος καὶ πᾶν ὄρνεον πετεινὸν κατὰ γένος αὐτοῦ
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

## Genesis 7:15

Greek: εἰσῆλθον πρὸς Νῶε εἰς τὴν κιβωτόν, δύο δύο ἄρσεν καὶ θῆλυ ἀπὸ πάσης σαρκός, ἐν ᾧ ἐστι πνεῦμα ζωῆς.
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

## Genesis 7:16

Greek: καὶ τὰ εἰσπορευόμενα ἄρσεν καὶ θῆλυ ἀπὸ πάσης σαρκὸς εἰσῆλθε, καθὰ ἐνετείλατο ὁ Θεὸς τῷ Νῶε. καὶ ἔκλεισε Κύριος ὁ Θεὸς τὴν κιβωτὸν ἔξωθεν αὐτοῦ.
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

## Genesis 7:17

Greek: Καὶ ἐγένετο ὁ κατακλυσμὸς τεσσαράκοντα ἡμέρας καὶ τεσσαράκοντα νύκτας ἐπὶ τῆς γῆς, καὶ ἐπεπληθύνθη τὸ ὕδωρ καὶ ἐπῆρε τὴν κιβωτόν, καὶ ὑψώθη ἀπὸ τῆς γῆς.
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

## Genesis 7:18

Greek: καὶ ἐπεκράτει τὸ ὕδωρ καὶ ἐπληθύνετο σφόδρα ἐπὶ τῆς γῆς, καί ἐπεφέρετο ἡ κιβωτὸς ἐπάνω τοῦ ὕδατος.
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

## Genesis 7:19

Greek: τὸ δὲ ὕδωρ ἐπεκράτει σφόδρα σφόδρα ἐπὶ τῆς γῆς καὶ ἐκάλυψε πάντα τὰ ὄρη τὰ ὑψηλά, ἃ ἦν ὑποκάτω τοῦ οὐρανοῦ·
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

## Genesis 7:20

Greek: πεντεκαίδεκα πήχεις ὑπεράνω ὑψώθη τὸ ὕδωρ καὶ ἐπεκάλυψε πάντα τὰ ὄρη τὰ ὑψηλά.
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

## Genesis 7:21

Greek: καὶ ἀπέθανε πᾶσα σὰρξ κινουμένη ἐπὶ τῆς γῆς τῶν πετεινῶν καὶ τῶν κτηνῶν καὶ ἀπὸ θηρίων καὶ πᾶν ἑρπετὸν κινούμενον ἐπὶ τῆς γῆς καὶ πᾶς ἄνθρωπος.
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

## Genesis 7:22

Greek: καὶ πάντα, ὅσα ἔχει πνοὴν ζωῆς, καὶ πᾶν, ὃ ἦν ἐπὶ τῆς ξηρᾶς, ἀπέθανε.
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

## Genesis 7:23

Greek: καὶ ἐξήλειψε πᾶν τὸ ἀνάστημα, ὃ ἦν ἐπί προσώπου τῆς γῆς, ἀπὸ ἀνθρώπου ἕως κτήνους καὶ ἑρπετῶν καὶ τῶν πετεινῶν τοῦ οὐρανοῦ, καὶ ἐξηλείφθησαν ἀπὸ τῆς γῆς· καὶ κατελείφθη μόνος Νῶε καὶ οἱ μετ᾿ αὐτοῦ ἐν τῇ κιβωτῷ.
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

## Genesis 7:24

Greek: καὶ ὑψώθη τὸ ὕδωρ ἐπὶ τῆς γῆς ἡμέρας ἑκατὸν πεντήκοντα.
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

# Chapter 8

## Genesis 8:1

Greek: ΚΑΙ ἀνεμνήσθη ὁ Θεὸς τοῦ Νῶε καὶ πάντων τῶν θηρίων καὶ πάντων τῶν κτηνῶν καὶ πάντων τῶν πετεινῶν καὶ πάντων τῶν ἑρπετῶν τῶν ἑρπόντων, ὅσα ἦν μετ᾿ αὐτοῦ ἐν τῇ κιβωτῷ, καὶ ἐπήγαγεν ὁ Θεὸς πνεῦμα ἐπὶ τὴν γῆν, καὶ ἐκόπασε τὸ ὕδωρ,
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

## Genesis 8:2

Greek: καὶ ἐπεκαλύφθησαν αἱ πηγαὶ τῆς ἀβύσσου καὶ οἱ καταρράκται τοῦ οὐρανοῦ, καὶ συνεσχέθη ὁ ὑετὸς ἀπὸ τοῦ οὐρανοῦ.
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

## Genesis 8:3

Greek: καὶ ἐνεδίδου τὸ ὕδωρ πορευόμενον ἀπὸ τῆς γῆς, καὶ ἠλαττονοῦτο τὸ ὕδωρ μετὰ πεντήκοντα καὶ ἑκατὸν ἡμέρας.
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

## Genesis 8:4

Greek: καὶ ἐκάθισεν ἡ κιβωτὸς ἐν μηνὶ τῷ ἑβδόμῳ, ἑβδόμῃ καὶ εἰκάδι τοῦ μηνός, ἐπὶ τὰ ὄρη τὰ ᾿Αραράτ.
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

## Genesis 8:5

Greek: τὸ δὲ ὕδωρ ἠλαττονοῦτο ἕως τοῦ δεκάτου μηνός· καὶ ἐν τῷ δεκάτῳ μηνί, τῇ πρώτῃ τοῦ μηνός, ὤφθησαν αἱ κεφαλαὶ τῶν ὀρέων.
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

## Genesis 8:6

Greek: καὶ ἐγένετο μετὰ τεσσαράκοντα ἡμέρας ἠνέῳξε Νῶε τὴν θυρίδα τῆς κιβωτοῦ, ἣν ἐποίησε, καὶ ἀπέστειλε τὸν κόρακα τοῦ ἰδεῖν, εἰ κεκόπακε τὸ ὕδωρ·
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

## Genesis 8:7

Greek: καὶ ἐξελθών, οὐκ ἀνέστρεψεν ἕως τοῦ ξηρανθῆναι τὸ ὕδωρ ἀπὸ τῆς γῆς.
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

## Genesis 8:8

Greek: καὶ ἀπέστειλε τὴν περιστερὰν ὀπίσω αὐτοῦ ἰδεῖν, εἰ κεκόπακε τὸ ὕδωρ ἀπὸ τῆς γῆς.
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

## Genesis 8:9

Greek: καὶ οὐχ εὑροῦσαι ἡ περιστερὰ ἀνάπαυσιν τοῖς ποσὶν αὐτῆς, ἀνέστρεψε πρὸς αὐτὸν εἰς τὴν κιβωτόν, ὅτι ὕδωρ ἦν ἐπὶ πᾶν τὸ πρόσωπον τῆς γῆς, καὶ ἐκτείνας τὴν χεῖρα ἔλαβεν αὐτήν, καὶ εἰσήγαγεν αὐτὴν πρὸς ἑαυτὸν εἰς τὴν κιβωτόν.
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

## Genesis 8:10

Greek: καὶ ἐπισχὼν ἔτι ἡμέρας ἑπτὰ ἑτέρας, πάλιν ἐξαπέστειλε τὴν περιστερὰν ἐκ τῆς κιβωτοῦ·
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

## Genesis 8:11

Greek: καὶ ἀνέστρεψε πρὸς αὐτὸν ἡ περιστερὰ τὸ πρὸς ἑσπέραν, καὶ εἶχε φύλλον ἐλαίας κάρφος ἐν τῷ στόματι αὐτῆς, καὶ ἔγνω Νῶε ὅτι κεκόπακε τὸ ὕδωρ ἀπὸ τῆς γῆς.
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

## Genesis 8:12

Greek: καὶ ἐπισχὼν ἔτι ἡμέρας ἑπτὰ ἑτέρας, πάλιν ἐξαπέστειλε τὴν περιστεράν, καὶ οὑ προσέθετο τοῦ ἐπιστρέψαι πρὸς αὐτὸν ἔτι.
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

## Genesis 8:13

Greek: καὶ ἐγένετο ἐν τῷ ἑνὶ καὶ ἑξακοσιοστῷ ἔτει ἐν τῇ ζωῇ τοῦ Νῶε, τοῦ πρώτου μηνός, μιᾷ τοῦ μηνός, ἐξέλιπε τὸ ὕδωρ ἀπὸ τῆς γῆς· καὶ ἀπεκάλυψε Νῶε τὴν στέγην τῆς κιβωτοῦ, ἣν ἐποίησε, καὶ εἶδεν ὅτι ἐξέλιπε τὸ ὕδωρ ἀπὸ προσώπου τῆς γῆς.
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

## Genesis 8:14

Greek: ἐν δὲ τῷ δευτέρῳ μηνὶ ἐξηράνθη ἡ γῆ, ἑβδόμῃ καὶ εἰκάδι τοῦ μηνός.
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

## Genesis 8:15

Greek: Καὶ εἶπε Κύριος ὁ Θεὸς πρὸς Νῶε λέγων·
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

## Genesis 8:16

Greek: ἔξελθε ἐκ τῆς κιβωτοῦ, σὺ καὶ ἡ γυνή σου καὶ οἱ υἱοί σου καὶ αἱ γυναῖκες τῶν υἱῶν σου μετὰ σοῦ
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

## Genesis 8:17

Greek: καὶ πάντα τὰ θηρία, ὅσα ἐστὶ μετὰ σοῦ, καὶ πᾶσα σὰρξ ἀπὸ πετεινῶν ἕως κτηνῶν, καὶ πᾶν ἑρπετὸν κινούμενον ἐπὶ τῆς γῆς ἐξάγαγε μετὰ σεαυτοῦ· καὶ αὐξάνεσθε καὶ πληθύνεσθε ἐπὶ τῆς γῆς.
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

## Genesis 8:18

Greek: καὶ ἐξῆλθε Νῶε καὶ ἡ γυνὴ αὐτοῦ καὶ οἱ υἱοὶ αὐτοῦ καὶ αἱ γυναῖκες τῶν υἱῶν αὐτοῦ μετ᾿ αὐτοῦ.
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

## Genesis 8:19

Greek: καὶ πάντα τὰ θηρία, καὶ πάντα τὰ κτήνη, καὶ πᾶν πετεινόν, καὶ πᾶν ἑρπετὸν κινούμενον ἐπὶ τῆς γῆς κατὰ γένος αὐτῶν, ἐξήλθοσαν ἐκ τῆς κιβωτοῦ.
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

## Genesis 8:20

Greek: καὶ ᾠκοδόμησε Νῶε θυσιαστήριον τῷ Κυρίῳ, καὶ ἔλαβεν ἀπὸ πάντων τῶν κτηνῶν τῶν καθαρῶν καὶ ἀπὸ πάντων τῶν πετεινῶν τῶν καθαρῶν καὶ ἀνήνεγκεν εἰς ὁλοκάρπωσιν ἐπὶ τὸ θυσιαστήριον.
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

## Genesis 8:21

Greek: καὶ ὠσφράνθη Κύριος ὁ Θεὸς ὀσμὴν εὐωδίας, καὶ εἶπε Κύριος ὁ Θεὸς διανοηθείς· οὐ προσθήτω ἔτι καταράσασθαι τὴν γῆν διὰ τὰ ἔργα τῶν ἀνθρώπων, ὅτι ἔγκειται ἡ διάνοια τοῦ ἀνθρώπου ἐπιμελῶς ἐπὶ τὰ πονηρὰ ἐκ νεότητος αὐτοῦ· οὐ προσθήσω οὖν ἔτι πατάξαι πᾶσαν σάρκα ζῶσαν, καθὼς ἐποίησα.
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

## Genesis 8:22

Greek: πάσας τὰς ἡμέρας τῆς γῆς, σπέρμα καὶ θερισμός, ψῦχος καὶ καῦμα, θέρος καὶ ἔαρ, ἡμέραν καὶ νύκτα οὐ καταπαύσουσι.
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

# Chapter 9

## Genesis 9:1

Greek: ΚΑΙ εὐλόγησεν ὁ Θεὸς τὸν Νῶε καὶ τοὺς υἱοὺς αὐτοῦ καὶ εἶπεν αὐτοῖς· αὐξάνεσθε καὶ πληθύνεσθε καὶ πληρώσατε τὴν γῆν καὶ κατακυριεύσατε αὐτῆς.
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

## Genesis 9:2

Greek: καὶ ὁ τρόμος καὶ ὁ φόβος ὑμῶν ἔσται ἐπὶ πᾶσι τοῖς θηρίοις τῆς γῆς, ἐπὶ πάντα τὰ πετεινὰ τοῦ οὐρανοῦ καὶ ἐπὶ πάντα τὰ κινούμενα ἐπὶ τῆς γῆς καὶ ἐπὶ πάντας τοὺς ἰχθύας τῆς θαλάσσης· ὑπὸ χεῖρας ὑμῖν δέδωκα.
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

## Genesis 9:3

Greek: καὶ πᾶν ἑρπετόν, ὅ ἐστι ζῶν, ὑμῖν ἔσται εἰς βρῶσιν· ὡς λάχανα χόρτου δέδωκα ὑμῖν τὰ πάντα.
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

## Genesis 9:4

Greek: πλὴν κρέας ἐν αἵματι ψυχῆς οὐ φάγεσθε·
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

## Genesis 9:5

Greek: καὶ γὰρ τὸ ὑμέτερον αἷμα τῶν ψυχῶν ὑμῶν ἐκ χειρὸς πάντων τῶν θηρίων ἐκζητήσω αὐτὸ καὶ ἐκ χειρὸς ἀνθρώπου ἀδελφοῦ ἐκζητήσω τὴν ψυχὴν τοῦ ἀνθρώπου.
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

## Genesis 9:6

Greek: ὁ ἐκχέων αἷμα ἀνθρώπου, ἀντὶ τοῦ αἵματος αὐτοῦ ἐκχυθήσεται, ὅτι ἐν εἰκόνι Θεοῦ ἐποίησα τὸν ἄνθρωπον.
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

## Genesis 9:7

Greek: ὑμεῖς δὲ αὐξάνεσθε καὶ πληθύνεσθε καὶ πληρώσατε τὴν γῆν, καὶ κατακυριεύσατε αὐτῆς.
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

## Genesis 9:8

Greek: Καὶ εἶπεν ὁ Θεός τῷ Νῷε καὶ τοῖς υἱοῖς αὐτοῦ μετ᾿ αὐτοῦ λέγων·
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

## Genesis 9:9

Greek: καὶ ἰδοὺ ἐγὼ ἀνίστημι τὴν διαθήκην μου ὑμῖν καὶ τῷ σπέρματι ὑμῶν μεθ᾿ ὑμᾶς
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

## Genesis 9:10

Greek: καὶ πάσῃ ψυχῇ ζώσῃ μεθ᾿ ὑμῶν, ἀπὸ ὀρνέων καὶ ἀπὸ κτηνῶν, καὶ πᾶσι τοῖς θηρίοις τῆς γῆς, ὅσα ἐστὶ μεθ᾿ ὑμῶν ἀπὸ πάντων τῶν ἐξελθόντων ἐκ τῆς κιβωτοῦ.
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

## Genesis 9:11

Greek: καὶ στήσω τὴν διαθήκην μου πρὸς ὑμᾶς, καὶ οὐκ ἀποθανεῖται πᾶσα σὰρξ ἔτι ἀπὸ τοῦ ὕδατος τοῦ κατακλυσμοῦ, καὶ οὐκ ἔτι ἔσται κατακλυσμὸς ὕδατος τοῦ καταφθεῖραι πᾶσαν τὴν γῆν.
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

## Genesis 9:12

Greek: καὶ εἶπε Κύριος ὁ Θεὸς πρὸς Νῶε· τοῦτο τὸ σημεῖον τῆς διαθήκης, ὃ ἐγὼ δίδωμι ἀνὰ μέσον ἐμοῦ καὶ ὑμῶν καὶ ἀνὰ μέσον πάσης ψυχῆς ζώσης, ἥ ἐστι μεθ᾿ ὑμῶν εἰς γενεὰς αἰωνίους·
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

## Genesis 9:13

Greek: τὸ τόξον μου τίθημι ἐν τῇ νεφέλῃ, καὶ ἔσται εἰς σημεῖον διαθήκης ἀνὰ μέσον ἐμοῦ καὶ τῆς γῆς.
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

## Genesis 9:14

Greek: καὶ ἔσται ἐν τῷ συννεφεῖν με νεφέλας ἐπὶ τὴν γῆν, ὀφθήσεται τὸ τόξον ἐν τῇ νεφέλῃ,
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

## Genesis 9:15

Greek: καὶ μνησθήσομαι τῆς διαθήκης μου, ἥ ἐστιν ἀνὰ μέσον ἐμοῦ καὶ ὑμῶν, καὶ ἀνὰ μέσον πάσης ψυχῆς ζώσης ἐν πάσῃ σαρκί, καὶ οὐκ ἔσται ἔτι τὸ ὕδωρ εἰς κατακλυσμόν, ὥστε ἐξαλεῖψαι πᾶσαν σάρκα.
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

## Genesis 9:16

Greek: καὶ ἔσται τὸ τόξον μου ἐν τῇ νεφέλῃ, καὶ ὄψομαι τοῦ μνησθῆναι διαθήκην αἰώνιον ἀνὰ μέσον ἐμοῦ καὶ τῆς γῆς καὶ ἀνὰ μέσον ψυχῆς ζώσης ἐν πᾶσι σαρκί, ἥ ἐστιν ἐπὶ τῆς γῆς.
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

## Genesis 9:17

Greek: καὶ εἶπεν ὁ Θεὸς τῷ Νῶε· τοῦτο τὸ σημεῖον τῆς διαθήκης, ἧς διεθέμην ἀνὰ μέσον ἐμοῦ καὶ ἀνὰ μέσον πάσης σαρκός, ἥ ἐστιν ἐπὶ τῆς γῆς.
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

## Genesis 9:18

Greek: ῏Ησαν δὲ οἱ υἱοὶ Νῶε, οἱ ἐξελθόντες ἐκ τῆς κιβωτοῦ, Σήμ, Χάμ, ᾿Ιάφεθ· Χάμ δὲ ἦν πατὴρ Χαναάν.
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

## Genesis 9:19

Greek: τρεῖς οὗτοί εἰσιν υἱοὶ Νῶε· ἀπὸ τούτων διεσπάρησαν ἐπί πᾶσαν τὴν γῆν.
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

## Genesis 9:20

Greek: Καὶ ἤρξατο Νῶε ἄνθρωπος γεωργὸς γῆς καὶ ἐφύτευσεν ἀμπελῶνα.
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

## Genesis 9:21

Greek: καὶ ἔπιεν ἐκ τοῦ οἴνου καὶ ἐμεθύσθη καὶ ἐγυμνώθη ἐν τῷ οἴκῳ αὐτοῦ.
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

## Genesis 9:22

Greek: καὶ εἶδε Χὰμ ὁ πατὴρ Χαναὰν τὴν γύμνωσιν τοῦ πατρὸς αὐτοῦ καὶ ἐξελθὼν ἀνήγγειλε τοῖς δυσὶν ἀδελφοῖς αὐτοῦ ἔξω.
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

## Genesis 9:23

Greek: καὶ λαβόντες Σὴμ καὶ ᾿Ιάφεθ τὸ ἱμάτιον ἐπέθεντο ἐπὶ τὰ δύο νῶτα αὐτῶν καὶ ἐπορεύθησαν ὀπισθοφανῶς καὶ συνεκάλυψαν τὴν γύμνωσιν τοῦ πατρὸς αὐτῶν, καὶ τὸ πρόσωπον αὐτῶν ὀπισθοφανῶς, καὶ τὴν γύμνωσιν τοῦ πατρὸς αὐτῶν οὐκ εἶδον.
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

## Genesis 9:24

Greek: ἐξένηψε δὲ Νῶε ἀπὸ τοῦ οἴνου καὶ ἔγνω ὅσα ἐποίησεν αὐτῷ ὁ υἱὸς αὐτοῦ ὁ νεώτερος,
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

## Genesis 9:25

Greek: καὶ εἶπεν· ἐπικατάρατος Χαναάν· παῖς οἰκέτης ἔσται τοῖς ἀδελφοῖς αὐτοῦ.
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

## Genesis 9:26

Greek: καὶ εἶπεν· εὐλογητὸς Κύριος ὁ Θεὸς τοῦ Σήμ, καὶ ἔσται Χαναὰν παῖς οἰκέτης αὐτοῦ.
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

## Genesis 9:27

Greek: πλατύναι ὁ Θεὸς τῷ ᾿Ιάφεθ, καὶ κατοικησάτω ἐν τοῖς οἴκοις τοῦ Σὴμ καὶ γενηθήτω Χαναὰν παῖς αὐτοῦ.
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

## Genesis 9:28

Greek: ῎Εζησε δὲ Νῶε μετὰ τὸν κατακλυσμὸν ἔτη τριακόσια πεντήκοντα.
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

## Genesis 9:29

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέραι Νῶε ἐννακόσια πεντήκοντα ἔτη, καὶ ἀπέθανεν.
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

# Chapter 10

## Genesis 10:1

Greek: ΑΥΤΑΙ δὲ αἱ γενέσεις τῶν υἱῶν Νῶε, Σήμ, Χάμ, ᾿Ιάφεθ, καὶ ἐγεννήθησαν αὐτοῖς υἱοὶ μετὰ τὸν κατακλυσμόν.
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

## Genesis 10:2

Greek: Υἱοὶ ᾿Ιάφεθ· Γαμὲρ καὶ Μαγὼγ καὶ Μαδοὶ καὶ ᾿Ιωύαν καὶ ᾿Ελισὰ καὶ Θοβὲλ καὶ Μοσόχ καὶ Θείρας.
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

## Genesis 10:3

Greek: καὶ υἱοὶ Γαμέρ· ᾿Ασχανὰζ καὶ Ριφὰθ καὶ Θοργαμά.
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

## Genesis 10:4

Greek: καὶ υἱοὶ ᾿Ιωύαν· ᾿Ελισὰ καὶ Θάρσεις, Κίτιοι, Ρόδιοι.
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

## Genesis 10:5

Greek: ἐκ τούτων ἀφωρίσθησαν νῆσοι τῶν ἐθνῶν ἐν τῇ γῇ αὐτῶν, ἕκαστος κατὰ γλῶσσαν ἐν ταῖς φυλαῖς αὐτῶν καὶ ἐν τοῖς ἔθνεσιν αὐτῶν.
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

## Genesis 10:6

Greek: Υἱοὶ δὲ Χάμ· Χοὺς καὶ Μερσαΐν Φοὺδ καὶ Χαναάν.
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

## Genesis 10:7

Greek: υἱοὶ δὲ Χούς· Σαβὰ καὶ Εὐϊλὰ καὶ Σαβαθὰ καὶ Ρεγμὰ καὶ Σαβαθακά. υἱοὶ δὲ Ρεγμά· Σαβὰ καὶ Δαδάν.
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

## Genesis 10:8

Greek: Χοὺς δὲ ἐγέννησε τὸν Νεβρώδ. οὗτος ἤρξατο εἶναι γίγας ἐπὶ τῆς γῆς·
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

## Genesis 10:9

Greek: οὗτος ἦν γίγας κυνηγὸς ἐναντίον Κυρίου τοῦ Θεοῦ· διὰ τοῦτο ἐροῦσιν, ὡς Νεβρὼδ γίγας κυνηγὸς ἐναντίον Κυρίου.
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

## Genesis 10:10

Greek: καὶ ἐγένετο ἀρχὴ τῆς βασιλείας αὐτοῦ Βαβυλὼν καὶ ᾿Ορὲχ καὶ ᾿Αρχὰδ καὶ Χαλάννη ἐν τῇ γῇ Σεναάρ.
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

## Genesis 10:11

Greek: ἐκ τῆς γῆς ἐκείνης ἐξῆλθεν ᾿Ασσοὺρ καὶ ᾠκοδόμησε τὴν Νινευΐ καὶ τὴν Ροωβὼθ πόλιν καὶ τὴν Χαλὰχ
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

## Genesis 10:12

Greek: καὶ τὴν Δασὴ ἀνὰ μέσον Νινευΐ καὶ ἀνὰ μέσο Χαλάχ· αὕτη ἡ πόλις μεγάλη.
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

## Genesis 10:13

Greek: καὶ Μεσραΐν ἐγέννησε τοὺς Λουδιεὶμ καὶ τοὺς ᾿Ενεμετιεὶμ καὶ τοὺς Λαβιεὶμ καὶ τοὺς Νεφθαλιεὶμ καὶ τοὺς Πατροσωνιεὶμ
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

## Genesis 10:14

Greek: καὶ τοὺς Χασλωνιείμ, ὅθεν ἐξῆλθε Φυλιστιείμ, καὶ τοὺς Καφθοριείμ.
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

## Genesis 10:15

Greek: Χαναὰν δὲ ἐγέννησε τὸν Σιδῶνα πρωτότοκον αὐτοῦ
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

## Genesis 10:16

Greek: καὶ τὸν Χετταῖον καὶ τὸν ᾿Ιεβουσαῖον καὶ τὸν ᾿Αμορραῖον καὶ τὸν Γεργεσαῖον καὶ τὸν Εὐαῖον καὶ τὸν ᾿Αρουκαῖον
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

## Genesis 10:17

Greek: καὶ τὸν ᾿Ασενναῖον καὶ τὸν ᾿Αράδιον καὶ τὸν Σαμαραῖον καὶ τὸν ᾿Αμαθί.
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

## Genesis 10:18

Greek: καὶ μετὰ τοῦτο διεσπάρησαν αἱ φυλαὶ τῶν Χαναναίων,
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

## Genesis 10:19

Greek: καὶ ἐγένετο τὰ ὅραι τῶν Χαναναίων ἀπὸ Σιδῶνος ἕως ἐλθεῖν εἰς Γεραρὰ καὶ Γαζάν, ἕως ἐλθεῖν ἕως Σοδόμων καὶ Γομόρρας, ᾿Αδαμὰ καὶ Σεβωΐμ ἕως Δασά.
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

## Genesis 10:20

Greek: οὗτοι υἱοὶ Χάμ, ἐν ταῖς φυλαῖς αὐτῶν, κατὰ γλώσσας αὐτῶν, ἐν ταῖς χώραις αὐτῶν καὶ ἐν τοῖς ἔθνεσιν αὐτῶν.
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

## Genesis 10:21

Greek: Καὶ τῷ Σὴμ ἐγεννήθη καὶ αὐτῷ, πατρὶ πάντων τῶν υἱῶν ῞Εβερ, ἀδελφῷ ᾿Ιάφεθ τοῦ μείζονος.
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

## Genesis 10:22

Greek: υἱοὶ Σήμ· ᾿Ελὰμ καὶ ᾿Ασσοὺρ καὶ ᾿Αρφαξὰδ καὶ Λοὺδ καὶ ᾿Αρὰμ καὶ Καϊνᾶν.
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

## Genesis 10:23

Greek: καὶ υἱοὶ ᾿Αράμ· Οὒζ καί Οὒλ καὶ Γατὲρ καὶ Μοσόχ.
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

## Genesis 10:24

Greek: καὶ ᾿Αρφαξὰδ ἐγέννησε τὸν Καϊνᾶν, καὶ Καϊνᾶν ἐγέννησε τὸν Σαλά, Σαλὰ δὲ ἐγέννησε τὸν ῞Εβερ.
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

## Genesis 10:25

Greek: καὶ τῷ ῞Εβερ ἐγεννήθησαν δύο υἱοί· ὄνομα τῷ ἑνὶ Φαλέγ, ὅτι ἐν ταῖς ἡμέραις αὐτοῦ διεμερίσθη ἡ γῆ, καὶ ὄνομα τῷ ἀδελφῷ αὐτοῦ ᾿Ιεκτάν.
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

## Genesis 10:26

Greek: ᾿Ιεκτὰν δὲ ἐγέννησε τὸν ᾿Ελμωδὰδ καὶ Σαλὲθ καὶ τὸν Σαρμὼθ καὶ ᾿Ιαρὰχ καὶ ῾Οδορρὰ καὶ Αἰβὴλ καὶ Δεκλὰ
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

## Genesis 10:27

Greek: καὶ Εὐὰλ καὶ ᾿Αβιμαὲλ καὶ Σαβὰ
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

## Genesis 10:28

Greek: καὶ Οὐφεὶρ καὶ Εὐειλὰ καὶ ᾿Ιωβάβ.
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

## Genesis 10:29

Greek: πάντες οὗτοι υἱοὶ ᾿Ιεκτάν.
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

## Genesis 10:30

Greek: καὶ ἐγένετο ἡ κατοίκησις αὐτῶν ἀπὸ Μασσῆ ἕως ἐλθεῖν εἰς Σαφηρά, ὄρος ἀνατολῶν.
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

## Genesis 10:31

Greek: οὗτοι υἱοὶ Σήμ, ἐν ταῖς φυλαῖς αὐτῶν, κατὰ γλώσσας αὐτῶν, ἐν ταῖς χώραις αὐτῶν καὶ ἐν τοῖς ἔθνεσιν αὐτῶν.
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

## Genesis 10:32

Greek: Αὗται αἱ φυλαὶ υἱῶν Νῶε κατὰ γενέσεις αὐτῶν, κατὰ ἔθνη αὐτῶν· ἀπὸ τούτων διεσπάρησαν νῆσοι τῶν ἐθνῶν ἐπὶ τῆς γῆς μετὰ τὸν κατακλυσμόν.
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

# Chapter 11

## Genesis 11:1

Greek: ΚΑΙ ἦν πᾶσα ἡ γῆ χεῖλος ἕν, καὶ φωνὴ μία πᾶσι.
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

## Genesis 11:2

Greek: καὶ ἐγένετο ἐν τῷ κινῆσαι αὐτοὺς ἀπὸ ἀνατολῶν, εὗρον πεδίον ἐν γῇ Σενναὰρ καὶ κατῴκησαν ἐκεῖ.
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

## Genesis 11:3

Greek: καὶ εἶπεν ἄνθρωπος τῷ πλησίον αὐτοῦ· δεῦτε πλινθεύσωμεν πλίνθους καὶ ὀπτήσωμεν αὐτὰς πυρί. καὶ ἐγένετο αὐτοῖς ἡ πλίνθος εἰς λίθον, καὶ ἄσφαλτος ἦν αὐτοῖς ὁ πηλός.
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

## Genesis 11:4

Greek: καὶ εἶπαν· δεῦτε οἰκοδομήσωμεν ἑαυτοῖς πόλιν καὶ πύργον, οὗ ἔσται ἡ κεφαλὴ ἕως τοῦ οὐρανοῦ, καὶ ποιήσωμεν ἑαυτοῖς ὄνομα πρὸ τοῦ διασπαρῆναι ἡμᾶς ἐπὶ προσώπου πάσης τῆς γῆς.
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

## Genesis 11:5

Greek: καὶ κατέβη Κύριος ἰδεῖν τὴν πόλιν καὶ τὸν πύργον, ὃν ᾠκοδόμησαν οἱ υἱοὶ τῶν ἀνθρώπων.
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

## Genesis 11:6

Greek: καὶ εἶπε Κύριος· ἰδοὺ γένος ἓν καὶ χεῖλος ἓν πάντων, καὶ τοῦτο ἤρξαντο ποιῆσαι, καὶ νῦν οὐκ ἐκλείψει ἀπ᾿ αὐτῶν πάντα, ὅσα ἂν ἐπιθῶνται ποιεῖν.
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

## Genesis 11:7

Greek: δεῦτε καὶ καταβάντες συγχέωμεν αὐτῶν ἐκεῖ τὴν γλῶσσαν, ἵνα μὴ ἀκούσωσιν ἕκαστος τὴν φωνὴν τοῦ πλησίον.
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

## Genesis 11:8

Greek: καὶ διέσπειρεν αὐτοὺς Κύριος ἐκεῖθεν ἐπὶ πρόσωπον πάσης τῆς γῆς, καὶ ἐπαύσαντο οἰκοδομοῦντες τὴν πόλιν καὶ τὸν πύργον.
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

## Genesis 11:9

Greek: διὰ τοῦτο ἐκλήθη τὸ ὄνομα αὐτῆς Σύγχυσις, ὅτι ἐκεῖ συνέχεε Κύριος τὰ χείλη πάσης τῆς γῆς, καὶ ἐκεῖθεν διέσπειρεν αὐτοὺς Κύριος ἐπὶ πρόσωπον πάσης τῆς γῆς.
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

## Genesis 11:10

Greek: Καὶ αὗται αἱ γενέσεις Σήμ. καί ἦν Σὴμ υἱὸς ἑκατὸν ἐτῶν, ὅτε ἐγέννησε τὸν ᾿Αρφαξάδ, δευτέρου ἔτους μετὰ τὸν κατακλυσμόν.
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

## Genesis 11:11

Greek: καὶ ἔζησε Σὴμ μετὰ τὸ γεννῆσαι αὐτὸν τὸν ᾿Αρφαξὰδ ἔτη πεντακόσια καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας καὶ ἀπέθανε.
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

## Genesis 11:12

Greek: Καὶ ἔζησεν ᾿Αρφαξὰδ ἑκατὸν τριάκοντα πέντε ἔτη καὶ ἐγέννησε τὸν Καϊνᾶν.
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

## Genesis 11:13

Greek: καὶ ἔζησεν ᾿Αρφαξὰδ μετὰ τὸ γεννῆσαι αὐτὸν τὸν Καϊνᾶν ἔτη τετρακόσια καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας καὶ ἀπέθανε. Καὶ ἔζησε Καϊνᾶν ἑκατὸν καὶ τριάκοντα ἔτη καὶ ἐγέννησε τὸν Σαλά. καὶ ἔζησε Καϊνᾶν μετὰ τὸ γεννῆσαι αὐτὸν τόν Σαλὰ ἔτη τριακόσια τριάκοντα καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας καὶ ἀπέθανε.
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

## Genesis 11:14

Greek: Καὶ ἔζησε Σαλὰ ἑκατὸν τριάκοντα ἔτη καὶ ἐγέννησε τὸν ῞Εβερ.
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

## Genesis 11:15

Greek: καὶ ἔζησε Σαλὰ μετὰ τὸ γεννῆσαι αὐτὸν τὸν ῞Εβερ τριακόσια τριάκοντα ἔτη καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας καὶ ἀπέθανε.
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

## Genesis 11:16

Greek: Καὶ ἔζησεν ῞Εβερ ἑκατὸν τριάκοντα τέσσαρα ετη καὶ ἐγέννησε τὸν Φαλέγ.
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

## Genesis 11:17

Greek: καί ἔζησεν ῞Εβερ μετὰ τὸ γεννῆσαι αὐτὸν τὸν Φαλὲγ ἔτη διακόσια ἑβδομήκοντα καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας καὶ ἀπέθανε.
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

## Genesis 11:18

Greek: Καὶ ἔζησε Φαλὲγ τριάκοντα καὶ ἑκατὸν ἔτη καὶ ἐγέννησε τὸν Ραγαῦ.
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

## Genesis 11:19

Greek: καὶ ἔζησε Φαλὲγ μετὰ τὸ γεννῆσαι αὐτὸν τὸν Ραγαῦ ἐννέα καὶ διακόσια ἔτη καὶ ἐγέννησεν υἱούς καὶ θυγατέρας καὶ ἀπέθανε.
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

## Genesis 11:20

Greek: Καὶ ἔζησε Ραγαῦ ἑκατὸν τριάκοντα καὶ δύο ἔτη καὶ ἐγέννησε τὸν Σερούχ.
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

## Genesis 11:21

Greek: καὶ ἔζησε Ραγαῦ μετὰ τὸ γεννῆσαι αὐτὸν τὸν Σεροὺχ διακόσια ἑπτὰ ἔτη καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας καὶ ἀπέθανε.
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

## Genesis 11:22

Greek: καὶ ἔζησε Σεροὺχ ἑκατὸν τριάκοντα ἔτη καὶ ἐγέννησε τὸν Ναχώρ.
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

## Genesis 11:23

Greek: Καὶ ἔζησε Σερούχ, μετὰ τό γεννῆσαι αὐτὸν τὸν Ναχώρ, ἔτη διακόσια καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας καὶ ἀπέθανε.
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

## Genesis 11:24

Greek: Καὶ ἔζησε Ναχὼρ ἔτη ἑκατὸν ἑβδομήκοντα ἐννέα καὶ ἐγέννησε τὸν Θάρα.
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

## Genesis 11:25

Greek: καὶ ἔζησε Ναχώρ, μετὰ τὸ γεννῆσαι αὐτὸν τὸν Θάρα, ἔτη ἑκατὸν εἰκοσιπέντε καὶ ἐγέννησεν υἱοὺς καὶ θυγατέρας καὶ ἀπέθανε.
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

## Genesis 11:26

Greek: Καὶ ἔζησε Θάρα ἑβδομήκοντα ἔτη καὶ ἐγέννησε τὸν ῞Αβραμ καὶ τὸν Ναχὼρ καὶ τὸν ᾿Αρράν.
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

## Genesis 11:27

Greek: Αὗται αἱ γενέσεις Θάρα· Θάρα ἐγέννησε τὸν ῞Αβραμ καὶ τὸν Ναχὼρ καὶ τὸν ᾿Αρράν, καὶ ᾿Αρρὰν ἐγέννησε τὸν Λώτ.
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

## Genesis 11:28

Greek: καὶ ἀπέθανεν ᾿Αρρὰν ἐνώπιον Θάρα τοῦ πατρὸς αὐτοῦ ἐν τῇ γῇ, ᾗ ἐγεννήθη, ἐν τῇ χώρᾳ τῶν Χαλδαίων.
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

## Genesis 11:29

Greek: καὶ ἔλαβον ῞Αβραμ καὶ Ναχὼρ ἑαυτοῖς γυναῖκας· ὄνομα τῇ γυναικὶ ῞Αβραμ Σάρα, καὶ ὄνομα τῇ γυναικὶ Ναχὼρ Μελχά, θυγάτηρ ᾿Αρρὰν καὶ πατὴρ Μελχὰ καὶ πατὴρ ᾿Ιεσχά.
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

## Genesis 11:30

Greek: καὶ ἦν Σάρα στεῖρα καὶ οὐκ ἐτεκνοποίει.
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

## Genesis 11:31

Greek: καὶ ἔλαβε Θάρα τὸν ῞Αβραμ υἱὸν αὐτοῦ καὶ τὸν Λὼτ υἱὸν ᾿Αρράν, υἱὸν τοῦ υἱοῦ αὐτοῦ, καὶ τὴν Σάραν τὴν νύμφην αὐτοῦ, γυναῖκα ῞Αβραμ τοῦ υἱοῦ αὐτοῦ, καὶ ἐξήγαγεν αὐτοὺς ἐκ τῆς χώρας τῶν Χαλδαίων πορευθῆναι εἰς γῆν Χαναὰν καὶ ἦλθον ἕως Χαρρὰν καὶ κατῴκησεν ἐκεῖ.
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

## Genesis 11:32

Greek: καὶ ἐγένοντο πᾶσαι αἱ ἡμέραι Θάρα ἐν γῇ Χαρρὰν διακόσια πέντε ἔτη, καὶ ἀπέθανε Θάρα ἐν Χαρράν.
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

# Chapter 12

## Genesis 12:1

Greek: ΚΑΙ εἶπε Κύριος τῷ ῞Αβραμ· ἔξελθε ἐκ τῆς γῆς σου καὶ ἐκ τῆς συγγενείας σου καὶ ἐκ τοῦ οἴκου τοῦ πατρός σου καὶ δεῦρο εἰς τὴν γῆν, ἣν ἄν σοι δείξω·
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

## Genesis 12:2

Greek: καὶ ποιήσω σε εἰς ἔθνος μέγα καὶ εὐλογήσω σε καὶ μεγαλυνῶ τὸ ὄνομά σου, καὶ ἔσῃ εὐλογημένος·
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

## Genesis 12:3

Greek: καὶ εὐλογήσω τοὺς εὐλογοῦντάς σε καὶ τοὺς καταρωμένους σε καταράσομαι· καὶ ἐνευλογηθήσονται ἐν σοὶ πᾶσαι αἱ φυλαὶ τῆς γῆς.
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

## Genesis 12:4

Greek: καὶ ἐπορεύθη ῞Αβραμ, καθάπερ ἐλάλησεν αὐτῷ Κύριος, καὶ ᾤχετο μετ᾿ αὐτοῦ Λώτ. ῞Αβραμ δὲ ἦν ἐτῶν ἑβδομηκονταπέντε, ὅτε ἐξῆλθε ἐκ Χαρράν.
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

## Genesis 12:5

Greek: καὶ ἔλαβεν ῞Αβραμ Σάραν τὴν γυναῖκα αὐτοῦ καὶ τὸν Λὼτ υἱὸν τοῦ ἀδελφοῦ αὐτοῦ καὶ πάντα τὰ ὑπάρχοντα αὐτῶν, ὅσα ἐκτήσαντο, καὶ πᾶσαν ψυχήν, ἣν ἐκτήσαντο ἐκ Χαρράν, καὶ ἐξήλθοσαν πορευθῆναι εἰς γῆν Χαναάν.
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

## Genesis 12:6

Greek: καὶ διώδευσεν ῞Αβραμ τὴν γῆν εἰς τὸ μῆκος αὐτῆς ἕως τοῦ τόπου Συχέμ, ἐπὶ τὴν δρῦν τὴν ὑψηλήν· οἱ δὲ Χαναναῖοι τότε κατῴκουν τὴν γῆν.
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

## Genesis 12:7

Greek: καὶ ὤφθη Κύριος τῷ ῞Αβραμ καὶ εἶπεν αὐτῷ· τῷ σπέρματί σου δώσω τὴν γῆν ταύτην. καὶ ᾠκοδόμησεν ἐκεῖ ῞Αβραμ θυσιαστήριον Κυρίῳ τῷ ὀφθέντι αὐτῷ.
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

## Genesis 12:8

Greek: καὶ ἀπέστη ἐκεῖθεν εἰς τὸ ὄρος κατὰ ἀνατολὰς Βαιθὴλ καὶ ἔστησεν ἐκεῖ τὴν σκηνὴν αὐτοῦ, Βαιθὴλ κατὰ θάλασσαν καὶ ᾿Αγγαὶ κατὰ ἀνατολάς· καὶ ᾠκοδόμησεν ἐκεῖ θυσιαστήριον τῷ Κυρίῳ καὶ ἐπεκαλέσατο ἐπὶ τῷ ὀνόματι Κυρίου.
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

## Genesis 12:9

Greek: καὶ ἀπῇρεν ῞Αβραμ καὶ πορευθεὶς ἐστρατοπέδευσεν ἐν τῇ ἐρήμῳ.
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

## Genesis 12:10

Greek: Καὶ ἐγένετο λιμὸς ἐπὶ τῆς γῆς, καὶ κατέβη ῞Αβραμ εἰς Αἴγυπτον παροικῆσαι ἐκεῖ, ὅτι ἐνίσχυσεν ὁ λιμὸς ἐπὶ τῆς γῆς.
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

## Genesis 12:11

Greek: ἐγένετο δέ, ἡνίκα ἤγγισεν ῞Αβραμ εἰσελθεῖν εἰς Αἴγυπτον, εἶπεν ῞Αβραμ Σάρᾳ τῇ γυναικί· γινώσκω ἐγώ, ὅτι γυνὴ εὐπρόσωπος εἶ·
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

## Genesis 12:12

Greek: ἔσται οὖν, ὡς ἂν ἴδωσί σε οἱ Αἰγύπτιοι, ἐροῦσιν ὅτι γυνὴ αὐτοῦ ἐστιν αὐτή, καὶ ἀποκτενοῦσί με, σὲ δὲ περιποιήσονται.
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

## Genesis 12:13

Greek: εἰπὸν οὖν, ὅτι ἀδελφὴ αὐτοῦ εἰμι, ὅπως ἂν εὖ μοι γένηται διὰ σέ, καὶ ζήσεται ἡ ψυχή μου ἕνεκέν σου.
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

## Genesis 12:14

Greek: ἐγένετο δέ, ἡνίκα εἰσῆλθεν ῞Αβραμ εἰς Αἴγυπτον, ἰδόντες οἱ Αἰγύπτιοι τὴν γυναῖκα αὐτοῦ, ὅτι καλὴ ἦν σφόδρα,
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

## Genesis 12:15

Greek: καὶ εἶδον αὐτὴν οἱ ἄρχοντες Φαραὼ καὶ ἐπῄνεσαν αὐτὴν πρὸς Φαραὼ καὶ εἰσήγαγον αὐτὴν εἰς τὸν οἶκον Φαραώ·
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

## Genesis 12:16

Greek: καὶ τῷ ῞Αβραμ εὖ ἐχρήσαντο δι᾿ αὐτήν, καὶ ἐγένοντο αὐτῷ πρόβατα καὶ μόσχοι καὶ ὄνοι καὶ παῖδες καὶ παιδίσκαι καὶ ἡμίονοι καὶ κάμηλοι.
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

## Genesis 12:17

Greek: καὶ ἤτασεν ὁ Θεὸς τὸν Φαραὼ ἐτασμοῖς μεγάλοις καὶ πονηροῖς καὶ τὸν οἶκον αὐτοῦ περὶ Σάρας τῆς γυναικὸς ῞Αβραμ.
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

## Genesis 12:18

Greek: καλέσας δὲ Φαραὼ τὸν ῞Αβραμ εἶπε· τί τοῦτο ἐποίησάς μοι, ὅτι οὐκ ἀπήγγειλάς μοι, ὅτι γυνή σου ἐστίν
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

## Genesis 12:19

Greek: ἱνατί εἶπας ὅτι ἀδελφή μου ἐστί; καὶ ἔλαβον αὐτὴν ἐμαυτῷ γυναῖκα, καὶ νῦν ἰδοὺ ἡ γυνή σου ἔναντί σου· λαβὼν ἀπότρεχε.
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

## Genesis 12:20

Greek: καὶ ἐνετείλατο Φαραὼ ἀνδράσι περὶ ῞Αβραμ συμπροπέμψαι αὐτὸν καὶ τὴν γυναῖκα αὐτοῦ καὶ πάντα, ὅσα ἦν αὐτῷ.
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

# Chapter 13

## Genesis 13:1

Greek: ΑΝΕΒΗ δὲ ῞Αβραμ ἐξ Αἰγύπτου, αὐτὸς καὶ ἡ γυνὴ αὐτοῦ καὶ πάντα τὰ αὐτοῦ καὶ Λὼτ μετ᾿ αὐτοῦ, εἰς τὴν ἔρημον.
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

## Genesis 13:2

Greek: ῞Αβραμ δὲ ἦν πλούσιος σφόδρα κτήνεσι καὶ ἀργυρίῳ καὶ χρυσίῳ.
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

## Genesis 13:3

Greek: καὶ ἐπορεύθη ὅθεν ἦλθεν εἰς τὴν ἔρημον ἕως Βαιθήλ, ἕως τοῦ τόπου, οὗ ἦν ἡ σκηνὴ αὐτοῦ τὸ πρότερον, ἀνὰ μέσον Βαιθὴλ καὶ ἀνὰ μέσον ᾿Αγγαί,
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

## Genesis 13:4

Greek: εἰς τὸν τόπον τοῦ θυσιαστηρίου, οὗ ἐποίησεν ἐκεῖ τὴν ἀρχήν· καὶ ἐπεκαλέσατο ἐκεῖ ῞Αβραμ τὸ ὄνομα τοῦ Κυρίου.
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

## Genesis 13:5

Greek: καὶ Λὼτ τῷ συμπορευομένῳ μετὰ ῞Αβραμ ἦν πρόβατα καὶ βόες καὶ σκηναί.
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

## Genesis 13:6

Greek: καὶ οὐκ ἐχώρει αὐτοὺς ἡ γῆ κατοικεῖν ἅμα, ὅτι ἦν τὰ ὑπάρχοντα αὐτῶν πολλά, καὶ οὐκ ἐχώρει αὐτοὺς ἡ γῆ κατοικεῖν ἅμα.
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

## Genesis 13:7

Greek: καὶ ἐγένετο μάχη ἀνὰ μέσον τῶν ποιμένων τῶν κτηνῶν τοῦ ῞Αβραμ καὶ ἀνὰ μέσον τῶν ποιμένων τῶν κτηνῶν τοῦ Λώτ· οἱ δὲ Χαναναῖοι καὶ οἱ Φερεζαῖοι τότε κατῴκουν τὴν γῆν.
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

## Genesis 13:8

Greek: εἶπε δὲ ῞Αβραμ τῷ Λώτ· μὴ ἔστω μάχη ἀνὰ μέσον ἐμοῦ καὶ σοῦ καὶ ἀνὰ μέσον τῶν ποιμένων μου καὶ ἀνὰ μέσον τῶν ποιμένων σου, ὅτι ἄνθρωποι ἀδελφοί ἐσμεν ἡμεῖς.
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

## Genesis 13:9

Greek: οὐκ ἰδοὺ πᾶσα ἡ γῆ ἐναντίον σου ἐστί; διαχωρίσθητι ἀπ᾿ ἐμοῦ· εἰ σὺ εἰς ἀριστερά, ἐγὼ εἰς δεξιά· εἰ δὲ σὺ εἰς δεξιά, ἐγὼ εἰς ἀριστερά.
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

## Genesis 13:10

Greek: καὶ ἐπάρας Λὼτ τοὺς ὀφθαλμοὺς αὐτοῦ, ἐπεῖδε πᾶσαν τὴν περίχωρον τοῦ ᾿Ιορδάνου, ὅτι πᾶσα ἦν ποτιζομένη πρὸ τοῦ καταστρέψαι τὸν Θεὸν Σόδομα καὶ Γόμορρα, ὡς ὁ παράδεισος τοῦ Θεοῦ καὶ ὡς ἡ γῆ Αἰγύπτου, ἕως ἐλθεῖν εἰς Ζόγορα.
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

## Genesis 13:11

Greek: καὶ ἐξελέξατο ἑαυτῷ Λὼτ πᾶσαν τὴν περίχωρον τοῦ ᾿Ιορδάνου, καὶ ἀπῇρε Λὼτ ἀπὸ ἀνατολῶν, καὶ διεχωρίσθησαν ἕκαστος ἀπὸ τοῦ ἀδελφοῦ αὐτοῦ.
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

## Genesis 13:12

Greek: ῞Αβραμ δὲ κατῴκησεν ἐν γῇ Χαναάν, Λὼτ δὲ κατῴκησεν ἐν πόλει τῶν περιχώρων καὶ ἐσκήνωσεν ἐν Σοδόμοις·
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

## Genesis 13:13

Greek: οἱ δὲ ἄνθρωποι οἱ ἐν Σοδόμοις πονηροὶ καὶ ἁμαρτωλοὶ ἐναντίον τοῦ Θεοῦ σφόδρα.
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

## Genesis 13:14

Greek: ῾Ο δὲ Θεὸς εἶπε τῷ ῞Αβραμ μετὰ τὸ διαχωρισθῆναι τὸν Λὼτ ἀπ᾿ αὐτοῦ· ἀνάβλεψον τοῖς ὀφθαλμοῖς σου καὶ ἴδε ἀπὸ τοῦ τόπου, οὗ νῦν σύ εἶ, πρὸς βορρᾶν καὶ λίβα καὶ ἀνατολὰς καὶ θάλασσαν·
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

## Genesis 13:15

Greek: ὅτι πᾶσαν τὴν γῆν, ἣν σὺ ὁρᾷς, σοὶ δώσω αὐτὴν καὶ τῷ σπέρματί σου ἕως αἰῶνος.
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

## Genesis 13:16

Greek: καὶ ποιήσω τὸ σπέρμα σου ὡς τὴν ἄμμον τῆς γῆς· εἰ δύναταί τις ἐξαριθμῆσαι τὴν ἄμμον τῆς γῆς, καὶ τὸ σπέρμα σου ἐξαριθμηθήσεται.
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

## Genesis 13:17

Greek: ἀναστὰς διόδευσον τὴν γῆν εἴς τε τὸ μῆκος αὐτῆς καὶ εἰς τὸ πλάτος, ὅτι σοὶ δώσω αὐτὴν καὶ τῷ σπέρματί σου εἰς τὸν αἰῶνα.
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

## Genesis 13:18

Greek: καὶ ἀποσκηνώσας ῞Αβραμ, ἐλθὼν κατῴκησε παρὰ τὴν δρῦν τὴν Μαμβρῆ, ἣ ἦν ἐν Χεβρώμ, καὶ ᾠκοδόμησεν ἐκεῖ θυσιαστήριον τῷ Κυρίῳ.
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

# Chapter 14

## Genesis 14:1

Greek: ΕΓΕΝΕΤΟ δὲ ἐν τῇ βασιλείᾳ τῇ ᾿Αμαρφὰλ βασιλέως Σενναάρ, καὶ ᾿Αριὼχ βασιλέως ᾿Ελλασάρ, Χοδολλογομὸρ βασιλεὺς ᾿Ελὰμ καὶ Θαργὰλ βασιλεὺς ἐθνῶν
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

## Genesis 14:2

Greek: ἐποίησαν πόλεμον μετὰ Βαλλὰ βασιλέως Σοδόμων καὶ μετὰ Βαρσὰ βασιλέως Γομόρρας καὶ μετὰ Σενναὰρ βασιλέως ᾿Αδαμὰ καὶ μετὰ Συμοβὸρ βασιλέως Σεβωείμ, καὶ βασιλέως Βαλάκ (αὕτη ἐστὶ Σηγώρ).
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

## Genesis 14:3

Greek: πάντες οὗτοι συνεφώνησαν ἐπὶ τὴν φάραγγα τὴν ἁλυκὴν (αὕτη ἡ θάλασσα τῶν ἁλῶν).
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

## Genesis 14:4

Greek: δώδεκα ἔτη αὐτοὶ ἐδούλευσαν τῷ Χοδολλογομόρ, τῷ δὲ τρισκαιδεκάτῳ ἔτει ἀπέστησαν.
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

## Genesis 14:5

Greek: ἐν δὲ τῷ τεσσαρεσκαιδεκάτῳ ἔτει ἦλθε Χοδολλογομὸρ καὶ οἱ βασιλεῖς μετ᾿ αὐτοῦ καὶ κατέκοψαν τοὺς γίγαντας τοὺς ἐν ᾿Ασταρὼθ καὶ Καρναΐν, καὶ ἔθνη ἰσχυρὰ ἅμα αὐτοῖς καὶ τοὺς ᾿Ομμαίους τοὺς ἐν Σαυῇ τῇ πόλει
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

## Genesis 14:6

Greek: καὶ τοὺς Χορραίους τοὺς ἐν τοῖς ὄρεσι Σηείρ, ἕως τῆς τερεβίνθου τῆς Φαράν, ἥ ἐστιν ἐν τῇ ἐρήμῳ.
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

## Genesis 14:7

Greek: καὶ ἀναστρέψαντες ἦλθον ἐπὶ τὴν πηγὴν τῆς κρίσεως (αὕτη ἐστὶ Κάδης) καὶ κατέκοψαν πάντας τοὺς ἄρχοντας ᾿Αμαλὴκ καὶ τοὺς ᾿Αμορραίους τοὺς κατοικοῦντας ἐν ᾿Ασασονθαμάρ.
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

## Genesis 14:8

Greek: ἐξῆλθε δὲ βασιλεὺς Σοδόμων καὶ βασιλεὺς Γομόρρας καὶ βασιλεὺς ᾿Αδαμὰ καὶ βασιλεὺς Σεβωεὶμ καὶ βασιλεὺς Βαλάκ (αὕτη ἐστὶ Σηγώρ) καὶ παρετάξαντο αὐτοῖς εἰς πόλεμον ἐν τῇ κοιλάδι τῇ ἁλυκῇ,
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

## Genesis 14:9

Greek: πρὸς Χοδολλογομὸρ βασιλέα ᾿Ελὰμ καὶ Θαργὰλ βασιλέα ἐθνῶν καὶ ᾿Αμαρφὰλ βασιλέα Σενναὰρ καὶ ᾿Αριὼχ βασιλέα ᾿Ελλασάρ, οἱ τέσσαρες βασιλεῖς πρὸς τοὺς πέντε.
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

## Genesis 14:10

Greek: ἡ δὲ κοιλὰς ἡ ἁλυκή, φρέατα ἀσφάλτου. ἔφυγε δὲ βασιλεὺς Σοδόμων καὶ βασιλεὺς Γομόρρας καὶ ἐνέπεσαν ἐκεῖ, οἱ δὲ καταλειφθέντες εἰς τὴν ὀρεινὴν ἔφυγον.
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

## Genesis 14:11

Greek: ἔλαβον δὲ τὴν ἵππον πᾶσαν τὴν Σοδόμων καὶ Γομόρρας καὶ πάντα τὰ βρώματα αὐτῶν καὶ ἀπῆλθον.
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

## Genesis 14:12

Greek: ἔλαβον δὲ καὶ τὸν Λὼτ τὸν υἱὸν τοῦ ἀδελφοῦ ῞Αβραμ καὶ τὴν ἀποσκευὴν αὐτοῦ καὶ ἀπῴχοντο· ἦν γὰρ κατοικῶν ἐν Σοδόμοις.
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

## Genesis 14:13

Greek: Παραγενόμενος δὲ τῶν ἀνασωθέντων τις ἀπήγγειλεν ῞Αβραμ τῷ περάτῃ· αὐτὸς δὲ κατῴκει παρὰ τῇ δρυΐ τῇ Μαμβρῇ ᾿Αμορραίου τοῦ ἀδελφοῦ ᾿Εσχὼλ καὶ τοῦ ἀδελφοῦ Αὐνάν, οἳ ἦσαν συνωμόται τοῦ ῞Αβραμ.
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

## Genesis 14:14

Greek: ἀκούσας δὲ ῞Αβραμ ὅτι ᾐχμαλώτευται Λὼτ ὁ ἀδελφιδοῦς αὐτοῦ, ἠρίθμησε τοὺς ἰδίους οἰκογενεῖς αὐτοῦ, τριακοσίους δέκα καὶ ὀκτώ, καὶ κατεδίωξεν ὀπίσω αὐτῶν ἕως Δάν.
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

## Genesis 14:15

Greek: καὶ ἐπέπεσεν ἐπ᾿ αὐτοὺς τὴν νύκτα αὐτὸς καὶ οἱ παῖδες αὐτοῦ, καὶ ἐπάταξεν αὐτοὺς καὶ κατεδίωξεν αὐτοὺς ἕως Χοβά, ἥ ἐστιν ἐν ἀριστερᾷ Δαμασκοῦ.
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

## Genesis 14:16

Greek: καὶ ἀπέστρεψε πᾶσαν τὴν ἵππον Σοδόμων, καὶ Λὼτ τὸν ἀδελφιδοῦν αὐτοῦ ἀπέστρεψε καὶ πάντα τὰ ὑπάρχοντα αὐτοῦ καὶ τὰς γυναῖκας καὶ τὸν λαόν.
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

## Genesis 14:17

Greek: ᾿Εξῆλθε δὲ βασιλεὺς Σοδόμων εἰς συνάντησιν αὐτῷ, μετὰ τὸ ὑποστρέψαι αὐτὸν ἀπὸ τῆς κοπῆς τοῦ Χοδολλογομὸρ καὶ τῶν βασιλέων τῶν μετ᾿ αὐτοῦ, εἰς τὴν κοιλάδα τοῦ Σαβύ (τοῦτο ἦν τὸ πεδίον τῶν βασιλέων).
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

## Genesis 14:18

Greek: καὶ Μελχισεδὲκ βασιλεὺς Σαλὴμ ἐξήνεγκεν ἄρτους καὶ οἶνον· ἦν δὲ ἱερεὺς τοῦ Θεοῦ τοῦ ὑψίστου.
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

## Genesis 14:19

Greek: καὶ εὐλόγησε τὸν ῞Αβραμ καὶ εἶπεν· εὐλογημένος ῞Αβραμ τῷ Θεῷ τῷ ὑψίστῳ, ὃς ἔκτισε τὸν οὐρανὸν καὶ τὴν γῆν.
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

## Genesis 14:20

Greek: καὶ εὐλογητὸς ὁ Θεὸς ὁ ὕψιστος, ὃς παρέδωκε τοὺς ἐχθρούς σου ὑποχειρίους σοι. καὶ ἔδωκεν αὐτῷ ῞Αβραμ δεκάτην ἀπὸ πάντων.
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

## Genesis 14:21

Greek: εἶπε δὲ βασιλεὺς Σοδόμων πρὸς ῞Αβραμ· δός μοι τοὺς ἄνδρας, τὴν δὲ ἵππον λάβε σεαυτῷ.
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

## Genesis 14:22

Greek: εἶπε δὲ ῞Αβραμ πρὸς τὸν βασιλέα Σοδόμων· ἐκτενῶ τὴν χεῖρά μου πρὸς Κύριον τὸν Θεὸν τὸν ὕψιστον, ὃς ἔκτισε τὸν οὐρανὸν καὶ τὴν γῆν,
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

## Genesis 14:23

Greek: εἰ ἀπὸ σπαρτίου ἕως σφυρωτῆρος ὑποδήματος λήψομαι ἀπὸ πάντων τῶν σῶν, ἵνα μὴ εἴπῃς, ὅτι ἐγὼ ἐπλούτισα τὸν ῞Αβραμ·
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

## Genesis 14:24

Greek: πλὴν ὧν ἔφαγον οἱ νεανίσκοι καὶ τῆς μερίδος τῶν ἀνδρῶν τῶν συμπορευθέντων μετ᾿ ἐμοῦ, ᾿Εσχώλ, Αὐνάν, Μαμβρῆ, οὗτοι λήψονται μερίδα.
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

# Chapter 15

## Genesis 15:1

Greek: ΜΕΤΑ δὲ τὰ ρήματα ταῦτα ἐγενήθη ρῆμα Κυρίου πρὸς ῞Αβραμ ἐν ὁράματι, λέγων· μὴ φοβοῦ ῞Αβραμ, ἐγὼ ὑπερασπίζω σου· ὁ μισθός σου πολὺς ἔσται σφόδρα.
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

## Genesis 15:2

Greek: λέγει δὲ ῞Αβραμ· δέσποτα Κύριε, τί μοι δώσεις; ἐγὼ δὲ ἀπολύομαι ἄτεκνος· ὁ δὲ υἱὸς Μασὲκ τῆς οἰκογενοῦς μου, οὗτος Δαμασκὸς ᾿Ελιέζερ.
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

## Genesis 15:3

Greek: καὶ εἶπεν ῞Αβραμ· ἐπειδὴ ἐμοὶ οὐκ ἔδωκας σπέρμα, ὁ δὲ οἰκογενής μου κληρονομήσει μοι.
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

## Genesis 15:4

Greek: καὶ εὐθὺς φωνὴ Κυρίου ἐγένετο πρὸς αὐτὸν λέγουσα· οὐ κληρονομήσει σε οὗτος, ἀλλ᾿ ὃς ἐξελεύσεται ἐκ σοῦ, οὗτος κληρονομήσει σε.
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

## Genesis 15:5

Greek: ἐξήγαγε δὲ αὐτὸν ἔξω καὶ εἶπεν αὐτῷ· ἀνάβλεψον δὴ εἰς τὸν οὐρανὸν καὶ ἀρίθμησον τοὺς ἀστέρας, εἰ δυνήσῃ ἐξαριθμῆσαι αὐτούς. καὶ εἶπεν· οὕτως ἔσται τὸ σπέρμα σου.
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

## Genesis 15:6

Greek: καὶ ἐπίστευσεν ῞Αβραμ τῷ Θεῷ, καὶ ἐλογίσθη αὐτῷ εἰς δικαιοσύνην.
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

## Genesis 15:7

Greek: εἶπε δὲ πρὸς αὐτόν· ἐγὼ ὁ Θεὸς ὁ ἐξαγαγών σε ἐκ χώρας Χαλδαίων, ὥστε δοῦναί σοι τὴν γῆν ταύτην κληρονομῆσαι.
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

## Genesis 15:8

Greek: εἶπε δέ, Δέσποτα Κύριε, κατὰ τί γνώσομαι ὅτι κληρονομήσω αὐτήν
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

## Genesis 15:9

Greek: εἶπε δὲ αὐτῷ· λάβε μοι δάμαλιν τριετίζουσαν καὶ αἶγα τριετίζουσαν καὶ κριὸν τριετίζοντα καὶ τρυγόνα καὶ περιστεράν.
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

## Genesis 15:10

Greek: ἔλαβε δὲ αὐτῷ πάντα ταῦτα καὶ διεῖλεν αὐτὰ μέσα καὶ ἔθηκεν αὐτὰ ἀντιπρόσωπα ἀλλήλοις, τὰ δὲ ὄρνεα οὐ διεῖλε.
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

## Genesis 15:11

Greek: κατέβη δὲ ὄρνεα ἐπὶ τὰ σώματα, ἐπὶ τὰ διχοτομήματα αὐτῶν, καὶ συνεκάθησεν αὐτοῖς ῞Αβραμ.
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

## Genesis 15:12

Greek: περὶ δὲ ἡλίου δυσμὰς ἔκστασις ἐπέπεσε τῷ ῞Αβραμ, καὶ ἰδοὺ φόβος σκοτεινὸς μέγας ἐπιπίπτει αὐτῷ.
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

## Genesis 15:13

Greek: καὶ ἐρρέθη πρὸς ῞Αβραμ· γινώσκων γνώσῃ ὅτι πάροικον ἔσται τὸ σπέρμα σου ἐν γῇ οὐκ ἰδίᾳ, καὶ δουλώσουσιν αὐτοὺς καὶ κακώσουσιν αὐτοὺς καὶ ταπεινώσουσιν αὐτοὺς τετρακόσια ἔτη.
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

## Genesis 15:14

Greek: τὸ δὲ ἔθνος, ᾧ ἐὰν δουλεύσωσι, κρινῶ ἐγώ· μετὰ δὲ ταῦτα ἐξελεύσονται ὧδε μετὰ ἀποσκευῆς πολλῆς.
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

## Genesis 15:15

Greek: σὺ δὲ ἀπελεύσῃ πρὸς τοὺς πατέρας σου ἐν εἰρήνῃ, τραφεὶς ἐν γήρᾳ καλῷ.
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

## Genesis 15:16

Greek: τετάρτῃ δὲ γενεᾷ ἀποστραφήσονται ὧδε· οὔπω γὰρ ἀναπεπλήρωνται αἱ ἁμαρτίαι τῶν ᾿Αμορραίων ἕως τοῦ νῦν.
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

## Genesis 15:17

Greek: ἐπεὶ δὲ ὁ ἥλιος ἐγένετο πρὸς δυσμάς, φλὸξ ἐγένετο, καὶ ἰδοὺ κλίβανος καπνιζόμενος καὶ λαμπάδες πυρός, αἳ διῆλθον ἀνὰ μέσον τῶν διχοτομημάτων τούτων.
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

## Genesis 15:18

Greek: ἐν τῇ ἡμέρᾳ ἐκείνῃ διέθετο Κύριος τῷ ῞Αβραμ διαθήκην λέγων· τῷ σπέρματί σου δώσω τὴν γῆν ταύτην, ἀπὸ τοῦ ποταμοῦ Αἰγύπτου ἕως τοῦ ποταμοῦ τοῦ μεγάλου, ποταμοῦ Εὐφράτου,
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

## Genesis 15:19

Greek: τοὺς Κεναίους καὶ τοὺς Κενεζαίους καὶ τούς Κεδμωναίους
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

## Genesis 15:20

Greek: καὶ τοὺς Χετταίους καὶ τοὺς Φερεζαίους καὶ Ραφαεὶν καὶ τοὺς ᾿Αμορραίους καὶ τοὺς Χαναναίους καὶ τοὺς Εὐαίους καὶ τοὺς Γεργεσαίους καὶ τοὺς ᾿Ιεβουσαίους.
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

# Chapter 16

## Genesis 16:1

Greek: ΣΑΡΑ δὲ γυνὴ ῞Αβραμ οὐκ ἔτικτεν αὐτῷ. ἦν δὲ αὐτῇ παιδίσκη Αἰγυπτία, ᾗ ὄνομα ῎Αγαρ.
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

## Genesis 16:2

Greek: εἶπε δὲ Σάρα πρὸς ῞Αβραμ· ἰδοὺ συνέκλεισέ με Κύριος τοῦ μὴ τίκτειν· εἴσελθε οὖν πρὸς τὴν παιδίσκην μου, ἵνα τεκνοποιήσωμαι ἐξ αὐτῆς. ὑπήκουσε δὲ ῞Αβραμ τῆς φωνῆς Σάρας.
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

## Genesis 16:3

Greek: καὶ λαβοῦσα Σάρα ἡ γυνὴ ῞Αβραμ ῎Αγαρ τὴν Αἰγυπτίαν τὴν ἑαυτῆς παιδίσκην, μετὰ δέκα ἔτη τοῦ οἰκῆσαι ῞Αβραμ ἐν γῇ Χαναάν, ἔδωκεν αὐτὴν τῷ ῞Αβραμ ἀνδρὶ αὐτῆς αὐτῷ γυναῖκα.
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

## Genesis 16:4

Greek: καὶ εἰσῆλθε πρὸς ῎Αγαρ, καὶ συνέλαβε. καὶ εἶδεν ὅτι ἐν γαστρὶ ἔχει, καὶ ἠτιμάσθη ἡ κυρία ἐναντίον αὐτῆς.
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

## Genesis 16:5

Greek: εἶπε δὲ Σάρα πρὸς ῞Αβραμ· ἀδικοῦμαι ἐκ σοῦ· ἐγὼ δέδωκα τὴν παιδίσκην μου εἰς τὸν κόλπον σου, ἰδοῦσα δὲ ὅτι ἐν γαστρὶ ἔχει, ἠτιμάσθην ἐναντίον αὐτῆς· κρίναι ὁ Θεὸς ἀνὰ μέσον ἐμοῦ καὶ σοῦ.
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

## Genesis 16:6

Greek: εἶπε δὲ ῞Αβραμ πρὸς Σάραν· ἰδοὺ ἡ παιδίσκη σου ἐν ταῖς χερσί σου· χρῶ αὐτῇ ὡς ἄν σοι ἀρεστόν ᾖ. καὶ ἐκάκωσεν αὐτὴν Σάρα, καὶ ἀπέδρα ἀπὸ προσώπου αὐτῆς.
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

## Genesis 16:7

Greek: Εὗρε δὲ αὐτὴν ἄγγελος Κυρίου ἐπὶ τῆς πηγῆς τοῦ ὕδατος ἐν τῇ ἐρήμῳ, ἐπὶ τῆς πηγῆς ἐν τῇ ὁδῷ Σούρ.
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

## Genesis 16:8

Greek: καὶ εἶπεν αὐτῇ ὁ ἄγγελος Κυρίου. ῎Αγαρ, παιδίσκη Σάρας, πόθεν ἔρχῃ καὶ ποῦ πορεύῃ; καὶ εἶπεν· ἀπὸ προσώπου Σάρας τῆς κυρίας μου ἐγὼ ἀποδιδράσκω.
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

## Genesis 16:9

Greek: εἶπε δὲ αὐτῇ ὁ ἄγγελος Κυρίου· ἀποστράφηθι πρὸς τὴν κυρίαν σου καὶ ταπεινώθητι ὑπὸ τὰς χεῖρας αὐτῆς.
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

## Genesis 16:10

Greek: καὶ εἶπεν αὐτῇ ὁ ἄγγελος Κυρίου· πληθύνων πληθυνῶ τὸ σπέρμα σου, καὶ οὐκ ἀριθμηθήσεται ὑπὸ τοῦ πλήθους.
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

## Genesis 16:11

Greek: καί εἶπεν αὐτῇ ὁ ἄγγελος Κυρίου· ἰδού, σὺ ἐν γαστρί ἔχεις καὶ τέξῃ υἱὸν καὶ καλέσεις τὸ ὄνομα αὐτοῦ ᾿Ισμαήλ, ὅτι ἐπήκουσε Κύριος τῇ ταπεινώσει σου.
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

## Genesis 16:12

Greek: οὗτος ἔσται ἄγροικος ἄνθρωπος αἱ χεῖρες αὐτοῦ ἐπὶ πάντας, καὶ αἱ χεῖρες πάντων ἐπ᾿ αὐτόν, καὶ κατὰ πρόσωπον πάντων τῶν ἀδελφῶν αὐτοῦ κατοικήσει.
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

## Genesis 16:13

Greek: καὶ ἐκάλεσεν ῎Αγαρ τὸ ὄνομα Κυρίου τοῦ λαλοῦντος πρὸς αὐτήν· σὺ ὁ Θεὸς ὁ ἐπιδών με, ὅτι εἶπε· καὶ γὰρ ἐνώπιον εἶδον ὀφθέντα μοι.
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

## Genesis 16:14

Greek: ἕνεκεν τούτου ἐκάλεσε τὸ φρέαρ Φρέαρ οὗ ἐνώπιον εἶδον· ἰδοὺ ἀνὰ μέσον Κάδης καὶ ἀνὰ μέσον Βαράδ.
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

## Genesis 16:15

Greek: Καὶ ἔτεκεν ῎Αγαρ τῷ ῞Αβραμ υἱόν, καὶ ἐκάλεσεν ῞Αβραμ τὸ ὄνομα τοῦ υἱοῦ αὐτοῦ, ὃν ἔτεκεν αὐτῷ ῎Αγαρ, ᾿Ισμαήλ.
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

## Genesis 16:16

Greek: ῞Αβραμ δὲ ἦν ἐτῶν ὀγδοηκονταέξ, ἡνίκα ἔτεκεν ῎Αγαρ τῷ ῞Αβραμ τὸν ᾿Ισμαήλ.
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

# Chapter 17

## Genesis 17:1

Greek: ΕΓΕΝΕΤΟ δὲ ῞Αβραμ ἐτῶν ἐνενηκονταεννέα, καὶ ὤφθη Κύριος τῷ ῞Αβραμ καὶ εἶπεν αὐτῷ· ἐγώ εἰμι ὁ Θεός σου· εὐαρέστει ἐνώπιον ἐμοῦ καὶ γίνου ἄμεμπτος,
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

## Genesis 17:2

Greek: καὶ θήσομαι τὴν διαθήκην μου ἀνὰ μέσον ἐμοῦ καὶ ἀνὰ μέσον σοῦ καὶ πληθυνῶ σε σφόδρα.
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

## Genesis 17:3

Greek: καὶ ἔπεσεν ῞Αβραμ ἐπὶ πρόσωπον αὐτοῦ, καὶ ἐλάλησεν αὐτῷ ὁ Θεὸς λέγων·
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

## Genesis 17:4

Greek: καὶ ἐγὼ ἰδοὺ ἡ διαθήκη μου μετὰ σοῦ, καὶ ἔσῃ πατὴρ πλήθους ἐθνῶν,
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

## Genesis 17:5

Greek: καὶ οὐ κληθήσεται ἔτι τὸ ὄνομά σου ῞Αβραμ, ἀλλ᾿ ἔσται τὸ ὄνομά σου ῾Αβραάμ, ὅτι πατέρα πολλῶν ἐθνῶν τέθεικά σε.
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

## Genesis 17:6

Greek: καὶ αὐξανῶ σε σφόδρα σφόδρα καὶ θήσω σε εἰς ἔθνη, καὶ βασιλεῖς ἐκ σοῦ ἐξελεύσονται.
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

## Genesis 17:7

Greek: καὶ στήσω τὴν διαθήκην μου ἀνὰ μέσον σοῦ καὶ ἀνὰ μέσον τοῦ σπέρματός σου μετά σέ, εἰς τὰς γενεὰς αὐτῶν, εἰς διαθήκην αἰώνιον, εἶναί σου Θεὸς καὶ τοῦ σπέρματός σου μετὰ σέ.
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

## Genesis 17:8

Greek: καὶ δώσω σοι καὶ τῷ σπέρματί σου μετὰ σὲ τὴν γῆν, ἣν παροικεῖς, πᾶσαν τὴν γῆν Χαναάν, εἰς κατάσχεσιν αἰώνιον καὶ ἔσομαι αὐτοῖς εἰς Θεόν.
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

## Genesis 17:9

Greek: καὶ εἶπεν ὁ Θεὸς πρὸς ῾Αβραάμ· σὺ δὲ τὴν διαθήκην μου διατηρήσεις, σὺ καὶ τὸ σπέρμα σου μετὰ σὲ εἰς τὰς γενεὰς αὐτῶν.
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

## Genesis 17:10

Greek: καὶ αὕτη ἡ διαθήκη, ἣν διατηρήσεις, ἀνὰ μέσον ἐμοῦ καὶ ὑμῶν καὶ ἀνὰ μέσον τοῦ σπέρματός σου μετὰ σὲ εἰς τὰς γενεὰς αὐτῶν· περιτμηθήσεται ὑμῶν πᾶν ἀρσενικόν,
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

## Genesis 17:11

Greek: καὶ περιτμηθήσεσθε τὴν σάρκα τῆς ἀκροβυστίας ὑμῶν, καὶ ἔσται εἰς σημεῖον διαθήκης ἀνὰ μέσον ἐμοῦ καὶ ὑμῶν.
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

## Genesis 17:12

Greek: καὶ παιδίον ὀκτὼ ἡμερῶν περιτμηθήσεται ὑμῖν, πᾶν ἀρσενικὸν εἰς τὰς γενεὰς ὑμῶν, ὁ οἰκογενὴς καὶ ὁ ἀργυρώνητος, ἀπὸ παντὸς υἱοῦ ἀλλοτρίου, ὃς οὐκ ἔστιν ἐκ τοῦ σπέρματός σου.
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

## Genesis 17:13

Greek: περιτομῇ περιτμηθήσεται ὁ οἰκογενὴς τῆς οἰκίας σου καὶ ὁ ἀργυρώνητος, καὶ ἔσται ἡ διαθήκη μου ἐπὶ τῆς σαρκὸς ὑμῶν εἰς διαθήκην αἰώνιον.
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

## Genesis 17:14

Greek: καὶ ἀπερίτμητος ἄρσην, ὃς οὐ περιτμηθήσεται τὴν σάρκα τῆς ἀκροβυστίας αὐτοῦ τῇ ἡμέρᾳ τῇ ὀγδόῃ, ἐξολοθρευθήσεται ἡ ψυχὴ ἐκείνη ἐκ τοῦ γένους αὐτῆς, ὅτι τὴν διαθήκην μου διεσκέδασε.
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

## Genesis 17:15

Greek: Καὶ εἶπεν ὁ Θεὸς τῷ ῾Αβραάμ· Σάρα ἡ γυνή σου οὐ κληθήσεται τὸ ὄνομα αὐτῆς Σάρα, ἀλλὰ Σάρρα ἔσται τὸ ὄνομα αὐτῆς.
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

## Genesis 17:16

Greek: εὐλογήσω δὲ αὐτήν, καὶ δώσω σοι ἐξ αὐτῆς τέκνον· καὶ εὐλογήσω αὐτό, καὶ ἔσται εἰς ἔθνη, καὶ βασιλεῖς ἐθνῶν ἐξ αὐτοῦ ἔσονται.
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

## Genesis 17:17

Greek: καὶ ἔπεσεν ῾Αβραὰμ ἐπὶ πρόσωπον αὐτοῦ καὶ ἐγέλασε καὶ εἶπεν ἐν τῇ διανοίᾳ αὐτοῦ λέγων· εἰ τῷ ἑκατονταετεῖ γενήσεται υἱός; καὶ εἰ ἡ Σάρρα ἐνενήκοντα ἐτῶν τέξεται
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

## Genesis 17:18

Greek: εἶπε δὲ ῾Αβραὰμ πρὸς τὸν Θεόν· ᾿Ισμαὴλ οὗτος ζήτω ἐναντίον σου.
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

## Genesis 17:19

Greek: εἶπε δὲ ὁ Θεὸς πρὸς ῾Αβραὰμ· ναί· ἰδοὺ Σάρρα ἡ γυνή σου τέξεταί σοι υἱόν, καὶ καλέσεις τὸ ὄνομα αὐτοῦ ᾿Ισαάκ, καὶ στήσω τὴν διαθήκην μου πρὸς αὐτὸν εἰς διαθήκην αἰώνιον, εἶναι αὐτῷ Θεὸς καὶ τῷ σπέρματι αὐτοῦ μετ᾿ αὐτόν.
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

## Genesis 17:20

Greek: περὶ δὲ ᾿Ισμαὴλ ἰδοὺ ἐπήκουσά σου· καὶ ἰδοὺ εὐλόγηκα αὐτὸν καὶ αὐξανῶ αὐτόν καὶ πληθυνῶ αὐτὸν σφόδρα· δώδεκα ἔθνη γεννήσει καὶ δώσω αὐτὸν εἰς ἔθνος μέγα.
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

## Genesis 17:21

Greek: τὴν δὲ διαθήκην μου στήσω πρὸς ᾿Ισαάκ, ὃν τέξεταί σοι Σάρρα εἰς τὸν καιρὸν τοῦτον, ἐν τῷ ἐνιαυτῷ τῷ ἑτέρῳ.
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

## Genesis 17:22

Greek: συνετέλεσε δὲ λαλῶν πρὸς αὐτὸν καὶ ἀνέβη ὁ Θεὸς ἀπό ῾Αβραάμ.
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

## Genesis 17:23

Greek: Καὶ ἔλαβεν ῾Αβραὰμ ᾿Ισμαὴλ τὸν υἱὸν ἑαυτοῦ καὶ πάντας τοὺς οἰκογενεῖς αὐτοῦ καὶ πάντας τοὺς ἀργυρωνήτους καὶ πᾶν ἄρσεν τῶν ἀνδρῶν τῶν ἐν τῷ οἴκῳ ῾Αβραὰμ καὶ περιέτεμε τὰς ἀκροβυστίας αὐτῶν ἐν τῷ καιρῷ τῆς ἡμέρας ἐκείνης, καθὰ ἐλάλησεν αὐτῷ ὁ Θεός.
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

## Genesis 17:24

Greek: ῾Αβραὰμ δὲ ἐνενηκονταεννέα ἦν ἐτῶν, ἡνίκα περιετέμετο τὴν σάρκα τῆς ἀκροβυστίας αὐτοῦ.
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

## Genesis 17:25

Greek: ᾿Ισμαὴλ δὲ ὁ υἱὸς αὐτοῦ ἦν ἐτῶν δεκατριῶν, ἡνίκα περιετέμετο τὴν σάρκα τῆς ἀκροβυστίας αὐτοῦ.
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

## Genesis 17:26

Greek: ἐν δὲ τῷ καιρῷ τῆς ἡμέρας ἐκείνης περιετμήθη ῾Αβραὰμ καὶ ᾿Ισμαὴλ ὁ υἱὸς αὐτοῦ·
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

## Genesis 17:27

Greek: καὶ πάντες οἱ ἄνδρες τοῦ οἴκου αὐτοῦ καὶ οἱ οἰκογενεῖς αὐτοῦ καὶ οἱ ἀργυρώνητοι ἐξ ἀλλογενῶν ἐθνῶν, περιέτεμεν αὐτούς.
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

# Chapter 18

## Genesis 18:1

Greek: ΩΦΘΗ δὲ αὐτῷ ὁ Θεὸς πρὸς τῇ δρυΐ τῇ Μαμβρῇ, καθημένου αὐτοῦ ἐπὶ τῆς θύρας τῆς σκηνῆς αὐτοῦ μεσημβρίας.
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

## Genesis 18:2

Greek: ἀναβλέψας δέ τοῖς ὀφθαλμοῖς αὐτοῦ εἶδε, καὶ ἰδοὺ τρεῖς ἄνδρες εἱστήκεισαν ἐπάνω αὐτοῦ· καὶ ἰδὼν προσέδραμεν εἰς συνάντησιν αὐτοῖς ἀπὸ τῆς θύρας τῆς σκηνῆς αὐτοῦ καὶ προσεκύνησεν ἐπὶ τὴν γῆν.
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

## Genesis 18:3

Greek: καὶ εἶπε· κύριε, εἰ ἄρα εὗρον χάριν ἐναντίον σου, μὴ παρέλθῃς τὸν παῖδά σου·
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

## Genesis 18:4

Greek: ληφθήτω δὴ ὕδωρ, καὶ νιψάτωσαν τοὺς πόδας ὑμῶν, καὶ καταψύξατε ὑπὸ τὸ δένδρον·
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

## Genesis 18:5

Greek: καὶ λήψομαι ἄρτον, καὶ φάγεσθε, καὶ μετὰ τοῦτο παρελεύσεσθε εἰς τὴν ὁδὸν ὑμῶν, οὗ ἕνεκεν ἐξεκλίνατε πρὸς τὸν παῖδα ὑμῶν. καὶ εἶπαν· οὕτω ποίησον, καθὼς εἴρηκας.
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

## Genesis 18:6

Greek: καὶ ἔσπευσεν ῾Αβραὰμ ἐπὶ τὴν σκηνὴν πρὸς Σάρραν καὶ εἶπεν αὐτῇ· σπεῦσον καὶ φύρασον τρία μέτρα σεμιδάλεως καὶ ποίησον ἐγκρυφίας.
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

## Genesis 18:7

Greek: καὶ εἰς τὰς βόας ἔδραμεν ῾Αβραὰμ καὶ ἔλαβεν ἁπαλὸν μοσχάριον καὶ καλὸν καὶ ἔδωκε τῷ παιδί, καὶ ἐτάχυνε τοῦ ποιῆσαι αὐτό.
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

## Genesis 18:8

Greek: ἔλαβε δὲ βούτυρον, καὶ γάλα, καὶ τὸ μοσχάριον ὃ ἐποίησε, καὶ παρέθηκεν αὐτοῖς, καὶ ἔφαγον· αὐτὸς δὲ παρειστήκει αὐτοῖς ὑπὸ τὸ δένδρον.
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

## Genesis 18:9

Greek: Εἶπε δὲ πρὸς αὐτόν· ποῦ Σάρρα ἡ γυνή σου; ὁ δὲ ἀποκριθεὶς εἶπεν· ἰδοὺ ἐν τῇ σκηνῇ.
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

## Genesis 18:10

Greek: εἶπε δέ· ἐπαναστρέφων ἥξω πρὸς σὲ κατὰ τὸν καιρὸν τοῦτον εἰς ὥρας, καὶ ἕξει υἱὸν Σάρρα ἡ γυνή σου. Σάρρα δὲ ἤκουσε πρὸς τῇ θύρᾳ τῆς σκηνῆς, οὖσα ὄπισθεν αὐτοῦ.
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

## Genesis 18:11

Greek: ῾Αβραὰμ δὲ καὶ Σάρρα πρεσβύτεροι προβεβηκότες ἡμερῶν, ἐξέλιπε δὲ τῇ Σάρρᾳ γίνεσθαι τὰ γυναικεῖα.
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

## Genesis 18:12

Greek: ἐγέλασε δὲ Σάρρα ἐν ἑαυτῇ, λέγουσα· οὔπω μέν μοι γέγονεν ἕως τοῦ νῦν, ὁ δὲ κύριός μου πρεσβύτερος.
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

## Genesis 18:13

Greek: καὶ εἶπε Κύριος πρὸς ῾Αβραάμ· τί ὅτι ἐγέλασε Σάρρα ἐν ἑαυτῇ, λέγουσα· ἆρά γε ἀληθῶς τέξομαι; ἐγὼ δὲ γεγήρακα.
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

## Genesis 18:14

Greek: μὴ ἀδυνατήσει παρὰ τῷ Θεῷ ρῆμα; εἰς τὸν καιρὸν τοῦτον ἀναστρέψω πρὸς σὲ εἰς ὥρας· καὶ ἔσται τῇ Σάρρᾳ υἱός.
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

## Genesis 18:15

Greek: ἠρνήσατο δὲ Σάρρα λέγουσα· οὐκ ἐγέλασα· ἐφοβήθη γάρ. καὶ εἶπεν αὐτῇ· οὐχί, ἀλλὰ ἐγέλασας.
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

## Genesis 18:16

Greek: ᾿Εξαναστάντες δὲ ἐκεῖθεν οἱ ἄνδρες κατέβλεψαν ἐπὶ πρόσωπον Σοδόμων καὶ Γομόρρας. ῾Αβραὰμ δὲ συνεπορεύετο μετ᾿ αὐτῶν συμπροπέμπων αὐτούς.
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

## Genesis 18:17

Greek: ὁ δὲ Κύριος εἶπεν· οὐ μὴ κρύψω ἐγὼ ἀπὸ ῾Αβραὰμ τοῦ παιδός μου, ἃ ἐγὼ ποιῶ.
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

## Genesis 18:18

Greek: ῾Αβραὰμ δὲ γινόμενος ἔσται εἰς ἔθνος μέγα καὶ πολύ, καὶ ἐνευλογηθήσονται ἐν αὐτῷ πάντα τὰ ἔθνη τῆς γῆς.
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

## Genesis 18:19

Greek: ᾔδειν γὰρ ὅτι συντάξει τοῖς υἱοῖς αὐτοῦ καὶ τῷ οἴκῳ αὐτοῦ μετ᾿ αὐτόν, καὶ φυλάξουσι τὰς ὁδοὺς Κυρίου ποιεῖν δικαιοσύνην καὶ κρίσιν, ὅπως ἂν ἐπαγάγῃ Κύριος ἐπὶ ῾Αβραὰμ πάντα, ὅσα ἐλάλησε πρὸς αὐτόν.
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

## Genesis 18:20

Greek: εἶπε δὲ Κύριος· κραυγὴ Σοδόμων καὶ Γομόρρας πεπλήθυνται πρός με, καὶ αἱ ἁμαρτίαι αὐτῶν μεγάλαι σφόδρα.
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

## Genesis 18:21

Greek: καταβὰς οὖν ὄψομαι, εἰ κατὰ τὴν κραυγὴν αὐτῶν τὴν ἐρχομένην πρός με συντελοῦνται, εἰ δὲ μή, ἵνα γνῶ.
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

## Genesis 18:22

Greek: καὶ ἀποστρέψαντες ἐκεῖθεν οἱ ἄνδρες ἦλθον εἰς Σόδομα. ῾Αβραὰμ δὲ ἔτι ἦν ἑστηκὼς ἐναντίον Κυρίου.
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

## Genesis 18:23

Greek: καὶ ἐγγίσας ῾Αβραὰμ εἶπε· μὴ συναπολέσῃς δίκαιον μετὰ ἀσεβοῦς καὶ ἔσται ὁ δίκαιος ὡς ὁ ἀσεβής
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

## Genesis 18:24

Greek: ἐὰν ὦσι πεντήκοντα δίκαιοι ἐν τῇ πόλει, ἀπολεῖς αὐτούς; οὐκ ἀνήσεις πάντα τὸν τόπον ἕνεκεν τῶν πεντήκοντα δικαίων, ἐὰν ὦσιν ἐν αὐτῇ
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

## Genesis 18:25

Greek: μηδαμῶς σὺ ποιήσεις ὡς τὸ ρῆμα τοῦτο, τοῦ ἀποκτεῖναι δίκαιον μετὰ ἀσεβοῦς, καὶ ἔσται ὁ δίκαιος ὡς ὁ ἀσεβής. μηδαμῶς· ὁ κρίνων πᾶσαν τὴν γῆν, οὐ ποιήσεις κρίσιν
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

## Genesis 18:26

Greek: εἶπε δὲ Κύριος· ἐὰν ὦσιν ἐν Σοδόμοις πεντήκοντα δίκαιοι ἐν τῇ πόλει, ἀφήσω ὅλην τὴν πόλιν καὶ πάντα τὸν τόπον δι᾿ αὐτούς.
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

## Genesis 18:27

Greek: καὶ ἀποκριθεὶς ῾Αβραὰμ εἶπε· νῦν ἠρξάμην λαλῆσαι πρὸς τὸν Κύριόν μου, ἐγὼ δέ εἰμι γῆ καὶ σποδός·
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

## Genesis 18:28

Greek: ἐὰν δὲ ἐλαττονωθῶσιν οἱ πεντήκοντα δίκαιοι εἰς τεσσαρακονταπέντε, ἀπολεῖς ἕνεκεν τῶν πέντε πᾶσαν τὴν πόλιν; καὶ εἶπεν· οὐ μὴ ἀπολέσω, ἐὰν εὕρω ἐκεῖ τεσσσαρακονταπέντε.
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

## Genesis 18:29

Greek: καὶ προσέθηκεν ἔτι λαλῆσαι πρὸς αὐτόν, καὶ εἶπεν· ἐὰν δὲ εὑρεθῶσιν ἐκεῖ τεσσαράκοντα; καὶ εἶπεν· οὐ μὴ ἀπολέσω ἕνεκεν τῶν τεσσαράκοντα.
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

## Genesis 18:30

Greek: καὶ εἶπε· μή τι κύριε, ἐὰν λαλήσω; ἐὰν δὲ εὑρεθῶσιν ἐκεῖ τριάκοντα; καὶ εἶπεν· οὐ μὴ ἀπολέσω ἕνεκεν τῶν τριάκοντα.
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

## Genesis 18:31

Greek: καὶ εἶπεν· ἐπειδὴ ἔχω λαλῆσαι πρὸς τὸν κύριον· ἐὰν δὲ εὑρεθῶσιν ἐκεῖ εἴκοσι; καὶ εἶπεν· οὐ μὴ ἀπολέσω, ἐὰν εὕρω ἐκεῖ εἴκοσι.
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

## Genesis 18:32

Greek: καὶ εἶπε· μήτι κύριε, ἐὰν λαλήσω ἔτι ἅπαξ· ἐὰν δὲ εὑρεθῶσιν ἐκεῖ δέκα; καὶ εἶπεν· οὐ μὴ ἀπολέσω ἕνεκεν τῶν δέκα.
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

## Genesis 18:33

Greek: ἀπῆλθε δὲ ὁ Κύριος, ὡς ἐπαύσατο λαλῶν τῷ ῾Αβραάμ, καὶ ῾Αβραὰμ ἀπέστρεψεν εἰς τὸν τόπον αὐτοῦ.
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

# Chapter 19

## Genesis 19:1

Greek: ΗΛΘΟΝ δὲ οἱ δύο ἄγγελοι εἰς Σόδομα ἑσπέρας· Λὼτ δὲ ἐκάθητο παρὰ τὴν πύλην Σοδόμων. ἰδὼν δὲ Λώτ, ἐξανέστη εἰς συνάντησιν αὐτοῖς καὶ προσεκύνησε τῷ προσώπῳ ἐπὶ τὴν γῆν.
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

## Genesis 19:2

Greek: καὶ εἶπεν· ἰδοὺ κύριοι, ἐκκλίνατε εἰς τὸν οἶκον τοῦ παιδὸς ὑμῶν καὶ καταλύσατε καὶ νίψασθε τοὺς πόδας ὑμῶν, καὶ ὀρθρίσαντες ἀπελεύσεσθε εἰς τὴν ὁδὸν ὑμῶν. καὶ εἶπαν· οὐχί, ἀλλ᾿ ἐν τῇ πλατείᾳ καταλύσομεν.
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

## Genesis 19:3

Greek: καὶ κατεβιάζετο αὐτούς, καὶ ἐξέκλιναν πρὸς αὐτὸν καὶ εἰσῆλθον εἰς τὸν οἶκον αὐτοῦ. καὶ ἐποίησεν αὐτοῖς πότον, καὶ ἀζύμους ἔπεψεν αὐτοῖς, καὶ ἔφαγον.
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

## Genesis 19:4

Greek: πρὸ τοῦ κοιμηθῆναι δέ, οἱ ἄνδρες τῆς πόλεως οἱ Σοδομῖται περικύκλωσαν τὴν οἰκίαν ἀπὸ νεανίσκου ἕως πρεσβυτέρου, ἅπας ὁ λαὸς ἅμα.
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

## Genesis 19:5

Greek: καὶ ἐξεκαλοῦντο τὸν Λὼτ καὶ ἔλεγον πρὸς αὐτόν· ποῦ εἰσιν οἱ ἄνδρες οἱ εἰσελθόντες πρὸς σὲ τὴν νύκτα; ἐξάγαγε αὐτοὺς πρὸς ἡμᾶς, ἵνα συγγενώμεθα αὐτοῖς.
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

## Genesis 19:6

Greek: ἐξῆλθε δὲ Λὼτ πρὸς αὐτοὺς πρὸς τὸ πρόθυρον, τὴν δὲ θύραν προσέῳξεν ὀπίσω αὐτοῦ.
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

## Genesis 19:7

Greek: εἶπε δὲ πρὸς αὐτούς· μηδαμῶς ἀδελφοί, μὴ πονηρεύσησθε.
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

## Genesis 19:8

Greek: εἰσὶ δέ μοι δύο θυγατέρες, αἳ οὐκ ἔγνωσαν ἄνδρα· ἐξάξω αὐτὰς πρὸς ὑμᾶς, καὶ χρᾶσθε αὐταῖς, καθὰ ἂν ἀρέσκῃ ὑμῖν· μόνον εἰς τοὺς ἀνδρας τούτους μὴ ποιήσητε ἄδικον, οὗ εἵνεκεν εἰσῆλθον ὑπὸ τὴν σκέπην τῶν δοκῶν μου.
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

## Genesis 19:9

Greek: εἶπαν δὲ αὐτῷ· ἀπόστα ἐκεῖ. εἰσῆλθες παροικεῖν· μὴ καὶ κρίσιν κρίνειν; νῦν οὖν σὲ κακώσωμεν μᾶλλον ἢ ἐκείνους. καὶ παρεβιάζοντο τὸν ἄνδρα τὸν Λὼτ σφόδρα. καὶ ἤγγισαν συντρίψαι τὴν θύραν.
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

## Genesis 19:10

Greek: ἐκτείναντες δὲ οἱ ἄνδρες τὰς χεῖρας εἰσεσπάσαντο τὸν Λὼτ πρὸς ἑαυτοὺς εἰς τὸν οἶκον, καὶ τὴν θύραν τοῦ οἴκου ἀπέκλεισαν·
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

## Genesis 19:11

Greek: τοὺς δὲ ἄνδρας τοὺς ὄντας ἐπὶ τῆς θύρας τοῦ οἴκου ἐπάταξαν ἐν ἀορασίᾳ ἀπὸ μικροῦ ἕως μεγάλου, καὶ παρελύθησαν ζητοῦντες τὴν θύραν.
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

## Genesis 19:12

Greek: Εἶπαν δὲ οἱ ἄνδρες ἢ πρὸς Λώτ· εἰσί σοι ὧδε γαμβροὶ ἢ υἱοὶ ἢ θυγατέρες; ἢ εἴτις σοι ἄλλος ἐστὶν ἐν τῇ πόλει, ἐξάγαγε ἐκ τοῦ τόπου τούτου·
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

## Genesis 19:13

Greek: ὅτι ἡμεῖς ἀπόλλυμεν τὸν τόπον τοῦτον, ὅτι ὑψώθη ἡ κραυγὴ αὐτῶν ἔναντι Κυρίου, καὶ ἀπέστειλεν ἡμᾶς Κύριος ἐκτρίψαι αὐτήν.
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

## Genesis 19:14

Greek: ἐξῆλθε δὲ Λὼτ καὶ ἐλάλησε πρὸς τοὺς γαμβροὺς αὐτοῦ τοὺς εἰληφότας τὰς θυγατέρας αὐτοῦ καὶ εἶπεν· ἀνάστητε καὶ ἐξέλθετε ἐκ τοῦ τόπου τούτου, ὅτι ἐκτρίβει Κύριος τὴν πόλιν. ἔδοξε δὲ γελοιάζειν ἐναντίον τῶν γαμβρῶν αὐτοῦ.
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

## Genesis 19:15

Greek: ἡνίκα δὲ ὄρθρος ἐγίνετο, ἐσπούδαζον οἱ ἄγγελοι τὸν Λὼτ λέγοντες· ἀναστὰς λάβε τὴν γυναῖκά σου καὶ τὰς δύο θυγατέρας σου, ἃς ἔχεις, καὶ ἔξελθε, ἵνα μὴ καὶ σὺ συναπόλῃ ταῖς ἀνομίαις τῆς πόλεως.
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

## Genesis 19:16

Greek: καὶ ἐταράχθησαν· καὶ ἐκράτησαν οἱ ἄγγελοι τῆς χειρὸς αὐτοῦ καὶ τῆς χειρὸς τῆς γυναικὸς αὐτοῦ καὶ τῶν χειρῶν τῶν δύο θυγατέρων αὐτοῦ, ἐν τῷ φείσασθαι Κύριον αὐτοῦ.
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

## Genesis 19:17

Greek: καὶ ἐγένετο, ἡνίκα ἐξήγαγον αὐτοὺς ἔξω καὶ εἶπαν· σῴζων σῷζε τὴν σεαυτοῦ ψυχήν· μὴ περιβλέψῃ εἰς τὰ ὀπίσω, μηδὲ στῇς ἐν πάσῃ τῇ περιχώρῳ· εἰς τὸ ὄρος σῴζου, μήποτε συμπαραληφθῇς.
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

## Genesis 19:18

Greek: εἶπε δὲ Λὼτ πρὸς αὐτούς· δέομαι κύριε,
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

## Genesis 19:19

Greek: ἐπειδὴ εὗρεν ὁ παῖς σου ἔλεος ἐναντίον σου καὶ ἐμεγάλυνας τὴν δικαιοσύνην σου, ὃ ποιεῖς ἐπ᾿ ἐμὲ τοῦ ζῆν τὴν ψυχήν μου, ἐγὼ δὲ οὐ δυνήσομαι διασωθῆναι εἰς τὸ ὄρος, μήποτε καταλάβῃ με τὰ κακὰ καὶ ἀποθάνω.
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

## Genesis 19:20

Greek: ἰδοὺ ἡ πόλις αὕτη ἐγγὺς τοῦ καταφυγεῖν με ἐκεῖ, ἥ ἐστι μικρά, καὶ ἐκεῖ διασωθήσομαι· οὐ μικρά ἐστι; καὶ ζήσεται ἡ ψυχή μου ἕνεκέν σου.
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

## Genesis 19:21

Greek: καὶ εἶπεν αὐτῷ· ἰδοὺ ἐθαύμασά σου τὸ πρόσωπον καὶ ἐπὶ τῷ ρήματι τούτῳ τοῦ μὴ καταστρέψαι τὴν πόλιν, περὶ ἧς ἐλάλησας·
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

## Genesis 19:22

Greek: σπεῦσον οὖν τοῦ σωθῆναι ἐκεῖ· οὐ γὰρ δυνήσομαι ποιῆσαι πρᾶγμα, ἕως τοῦ ἐλθεῖν σε ἐκεῖ. διὰ τοῦτο ἐκάλεσε τὸ ὄνομα τῆς πόλεως ἐκείνης Σηγώρ.
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

## Genesis 19:23

Greek: ὁ ἥλιος ἐξῆλθεν ἐπὶ τὴν γῆν, καὶ Λὼτ εἰσῆλθεν εἰς Σηγώρ,
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

## Genesis 19:24

Greek: καὶ Κύριος ἔβρεξεν ἐπὶ Σόδομα καὶ Γόμορρα θεῖον, καὶ πῦρ παρὰ Κυρίου ἐξ οὐρανοῦ
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

## Genesis 19:25

Greek: καὶ κατέστρεψε τὰς πόλεις ταύτας καὶ πᾶσαν τὴν περίχωρον καὶ πάντας τοὺς κατοικοῦντας ἐν ταῖς πόλεσι καὶ τὰ ἀνατέλλοντα ἐκ τῆς γῆς.
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

## Genesis 19:26

Greek: καὶ ἐπέβλεψεν ἡ γυνὴ αὐτοῦ εἰς τὰ ὀπίσω καὶ ἐγένετο στήλη ἁλός.
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

## Genesis 19:27

Greek: ῎Ωρθρισε δὲ ῾Αβραὰμ τῷ πρωΐ εἰς τὸν τόπον, οὗ εἱστήκει ἐναντίον Κυρίου.
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

## Genesis 19:28

Greek: καὶ ἐπέβλεψεν ἐπὶ πρόσωπον Σοδόμων καὶ Γομόρρας καὶ ἐπὶ πρόσωπον τῆς περιχώρου καὶ εἶδε, καὶ ἰδοὺ ἀνέβαινε φλὸξ ἐκ τῆς γῆς, ὡσεὶ ἀτμὶς καμίνου.
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

## Genesis 19:29

Greek: καὶ ἐγένετο ἐν τῷ ἐκτρίψαι Κύριον πάσας τὰς πόλεις τῆς περιοίκου, ἐμνήσθη ὁ Θεὸς τοῦ ῾Αβραὰμ καὶ ἐξαπέστειλε τὸν Λὼτ ἐκ μέσου τῆς καταστροφῆς, ἐν τῷ καταστρέψαι Κύριον τὰς πόλεις, ἐν αἷς κατῴκει ἐν αὐταῖς Λώτ.
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

## Genesis 19:30

Greek: ᾿Ανέβη δὲ Λὼτ ἐκ Σηγὼρ καὶ ἐκάθητο ἐν τῷ ὄρει αὐτὸς καὶ αἱ δύο θυγατέρες αὐτοῦ μετ᾿ αὐτοῦ· ἐφοβήθη γὰρ κατοικῆσαι ἐν Σηγώρ. καὶ κατῴκησεν ἐν τῷ σπηλαίῳ, αὐτὸς καὶ αἱ δύο θυγατέρες αὐτοῦ μετ᾿ αὐτοῦ.
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

## Genesis 19:31

Greek: εἶπε δὲ ἡ πρεσβυτέρα πρὸς τὴν νεωτέραν· ὁ πατὴρ ἡμῶν πρεσβύτερος, καὶ οὐδείς ἐστιν ἐπὶ τῆς γῆς, ὃς εἰσελεύσεται πρὸς ἡμᾶς, ὡς καθήκει πάσῃ τῇ γῇ·
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

## Genesis 19:32

Greek: δεῦρο καὶ ποτίσωμεν τὸν πατέρα ἡμῶν οἶνον καὶ κοιμηθῶμεν μετ᾿ αὐτοῦ καὶ ἐξαναστήσωμεν ἐκ τοῦ πατρὸς ἡμῶν σπέρμα.
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

## Genesis 19:33

Greek: ἐπότισαν δὲ τὸν πατέρα αὐτῶν οἶνον ἐν τῇ νυκτὶ ἐκείνῃ, καὶ εἰσελθοῦσα ἡ πρεσβυτέρα ἐκοιμήθη μετὰ τοῦ πατρὸς αὐτῆς ἐν τῇ νυκτὶ ἐκείνῃ, καὶ οὐκ ᾔδει ἐν τῷ κοιμηθῆναι αὐτὸν καὶ ἐν τῷ ἀναστῆναι.
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

## Genesis 19:34

Greek: ἐγένετο δὲ ἐν τῇ ἐπαύριον καὶ εἶπεν ἡ πρεσβυτέρα πρὸς τὴν νεωτέραν· ἰδοὺ ἐκοιμήθην χθὲς μετὰ τοῦ πατρὸς ἡμῶν· ποτίσωμεν αὐτὸν οἶνον καὶ ἐν τῇ νυκτὶ ταύτῃ, καὶ εἰσελθοῦσα κοιμήθητι μετ᾿ αὐτοῦ, καὶ ἐξαναστήσωμεν ἐκ τοῦ πατρὸς ἡμῶν σπέρμα.
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

## Genesis 19:35

Greek: ἐπότισαν δὲ καὶ ἐν τῇ νυκτὶ ἐκείνῃ τὸν πατέρα αὐτῶν οἶνον, καὶ εἰσελθοῦσα ἡ νεωτέρα ἐκοιμήθη μετὰ τοῦ πατρὸς αὐτῆς, καὶ οὐκ ᾔδει ἐν τῷ κοιμηθῆναι αὐτὸν καὶ ἀναστῆναι.
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

## Genesis 19:36

Greek: καὶ συνέλαβον αἱ δύο θυγατέρες Λὼτ ἐκ τοῦ πατρὸς αὐτῶν.
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

## Genesis 19:37

Greek: καὶ ἔτεκεν ἡ πρεσβυτέρα υἱὸν καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ Μωὰβ λέγουσα· ἐκ τοῦ πατρός μου· οὗτος πατὴρ Μωαβιτῶν ἕως τῆς σήμερον ἡμέρας.
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

## Genesis 19:38

Greek: ἔτεκε δὲ καὶ ἡ νεωτέρα υἱὸν καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ ᾿Αμμάν, λέγουσα· υἱὸς γένους μου· οὗτος πατὴρ ᾿Αμμανιτῶν ἕως τῆς σήμερον ἡμέρας.
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

# Chapter 20

## Genesis 20:1

Greek: ΚΑΙ ἐκίνησεν ἐκεῖθεν ῾Αβραὰμ εἰ γῆν πρὸς λίβα καὶ ᾤκησεν ἀνὰ μέσον Κάδης καὶ ἀνὰ μέσον Σούρ. καὶ παρῴκησεν ἐν Γεράροις.
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

## Genesis 20:2

Greek: εἶπε δὲ ῾Αβραὰμ περὶ Σάρρας τῆς γυναικὸς αὐτοῦ, ὅτι ἀδελφή μου ἐστίν· ἐφοβήθη γὰρ εἰπεῖν ὅτι γυνή μου ἐστί, μή ποτε ἀποκτείνωσιν αὐτὸν οἱ ἄνδρες τῆς πόλεως δι᾿ αὐτήν. ἀπέστειλε δὲ ᾿Αβιμέλεχ, βασιλεὺς Γεράρων, καὶ ἔλαβε τὴν Σάρραν.
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

## Genesis 20:3

Greek: καὶ εἰσῆλθεν ὁ Θεὸς πρὸς ᾿Αβιμέλεχ ἐν ὕπνῳ τὴν νύκτα καὶ εἶπεν· ἰδοὺ σὺ ἀποθνήσκεις περὶ τῆς γυναικός, ἧς ἔλαβες, αὕτη δέ ἐστι συνῳκηυῖα ἀνδρί.
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

## Genesis 20:4

Greek: ᾿Αβιμέλεχ δὲ οὐχ ἥψατο αὐτῆς καὶ εἶπε· Κύριε, ἔθνος ἀγνοοῦν καὶ δίκαιον ἀπολεῖς
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

## Genesis 20:5

Greek: οὐκ αὐτός μοι εἶπεν, ἀδελφή μου ἐστί; καὶ αὕτη μοι εἶπεν, ἀδελφός μου ἐστίν; ἐν καθαρᾷ καρδίᾳ καὶ ἐν δικαιοσύνῃ χειρῶν ἐποίησα τοῦτο.
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

## Genesis 20:6

Greek: λίγο εἶπε δὲ αὐτῷ ὁ Θεὸς καθ᾿ ὕπνον· κἀγὼ ἔγνων ὅτι ἐν καθαρᾷ καρδίᾳ ἐποίησας τοῦτο, καὶ ἐφεισάμην σου τοῦ μὴ ἁμαρτεῖν σε εἰς ἐμέ· ἕνεκα τούτου οὐκ ἀφῆκά σε ἅψασθαι αὐτῆς.
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

## Genesis 20:7

Greek: νῦν δὲ ἀπόδος τὴν γυναῖκα τῷ ἀνθρώπῳ, ὅτι προφήτης ἐστὶ καὶ προσεύξεται περὶ σοῦ καὶ ζήσῃ· εἰ δὲ μὴ ἀποδίδως, γνώσῃ ὅτι ἀποθανῇ σὺ καὶ πάντα τὰ σά.
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

## Genesis 20:8

Greek: καὶ ὤρθρισεν ᾿Αβιμέλεχ τῷ πρωΐ καὶ ἐκάλεσε πάντας τοὺς παῖδας αὐτοῦ καὶ ἐλάλησε πάντα τὰ ρήματα ταῦτα εἰς τὰ ὦτα αὐτῶν, ἐφοβήθησαν δὲ πάντες οἱ ἄνθρωποι σφόδρα.
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

## Genesis 20:9

Greek: καὶ ἐκάλεσεν ᾿Αβιμέλεχ τὸν ῾Αβραάμ, καὶ εἶπεν αὐτῷ· τί τοῦτο ἐποίησας ἡμῖν; μήτι ἡμάρτομεν εἰς σέ, ὅτι ἐπήγαγες ἐπ᾿ ἐμὲ καὶ ἐπὶ τὴν βασιλείαν μου ἁμαρτίαν μεγάλην; ἔργον, ὃ οὐδεὶς ποιήσει, πεποίηκάς μοι.
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

## Genesis 20:10

Greek: εἶπε δὲ ᾿Αβιμέλεχ τῷ ῾Αβραάμ· τί ἐνιδὼν ἐποίησας τοῦτο
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

## Genesis 20:11

Greek: εἶπε δὲ ῾Αβραάμ· εἶπα γάρ, ἄρα οὐκ ἔστι θεοσέβεια ἐν τῷ τόπῳ τούτῳ, ἐμέ τε ἀποκτενοῦσιν ἕνεκεν τῆς γυναικός μου.
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

## Genesis 20:12

Greek: καὶ γὰρ ἀληθῶς ἀδελφή μου ἐστὶν ἐκ πατρός, ἀλλ᾿ οὐκ ἐκ μητρός· ἐγενήθη δέ μοι εἰς γυναῖκα.
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

## Genesis 20:13

Greek: ἐγένετο δέ, ἡνίκα ἐξήγαγέ με ὁ Θεὸς ἐκ τοῦ οἴκου τοῦ πατρός μου, καὶ εἶπα αὐτῇ· ταύτην τὴν δικαιοσύνην ποιήσεις εἰς ἐμέ, εἰς πάντα τόπον οὗ ἐὰν εἰσέλθωμεν ἐκεῖ, εἰπὸν ἐμέ, ὅτι ἀδελφός μου ἐστίν.
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

## Genesis 20:14

Greek: ἔλαβε δὲ ᾿Αβιμέλεχ χίλια δίδραχμα καὶ πρόβατα καὶ μόσχους καὶ παῖδας καὶ παιδίσκας καὶ ἔδωκε τῷ ῾Αβραὰμ καὶ ἀπέδωκεν αὐτῷ Σάρραν τὴν γυναῖκα αὐτοῦ.
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

## Genesis 20:15

Greek: καὶ εἶπεν ᾿Αβιμέλεχ τῷ ῾Αβραάμ· ἰδοὺ ἡ γῆ μου ἐναντίον σου· οὗ ἐάν σοι ἀρέσκῃ, κατοίκει.
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

## Genesis 20:16

Greek: τῇ δὲ Σάρρᾳ εἶπεν· ἰδοὺ δέδωκα χίλια δίδραχμα τῷ ἀδελφῷ σου· ταῦτα ἔσται σοι εἰς τὴν τιμὴ τοῦ προσώπου σου καὶ πάσαις ταῖς μετὰ σοῦ· καὶ πάντα ἀλήθευσον.
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

## Genesis 20:17

Greek: προσηύξατο δὲ ῾Αβραὰμ πρὸς τὸν Θεόν, καὶ ἰάσατο ὁ Θεὸς τὸν ᾿Αβιμέλεχ καὶ τὴν γυναῖκα αὐτοῦ καὶ τὰς παιδίσκας αὐτοῦ, καὶ ἔτεκον·
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

## Genesis 20:18

Greek: ὅτι συγκλείων συνέκλεισε Κύριος ἔξωθεν πᾶσαν μήτραν ἐν τῷ οἴκῳ ᾿Αβιμέλεχ, ἕνεκεν Σάρρας τῆς γυναικὸς ῾Αβραάμ.
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

# Chapter 21

## Genesis 21:1

Greek: ΚΑΙ Κύριος ἐπεσκέψατο τὴν Σάρραν, καθὰ εἶπε, καὶ ἐποίησε Κύριος τῇ Σάρρᾳ καθὰ ἐλάλησε,
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

## Genesis 21:2

Greek: καὶ συλλαβοῦσα ἔτεκε τῷ ῾Αβραὰμ υἱὸν εἰς τὸ γῆρας, εἰς τὸν καιρόν, καθὰ ἐλάλησεν αὐτῷ Κύριος.
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

## Genesis 21:3

Greek: καὶ ἐκάλεσεν ῾Αβραὰμ τὸ ὄνομα τοῦ υἱοῦ αὐτοῦ τοῦ γενομένου αὐτῷ, ὃν ἔτεκεν αὐτῷ Σάρρα, ᾿Ισαάκ.
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

## Genesis 21:4

Greek: περιέτεμε δὲ ῾Αβραὰμ τὸν ᾿Ισαὰκ τῇ ἡμέρᾳ τῇ ὀγδόῃ, καθὰ ἐνετείλατο αὐτῷ ὁ Θεός.
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

## Genesis 21:5

Greek: καὶ ῾Αβραὰμ ἦν ἑκατὸν ἐτῶν, ἡνίκα ἐγένετο αὐτῷ ᾿Ισαὰκ ὁ υἱὸς αὐτοῦ.
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

## Genesis 21:6

Greek: εἶπε δὲ Σάρρα· γέλωτά μοι ἐποίησε Κύριος· ὃς γὰρ ἂν ἀκούσῃ, συγχαρεῖταί μοι.
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

## Genesis 21:7

Greek: καὶ εἶπε· τίς ἀναγγελεῖ τῷ ῾Αβραάμ, ὅτι θηλάζει παιδίον Σάρρα; ὅτι ἔτεκον υἱὸν ἐν τῷ γήρᾳ μου.
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

## Genesis 21:8

Greek: Καὶ ηὐξήθη τὸ παιδίον καὶ ἀπεγαλακτίσθη, καὶ ἐποίησεν ῾Αβραὰμ δοχὴν μεγάλην, ᾗ ἡμέρᾳ ἀπεγαλακτίσθη ᾿Ισαὰκ ὁ υἱὸς αὐτοῦ.
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

## Genesis 21:9

Greek: ἰδοῦσα δὲ Σάρρα τὸν υἱὸν ῎Αγαρ τῆς Αἰγυπτίας, ὃς ἐγένετο τῷ ῾Αβραάμ, παίζοντα μετὰ ᾿Ισαὰκ τοῦ υἱοῦ αὐτῆς·
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

## Genesis 21:10

Greek: καὶ εἶπε τῷ ῾Αβραάμ· ἔκβαλε τὴν παιδίσκην ταύτην καὶ τὸν υἱὸν αὐτῆς· οὐ γὰρ μὴ κληρονομήσει ὁ υἱὸς τῆς παιδίσκης ταύτης μετὰ τοῦ υἱοῦ μου ᾿Ισαάκ.
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

## Genesis 21:11

Greek: σκληρὸν δὲ ἐφάνη τὸ ρῆμα σφόδρα ἐναντίον ῾Αβραὰμ περὶ τοῦ υἱοῦ αὐτοῦ.
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

## Genesis 21:12

Greek: εἶπε δὲ ὁ Θεὸς τῷ ῾Αβραάμ· μὴ σκληρὸν ἔστω ἐναντίον σου περὶ τοῦ παιδίου καὶ περὶ τῆς παιδίσκης· πάντα ἂν ὅσα εἴπῃ σοι Σάρρα, ἄκουε τῆς φωνῆς αὐτῆς, ὅτι ἐν ᾿Ισαὰκ κληθήσεταί σοι σπέρμα.
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

## Genesis 21:13

Greek: καὶ τὸν υἱὸν δὲ τῆς παιδίσκης ταύτης εἰς ἔθνος μέγα ποιήσω αὐτόν, ὅτι σπέρμα σόν ἐστιν.
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

## Genesis 21:14

Greek: ἀνέστη δὲ ῾Αβραὰμ τὸ πρωΐ καὶ ἔλαβεν ἄρτους καὶ ἀσκὸν ὕδατος καὶ ἔδωκε τῇ ῎Αγαρ καὶ ἐπέθηκεν ἐπὶ τῶν ὤμων αὐτῆς τὸ παιδίον καὶ ἀπέστειλεν αὐτήν. ἀπελθοῦσα δὲ ἐπλανᾶτο κατὰ τὴν ἔρημον, κατὰ τὸ φρέαρ τοῦ ὅρκου.
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

## Genesis 21:15

Greek: ἐξέλιπε δὲ τὸ ὕδωρ ἐκ τοῦ ἀσκοῦ, καὶ ἔρριψε τὸ παιδίον ὑποκάτω μιᾶς ἐλάτης.
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

## Genesis 21:16

Greek: ἀπελθοῦσα δὲ ἐκάθητο ἀπέναντι αὐτοῦ μακρόθεν ὡσεὶ τόξου βολήν· εἶπε γάρ, οὐ μὴ ἴδω τὸν θάνατον τοῦ παιδίου μου. καὶ ἐκάθισεν ἀπέναντι αὐτοῦ, ἀναβοῆσαν δὲ τὸ παιδίον ἔκλαυσεν.
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

## Genesis 21:17

Greek: εἰσήκουσε δὲ ὁ Θεὸς τῆς φωνῆς τοῦ παιδίου ἐκ τοῦ τόπου, οὗ ἦν, καὶ ἐκάλεσεν ἄγγελος Θεοῦ τὴν ῎Αγαρ ἐκ τοῦ οὐρανοῦ καὶ εἶπεν αὐτῇ· τί ἐστιν ῎Αγαρ; μὴ φοβοῦ· ἐπακήκοε γὰρ ὁ Θεὸς τῆς φωνῆς τοῦ παιδίου ἐκ τοῦ τόπου, οὗ ἐστιν.
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

## Genesis 21:18

Greek: ἀνάστηθι καὶ λαβὲ τὸ παιδίον καὶ κράτησον τῇ χειρί σου αὐτό· εἰς γὰρ ἔθνος μέγα ποιήσω αὐτό.
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

## Genesis 21:19

Greek: καὶ ἀνέῳξεν ὁ Θεὸς τοὺς ὀφθαλμοὺς αὐτῆς, καὶ εἶδε φρέαρ ὕδατος ζῶντος καὶ ἐπορεύθη καὶ ἔπλησε τὸν ἀσκὸν ὕδατος καὶ ἐπότισε τὸ παιδίον.
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

## Genesis 21:20

Greek: καὶ ἦν ὁ Θεὸς μετὰ τοῦ παιδίου, καὶ ηὐξήθη. καὶ κατῴκησεν ἐν τῇ ἐρήμῳ, ἐγένετο δὲ τοξότης.
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

## Genesis 21:21

Greek: καὶ κατῴκησεν ἐν τῇ ἐρήμῳ τῇ Φαράν, καὶ ἔλαβεν αὐτῷ ἡ μήτηρ γυναῖκα ἐκ γῆς Αἰγύπτου.
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

## Genesis 21:22

Greek: ᾿Εγένετο δὲ ἐν τῷ καιρῷ ἐκείνῳ καὶ εἶπεν ᾿Αβιμέλεχ καὶ ῾Οχοζὰθ ὁ νυμφαγωγὸς αὐτοῦ καὶ Φιχὸλ ὁ ἀρχιστράτηγος τῆς δυνάμεως αὐτοῦ πρὸς ῾Αβραὰμ λέγων· ὁ Θεὸς μετὰ σοῦ ἐν πᾶσιν, οἷς ἐὰν ποιῇς·
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

## Genesis 21:23

Greek: νῦν οὖν ὄμοσόν μοι τὸν Θεόν, μὴ ἀδικήσειν με μηδὲ τὸ σπέρμα μου, μηδὲ τὸ ὄνομά μου· ἀλλὰ κατὰ τὴν δικαιοσύνην, ἣν ἐποίησα μετὰ σοῦ, ποιήσεις μετ᾿ ἐμοῦ, καὶ τῇ γῇ, ᾗ σὺ παρῴκησας ἐν αὐτῇ.
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

## Genesis 21:24

Greek: καὶ εἶπεν ῾Αβραάμ· ἐγὼ ὀμοῦμαι.
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

## Genesis 21:25

Greek: καὶ ἤλεγξεν ῾Αβραὰμ τὸν ᾿Αβιμέλεχ περὶ τῶν φρεάτων τοῦ ὕδατος, ὧν ἀφείλοντο οἱ παῖδες τοῦ ᾿Αβιμέλεχ.
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

## Genesis 21:26

Greek: καὶ εἶπεν αὐτῷ ᾿Αβιμέλεχ· οὐκ ἔγνων τίς ἐποίησέ σοι τὸ ρῆμα τοῦτο, οὐδὲ σύ μοι ἀπήγγειλας, οὐδὲ ἐγὼ ἤκουσα, ἀλλ᾿ ἢ σήμερον.
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

## Genesis 21:27

Greek: καὶ ἔλαβεν ῾Αβραὰμ πρόβατα καὶ μόσχους, καὶ ἔδωκε τῷ ᾿Αβιμέλεχ, καὶ διέθεντο ἀμφότεροι διαθήκην.
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

## Genesis 21:28

Greek: καὶ ἔστησεν ῾Αβραὰμ ἑπτὰ ἀμνάδας προβάτων μόνας.
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

## Genesis 21:29

Greek: καὶ εἶπεν ᾿Αβιμέλεχ τῷ ῾Αβραάμ· τί εἰσιν αἱ ἑπτὰ ἀμνάδες τῶν προβάτων τούτων, ἃς ἔστησας μόνας
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

## Genesis 21:30

Greek: καὶ εἶπεν ῾Αβραάμ, ὅτι τὰς ἑπτὰ ἀμνάδας λήψῃ παρ᾿ ἐμοῦ, ἵνα ὦσί μοι εἰς μαρτύριον, ὅτι ἐγὼ ὤρυξα τὸ φρέαρ τοῦτο.
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

## Genesis 21:31

Greek: διὰ τοῦτο ἐπωνόμασε τὸ ὄνομα τοῦ τόπου ἐκείνου, Φρέαρ ὁρκισμοῦ, ὅτι ἐκεῖ ὤμοσαν ἀμφότεροι.
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

## Genesis 21:32

Greek: καὶ διέθεντο διαθήκην ἐν τῷ φρέατι τοῦ ὁρκισμοῦ. ἀνέστη δὲ ᾿Αβιμέλεχ καὶ ῾Οχοζὰθ ὁ νυμφαγωγὸς αὐτοῦ καὶ Φιχὸλ ὁ ἀρχιστράτητος τῆς δυνάμεως αὐτοῦ, καὶ ἐπέστρεψαν εἰς τὴν γῆν τῶν Φυλιστιείμ.
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

## Genesis 21:33

Greek: καὶ ἐφύτευσεν· ῾Αβραὰμ ἄρουραν ἐπὶ τῷ φρέατι τοῦ ὅρκου καὶ ἐπεκαλέσατο ἐκεῖ τὸ ὄνομα Κυρίου, Θεὸς αἰώνιος.
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

## Genesis 21:34

Greek: παρῴκησε δὲ ῾Αβραὰμ ἐν τῇ γῇ τῶν Φυλιστιεὶμ ἡμέρας πολλάς.
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

# Chapter 22

## Genesis 22:1

Greek: ΚΑΙ ἐγένετο μετὰ τὰ ρήματα ταῦτα ὁ Θεός ἐπείρασε τὸν ῾Αβραὰμ καὶ εἶπεν αὐτῷ· ῾Αβραάμ, ῾Αβραάμ. ὁ δὲ εἶπεν· ἰδοὺ ἐγώ.
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

## Genesis 22:2

Greek: καὶ εἶπε· λαβὲ τὸν υἱόν σου τὸν ἀγαπητόν, ὃν ἠγάπησας, τὸν ᾿Ισαάκ, καὶ πορεύθητι εἰς τὴν γῆν τὴν ὑψηλὴν καὶ ἀνένεγκον αὐτὸν ἐκεῖ εἰς ὁλοκάρπωσιν ἐφ᾿ ἓν τῶν ὀρέων, ὧν ἄν σοι εἴπω.
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

## Genesis 22:3

Greek: ἀναστὰς δὲ ῾Αβραὰμ τὸ πρωΐ ἐπέσαξε τὴν ὄνον αὐτοῦ· παρέλαβε δὲ μεθ᾿ ἑαυτοῦ δύο παῖδας καὶ ᾿Ισαὰκ τὸν υἱὸν αὐτοῦ καὶ σχίσας ξύλα εἰς ὁλοκάρπωσιν, ἀναστὰς ἐπορεύθη καὶ ἦλθεν ἐπὶ τὸν τόπον, ὃν εἶπεν αὐτῷ ὁ Θεός, τῇ ἡμέρᾳ τῇ τρίτῃ.
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

## Genesis 22:4

Greek: καὶ ἀναβλέψας ῾Αβραὰμ τοῖς ὀφθαλμοῖς αὐτοῦ, εἶδε τὸν τόπον μακρόθεν.
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

## Genesis 22:5

Greek: καὶ εἶπεν ῾Αβραὰμ τοῖς παισὶν αὐτοῦ· καθίσατε αὐτοῦ μετὰ τῆς ὄνου, ἐγὼ δὲ καὶ τὸ παιδάριον διελευσόμεθα ἕως ὧδε καὶ προσκυνήσαντες ἀναστρέψομεν πρὸς ὑμᾶς.
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

## Genesis 22:6

Greek: ἔλαβε δὲ ῾Αβραὰμ τὰ ξύλα τῆς ὁλοκαρπώσεως καὶ ἐπέθηκεν ᾿Ισαὰκ τῷ υἱῷ αὐτοῦ· ἔλαβε δὲ μετὰ χεῖρας καὶ τὸ πῦρ καὶ τὴν μάχαιραν, καὶ ἐπορεύθησαν οἱ δύο ἅμα.
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

## Genesis 22:7

Greek: εἶπε δὲ ᾿Ισαὰκ πρὸς ῾Αβραὰμ τὸν πατέρα αὐτοῦ· πάτερ. ὁ δὲ εἶπε· τί ἐστι, τέκνον; εἶπε δέ· ἰδοὺ τὸ πῦρ καὶ τὰ ξύλα· ποῦ ἐστι τὸ πρόβατον τὸ εἰς ὁλοκάρπωσιν
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

## Genesis 22:8

Greek: εἶπε δὲ ῾Αβραάμ· ὁ Θεὸς ὄψεται ἑαυτῷ πρόβατον εἰς ὁλοκάρπωσιν, τέκνον. πορευθέντες δὲ ἀμφότεροι ἅμα,
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

## Genesis 22:9

Greek: ἦλθον ἐπὶ τὸν τόπον, ὃν εἶπεν αὐτῷ ὁ Θεός. καὶ ᾠκοδόμησεν ἐκεῖ ῾Αβραὰμ τὸ θυσιαστήριον καὶ ἐπέθηκε τὰ ξύλα, καὶ συμποδίσας ᾿Ισαὰκ τὸν υἱὸν αὐτοῦ, ἐπέθηκεν αὐτὸν ἐπὶ τὸ θυσιαστήριον ἐπάνω τῶν ξύλων.
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

## Genesis 22:10

Greek: καὶ ἐξέτεινεν ῾Αβραὰμ τὴν χεῖρα αὐτοῦ λαβεῖν τὴν μάχαιραν σφάξαι τὸν υἱὸν αὐτοῦ.
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

## Genesis 22:11

Greek: καὶ ἐκάλεσεν αὐτὸν ἄγγελος Κυρίου ἐκ τοῦ οὐρανοῦ καὶ εἶπεν· ῾Αβραάμ, ῾Αβραάμ. ὁ δὲ εἶπεν· ἰδοὺ ἐγώ.
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

## Genesis 22:12

Greek: καὶ εἶπε· μὴ ἐπιβάλῃς τὴν χεῖρά σου ἐπὶ τὸ παιδάριον μηδὲ ποιήσῃς αὐτῷ μηδέν· νῦν γὰρ ἔγνων, ὅτι φοβῇ σὺ τὸν Θεὸν καὶ οὐκ ἐφείσω τοῦ υἱοῦ σου τοῦ ἀγαπητοῦ δι᾿ ἐμέ.
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

## Genesis 22:13

Greek: καὶ ἀναβλέψας ῾Αβραὰμ τοῖς ὀφθαλμοῖς αὐτοῦ εἶδε, καὶ ἰδοὺ κριὸς εἷς κατεχόμενος ἐν φυτῷ Σαβὲκ τῶν κεράτων· καὶ ἐπορεύθη ῾Αβραὰμ καὶ ἔλαβε τὸν κριὸν καὶ ἀνήνεγκεν αὐτὸν εἰς ὁλοκάρπωσιν ἀντὶ ᾿Ισαὰκ τοῦ υἱοῦ αὐτοῦ.
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

## Genesis 22:14

Greek: καὶ ἐκάλεσεν ῾Αβραὰμ τὸ ὄνομα τοῦ τόπου ἐκείνου, Κύριος εἶδεν, ἵνα εἴπωσι σήμερον, ἐν τῷ ὄρει Κύριος ὤφθη.
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

## Genesis 22:15

Greek: καὶ ἐκάλεσεν ἄγγελος Κυρίου τὸν ῾Αβραὰμ δεύτερον ἐκ τοῦ οὐρανοῦ, λέγων·
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

## Genesis 22:16

Greek: κατ᾿ ἐμαυτοῦ ὤμοσα, λέγει Κύριος, οὗ εἵνεκεν ἐποίησας τὸ ρῆμα τοῦτο, καὶ οὐκ ἐφείσω τοῦ υἱοῦ σου τοῦ ἀγαπητοῦ δι᾿ ἐμέ,
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

## Genesis 22:17

Greek: ἦ μὴν εὐλογῶν εὐλογήσω σε, καὶ πληθύνων πληθυνῶ τὸ σπέρμα σου, ὡς τοὺς ἀστέρας τοῦ οὐρανοῦ καὶ ὡς τὴν ἄμμον τὴν παρὰ τὸ χεῖλος τῆς θαλάσσης, καὶ κληρονομήσει τὸ σπέρμα σου τὰς πόλεις τῶν ὑπεναντίων·
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

## Genesis 22:18

Greek: καὶ ἐνευλογηθήσονται ἐν τῷ σπέρματί σου πάντα τὰ ἔθνη τῆς γῆς, ἀνθ᾿ ὧν ὑπήκουσας τῆς ἐμῆς φωνῆς.
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

## Genesis 22:19

Greek: ἀπεστράφη δὲ ῾Αβραὰμ πρὸς τοὺς παῖδας αὐτοῦ, καὶ ἀναστάντες ἐπορεύθησαν ἅμα ἐπὶ τὸ φρέαρ τοῦ ὅρκου. καὶ κατῴκησεν ῾Αβραὰμ ἐπὶ τὸ φρέαρ τοῦ ὅρκου.
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

## Genesis 22:20

Greek: ᾿Εγένετο δὲ μετὰ τὰ ρήματα ταῦτα καὶ ἀνηγγέλη τῷ ῾Αβραὰμ λέγοντες· ἰδοὺ τέτοκε Μελχὰ καὶ αὐτὴ υἱοὺς τῷ Ναχὼρ τῷ ἀδελφῷ σου,
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

## Genesis 22:21

Greek: τὸν Οὒζ πρωτότοκον καὶ τὸν Βαὺξ ἀδελφὸν αὐτοῦ καὶ τὸν Καμουὴλ πατέρα Σύρων
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

## Genesis 22:22

Greek: καὶ τὸν Χαζὰδ καὶ ᾿Αζαῦ καὶ τὸν Φαλδὲς καὶ τὸν ᾿Ιελδὰφ καὶ τὸν Βαθουήλ·
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

## Genesis 22:23

Greek: Βαθουὴλ δὲ ἐγέννησε τὴν Ρεβέκκαν. ὀκτὼ οὗτοι υἱοί, οὓς ἔτεκε Μελχὰ τῷ Ναχὼρ τῷ ἀδελφῷ ῾Αβραάμ.
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

## Genesis 22:24

Greek: καὶ ἡ παλλακὴ αὐτοῦ, ᾗ ὄνομα Ρεημά, ἔτεκε καὶ αὐτὴ τὸν Ταβὲκ καὶ τὸν Ταὰμ καὶ τὸν Τοχὸς καὶ τὸν Μοχά.
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

# Chapter 23

## Genesis 23:1

Greek: ΕΓΕΝΕΤΟ δὲ ἡ ζωὴ Σάρρας ἔτη ἑκατὸν εἰκοσιεπτά.
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

## Genesis 23:2

Greek: καὶ ἀπέθανε Σάρρα ἐν πόλει ᾿Αρβόκ, ἥ ἐστιν ἐν τῷ κοιλώματι (αὕτη ἐστὶ Χεβρών) ἐν τῇ γῇ Χαναάν. ἦλθε δὲ ῾Αβραὰμ κόψασθαι Σάρραν καὶ πενθῆσαι.
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

## Genesis 23:3

Greek: καὶ ἀνέστη ῾Αβραὰμ ἀπὸ τοῦ νεκροῦ αὐτοῦ καὶ εἶπεν ῾Αβραὰμ τοῖς υἱοῖς τοῦ Χὲτ λέγων·
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

## Genesis 23:4

Greek: πάροικος καὶ παρεπίδημος ἐγώ εἰμι μεθ᾿ ὑμῶν· δότε μοι οὖν κτῆσιν τάφου μεθ᾿ ὑμῶν, καὶ θάψω τὸν νεκρόν μου ἀπ᾿ ἐμοῦ.
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

## Genesis 23:5

Greek: ἀπεκρίθησαν δὲ οἱ υἱοὶ Χὲτ πρὸς ῾Αβραὰμ λέγοντες· μὴ κύριε·
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

## Genesis 23:6

Greek: ἄκουσον δὲ ἡμῶν. βασιλεὺς παρὰ Θεοῦ σὺ εἶ ἐν ἡμῖν· ἐν τοῖς ἐκλεκτοῖς μνημείοις ἡμῶν θάψον τὸν νεκρόν σου· οὐδεὶς γὰρ ἡμῶν οὐ μὴ κωλύσει τὸ μνημεῖον αὐτοῦ ἀπὸ σοῦ τοῦ θάψαι τὸν νεκρόν σου ἐκεῖ.
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

## Genesis 23:7

Greek: ἀναστὰς δὲ ῾Αβραὰμ προσεκύνησε τῷ λαῷ τῆς γῆς, τοῖς υἱοῖς τοῦ Χέτ,
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

## Genesis 23:8

Greek: καὶ ἐλάλησε πρὸς αὐτοὺς ῾Αβραὰμ λέγων· εἰ ἔχετε τῇ ψυχῇ ὑμῶν, ὥστε θάψαι τὸν νεκρόν μου ἀπὸ προσώπου μου, ἀκούσατέ μου καὶ λαλήσατε περὶ ἐμοῦ ᾿Εφρὼν τῷ τοῦ Σαάρ,
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

## Genesis 23:9

Greek: καὶ δότω μοι τὸ σπήλαιον τὸ διπλοῦν, ὅ ἐστιν αὐτῷ, τὸ ὂν ἐν μέρει τοῦ ἀγροῦ αὐτοῦ· ἀργυρίου τοῦ ἀξίου δότω μοι αὐτὸ ἐν ὑμῖν εἰς κτῆσιν μνημείου.
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

## Genesis 23:10

Greek: ᾿Εφρὼν δὲ ἐκάθητο ἐν μέσῳ τῶν υἱῶν Χέτ· ἀποκριθεὶς δὲ ᾿Εφρὼν ὁ Χετταῖος πρὸς ῾Αβραὰμ εἶπεν, ἀκουόντων τῶν υἱῶν Χὲτ καὶ τῶν εἰσπορευομένων εἰς τὴν πόλιν πάντων, λέγων·
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

## Genesis 23:11

Greek: παρ᾿ ἐμοὶ γενοῦ, κύριε, καὶ ἄκουσόν μου· τὸν ἀγρὸν καὶ τὸ σπήλαιον τὸ ἐν αὐτῷ σοὶ δίδωμι· ἐναντίον πάντων τῶν πολιτῶν μου δέδωκά σοι· θάψον τὸν νεκρόν σου·
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

## Genesis 23:12

Greek: καὶ προσεκύνησεν ῾Αβραὰμ ἐναντίον τοῦ λαοῦ τῆς γῆς
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

## Genesis 23:13

Greek: καὶ εἶπε τῷ ᾿Εφρὼν εἰς τὰ ὦτα ἐναντίον τοῦ λαοῦ τῆς γῆς· ἐπειδὴ πρὸς ἐμοῦ εἶ, ἄκουσόν μου· τὸ ἀργύριον τοῦ ἀγροῦ λάβε παρ᾿ ἐμοῦ, καὶ θάψω τὸν νεκρόν μου ἐκεῖ.
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

## Genesis 23:14

Greek: ἀπεκρίθη δὲ ᾿Εφρὼν τῷ ᾿Αβραὰμ λέγων·
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

## Genesis 23:15

Greek: οὐχὶ κύριε, ἀκήκοα γάρ, γῆ τετρακοσίων διδράχμων ἀργυρίου, ἀλλὰ τί ἂν εἴη τοῦτο ἀνὰ μέσον ἐμοῦ καὶ σοῦ; σὺ δὲ τὸν νεκρόν σου θάψον.
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

## Genesis 23:16

Greek: καὶ ἤκουσεν ῾Αβραὰμ τοῦ ᾿Εφρών, καὶ ἀποκατέστησεν ῾Αβραὰμ τῷ ᾿Εφρὼν τὸ ἀργύριον, ὃ ἐλάλησεν εἰς τὰ ὦτα τῶν υἱῶν Χέτ, τετρακόσια δίδραχμα ἀργυρίου δοκίμου ἐμπόροις.
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

## Genesis 23:17

Greek: καὶ ἔστη ὁ ἀγρὸς ᾿Εφρών, ὃς ἦν ἐν τῷ διπλῷ σπηλαίῳ, ὅς ἐστι κατὰ πρόσωπον Μαμβρῆ, ὁ ἀγρὸς καὶ τὸ σπήλαιον, ὃ ἦν ἐν αὐτῷ, καὶ πᾶν δένδρον, ὃ ἦν ἐν τῷ ἀγρῷ, καὶ πᾶν ὅ ἐστιν ἐν τοῖς ὁρίοις αὐτοῦ κύκλῳ,
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

## Genesis 23:18

Greek: τῷ ῾Αβραάμ, εἰς κτῆσιν ἐναντίον τῶν υἱῶν Χὲτ καὶ πάντων τῶν εἰσπορευομένων εἰς τὴν πόλιν.
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

## Genesis 23:19

Greek: μετὰ ταῦτα ἔθαψεν ῾Αβραὰμ Σάρραν τὴν γυναῖκα αὐτοῦ ἐν τῷ σπηλαίῳ τοῦ ἀγροῦ τῷ διπλῷ, ὅ ἐστιν ἀπέναντι Μαμβρῆ (αὕτη ἐστὶ Χεβρών) ἐν τῇ γῇ Χαναάν.
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

## Genesis 23:20

Greek: καὶ ἐκυρώθη ὁ ἀγρὸς καὶ τὸ σπήλαιον, ὃ ἦν ἐν αὐτῷ, τῷ ῾Αβραὰμ εἰς κτῆσιν τάφου παρὰ τῶν υἱῶν Χέτ.
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

# Chapter 24

## Genesis 24:1

Greek: ΚΑΙ ῾Αβραὰμ ἦν πρεσβύτερος προβεβηκὼς ἡμερῶν, καὶ ὁ Κύριος ηὐλόγησε τὸν ῾Αβραὰμ κατὰ πάντα.
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

## Genesis 24:2

Greek: καὶ εἶπεν ῾Αβραὰμ τῷ παιδὶ αὐτοῦ τῷ πρεσβυτέρῳ τῆς οἰκίας αὐτοῦ τῷ ἄρχοντι πάντων τῶν αὐτοῦ· θὲς τὴν χεῖρά σου ὑπὸ τὸν μηρόν μου,
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

## Genesis 24:3

Greek: καὶ ἐξορκιῶ σε Κύριον τὸν Θεὸν τοῦ οὐρανοῦ καὶ τὸν Θεὸν τῆς γῆς, ἵνα μὴ λάβῃς γυναῖκα τῷ υἱῷ μου ᾿Ισαὰκ ἀπὸ τῶν θυγατέρων τῶν Χαναναίων, μεθ᾿ ὧν ἐγὼ οἰκῶ ἐν αὐτοῖς,
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

## Genesis 24:4

Greek: ἀλλ᾿ ἢ εἰς τὴν γῆν μου, οὗ ἐγεννήθην, πορεύσῃ καὶ εἰς τὴν φυλήν μου καὶ λήψῃ γυναῖκα τῷ υἱῷ μου ᾿Ισαὰκ ἐκεῖθεν.
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

## Genesis 24:5

Greek: εἶπε δὲ πρὸς αὐτὸν ὁ παῖς· μή ποτε οὐ βούληται ἡ γυνὴ πορευθῆναι μετ᾿ ἐμοῦ ὀπίσω εἰς τὴν γῆν ταύτην· ἀποστρέψω τὸν υἱόν σου εἰς τὴν γῆν, ὅθεν ἐξῆλθες ἐκεῖθεν
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

## Genesis 24:6

Greek: εἶπε δὲ πρὸς αὐτὸν ῾Αβραάμ· πρόσεχε σεαυτῷ, μὴ ἀποστρέψῃς τὸν υἱόν μου ἐκεῖ.
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

## Genesis 24:7

Greek: Κύριος ὁ Θεὸς τοῦ οὐρανοῦ καὶ ὁ Θεὸς τῆς γῆς, ὃς ἔλαβέ με ἐκ τοῦ οἴκου τοῦ πατρός μου καὶ ἐκ τῆς γῆς, ἧς ἐγεννήθην, ὃς ἐλάλησέ μοι καὶ ὃς ὤμοσέ μοι λέγων· σοὶ δώσω τὴν γῆν ταύτην καὶ τῷ σπέρματί σου, αὐτὸς ἀποστελεῖ τὸν ἄγγελον αὐτοῦ ἔμπροσθέν σου. καὶ λήψῃ γυναῖκα τῷ υἱῷ μου ἐκεῖθεν.
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

## Genesis 24:8

Greek: ἐὰν δὲ μὴ θέλῃ ἡ γυνὴ πορευθῆναι μετὰ σοῦ εἰς τὴν γῆν ταύτην, καθαρὸς ἔσῃ ἀπὸ τοῦ ὅρκου μου· μόνον τὸν υἱόν μου μὴ ἀποστρέψῃς ἐκεῖ.
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

## Genesis 24:9

Greek: καὶ ἔθηκεν ὁ παῖς τὴν χεῖρα αὐτοῦ ὑπὸ τὸν μηρὸν ῾Αβραὰμ τοῦ κυρίου αὐτοῦ καὶ ὤμοσεν αὐτῷ περὶ τοῦ ρήματος τούτου.
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

## Genesis 24:10

Greek: Καὶ ἔλαβεν ὁ παῖς δέκα καμήλους ἀπὸ τῶν καμήλων τοῦ κυρίου αὐτοῦ καὶ ἀπὸ πάντων τῶν ἀγαθῶν τοῦ κυρίου αὐτοῦ μεθ᾿ ἑαυτοῦ καὶ ἀναστὰς ἐπορεύθη εἰς τὴν Μεσοποταμίαν εἰς τὴν πόλιν Ναχώρ.
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

## Genesis 24:11

Greek: καὶ ἐκοίμισε τὰς καμήλους ἔξω τῆς πόλεως παρὰ τὸ φρέαρ τοῦ ὕδατος τὸ πρὸς ὀψέ, ἡνίκα ἐκπορεύονται αἱ ὑδρευόμεναι.
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

## Genesis 24:12

Greek: καὶ εἶπε· Κύριε ὁ Θεὸς τοῦ κυρίου μου ῾Αβραάμ, εὐόδωσον ἐναντίον ἐμοῦ σήμερον καὶ ποίησον ἔλεος μετὰ τοῦ κυρίου μου ῾Αβραάμ.
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

## Genesis 24:13

Greek: ἰδοὺ ἐγὼ ἕστηκα ἐπὶ τῆς πηγῆς τοῦ ὕδατος, αἱ δὲ θυγατέρες τῶν οἰκούντων τὴν πόλιν ἐκπορεύονται ἀντλῆσαι ὕδωρ,
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

## Genesis 24:14

Greek: καὶ ἔσται ἡ παρθένος, ᾗ ἂν ἐγὼ εἴπω, ἐπίκλινον τὴν ὑδρίαν σου, ἵνα πίω, καὶ εἴπῃ μοι, πίε σύ, καὶ τὰς καμήλους σου ποτιῶ, ἕως ἂν παύσωνται πίνουσαι, ταύτην ἡτοίμασας τῷ παιδί σου τῷ ᾿Ισαάκ, καὶ ἐν τούτῳ γνώσομαι ὅτι ἐποίησας ἔλεος μετὰ τοῦ κυρίου μου ῾Αβραάμ.
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

## Genesis 24:15

Greek: καὶ ἐγένετο πρὸ τοῦ συντελέσαι αὐτὸν λαλοῦντα ἐν τῇ διανοίᾳ αὐτοῦ, καὶ ἰδοὺ Ρεβέκκα ἐξεπορεύετο ἡ τεχθεῖσα Βαθουήλ, υἱῷ Μελχὰς τῆς γυναικὸς Ναχώρ, ἀδελφοῦ δὲ ῾Αβραάμ, ἔχουσα τὴν ὑδρίαν ἐπὶ τῶν ὤμων αὐτῆς.
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

## Genesis 24:16

Greek: ἡ δὲ παρθένος ἦν καλὴ τῇ ὄψει σφόδρα· παρθένος ἦν, ἀνὴρ οὐκ ἔγνω αὐτήν. καταβᾶσα δὲ ἐπὶ τὴν πηγὴν ἔπλησε τὴν ὑδρίαν αὐτῆς καὶ ἀνέβη.
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

## Genesis 24:17

Greek: ἐπέδραμε δὲ ὁ παῖς εἰς συνάντησιν αὐτῆς καὶ εἶπε· πότισόν με μικρὸν ὕδωρ ἐκ τῆς ὑδρίας σου.
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

## Genesis 24:18

Greek: ἡ δὲ εἶπε· πίε, κύριε. καὶ ἔσπευσε καὶ καθεῖλε τὴν ὑδρίαν ἐπὶ τὸν βραχίονα αὐτῆς καὶ ἐπότισεν αὐτόν, ἕως ἐπαύσατο πίνων.
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

## Genesis 24:19

Greek: καὶ εἶπε· καὶ ταῖς καμήλοις σου ὑδρεύσομαι, ἕως ἂν πᾶσαι πίωσι.
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

## Genesis 24:20

Greek: καὶ ἔσπευσε καὶ ἐξεκένωσε τὴν ὑδρίαν εἰς τὸ ποτιστήριον καὶ ἔδραμεν ἐπὶ τὸ φρέαρ ἀντλῆσαι πάλιν καὶ ὑδρεύσατο πάσαις ταῖς καμήλοις.
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

## Genesis 24:21

Greek: ὁ δὲ ἄνθρωπος κατεμάνθανεν αὐτὴν καὶ παρεσιώπα τοῦ γνῶναι, εἰ εὐώδωκε Κύριος τὴν ὁδὸν αὐτοῦ ἢ οὔ.
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

## Genesis 24:22

Greek: ἐγένετο δέ, ἡνίκα ἐπαύσαντο πᾶσαι αἱ κάμηλοι πίνουσαι, ἔλαβεν ὁ ἄνθρωπος ἐνώτια χρυσᾶ ἀνὰ δραχμὴν ὁλκῆς καὶ δύο ψέλλια ἐπὶ τὰς χεῖρας αὐτῆς, δέκα χρυσῶν ὁλκὴ αὐτῶν.
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

## Genesis 24:23

Greek: καὶ ἐπηρώτησεν αὐτὴν καὶ εἶπε· θυγάτηρ τίνος εἶ; ἀνάγγειλόν μοι, εἰ ἔστι παρὰ τῷ πατρί σου τόπος ἡμῖν τοῦ καταλῦσαι.
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

## Genesis 24:24

Greek: ἡ δὲ εἶπεν αὐτῷ· θυγάτηρ Βαθουήλ εἰμι τοῦ Μελχάς, ὃν ἔτεκε τῷ Ναχώρ.
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

## Genesis 24:25

Greek: καὶ εἶπεν αὐτῷ· καὶ ἄχυρα καὶ χορτάσματα πολλὰ παρ᾿ ἡμῖν καὶ τόπος τοῦ καταλῦσαι.
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

## Genesis 24:26

Greek: καὶ εὐδοκήσας ὁ ἄνθρωπος προσεκύνησε τῷ Κυρίῳ καὶ εἶπεν·
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

## Genesis 24:27

Greek: εὐλογητὸς Κύριος ὁ Θεὸς τοῦ κυρίου μου ῾Αβραάμ, ὃς οὐκ ἐγκατέλιπε τὴν δικαιοσύνην αὐτοῦ καὶ τὴν ἀλήθειαν ἀπὸ τοῦ κυρίου μου· ἐμέ τε εὐώδωκε Κύριος εἰς οἶκον τοῦ ἀδελφοῦ τοῦ κυρίου μου.
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

## Genesis 24:28

Greek: Καὶ δραμοῦσα ἡ παῖς ἀνήγγειλεν εἰς τὸν οἶκον τῆς μητρὸς αὐτῆς κατὰ τὰ ρήματα ταῦτα.
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

## Genesis 24:29

Greek: τῇ δὲ Ρεβέκκᾳ ἀδελφὸς ἦν ᾧ ὄνομα Λάβαν· καὶ ἔδραμε Λάβαν πρὸς τὸν ἄνθρωπον ἔξω ἐπὶ τὴν πηγήν.
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

## Genesis 24:30

Greek: καὶ ἐγένετο ἡνίκα εἶδε τὰ ἐνώτια καὶ τὰ ψέλλια ἐν ταῖς χερσὶ τῆς ἀδελφῆς αὐτοῦ καὶ ὅτε ἤκουσε τὰ ρήματα Ρεβέκκας τῆς ἀδελφῆς αὐτοῦ λεγούσης· οὕτω λελάληκέ μοι ὁ ἄνθρωπος, καὶ ἦλθε πρὸς τὸν ἄνθρωπον ἑστηκότος αὐτοῦ ἐπὶ τῶν καμήλων ἐπὶ τῆς πηγῆς
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

## Genesis 24:31

Greek: καὶ εἶπεν αὐτῷ· δεῦρο εἴσελθε· εὐλογητὸς Κυρίου· ἱνατί ἕστηκας ἔξω; ἐγὼ δὲ ἡτοίμασα τὴν οἰκίαν καὶ τόπον ταῖς καμήλοις.
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

## Genesis 24:32

Greek: εἰσῆλθε δὲ ὁ ἄνθρωπος εἰς τὴν οἰκίαν καὶ ἀπέσαξε τὰς καμήλους καὶ ἔδωκεν ἄχυρα καὶ χορτάσματα ταῖς καμήλοις καὶ ὕδωρ νίψασθαι τοῖς ποσὶν αὐτοῦ καὶ τοῖς ποσὶ τῶν ἀνδρῶν τῶν μετ᾿ αὐτοῦ.
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

## Genesis 24:33

Greek: καὶ παρέθηκεν αὐτοῖς ἄρτους φαγεῖν. καὶ εἶπεν· οὐ μὴ φάγω, ἕως τοῦ λαλῆσαί με τὰ ρήματά μου. καὶ εἶπαν· λάλησον.
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

## Genesis 24:34

Greek: Καὶ εἶπε· παῖς ῾Αβραὰμ ἐγώ εἰμι.
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

## Genesis 24:35

Greek: Κύριος δὲ ηὐλόγησε τὸν κύριόν μου σφόδρα, καὶ ὑψώθη· καὶ ἔδωκεν αὐτῷ πρόβατα καὶ μόσχους καὶ ἀργύριον καὶ χρυσίον, παῖδας καὶ παιδίσκας, καμήλους καὶ ὄνους.
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

## Genesis 24:36

Greek: καὶ ἔτεκε Σάρρα ἡ γυνὴ τοῦ κυρίου μου υἱὸν ἕνα τῷ κυρίῳ μου μετὰ τὸ γηράσαι αὐτόν, καὶ ἔδωκεν αὐτῷ ὅσα ἦν αὐτῷ.
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

## Genesis 24:37

Greek: καὶ ὥρκισέ με ὁ κύριός μου, λέγων· οὐ λήψῃ γυναῖκα τῷ υἱῷ μου ἀπὸ τῶν θυγατέρων τῶν Χαναναίων, ἐν οἷς ἐγὼ παροικῶ ἐν τῇ γῇ αὐτῶν,
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

## Genesis 24:38

Greek: ἀλλ᾿ ἢ εἰς τὸν οἶκον τοῦ πατρός μου πορεύσῃ καὶ εἰς τὴν φυλήν μου καὶ λήψῃ γυναῖκα τῷ υἱῷ μου ἐκεῖθεν.
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

## Genesis 24:39

Greek: εἶπα δὲ τῷ κυρίῳ μου· μήποτε οὐ πορεύσεται ἡ γυνὴ μετ᾿ ἐμοῦ.
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

## Genesis 24:40

Greek: καὶ εἶπέ μοι· Κύριος ὁ Θεός, ᾧ εὐηρέστησα ἐναντίον αὐτοῦ, αὐτὸς ἐξαποστελεῖ τὸν ἄγγελον αὐτοῦ μετὰ σοῦ καὶ εὐοδώσει τὴν ὁδόν σου, καὶ λήψῃ γυναῖκα τῷ υἱῷ μου ἐκ τῆς φυλῆς μου καὶ ἐκ τοῦ οἴκου τοῦ πατρός μου.
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

## Genesis 24:41

Greek: τότε ἀθῷος ἔσῃ ἀπὸ τῆς ἀρᾶς μου· ἡνίκα γὰρ ἐὰν ἔλθῃς εἰς τὴν φυλήν μου καὶ μή σοι δῶσι, καὶ ἔσῃ ἀθῷος ἀπὸ τοῦ ὁρκισμοῦ μου.
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

## Genesis 24:42

Greek: καὶ ἐλθὼν σήμερον ἐπὶ τὴν πηγὴν εἶπα· Κύριε ὁ Θεὸς τοῦ κυρίου μου ῾Αβραάμ, εἰ σὺ εὐοδοῖς τὴν ὁδόν μου, ἐν ᾗ νῦν ἐγὼ πορεύομαι ἐν αὐτῇ,
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

## Genesis 24:43

Greek: ἰδοὺ ἐγὼ ἐφέστηκα ἐπὶ τῆς πηγῆς τοῦ ὕδατος, καὶ αἱ θυγατέρες τῶν ἀνθρώπων τῆς πόλεως ἐκπορεύονται ἀντλῆσαι ὕδωρ, καὶ ἔσται ἡ παρθένος, ᾗ ἂν ἐγὼ εἴπω, πότισόν με ἐκ τῆς ὑδρίας σου μικρὸν ὕδωρ,
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

## Genesis 24:44

Greek: καὶ εἴπῃ μοι, καὶ σὺ πίε καὶ ταῖς καμήλοις σου ὑδρεύσομαι, αὕτη ἡ γυνή, ἣν ἡτοίμασε Κύριος τῷ ἑαυτοῦ θεράποντι ᾿Ισαάκ, καὶ ἐν τούτῳ γνώσομαι, ὅτι πεποίηκας ἔλεος τῷ κυρίῳ μου ῾Αβραάμ.
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

## Genesis 24:45

Greek: καὶ ἐγένετο πρὸ τοῦ συντελέσαι με λαλοῦντα ἐν τῇ διανοίᾳ μου, εὐθὺς Ρεβέκκα ἐξεπορεύετο ἔχουσα τὴν ὑδρίαν ἐπὶ τῶν ὤμων καὶ κατέβη ἐπὶ τὴν πηγὴν καὶ ὑδρεύσατο. εἶπα δὲ αὐτῇ· πότισόν με.
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

## Genesis 24:46

Greek: καί σπεύσασα καθεῖλε τὴν ὑδρίαν ἐπὶ τὸν βραχίονα αὐτῆς ἀφ᾿ ἑαυτῆς καὶ εἶπε· πίε σύ, καὶ τὰς καμήλους σου ποτιῶ. καὶ ἔπιον καὶ τὰς καμήλους ἐπότισε.
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

## Genesis 24:47

Greek: καὶ ἠρώτησα αὐτήν· καὶ εἶπα· θυγάτηρ τίνος εἶ; ἀνάγγειλόν μοι. ἡ δὲ ἔφη· θυγάτηρ Βαθουήλ εἰμι τοῦ υἱοῦ Ναχώρ, ὃν ἔτεκεν αὐτῷ Μελχά. καὶ περιέθηκα αὐτῇ τὰ ἐνώτια καί τὰ ψέλλια περὶ τὰς χεῖρας αὐτῆς·
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

## Genesis 24:48

Greek: καὶ εὐδοκήσας προσεκύνησα τῷ Κυρίῳ καὶ εὐλόγησα Κύριον τὸν Θεὸν τοῦ κυρίου μου ῾Αβραάμ, ὃς εὐώδωσέ με ἐν ὁδῷ ἀληθείας, λαβεῖν τὴν θυγατέρα τοῦ ἀδελφοῦ τοῦ κυρίου μου τῷ υἱῷ αὐτοῦ.
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

## Genesis 24:49

Greek: εἰ οὖν ποιεῖτε ὑμεῖς ἔλεος καὶ δικαιοσύνην πρὸς τὸν κύριόν μου, ἀπαγγείλατέ μοι, εἰ δὲ μή, ἀπαγγείλατέ μοι, ἵνα ἐπιστρέψω εἰς δεξιὰν ἢ ἀριστεράν.
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

## Genesis 24:50

Greek: ᾿Αποκριθεὶς δὲ Λάβαν καὶ Βαθουὴλ εἶπαν· παρὰ Κυρίου ἐξῆλθε τὸ πρόσταγμα τοῦτο· οὐ δυνησόμεθα οὖν σοι ἀντειπεῖν κακὸν ἢ καλόν.
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

## Genesis 24:51

Greek: ἰδοὺ Ρεβέκκα ἐνώπιόν σου· λαβὼν ἀπότρεχε. καί ἔστω γυνὴ τῷ υἱῷ τοῦ κυρίου σου, καθὰ ἐλάλησε Κύριος.
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

## Genesis 24:52

Greek: ἐγένετο δὲ ἐν τῷ ἀκοῦσαι τὸν παῖδα τοῦ ῾Αβραὰμ τῶν ρημάτων τούτων, προσεκύνησεν ἐπὶ τὴν γῆν τῷ Κυρίῳ.
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

## Genesis 24:53

Greek: καὶ ἐξενέγκας ὁ παῖς σκεύη ἀργυρᾶ καὶ χρυσᾶ καὶ ἱματισμὸν ἔδωκε τῇ Ρεβέκκᾳ καὶ δῶρα ἔδωκε τῷ ἀδελφῷ αὐτῆς καὶ τῇ μητρὶ αὐτῆς.
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

## Genesis 24:54

Greek: καὶ ἔφαγον καὶ ἔπιον καὶ αὐτὸς καὶ οἱ ἄνδρες οἱ μετ᾿ αὐτοῦ ὄντες, καὶ ἐκοιμήθησαν. Καὶ ἀναστὰς τὸ πρωΐ εἶπεν· ἐκπέμψατέ με, ἵνα ἀπέλθω πρὸς τὸν κύριόν μου.
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

## Genesis 24:55

Greek: εἶπαν δὲ οἱ ἀδελφοὶ αὐτῆς καὶ ἡ μήτηρ· μεινάτω ἡ παρθένος μεθ᾿ ἡμῶν ἡμέρας ὡσεὶ δέκα, καὶ μετὰ ταῦτα ἀπελεύσεται.
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

## Genesis 24:56

Greek: ὁ δὲ εἶπε πρὸς αὐτούς· μὴ κατέχετέ με, καὶ Κύριος εὐώδωσε τὴν ὁδόν μου ἐν ἐμοί· ἐκπέμψατέ με, ἵνα ἀπέλθω πρὸς τὸν κύριόν μου.
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

## Genesis 24:57

Greek: οἱ δὲ εἶπαν· καλέσωμεν τὴν παῖδα καὶ ἐρωτήσωμεν τὸ στόμα αὐτῆς.
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

## Genesis 24:58

Greek: καὶ ἐκάλεσαν τὴν Ρεβέκκαν καὶ εἶπαν αὐτῇ· πορεύσῃ μετὰ τοῦ ἀνθρώπου τούτου; ἡ δὲ εἶπε· πορεύσομαι.
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

## Genesis 24:59

Greek: καὶ ἐξέπεμψαν Ρεβέκκαν τὴν ἀδελφὴν αὐτῶν καὶ τὰ ὑπάρχοντα αὐτῆς καὶ τὸν παῖδα τοῦ ῾Αβραὰμ καὶ τοὺς μετ᾿ αὐτοῦ.
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

## Genesis 24:60

Greek: καὶ εὐλόγησαν Ρεβέκκαν καὶ εἶπαν αὐτῇ· ἀδελφὴ ἡμῶν εἶ· γίνου εἰς χιλιάδας μυριάδων, καὶ κληρονομησάτω τὸ σπέρμα σου τὰς πόλεις τῶν ὑπεναντίων.
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

## Genesis 24:61

Greek: ἀναστᾶσα δὲ Ρεβέκκα καὶ αἱ ἅβραι αὐτῆς, ἐπέβησαν ἐπὶ τὰς καμήλους καὶ ἐπορεύθησαν μετὰ τοῦ ἀνθρώπου, καὶ ἀναλαβὼν ὁ παῖς τὴν Ρεβέκκαν ἀπῆλθεν.
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

## Genesis 24:62

Greek: ᾿Ισαὰκ δὲ διεπορεύετο διὰ τῆς ἐρήμου κατὰ τὸ φρέαρ τῆς ὁράσεως· αὐτὸς δὲ κατώκει ἐν τῇ γῇ τῇ πρὸς λίβα.
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

## Genesis 24:63

Greek: καὶ ἐξῆλθεν ᾿Ισαὰκ ἀδολεσχῆσαι εἰς τὸ πεδίον τὸ πρὸς δείλης καὶ ἀναβλέψας τοῖς ὀφθαλμοῖς αὐτοῦ εἶδε καμήλους ἐρχομένας.
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

## Genesis 24:64

Greek: καὶ ἀναβλέψασα Ρεβέκκα τοῖς ὀφθαλμοῖς εἶδε τὸν ᾿Ισαὰκ καὶ κατεπήδησεν ἀπὸ τῆς καμήλου.
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

## Genesis 24:65

Greek: καὶ εἶπε τῷ παιδί· τίς ἐστιν ὁ ἄνθρωπος ἐκεῖνος ὁ πορευόμενος ἐν τῷ πεδίῳ εἰς συνάντησιν ἡμῖν; εἶπε δὲ ὁ παῖς· οὗτός ἐστιν ὁ κύριός μου. ἡ δὲ λαβοῦσα τὸ θέριστρον περιεβάλετο.
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

## Genesis 24:66

Greek: καὶ διηγήσατο ὁ παῖς τῷ ᾿Ισαὰκ πάντα τὰ ρήματα, ἃ ἐποίησεν.
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

## Genesis 24:67

Greek: εἰσῆλθε δὲ ᾿Ισαὰκ εἰς τὸν οἶκον τῆς μητρὸς αὐτοῦ καὶ ἔλαβε τὴν Ρεβέκκαν, καὶ ἐγένετο αὐτοῦ γυνή, καὶ ἠγάπησεν αὐτήν· καὶ παρεκλήθη ᾿Ισαὰκ περὶ Σάρρας τῆς μητρὸς αὐτοῦ.
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

# Chapter 25

## Genesis 25:1

Greek: ΠΡΟΣΘΕΜΕΝΟΣ δὲ ῾Αβραὰμ ἔλαβε γυναῖκα, ἧ ὄνομα Χεττούρα.
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

## Genesis 25:2

Greek: ἔτεκε δὲ αὐτῷ τὸν Ζομβρᾶν καὶ τὸν ᾿Ιεζὰν καὶ τὸν Μαδὰλ καὶ τὸν Μαδιὰμ καὶ τὸν ᾿Ιεσβὼκ καὶ τὸν Σωκέ.
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

## Genesis 25:3

Greek: Ιεζὰν δὲ ἐγέννησε καὶ τὸν Θαιμὰν τὸν Σαβὰ καὶ τὸν Δεδάν· υἱοὶ δὲ Δεδὰν ἐγένοντο Ραγουὴλ καὶ Ναβδεὴλ καὶ ᾿Ασσουριεὶμ καὶ Λατουσιεὶμ καὶ Λαωμείμ.
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

## Genesis 25:4

Greek: υἱοὶ δὲ Μαδιὰμ Γεφὰρ καὶ ᾿Αφεὶρ καὶ ᾿Ενὼχ καὶ ᾿Αβειρὰ καὶ ᾿Ελδαγά. πάντες οὗτοι ἦσαν υἱοὶ Χεττούρας.
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

## Genesis 25:5

Greek: ῎Εδωκε δὲ ῾Αβραὰμ πάντα τὰ ὑπάρχοντα αὐτοῦ ᾿Ισαὰκ τῷ υἱῷ αὐτοῦ,
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

## Genesis 25:6

Greek: καὶ τοῖς υἱοῖς τῶν παλλακῶν αὐτοῦ ἔδωκεν ῾Αβραὰμ δόματα καὶ ἐξαπέστειλεν αὐτοὺς ἀπὸ ᾿Ισαὰκ τοῦ υἱοῦ αὐτοῦ, ἔτι ζῶντος αὐτοῦ, πρὸς ἀνατολὰς εἰς γῆν ἀνατολῶν.
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

## Genesis 25:7

Greek: ταῦτα δὲ τὰ ἔτη ἡμερῶν τῆς ζωῆς ῾Αβραὰμ ὅσα ἔζησεν, ἑκατὸν ἑβδομηκονταπέντε ἔτη.
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

## Genesis 25:8

Greek: καὶ ἐκλείπων ἀπέθανεν ῾Αβραὰμ ἐν γήρᾳ καλῷ πρεσβύτης καὶ πλήρης ἡμερῶν καὶ προσετέθη πρὸς τὸν λαὸν αὐτοῦ.
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

## Genesis 25:9

Greek: καὶ ἔθαψαν αὐτὸν ᾿Ισαὰκ καὶ ᾿Ισμαὴλ οἱ υἱοὶ αὐτοῦ εἰς τὸ σπήλαιον τὸ διπλοῦν, εἰς τὸν ἀγρὸν ᾿Εφρὼν τοῦ Σαὰρ τοῦ Χετταίου, ὅς ἐστιν ἀπέναντι Μαμβρῆ,
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

## Genesis 25:10

Greek: τὸν ἀγρὸν καὶ τὸ σπήλαιον, ὃ ἐκτήσατο ῾Αβραὰμ παρὰ τῶν υἱῶν τοῦ Χέτ, ἐκεῖ ἔθαψαν ῾Αβραὰμ καὶ Σάρραν τὴν γυναῖκα αὐτοῦ.
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

## Genesis 25:11

Greek: ἐγένετο δὲ μετὰ τὸ ἀποθανεῖν ῾Αβραάμ, εὐλόγησεν ὁ Θεὸς τὸν ᾿Ισαὰκ υἱὸν αὐτοῦ· καὶ κατῴκησεν ᾿Ισαὰκ παρὰ τὸ φρέαρ τῆς ὁράσεως.
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

## Genesis 25:12

Greek: Αὗται δέ αἱ γενέσεις ᾿Ισμαὴλ τοῦ υἱοῦ ῾Αβραάμ, ὃν ἔτεκεν ῎Αγαρ ἡ Αἰγυπτία ἡ παιδίσκη Σάρρας τῷ ῾Αβραάμ.
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

## Genesis 25:13

Greek: καὶ ταῦτα τὰ ὀνόματα τῶν υἱῶν ᾿Ισμαὴλ κατ᾿ ὀνόματα τῶν γενεῶν αὐτοῦ· πρωτότοκος ᾿Ισμαὴλ Ναβαιώθ, καὶ Κηδὰρ καὶ Ναβδεὴλ καὶ Μασσὰμ
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

## Genesis 25:14

Greek: καὶ Μασμὰ καὶ Δουμὰ καὶ Μασσῆ
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

## Genesis 25:15

Greek: καὶ Χοδδὰν καὶ Θαιμὰν καὶ ᾿Ιετοὺρ καὶ Ναφὲς καὶ Κεδμά.
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

## Genesis 25:16

Greek: οὗτοί εἰσιν οἱ υἱοὶ ᾿Ισμαὴλ καὶ ταῦτα τὰ ὀνόματα αὐτῶν ἐν ταῖς σκηναῖς αὐτῶν καὶ ἐν ταῖς ἐπαύλεσιν αὐτῶν· δώδεκα ἄρχοντες κατὰ ἔθνη αὐτῶν.
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

## Genesis 25:17

Greek: καὶ ταῦτα τὰ ἔτη τῆς ζωῆς ᾿Ισμαήλ· ἑκατὸν τριακονταεπτὰ ἔτη· καὶ ἐκλείπων ἀπέθανε καὶ προσετέθη πρὸς τὸ γένος αὐτοῦ.
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

## Genesis 25:18

Greek: κατῴκησε δὲ ἀπὸ Εὐϊλὰτ ἕως Σούρ, ἥ ἐστι κατὰ πρόσωπον Αἰγύπτου, ἕως ἐλθεῖν πρὸς ᾿Ασσυρίους· κατὰ πρόσωπον πάντων τῶν ἀδελφῶν αὐτοῦ κατῴκησε.
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

## Genesis 25:19

Greek: Καὶ αὗται αἱ γενέσεις ᾿Ισαὰκ τοῦ υἱοῦ ῾Αβραάμ·
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

## Genesis 25:20

Greek: ῾Αβραὰμ ἐγέννησε τὸν ᾿Ισαάκ. ἦν δὲ ᾿Ισαὰκ ἐτῶν τεσσαράκοντα, ὅτε ἔλαβε τὴν Ρεβέκκαν θυγατέρα Βαθουὴλ τοῦ Σύρου ἐκ τῆς Μεσοποταμίας Συρίας, ἀδελφὴν Λάβαν τοῦ Σύρου, ἑαυτῷ εἰς γυναῖκα.
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

## Genesis 25:21

Greek: ἐδέετο δὲ ᾿Ισαὰκ Κυρίου περὶ Ρεβέκκας τῆς γυναικὸς αὐτοῦ, ὅτι στεῖρα ἦν· ἐπήκουσε δὲ αὐτοῦ ὁ Θεός, καὶ συνέλαβεν ἐν γαστρὶ Ρεβέκκα ἡ γυνὴ αὐτοῦ.
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

## Genesis 25:22

Greek: ἐσκίρτων δὲ τὰ παιδία ἐν αὐτῇ· εἶπε δέ, εἰ οὕτω μοι μέλλει γίνεσθαι, ἵνα τί μοι τοῦτο; ἐπορεύθη δὲ πυθέσθαι παρὰ Κυρίου.
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

## Genesis 25:23

Greek: καὶ εἶπε Κύριος αὐτῇ· δύο ἔθνη ἐν γαστρί σου εἰσί, καὶ δύο λαοὶ ἐκ τῆς κοιλίας σου διασταλήσονται· καὶ λαὸς λαοῦ ὑπερέξει, καὶ ὁ μείζων δουλεύσει τῷ ἐλάσσονι.
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

## Genesis 25:24

Greek: καὶ ἐπληρώθησαν αἱ ἡμέραι τοῦ τεκεῖν αὐτήν, καὶ τῇδε ἦν δίδυμα ἐν τῇ κοιλίᾳ αὐτῆς.
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

## Genesis 25:25

Greek: ἐξῆλθε δὲ ὁ πρωτότοκος πυρράκης, ὅλος ὡσεὶ δορὰ δασύς· ἐπωνόμασε δὲ τὸ ὄνομα αὐτοῦ ῾Ησαῦ.
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

## Genesis 25:26

Greek: καὶ μετὰ τοῦτο ἐξῆλθεν ὁ ἀδελφὸς αὐτοῦ, καὶ ἡ χεὶρ αὐτοῦ ἐπειλημμένη τῆς πτέρνης ῾Ησαῦ· καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ ᾿Ιακώβ. ᾿Ισαὰκ δὲ ἦν ἐτῶν ἑξήκοντα, ὅτε ἔτεκεν αὐτοὺς Ρεβέκκα.
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

## Genesis 25:27

Greek: Ηὐξήθησαν δὲ οἱ νεανίσκοι, καὶ ἦν ῾Ησαῦ ἄνθρωπος εἰδὼς κυνηγεῖν, ἄγροικος, ᾿Ιακὼβ δὲ ἄνθρωπος ἄπλαστος, οἰκῶν οἰκίαν.
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

## Genesis 25:28

Greek: ἠγάπησε δὲ ᾿Ισαὰκ τὸν ῾Ησαῦ, ὅτι ἡ θήρα αὐτοῦ βρῶσις αὐτῷ· Ρεβέκκα δὲ ἠγάπα τὸν ᾿Ιακώβ.
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

## Genesis 25:29

Greek: ἥψησε δὲ ᾿Ιακὼβ ἕψημα· ἦλθε δὲ ῾Ησαῦ ἐκ τοῦ πεδίου ἐκλείπων,
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

## Genesis 25:30

Greek: καὶ εἶπεν ῾Ησαῦ τῷ ᾿Ιακώβ· γεῦσόν με ἀπὸ τοῦ ἑψήματος τοῦ πυρροῦ τούτου, ὅτι ἐκλείπω. διὰ τοῦτο ἐκλήθη τὸ ὄνομα αὐτοῦ ᾿Εδώμ.
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

## Genesis 25:31

Greek: εἶπε δὲ ᾿Ιακὼβ τῷ ῾Ησαῦ· ἀπόδου μοι σήμερον τὰ πρωτοτόκιά σου ἐμοί.
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

## Genesis 25:32

Greek: καὶ εἶπεν ῾Ησαῦ· ἰδοὺ ἐγὼ πορεύομαι τελευτᾶν, καὶ ἵνα τί μοι ταῦτα τὰ πρωτοτόκια
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

## Genesis 25:33

Greek: καὶ εἶπεν αὐτῷ ᾿Ιακώβ· ὄμοσόν μοι σήμερον. καὶ ὤμοσεν αὐτῷ· ἀπέδοτο δὲ ῾Ησαῦ τὰ πρωτοτόκια τῷ ᾿Ιακώβ.
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

## Genesis 25:34

Greek: ᾿Ιακὼβ δὲ ἔδωκε τῷ ῾Ησαῦ ἄρτον καὶ ἕψημα φακοῦ, καὶ ἔφαγε καὶ ἔπιε καὶ ἀναστὰς ᾤχετο· καὶ ἐφαύλισεν ῾Ησαῦ τὰ πρωτοτόκια.
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

# Chapter 26

## Genesis 26:1

Greek: ΕΓΕΝΕΤΟ δὲ λιμὸς ἐπὶ τῆς γῆς χωρὶς τοῦ λιμοῦ τοῦ πρότερον, ὃς ἐγένετο ἐν τῷ καιρῷ τοῦ ῾Αβραάμ· ἐπορεύθη δὲ ᾿Ισαὰκ πρὸς ᾿Αβιμέλεχ βασιλέα Φυλιστιεὶμ εἰς Γέραρα.
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

## Genesis 26:2

Greek: ὤφθη δὲ αὐτῷ Κύριος καὶ εἶπε· μὴ καταβῇς εἰς Αἴγυπτον· κατοίκησον δὲ ἐν τῇ γῇ, ᾗ ἄν σοι εἴπω.
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

## Genesis 26:3

Greek: καὶ παροίκει ἐν τῇ γῇ ταύτῃ, καὶ ἔσομαι μετὰ σοῦ καὶ εὐλογήσω σε· σοὶ γὰρ καὶ τῷ σπέρματί σου δώσω πᾶσαν τὴν γῆν ταύτην καὶ στήσω τὸν ὅρκον μου, ὃν ὤμοσα τῷ ῾Αβραὰμ τῷ πατρί σου.
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

## Genesis 26:4

Greek: καὶ πληθυνῶ τὸ σπέρμα σου ὡς τοὺς ἀστέρας τοῦ οὐρανοῦ καὶ δώσω τῷ σπέρματί σου πᾶσαν τὴν γῆν ταύτην, καὶ εὐλογηθήσονται ἐν τῷ σπέρματί σου πάντα τὰ ἔθνη τῆς γῆς,
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

## Genesis 26:5

Greek: ἀνθ᾿ ὧν ὑπήκουσεν ῾Αβραὰμ ὁ πατήρ σου τῆς ἐμῆς φωνῆς καὶ ἐφύλαξε τὰ προστάγματά μου καὶ τὰς ἐντολάς μου καὶ τὰ δικαιώματά μου καὶ τὰ νόμιμά μου.
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

## Genesis 26:6

Greek: κατῴκησε δὲ ᾿Ισαὰκ ἐν Γεράροις.
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

## Genesis 26:7

Greek: ᾿Επηρώτησαν δὲ οἱ ἄνδρες τοῦ τόπου περὶ Ρεβέκκας τῆς γυναικὸς αὐτοῦ, καὶ εἶπεν· ἀδελφή μου ἐστίν· ἐφοβήθη γὰρ εἰπεῖν ὅτι γυνή μου ἐστί, μήποτε ἀποκτείνωσιν αὐτὸν οἱ ἄνδρες τοῦ τόπου περὶ Ρεβέκκας, ὅτι ὡραία τῇ ὄψει ἦν.
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

## Genesis 26:8

Greek: ἐγένετο δὲ πολυχρόνιος ἐκεῖ· καὶ παρακύψας ᾿Αβιμέλεχ ὁ βασιλεὺς Γεράρων διὰ τῆς θυρίδος, εἶδε τὸν ᾿Ισαὰκ παίζοντα μετὰ Ρεβέκκας τῆς γυναικὸς αὐτοῦ.
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

## Genesis 26:9

Greek: ἐκάλεσε δὲ ᾿Αβιμέλεχ τὸν ᾿Ισαὰκ καὶ εἶπεν αὐτῷ· ἆρά γε γυνή σου ἐστί; τί ὅτι εἶπας, ἀδελφή μου ἐστίν; εἶπε δὲ αὐτῷ ᾿Ισαάκ· εἶπα γάρ, μήποτε ἀποθάνω δι᾿ αὐτήν.
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

## Genesis 26:10

Greek: εἶπε δὲ αὐτῷ ᾿Αβιμέλεχ· τί τοῦτο ἐποίησας ἡμῖν; μικροῦ ἐκοιμήθη τις ἐκ τοῦ γένους μου μετὰ τῆς γυναικός σου, καὶ ἐπήγαγες ἂν ἐφ᾿ ἡμᾶς ἄγνοιαν.
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

## Genesis 26:11

Greek: συνέταξε δὲ ᾿Αβιμέλεχ παντὶ τῷ λαῷ αὐτοῦ, λέγων· πᾶς ὁ ἁψάμενος τοῦ ἀνθρώπου τούτου ἢ τῆς γυναικὸς αὐτοῦ, θανάτῳ ἔνοχος ἔσται.
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

## Genesis 26:12

Greek: ἔσπειρε δὲ ᾿Ισαὰκ ἐν τῇ γῇ ἐκείνῃ καὶ εὗρεν ἐν τῷ ἐνιαυτῷ ἐκείνῳ ἑκατοστεύουσαν κριθήν· εὐλόγησε δὲ αὐτὸν Κύριος.
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

## Genesis 26:13

Greek: καὶ ὑψώθη ὁ ἄνθρωπος. καὶ προβαίνων μείζων ἐγίνετο, ἕως οὗ μέγας ἐγένετο σφόδρα·
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

## Genesis 26:14

Greek: ἐγένετο δὲ αὐτῷ κτήνη προβάτων καὶ κτήνη βοῶν καὶ γεώργια πολλά. ἐζήλωσαν δὲ αὐτὸν οἱ Φυλιστιείμ,
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

## Genesis 26:15

Greek: καὶ πάντα τὰ φρέατα, ἃ ὤρυξαν οἱ παῖδες τοῦ πατρὸς αὐτοῦ ἐν τῷ χρόνῳ τοῦ πατρὸς αὐτοῦ, ἐνέφραξαν αὐτὰ οἱ Φυλιστιεὶμ καὶ ἔπλησαν αὐτὰ γῆς.
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

## Genesis 26:16

Greek: εἶπε δὲ ᾿Αβιμέλεχ πρὸς ᾿Ισαάκ· ἄπελθε ἀφ᾿ ἡμῶν, ὅτι δυνατώτερος ἡμῶν ἐγένου σφόδρα.
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

## Genesis 26:17

Greek: καὶ ἀπῆλθεν ἐκεῖθεν ᾿Ισαὰκ καὶ κατέλυσεν ἐν τῇ φάραγγι Γεράρων καὶ κατῴκησεν ἐκεῖ.
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

## Genesis 26:18

Greek: καὶ πάλιν ᾿Ισαὰκ ὤρυξε τὰ φρέατα τοῦ ὕδατος, ἃ ὤρυξαν οἱ παῖδες ῾Αβραὰμ τοῦ πατρὸς αὐτοῦ καὶ ἐνέφραξαν αὐτὰ οἱ Φυλιστιεὶμ μετὰ τὸ ἀποθανεῖν ῾Αβραὰμ τὸν πατέρα αὐτοῦ, καὶ ἐπωνόμασεν αὐτοῖς ὀνόματα κατὰ τὰ ὀνόματα, ἃ ὠνόμασεν ὁ πατὴρ αὐτοῦ.
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

## Genesis 26:19

Greek: καὶ ὤρυξαν οἱ παῖδες ᾿Ισαὰκ ἐν τῇ φάραγγι Γεράρων καὶ εὗρον ἐκεῖ φρέαρ ὕδατος ζῶντος.
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

## Genesis 26:20

Greek: καὶ ἐμαχέσαντο οἱ ποιμένες Γεράρων μετὰ τῶν ποιμένων ᾿Ισαάκ, φάσκοντες αὐτῶν εἶναι τὸ ὕδωρ. καὶ ἐκάλεσαν τὸ ὄνομα τοῦ φρέατος ᾿Αδικία· ἠδίκησαν γὰρ αὐτόν.
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

## Genesis 26:21

Greek: ἀπάρας δὲ ᾿Ισαὰκ ἐκεῖθεν ὤρυξε φρέαρ ἕτερον, ἐκρίνοντο δὲ καὶ περὶ ἐκείνου· καὶ ἐπωνόμασε τὸ ὄνομα αὐτοῦ ᾿Εχθρία.
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

## Genesis 26:22

Greek: ἀπάρας δὲ ἐκεῖθεν ὤρυξε φρέαρ ἕτερον, καὶ οὐκ ἐμαχέσαντο περὶ αὐτοῦ· καὶ ἐπωνόμασε τὸ ὄνομα αὐτοῦ Εὐρυχωρία, λέγων· διότι νῦν ἐπλάτυνε Κύριος ἡμῖν καὶ ηὔξησεν ἡμᾶς ἐπὶ τῆς γῆς.
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

## Genesis 26:23

Greek: ᾿Ανέβη δὲ ἐκεῖθεν ἐπὶ τὸ φρέαρ τοῦ ὅρκου.
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

## Genesis 26:24

Greek: καὶ ὤφθη αὐτῷ Κύριος ἐν τῇ νυκτὶ ἐκείνῃ καὶ εἶπεν· ἐγώ εἰμι ὁ Θεὸς ῾Αβραὰμ τοῦ πατρός σου· μὴ φοβοῦ· μετὰ σοῦ γάρ εἰμι καὶ εὐλογήσω σε καὶ πληθυνῶ τὸ σπέρμα σου δι᾿ ῾Αβραὰμ τὸν πατέρα σου.
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

## Genesis 26:25

Greek: καὶ ᾠκοδόμησεν ἐκεῖ θυσιαστήριον καὶ ἐπεκαλέσατο τὸ ὄνομα Κυρίου καὶ ἔπηξεν ἐκεῖ τὴν σκηνὴν αὐτοῦ· ὤρυξαν δὲ ἐκεῖ οἱ παῖδες ᾿Ισαὰκ φρέαρ ἐν τῇ φάραγγι Γεράρων.
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

## Genesis 26:26

Greek: καὶ ᾿Αβιμέλεχ ἐπορεύθη πρὸς αὐτὸν ἀπὸ Γεράρων καὶ ῾Οχοζὰθ ὁ νυμφαγωγὸς αὐτοῦ καὶ Φιχὸλ ὁ ἀρχιστράτηγος τῆς δυνάμεως αὐτοῦ.
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

## Genesis 26:27

Greek: καὶ εἶπεν αὐτοῖς ᾿Ισαάκ· ἵνα τί ἤλθετε πρός με; ὑμεῖς δὲ ἐμισήσατέ με καὶ ἐξαπεστείλατέ με ἀφ᾿ ὑμῶν.
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

## Genesis 26:28

Greek: οἱ δὲ εἶπαν· ἰδόντες ἑωράκαμεν, ὅτι ἦν Κύριος μετὰ σοῦ, καὶ εἴπαμεν· γενέσθω ἀρὰ ἀνὰ μέσον ἡμῶν καὶ ἀνὰ μέσον σοῦ, καὶ διαθησόμεθα μετὰ σοῦ διαθήκην,
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

## Genesis 26:29

Greek: μὴ ποιῆσαι μεθ᾿ ἡμῶν κακόν, καθότι οὐκ ἐβδελυξάμεθά σε ἡμεῖς, καὶ ὃν τρόπον ἐχρησάμεθά σοι καλῶς καί ἐξαπεστείλαμέν σε μετ᾿ εἰρήνης· καὶ νῦν εὐλογημένος σὺ ὑπὸ Κυρίου.
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

## Genesis 26:30

Greek: καὶ ἐποίησεν αὐτοῖς δοχήν, καὶ ἔφαγον καὶ ἔπιον·
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

## Genesis 26:31

Greek: καὶ ἀναστάντες τὸ πρωΐ, ὤμοσεν ἕκαστος τῷ πλησίον αὐτοῦ, καὶ ἐξαπέστειλεν αὐτοὺς ᾿Ισαάκ, καὶ ἀπῴχοντο ἀπ᾿ αὐτοῦ μετὰ σωτηρίας.
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

## Genesis 26:32

Greek: ἐγένετο δὲ ἐν τῇ ἡμέρᾳ ἐκείνῃ καὶ παραγενόμενοι οἱ παῖδες ᾿Ισαὰκ ἀπήγγειλαν αὐτῷ περὶ τοῦ φρέατος, οὗ ὤρυξαν, καὶ εἶπαν· οὐχ εὕρομεν ὕδωρ.
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

## Genesis 26:33

Greek: καὶ ἐκάλεσεν αὐτὸ ῞Ορκος· διὰ τοῦτο ἐκάλεσεν ὄνομα τῇ πόλει ἐκείνῃ Φρέαρ ὅρκου ἕως τῆς σήμερον ἡμέρας.
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

## Genesis 26:34

Greek: ῏Ην δὲ ῾Ησαῦ ἐτῶν τεσσαράκοντα καὶ ἔλαβε γυναῖκα ᾿Ιουδίθ, θυγατέρα Βεὼχ τοῦ Χετταίου καὶ τὴν Βασεμάθ, θυγατέρα ῾Ελὼν Χετταίου.
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

## Genesis 26:35

Greek: καὶ ἦσαν ἐρίζουσαι τῷ ᾿Ισαὰκ καὶ τῇ Ρεβέκκᾳ.
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

# Chapter 27

## Genesis 27:1

Greek: ΕΓΕΝΕΤΟ δὲ μετὰ τὸ γηράσαι τὸν ᾿Ισαὰκ καὶ ἠμβλύνθησαν οἱ ὀφθαλμοὶ αὐτοῦ τοῦ ὁρᾶν, καὶ ἐκάλεσεν ῾Ησαῦ τὸν υἱὸν αὐτοῦ τὸν πρεσβύτερον καί εἶπεν αὐτῷ· υἱέ μου· καὶ εἶπεν· ἰδοὺ ἐγώ.
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

## Genesis 27:2

Greek: καὶ εἶπεν· ἰδοὺ γεγήρακα καὶ οὐ γινώσκω τὴν ἡμέραν τῆς τελευτῆς μου·
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

## Genesis 27:3

Greek: νῦν οὖν λαβὲ τὸ σκεῦός σου, τήν τε φαρέτραν καὶ τὸ τόξον, καὶ ἔξελθε εἰς τὸ πεδίον καὶ θήρευσόν μοι θήραν
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

## Genesis 27:4

Greek: καὶ ποίησόν μοι ἐδέσματα, ὡς φιλῶ ἐγώ, καὶ ἔνεγκέ μοι, ἵνα φάγω, ὅπως εὐλογήσῃ σε ἡ ψυχή μου πρὶν ἀποθανεῖν με.
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

## Genesis 27:5

Greek: Ρεβέκκα δὲ ἤκουσε λαλοῦντος ᾿Ισαὰκ πρὸς ῾Ησαῦ τὸν υἱὸν αὐτοῦ. ἐπορεύθη δὲ ῾Ησαῦ εἰς τὸ πεδίον θηρεῦσαι θήραν τῷ πατρὶ αὐτοῦ·
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

## Genesis 27:6

Greek: Ρεβέκκα δὲ εἶπε πρὸς ᾿Ιακὼβ τὸν υἱὸν αὐτῆς, τὸν ἐλάσσω· ἰδέ, ἤκουσα τοῦ πατρός σου λαλοῦντος πρὸς ῾Ησαῦ τὸν ἀδελφόν σου λέγοντος·
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

## Genesis 27:7

Greek: ἔνεγκόν μοι θήραν καὶ ποίησόν μοι ἐδέσματα, ἵνα φαγὼν εὐλογήσω σε ἐναντίον Κυρίου πρὸ τοῦ ἀποθανεῖν με.
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

## Genesis 27:8

Greek: νῦν οὖν, υἱέ μου, ἄκουσόν μου, καθὰ ἐγώ σοι ἐντέλλομαι.
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

## Genesis 27:9

Greek: καὶ πορευθεὶς εἰς τὰ πρόβατα λαβέ μοι ἐκεῖθεν δύο ἐρίφους ἁπαλοὺς καὶ καλούς, καὶ ποιήσω αὐτοὺς ἐδέσματα τῷ πατρί σου, ὡς φιλεῖ,
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

## Genesis 27:10

Greek: καὶ εἰσοίσεις τῷ πατρί σου καὶ φάγεται, ὅπως εὐλογήσῃ σε ὁ πατήρ σου πρὸ τοῦ ἀποθανεῖν αὐτόν.
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

## Genesis 27:11

Greek: εἶπε δὲ ᾿Ιακὼβ πρὸς Ρεβέκκαν τὴν μητέρα αὐτοῦ· ἔστιν ῾Ησαῦ ὁ ἀδελφός μου ἀνὴρ δασύς, ἐγὼ δὲ ἀνὴρ λεῖος·
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

## Genesis 27:12

Greek: μή ποτε ψηλαφήσῃ με ὁ πατήρ, καὶ ἔσομαι ἐναντίον αὐτοῦ ὡς καταφρονῶν καὶ ἐπάξω ἐπ᾿ ἐμαυτὸν κατάραν καὶ οὐκ εὐλογίαν.
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

## Genesis 27:13

Greek: εἶπε δὲ αὐτῷ ἡ μήτηρ· ἐπ᾿ ἐμὲ ἡ κατάρα σου, τέκνον· μόνον ὑπάκουσόν μοι τῆς φωνῆς καὶ πορευθεὶς ἔνεγκέ μοι.
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

## Genesis 27:14

Greek: πορευθεὶς δὲ ἔλαβε καὶ ἤνεγκε τῇ μητρί, καὶ ἐποίησεν ἡ μήτηρ αὐτοῦ ἐδέσματα, καθὰ ἐφίλει ὁ πατὴρ αὐτοῦ.
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

## Genesis 27:15

Greek: καὶ λαβοῦσα Ρεβέκκα τὴν στολὴν ῾Ησαῦ τοῦ υἱοῦ αὐτῆς τοῦ πρεσβυτέρου τὴν καλήν, ἣ ἦν παρ᾿ αὐτῇ ἐν τῷ οἴκῳ, ἐνέδυσεν αὐτὴν ᾿Ιακὼβ τὸν υἱὸν αὐτῆς τὸν νεώτερον
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

## Genesis 27:16

Greek: καὶ τὰ δέρματα τῶν ἐρίφων περιέθηκεν ἐπὶ τοὺς βραχίονας αὐτοῦ καὶ ἐπὶ τὰ γυμνὰ τοῦ τραχήλου αὐτοῦ
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

## Genesis 27:17

Greek: καὶ ἔδωκε τὰ ἐδέσματα καὶ τοὺς ἄρτους, οὓς ἐποίησεν εἰς τὰς χεῖρας ᾿Ιακὼβ τοῦ υἱοῦ αὐτῆς.
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

## Genesis 27:18

Greek: καὶ εἰσήνεγκε τῷ πατρὶ αὐτοῦ. εἶπε δέ· πάτερ. ὁ δὲ εἶπεν· ἰδοὺ ἐγώ· τίς εἶ σὺ τέκνον
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

## Genesis 27:19

Greek: καὶ εἶπεν ᾿Ιακὼβ τῷ πατρί· ἐγὼ ῾Ησαῦ ὁ πρωτότοκός σου· πεποίηκα καθὰ ἐλάλησάς μοι· ἀναστὰς κάθισον καὶ φάγε ἀπὸ τῆς θήρας μου, ὅπως εὐλογήσῃ με ἡ ψυχή σου.
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

## Genesis 27:20

Greek: εἶπε δὲ ᾿Ισαὰκ τῷ υἱῷ αὐτοῦ· τί τοῦτο, ὃ ταχὺ εὗρες, ὦ τέκνον; ὁ δὲ εἶπεν· ὃ παρέδωκε Κύριος ὁ Θεός σου ἐναντίον μου.
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

## Genesis 27:21

Greek: εἶπε δὲ ᾿Ισαὰκ τῷ ᾿Ιακώβ· ἔγγισόν μοι καὶ ψηλαφήσω σε, τέκνον, εἰ σὺ εἶ ὁ υἱός μου ῾Ησαῦ ἢ οὔ.
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

## Genesis 27:22

Greek: ἤγγισε δὲ ᾿Ιακὼβ πρὸς ᾿Ισαὰκ τὸν πατέρα αὐτοῦ, καὶ ἐψηλάφησεν αὐτὸν καὶ εἶπεν· ἡ μὲν φωνὴ φωνὴ ᾿Ιακώβ, αἱ δὲ χεῖρες χεῖρες ῾Ησαῦ.
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

## Genesis 27:23

Greek: καὶ οὐκ ἐπέγνω αὐτόν· ἦσαν γὰρ αἱ χεῖρες αὐτοῦ ὡς αἱ χεῖρες ῾Ησαῦ τοῦ ἀδελφοῦ αὐτοῦ δασεῖαι· καὶ εὐλόγησεν αὐτὸν
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

## Genesis 27:24

Greek: καὶ εἶπε· σὺ εἶ ὁ υἱός μου ῾Ησαῦ; ὁ δὲ εἶπεν· ἐγώ.
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

## Genesis 27:25

Greek: καὶ εἶπε· προσάγαγέ μοι, καὶ φάγομαι ἀπὸ τῆς θήρας σου, τέκνον, ἵνα εὐλογήσῃ σε ἡ ψυχή μου. καὶ προσήνεγκεν αὐτῷ, καὶ ἔφαγε· καὶ εἰσήνεγκεν αὐτῷ οἶνον, καὶ ἔπιε.
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

## Genesis 27:26

Greek: καὶ εἶπεν αὐτῷ ᾿Ισαὰκ ὁ πατὴρ αὐτοῦ· ἔγγισόν μοι καὶ φίλησόν με τέκνον.
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

## Genesis 27:27

Greek: καὶ ἐγγίσας ἐφίλησεν αὐτόν, καὶ ὠσφράνθη τὴν ὀσμὴν τῶν ἱματίων αὐτοῦ καὶ εὐλόγησεν αὐτὸν καὶ εἶπεν· ἰδοὺ ὀσμὴ τοῦ υἱοῦ μου ὡς ὀσμὴ ἀγροῦ πλήρους, ὃν εὐλόγησε Κύριος.
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

## Genesis 27:28

Greek: καὶ δῴη σοι ὁ Θεὸς ἀπὸ τῆς δρόσου τοῦ οὐρανοῦ καὶ ἀπὸ τῆς πιότητος τῆς γῆς καὶ πλῆθος σίτου καὶ οἴνου.
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

## Genesis 27:29

Greek: καὶ δουλευσάτωσάν σοι ἔθνη, καὶ προσκυνησάτωσάν σοι ἄρχοντες· καὶ γίνου κύριος τοῦ ἀδελφοῦ σου, καὶ προσκυνήσουσί σε οἱ υἱοὶ τοῦ πατρός σου. ὁ καταρώμενός σε ἐπικατάρατος, ὁ δὲ εὐλογῶν σε εὐλογημένος.
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

## Genesis 27:30

Greek: Καὶ ἐγένετο μετὰ τὸ παύσασθαι ᾿Ισαὰκ εὐλογοῦντα ᾿Ιακὼβ τὸν υἱὸν αὐτοῦ καὶ ἐγένετο, ὡς ἐξῆλθεν ᾿Ιακὼβ ἀπὸ προσώπου ᾿Ισαὰκ τοῦ πατρὸς αὐτοῦ, καὶ ῾Ησαῦ ὁ ἀδελφὸς αὐτοῦ ἦλθεν ἀπὸ τῆς θήρας.
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

## Genesis 27:31

Greek: καὶ ἐποίησε καὶ αὐτὸς ἐδέσματα καὶ προσήνεγκε τῷ πατρὶ αὐτοῦ. καὶ εἶπε τῷ πατρί· ἀναστήτω ὁ πατήρ μου καὶ φαγέτω ἀπὸ τῆς θήρας τοῦ υἱοῦ αὐτοῦ, ὅπως εὐλογήσῃ με ἡ ψυχή σου.
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

## Genesis 27:32

Greek: καὶ εἶπεν αὐτῷ ᾿Ισαὰκ ὁ πατὴρ αὐτοῦ· τίς εἶ σύ; ὁ δὲ εἶπεν· ἐγώ εἰμι ὁ υἱός σου ὁ πρωτότοκος ῾Ησαῦ.
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

## Genesis 27:33

Greek: ἐξέστη δὲ ᾿Ισαὰκ ἔκστασιν μεγάλην σφόδρα καὶ εἶπε· τίς οὖν ὁ θηρεύσας μοι θήραν καὶ εἰσενέγκας μοι; καὶ ἔφαγον ἀπὸ πάντων πρὸ τοῦ ἐλθεῖν σε καὶ εὐλόγησα αὐτόν, καὶ εὐλογημένος ἔσται.
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

## Genesis 27:34

Greek: ἐγένετο δέ, ἡνίκα ἤκουσεν ῾Ησαῦ τὰ ῥήματα τοῦ πατρὸς αὐτοῦ ᾿Ισαάκ, ἀνεβόησε φωνὴν μεγάλην καὶ πικρὰν σφόδρα καὶ εἶπεν· εὐλόγησον δή κἀμέ, πάτερ.
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

## Genesis 27:35

Greek: εἶπε δὲ αὐτῷ· ἐλθὼν ὁ ἀδελφός σου μετὰ δόλου ἔλαβε τὴν εὐλογίαν σου.
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

## Genesis 27:36

Greek: καὶ εἶπε· δικαίως ἐκλήθη τὸ ὄνομα αὐτοῦ ᾿Ιακώβ· ἐπτέρνικε γάρ με ἰδοὺ δεύτερον τοῦτο· τά τε πρωτοτόκιά μου εἴληφε καὶ νῦν ἔλαβε τὴν εὐλογίαν μου· καὶ εἶπεν ῾Ησαῦ τῷ πατρὶ αὐτοῦ· οὐχ ὑπελίπου μοι εὐλογίαν, πάτερ
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

## Genesis 27:37

Greek: ἀποκριθεὶς δὲ ᾿Ισαὰκ εἶπε τῷ ῾Ησαῦ· εἰ κύριον αὐτὸν πεποίηκά σου καὶ πάντας τοὺς ἀδελφούς αὐτοῦ πεποίηκα αὐτοῦ οἰκέτας, σίτῳ καὶ οἴνῳ ἐστήριξα αὐτόν, σοὶ δὲ τί ποιήσω, τέκνον
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

## Genesis 27:38

Greek: εἶπε δὲ ῾Ησαῦ πρὸς τὸν πατέρα αὐτοῦ· μὴ εὐλογία μία σοί ἐστι, πάτερ; εὐλόγησον δὴ κἀμέ, πάτερ. κατανυχθέντος δὲ ᾿Ισαὰκ ἀνεβόησε φωνῇ ῾Ησαῦ καὶ ἔκλαυσεν.
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

## Genesis 27:39

Greek: ἀποκριθεὶς δὲ ᾿Ισαὰκ ὁ πατὴρ αὐτοῦ εἶπεν αὐτῷ· ἰδοὺ ἀπὸ τῆς πιότητος τῆς γῆς ἔσται ἡ κατοίκησίς σου καὶ ἀπὸ τῆς δρόσου τοῦ οὐρανοῦ ἄνωθεν.
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

## Genesis 27:40

Greek: καὶ ἐπὶ τῇ μαχαίρᾳ σου ζήσῃ καὶ τῷ ἀδελφῷ σου δουλεύσεις· ἔσται δὲ ἡνίκα ἐὰν καθέλῃς, καὶ ἐκλύσῃς τὸν ζυγὸν αὐτοῦ ἀπὸ τοῦ τραχήλου σου.
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

## Genesis 27:41

Greek: Καὶ ἐνεκότει ῾Ησαῦ τῷ ᾿Ιακὼβ περὶ τῆς εὐλογίας ἧς εὐλόγησεν αὐτὸν ὁ πατὴρ αὐτοῦ· εἶπε δὲ ῾Ησαῦ ἐν τῇ διανοίᾳ αὐτοῦ· ἐγγισάτωσαν αἱ ἡμέραι τοῦ πένθους τοῦ πατρός μου, ἵνα ἀποκτείνω ᾿Ιακὼβ τὸν ἀδελφόν μου.
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

## Genesis 27:42

Greek: ἀπηγγέλη δὲ Ρεβέκκᾳ τὰ ρήματα ῾Ησαῦ τοῦ υἱοῦ αὐτῆς τοῦ πρεσβυτέρου, καὶ πέμψασα ἐκάλεσεν ᾿Ιακὼβ τὸν υἱὸν αὐτῆς τὸν νεώτερον καὶ εἶπεν αὐτῷ· ἰδοὺ ῾Ησαῦ ὁ ἀδελφός σου ἀπειλεῖ σοι τοῦ ἀποκτεῖναί σε·
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

## Genesis 27:43

Greek: νῦν οὖν, τέκνον, ἄκουσόν μου τῆς φωνῆς καὶ ἀναστὰς ἀπόδραθι εἰς τὴν Μεσοποταμίαν πρὸς Λάβαν τὸν ἀδελφόν μου εἰς Χαρράν.
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

## Genesis 27:44

Greek: καὶ οἴκησον μετ᾿ αὐτοῦ ἡμέρας τινάς,
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

## Genesis 27:45

Greek: ἕως τοῦ ἀποστρέψαι τὸν θυμὸν καὶ τὴν ὀργὴν τοῦ ἀδελφοῦ σου ἀπὸ σοῦ, καὶ ἐπιλάθηται ἃ πεποίηκας αὐτῷ. καὶ ἀποστείλασα μεταπέμψομαί σε ἐκεῖθεν, μή ποτε ἀποτεκνωθῶ ἀπὸ τῶν δύο ὑμῶν ἐν ἡμέρᾳ μιᾷ.
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

## Genesis 27:46

Greek: Εἶπε δὲ Ρεβέκκα πρὸς ᾿Ισαάκ· προσώχθικα τῇ ζωῇ μου διὰ τὰς θυγατέρας τῶν υἱῶν Χέτ· εἰ λήψεται ᾿Ιακὼβ γυναῖκα ἀπὸ τῶν θυγατέρων τῆς γῆς ταύτης, ἵνα τί μοι τὸ ζῆν
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

# Chapter 28

## Genesis 28:1

Greek: ΠΡΟΣΚΑΛΕΣΑΜΕΝΟΣ δὲ ᾿Ισαὰκ τὸν ᾿Ιακὼβ εὐλόγησεν αὐτὸν καὶ ἐνετείλατο αὐτῷ λέγων· οὐ λήψῃ γυναῖκα ἐκ τῶν θυγατέρων τῶν Χαναναίων·
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

## Genesis 28:2

Greek: ἀναστὰς ἀπόδραθι εἰς τὴν Μεσοποταμίαν, εἰς τὸν οἶκον Βαθουὴλ τοῦ πατρὸς τῆς μητρός σου καὶ λάβε σεαυτῷ ἐκεῖθεν γυναῖκα ἐκ τῶν θυγατέρων Λάβαν τοῦ ἀδελφοῦ τῆς μητρός σου.
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

## Genesis 28:3

Greek: ὁ δὲ Θεός μου εὐλογήσαι σε καὶ αὐξήσαι σε καὶ πληθύναι σε, καὶ ἔσῃ εἰς συναγωγὰς ἐθνῶν·
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

## Genesis 28:4

Greek: καὶ δῴη σοι τὴν εὐλογίαν ῾Αβραὰμ τοῦ πατρός μου σοὶ καὶ τῷ σπέρματί σου μετὰ σέ, κληρονομῆσαι τὴν γῆν τῆς παροικήσεώς σου, ἣν ἔδωκεν ὁ Θεὸς τῷ ῾Αβραάμ.
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

## Genesis 28:5

Greek: καὶ ἀπέστειλεν ᾿Ισαὰκ τὸν ᾿Ιακὼβ καὶ ἐπορεύθη εἰς τὴν Μεσσοποταμίαν πρὸς Λάβαν τὸν υἱὸν Βαθουὴλ τοῦ Σύρου, ἀδελφὸν Ρεβέκκας τῆς μητρὸς ᾿Ιακὼβ καὶ ῾Ησαῦ.
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

## Genesis 28:6

Greek: Εἶδε δὲ ῾Ησαῦ ὅτι εὐλόγησεν ᾿Ισαὰκ τὸν ᾿Ιακώβ, καὶ ἀπῴχετο εἰς τὴν Μεσοποταμίαν Συρίας λαβεῖν ἑαυτῷ γυναῖκα ἐκεῖθεν ἐν τῷ εὐλογεῖν αὐτὸν καὶ ἐνετείλατο αὐτῷ λέγων· οὐ λήψῃ γυναῖκα ἐκ τῶν θυγατέρων τῶν Χαναναίων,
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

## Genesis 28:7

Greek: καὶ ἤκουσεν ᾿Ιακὼβ τοῦ πατρὸς καὶ τῆς μητρὸς αὐτοῦ καὶ ἐπορεύθη εἰς τὴν Μεσοποταμίαν Συρίας.
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

## Genesis 28:8

Greek: ἰδὼν δὲ καὶ ῾Ησαῦ ὅτι πονηραί εἰσιν αἱ θυγατέρες Χαναὰν ἐναντίον ᾿Ισαὰκ τοῦ πατρὸς αὐτοῦ,
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

## Genesis 28:9

Greek: ἐπορεύθη ῾Ησαῦ πρὸς ᾿Ισμαὴλ καὶ ἔλαβε τὴν Μαελὲθ θυγατέρα ᾿Ισμαὴλ τοῦ υἱοῦ ῾Αβραάμ, ἀδελφὴν Ναβεώθ, πρὸς ταῖς γυναιξὶν αὐτοῦ γυναῖκα.
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

## Genesis 28:10

Greek: Καὶ ἐξῆλθεν ᾿Ιακὼβ ἀπὸ τοῦ φρέατος τοῦ ὅρκου καὶ ἐπορεύθη εἰς Χαρράν.
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

## Genesis 28:11

Greek: καὶ ἀπήντησε τόπῳ καὶ ἐκοιμήθῃ ἐκεῖ· ἔδυ γὰρ ὁ ἥλιος· καὶ ἔλαβεν ἀπὸ τῶν λίθων τοῦ τόπου, καὶ ἔθηκε πρὸς κεφαλῆς αὐτοῦ καὶ ἐκοιμήθη ἐν τῷ τόπῳ ἐκείνῳ.
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

## Genesis 28:12

Greek: καὶ ἐνυπνιάσθη, καὶ ἰδοὺ κλίμαξ ἐστηριγμένη ἐν τῇ γῇ, ἧς ἡ κεφαλὴ ἀφικνεῖτο εἰς τὸν οὐρανόν, καὶ οἱ ἄγγελοι τοῦ Θεοῦ ἀνέβαινον καὶ κατέβαινον ἐπ᾿ αὐτῆς.
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

## Genesis 28:13

Greek: ὁ δὲ Κύριος ἐπεστήρικτο ἐπ᾿ αὐτῆς καὶ εἶπεν· ἐγώ εἰμι ὁ Θεὸς ῾Αβραὰμ τοῦ πατρός σου, καὶ ὁ Θεὸς ᾿Ισαάκ· μὴ φοβοῦ· ἡ γῆ, ἐφ᾿ ἧς σὺ καθεύδεις ἐπ᾿ αὐτῆς, σοὶ δώσω αὐτήν, καὶ τῷ σπέρματί σου.
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

## Genesis 28:14

Greek: καὶ ἔσται τὸ σπέρμα σου ὡς ἡ ἄμμος τῆς γῆς καὶ πλατυνθήσεται ἐπὶ θάλασσαν καὶ ἐπὶ λίβα καὶ ἐπὶ βορρᾶν, καὶ ἐπ᾿ ἀνατολάς, καὶ ἐνευλογηθήσονται ἐν σοὶ πᾶσαι αἱ φυλαὶ τῆς γῆς καὶ ἐν τῷ σπέρματί σου.
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

## Genesis 28:15

Greek: καὶ ἰδοὺ ἐγώ εἰμι μετὰ σοῦ διαφυλάσσων σε ἐν τῇ ὁδῷ πάσῃ, οὗ ἂν πορευθῇς, καὶ ἀποστρέψω σε εἰς τὴν γῆν ταύτην, ὅτι οὐ μή σε ἐγκαταλίπω, ἕως τοῦ ποιῆσαί με πάντα ὅσα ἐλάλησά σοι.
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

## Genesis 28:16

Greek: καὶ ἐξηγέρθη ᾿Ιακὼβ ἐκ τοῦ ὕπνου αὐτοῦ καὶ εἶπεν· ὅτι ἔστι Κύριος ἐν τῷ τόπῳ τούτῳ, ἐγὼ δὲ οὐκ ᾔδειν.
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

## Genesis 28:17

Greek: καὶ ἐφοβήθη καὶ εἶπεν· ὡς φοβερὸς ὁ τόπος οὗτος· οὐκ ἔστι τοῦτο ἀλλ᾿ ἢ οἶκος Θεοῦ, καὶ αὕτη ἡ πύλη τοῦ οὐρανοῦ.
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

## Genesis 28:18

Greek: καὶ ἀνέστη ᾿Ιακὼβ τὸ πρωΐ καὶ ἔλαβε τὸν λίθον, ὃν ὑπέθηκεν ἐκεῖ πρὸς κεφαλῆς αὐτοῦ, καὶ ἔστησεν αὐτὸν στήλην καὶ ἐπέχεεν ἔλαιον ἐπὶ τὸ ἄκρον αὐτῆς.
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

## Genesis 28:19

Greek: καὶ ἐκάλεσε τὸ ὄνομα τοῦ τόπου ἐκείνου Οἶκος Θεοῦ· καὶ Οὐλαμλοὺζ ἦν ὄνομα τῇ πόλει τὸ πρότερον.
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

## Genesis 28:20

Greek: καὶ ηὔξατο ᾿Ιακὼβ εὐχὴν λέγων· ἐὰν ᾖ Κύριος ὁ Θεὸς μετ᾿ ἐμοῦ καὶ διαφυλάξῃ με ἐν τῇ ὁδῷ ταύτῃ, ᾗ ἐγὼ πορεύομαι, καὶ δῷ μοι ἄρτον φαγεῖν καὶ ἱμάτιον περιβαλέσθαι
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

## Genesis 28:21

Greek: καὶ ἀποστρέψῃ με μετὰ σωτηρίας εἰς τὸν οἶκον τοῦ πατρός μου, καὶ ἔσται Κύριός μοι εἰς Θεόν,
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

## Genesis 28:22

Greek: καὶ ὁ λίθος οὗτος, ὃν ἔστησα στήλην, ἔσται μοι οἶκος Θεοῦ, καὶ πάντων, ὧν ἐάν μοι δῷς, δεκάτην ἀποδεκατώσω αὐτά σοι.
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

# Chapter 29

## Genesis 29:1

Greek: ΚΑΙ ἐξάρας ᾿Ιακὼβ τοὺς πόδας ἐπορεύθη εἰς γῆν ἀνατολῶν πρὸς Λάβαν τὸν υἱὸν Βαθουὴλ τοῦ Σύρου, ἀδελφὸν δὲ Ρεβέκκας μητρὸς ᾿Ιακὼβ καὶ ῾Ησαῦ.
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

## Genesis 29:2

Greek: καὶ ὁρᾷ καὶ ἰδοὺ φρέαρ ἐν τῷ πεδίῳ, ἦσαν δὲ ἐκεῖ τρία ποίμνια προβάτων ἀναπαυόμενα ἐπ᾿ αὐτοῦ· ἐκ γὰρ τοῦ φρέατος ἐκείνου ἐπότιζον τὰ ποίμνια, λίθος δὲ ἦν μέγας ἐπὶ τῷ στόματι τοῦ φρέατος,
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

## Genesis 29:3

Greek: καὶ συνήγοντο ἐκεῖ πάντα τὰ ποίμνια καὶ ἀπεκύλιον τὸν λίθον ἀπὸ τοῦ στόματος τοῦ φρέατος καὶ ἐπότιζον τὰ πρόβατα καὶ ἀποκαθίστων τὸν λίθον ἐπὶ τὸ στόμα τοῦ φρέατος εἰς τὸν τόπον αὐτοῦ.
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

## Genesis 29:4

Greek: εἶπε δὲ αὐτοῖς ᾿Ιακώβ· ἀδελφοί, πόθεν ἐστὲ ὑμεῖς; οἱ δὲ εἶπαν· ἐκ Χαρρὰν ἐσμέν.
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

## Genesis 29:5

Greek: εἶπε δὲ αὐτοῖς· γινώσκετε Λάβαν τὸν υἱὸν Ναχώρ; οἱ δὲ εἶπαν· γινώσκομεν.
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

## Genesis 29:6

Greek: εἶπε δὲ αὐτοῖς· ὑγιαίνει; οἱ δὲ εἶπαν· ὑγιαίνει. καὶ ἰδοὺ Ραχὴλ ἡ θυγάτηρ αὐτοῦ ἤρχετο μετὰ τῶν προβάτων.
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

## Genesis 29:7

Greek: καὶ εἶπεν ᾿Ιακώβ· ἔτι ἐστὶν ἡμέρα πολλή, οὔπω ὥρα συναχθῆναι τὰ κτήνη· ποτίσαντες τὰ πρόβατα ἀπελθόντες βόσκετε.
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

## Genesis 29:8

Greek: οἱ δὲ εἶπαν· οὐ δυνησόμεθα ἕως τοῦ συναχθῆναι πάντας τοὺς ποιμένας, καὶ ἀποκυλίσουσι τὸν λίθον ἀπὸ τοῦ στόματος τοῦ φρέατος, καὶ ποτιοῦμεν τὰ πρόβατα.
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

## Genesis 29:9

Greek: ἔτι αὐτοῦ λαλοῦντος αὐτοῖς καὶ ἰδοὺ Ραχὴλ ἡ θυγάτηρ Λάβαν ἤρχετο μετὰ τῶν προβάτων τοῦ πατρὸς αὐτῆς· αὐτὴ γὰρ ἔβοσκε τὰ πρόβατα τοῦ πατρὸς αὐτῆς.
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

## Genesis 29:10

Greek: ἐγένετο δέ, ὡς εἶδεν ᾿Ιακὼβ τὴν Ραχὴλ τὴν θυγατέρα Λάβαν τοῦ ἀδελφοῦ τῆς μητρὸς αὐτοῦ, καὶ τὰ πρόβατα Λάβαν τοῦ ἀδελφοῦ τῆς μητρὸς αὐτοῦ, καὶ προσελθὼν ᾿Ιακὼβ ἀπεκύλισε τὸν λίθον ἀπὸ τοῦ στόματος τοῦ φρέατος καὶ ἐπότιζε τὰ πρόβατα Λάβαν τοῦ ἀδελφοῦ τῆς μητρὸς αὐτοῦ.
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

## Genesis 29:11

Greek: καὶ ἐφίλησεν ᾿Ιακὼβ τὴν Ραχήλ· καὶ βοήσας τῇ φωνῇ αὐτοῦ ἔκλαυσε.
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

## Genesis 29:12

Greek: καὶ ἀπήγγειλε τῇ Ραχήλ, ὅτι ἀδελφὸς τοῦ πατρὸς αὐτῆς ἐστι καὶ ὅτι υἱὸς Ρεβέκκας ἐστί, καὶ δραμοῦσα ἀπήγγειλε τῷ πατρὶ αὐτῆς κατὰ τά ρήματα ταῦτα.
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

## Genesis 29:13

Greek: ἐγένετο δέ, ὡς ἤκουσε Λάβαν τὸ ὄνομα ᾿Ιακὼβ τοῦ υἱοῦ τῆς ἀδελφῆς αὐτοῦ, ἔδραμεν εἰς συνάντησιν αὐτῷ καὶ περιλαβὼν αὐτὸν ἐφίλησε καὶ εἰσήγαγεν αὐτὸν εἰς τὸν οἶκον αὐτοῦ. καὶ διηγήσατο τῷ Λάβαν πάντας τοὺς λόγους τούτους.
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

## Genesis 29:14

Greek: καὶ εἶπεν αὐτῷ Λάβαν· ἐκ τῶν ὀστῶν μου καὶ ἐκ τῆς σαρκός μου εἶ σύ. καὶ ἦν μετ᾿ αὐτοῦ μῆνα ἡμερῶν.
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

## Genesis 29:15

Greek: Εἶπε δὲ Λάβαν τῷ ᾿Ιακώβ· ὅτι γὰρ ἀδελφός μου εἶ, οὐ δουλεύσεις μοι δωρεάν· ἀπάγγειλόν μοι, τίς ὁ μισθός σου ἐστί
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

## Genesis 29:16

Greek: τῷ δὲ Λάβαν ἦσαν δύο θυγατέρες, ὄνομα τῇ μείζονι Λεία, καὶ ὄνομα τῇ νεωτέρᾳ Ραχήλ.
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

## Genesis 29:17

Greek: οἱ δὲ ὀφθαλμοὶ Λείας ἀσθενεῖς, Ραχὴλ δὲ ἦν καλὴ τῷ εἴδει καὶ ὡραία τῇ ὄψει σφόδρα.
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

## Genesis 29:18

Greek: ἠγάπησε δὲ ᾿Ιακὼβ τὴν Ραχὴλ καὶ εἶπε· δουλεύσω σοι ἑπτὰ ἔτη περὶ Ραχὴλ τῆς θυγατρός σου τῆς νεωτέρας.
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

## Genesis 29:19

Greek: εἶπε δὲ αὐτῷ Λάβαν· βέλτιον δοῦναί με αὐτήν σοι, ἢ δοῦναί με αὐτὴν ἀνδρὶ ἑτέρῳ· οἴκησον μετ᾿ ἐμοῦ.
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

## Genesis 29:20

Greek: καὶ ἐδούλευσεν ᾿Ιακὼβ περὶ Ραχὴλ ἑπτὰ ἔτη, καὶ ἦσαν ἐναντίον αὐτοῦ ὡς ἡμέραι ὀλίγαι, παρὰ τὸ ἀγαπᾷν αὐτὸν αὐτήν.
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

## Genesis 29:21

Greek: εἶπε δὲ ᾿Ιακὼβ τῷ Λάβαν· δός μοι τὴν γυναῖκά μου, πεπλήρωνται γὰρ αἱ ἡμέραι, ὅπως εἰσέλθω πρὸς αὐτήν.
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

## Genesis 29:22

Greek: συνήγαγε δὲ Λάβαν πάντας τοὺς ἄνδρας τοῦ τόπου καὶ ἐποίησε γάμον.
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

## Genesis 29:23

Greek: καὶ ἐγένετο ἑσπέρα, καὶ λαβὼν Λείαν τὴν θυγατέρα αὐτοῦ εἰσήγαγε πρὸς ᾿Ιακὼβ καὶ εἰσῆλθε πρὸς αὐτὴν ᾿Ιακώβ.
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

## Genesis 29:24

Greek: ἔδωκε δὲ Λάβαν Λείᾳ τῇ θυγατρὶ αὐτοῦ Ζελφὰν τὴν παιδίσκην αὐτοῦ αὐτῇ παιδίσκην.
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

## Genesis 29:25

Greek: ἐγένετο δὲ πρωΐ, καὶ ἰδοὺ ἦν Λεία. εἶπε δὲ ᾿Ιακὼβ τῷ Λάβαν· τί τοῦτο ἐποίησάς μοι; οὐ περὶ Ραχὴλ ἐδούλευσα παρὰ σοί; καὶ ἱνατί παρελογίσω με
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

## Genesis 29:26

Greek: ἀπεκρίθη δὲ Λάβαν· οὐκ ἔστιν οὕτως ἐν τῷ τόπῳ ἡμῶν, δοῦναι τὴν νεωτέραν πρὶν ἢ τὴν πρεσβυτέραν·
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

## Genesis 29:27

Greek: συντέλεσον οὖν τὰ ἕβδομα ταύτης, καὶ δώσω σοι καὶ ταύτην ἀντὶ τῆς ἐργασίας, ἧς ἐργᾷ παρ᾿ ἐμοί, ἔτι ἑπτὰ ἔτη ἕτερα.
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

## Genesis 29:28

Greek: ἐποίησε δὲ ᾿Ιακὼβ οὕτως καὶ ἀνεπλήρωσε τὰ ἕβδομα ταύτης, καὶ ἔδωκεν αὐτῷ Λάβαν Ραχὴλ τὴν θυγατέρα αὐτοῦ αὐτῷ γυναῖκα.
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

## Genesis 29:29

Greek: ἔδωκε δὲ Λάβαν τῇ θυγατρὶ αὐτοῦ Βαλλὰν τὴν παιδίσκην αὐτοῦ αὐτῇ παιδίσκην.
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

## Genesis 29:30

Greek: καὶ εἰσῆλθε πρὸς Ραχήλ· ἠγάπησε δὲ Ραχὴλ μᾶλλον ἢ Λείαν· καὶ ἐδούλευσεν αὐτῷ ἑπτὰ ἔτη ἕτερα.
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

## Genesis 29:31

Greek: ᾿Ιδὼν δὲ Κύριος ὁ Θεὸς ὅτι ἐμισεῖτο Λεία, ἤνοιξε τὴν μήτραν αὐτῆς· Ραχὴλ δὲ ἦν στεῖρα·
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

## Genesis 29:32

Greek: καὶ συνέλαβε Λεία καὶ ἔτεκεν υἱὸν τῷ ᾿Ιακώβ· ἐκάλεσε δὲ τὸ ὄνομα αὐτοῦ Ρουβὴν λέγουσα· διότι εἶδέ μου Κύριος τὴν ταπείνωσιν, καὶ ἔδωκέ μοι υἱόν· νῦν οὖν ἀγαπήσει με ὁ ἀνήρ μου.
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

## Genesis 29:33

Greek: καὶ συνέλαβε πάλιν καὶ ἔτεκεν υἱὸν δεύτερον τῷ ᾿Ιακὼβ καὶ εἶπεν· ὅτι ἤκουσε Κύριος ὅτι μισοῦμαι, καὶ προσέδωκέ μοι καὶ τοῦτον· ἐκάλεσε δὲ τὸ ὄνομα αὐτοῦ Συμεών·
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

## Genesis 29:34

Greek: καὶ συνέλαβεν ἔτι καὶ ἔτεκεν υἱὸν καὶ εἶπεν· ἐν τῷ νῦν καιρῷ πρὸς ἐμοῦ ἔσται ὁ ἀνήρ μου, τέτοκα γὰρ αὐτῷ τρεῖς υἱούς· διὰ τοῦτο ἐκάλεσε τὸ ὄνομα αὐτοῦ Λευεί.
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

## Genesis 29:35

Greek: καὶ συλλαβοῦσα ἔτι ἔτεκεν υἱὸν καὶ εἶπε· νῦν ἔτι τοῦτο ἐξομολογήσομαι τῷ Κυρίῳ· διὰ τοῦτο ἐκάλεσε τὸ ὄνομα αὐτοῦ ᾿Ιούδαν. καὶ ἔστη τοῦ τίκτειν.
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

# Chapter 30

## Genesis 30:1

Greek: ΙΔΟΥΣΑ δὲ Ραχὴλ ὅτι οὐ τέτοκε τῷ ᾿Ιακώβ, καὶ ἐζήλωσε Ραχὴλ τὴν ἀδελφὴν αὐτῆς καὶ εἶπε τῷ ᾿Ιακώβ· δός μοι τέκνα· εἰ δὲ μή, τελευτήσω ἐγώ.
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

## Genesis 30:2

Greek: θυματωθεὶς δὲ ᾿Ιακὼβ τῇ Ραχὴλ εἶπεν αὐτῇ· μὴ ἀντὶ Θεοῦ ἐγώ εἰμι, ὃς ἐστέρησέ σε καρπὸν κοιλίας
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

## Genesis 30:3

Greek: εἶπε δὲ Ραχὴλ τῷ ᾿Ιακώβ· ἰδοὺ ἡ παιδίσκη μου Βαλλά· εἴσελθε πρὸς αὐτήν, καὶ τέξεται ἐπὶ τῶν γονάτων μου, καὶ τεκνοποιήσομαι κἀγὼ ἐξ αὐτῆς.
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

## Genesis 30:4

Greek: καὶ ἔδωκεν αὐτῷ Βαλλὰν τὴν παιδίσκην αὐτῆς αὐτῷ γυναῖκα· καὶ εἰσῆλθε πρὸς αὐτὴν ᾿Ιακώβ.
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

## Genesis 30:5

Greek: καὶ συνέλαβε Βαλλὰ ἡ παιδίσκη Ραχὴλ καὶ ἔτεκε τῷ ᾿Ιακὼβ υἱόν.
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

## Genesis 30:6

Greek: καὶ εἶπε Ραχήλ· ἔκρινέ μοι ὁ Θεὸς καὶ ἐπήκουσε τῆς φωνῆς μου καὶ ἔδωκέ μοι υἱόν· διὰ τοῦτο ἐκάλεσε τὸ ὄνομα αὐτοῦ Δάν.
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

## Genesis 30:7

Greek: καὶ συνέλαβεν ἔτι Βαλλὰ ἡ παιδίσκη Ραχὴλ καὶ ἔτεκεν υἱὸν δεύτερον τῷ ᾿Ιακώβ.
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

## Genesis 30:8

Greek: καὶ εἶπε Ραχήλ· συναντελάβετό μου ὁ Θεός, καὶ συνανεστράφην τῇ ἀδελφῇ μου καὶ ἠδυνάσθην· καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ Νεφθαλείμ.
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

## Genesis 30:9

Greek: Εἶδε δὲ Λεία ὅτι ἔστη τοῦ τίκτειν, καὶ ἔλαβε Ζελφὰν τὴν παιδίσκην αὐτῆς καὶ ἔδωκεν αὐτὴν τῷ ᾿Ιακὼβ γυναῖκα. καὶ εἰσῆλθε πρὸς αὐτὴν
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

## Genesis 30:10

Greek: καὶ συνέλαβε Ζελφὰ ἡ παιδίσκη Λείας καὶ ἔτεκε τῷ ᾿Ιακὼβ υἱόν.
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

## Genesis 30:11

Greek: καὶ εἶπε Λεία. ἐν τύχῃ· καὶ ἐπωνόμασε τὸ ὄνομα αὐτοῦ Γάδ.
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

## Genesis 30:12

Greek: καὶ συνέλαβεν ἔτι Ζελφὰ ἡ παιδίσκη Λείας καὶ ἔτεκε τῷ ᾿Ιακὼβ υἱὸν δεύτερον.
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

## Genesis 30:13

Greek: καὶ εἶπε Λεία· μακαρία ἐγώ, ὅτι μακαριοῦσί με αἱ γυναῖκες· καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ ᾿Ασήρ.
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

## Genesis 30:14

Greek: ᾿Επορεύθη δὲ Ρουβὴν ἐν ἡμέρᾳ θερισμοῦ πυρῶν καὶ εὗρε μῆλα μανδραγορῶν ἐν τῷ ἀγρῷ καὶ ἤνεγκεν αὐτὰ πρὸς Λείαν τὴν μητέρα αὐτοῦ· εἶπε δὲ Ραχὴλ Λείᾳ τῇ ἀδελφῇ αὐτῆς· δός μοι τῶν μανδραγορῶν τοῦ υἱοῦ σου.
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

## Genesis 30:15

Greek: εἶπε δὲ Λεία· οὐχ ἱκανόν σοι ὅτι ἔλαβες τὸν ἄνδρα μου; μὴ καὶ τοὺς μανδραγόρας τοῦ υἱοῦ μου λήψῃ; εἶπε δὲ Ραχήλ· οὐχ οὕτως· κοιμηθήτω μετὰ σοῦ τὴν νύκτα ταύτην ἀντὶ τῶν μανδραγορῶν τοῦ υἱοῦ σου.
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

## Genesis 30:16

Greek: εἰσῆλθε δὲ ᾿Ιακὼβ ἐξ ἀγροῦ ἑσπέρας, καὶ ἐξῆλθε Λεία εἰς συνάντησιν αὐτῷ καὶ εἶπε· πρὸς ἐμὲ εἰσελεύσῃ σήμερον· μεμίσθωμαι γάρ σε ἀντὶ τῶν μανδραγορῶν τοῦ υἱοῦ μου. καὶ ἐκοιμήθη μετ᾿ αὐτῆς τὴν νύκτα ἐκείνην.
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

## Genesis 30:17

Greek: καὶ ἐπήκουσεν ὁ Θεὸς Λείας, καὶ συλλαβοῦσα ἔτεκε τῷ ᾿Ιακὼβ υἱὸν πέμπτον.
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

## Genesis 30:18

Greek: καὶ εἶπε Λεία· δέδωκέ μοι ὁ Θεὸς τὸν μισθόν μου, ἀνθ᾿ οὗ ἔδωκα τὴν παιδίσκην μου τῷ ἀνδρί μου· καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ ᾿Ισσάχαρ, ὅ ἐστι μισθός.
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

## Genesis 30:19

Greek: καὶ συνέλαβεν ἔτι Λεία καὶ ἔτεκεν υἱὸν ἕκτον τῷ ᾿Ιακώβ.
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

## Genesis 30:20

Greek: καὶ εἶπε Λεία· δεδώρηται ὁ Θεός μοι δῶρον καλὸν ἐν τῷ νῦν καιρῷ· αἱρετιεῖ με ὁ ἀνήρ μου, τέτοκα γὰρ αὐτῷ υἱοὺς ἕξ· καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ Ζαβουλών.
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

## Genesis 30:21

Greek: καὶ μετὰ τοῦτο ἔτεκε θυγατέρα καὶ ἐκάλεσε τὸ ὄνομα αὐτῆς Δείνα.
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

## Genesis 30:22

Greek: ᾿Εμνήσθη δὲ ὁ Θεὸς τῆς Ραχήλ, καὶ ἐπήκουσεν αὐτῆς ὁ Θεὸς καὶ ἀνέῳξεν αὐτῆς τὴν μήτραν,
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

## Genesis 30:23

Greek: καὶ συλλαβοῦσα ἔτεκε τῷ ᾿Ιακὼβ υἱόν. εἶπε δὲ Ραχήλ· ἀφεῖλεν ὁ Θεός μου τὸ ὄνειδος·
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

## Genesis 30:24

Greek: καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ ᾿Ιωσὴφ λέγουσα· προσθέτω ὁ Θεός μοι υἱὸν ἕτερον.
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

## Genesis 30:25

Greek: ᾿Εγένετο δὲ ὡς ἔτεκε Ραχὴλ τὸν ᾿Ιωσήφ, εἶπεν ᾿Ιακὼβ τῷ Λάβαν· ἀπόστειλόν με, ἵνα ἀπέλθω εἰς τὸν τόπον μου καὶ εἰς τὴν γῆν μου.
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

## Genesis 30:26

Greek: ἀπόδος τὰς γυναῖκάς μου καὶ τὰ παιδία μου, περὶ ὧν δεδούλευκά σοι, ἵνα ἀπέλθω· σὺ γὰρ γινώσκεις τὴν δουλείαν, ἣν δεδούλευκά σοι.
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

## Genesis 30:27

Greek: εἶπε δὲ αὐτῷ Λάβαν· εἰ εὗρον χάριν ἐναντίον σου, οἰωνισάμην ἄν· εὐλόγησε γάρ με ὁ Θεὸς ἐπὶ τῇ σῇ εἰσόδῳ.
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

## Genesis 30:28

Greek: διάστειλον τὸν μισθόν σου πρός με, καὶ δώσω.
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

## Genesis 30:29

Greek: εἶπε δὲ ᾿Ιακώβ· σὺ γινώσκεις ἃ δεδούλευκά σοι καὶ ὅσα ἦν κτήνη σου μετ᾿ ἐμοῦ·
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

## Genesis 30:30

Greek: μικρὰ γὰρ ἦν ὅσα σοι ἐναντίον ἐμοῦ, καὶ ηὐξήθη εἰς πλῆθος, καὶ εὐλόγησέ σε Κύριος ὁ Θεὸς ἐπὶ τῷ ποδί μου. νῦν οὖν πότε ποιήσω κἀγὼ ἐμαυτῷ οἶκον
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

## Genesis 30:31

Greek: καὶ εἶπεν αὐτῷ Λάβαν· τί σοι δώσω; εἶπε δὲ αὐτῷ ᾿Ιακώβ· οὐ δώσεις μοι οὐδέν· ἐὰν ποιήσῃς μοι τὸ ρῆμα τοῦτο, πάλιν ποιμανῶ τὰ πρόβατά σου καὶ φυλάξω.
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

## Genesis 30:32

Greek: παρελθέτω πάντα τὰ πρόβατά σου σήμερον, καὶ διαχώρισον ἐκεῖθεν πᾶν πρόβατον φαιὸν ἐν τοῖς ἄρνασι καὶ πᾶν διάλευκον καὶ ραντὸν ἐν ταῖς αἰξίν· ἔσται μοι μισθός.
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

## Genesis 30:33

Greek: καὶ ἐπακούσεταί μοι ἡ δικαιοσύνη μου ἐν τῇ ἡμέρᾳ τῇ ἐπαύριον, ὅτι ἐστὶν ὁ μισθός μου ἐνώπιόν σου· πᾶν, ὃ ἐὰν μὴ ᾖ ραντὸν καὶ διάλευκον ἐν ταῖς αἰξὶ καὶ φαιὸν ἐν τοῖς ἄρνασι, κεκλεμμένον ἔσται παρ᾿ ἐμοί.
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

## Genesis 30:34

Greek: εἶπε δὲ αὐτῷ Λάβαν· ἔστω κατὰ τὸ ρῆμά σου.
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

## Genesis 30:35

Greek: καὶ διέστειλεν ἐν τῇ ἡμέρᾳ ἐκείνῃ τοὺς τράγους τοὺς ραντοὺς καὶ τοὺς διαλεύκους καὶ πάσας τὰς αἶγας τὰς ραντὰς καὶ τὰς διαλεύκους καὶ πᾶν, ὃ ἦν φαιὸν ἐν τοῖς ἄρνασι, καὶ πᾶν ὃ ἦν λευκὸν ἐν αὐτοῖς, καὶ ἔδωκε διὰ χειρὸς τῶν υἱῶν αὐτοῦ.
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

## Genesis 30:36

Greek: καὶ ἀπέστησεν ὁδὸν τριῶν ἡμερῶν ἀνὰ μέσον αὐτῶν καὶ ἀνὰ μέσον ᾿Ιακώβ. ᾿Ιακὼβ δὲ ἐποίμανε τὰ πρόβατα Λάβαν τὰ ὑπολειφθέντα.
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

## Genesis 30:37

Greek: ἔλαβε δὲ ἑαυτῷ ᾿Ιακὼβ ράβδον στυρακίνην χλωρὰν καὶ καρυΐνην καὶ πλατάνου, καὶ ἐλέπισεν αὐτὰς ᾿Ιακὼβ λεπίσματα λευκὰ περισύρων τὸ χλωρόν· ἐφαίνετο δὲ ἐπὶ ταῖς ράβδοις τὸ λευκόν, ὃ ἐλέπισε, ποικίλον.
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

## Genesis 30:38

Greek: καὶ παρέθηκε τὰς ράβδους, ἃς ἐλέπισεν ἐν τοῖς ληνοῖς τῶν ποτιστηρίων τοῦ ὕδατος, ἵνα ὡς ἂν ἔλθωσι τὰ πρόβατα πιεῖν ἐνώπιον τῶν ράβδων, ἐλθόντων αὐτῶν πιεῖν, ἐγκισσήσωσι τὰ πρόβατα εἰς τὰς ράβδους·
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

## Genesis 30:39

Greek: καὶ ἐνεκίσσων τὰ πρόβατα εἰς τὰς ράβδους καὶ ἔτικτον τὰ πρόβατα διάλευκα καὶ ποικίλα καὶ σποδοειδῆ ραντά.
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

## Genesis 30:40

Greek: τοὺς δὲ ἀμνοὺς διέστειλεν ᾿Ιακὼβ καὶ ἔστησεν ἐναντίον τῶν προβάτων κριὸν διάλευκον καὶ πᾶν ποικίλον ἐν τοῖς ἀμνοῖς· καὶ διεχώρισεν ἑαυτῷ ποίμνια καθ᾿ ἑαυτὸν καὶ οὐκ ἔμιξεν αὐτὰ εἰς τὰ πρόβατα Λάβαν.
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

## Genesis 30:41

Greek: ἐγένετο δὲ ἐν τῷ καιρῷ, ᾧ ἐνεκίσσων τὰ πρόβατα ἐν γαστρὶ λαμβάνοντα, ἔθηκεν ᾿Ιακὼβ τὰς ράβδους ἐναντίον τῶν προβάτων ἐν τοῖς ληνοῖς τοῦ ἐγκισσῆσαι αὐτὰ κατὰ τὰς ράβδους·
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

## Genesis 30:42

Greek: ἡνίκα δ᾿ ἂν ἔτεκε τὰ πρόβατα, οὐκ ἐτίθει· ἐγένετο δὲ τὰ μὲν ἄσημα τοῦ Λάβαν, τά δὲ ἐπίσημα τοῦ ᾿Ιακώβ.
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

## Genesis 30:43

Greek: καὶ ἐπλούτισεν ὁ ἄνθρωπος σφόδρα σφόδρα, καὶ ἐγένετο αὐτῷ κτήνη πολλὰ καὶ βόες καὶ παῖδες, καὶ παιδίσκαι καὶ κάμηλοι καὶ ὄνοι.
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

# Chapter 31

## Genesis 31:1

Greek: ΗΚΟΥΣΕ δὲ ᾿Ιακὼβ τὰ ρήματα τῶν υἱῶν Λάβαν λεγόντων· εἴληφεν ᾿Ιακὼβ πάντα τὰ τοῦ πατρὸς ἡμῶν καὶ ἐκ τῶν τοῦ πατρὸς ἡμῶν πεποίηκε πᾶσαν τὴν δόξαν ταύτην.
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

## Genesis 31:2

Greek: καὶ εἶδεν ᾿Ιακὼβ τὸ πρόσωπον τοῦ Λάβαν, καὶ ἰδοὺ οὐκ ἦν πρὸς αὐτὸν ὡσεὶ ἐχθὲς καὶ τρίτην ἡμέραν.
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

## Genesis 31:3

Greek: εἶπε δὲ Κύριος πρὸς ᾿Ιακώβ· ἀποστρέφου εἰς τὴν γῆν τοῦ πατρός σου καὶ εἰς τὴν γενεάν σου, καὶ ἔσομαι μετὰ σοῦ.
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

## Genesis 31:4

Greek: ἀποστείλας δὲ ᾿Ιακὼβ ἐκάλεσε Λείαν καὶ Ραχὴλ εἰς τὸ πεδίον, οὗ ἦν τὰ ποίμνια.
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

## Genesis 31:5

Greek: καὶ εἶπεν αὐταῖς· ὁρῶ ἐγὼ τὸ πρόσωπον τοῦ πατρὸς ὑμῶν, ὅτι οὐκ ἔστι πρὸς ἐμοῦ ὡς ἐχθὲς καὶ τρίτην ἡμέραν· ὁ δὲ Θεὸς τοῦ πατρός μου ἦν μετ᾿ ἐμοῦ.
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

## Genesis 31:6

Greek: καὶ αὐταὶ δὲ οἴδατε, ὅτι ἐν πάσῃ τῇ ἰσχύϊ μου δεδούλευκα τῷ πατρὶ ὑμῶν.
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

## Genesis 31:7

Greek: ὁ δὲ πατὴρ ὑμῶν παρεκρούσατό με καὶ ἤλλαξε τὸν μισθόν μου τῶν δέκα ἀμνῶν, καὶ οὐκ ἔδωκεν αὐτῷ ὁ Θεὸς κακοποιῆσαί με.
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

## Genesis 31:8

Greek: ἐὰν οὕτως εἴπῃ, τὰ ποικίλα ἔσται σου μισθός, καὶ τέξεται πάντα τὰ πρόβατα ποικίλα· ἐὰν δὲ εἴπῃ, τὰ λευκὰ ἔσται σου μισθός, καὶ τέξεται πάντα τὰ πρόβατα λευκά·
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

## Genesis 31:9

Greek: καὶ ἀφείλετο ὁ Θεὸς πάντα τὰ κτήνη τοῦ πατρὸς ὑμῶν καὶ ἔδωκέ μοι αὐτά.
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

## Genesis 31:10

Greek: καὶ ἐγένετο ἡνίκα ἐνεκίσσων τὰ πρόβατα ἐν γαστρὶ λαμβάνοντα, καὶ εἶδον τοῖς ὀφθαλμοῖς μου ἐν τῷ ὕπνῳ, καὶ ἰδοὺ οἱ τράγοι καὶ οἱ κριοὶ ἀναβαίνοντες ἐπὶ τὰ πρόβατα καὶ τὰς αἶγας διάλευκοι καὶ ποικίλοι καὶ σποδοειδεῖς ραντοί.
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

## Genesis 31:11

Greek: καὶ εἶπέ μοι ὁ ἄγγελος τοῦ Θεοῦ καθ᾿ ὕπνον· ᾿Ιακώβ· ἐγὼ δὲ εἶπα· τί ἐστι
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

## Genesis 31:12

Greek: καὶ εἶπεν· ἀνάβλεψον τοῖς ὀφθαλμοῖς σου, καὶ ἰδὲ τοὺς τράγους καὶ τοὺς κριοὺς ἀναβαίνοντας ἐπὶ τὰ πρόβατα καὶ τὰς αἶγας διαλεύκους καὶ ποικίλους καὶ σποδοειδεῖς ραντούς· ἑώρακα γάρ ὅσα σοι Λάβαν ποιεῖ·
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

## Genesis 31:13

Greek: ἐγώ εἰμι ὁ Θεὸς ὁ ὀφθείς σοι ἐν τόπῳ Θεοῦ, οὗ ἤλειψάς μοι ἐκεῖ στήλην καὶ ηὔξω μοι ἐκεῖ εὐχήν· νῦν οὖν ἀνάστηθι καὶ ἔξελθε ἐκ τῆς γῆς ταύτης καὶ ἄπελθε εἰς τὴν γῆν τῆς γενέσεώς σου, καὶ ἔσομαι μετὰ σοῦ.
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

## Genesis 31:14

Greek: καὶ ἀποκριθεῖσαι Ραχὴλ καὶ Λεία εἶπαν αὐτῷ· μή ἐστιν ἡμῖν ἔτι μερὶς ἢ κληρονομία ἐν τῷ οἴκῳ τοῦ πατρὸς ἡμῶν
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

## Genesis 31:15

Greek: οὐχ ὡς αἱ ἀλλότριαι λελογίσμεθα αὐτῷ; πέπρακε γὰρ ἡμᾶς καὶ καταβρώσει κατέφαγε τὸ ἀργύριον ἡμῶν.
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

## Genesis 31:16

Greek: πάντα τὸν πλοῦτον καὶ τὴν δόξαν, ἣν ἀφείλετο ὁ Θεὸς τοῦ πατρὸς ἡμῶν, ἡμῖν ἔσται καὶ τοῖς τέκνοις ἡμῶν. νῦν οὖν ὅσα σοι εἴρηκεν ὁ Θεός, ποίει.
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

## Genesis 31:17

Greek: ᾿Αναστὰς δὲ ᾿Ιακὼβ ἔλαβε τὰς γυναῖκας αὐτοῦ καὶ τὰ παιδία αὐτοῦ ἐπὶ τὰς καμήλους.
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

## Genesis 31:18

Greek: καὶ ἀπήγαγε πάντα τὰ ὑπάρχοντα αὐτῷ, καὶ πᾶσαν τὴν ἀποσκευὴν αὐτοῦ, ἣν περιεποιήσατο ἐν τῇ Μεσοποταμίᾳ, καὶ πάντα τὰ αὐτοῦ ἀπελθεῖν πρὸς ᾿Ισαὰκ τὸν πατέρα αὐτοῦ εἰς γῆν Χαναάν.
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

## Genesis 31:19

Greek: Λάβαν δὲ ᾤχετο κεῖραι τὰ πρόβατα αὐτοῦ· ἔκλεψε δὲ Ραχὴλ τὰ εἴδωλα τοῦ πατρὸς αὐτῆς.
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

## Genesis 31:20

Greek: ἔκρυψε δὲ ᾿Ιακὼβ Λάβαν τὸν Σύρον τοῦ μὴ ἀναγγεῖλαι αὐτῷ, ὅτι ἀποδιδράσκει.
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

## Genesis 31:21

Greek: καὶ ἀπέδρα αὐτὸς καὶ τὰ αὐτοῦ πάντα καὶ διέβη τὸν ποταμὸν καὶ ὥρμησεν εἰς τὸ ὄρος Γαλαάδ.
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

## Genesis 31:22

Greek: ἀνηγγέλη δὲ Λάβαν τῷ Σύρῳ τῇ ἡμέρᾳ τῇ τρίτῃ, ὅτι ἀπέδρα ᾿Ιακώβ,
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

## Genesis 31:23

Greek: καὶ παραλαβὼν τοὺς ἀδελφοὺς αὐτοῦ μεθ᾿ ἑαυτοῦ, ἐδίωξεν ὀπίσω αὐτοῦ ὁδὸν ἡμερῶν ἑπτὰ καὶ κατέλαβεν αὐτὸν ἐν τῷ ὄρει Γαλαάδ.
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

## Genesis 31:24

Greek: ἦλθε δὲ ὁ Θεὸς πρὸς Λάβαν τὸν Σύρον καθ᾿ ὕπνον τὴν νύκτα καὶ εἶπεν αὐτῷ· φύλαξε σεαυτόν, μήποτε λαλήσῃς μετὰ ᾿Ιακὼβ πονηρά.
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

## Genesis 31:25

Greek: καὶ κατέλαβε Λάβαν τὸν ᾿Ιακώβ· ᾿Ιακὼβ δὲ ἔπηξε τὴν σκηνὴν αὐτοῦ ἐν τῷ ὄρει· Λάβαν δὲ ἔστησε τοὺς ἀδελφοὺς αὐτοῦ ἐν τῷ ὄρει Γαλαάδ.
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

## Genesis 31:26

Greek: εἶπε δὲ Λάβαν τῷ ᾿Ιακώβ· τί ἐποίησας; ἱνατί κρυφῇ ἀπέδρας καὶ ἐκλοποφόρησάς με καὶ ἀπήγαγες τὰς θυγατέρας μου ὡς αἰχμαλώτιδας μαχαίρᾳ
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

## Genesis 31:27

Greek: καὶ εἰ ἀνήγγειλάς μοι, ἐξαπέστειλα ἄν σε μετ᾿ εὐφροσύνης καὶ μετὰ μουσικῶν καὶ τυμπάνων καὶ κιθάρας,
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

## Genesis 31:28

Greek: καὶ οὐκ ἠξιώθην καταφιλῆσαι τὰ παιδία μου καὶ τὰς θυγατέρας μου. νῦν δὲ ἀφρόνως ἔπραξας.
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

## Genesis 31:29

Greek: καὶ νῦν ἰσχύει ἡ χείρ μου κακοποιῆσαί σε· ὁ δὲ Θεὸς τοῦ πατρός σου ἐχθὲς εἶπε πρός με λέγων· φύλαξε σεαυτόν, μή ποτε λαλήσῃς μετὰ ᾿Ιακὼβ πονηρά.
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

## Genesis 31:30

Greek: νῦν οὖν πεπόρευσαι· ἐπιθυμίᾳ γὰρ ἐπεθύμησας ἀπελθεῖν εἰς τὸν οἶκον τοῦ πατρός σου· ἱνατί ἔκλεψας τοὺς θεούς μου
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

## Genesis 31:31

Greek: ἀποκριθεὶς δὲ ᾿Ιακὼβ εἶπε τῷ Λάβαν· ὅτι ἐφοβήθην· εἶπα γάρ· μή ποτε ἀφέλῃς τὰς θυγατέρας σου ἀπ᾿ ἐμοῦ καὶ πάντα τὰ ἐμά.
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

## Genesis 31:32

Greek: καὶ εἶπεν ᾿Ιακώβ· παρ᾿ ᾧ ἂν εὕρῃς τοὺς θεούς σου, οὐ ζήσεται ἐναντίον τῶν ἀδελφῶν ἡμῶν· ἐπίγνωθι τί ἐστι παρ᾿ ἐμοὶ τῶν σῶν καὶ λαβέ. καὶ οὐκ ἐπέγνω παρ᾿ αὐτῷ οὐδέν. οὐκ ᾔδει δὲ ᾿Ιακώβ, ὅτι Ραχὴλ ἡ γυνὴ αὐτοῦ ἔκλεψεν αὐτούς.
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

## Genesis 31:33

Greek: εἰσελθὼν δὲ Λάβαν ἠρεύνησεν εἰς τὸν οἶκον Λείας καὶ οὐχ εὗρεν· καὶ ἐξῆλθεν ἐκ τοῦ οἴκου Λείας καὶ ἠρεύνησε τὸν οἶκον ᾿Ιακὼβ καὶ ἐν τῷ οἴκῳ τῶν δύο παιδισκῶν καὶ οὐχ εὗρεν. εἰσῆλθε δὲ καὶ εἰς τὸν οἶκον Ραχήλ.
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

## Genesis 31:34

Greek: Ραχὴλ δὲ ἔλαβε τὰ εἴδωλα καὶ ἐνέβαλεν αὐτὰ εἰς τὰ σάγματα τῆς καμήλου καὶ ἐπεκάθισεν αὐτοῖς.
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

## Genesis 31:35

Greek: καὶ εἶπε τῷ πατρὶ αὐτῆς· μὴ βαρέως φέρε, κύριε· οὐ δύναμαι ἀναστῆναι ἐνώπιόν σου, ὅτι τὰ κατ᾿ ἐθισμὸν τῶν γυναικῶν μοι ἐστίν· ἠρεύνησε δὲ Λάβαν ἐν ὅλῳ τῷ οἴκῳ καὶ οὐχ εὗρε τὰ εἴδωλα.
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

## Genesis 31:36

Greek: ὠργίσθη δὲ ᾿Ιακὼβ καὶ ἐμαχέσατο τῷ Λάβαν· ἀποκριθεὶς δὲ ᾿Ιακὼβ εἶπε τῷ Λάβαν· τί τὸ ἀδίκημά μου καὶ τί τὸ ἁμάρτημά μου, ὅτι κατεδίωξας ὀπίσω μου
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

## Genesis 31:37

Greek: καὶ ὅτι ἠρεύνησας πάντα τὰ σκεύη τοῦ οἴκου μου; τί εὗρες ἀπὸ πάντων τῶν σκευῶν τοῦ οἴκου σου; θές ὧδε ἐνώπιον τῶν ἀδελφῶν σου καὶ τῶν ἀδελφῶν μου, καὶ ἐλεγξάτωσαν ἀνὰ μέσον τῶν δύο ἡμῶν.
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

## Genesis 31:38

Greek: ταῦτά μοι εἴκοσιν ἔτη ἐγώ εἰμι μετὰ σοῦ· τὰ πρόβατά σου καὶ αἱ αἶγές σου οὐκ ἠτεκνώθησαν· κριοὺς τῶν προβάτων σου οὐ κατέφαγον·
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

## Genesis 31:39

Greek: θηριάλωτον οὐκ ἐνήνοχά σοι, ἐγὼ ἀπετίννυον παρ᾿ ἐμαυτοῦ κλέμματα ἡμέρας καὶ κλέμματα νυκτός·
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

## Genesis 31:40

Greek: ἐγενόμην τῆς ἡμέρας συγκαιόμενος τῷ καύματι καὶ τῷ παγετῷ τῆς νυκτός, καὶ ἀφίστατο ὁ ὕπνος μου ἀπὸ τῶν ὀφθαλμῶν μου.
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

## Genesis 31:41

Greek: ταῦτά μοι εἴκοσιν ἔτη ἐγώ εἰμι ἐν τῇ οἰκιίᾳ σου· ἐδούλευσά σοι δεκατέσσαρα ἔτη ἀντὶ τῶν δύο θυγατέρων σου καὶ ἓξ ἔτη ἐν τοῖς προβάτοις σου, καὶ παρελογίσω τὸν μισθόν μου δέκα ἀμνάσιν.
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

## Genesis 31:42

Greek: εἰ μὴ ὁ Θεὸς τοῦ πατρός μου ῾Αβραὰμ καὶ ὁ φόβος ᾿Ισαὰκ ἦν μοι, νῦν ἂν κενόν με ἐξαπέστειλας· τὴν ταπείνωσίν μου καὶ τὸν κόπον τῶν χειρῶν μου εἶδεν ὁ Θεὸς καὶ ἤλεγξέ σε ἐχθές.
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

## Genesis 31:43

Greek: ἀποκριθεὶς δὲ Λάβαν εἶπε τῷ ᾿Ιακώβ· αἱ θυγατέρες θυγατέρες μου, καὶ οἱ υἱοὶ υἱοί μου, καὶ τὰ κτήνη κτήνη μου, καὶ πάντα, ὅσα σὺ ὁρᾷς, ἐμά ἐστι καὶ τῶν θυγατέρων μου· τί ποιήσω ταύταις σήμερον ἢ τοῖς τέκνοις αὐτῶν, οἷς ἔτεκον
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

## Genesis 31:44

Greek: νῦν οὖν δεῦρο διαθώμεθα διαθήκην ἐγώ τε καὶ σύ, καὶ ἔσται εἰς μαρτύριον ἀνὰ μέσον ἐμοῦ καὶ σοῦ, εἶπε δὲ αὐτῷ· ἰδοὺ οὐδεὶς μεθ᾿ ἡμῶν ἐστιν, ἰδέ, ὁ Θεὸς μάρτυς ἀνὰ μέσον ἐμοῦ καὶ σοῦ.
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

## Genesis 31:45

Greek: λαβὼν δὲ ᾿Ιακὼβ λίθον ἔστησεν αὐτὸν στήλην.
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

## Genesis 31:46

Greek: εἶπε δὲ ᾿Ιακὼβ τοῖς ἀδελφοῖς αὐτοῦ· συλλέγετε λίθους. καὶ συνέλεξαν λίθους καὶ ἐποίησαν βουνόν, καὶ ἔφαγον ἐκεῖ ἐπὶ τοῦ βουνοῦ.
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

## Genesis 31:47

Greek: καὶ εἶπεν αὐτῷ Λάβαν· ὁ βουνὸς οὗτος μαρτυρεῖ ἀνὰ μέσον ἐμοῦ καὶ σοῦ σήμερον.
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

## Genesis 31:48

Greek: καὶ ἐκάλεσεν αὐτὸν Λάβαν Βουνὸς τῆς μαρτυρίας. ᾿Ιακὼβ δὲ ἐκάλεσεν αὐτὸν Βουνὸς μάρτυς. εἶπε δὲ Λάβαν τῷ ᾿Ιακώβ· ἰδοὺ ὁ βουνὸς οὗτος καὶ ἡ στήλη, ἣν ἔστησα ἀνὰ μέσον ἐμοῦ καὶ σοῦ, μαρτυρεῖ ὁ βουνὸς οὗτος, καὶ μαρτυρεῖ ἡ στήλη αὕτη· διὰ τοῦτο ἐκλήθη τὸ ὄνομα αὐτοῦ, Βουνὸς μαρτυρεῖ.
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

## Genesis 31:49

Greek: καὶ ἡ ῞Ορασις, ἣν εἶπεν· ἐπίδοι ὁ Θεὸς ἀνὰ μέσον ἐμοῦ καὶ σοῦ, ὅτι ἀποστησόμεθα ἕτερος ἀφ᾿ ἑτέρου.
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

## Genesis 31:50

Greek: εἰ ταπεινώσεις τὰς θυγατέρας μου, εἰ λήψῃ γυναῖκας πρὸς ταῖς θυγατράσι μου, ὅρα, οὐδεὶς μεθ᾿ ἡμῶν ἐστιν ὁρῶν· Θεὸς μάρτυς μεταξὺ ἐμοῦ καὶ μεταξὺ σοῦ.
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

## Genesis 31:51

Greek: καὶ εἶπε Λάβαν τῷ ᾿Ιακώβ· ἰδοὺ ὁ βουνὸς οὗτος καὶ μάρτυς ἡ στήλη αὕτη.
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

## Genesis 31:52

Greek: ἐὰν τε γὰρ ἐγὼ μὴ διαβῶ πρὸς σὲ μηδὲ σὺ διαβῇς πρός με τὸν βουνὸν τοῦτον καὶ τὴν στήλην ταύτην ἐπὶ κακίᾳ,
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

## Genesis 31:53

Greek: ὁ Θεὸς ῾Αβραὰμ καὶ ὁ Θεὸς Ναχὼρ κρινεῖ ἀνὰ μέσον ἡμῶν.
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

## Genesis 31:54

Greek: καὶ ὤμοσεν ᾿Ιακὼβ κατὰ τοῦ φόβου τοῦ πατρὸς αὐτοῦ ᾿Ισαάκ, καὶ ἔθυσε θυσίαν ἐν τῷ ὄρει καὶ ἐκάλεσε τοὺς ἀδελφοὺς αὐτοῦ, καὶ ἔφαγον καὶ ἔπιον καὶ ἐκοιμήθησαν ἐν τῷ ὄρει.
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

## Genesis 31:55

Greek: ἀναστὰς δὲ Λάβαν τὸ πρωΐ κατεφίλησε τοὺς υἱοὺς καὶ τὰς θυγατέρας αὐτοῦ καὶ εὐλόγησεν αὐτούς, καὶ ἀποστραφεὶς Λάβαν ἀπῆλθεν εἰς τὸν τόπον αὐτοῦ.
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

# Chapter 32

## Genesis 32:1

Greek: ΚΑΙ ᾿Ιακὼβ ἀπῆλθεν εἰς τὴν ὁδὸν ἑαυτοῦ. καὶ ἀναβλέψας εἶδε παρεμβολὴν Θεοῦ παρεμβεβληκυῖαν, καὶ συνήντησαν αὐτῷ οἱ ἄγγελοι τοῦ Θεοῦ.
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

## Genesis 32:2

Greek: εἶπε δὲ ᾿Ιακώβ, ἡνίκα εἶδεν αὐτούς· παρεμβολὴ Θεοῦ αὕτη· καὶ ἐκάλεσε τὸ ὄνομα τοῦ τόπου ἐκείνου Παρεμβολαί.
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

## Genesis 32:3

Greek: ᾿Απέστειλε δὲ ᾿Ιακὼβ ἀγγέλους ἔμπροσθεν αὐτοῦ πρὸς ῾Ησαῦ τὸν ἀδελφὸν αὐτοῦ εἰς γῆν Σηείρ, εἰς χώραν ᾿Εδώμ.
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

## Genesis 32:4

Greek: καὶ ἐνετείλατο αὐτοῖς λέγων· οὕτως ἐρεῖτε τῷ κυρίῳ μου ῾Ησαῦ· οὕτως λέγει ὁ παῖς σου ᾿Ιακώβ· μετὰ Λάβαν παρῴκησα, καὶ ἐχρόνισα ἕως τοῦ νῦν,
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

## Genesis 32:5

Greek: καὶ ἐγένοντό μοι βόες καὶ ὄνοι καὶ πρόβατα καὶ παῖδες καὶ παιδίσκαι, καὶ ἀπέστειλα ἀναγγεῖλαι τῷ κυρίῳ μου ῾Ησαῦ, ἵνα εὕρῃ ὁ παῖς σου χάριν ἐναντίον σου.
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

## Genesis 32:6

Greek: καὶ ἀνέστρεψαν οἱ ἄγγελοι πρὸς ᾿Ιακὼβ λέγοντες· ἤλθομεν πρὸς τὸν ἀδελφόν σου ῾Ησαῦ, καὶ ἰδοὺ αὐτὸς ἔρχεται εἰς συνάντησίν σοι καὶ τετρακόσιοι ἄνδρες μετ᾿ αὐτοῦ.
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

## Genesis 32:7

Greek: ἐφοβήθη δὲ ᾿Ιακὼβ σφόδρα, καὶ ἠπορεῖτο. καὶ διεῖλε τὸν λαὸν τὸν μεθ᾿ ἑαυτοῦ καὶ τοὺς βόας καὶ τὰς καμήλους καὶ τὰ πρόβατα εἰς δύο παρεμβολάς,
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

## Genesis 32:8

Greek: καὶ εἶπεν ᾿Ιακώβ· ἐὰν ἔλθῃ ῾Ησαῦ εἰς παρεμβολὴν μίαν καὶ κόψῃ αὐτήν, ἔσται ἡ παρεμβολὴ ἡ δευτέρα εἰς τὸ σώζεσθαι.
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

## Genesis 32:9

Greek: εἶπε δὲ ᾿Ιακώβ· ὁ Θεὸς τοῦ πατρός μου ῾Αβραὰμ καὶ ὁ Θεὸς τοῦ πατρός μου ᾿Ισαάκ, Κύριε σὺ ὁ εἰπών μοι, ἀπότρεχε εἰς τὴν γῆν τῆς γενέσεώς σου καὶ εὖ σε ποιήσω,
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

## Genesis 32:10

Greek: ἱκανούσθω μοι ἀπὸ πάσης δικαιοσύνης καὶ ἀπὸ πάσης ἀληθείας, ἧς ἐποίησας τῷ παιδί σου· ἐν γὰρ τῇ ῥάβδῳ μου ταύτῃ διέβην τὸν ᾿Ιορδάνην τοῦτον, νυνὶ δὲ γέγονα εἰς δύο παρεμβολάς.
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

## Genesis 32:11

Greek: ἐξελοῦ με ἐκ χειρὸς τοῦ ἀδελφοῦ μου, ἐκ χειρὸς ῾Ησαῦ, ὅτι φοβοῦμαι ἐγὼ αὐτόν, μή ποτε ἐλθὼν πατάξῃ με καὶ μητέρα ἐπὶ τέκνοις.
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

## Genesis 32:12

Greek: σὺ δὲ εἶπας· εὖ σε ποιήσω καὶ θήσω τὸ σπέρμα σου ὡς τὴν ἄμμον τῆς θαλάσσης, ἣ οὐκ ἀριθμηθήσεται ἀπὸ τοῦ πλήθους.
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

## Genesis 32:13

Greek: καὶ ἐκοιμήθη ἐκεῖ τὴν νύκτα ἐκείνην. καὶ ἔλαβεν ὧν ἔφερε δῶρα καὶ ἐξαπέστειλεν ῾Ησαῦ τῷ ἀδελφῷ αὐτοῦ,
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

## Genesis 32:14

Greek: αἶγας διακοσίας, τράγους εἴκοσι, πρόβατα διακόσια, κριοὺς εἴκοσι,
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

## Genesis 32:15

Greek: καμήλους θηλαζούσας, καὶ τὰ παιδία αὐτῶν τριάκοντα, βόας τεσσαράκοντα, ταύρους δέκα, ὄνους εἴκοσι καὶ πώλους δέκα.
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

## Genesis 32:16

Greek: καὶ ἔδωκεν αὐτὰ τοῖς παισὶν αὐτοῦ ποίμνιον κατὰ μόνας. εἶπε δὲ τοῖς παισὶν αὐτοῦ· προπορεύεσθε ἔμπροσθέν μου, καὶ διάστημα ποιεῖτε ἀνὰ μέσον ποίμνης καὶ ποίμνης.
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

## Genesis 32:17

Greek: καὶ ἐνετείλατο τῷ πρώτῳ, λέγων· ἐάν σοι συναντήσῃ ῾Ησαῦ ὁ ἀδελφός μου καὶ ἐρωτᾷ σε, λέγων· τίνος εἶ καὶ ποῦ πορεύῃ, καὶ τίνος ταῦτα τὰ προπορευόμενά σου
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

## Genesis 32:18

Greek: ἐρεῖς· τοῦ παιδός σου ᾿Ιακώβ· δῶρα ἀπέσταλκε τῷ κυρίῳ μου ῾Ησαῦ, καὶ ἰδοὺ αὐτὸς ὀπίσω ἡμῶν.
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

## Genesis 32:19

Greek: καὶ ἐνετείλατο τῷ πρώτῳ καὶ τῷ δευτέρῳ καὶ τῷ τρίτῳ καὶ πᾶσι τοῖς προπορευομένοις ὀπίσω τῶν ποιμνίων τούτων, λέγων· κατὰ τὸ ρῆμα τοῦτο λαλήσατε ῾Ησαῦ ἐν τῷ εὑρεῖν ὑμᾶς αὐτὸν
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

## Genesis 32:20

Greek: καὶ ἐρεῖτε· ἰδοὺ ὁ παῖς σου ᾿Ιακὼβ παραγίνεται ὀπίσω ἡμῶν. εἶπε γάρ· ἐξιλάσομαι τὸ πρόσωπον αὐτοῦ ἐν τοῖς δώροις τοῖς προπορευομένοις αὐτοῦ, καὶ μετὰ τοῦτο ὄψομαι τὸ πρόσωπον αὐτοῦ· ἴσως γὰρ προσδέξεται τὸ πρόσωπόν μου.
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

## Genesis 32:21

Greek: καὶ προεπορεύετο τὰ δῶρα κατὰ πρόσωπον αὐτοῦ, αὐτὸς δὲ ἐκοιμήθη τὴν νύκτα ἐκείνην ἐν τῇ παρεμβολῇ.
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

## Genesis 32:22

Greek: ᾿Αναστὰς δὲ τὴν νύκτα ἐκείνην ἔλαβε τὰς δύο γυναῖκας καὶ τὰς δύο παιδίσκας καὶ τὰ ἕνδεκα παιδία αὐτοῦ καὶ διέβη τὴν διάβασιν τοῦ ᾿Ιαβώκ·
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

## Genesis 32:23

Greek: καὶ ἔλαβεν αὐτοὺς καὶ διέβη τὸν χειμάρρουν καὶ διεβίβασε πάντα τὰ αὐτοῦ.
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

## Genesis 32:24

Greek: ὑπελείφθη δὲ ᾿Ιακὼβ μόνος, καὶ ἐπάλαιεν ἄνθρωπος μετ᾿ αὐτοῦ ἕως πρωΐ.
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

## Genesis 32:25

Greek: εἶδε δέ, ὅτι οὐ δύναται πρὸς αὐτόν, καὶ ἥψατο τοῦ πλάτους τοῦ μηροῦ αὐτοῦ, καὶ ἐνάρκησε τὸ πλάτος τοῦ μηροῦ ᾿Ιακὼβ ἐν τῷ παλαίειν αὐτὸν μετ᾿ αὐτοῦ.
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

## Genesis 32:26

Greek: καὶ εἶπεν αὐτῷ· ἀπόστειλόν με· ἀνέβη γὰρ ὁ ὄρθρος. ὁ δὲ εἶπεν· οὐ μή σε ἀποστείλω, ἐὰν μή με εὐλογήσῃς.
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

## Genesis 32:27

Greek: εἶπε δὲ αὐτῷ· τί τὸ ὄνομά σου ἐστίν, ὁ δὲ εἶπεν· ᾿Ιακώβ.
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

## Genesis 32:28

Greek: καὶ εἶπεν αὐτῷ· οὐ κληθήσεται ἔτι τὸ ὄνομά σου ᾿Ιακώβ, ἀλλ᾿ ᾿Ισραὴλ ἔσται τὸ ὄνομά σου, ὅτι ἐνίσχυσας μετὰ Θεοῦ, καὶ μετ᾿ ἀνθρώπων δυνατὸς ἔσῃ.
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

## Genesis 32:29

Greek: ἠρώτησε δὲ ᾿Ιακὼβ καὶ εἶπεν· ἀνάγγειλόν μοι τὸ ὄνομά σου. καὶ εἶπεν· ἱνατί τοῦτο ἐρωτᾶς σὺ τὸ ὄνομά μου; καὶ εὐλόγησεν αὐτὸν ἐκεῖ.
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

## Genesis 32:30

Greek: καὶ ἐκάλεσεν ᾿Ιακὼβ τὸ ὄνομα τοῦ τόπου ἐκείνου, Εἶδος Θεοῦ· εἶδον γὰρ Θεὸν πρόσωπον πρὸς πρόσωπον, καὶ ἐσώθη μου ἡ ψυχή.
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

## Genesis 32:31

Greek: ἀνέτειλε δὲ αὐτῷ ὁ ἥλιος, ἡνίκα παρῆλθε τὸ εἶδος τοῦ Θεοῦ· αὐτὸς δέ ἐπέσκαζε τῷ μηρῷ αὐτοῦ·
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

## Genesis 32:32

Greek: ἕνεκεν τούτου οὐ μὴ φάγωσιν υἱοὶ ᾿Ισραὴλ τὸ νεῦρον, ὃ ἐνάρκησεν, ὅ ἐστιν ἐπὶ τοῦ πλάτους τοῦ μηροῦ, ἕως τῆς ἡμέρας ταύτης, ὅτι ἥψατο τοῦ πλάτους τοῦ μηροῦ ᾿Ιακὼβ τοῦ νεύρου, ὃ ἐνάρκησεν.
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

# Chapter 33

## Genesis 33:1

Greek: ΑΝΑΒΛΕΨΑΣ δὲ ᾿Ιακὼβ τοῖς ὀφθαλμοῖς αὐτοῦ εἶδε καὶ ἰδοὺ ῾Ησαῦ ὁ ἀδελφὸς αὐτοῦ ἐρχόμενος καὶ τετρακόσιοι ἄνδρες μετ᾿ αὐτοῦ. καὶ διεῖλεν ᾿Ιακὼβ τὰ παιδία ἐπὶ Λείαν καὶ ἐπί Ραχὴλ καὶ τὰς δύος παιδίσκας.
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

## Genesis 33:2

Greek: καὶ ἔθετο τὰς δύο παιδίσκας καὶ τοὺς υἱοὺς αὐτῶν ἐν πρώτοις καὶ Λείαν καὶ τὰ παιδία αὐτῆς ὀπίσω καὶ Ραχὴλ καὶ ᾿Ιωσὴφ ἐσχάτους.
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

## Genesis 33:3

Greek: αὐτὸς δὲ προῆλθεν ἔμπροσθεν αὐτῶν καὶ προσεκύνησεν ἐπὶ τὴν γῆν ἑπτάκις ἕως τοῦ ἐγγίσαι τῷ ἀδελφῷ αὐτοῦ.
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

## Genesis 33:4

Greek: καὶ προσέδραμεν ῾Ησαῦ εἰς συνάντησιν αὐτῷ καὶ περιλαβὼν αὐτὸν προσέπεσεν ἐπὶ τὸν τράχηλον αὐτοῦ καὶ κατεφίλησεν αὐτὸν καὶ ἔκλαυσαν ἀμφότεροι.
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

## Genesis 33:5

Greek: καὶ ἀναβλέψας ῾Ησαῦ εἶδε τὰς γυναῖκας καὶ τὰ παιδία καὶ εἶπε· τί ταῦτά σοι ἐστίν; ὁ δὲ εἶπε· τὰ παιδία, οἷς ἠλέησεν ὁ Θεὸς τὸν παῖδά σου.
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

## Genesis 33:6

Greek: καὶ προσήγγισαν αἱ παιδίσκαι καὶ τὰ τέκνα αὐτῶν καὶ προσεκύνησαν,
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

## Genesis 33:7

Greek: καὶ προσήγγισε Λεία καὶ τὰ τέκνα αὐτῆς καὶ προσεκύνησαν. καὶ μετὰ ταῦτα προσήγγισε Ραχὴλ καὶ ᾿Ιωσὴφ καὶ προσεκύνησαν.
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

## Genesis 33:8

Greek: καὶ εἶπε· τί ταῦτά σοι ἐστί, πᾶσαι αἱ παρεμβολαί αὗται, αἷς ἀπήντηκα; ὁ δὲ εἶπεν· ἵνα εὕρῃ ὁ παῖς σου χάριν ἐναντίον σου, κύριε.
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

## Genesis 33:9

Greek: εἶπε δὲ ῾Ησαῦ· ἔστι μοι πολλά, ἀδελφέ· ἔστω σοι τὰ σά.
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

## Genesis 33:10

Greek: εἶπε δὲ ᾿Ιακώβ· εἰ εὗρον χάριν ἐναντίον σου, δέξαι τὰ δῶρα διὰ τῶν ἐμῶν χειρῶν· ἕνεκεν τούτου εἶδον τὸ πρόσωπόν σου, ὡς ἄν τις ἴδοι πρόσωπον Θεοῦ, καὶ εὐδοκήσεις με.
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

## Genesis 33:11

Greek: λαβὲ τὰς εὐλογίας μου, ἃς ἤνεγκά σοι, ὅτι ἠλέησέ με ὁ Θεὸς καὶ ἔστι μοι πάντα. καὶ ἐβιάσατο αὐτὸν καὶ ἔλαβε·
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

## Genesis 33:12

Greek: καὶ εἶπεν· ἀπάραντες πορευσώμεθα ἐπ᾿ εὐθεῖαν.
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

## Genesis 33:13

Greek: εἶπε δὲ αὐτῷ· ὁ κύριός μου γινώσκει, ὅτι τὰ παιδία ἁπαλώτερα καὶ τὰ πρόβατα καὶ αἱ βόες λοχεύονται ἐπ᾿ ἐμέ· ἐὰν οὖν καταδιώξω αὐτὰ ἡμέραν μίαν, ἀποθανοῦνται πάντα τὰ κτήνη.
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

## Genesis 33:14

Greek: προελθέτω ὁ κύριός μου ἔμπροσθεν τοῦ παιδὸς αὐτοῦ, ἐγὼ δὲ ἐνισχύσω ἐν τῇ ὁδῷ κατὰ σχολὴν τῆς πορεύσεως τῆς ἐναντίον μου καὶ κατὰ πόδα τῶν παιδαρίων, ἕως τοῦ ἐλθεῖν με πρὸς τὸν κύριόν μου εἰς Σηείρ.
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

## Genesis 33:15

Greek: εἶπε δὲ ῾Ησαῦ· καταλείψω μετὰ σοῦ ἀπὸ τοῦ λαοῦ τοῦ μετ᾿ ἐμοῦ. ὁ δὲ εἶπεν· ἱνατί τοῦτο; ἱκανόν, ὅτι εὗρον χάριν ἐναντίον σου, κύριε.
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

## Genesis 33:16

Greek: ἀπέστρεψε δὲ ῾Ησαῦ ἐν τῇ ἡμέρᾳ ἐκείνῃ εἰς τὴν ὁδὸν αὐτοῦ εἰς Σηείρ.
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

## Genesis 33:17

Greek: Καὶ ᾿Ιακὼβ ἀπαίρει εἰς σκηνάς· καὶ ἐποίησεν ἑαυτῷ ἐκεῖ οἰκίας καὶ τοῖς κτήνεσιν αὐτοῦ ἐποίησε σκηνάς· διὰ τοῦτο ἐκάλεσε τὸ ὄνομα τοῦ τόπου ἐκείνου, Σκηναί.
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

## Genesis 33:18

Greek: καὶ ἦλθεν ᾿Ιακὼβ εἰς Σαλὴμ πόλιν Σικίμων, ἥ ἐστιν ἐν γῇ Χαναάν, ὅτε ἐπανῆλθεν ἐκ τῆς Μεσοποταμίας Συρίας, καὶ παρενέβαλε κατὰ πρόσωπον τῆς πόλεως.
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

## Genesis 33:19

Greek: καὶ ἐκτήσατο τὴν μερίδα τοῦ ἀγροῦ, οὗ ἔστησεν ἐκεῖ τὴν σκηνὴν αὐτοῦ, παρὰ ᾿Εμὼρ πατρὸς Συχὲμ ἑκατὸν ἀμνῶν.
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

## Genesis 33:20

Greek: καὶ ἔστησεν ἐκεῖ θυσιαστήριον καὶ ἐπεκαλέσατο τὸν Θεὸν ᾿Ισραήλ.
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

# Chapter 34

## Genesis 34:1

Greek: ΕΞΗΛΘΕ δὲ Δείνα ἡ θυγάτηρ Λείας, ἣν ἔτεκε τῷ ᾿Ιακώβ, καταμαθεῖν τὰς θυγατέρας τῶν ἐγχωρίων.
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

## Genesis 34:2

Greek: καὶ εἶδεν αὐτὴν Συχὲμ ὁ υἱὸς ᾿Εμμὼρ ὁ Εὐαῖος, ὁ ἄρχων τῆς γῆς καὶ λαβὼν αὐτήν, ἐκοιμήθη μετ᾿ αὐτῆς καὶ ἐταπείνωσεν αὐτήν.
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

## Genesis 34:3

Greek: καὶ προσέσχε τῇ ψυχῇ Δείνας τῆς θυγατρὸς ᾿Ιακὼβ καὶ ἠγάπησε τὴν παρθένον καὶ ἐλάλησε κατὰ τὴν διάνοιαν τῆς παρθένου αὐτῇ.
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

## Genesis 34:4

Greek: εἶπε Συχὲμ πρὸς ᾿Εμμὼρ τὸν πατέρα αὐτοῦ λέγων· λαβέ μοι τὴν παῖδα ταύτην εἰς γυναῖκα.
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

## Genesis 34:5

Greek: ᾿Ιακὼβ δὲ ἤκουσεν, ὅτι ἐμίανεν ὁ υἱὸς ᾿Εμμὼρ Δείναν τὴν θυγατέρα αὐτοῦ· οἱ δὲ υἱοὶ αὐτοῦ ἦσαν μετὰ τῶν κτηνῶν αὐτοῦ ἐν τῷ πεδίῳ. παρεσιώπησε δὲ ᾿Ιακὼβ ἕως τοῦ ἐλθεῖν αὐτούς.
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

## Genesis 34:6

Greek: ἐξῆλθε δὲ ᾿Εμμὼρ ὁ πατὴρ Συχὲμ πρὸς ᾿Ιακὼβ λαλῆσαι αὐτῷ.
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

## Genesis 34:7

Greek: οἱ δὲ υἱοὶ ᾿Ιακὼβ ἦλθον ἐκ τοῦ πεδίου· ὡς δὲ ἤκουσαν, κατενύγησαν οἱ ἄνδρες, καὶ λυπηρὸν ἦν αὐτοῖς σφόδρα, ὅτι ἄσχημον ἐποίησεν ἐν ᾿Ισραὴλ κοιμηθεὶς μετὰ τῆς θυγατρός ᾿Ιακώβ, καὶ οὐχ οὕτως ἔσται.
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

## Genesis 34:8

Greek: καὶ ἐλάλησεν ᾿Εμμὼρ αὐτοῖς λέγων· Συχὲμ ὁ υἱός μου προείλετο τῇ ψυχῇ τὴν θυγατέρα ὑμῶν· δότε οὖν αὐτὴν αὐτῷ γυναῖκα
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

## Genesis 34:9

Greek: καὶ ἐπιγαμβρεύσασθε ἡμῖν· τὰς θυγατέρας ὑμῶν δότε ἡμῖν καὶ τὰς θυγατέρας ἡμῶν λάβετε τοῖς υἱοῖς ὑμῶν.
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

## Genesis 34:10

Greek: καὶ ἐν ἡμῖν κατοικεῖτε, καὶ ἡ γῆ ἰδοὺ πλατεῖα ἐναντίον ὑμῶν· κατοικεῖτε καὶ ἐμπορεύεσθε ἐπ᾿ αὐτῆς καὶ ἐγκτᾶσθε ἐν αὐτῇ.
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

## Genesis 34:11

Greek: εἶπε δὲ Συχὲμ πρὸς τὸν πατέρα αὐτῆς καὶ πρὸς τοὺς ἀδελφοὺς αὐτῆς· εὕροιμι χάριν ἐναντίον ὑμῶν, καὶ ὃ ἐὰν εἴπητε, δώσομεν.
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

## Genesis 34:12

Greek: πληθύνατε τὴν φερνὴν σφόδρα, καὶ δώσω καθότι ἂν εἴπητέ μοι, καὶ δώσατέ μοι τὴν παῖδα ταύτην εἰς γυναῖκα.
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

## Genesis 34:13

Greek: ἀπεκρίθησαν δὲ οἱ υἱοὶ ᾿Ιακὼβ τῷ Συχὲμ καὶ ᾿Εμμὼρ τῷ πατρὶ αὐτοῦ μετὰ δόλου καὶ ἐλάλησαν αὐτοῖς, ὅτι ἐμίαναν Δείνα τὴν ἀδελφὴν αὐτῶν,
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

## Genesis 34:14

Greek: καὶ εἶπαν αὐτοῖς Συμεὼν καὶ Λευὶ οἱ ἀδελφοὶ Δείνας· οὐ δυνησόμεθα ποιῆσαι τὸ ρῆμα τοῦτο, δοῦναι τὴν ἀδελφὴν ἡμῶν ἀνθρώπῳ, ὃς ἔχει ἀκροβυστίαν· ἔστι γὰρ ὄνειδος ἡμῖν.
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

## Genesis 34:15

Greek: μόνον ἐν τούτῳ ὁμοιωθησόμεθα ὑμῖν καΙ κατοικήσομεν ἐν ὑμῖν, ἐὰν γένησθε ὡς ἡμεῖς καὶ ὑμεῖς ἐν τῷ περιτμηθῆναι ὑμῶν πᾶν ἀρσενικόν.
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

## Genesis 34:16

Greek: καὶ δώσομεν τὰς θυγατέρας ἡμῶν ὑμῖν καὶ ἀπό τῶν θυγατέρων ὑμῶν ληψόμεθα ἡμῖν γυναῖκας καὶ οἰκήσομεν παρ᾿ ὑμῖν καὶ ἐσόμεθα ὡς γένος ἕν.
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

## Genesis 34:17

Greek: ἐὰν δὲ μὴ εἰσακούσητε ἡμῶν τοῦ περιτεμέσθαι, λαβόντες τὴν θυγατέρα ἡμῶν ἀπελευσόμεθα.
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

## Genesis 34:18

Greek: καὶ ἤρεσαν οἱ λόγοι ἐναντίον ᾿Εμμὼρ καὶ ἐναντίον Συχὲμ τοῦ υἱοῦ ᾿Εμμώρ.
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

## Genesis 34:19

Greek: καὶ οὐκ ἐχρόνισεν ὁ νεανίσκος τοῦ ποιῆσαι τὸ ρῆμα τοῦτο· ἐνέκειτο γὰρ τῇ θυγατρὶ ᾿Ιακώβ· αὐτὸς δὲ ἦν ἐνδοξότατος πάντων τῶν ἐν τῷ οἴκῳ τοῦ πατρὸς αὐτοῦ.
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

## Genesis 34:20

Greek: ἦλθε δὲ ᾿Εμμὼρ καὶ Συχὲμ ὁ υἱὸς αὐτοῦ πρὸς τὴν πύλην τῆς πόλεως αὐτῶν καὶ ἐλάλησαν πρὸς τοὺς ἄνδρας τῆς πόλεως αὐτῶν λέγοντες·
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

## Genesis 34:21

Greek: οἱ ἄνθρωποι οὗτοι εἰρηνικοί εἰσι, μεθ᾿ ἡμῶν οἰκείτωσαν ἐπὶ τῆς γῆς καὶ ἐμπορευέσθωσαν αὐτήν, ἡ δὲ γῆ ἰδοὺ πλατεῖα ἐναντίον αὐτῶν. τὰς θυγατέρας αὐτῶν ληψόμεθα ἡμῖν γυναῖκας καὶ τὰς θυγατέρας ἡμῶν δώσομεν αὐτοῖς.
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

## Genesis 34:22

Greek: ἐν τούτῳ μόνον ὁμοιωθήσονται ἡμῖν οἱ ἄνθρωποι τοῦ κατοικεῖν μεθ᾿ ἡμῶν, ὥστε εἶναι λαὸν ἕνα, ἐν τῷ περιτεμέσθαι ἡμῶν πᾶν ἀρσενικόν, καθὰ καὶ αὐτοὶ περιτέτμηνται.
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

## Genesis 34:23

Greek: καὶ τὰ κτήνη αὐτῶν καὶ τὰ τετράποδα καὶ τὰ ὑπάρχοντα αὐτῶν οὐχ ἡμῶν ἔσται· μόνον ἐν τούτῳ ὁμοιωθῶμεν αὐτοῖς, καὶ οἰκήσουσι μεθ᾿ ἡμῶν.
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

## Genesis 34:24

Greek: καὶ εἰσήκουσαν ᾿Εμμὼρ καὶ Συχὲμ τοῦ υἱοῦ αὐτοῦ πάντες οἱ ἐμπορευόμενοι τὴν πύλην τῆς πόλεως αὐτῶν καὶ περιετέμοντο τὴν σάρκα τῆς ἀκροβυστίας αὐτῶν πᾶς ἄρσην.
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

## Genesis 34:25

Greek: ἐγένετο δὲ ἐν τῇ ἡμέρᾳ τῇ τρίτῃ, ὅτε ἦσαν ἐν τῷ πόνῳ, ἔλαβον οἱ δύο υἱοὶ ᾿Ιακὼβ Συμεὼν καὶ Λευὶ ἀδελφοὶ Δείνας ἕκαστος τὴν μάχαιραν αὐτοῦ καὶ εἰσῆλθον εἰς τὴν πόλιν ἀσφαλῶς καὶ ἀπέκτειναν πᾶν ἀρσενικόν·
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

## Genesis 34:26

Greek: τόν τε ᾿Εμμὼρ καὶ Συχὲμ τὸν υἱὸν αὐτοῦ ἀπέκτειναν ἐν στόματι μαχαίρας. καὶ ἔλαβον τὴν Δείναν ἐκ τοῦ οἴκου τοῦ Συχὲμ καὶ ἐξῆλθον.
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

## Genesis 34:27

Greek: οἱ δὲ υἱοὶ ᾿Ιακὼβ εἰσῆλθον ἐπὶ τοὺς τραυματίας καὶ διήρπασαν τὴν πόλιν, ἐν ᾗ ἐμίαναν Δείναν τὴν ἀδελφὴν αὐτῶν,
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

## Genesis 34:28

Greek: καὶ τὰ πρόβατα αὐτῶν καὶ τοὺς βόας αὐτῶν καὶ τοὺς ὄνους αὐτῶν, ὅσα τε ἦν ἐν τῇ πόλει καὶ ὅσα ἦν ἐν τῷ πεδίῳ, ἔλαβον.
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

## Genesis 34:29

Greek: καὶ πάντα τὰ σώματα αὐτῶν καὶ πᾶσαν τὴν ἀποσκευὴν αὐτῶν καὶ τὰς γυναῖκας αὐτῶν ᾐχμαλώτευσαν, καὶ διήρπασαν ὅσα τε ἦν ἐν τῇ πόλει καὶ ὅσα ἦν ἐν ταῖς οἰκίαις.
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

## Genesis 34:30

Greek: εἶπε δὲ ᾿Ιακὼβ πρὸς Συμεὼν καὶ Λευί· μισητόν με πεποιήκατε, ὥστε πονηρόν με εἶναι πᾶσι τοῖς κατοικοῦσι τὴν γῆν, ἔν τε τοῖς Χαναναίοις καὶ ἐν τοῖς Φερεζαίοις· ἐγὼ δὲ ὀλιγοστός εἰμι ἐν ἀριθμῷ, καὶ συναχθέντες ἐπ᾿ ἐμὲ συγκόψουσί με, καὶ ἐκτριβήσομαι ἐγὼ καὶ ὁ οἶκός μου.
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

## Genesis 34:31

Greek: οἱ δὲ εἶπαν· ἀλλ᾿ ὡσεὶ πόρνῃ χρήσονται τῇ ἀδελφῇ ἡμῶν
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

# Chapter 35

## Genesis 35:1

Greek: ΕΙΠΕ δὲ ὁ Θεὸς πρὸς ᾿Ιακώβ· ἀναστὰς ἀνάβηθι εἰς τὸν τόπον Βαιθὴλ καὶ οἴκει ἐκεῖ καὶ ποίησον ἐκεῖ θυσιαστήριον τῷ Θεῷ τῷ ὀφθέντι σοι ἐν τῷ ἀποδιδράσκειν σε ἀπὸ προσώπου ῾Ησαῦ τοῦ ἀδελφοῦ σου.
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

## Genesis 35:2

Greek: εἶπε δὲ ᾿Ιακὼβ τῷ οἴκῳ αὐτοῦ καὶ πᾶσι τοῖς μετ᾿ αὐτοῦ· ἄρατε τοὺς θεοὺς τοὺς ἀλλοτρίους τοὺς μεθ᾿ ὑμῶν ἐκ μέσου ὑμῶν καὶ καθαρίσθητε καὶ ἀλλάξατε τὰς στολὰς ὑμῶν,
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

## Genesis 35:3

Greek: καὶ ἀναστάντες ἀναβῶμεν εἰς Βαιθὴλ καὶ ποιήσωμεν ἐκεῖ θυσιαστήριον τῷ Θεῷ τῷ ἐπακούσαντί μου ἐν ἡμέρᾳ θλίψεως, ὃς ἦν μετ᾿ ἐμοῦ καὶ διέσωσέ με ἐν τῇ ὁδῷ, ᾗ ἐπορεύθην.
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

## Genesis 35:4

Greek: καὶ ἔδωκαν τῷ ᾿Ιακὼβ τοὺς θεοὺς τοὺς ἀλλοτρίους, οἳ ἦσαν ἐν ταῖς χερσὶν αὐτῶν, καὶ τὰ ἐνώτια τὰ ἐν τοῖς ὠσὶν αὐτῶν, καὶ κατέκρυψεν αὐτὰ ᾿Ιακὼβ ὑπὸ τὴν τερέβινθον τὴν ἐν Σικίμοις καὶ ἀπώλεσαν αὐτὰ ἕως τῆς σήμερον ἡμέρας.
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

## Genesis 35:5

Greek: καὶ ἐξῇρεν ᾿Ισραὴλ ἐκ Σικίμων, καὶ ἐγένετο φόβος Θεοῦ ἐπὶ τὰς πόλεις τὰς κύκλῳ αὐτῶν, καὶ οὐ κατεδίωξαν ὀπίσω τῶν υἱῶν ᾿Ισραήλ.
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

## Genesis 35:6

Greek: ἦλθε δὲ ᾿Ιακὼβ εἰς Λουζά, ἥ ἐστιν ἐν γῇ Χαναάν, ἥ ἐστι Βαιθήλ, αὐτὸς καὶ πᾶς ὁ λαός, ὃς ἦν μετ᾿ αὐτοῦ.
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

## Genesis 35:7

Greek: καὶ ᾠκοδόμησεν ἐκεῖ θυσιαστήριον καὶ ἐκάλεσε τὸ ὄνομα τοῦ τόπου Βαιθήλ. ἐκεῖ γὰρ ἐφάνη αὐτῷ ὁ Θεὸς ἐν τῷ ἀποδιδράσκειν αὐτὸν ἀπὸ προσώπου ῾Ησαῦ τοῦ ἀδελφοῦ αὐτοῦ.
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

## Genesis 35:8

Greek: ἀπέθανε δὲ Δεβῶρα ἡ τροφὸς Ρεβέκκας καὶ ἐτάφη κατώτερον Βαιθὴλ ὑπὸ τὴν βάλανον, καὶ ἐκάλεσεν ᾿Ιακὼβ τὸ ὄνομα αὐτῆς Βάλανος πένθους.
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

## Genesis 35:9

Greek: ῎Ωφθη δὲ ὁ Θεὸς τῷ ᾿Ιακὼβ ἔτι ἐν Λουζᾷ, ὅτε παρεγένετο ἐκ Μεσοποταμίας τῆς Συρίας, καὶ εὐλόγησεν αὐτὸν ὁ Θεός.
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

## Genesis 35:10

Greek: καὶ εἶπεν αὐτῷ ὁ Θεός· τὸ ὄνομά σου οὐ κληθήσεται ἔτι ᾿Ιακώβ, ἀλλ᾿ ᾿Ισραὴλ ἔσται τὸ ὄνομά σου. καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ ᾿Ισραήλ.
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

## Genesis 35:11

Greek: εἶπε δὲ αὐτῷ ὁ Θεός· ἐγὼ ὁ Θεός σου· αὐξάνου καὶ πληθύνου· ἔθνη καὶ συναγωγαὶ ἐθνῶν ἔσονται ἐκ σοῦ, καὶ βασιλεῖς ἐκ τῆς ὀσφύος σου ἐξελεύσονται.
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

## Genesis 35:12

Greek: καὶ τὴν γῆν, ἣν ἔδωκα ῾Αβραὰμ καὶ ᾿Ισαάκ, σοὶ δέδωκα αὐτήν· σοὶ ἔσται, καὶ τῷ σπέρματί σου μετὰ σὲ δώσω τὴν γῆν ταύτην.
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

## Genesis 35:13

Greek: ἀνέβη δὲ ὁ Θεὸς ἀπ᾿ αὐτοῦ ἐκ τοῦ τόπου, οὗ ἐλάλησε μετ᾿ αὐτοῦ.
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

## Genesis 35:14

Greek: καὶ ἔστησεν ᾿Ιακὼβ στήλην ἐν τῷ τόπῳ, ᾧ ἐλάλησε μετ᾿ αὐτοῦ ὁ Θεός, στήλην λιθίνην, καὶ ἔσπεισεν ἐπ᾿ αὐτὴν σπονδὴν καὶ ἐπέχεεν ἐπ᾿ αὐτὴν ἔλαιον.
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

## Genesis 35:15

Greek: καὶ ἐκάλεσεν ᾿Ιακὼβ τὸ ὄνομα τοῦ τόπου, ἐν ᾧ ἐλάλησε μετ᾿ αὐτοῦ ἐκεῖ ὁ Θεός, Βαιθήλ.
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

## Genesis 35:16

Greek: ᾿Απάρας δὲ ᾿Ιακὼβ ἐκ Βαιθήλ, ἔπηξε τὴν σκηνὴν αὐτοῦ ἐπέκεινα τοῦ πύργου Γαδέρ. ἐγένετο δὲ ἡνίκα ἤγγισεν εἰς Χαβραθὰ τοῦ ἐλθεῖν εἰς τὴν ᾿Εφραθᾶ, ἔτεκε Ραχὴλ καὶ ἐδυστόκησεν ἐν τῷ τοκετῷ.
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

## Genesis 35:17

Greek: ἐγένετο δὲ ἐν τῷ σκληρῶς αὐτὴν τίκτειν, εἶπεν αὐτῇ ἡ μαῖα· θάρσει, καὶ γὰρ οὗτός σοί ἐστιν υἱός.
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

## Genesis 35:18

Greek: ἐγένετο δὲ ἐν τῷ ἀφιέναι αὐτὴν τὴν ψυχήν, ἀπέθνησκε γάρ, ἐκάλεσε τὸ ὄνομα αὐτοῦ Υἱὸς ὀδύνης μου· ὁ δὲ πατὴρ ἐκάλεσε τὸ ὄνομα αὐτοῦ Βενιαμίν.
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

## Genesis 35:19

Greek: ἀπέθανε δὲ Ραχὴλ καὶ ἐτάφη ἐν τῇ ὁδῷ τοῦ ἱπποδρόμου ᾿Εφραθᾶ (αὕτη ἐστὶ Βηθλεέμ).
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

## Genesis 35:20

Greek: καὶ ἔστησεν ᾿Ιακὼβ στήλην ἐπὶ τοῦ μνημείου αὐτῆς· αὕτη ἐστὶν ἡ στήλη ἐπὶ τοῦ μνημείου Ραχὴλ ἕως τῆς ἡμέρας ταύτης.
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

## Genesis 35:21

Greek: ἐγένετο δέ ἡνίκα κατῴκησεν ᾿Ισραὴλ ἐν τῇ γῇ ἐκείνῃ, ἐπορεύθη Ρουβὴν καὶ ἐκοιμήθη μετὰ Βαλλᾶς τῆς παλλακῆς τοῦ πατρὸς αὐτοῦ ᾿Ιακώβ· καὶ ἤκουσεν ᾿Ισραήλ, καὶ πονηρὸν ἐφάνη ἐναντίον αὐτοῦ.
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

## Genesis 35:22

Greek: ῏Ησαν δὲ οἱ υἱοὶ ᾿Ιακὼβ δώδεκα.
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

## Genesis 35:23

Greek: υἱοὶ Λείας· πρωτότοκος ᾿Ιακὼβ Ρουβήν, Συμεών, Λευί, ᾿Ιούδας, ᾿Ισσάχαρ, Ζαβουλών.
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

## Genesis 35:24

Greek: υἱοὶ δὲ Ραχήλ· ᾿Ιωσὴφ καὶ Βενιαμίν.
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

## Genesis 35:25

Greek: υἱοὶ δὲ Βαλλᾶς παιδίσκης Ραχήλ· Δὰν καὶ Νεφθαλείμ.
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

## Genesis 35:26

Greek: υἱοὶ δὲ Ζελφᾶς παιδίσκης Λείας· Γὰδ καὶ ᾿Ασήρ. οὗτοι υἱοὶ ᾿Ιακώβ, οἳ ἐγένοντο αὐτῷ ἐν Μεσοποταμίᾳ τῆς Συρίας.
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

## Genesis 35:27

Greek: ῏Ηλθε δὲ ᾿Ιακὼβ πρὸς ᾿Ισαὰκ τὸν πατέρα αὐτοῦ εἰς Μαμβρῆ, εἰς πόλιν τοῦ πεδίου (αὕτη ἐστὶ Χεβρών) ἐν γῇ Χαναάν, οὗ παρῴκησεν ῾Αβραὰμ καὶ ᾿Ισαάκ.
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

## Genesis 35:28

Greek: ἐγένοντο δὲ αἱ ἡμέραι ᾿Ισαάκ, ἃς ἔζησεν, ἔτη ἑκατὸν ὀγδοήκοντα,
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

## Genesis 35:29

Greek: καὶ ἐκλείπων ᾿Ισαὰκ ἀπέθανε καὶ προσετέθη πρὸς τὸ γένος αὐτοῦ πρεσβύτερος καὶ πλήρης ἡμερῶν, καὶ ἔθαψαν αὐτὸν ῾Ησαῦ καὶ ᾿Ιακὼβ οἱ υἱοὶ αὐτοῦ.
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

# Chapter 36

## Genesis 36:1

Greek: ΑΥΤΑΙ δὲ αἱ γενέσεις ῾Ησαῦ (αὐτός ἐστιν ᾿Εδώμ)·
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

## Genesis 36:2

Greek: ῾Ησαῦ δὲ ἔλαβε τὰς γυναῖκας ἑαυτῷ ἀπὸ τῶν θυγατέρων τῶν Χαναναίων, τὴν ᾿Αδὰ θυγατέρα Αἰλὼμ τοῦ Χετταίου καὶ τοῦ ᾿Ολιβεμὰ θυγατέρα ᾿Ανὰ τοῦ υἱοῦ Σεβεγὼν τοῦ Εὐαίου
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

## Genesis 36:3

Greek: καὶ τὴν Βασεμὰθ θυγατέρα ᾿Ισμαὴλ ἀδελφὴν Ναβεώθ.
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

## Genesis 36:4

Greek: ἔτεκε δὲ αὐτῷ ᾿Αδὰ τὸν ῾Ελιφάς, καὶ Βασεμὰθ ἔτεκε τὸν Ραγουήλ,
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

## Genesis 36:5

Greek: καὶ ᾿Ολιβεμὰ ἔτεκε τὸν ᾿Ιεοὺς καὶ τὸν ᾿Ιεγλὸμ καὶ τὸν Κορέ· οὗτοι υἱοὶ ῾Ησαῦ, οἳ ἐγένοντο αὐτῷ ἐν γῇ Χαναάν.
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

## Genesis 36:6

Greek: ἔλαβε δὲ ῾Ησαῦ τὰς γυναῖκας αὐτοῦ καὶ τοὺς υἱοὺς αὐτοῦ καὶ τὰς θυγατέρας αὐτοῦ καὶ πάντα τὰ σώματα τοῦ οἴκου αὐτοῦ καὶ πάντα τὰ ὑπάρχοντα αὐτοῦ καὶ πάντα τὰ κτήνη καὶ πάντα ὅσα ἐκτήσατο καὶ πάντα ὅσα περιεποιήσατο ἐν γῇ Χαναάν, καὶ ἐπορεύθη ῾Ησαῦ ἐκ τῆς γῆς Χαναὰν ἀπό προσώπου ᾿Ιακὼβ τοῦ ἀδελφοῦ αὐτοῦ.
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

## Genesis 36:7

Greek: ἦν γὰρ αὐτῶν τὰ ὑπάρχοντα πολλὰ τοῦ οἰκεῖν ἅμα, καὶ οὐκ ἠδύνατο ἡ γῆ τῆς παροικήσεως αὐτῶν φέρειν αὐτοὺς ἀπὸ τοῦ πλήθους τῶν ὑπαρχόντων αὐτῶν.
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

## Genesis 36:8

Greek: κατῴκησε δὲ ῾Ησαῦ ἐν τῷ ὄρει Σηεὶρ (῾Ησαῦ αὐτός ἐστιν ᾿Εδώμ).
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

## Genesis 36:9

Greek: Αὗται δὲ αἱ γενέσεις ῾Ησαῦ πατρὸς ᾿Εδὼμ ἐν τῷ ὄρει Σηείρ,
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

## Genesis 36:10

Greek: καὶ ταῦτα τὰ ὀνόματα τῶν υἱῶν ῾Ησαῦ· ῾Ελιφὰς υἱὸς ᾿Αδᾶς γυναικὸς ῾Ησαῦ καὶ Ραγουὴλ υἱὸς Βασεμὰθ γυναικὸς ῾Ησαῦ.
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

## Genesis 36:11

Greek: ἐγένοντο δὲ ῾Ελιφὰς υἱοί· Θαιμάν, ῾Ωμάρ, Σωφάρ, Γοθὼμ καὶ Κενέζ·
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

## Genesis 36:12

Greek: Θαμνὰ δὲ ἦν παλλακὴ ῾Ελιφὰς τοῦ υἱοῦ ῾Ησαῦ καὶ ἔτεκε τῷ ῾Ελιφὰς τὸν ᾿Αμαλήκ· οὗτοι υἱοὶ ᾿Αδᾶς γυναικὸς ῾Ησαῦ.
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

## Genesis 36:13

Greek: οὗτοι δὲ υἱοὶ Ραγουήλ· Ναχόθ, Ζαρέ, Σομέ, καὶ Μοζέ· οὗτοι ἦσαν υἱοὶ Βασεμὰθ γυναικὸς ῾Ησαῦ.
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

## Genesis 36:14

Greek: οὗτοι δὲ υἱοὶ ᾿Ολιβεμᾶς θυγατρὸς ᾿Ανὰ τοῦ υἱοῦ Σεβεγών, γυναικὸς ῾Ησαῦ· ἔτεκε δὲ τῷ ῾Ησαῦ τὸν ᾿Ιεοὺς καὶ τὸν ᾿Ιεγλὸμ καὶ τὸν Κορέ.
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

## Genesis 36:15

Greek: οὗτοι ἡγεμόνες υἱοὶ ῾Ησαῦ· υἱοὶ ῾Ελιφὰς πρωτοτόκου ῾Ησαῦ· ἡγεμὼν Θαιμάν, ἡγεμὼν ῾Ωμάρ, ἡγεμὼν Σωφάρ, ἡγεμὼν Κενέζ,
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

## Genesis 36:16

Greek: ἡγεμὼν Κορέ, ἡγεμὼν Γοθώμ, ἡγεμὼν ᾿Αμαλήκ· οὗτοι ἡγεμόνες ῾Ελιφὰς ἐν γῇ ᾿Ιδουμαίᾳ· οὗτοι υἱοὶ ᾿Αδᾶς.
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

## Genesis 36:17

Greek: καὶ οὗτοι υἱοὶ Ραγουὴλ υἱοῦ ῾Ησαῦ· ἡγεμὼν Ναχώθ, ἡγεμὼν Ζαρέ, ἡγεμὼν Σομέ, ἡγεμὼν Μοζέ· οὗτοι ἡγεμόνες Ραγουὴλ ἐν γῇ ᾿Εδώμ· οὗτοι υἱοὶ Βασεμὰθ γυναικὸς ῾Ησαῦ.
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

## Genesis 36:18

Greek: οὗτοι δὲ υἱοὶ ᾿Ολιβεμᾶς γυναικὸς ῾Ησαῦ· ἡγεμὼν ᾿Ιεούλ, ἡγεμὼν ᾿Ιεγλόμ, ἡγεμὼν Κορέ· οὗτοι ἡγεμόνες ᾿Ολιβεμᾶς θυγατρὸς ᾿Ανὰ γυναικὸς ῾Ησαῦ.
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

## Genesis 36:19

Greek: οὗτοι υἱοὶ ῾Ησαῦ, καὶ οὗτοι ἡγεμόνες αὐτῶν. οὗτοί εἰσιν υἱοὶ ᾿Εδώμ.
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

## Genesis 36:20

Greek: Οὗτοι δὲ υἱοὶ Σηεὶρ τοῦ Χορραίου τοῦ κατοικοῦντος τὴν γῆν· Λωτά, Σωβάλ, Σεβεγών, ᾿Ανὰ
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

## Genesis 36:21

Greek: καὶ Δησὼν καὶ ᾿Ασὰρ καὶ Ρισών· οὗτοι ἡγεμόνες τοῦ Χορραίου τοῦ υἱοῦ Σηεὶρ ἐν τῇ γῇ ᾿Εδώμ.
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

## Genesis 36:22

Greek: ἐγένοντο δὲ υἱοὶ Λωτάν· Χορρὶ καὶ Αἰμάν· ἀδελφὴ δὲ Λωτὰν Θαμνά.
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

## Genesis 36:23

Greek: οὗτοι δὲ υἱοὶ Σωβάλ· Γωλὰμ καὶ Μαναχὰθ καὶ Γαιβὴλ καὶ Σωφὰρ καὶ ῾Ωμάρ.
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

## Genesis 36:24

Greek: καὶ οὗτοι υἱοὶ Σεβεγών· ᾿Αϊέ καὶ ᾿Ανά· οὗτός ἐστιν ᾿Ανά, ὃς εὗρε τὸν ᾿Ιαμεὶν ἐν τῇ ἐρήμῳ, ὅτε ἔνεμε τὰ ὑποζύγια Σεβεγὼν τοῦ πατρὸς αὐτοῦ.
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

## Genesis 36:25

Greek: οὗτοι δὲ υἱοὶ ᾿Ανά· Δησὼν καὶ ᾿Ολιβεμὰ θυγάτηρ ᾿Ανά.
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

## Genesis 36:26

Greek: οὗτοι δὲ υἱοὶ Δησών· ᾿Αμαδὰ καὶ ᾿Ασβὰν καὶ ᾿Ιθρὰν καὶ Χαρράν.
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

## Genesis 36:27

Greek: οὗτοι δὲ υἱοὶ ᾿Ασάρ· Βαλαὰμ καὶ Ζουκὰμ καὶ ᾿Ιουκάμ.
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

## Genesis 36:28

Greek: οὗτοι δὲ υἱοὶ Ρισών· ῟Ως καὶ ᾿Αράν.
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

## Genesis 36:29

Greek: οὗτοι δὲ ἡγεμόνες Χορρί· ἡγεμὼν Λωτάν, ἡγεμὼν Σωβάλ, ἡγεμὼν Σεβεγών, ἡγεμὼν ᾿Ανά,
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

## Genesis 36:30

Greek: ἡγεμὼν Δησών, ἡγεμὼν ᾿Ασάρ, ἡγεμὼν Ρισών. οὗτοι ἡγεμόνες Χορρὶ ἐν ταῖς ἡγεμονίαις αὐτῶν ἐν γῇ ᾿Εδώμ.
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

## Genesis 36:31

Greek: Καὶ οὗτοι οἱ βασιλεῖς οἱ βασιλεύσαντες ἐν ᾿Εδὼμ πρὸ τοῦ βασιλεῦσαι βασιλέα ἐν ᾿Ισραήλ.
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

## Genesis 36:32

Greek: καὶ ἐβασίλευσεν ἐν ᾿Εδὼμ Βαλὰκ υἱὸς Βεώρ, καὶ ὄνομα τῇ πόλει αὐτοῦ Δενναβά.
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

## Genesis 36:33

Greek: ἀπέθανε δὲ Βαλάκ, καὶ ἐβασίλευσεν ἀντ᾿ αὐτοῦ ᾿Ιωβὰβ υἱὸς Ζαρὰ ἐκ Βοσόρρας.
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

## Genesis 36:34

Greek: ἀπέθανε δὲ ᾿Ιωβάβ, καὶ ἐβασίλευσεν ἀντ᾿ αὐτοῦ ᾿Ασὼμ ἐκ τῆς γῆς Θαιμανών.
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

## Genesis 36:35

Greek: ἀπέθανε δὲ ᾿Ασώμ, καὶ ἐβασίλευσεν ἀντ᾿ αὐτοῦ ᾿Αδὰδ υἱὸς Βαρὰδ ὁ ἐκκόψας Μαδιὰμ ἐν τῷ πεδίῳ Μωάβ, καὶ ὄνομα τῇ πόλει αὐτοῦ Γετθαίμ.
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

## Genesis 36:36

Greek: ἀπέθανε δὲ ᾿Αδάδ, καὶ ἐβασίλευσεν ἀντ᾿ αὐτοῦ Σαμαδὰ ἐκ Μασεκκᾶς.
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

## Genesis 36:37

Greek: ἀπέθανε δὲ Σαμαδά, καὶ ἐβασίλευσεν ἀντ᾿ αὐτοῦ Σαοὺλ ἐκ Ροωβὼθ τῆς παρὰ ποταμόν.
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

## Genesis 36:38

Greek: ἀπέθανε δὲ Σαούλ, καὶ ἐβασίλευσεν ἀντ᾿ αὐτοῦ Βαλαεννὼν υἱὸς ᾿Αχοβώρ.
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

## Genesis 36:39

Greek: ἀπέθανε δὲ Βαλαεννὼν υἱὸς ᾿Αχοβώρ, καὶ ἐβασίλευσεν ἀντ᾿ αὐτοῦ ᾿Αρὰδ υἱὸς Βαράδ, καὶ ὄνομα τῇ πόλει αὐτοῦ Φογώρ, ὄνομα δὲ τῇ γυναικὶ αὐτοῦ Μετεβεήλ, θυγάτηρ Ματραΐθ, υἱοῦ Μαιζοώβ.
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

## Genesis 36:40

Greek: Ταῦτα τὰ ὀνόματα τῶν ἡγεμόνων ῾Ησαῦ ἐν ταῖς φυλαῖς αὐτῶν κατὰ τόπον αὐτῶν, ἐν ταῖς χώραις αὐτῶν καὶ ἐν τοῖς ἔθνεσιν αὐτῶν. ἡγεμὼν Θαμνά, ἡγεμὼν Γωλά, ἡγεμὼν ᾿Ιεθέρ,
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

## Genesis 36:41

Greek: ἡγεμὼν ᾿Ολιβεμάς, ἡγεμὼν ῾Ηλάς, ἡγεμὼν Φινών,
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

## Genesis 36:42

Greek: ἡγεμὼν Κενέζ, ἡγεμὼν Θαιμάν, ἡγεμὼν Μαζάρ,
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

## Genesis 36:43

Greek: ἡγεμὼν Μαγεδιήλ, ἡγεμὼν Ζαφωίν. οὗτοι ἡγεμόνες ᾿Εδὼμ ἐν ταῖς κατῳκοδομημέναις ἐν τῇ γῇ τῆς κτήσεως αὐτῶν. οὗτος ῾Ησαῦ πατὴρ ᾿Εδώμ.
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

# Chapter 37

## Genesis 37:1

Greek: ΚΑΤῼΚΕΙ δὲ ᾿Ιακὼβ ἐν τῇ γῇ, οὗ παρώκησεν ὁ πατὴρ αὐτοῦ, ἐν γῇ Χαναάν.
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

## Genesis 37:2

Greek: αὗται δὲ αἱ γενέσεις ᾿Ιακώβ· ᾿Ιωσὴφ δὲ δέκα καὶ ἑπτὰ ἐτῶν ἦν, ποιμαίνων τὰ πρόβατα τοῦ πατρὸς αὐτοῦ μετὰ τῶν ἀδελφῶν αὐτοῦ, ὢν νέος, μετὰ τῶν υἱῶν Βαλλᾶς καὶ μετὰ τῶν υἱῶν Ζελφᾶς τῶν γυναικῶν τοῦ πατρὸς αὐτοῦ· κατήνεγκαν δὲ ᾿Ιωσὴφ ψόγον πονηρὸν πρὸς ᾿Ισραὴλ τὸν πατέρα αὐτῶν.
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

## Genesis 37:3

Greek: ᾿Ιακὼβ δέ ἠγάπα τὸν ᾿Ιωσὴφ παρὰ πάντας τοὺς υἱοὺς αὐτοῦ, ὅτι υἱὸς γήρως ἦν αὐτῷ· ἐποίησε δὲ αὐτῷ χιτῶνα ποικίλον.
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

## Genesis 37:4

Greek: ἰδόντες δὲ οἱ ἀδελφοὶ αὐτοῦ, ὅτι αὐτὸν ὁ πατὴρ φιλεῖ ἐκ πάντων τῶν υἱῶν αὐτοῦ, ἐμίσησαν αὐτὸν καὶ οὐκ ἠδύναντο λαλεῖν αὐτῷ οὐδὲν εἰρηνικόν.
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

## Genesis 37:5

Greek: ᾿Ενυπνιασθεὶς δὲ ᾿Ιωσὴφ ἐνύπνιον ἀπήγγειλεν αὐτὸ τοῖς ἀδελφοῖς αὐτοῦ.
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

## Genesis 37:6

Greek: καὶ εἶπεν αὐτοῖς· ἀκούσατε τοῦ ἐνυπνίου τούτου, οὗ ἐνυπνιάσθην·
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

## Genesis 37:7

Greek: ᾤμην ὑμᾶς δεσμεύειν δράγματα ἐν μέσῳ τῷ πεδίῳ, καὶ ἀνέστη τὸ ἐμὸν δράγμα καὶ ὠρθώθη, περιστραφέντα δὲ τὰ δράγματα ὑμῶν προσεκύνησαν τὸ ἐμὸν δράγμα.
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

## Genesis 37:8

Greek: εἶπαν δὲ αὐτῷ οἱ ἀδελφοὶ αὐτοῦ· μὴ βασιλεύων βασιλεύσεις ἐφ᾿ ἡμᾶς ἢ κυριεύων κυριεύσεις ἡμῶν; καὶ προσέθεντο ἔτι μισεῖν αὐτὸν ἕνεκεν τῶν ἐνυπνίων αὐτοῦ καὶ ἕνεκεν τῶν ρημάτων αὐτοῦ.
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

## Genesis 37:9

Greek: εἶδε δὲ ἐνύπνιον ἕτερον καὶ διηγήσατο αὐτῷ τῷ πατρὶ αὐτοῦ καὶ τοῖς ἀδελφοῖς αὐτοῦ, καὶ εἶπεν· ἰδοὺ ἐνυπνιασάμην ἐνύπνιον ἕτερον, ὥσπερ ὁ ἥλιος καὶ ἡ σελήνη καὶ ἕνδεκα ἀστέρες προσεκύνουν με.
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

## Genesis 37:10

Greek: καὶ ἐπετίμησεν αὐτῷ ὁ πατὴρ αὐτοῦ καὶ εἶπεν αὐτῷ· τί τὸ ἐνύπνιον τοῦτο, ὃ ἐνυπνιάσθης; ἆρά γε ἐλθόντες ἐλευσόμεθα ἐγώ τε καὶ ἡ μήτηρ σου καὶ οἱ ἀδελφοί σου προσκυνῆσαί σοι ἐπὶ τὴν γῆν
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

## Genesis 37:11

Greek: ἐζήλωσαν δὲ αὐτὸν οἱ ἀδελφοὶ αὐτοῦ, ὁ δὲ πατὴρ αὐτοῦ διετήρησε τὸ ρῆμα.
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

## Genesis 37:12

Greek: ᾿Επορεύθησαν δὲ οἱ ἀδελφοὶ αὐτοῦ βόσκειν τὰ πρόβατα τοῦ πατρὸς αὐτῶν εἰς Συχέμ.
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

## Genesis 37:13

Greek: καὶ εἶπεν ᾿Ισραὴλ πρὸς ᾿Ιωσήφ· οὐχὶ οἱ ἀδελφοί σου ποιμαίνουσιν εἰς Συχέμ; δεῦρο ἀποστείλω σε πρὸς αὐτούς. εἶπε δὲ αὐτῷ· ἰδοὺ ἐγώ.
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

## Genesis 37:14

Greek: εἶπε δὲ αὐτῷ ᾿Ισραήλ· πορευθεὶς ἰδέ, εἰ ὑγιαίνουσιν οἱ ἀδελφοί σου καὶ τὰ πρόβατα, καὶ ἀνάγγειλόν μοι. καὶ ἀπέστειλεν αὐτὸν ἐκ τῆς κοιλάδος τῆς Χεβρών, καὶ ἦλθεν εἰς Συχέμ.
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

## Genesis 37:15

Greek: καὶ εὗρεν αὐτὸν ἄνθρωπος πλανώμενον ἐν τῷ πεδίῳ· ἠρώτησε δὲ αὐτὸν ὁ ἄνθρωπος λέγων· τί ζητεῖς
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

## Genesis 37:16

Greek: ὁ δὲ εἶπε· τοὺς ἀδελφούς μου ζητῶ· ἀπάγγειλόν μοι, ποῦ βόσκουσιν.
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

## Genesis 37:17

Greek: εἶπε δὲ αὐτῷ ὁ ἄνθρωπος· ἀπῄρκασιν ἐντεῦθεν, ἤκουσα γὰρ αὐτῶν λεγόντων· πορευθῶμεν εἰς Δωθαείμ. καὶ ἐπορεύθη ᾿Ιωσὴφ κατόπισθεν τῶν ἀδελφῶν αὐτοῦ καὶ εὗρεν αὐτοὺς ἐν Δωθαείμ.
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

## Genesis 37:18

Greek: προεῖδον δὲ αὐτὸν μακρόθεν πρὸ τοῦ ἐγγίσαι αὐτὸν πρὸς αὐτοὺς καὶ ἐπονηρεύοντο τοῦ ἀποκτεῖναι αὐτόν.
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

## Genesis 37:19

Greek: εἶπε δὲ ἕκαστος πρὸς τὸν ἀδελφὸν αὐτοῦ· ἰδοὺ ὁ ἐνυπνιαστὴς ἐκεῖνος ἔρχεται·
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

## Genesis 37:20

Greek: νῦν οὖν δεῦτε ἀποκτείνωμεν αὐτὸν καὶ ρίψωμεν αὐτὸν εἰς ἕνα τῶν λάκκων καὶ ἐροῦμεν· θηρίον πονηρὸν κατέφαγεν αὐτόν· καὶ ὀψόμεθα, τί ἔσται τὰ ἐνύπνια αὐτοῦ.
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

## Genesis 37:21

Greek: ἀκούσας δὲ Ρουβὴν ἐξείλετο αὐτὸν ἐκ τῶν χειρῶν αὐτῶν καὶ εἶπεν· οὐ πατάξωμεν αὐτὸν εἰς ψυχήν.
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

## Genesis 37:22

Greek: εἶπε δὲ αὐτοῖς Ρουβήν· μὴ ἐκχέητε αἷμα· ἐμβάλλετε αὐτὸν εἰς ἕνα τῶν λάκκων τούτων τῶν ἐν τῇ ἐρήμῳ, χεῖρα δὲ μὴ ἐπενέγκητε αὐτῷ· ὅπως ἐξέληται αὐτὸν ἐκ τῶν χειρῶν αὐτῶν καὶ ἀποδῷ αὐτὸν τῷ πατρὶ αὐτοῦ.
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

## Genesis 37:23

Greek: ἐγένετο δὲ ἡνίκα ἦλθεν ᾿Ιωσὴφ πρὸς τοὺς ἀδελφοὺς αὐτοῦ, ἐξέδυσαν ᾿Ιωσὴφ τὸν χιτῶνα τὸν ποικίλον τὸν περὶ αὐτόν
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

## Genesis 37:24

Greek: καὶ λαβόντες αὐτόν ἔρριψαν εἰς τὸν λάκκον· ὁ δὲ λάκκος κενός, ὕδωρ οὐκ εἶχεν.
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

## Genesis 37:25

Greek: ᾿Εκάθισαν δὲ φαγεῖν ἄρτον καὶ ἀναβλέψαντες τοῖς ὀφθαλμοῖς εἶδον, καὶ ἰδοὺ ὁδοιπόροι ᾿Ισμαηλῖται ἤρχοντο ἐκ Γαλαάδ, καὶ αἱ κάμηλοι αὐτῶν ἔγεμαν θυμιαμάτων καὶ ρητίνης καὶ στακτῆς· ἐπορεύοντο δὲ καταγαγεῖν εἰς Αἴγυπτον.
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

## Genesis 37:26

Greek: εἶπε δὲ ᾿Ιούδας πρὸς τούς ἀδελφοὺς αὐτοῦ· τί χρήσιμον, ἐὰν ἀποκτείνωμεν τὸν ἀδελφὸν ἡμῶν καὶ κρύψωμεν τὸ αἷμα αὐτοῦ
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

## Genesis 37:27

Greek: δεῦτε ἀποδώμεθα αὐτὸν τοῖς ᾿Ισμαηλίταις τούτοις, αἱ δὲ χεῖρες ἡμῶν μὴ ἔστωσαν ἐπ᾿ αὐτόν, ὅτι ἀδελφὸς ἡμῶν καὶ σὰρξ ἡμῶν ἐστιν. ἤκουσαν δὲ οἱ ἀδελφοὶ αὐτοῦ.
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

## Genesis 37:28

Greek: καὶ παρεπορεύοντο οἱ ἄνθρωποι οἱ Μαδιηναῖοι ἔμποροι, καὶ ἐξείλκυσαν καὶ ἀνεβίβασαν τὸν ᾿Ιωσὴφ ἐκ τοῦ λάκκου καὶ ἀπέδοντο τὸν ᾿Ιωσὴφ τοῖς ᾿Ισμαηλίταις εἴκοσι χρυσῶν, καὶ κατήγαγον τὸν ᾿Ιωσὴφ εἰς Αἴγυπτον.
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

## Genesis 37:29

Greek: ἀνέστρεψε δὲ Ρουβὴν ἐπὶ τὸν λάκκον καὶ οὐχ ὁρᾷ τὸν ᾿Ιωσὴφ ἐν τῷ λάκκῳ. καὶ διέρρηξε τὰ ἱμάτια αὐτοῦ.
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

## Genesis 37:30

Greek: καὶ ἐπέστρεψε πρὸς τοὺς ἀδελφοὺς αὐτοῦ. καὶ εἶπε· τὸ παιδάριον οὐκ ἔστιν, ἐγὼ δὲ ποῦ πορεύομαι ἔτι
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

## Genesis 37:31

Greek: Λαβόντες δὲ τὸν χιτῶνα τοῦ ᾿Ιωσὴφ ἔσφαξαν ἔριφον αἰγῶν καὶ ἐμόλυναν τὸν χιτῶνα τῷ αἵματι.
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

## Genesis 37:32

Greek: καὶ ἀπέστειλαν τὸν χιτῶνα τὸν ποικίλον καὶ εἰσήνεγκαν τῷ πατρὶ αὐτῶν. καὶ εἶπαν· τοῦτον εὕρομεν, ἐπίγνωθι εἰ χιτὼν τοῦ υἱοῦ σού ἐστιν ἢ οὔ.
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

## Genesis 37:33

Greek: καὶ ἐπέγνω αὐτὸν καὶ εἶπε· χιτὼν τοῦ υἱοῦ μού ἐστι· θηρίον πονηρὸν κατέφαγεν αὐτόν, θηρίον ἥρπασε τὸν ᾿Ιωσήφ.
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

## Genesis 37:34

Greek: διέρρηξε δὲ ᾿Ιακὼβ τὰ ἱμάτια αὐτοῦ καὶ ἐπέθετο σάκκον ἐπὶ τὴν ὀσφὺν αὐτοῦ καὶ ἐπένθει τὸν υἱὸν αὐτοῦ ἡμέρας πολλάς.
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

## Genesis 37:35

Greek: συνήχθησαν δὲ πάντες οἱ υἱοὶ αὐτοῦ καὶ αἱ θυγατέρες καὶ ἦλθον παρακαλέσαι αὐτόν, καὶ οὐκ ἤθελε παρακαλεῖσθαι λέγων ὅτι· καταβήσομαι πρὸς τὸν υἱόν μου πενθῶν εἰς ᾅδου. καὶ ἔκλαυσεν αὐτὸν ὁ πατὴρ αὐτοῦ.
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

## Genesis 37:36

Greek: οἱ δὲ Μαδιηναῖοι ἀπέδοντο τὸν ᾿Ιωσὴφ εἰς Αἴγυπτον τῷ Πετεφρῇ τῷ σπάδοντι Φαραώ, ἀρχιμαγείρῳ.
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

# Chapter 38

## Genesis 38:1

Greek: ΕΓΕΝΕΤΟ δέ ἐν τῷ καιρῷ ἐκείνῳ, κατέβη ᾿Ιούδας ἀπὸ τῶν ἀδελφῶν αὐτοῦ καὶ ἀφίκετο ἕως πρὸς ἄνθρωπόν τινα ᾿Οδολλαμίτην, ᾧ ὄνομα Εἰράς.
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

## Genesis 38:2

Greek: καὶ εἶδεν ἐκεῖ ᾿Ιούδας θυγατέρα ἀνθρώπου Χαναναίου, ᾗ ὄνομα Σαυά, καὶ ἔλαβεν αὐτὴν καὶ εἰσῆλθε πρὸς αὐτήν.
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

## Genesis 38:3

Greek: καὶ συλλαβοῦσα ἔτεκεν υἱὸν καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ ῎Ηρ.
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

## Genesis 38:4

Greek: καὶ συλλαβοῦσα ἔτεκεν υἱὸν ἔτι καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ Αὐνάν.
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

## Genesis 38:5

Greek: καὶ προσθεῖσα ἔτεκεν υἱὸν καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ Σηλώμ. αὕτη δὲ ἦν ἐν Χασβί, ἡνίκα ἔτεκεν αὐτούς.
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

## Genesis 38:6

Greek: καὶ ἔλαβεν ᾿Ιούδας γυναῖκα ῍Ηρ τῷ πρωτοτόκῳ αὐτοῦ, ᾗ ὄνομα Θάμαρ.
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

## Genesis 38:7

Greek: ἐγένετο δὲ ῍Ηρ πρωτότοκος ᾿Ιούδα πονηρὸς ἔναντι Κυρίου, καὶ ἀπέκτεινεν αὐτὸν ὁ Θεός.
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

## Genesis 38:8

Greek: εἶπε δὲ ᾿Ιούδας τῷ Αὐνάν· εἴσελθε πρὸς τὴν γυναῖκα τοῦ ἀδελφοῦ σου καὶ ἐπιγάμβρευσαι αὐτὴν καὶ ἀνάστησον σπέρμα τῷ ἀδελφῷ σου.
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

## Genesis 38:9

Greek: γνοὺς δὲ Αὐνὰν ὅτι οὐκ αὐτῷ ἔσται τὸ σπέρμα, ἐγίνετο ὅταν εἰσήρχετο πρὸς τὴν γυναῖκα τοῦ ἀδελφοῦ αὐτοῦ, ἐξέχεεν ἐπὶ τὴν γῆν τοῦ μὴ δοῦναι σπέρμα τῷ ἀδελφῷ αὐτοῦ.
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

## Genesis 38:10

Greek: πονηρὸν δὲ ἐφάνη ἐναντίον τοῦ Θεοῦ, ὅτι ἐποίησε τοῦτο, καὶ ἐθανάτωσε καὶ τοῦτον.
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

## Genesis 38:11

Greek: εἶπε δὲ ᾿Ιούδας Θάμαρ τῇ νύμφῃ αὐτοῦ· κάθου χήρα ἐν τῷ οἴκῳ τοῦ πατρός σου ἕως μέγας γένηται Σηλὼμ ὁ υἱός μου. εἶπε γάρ· μή ποτε ἀποθάνῃ καὶ οὗτος, ὥσπερ καὶ οἱ ἀδελφοὶ αὐτοῦ. ἀπελθοῦσα δὲ Θάμαρ ἐκάθητο ἐν τῷ οἴκῳ τοῦ πατρὸς αὐτῆς.
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

## Genesis 38:12

Greek: ᾿Επληθύνθησαν δὲ αἱ ἡμέραι καὶ ἀπέθανε Σαυὰ ἡ γυνὴ ᾿Ιούδα· καὶ παρακληθεὶς ᾿Ιούδας ἀνέβη ἐπὶ τοὺς κείροντας τά πρόβατα αὐτοῦ, αὐτὸς καὶ Εἰρὰς ὁ ποιμὴν αὐτοῦ ὁ ᾿Οδολλαμίτης εἰς Θαμνά.
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

## Genesis 38:13

Greek: καὶ ἀπηγγέλη Θάμαρ τῇ νύμφῃ αὐτοῦ λέγοντες· ἰδοὺ ὁ πενθερός σου ἀναβαίνει εἰς Θαμνὰ κεῖραι τὰ πρόβατα αὐτοῦ.
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

## Genesis 38:14

Greek: καὶ περιελομένη τὰ ἱμάτια τῆς χηρεύσεως ἀφ᾿ ἑαυτῆς, περιεβάλετο θέριστρον καὶ ἐκαλλωπίσατο καὶ ἐκάθισε πρὸς ταῖς πύλαις Αἰνάν, ἥ ἐστιν ἐν παρόδῳ Θαμνά· εἶδε γὰρ ὅτι μέγας γέγονε Σηλώμ, αὐτὸς δὲ οὐκ ἔδωκεν αὐτὴν αὐτῷ γυναῖκα.
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

## Genesis 38:15

Greek: καὶ ἰδὼν αὐτὴν ᾿Ιούδας ἔδοξεν αὐτὴν πόρνην εἶναι· κατεκαλύψατο γὰρ τὸ πρόσωπον αὐτῆς, καὶ οὐκ ἐπέγνω αὐτήν.
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

## Genesis 38:16

Greek: ἐξέκλινε δὲ πρὸς αὐτὴν τὴν ὁδὸν καὶ εἶπεν αὐτῇ· ἔασόν με εἰσελθεῖν πρὸς σέ· οὐ γὰρ ἔγνω ὅτι νύμφη αὐτοῦ ἐστίν. ἡ δὲ εἶπε· τί μοι δώσεις, ἐὰν εἰσέλθῃς πρός με
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

## Genesis 38:17

Greek: ὁ δὲ εἶπεν· ἐγώ σοι ἀποστελῶ ἔριφον αἰγῶν ἐκ τῶν προβάτων μου, ἡ δὲ εἶπεν· ἐὰν δῷς μοι ἀρραβῶνα, ἕως τοῦ ἀποστεῖλαί σε.
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

## Genesis 38:18

Greek: ὁ δὲ εἶπε· τίνα τὸν ἀρραβῶνά σοι δώσω; ἡ δὲ εἶπε· τὸν δακτύλιόν σου καὶ τὸν ὁρμίσκον, καὶ τὴν ράβδον τὴν ἐν τῇ χειρί σου. καὶ ἔδωκεν αὐτῇ καὶ εἰσῆλθε πρὸς αὐτήν, καὶ ἐν γαστρὶ ἔλαβεν ἐξ αὐτοῦ.
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

## Genesis 38:19

Greek: καὶ ἀναστᾶσα ἀπῆλθε καὶ περιείλετο τὸ θέριστρον αὐτῆς ἀφ᾿ ἑαυτῆς καὶ ἐνεδύσατο τὰ ἱμάτια τῆς χηρεύσεως αὐτῆς.
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

## Genesis 38:20

Greek: ἀπέστειλε δὲ ᾿Ιούδας τὸν ἔριφον ἐξ αἰγῶν ἐν χειρὶ τοῦ ποιμένος αὐτοῦ τοῦ ᾿Οδολλαμίτου κομίσασθαι παρὰ τῆς γυναικὸς τὸν ἀρραβῶνα, καὶ οὐχ εὗρεν αὐτήν.
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

## Genesis 38:21

Greek: ἐπηρώτησε δὲ τοὺς ἄνδρας τοὺς ἐκ τοῦ τόπου· ποῦ ἐστιν ἡ πόρνη ἡ γενομένη ἐν Αἰνὰν ἐπὶ τῆς ὁδοῦ; καὶ εἶπαν· οὐκ ἦν ἐνταῦθα πόρνη.
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

## Genesis 38:22

Greek: καὶ ἀπεστράφη πρὸς ᾿Ιούδαν καὶ εἶπεν· οὐχ εὗρον, καὶ οἱ ἄνθρωποι οἱ ἐκ τοῦ τόπου λέγουσι μὴ εἶναι ὧδε πόρνην.
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

## Genesis 38:23

Greek: εἶπε δὲ ᾿Ιούδας· ἐχέτω αὐτά, ἀλλὰ μή ποτε καταγελασθῶμεν· ἐγὼ μὲν ἀπέσταλκα τὸν ἔριφον τοῦτον, σὺ δὲ οὐχ εὕρηκας.
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

## Genesis 38:24

Greek: ᾿Εγένετο δὲ μετὰ τρίμηνον ἀνηγγέλη τῷ ᾿Ιούδᾳ λέγοντες· ἐκπεπόρνευκε Θάμαρ ἡ νύμφη σου καὶ ἰδοὺ ἐν γαστρὶ ἔχει ἐκ πορνείας. εἶπε δὲ ᾿Ιούδας· ἐξαγάγετε αὐτήν, καὶ κατακαυθήτω.
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

## Genesis 38:25

Greek: αὐτὴ δὲ ἀγομένη ἀπέστειλε πρὸς τὸν πενθερὸν αὐτῆς λέγουσα· ἐκ τοῦ ἀνθρώπου, οὗτινος ταῦτά ἐστιν, ἐγὼ ἐν γαστρὶ ἔχω. καὶ εἶπεν· ἐπίγνωθι, τίνος ὁ δακτύλιος καὶ ὁ ὁρμίσκος καὶ ἡ ράβδος αὕτη.
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

## Genesis 38:26

Greek: ἐπέγνω δὲ ᾿Ιούδας καὶ εἶπε· δεδικαίωται Θάμαρ ἢ ἐγώ, οὗ ἕνεκεν οὐκ ἔδωκα αὐτὴν Σηλὼν τῷ υἱῷ μου. καὶ οὐ προσέθετο ἔτι τοῦ γνῶναι αὐτήν.
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

## Genesis 38:27

Greek: ᾿Εγένετο δὲ ἡνίκα ἔτικτε, καὶ τῇδε ἦν δίδυμα ἐν τῇ γαστρὶ αὐτῆς.
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

## Genesis 38:28

Greek: ἐγένετο δὲ ἐν τῷ τίκτειν αὐτήν, ὁ εἷς προεξήνεγκε τὴν χεῖρα· λαβοῦσα δὲ ἡ μαῖα ἔδησεν ἐπί τὴν χεῖρα αὐτοῦ κόκκινον λέγουσα· οὗτος ἐξελεύσεται πρότερος.
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

## Genesis 38:29

Greek: ὡς δὲ ἐπισυνήγαγε τὴν χεῖρα, καὶ εὐθὺς ἐξῆλθεν ὁ ἀδελφὸς αὐτοῦ. ἡ δὲ εἶπε· τί διεκόπη διὰ σὲ φραγμός; καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ Φαρές.
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

## Genesis 38:30

Greek: καί μετὰ τοῦτο ἐξῆλθεν ὁ ἀδελφὸς αὐτοῦ, ἐφ᾿ ᾧ ἦν ἐπὶ τῇ χειρὶ αὐτοῦ τὸ κόκκινον· καὶ ἐκάλεσε τὸ ὄνομα αὐτοῦ Ζαρά.
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

# Chapter 39

## Genesis 39:1

Greek: ΙΩΣΗΦ δὲ κατήχθη εἰς Αἴγυπτον, καὶ ἐκτήσατο αὐτὸν Πετεφρὴς ὁ εὐνοῦχος Φαραώ, ὁ ἀρχιμάγειρος, ἀνὴρ Αἰγύπτιος, ἐκ χειρῶν τῶν ᾿Ισμαηλιτῶν, οἳ κατήγαγον αὐτὸν ἐκεῖ.
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

## Genesis 39:2

Greek: καὶ ἦν Κύριος μετὰ ᾿Ιωσήφ, καὶ ἦν ἀνὴρ ἐπιτυγχάνων καὶ ἐγένετο ἐν τῷ οἴκῳ παρὰ τῷ κυρίῳ αὐτοῦ τῷ Αἰγυπτίῳ.
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

## Genesis 39:3

Greek: ᾔδει δὲ ὁ κύριος αὐτοῦ, ὅτι ὁ Κύριος ἦν μετ᾿ αὐτοῦ καὶ ὅσα ἐὰν ποιῇ, Κύριος εὐοδοῖ ἐν ταῖς χερσὶν αὐτοῦ.
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

## Genesis 39:4

Greek: καὶ εὗρεν ᾿Ιωσὴφ χάριν ἐναντίον τοῦ κυρίου αὐτοῦ, καὶ εὐηρέστησεν αὐτῷ, καὶ κατέστησεν αὐτὸν ἐπὶ τοῦ οἴκου αὐτοῦ καὶ πάντα, ὅσα ἦν αὐτῷ, ἔδωκε διὰ χειρὸς ᾿Ιωσήφ.
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

## Genesis 39:5

Greek: ἐγένετο δὲ μετὰ τὸ καταστῆναι αὐτὸν ἐπὶ τοῦ οἴκου αὐτοῦ καὶ ἐπὶ πάντα, ὅσα ἦν αὐτῷ, καὶ ηὐλόγησε Κύριος τὸν οἶκον τοῦ Αἰγυπτίου διὰ ᾿Ιωσήφ, καὶ ἐγενήθη εὐλογία Κυρίου ἐν πᾶσι τοῖς ὑπάρχουσιν αὐτῷ ἐν τῷ οἴκῳ καὶ ἐν τῷ ἀγρῷ αὐτοῦ.
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

## Genesis 39:6

Greek: καὶ ἐπέτρεψε πάντα, ὅσα ἦν αὐτῷ, εἰς χεῖρας ᾿Ιωσὴφ καὶ οὐκ ᾔδει τῶν καθ᾿ αὑτὸν οὐδὲν πλὴν τοῦ ἄρτου, οὗ ἤσθιεν αὐτός. Καὶ ἦν ᾿Ιωσὴφ καλὸς τῷ εἴδει καὶ ὡραῖος τῇ ὄψει σφόδρα.
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

## Genesis 39:7

Greek: καὶ ἐγένετο μετὰ τὰ ρήματα ταῦτα καὶ ἐπέβαλεν ἡ γυνὴ τοῦ κυρίου αὐτοῦ τοὺς ὀφθαλμοὺς αὐτῆς ἐπὶ ᾿Ιωσὴφ καὶ εἶπε· κοιμήθητι μετ᾿ ἐμοῦ.
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

## Genesis 39:8

Greek: ὁ δὲ οὐκ ἤθελεν, εἶπε δὲ τῇ γυναικὶ τοῦ κυρίου αὐτοῦ· εἰ ὁ κύριός μου οὐ γινώσκει δι᾿ ἐμὲ οὐδὲν ἐν τῷ οἴκῳ αὐτοῦ, καὶ πάντα, ὅσα ἐστὶν αὐτῷ, ἔδωκεν εἰς τὰς χεῖράς μου
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

## Genesis 39:9

Greek: καὶ οὐχ ὑπερέχει ἐν τῇ οἰκίᾳ ταύτῃ οὐδὲν ἐμοῦ, οὐδὲ ὑπεξῄρηται ἀπ᾿ ἐμοῦ οὐδὲν πλὴν σοῦ, διὰ τὸ σὲ γυναῖκα αὐτοῦ εἶναι, καὶ πῶς ποιήσω τὸ ρῆμα τὸ πονηρὸν τοῦτο, καὶ ἁμαρτήσομαι ἐναντίον τοῦ Θεοῦ
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

## Genesis 39:10

Greek: ἡνίκα δὲ ἐλάλει τῷ ᾿Ιωσὴφ ἡμέραν ἐξ ἡμέρας, καὶ οὐχ ὑπήκουεν αὐτῇ καθεύδειν μετ᾿ αὐτῆς τοῦ συγγενέσθαι αὐτῇ.
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

## Genesis 39:11

Greek: ἐγένετο δὲ τοιαύτη τις ἡμέρα, καὶ εἰσῆλθεν ᾿Ιωσὴφ εἰς τὴν οἰκίαν ποιεῖν τὰ ἔργα αὐτοῦ, καὶ οὐδεὶς ἦν τῶν ἐν τῇ οἰκίᾳ ἔσω,
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

## Genesis 39:12

Greek: καὶ ἐπεσπάσατο αὐτὸν τῶν ἱματίων λέγουσα· κοιμήθητι μετ᾿ ἐμοῦ. καὶ καταλιπὼν τὰ ἱμάτια αὐτοῦ ἐν ταῖς χερσὶν αὐτῆς ἔφυγε καὶ ἐξῆλθεν ἔξω.
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

## Genesis 39:13

Greek: καὶ ἐγένετο ὡς εἶδεν, ὅτι καταλιπὼν τὰ ἱμάτια αὐτοῦ ἐν ταῖς χερσὶν αὐτῆς ἔφυγε καὶ ἐξῆλθεν ἔξω,
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

## Genesis 39:14

Greek: καὶ ἐκάλεσε τοὺς ὄντας ἐν τῇ οἰκίᾳ καὶ εἶπεν αὐτοῖς λέγουσα· ἴδετε, εἰσήγαγεν ἡμῖν παῖδα ῾Εβραῖον ἐμπαίζειν ἡμῖν· εἰσῆλθε πρός με λέγων· κοιμήθητι μετ᾿ ἐμοῦ, καὶ ἐβόησα φωνῇ μεγάλῃ·
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

## Genesis 39:15

Greek: ἐν δὲ τῷ ἀκοῦσαι αὐτὸν ὅτι ὕψωσα τὴν φωνήν μου καὶ ἐβόησα, καταλιπὼν τὰ ἱμάτια αὐτοῦ παρ᾿ ἐμοὶ ἔφυγε καὶ ἐξῆλθεν ἔξω.
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

## Genesis 39:16

Greek: καὶ καταλιμπάνει τὰ ἱμάτια παρ᾿ ἑαυτῇ, ἕως ἦλθεν ὁ κύριος εἰς τὸν οἶκον αὐτοῦ.
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

## Genesis 39:17

Greek: καὶ ἐλάλησεν αὐτῷ κατὰ τὰ ρήματα ταῦτα λέγουσα· εἰσῆλθε πρός με ὁ παῖς ὁ ῾Εβραῖος, ὃν εἰσήγαγες πρὸς ἡμᾶς, ἐμπαῖξαί μοι καὶ εἶπέ μοι· κοιμηθήσομαι μετὰ σοῦ·
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

## Genesis 39:18

Greek: ὡς δὲ ἤκουσεν ὅτι ὕψωσα τὴν φωνήν μου καὶ ἐβόησα, καταλιπὼν τὰ ἱμάτια αὐτοῦ παρ᾿ ἐμοὶ ἔφυγε καὶ ἐξῆλθεν ἔξω.
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

## Genesis 39:19

Greek: ἐγένετο δέ, ὡς ἤκουσεν ὁ κύριος αὐτοῦ τὰ ρήματα τῆς γυναικὸς αὐτοῦ, ὅσα ἐλάλησε πρὸς αὐτόν, λέγουσα· οὕτως ἐποίησέ μοι ὁ παῖς σου, καὶ ἐθυμώθη ὀργῇ.
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

## Genesis 39:20

Greek: καὶ λαβὼν ὁ κύριος ᾿Ιωσὴφ ἐνέβαλεν αὐτὸν εἰς τὸ ὀχύρωμα, εἰς τὸν τόπον, ἐν ᾦ οἱ δεσμῶται τοῦ βασιλέως κατέχονται ἐκεῖ ἐν τῷ ὀχυρώματι.
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

## Genesis 39:21

Greek: Καὶ ἦν Κύριος μετὰ ᾿Ιωσὴφ καὶ κατέχεεν αὐτοῦ ἔλεος καὶ ἔδωκεν αὐτῷ χάριν ἐναντίον τοῦ ἀρχιδεσμοφύλακος,
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

## Genesis 39:22

Greek: καὶ ἔδωκεν ὁ ἀρχιδεσμοφύλαξ τὸ δεσμωτήριον διὰ χειρὸς ᾿Ιωσὴφ καὶ πάντας τοὺς ἀπηγμένους, ὅσοι ἐν τῷ δεσμωτηρίῳ, καὶ πάντα ὅσα ποιοῦσιν ἐκεῖ, αὐτὸς ἦν ποιῶν.
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

## Genesis 39:23

Greek: οὐκ ἦν ὁ ἀρχιδεσμοφύλαξ τοῦ δεσμωτηρίου γινώσκων δι᾿ αὐτὸν οὐδέν· πάντα γὰρ ἦν διὰ χειρὸς ᾿Ιωσὴφ διὰ τὸ τὸν Κύριον μετ᾿ αὐτοῦ εἶναι, καὶ ὅσα αὐτὸς ἐποίει, ὁ Κύριος εὐώδου ἐν ταῖς χερσὶν αὐτοῦ.
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

# Chapter 40

## Genesis 40:1

Greek: ΕΓΕΝΕΤΟ δὲ μετὰ τὰ ρήματα ταῦτα ἥμαρτεν ὁ ἀρχιοινοχόος τοῦ βασιλέως Αἰγύπτου καὶ ὁ ἀρχισιτοποιὸς τῷ κυρίῳ αὐτῶν βασιλεῖ Αἰγύπτου.
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

## Genesis 40:2

Greek: καὶ ὠργίσθη Φαραὼ ἐπὶ τοῖς δυσὶν εὐνούχοις αὐτοῦ, ἐπὶ τῷ ἀρχιοινοχόῳ καὶ ἐπὶ τῷ ἀρχισιτοποιῷ,
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

## Genesis 40:3

Greek: καὶ ἔθετο αὐτοὺς ἐν φυλακῇ εἰς τὸ δεσμωτήριον, εἰς τὸν τόπον, οὗ ᾿Ιωσὴφ ἀπῆκτο ἐκεῖ.
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

## Genesis 40:4

Greek: καὶ συνέστησεν ὁ ἀρχιδεσμώτης τῷ ᾿Ιωσὴφ αὐτούς, καὶ παρέστη αὐτοῖς· ἦσαν δὲ ἡμέρας ἐν τῇ φυλακῇ.
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

## Genesis 40:5

Greek: καὶ εἶδον ἀμφότεροι ἐνύπνιον ἐν μιᾷ νυκτί· ἡ δὲ ὅρασις τοῦ ἐνυπνίου τοῦ ἀρχιοινοχόου καὶ ἀρχισιτοποιοῦ, οἳ ἦσαν τῷ βασιλεῖ Αἰγύπτου, οἱ ὄντες ἐν τῷ δεσμωτηρίῳ, ἦν αὕτη.
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

## Genesis 40:6

Greek: εἰσῆλθε δὲ πρὸς αὐτοὺς ᾿Ιωσὴφ τῷ πρωΐ καὶ εἶδεν αὐτούς, καὶ ἦσαν τεταραγμένοι.
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

## Genesis 40:7

Greek: καὶ ἠρώτα τοὺς εὐνούχους Φαραώ, οἳ ἦσαν μετ᾿ αὐτοῦ ἐν τῇ φυλακῇ παρὰ τῷ κυρίῳ αὐτοῦ, λέγων· τί ὅτι τὰ πρόσωπα ὑμῶν σκυθρωπὰ σήμερον
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

## Genesis 40:8

Greek: οἱ δὲ εἶπαν αὐτῷ· ἐνύπνιον εἴδομεν, καὶ ὁ συγκρίνων οὐκ ἔστιν αὐτό. εἶπε δὲ αὐτοῖς ᾿Ιωσήφ· οὐχὶ διὰ τοῦ Θεοῦ ἡ διασάφησις αὐτῶν ἐστι; διηγήσασθε οὖν μοι.
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

## Genesis 40:9

Greek: καὶ διηγήσατο ὁ ἀρχιοινοχόος τὸ ἐνύπνιον αὐτοῦ τῷ ᾿Ιωσὴφ καὶ εἶπεν· ἐν τῷ ὕπνῳ μου ἦν ἄμπελος ἐναντίον μου·
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

## Genesis 40:10

Greek: ἐν δὲ τῇ ἀμπέλῳ τρεῖς πυθμένες, καὶ αὐτὴ θάλλουσα ἀνενηνοχυῖα βλαστούς· πέπειροι οἱ βότρυες σταφυλῆς.
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

## Genesis 40:11

Greek: καὶ τὸ ποτήριον Φαραὼ ἐν τῇ χειρί μου· καὶ ἔλαβον τὴν σταφυλὴν καὶ ἐξέθλιψα αὐτὴν εἰς τὸ ποτήριον καὶ ἔδωκα τὸ ποτήριον εἰς τὴν χεῖρα Φαραώ.
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

## Genesis 40:12

Greek: καὶ εἶπεν αὐτῷ ᾿Ιωσήφ· τοῦτο ἡ σύγκρισις αὐτοῦ· οἱ τρεῖς πυθμένες τρεῖς ἡμέραι εἰσίν·
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

## Genesis 40:13

Greek: ἔτι τρεῖς ἡμέραι καὶ μνησθήσεται Φαραὼ τῆς ἀρχῆς σου καὶ ἀποκαταστήσει σε ἐπί τὴν ἀρχιοινοχοΐαν σου, καὶ δώσεις τὸ ποτήριον Φαραὼ εἰς τὴν χεῖρα αὐτοῦ κατὰ τὴν ἀρχήν σου τὴν προτέραν, ὡς ἦσθα οἰνοχοῶν.
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

## Genesis 40:14

Greek: ἀλλὰ μνήσθητί μου διὰ σεαυτοῦ, ὅταν εὖ γένηταί σοι, καὶ ποιήσεις ἐν ἐμοὶ ἔλεος καὶ μνησθήσει περὶ ἐμοῦ πρὸς Φαραὼ καὶ ἐξάξεις με ἐκ τοῦ ὀχυρώματος τούτου·
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

## Genesis 40:15

Greek: ὅτι κλοπῇ ἐκλάπην ἐκ γῆς ῾Εβραίων καὶ ὧδε οὐκ ἐποίησα οὐδέν, ἀλλ᾿ ἐνέβαλόν με εἰς τὸν λάκκον τοῦτον.
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

## Genesis 40:16

Greek: καὶ εἶδεν ὁ ἀρχισιτοποιός, ὅτι ὀρθῶς συνέκρινε, καὶ εἶπε τῷ ᾿Ιωσήφ· κἀγὼ εἶδον ἐνύπνιον καὶ ᾤμην τρία κανᾶ χονδριτῶν αἴρειν ἐπὶ τῆς κεφαλῆς μου·
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

## Genesis 40:17

Greek: ἐν δὲ κανῷ τῷ ἐπάνω ἀπὸ πάντων τῶν γενῶν, ὧν Φαραὼ ἐσθίει ἔργον σιτοποιοῦ, καὶ τὰ πετεινὰ τοῦ οὐρανοῦ κατήσθιεν αὐτὰ ἀπὸ τοῦ κανοῦ τοῦ ἐπάνω τῆς κεφαλῆς μου.
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

## Genesis 40:18

Greek: ἀποκριθεὶς δὲ ᾿Ιωσὴφ εἶπεν αὐτῷ· αὕτη ἡ σύγκρισις αὐτοῦ· τὰ τρία κανᾶ τρεῖς ἡμέραι εἰσίν·
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

## Genesis 40:19

Greek: ἔτι τριῶν ἡμερῶν καὶ ἀφελεῖ Φαραὼ τὴν κεφαλήν σου ἀπὸ σοῦ καὶ κρεμάσει σε ἐπὶ ξύλου, καὶ φάγεται τὰ ὄρνεα τοῦ οὐρανοῦ τὰς σάρκας σου ἀπὸ σοῦ.
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

## Genesis 40:20

Greek: ἐγένετο δὲ ἐν τῇ ἡμέρᾳ τῇ τρίτῃ, ἡμέρα γενέσεως ἦν Φαραώ, καὶ ἐποίει πότον πᾶσι τοῖς παισὶν αὐτοῦ. καὶ ἐμνήσθη τῆς ἀρχῆς τοῦ οἰνοχόου καὶ τῆς ἀρχῆς τοῦ σιτοποιοῦ ἐν μέσῳ τῶν παίδων αὐτοῦ,
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

## Genesis 40:21

Greek: καὶ ἀποκατέστησε τὸν ἀρχιοινοχόον ἐπὶ τὴν ἀρχὴν αὐτοῦ, καὶ ἔδωκε τὸ ποτήριον εἰς τὴν χεῖρα Φαραώ,
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

## Genesis 40:22

Greek: τὸν δὲ ἀρχισιτοποιὸν ἐκρέμασε, καθὰ συνέκρινεν αὐτοῖς ᾿Ιωσήφ.
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

## Genesis 40:23

Greek: καὶ οὐκ ἐμνήσθη ὁ ἀρχιοινοχόος τοῦ ᾿Ιωσήφ, ἀλλ᾿ ἐπελάθετο αὐτοῦ.
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

# Chapter 41

## Genesis 41:1

Greek: ΕΓΕΝΕΤΟ δὲ μετὰ δύο ἔτη ἡμερῶν, Φαραὼ εἶδεν ἐνύπνιον· ᾤετο ἑστάναι ἐπὶ τοῦ ποταμοῦ,
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

## Genesis 41:2

Greek: καὶ ἰδοὺ ὥσπερ ἐκ τοῦ ποταμοῦ ἀνέβαινον ἑπτὰ βόες καλαὶ τῷ εἴδει καὶ ἐκλεκταὶ ταῖς σαρξὶ καὶ ἐβόσκοντο ἐν τῷ ῎Αχει.
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

## Genesis 41:3

Greek: ἄλλαι δὲ ἑπτὰ βόες ἀνέβαινον μετὰ ταύτας ἐκ τοῦ ποταμοῦ αἰσχραὶ τῷ εἴδει καὶ λεπταὶ ταῖς σαρξὶ καὶ ἐνέμοντο παρὰ τὰς βόας ἐπὶ τὸ χεῖλος τοῦ ποταμοῦ·
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

## Genesis 41:4

Greek: καὶ κατέφαγον αἱ ἑπτὰ βόες αἱ αἰσχραὶ καὶ λεπταὶ ταῖς σαρξὶ τὰς ἑπτὰ βόας τὰς καλὰς τῷ εἴδει καὶ τὰς ἐκλεκτὰς ταῖς σαρξί. ἠγέρθη δὲ Φαραώ.
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

## Genesis 41:5

Greek: καὶ ἐνυπνιάσθη τὸ δεύτερον, καὶ ἰδοὺ ἑπτὰ στάχυες ἀνέβαινον ἐν τῷ πυθμένι ἑνὶ ἐκλεκτοὶ καὶ καλοί·
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

## Genesis 41:6

Greek: καὶ ἰδοὺ ἑπτὰ στάχυες λεπτοὶ καὶ ἀνεμόφθοροι ἀνεφύοντο μετ᾿ αὐτούς·
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

## Genesis 41:7

Greek: καὶ κατέπιον οἱ ἑπτὰ στάχυες οἱ λεπτοὶ καὶ ἀνεμόφθοροι τοὺς ἑπτὰ στάχυας τοὺς ἐκλεκτοὺς καὶ τοὺς πλήρεις. ἠγέρθη δὲ Φαραώ, καὶ ἦν ἐνύπνιον.
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

## Genesis 41:8

Greek: ᾿Εγένετο δὲ πρωΐ καὶ ἐταράχθη ἡ ψυχὴ αὐτοῦ, καὶ ἀποστείλας ἐκάλεσε πάντας τοὺς ἐξηγητὰς Αἰγύπτου καὶ πάντας τοὺς σοφοὺς αὐτῆς, καὶ διηγήσατο αὐτοῖς Φαραὼ τὸ ἐνύπνιον αὐτοῦ, καὶ οὐκ ἦν ὁ ἀπαγγέλλων αὐτὸ τῷ Φαραώ.
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

## Genesis 41:9

Greek: καὶ ἐλάλησεν ὁ ἀρχιοινοχόος πρὸς Φαραὼ λέγων· τὴν ἁμαρτίαν μου ἀναμιμνήσκω σήμερον.
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

## Genesis 41:10

Greek: Φαραὼ ὠργίσθη τοῖς παισὶν αὐτοῦ καὶ ἔθετο ἡμᾶς ἐν φυλακῇ ἐν τῷ οἴκῳ τοῦ ἀρχιμαγείρου, ἐμέ τε καὶ τὸν ἀρχισιτοποιόν.
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

## Genesis 41:11

Greek: καὶ εἴδομεν ἐνύπνιον ἀμφότεροι ἐν νυκτὶ μιᾷ ἐγὼ καὶ αὐτός, ἕκαστος κατὰ τὸ αὐτοῦ ἐνύπνιον εἴδομεν.
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

## Genesis 41:12

Greek: ἦν δὲ ἐκεῖ μεθ᾿ ἡμῶν νεανίσκος παῖς ῾Εβραῖος τοῦ ἀρχιμαγείρου, καὶ διηγησάμεθα αὐτῷ, καὶ συνέκρινεν ἡμῖν.
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

## Genesis 41:13

Greek: ἐγενήθη δέ, καθὼς συνέκρινεν ἡμῖν, οὕτω καὶ συνέβη, ἐμέ τε ἀποκατασταθῆναι ἐπὶ τὴν ἀρχήν μου, ἐκεῖνον δὲ κρεμασθῆναι.
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

## Genesis 41:14

Greek: ᾿Αποστείλας δὲ Φαραὼ ἐκάλεσε τὸν ᾿Ιωσήφ, καὶ ἐξήγαγον αὐτὸν ἀπὸ τοῦ ὀχυρώματος καὶ ἐξύρησαν αὐτὸν καὶ ἤλλαξαν τὴν στολὴν αὐτοῦ, καὶ ἦλθε πρὸς Φαραώ.
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

## Genesis 41:15

Greek: εἶπε δὲ Φαραὼ πρὸς ᾿Ιωσήφ· ἐνύπνιον ἑώρακα, καὶ ὁ συγκρίνων οὐκ ἔστιν αὐτό· ἐγὼ δὲ ἀκήκοα περὶ σοῦ λεγόντων, ἀκούσαντά σε ἐνύπνια συγκρῖναι αὐτά.
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

## Genesis 41:16

Greek: ἀποκριθεὶς δὲ ᾿Ιωσὴφ τῷ Φαραὼ εἶπεν· ἄνευ τοῦ Θεοῦ οὐκ ἀποκριθήσεται τὸ σωτήριον Φαραώ.
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

## Genesis 41:17

Greek: ἐλάλησε δὲ Φαραὼ τῷ ᾿Ιωσὴφ λέγων· ἐν τῷ ὕπνῳ μου ᾤμην ἑστάναι παρὰ τὸ χεῖλος τοῦ ποταμοῦ,
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

## Genesis 41:18

Greek: καὶ ὥσπερ ἐκ τοῦ ποταμοῦ ἀνέβαινον ἑπτὰ βόες καλαὶ τῷ εἴδει καὶ ἐκλεκταὶ ταῖς σαρξί, καὶ ἐνέμοντο ἐν τῷ ῎Αχει.
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

## Genesis 41:19

Greek: καὶ ἰδοὺ ἑπτὰ βόες ἕτεραι ἀνέβαινον ὀπίσω αὐτῶν ἐκ τοῦ ποταμοῦ πονηραὶ καὶ αἰσχραὶ τῷ εἴδει καὶ λεπταὶ ταῖς σαρξίν, οἵας οὐκ εἶδον τοιαύτας ἐν ὅλῃ γῇ Αἰγύπτου αἰσχροτέρας·
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

## Genesis 41:20

Greek: καὶ κατέφαγον αἱ ἑπτὰ βόες αἱ αἰσχραὶ καὶ λεπταὶ τὰς ἑπτὰ βόας τὰς πρώτας τὰς καλὰς καὶ τὰς ἐκλεκτάς,
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

## Genesis 41:21

Greek: καὶ εἰσῆλθον εἰς τὰς κοιλίας αὐτῶν καὶ οὐ διάδηλοι ἐγένοντο, ὅτι εἰσῆλθον εἰς τὰς κοιλίας αὐτῶν, καὶ αἱ ὄψεις αὐτῶν αἰσχραί, καθὰ καὶ τὴν ἀρχήν· ἐξεγερθεὶς δὲ ἐκοιμήθην
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

## Genesis 41:22

Greek: καὶ εἶδον πάλιν ἐν τῷ ὕπνῳ μου, καὶ ὥσπερ ἑπτὰ στάχυες ἀνέβαινον ἐν πυθμένι ἑνὶ πλήρεις καὶ καλοί·
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

## Genesis 41:23

Greek: ἄλλοι δὲ ἑπτὰ στάχυες λεπτοὶ καὶ ἀνεμόφθοροι ἀνεφύοντο ἐχόμενοι αὐτῶν.
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

## Genesis 41:24

Greek: καὶ κατέπιον οἱ ἑπτὰ στάχυες οἱ λεπτοὶ καὶ ἀνεμόφθοροι τοὺς ἑπτὰ στάχυας τοὺς καλοὺς καὶ τοὺς πλήρεις. εἶπα οὖν τοῖς ἐξηγηταῖς, καὶ οὐκ ἦν ὁ ἀπαγγέλλων μοι αὐτό.
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

## Genesis 41:25

Greek: Καὶ εἶπεν ᾿Ιωσὴφ τῷ Φαραώ· τὸ ἐνύπνιον Φαραὼ ἕν ἐστιν· ὅσα ὁ Θεὸς ποιεῖ, ἔδειξε τῷ Φαραώ.
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

## Genesis 41:26

Greek: αἱ ἑπτὰ βόες αἱ καλαὶ ἑπτὰ ἔτη ἐστί, καὶ οἱ ἑπτὰ στάχυες οἱ καλοὶ ἑπτὰ ἔτη ἐστί· τὸ ἐνύπνιον Φαραὼ ἕν ἐστι,
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

## Genesis 41:27

Greek: καὶ αἱ ἑπτὰ βόες αἱ λεπταὶ αἱ ἀναβαίνουσαι ὀπίσω αὐτῶν ἑπτὰ ἔτη ἐστί, καὶ οἱ ἑπτὰ στάχυες οἱ λεπτοὶ καὶ ἀνεμόφθοροι ἔσονται ἑπτὰ ἔτη λιμοῦ.
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

## Genesis 41:28

Greek: τὸ δὲ ρῆμα, ὃ εἴρηκα Φαραώ, ὅσα ὁ Θεὸς ποιεῖ, ἔδειξε τῷ Φαραώ,
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

## Genesis 41:29

Greek: ἰδοὺ ἑπτὰ ἔτη ἔρχεται εὐθηνία πολλὴ ἐν πάσῃ γῇ Αἰγύπτου·
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

## Genesis 41:30

Greek: ἥξει δὲ ἑπτὰ ἔτη λιμοῦ μετὰ ταῦτα, καὶ ἐπιλήσονται τῆς πλησμονῆς τῆς ἐσομένης ἐν ὅλῃ Αἰγύπτῳ, καὶ ἀναλώσει ὁ λιμὸς τὴν γῆν,
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

## Genesis 41:31

Greek: καὶ οὐκ ἐπιγνωσθήσεται ἡ εὐθηνία ἐπὶ τῆς γῆς ἀπὸ τοῦ λιμοῦ τοῦ ἐσομένου μετὰ ταῦτα· ἰσχυρὸς γὰρ ἔσται σφόδρα.
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

## Genesis 41:32

Greek: περὶ δὲ τοῦ δευτερῶσαι τὸ ἐνύπνιον Φαραὼ δίς, ὅτι ἀληθὲς ἔσται τὸ ρῆμα τὸ παρὰ τοῦ Θεοῦ, καὶ ταχυνεῖ ὁ Θεὸς τοῦ ποιῆσαι αὐτό.
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

## Genesis 41:33

Greek: νῦν οὖν σκέψαι ἄνθρωπον φρόνιμον καὶ συνετὸν καὶ κατάστησον αὐτὸν ἐπὶ γῆς Αἰγύπτου·
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

## Genesis 41:34

Greek: καὶ ποιησάτω Φαραὼ καὶ καταστησάτω τοπάρχας ἐπὶ τῆς γῆς, καὶ ἀποπεμπτωσάτωσαν πάντα τὰ γεννήματα τῆς γῆς Αἰγύπτου τῶν ἑπτὰ ἐτῶν τῆς εὐθηνίας
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

## Genesis 41:35

Greek: καὶ συναγαγέτωσαν πάντα τὰ βρώματα τῶν ἑπτὰ ἐτῶν τῶν ἐρχομένων τῶν καλῶν τούτων, καὶ συναχθήτω ὁ σῖτος ὑπὸ χεῖρα Φαραώ, βρώματα ἐν ταῖς πόλεσι φυλαχθήτω·
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

## Genesis 41:36

Greek: καὶ ἔσται τὰ βρώματα τὰ πεφυλαγμένα τῇ γῇ εἰς τὰ ἑπτὰ ἔτη τοῦ λιμοῦ, ἃ ἔσονται ἐν γῇ Αἰγύπτου, καὶ οὐκ ἐκτριβήσεται ἡ γῇ ἐν τῷ λιμῷ.
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

## Genesis 41:37

Greek: ῎Ηρεσε δὲ τὸ ρῆμα ἐναντίον Φαραὼ καὶ ἐναντίον πάντων τῶν παίδων αὐτοῦ,
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

## Genesis 41:38

Greek: καὶ εἶπε Φαραὼ πᾶσι τοῖς παισὶν αὐτοῦ· μὴ εὑρήσομεν ἄνθρωπον τοιοῦτον, ὃς ἔχει πνεῦμα Θεοῦ ἐν αὐτῷ
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

## Genesis 41:39

Greek: εἶπε δὲ Φαραὼ τῷ ᾿Ιωσήφ· ἐπειδὴ ἔδειξεν ὁ Θεός σοι πάντα ταῦτα, οὐκ ἔστιν ἄνθρωπος φρονιμώτερος καὶ συνετώτερός σου·
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

## Genesis 41:40

Greek: σὺ ἔσῃ ἐπὶ τῷ οἴκῳ μου, καὶ ἐπὶ τῷ στόματί σου ὑπακούσεται πᾶς ὁ λαός μου· πλὴν τὸν θρόνον ὑπερέξω σου ἐγώ.
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

## Genesis 41:41

Greek: εἶπε δὲ Φαραὼ τῷ ᾿Ιωσήφ· ἰδοὺ καθίστημί σε σήμερον ἐπὶ πάσης γῆς Αἰγύπτου.
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

## Genesis 41:42

Greek: καὶ περιελόμενος Φαραὼ τὸν δακτύλιον ἀπὸ τῆς χειρὸς αὐτοῦ, περιέθηκεν αὐτὸν ἐπί τὴν χεῖρα ᾿Ιωσὴφ καὶ ἐνέδυσεν αὐτὸν στολὴν βυσσίνην καὶ περιέθηκε κλοιὸν χρυσοῦν περὶ τὸν τράχηλον αὐτοῦ·
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

## Genesis 41:43

Greek: καὶ ἀνεβίβασεν αὐτὸν ἐπὶ τὸ ἅρμα τὸ δεύτερον τῶν αὐτοῦ, καὶ ἐκήρυξεν ἔμπροσθεν αὐτοῦ κήρυξ· καὶ κατέστησεν αὐτὸν ἐφ᾿ ὅλης γῆς Αἰγύπτου.
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

## Genesis 41:44

Greek: εἶπε δὲ Φαραὼ τῷ ᾿Ιωσήφ· ἐγὼ Φαραώ, ἄνευ σοῦ οὐκ ἐξαρεῖ οὐδεὶς τὴν χεῖρα αὐτοῦ ἐπὶ πάσης γῆς Αἰγύπτου.
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

## Genesis 41:45

Greek: καὶ ἐκάλεσε Φαραὼ τὸ ὄνομα ᾿Ιωσήφ, Ψονθομφανήχ· καὶ ἔδωκεν αὐτῷ τὴν ᾿Ασεννὲθ θυγατέρα Πετεφρῆ ἱερέως ῾Ηλιουπόλεως αὐτῷ εἰς γυναῖκα.
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

## Genesis 41:46

Greek: ᾿Ιωσὴφ δὲ ἦν ἐτῶν τριάκοντα, ὅτε ἔστη ἐναντίον Φαραὼ βασιλέως Αἰγύπτου. ᾿Εξῆλθε δὲ ᾿Ιωσὴφ ἀπὸ προσώπου Φαραώ, καὶ διῆλθε πᾶσαν γῆν Αἰγύπτου.
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

## Genesis 41:47

Greek: καὶ ἐποίησεν ἡ γῆ ἐν τοῖς ἑπτὰ ἔτεσι τῆς εὐθηνίας δράγματα·
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

## Genesis 41:48

Greek: καὶ συνήγαγε πάντα τὰ βρώματα τῶν ἑπτὰ ἐτῶν, ἐν οἷς ἦν ἡ εὐθυνία ἐν τῇ γῇ Αἰγύπτου, καὶ ἔθηκε τὰ βρώματα ἐν ταῖς πόλεσι, βρώματα τῶν πεδίων τῆς πόλεως τῶν κύκλῳ αὐτῆς ἔθηκεν ἐν αὐτῇ.
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

## Genesis 41:49

Greek: καὶ συνήγαγεν ᾿Ιωσὴφ σῖτον ὡσεὶ τὴν ἄμμον τῆς θαλάσσης πολὺν σφόδρα, ἕως οὐκ ἠδύνατο ἀριθμηθῆναι, οὐ γὰρ ἦν ἀριθμός.
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

## Genesis 41:50

Greek: Τῷ δὲ ᾿Ιωσὴφ ἐγένοντο υἱοὶ δύο πρὸ τοῦ ἐλθεῖν τὰ ἑπτὰ ἔτη τοῦ λιμοῦ, οὓς ἔτεκεν αὐτῷ ᾿Ασεννὲθ ἡ θυγάτηρ Πετεφρῆ ἱερέως ῾Ηλιουπόλεως.
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

## Genesis 41:51

Greek: ἐκάλεσε δὲ ᾿Ιωσὴφ τὸ ὄνομα τοῦ πρωτοτόκου Μανασσῆ, ὅτι ἐπιλαθέσθαι με ἐποίησεν ὁ Θεὸς πάντων τῶν πόνων μου καὶ πάντων τῶν τοῦ πατρός μου.
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

## Genesis 41:52

Greek: τὸ δὲ ὄνομα τοῦ δευτέρου ἐκάλεσεν ᾿Εφραΐμ, ὅτι ηὔξησέ με ὁ Θεὸς ἐν γῇ ταπεινώσεώς μου.
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

## Genesis 41:53

Greek: Παρῆλθε δὲ τὰ ἑπτὰ ἔτη τῆς εὐθηνίας, ἃ ἐγένοντο ἐν τῇ γῇ Αἰγύπτου,
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

## Genesis 41:54

Greek: καὶ ἤρξατο τὰ ἑπτὰ ἔτη τοῦ λιμοῦ ἔρχεσθαι, καθὰ εἶπεν ᾿Ιωσήφ. καὶ ἐγένετο λιμὸς ἐν πάσῃ τῇ γῇ, ἐν δὲ πάσῃ τῇ γῇ Αἰγύπτου ἦσαν ἄρτοι.
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

## Genesis 41:55

Greek: καὶ ἐπείνασε πᾶσα ἡ γῆ Αἰγύπτου, ἔκραξε δὲ ὁ λαὸς πρὸς Φαραὼ περὶ ἄρτων· εἶπε δὲ Φαραὼ πᾶσι τοῖς Αἰγυπτίοις· πορεύεσθε πρὸς ᾿Ιωσήφ, καὶ ὃ ἐὰν εἴπῃ ὑμῖν, ποιήσατε.
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

## Genesis 41:56

Greek: καὶ ὁ λιμὸς ἦν ἐπὶ προσώπου πάσης τῆς γῆς· ἀνέῳξε δὲ ᾿Ιωσὴφ πάντας τοὺς σιτοβολῶνας καὶ ἐπώλει πᾶσι τοῖς Αἰγυπτίοις.
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

## Genesis 41:57

Greek: καὶ πᾶσαι αἱ χῶραι ἦλθον εἰς Αἴγυπτον ἀγοράζειν πρὸς ᾿Ιωσήφ· ἐπεκράτησε γὰρ ὁ λιμὸς ἐν πάσῃ τῇ γῇ.
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

# Chapter 42

## Genesis 42:1

Greek: ΙΔΩΝ δὲ ᾿Ιακὼβ ὅτι ἐστὶ πρᾶσις ἐν Αἰγύπτῳ, εἶπε τοῖς υἱοῖς αὐτοῦ· ἱνατί ραθυμεῖτε
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

## Genesis 42:2

Greek: ἰδοὺ ἀκήκοα ὅτι ἐστὶ σῖτος ἐν Αἰγύπτῳ· κατάβητε ἐκεῖ καὶ πρίασθε ἡμῖν μικρὰ βρώματα, ἵνα ζήσωμεν καὶ μὴ ἀποθάνωμεν.
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

## Genesis 42:3

Greek: κατέβησαν δὲ οἱ ἀδελφοὶ ᾿Ιωσὴφ οἱ δέκα πρίασθαι σῖτον ἐξ Αἰγύπτου·
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

## Genesis 42:4

Greek: τὸν δὲ Βενιαμὶν τὸν ἀδελφὸν ᾿Ιωσὴφ οὐκ ἀπέστειλε μετὰ τῶν ἀδελφῶν αὐτοῦ, εἶπε γάρ· μή ποτε συμβῇ αὐτῷ μαλακία.
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

## Genesis 42:5

Greek: ῏Ηλθον δὲ οἱ υἱοὶ ᾿Ισραὴλ ἀγοράζειν μετὰ τῶν ἐρχομένων· ἦν γὰρ ὁ λιμὸς ἐν γῇ Χαναάν.
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

## Genesis 42:6

Greek: ᾿Ιωσὴφ δὲ ἦν ὁ ἄρχων τῆς γῆς, οὗτος ἐπώλει παντὶ τῷ λαῷ τῆς γῆς· ἐλθόντες δὲ οἱ ἀδελφοὶ ᾿Ιωσὴφ προσεκύνησαν αὐτῷ ἐπὶ πρόσωπον ἐπὶ τὴν γῆν.
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

## Genesis 42:7

Greek: ἰδὼν δὲ ᾿Ιωσὴφ τούς ἀδελφοὺς αὐτοῦ ἐπέγνω καὶ ἠλλοτριοῦτο ἀπ᾿ αὐτῶν καὶ ἐλάλησεν αὐτοῖς σκληρὰ καὶ εἶπεν αὐτοῖς· πόθεν ἥκατε; οἱ δὲ εἶπον· ἐκ γῆς Χαναὰν ἀγοράσαι βρώματα.
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

## Genesis 42:8

Greek: ἐπέγνω δὲ ᾿Ιωσὴφ τοὺς ἀδελφοὺς αὐτοῦ, αὐτοὶ δὲ οὐκ ἐπέγνωσαν αὐτόν.
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

## Genesis 42:9

Greek: καὶ ἐμνήσθη ᾿Ιωσὴφ τῶν ἐνυπνίων αὐτοῦ, ὧν εἶδεν αὐτός, καὶ εἶπεν αὐτοῖς· κατάσκοποί ἐστε, κατανοῆσαι τὰ ἴχνη τῆς χώρας ἥκατε.
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

## Genesis 42:10

Greek: οἱ δὲ εἶπαν· οὐχί, κύριε, οἱ παῖδές σου ἤλθομεν πρίασθαι βρώματα·
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

## Genesis 42:11

Greek: πάντες ἐσμὲν υἱοὶ ἑνὸς ἀνθρώπου· εἰρηνικοί ἐσμεν, οὐκ εἰσὶν οἱ παῖδές σου κατάσκοποι.
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

## Genesis 42:12

Greek: εἶπε δὲ αὐτοῖς· οὐχί, ἀλλὰ τὰ ἴχνη τῆς γῆς ἤλθετε ἰδεῖν.
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

## Genesis 42:13

Greek: οἱ δὲ εἶπαν· δώδεκά ἐσμεν οἱ παῖδες σου ἀδελφοὶ ἐν γῇ Χαναάν, καὶ ἰδοὺ ὁ νεώτερος μετὰ τοῦ πατρὸς ἡμῶν σήμερον, ὁ δὲ ἕτερος οὐχ ὑπάρχει.
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

## Genesis 42:14

Greek: εἶπε δὲ αὐτοῖς ᾿Ιωσήφ· τοῦτό ἐστιν ὃ εἴρηκα ὑμῖν λέγων, ὅτι κατάσκοποί ἐστε·
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

## Genesis 42:15

Greek: ἐν τούτῳ φανεῖσθε· νὴ τὴν ὑγίειαν Φαραώ, οὐ μὴ ἐξέλθητε ἐντεῦθεν, ἐὰν μὴ ὁ ἀδελφὸς ὑμῶν ὁ νεώτερος ἔλθῃ ὧδε.
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

## Genesis 42:16

Greek: ἀποστείλατε ἐξ ὑμῶν ἕνα καὶ λάβετε τὸν ἀδελφὸν ὑμῶν, ὑμεῖς δὲ ἀπάχθητε ἕως τοῦ φανερὰ γενέσθαι τὰ ρήματα ὑμῶν, εἰ ἀληθεύετε ἢ οὔ· εἰ δὲ μή, νὴ τὴν ὑγίειαν Φαραώ, ἦ μὴν κατάσκοποί ἐστε.
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

## Genesis 42:17

Greek: καὶ ἔθετο αὐτοὺς ἐν φυλακῇ ἡμέρας τρεῖς.
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

## Genesis 42:18

Greek: Εἶπε δὲ αὐτοῖς τῇ ἡμέρᾳ τῇ τρίτῃ· τοῦτο ποιήσατε καὶ ζήσεσθε, τὸν Θεὸν γὰρ ἐγὼ φοβοῦμαι·
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

## Genesis 42:19

Greek: εἰ εἰρηνικοί ἐστε, ἀδελφὸς ὑμῶν κατασχεθήτω εἷς ἐν τῇ φυλακῇ, αὐτοὶ δὲ βαδίσατε καὶ ἀπαγάγετε τὸν ἀγορασμὸν τῆς σιτοδοσίας ὑμῶν,
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

## Genesis 42:20

Greek: καὶ τὸν ἀδελφὸν ὑμῶν τὸν νεώτερον ἀγάγετε πρός με, καὶ πιστευθήσονται τὰ ρήματα ὑμῶν· εἰ δὲ μή, ἀποθανεῖσθε. ἐποίησαν δὲ οὕτως.
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

## Genesis 42:21

Greek: καὶ εἶπεν ἕκαστος πρὸς τὸν ἀδελφὸν αὐτοῦ· ναί, ἐν ἁμαρτίαις γάρ ἐσμεν περὶ τοῦ ἀδελφοῦ ἡμῶν, ὅτι ὑπερείδομεν τὴν θλῖψιν τῆς ψυχῆς αὐτοῦ, ὅτε κατεδέετο ἡμῶν, καὶ οὐκ εἰσηκούσαμεν αὐτοῦ· καὶ ἕνεκεν τούτου ἐπῆλθεν ἐφ᾿ ἡμᾶς ἡ θλῖψις αὕτη.
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

## Genesis 42:22

Greek: ἀποκριθεὶς δὲ Ρουβὴν εἶπεν αὐτοῖς· οὐκ ἐλάλησα ὑμῖν λέγων, μὴ ἀδικήσητε τὸ παιδάριον; καὶ οὐκ ἠκούσατέ μου; καὶ ἰδοὺ τὸ αἷμα αὐτοῦ ἐκζητεῖται.
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

## Genesis 42:23

Greek: αὐτοὶ δὲ οὐκ ᾔδεισαν ὅτι ἀκούει ᾿Ιωσήφ· ὁ γὰρ ἑρμηνευτὴς ἀνὰ μέσον αὐτῶν ἦν.
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

## Genesis 42:24

Greek: ἀποστραφεὶς δὲ ἀπ᾿ αὐτῶν ἔκλαυσεν ᾿Ιωσήφ. καὶ πάλιν προσῆλθε πρὸς αὐτοὺς καὶ εἶπεν αὐτοῖς· καὶ ἔλαβε τὸν Συμεὼν ἀπ᾿ αὐτῶν καὶ ἔδησεν αὐτὸν ἐναντίον αὐτῶν.
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

## Genesis 42:25

Greek: ἐνετείλατο δὲ ᾿Ιωσήφ ἐμπλῆσαι τὰ ἀγγεῖα αὐτῶν σίτου καὶ ἀποδοῦναι τὸ ἀργύριον αὐτῶν ἑκάστῳ εἰς τὸν σάκκον αὐτοῦ καὶ δοῦναι αὐτοῖς ἐπισιτισμὸν εἰς τὴν ὁδόν. καὶ ἐγενήθη αὐτοῖς οὕτως.
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

## Genesis 42:26

Greek: καὶ ἐπιθέντες τὸν σῖτον ἐπὶ τοὺς ὄνους αὐτῶν ἀπῆλθον ἐκεῖθεν.
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

## Genesis 42:27

Greek: λύσας δὲ εἷς τὸν μάρσιππον αὐτοῦ δοῦναι χορτάσματα τοῖς ὄνοις αὐτοῦ, οὗ κατέλυσαν, καὶ εἶδε τὸν δεσμὸν τοῦ ἀργυρίου αὐτοῦ, καὶ ἦν ἐπάνω τοῦ στόματος τοῦ μαρσίππου·
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

## Genesis 42:28

Greek: καὶ εἶπε τοῖς ἀδελφοῖς αὐτοῦ· ἐπεδόθη μοι τὸ ἀργύριον, καὶ ἰδοὺ τοῦτο ἐν τῷ μαρσίππῳ μου, καὶ ἐξέστη ἡ καρδία αὐτῶν, καὶ ἐταράχθησαν πρὸς ἀλλήλους λέγοντες· τί τοῦτο ἐποίησεν ὁ Θεὸς ἡμῖν
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

## Genesis 42:29

Greek: ῏Ηλθον δὲ πρὸς ᾿Ιακὼβ τὸν πατέρα αὐτῶν εἰς γῆν Χαναὰν καὶ ἀπήγγειλαν αὐτῷ πάντα τὰ συμβάντα αὐτοῖς, λέγοντες·
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

## Genesis 42:30

Greek: λελάληκεν ὁ ἄνθρωπος ὁ κύριος τῆς γῆς πρὸς ἡμᾶς σκληρὰ καὶ ἔθετο ἡμᾶς ἐν φυλακῇ ὡς κατασκοπεύοντας τὴν γῆν.
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

## Genesis 42:31

Greek: εἴπαμεν δὲ αὐτῷ· εἰρηνικοί ἐσμέν, οὐκ ἐσμὲν κατάσκοποι·
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

## Genesis 42:32

Greek: δώδεκα ἀδελφοί ἐσμεν, υἱοὶ τοῦ πατρὸς ἡμῶν· ὁ εἷς οὐχ ὑπάρχει, ὁ δὲ μικρὸς μετὰ τοῦ πατρὸς ἡμῶν σήμερον ἐν γῇ Χαναάν.
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

## Genesis 42:33

Greek: εἶπε δὲ ἡμῖν ὁ ἄνθρωπος ὁ κύριος τῆς γῆς· ἐν τούτῳ γνώσομαι ὅτι εἰρηνικοί ἐστε· ἀδελφὸν ἕνα ἄφετε ὧδε μετ᾿ ἐμοῦ, τὸν δὲ ἀγορασμὸν τῆς σιτοδοσίας τοῦ οἴκου ὑμῶν λαβόντες ἀπέλθατε.
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

## Genesis 42:34

Greek: καὶ ἀγάγετε πρός με τὸν ἀδελφὸν ὑμῶν τὸν νεώτερον, καὶ γνώσομαι ὅτι οὐ κατάσκοποί ἐστε, ἀλλ᾿ ὅτι εἰρηνικοί ἐστε, καὶ τὸν ἀδελφὸν ὑμῶν ἀποδώσω ὑμῖν, καὶ τῇ γῇ ἐμπορεύσεσθε.
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

## Genesis 42:35

Greek: ἐγένετο δὲ ἐν τῷ κατακενοῦν αὐτοὺς τοὺς σάκκους αὐτῶν, καὶ ἦν ἑκάστου ὁ δεσμὸς τοῦ ἀργυρίου ἐν τῷ σάκκῳ αὐτῶν· καὶ εἶδον τοὺς δεσμοὺς τοῦ ἀργυρίου αὐτῶν αὐτοὶ καὶ ὁ πατὴρ αὐτῶν, καὶ ἐφοβήθησαν.
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

## Genesis 42:36

Greek: εἶπε δὲ αὐτοῖς ᾿Ιακὼβ ὁ πατὴρ αὐτῶν· ἐμὲ ἠτεκνώσατε, ᾿Ιωσὴφ οὔκ ἔστι, Συμεὼν οὐκ ἔστι, καὶ τὸν Βενιαμὶν λήψεσθε; ἐπ᾿ ἐμὲ ἐγένετο ταῦτα πάντα.
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

## Genesis 42:37

Greek: εἶπε δὲ Ρουβὴν τῷ πατρὶ αὐτῶν λέγων· τοὺς δύο υἱούς μου ἀπόκτεινον, ἐὰν μὴ ἀγάγω αὐτὸν πρὸς σέ· δὸς αὐτὸν εἰς τὴν χεῖρά μου, κἀγὼ ἀνάξω αὐτὸν πρὸς σέ.
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

## Genesis 42:38

Greek: ὁ δὲ εἶπεν· οὐ καταβήσεται ὁ υἱός μου μεθ᾿ ὑμῶν, ὅτι ὁ ἀδελφὸς αὐτοῦ ἀπέθανε καὶ αὐτὸς μόνος καταλέλειπται· καὶ συμβήσεται αὐτὸν μαλακισθῆναι ἐν τῇ ὁδῷ, ᾗ ἐὰν πορεύησθε, καὶ κατάξετέ μου τὸ γῆρας μετὰ λύπης εἰς ἅδου.
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

## Genesis 42:39

Greek: ὁ δὲ λιμὸς ἐνίσχυσεν ἐπὶ τῆς γῆς.
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

# Chapter 43

## Genesis 43:1

Greek: ΕΓΕΝΕΤΟ δὲ ἡνίκα συνετέλεσαν καταφαγεῖν τὸν σῖτον, ὃν ἤνεγκαν ἐξ Αἰγύπτου, καὶ εἶπεν αὐτοῖς ὁ πατὴρ αὐτῶν· πάλιν πορευθέντες πρίασθε ἡμῖν μικρὰ βρώματα.
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

## Genesis 43:2

Greek: εἶπε δὲ αὐτῷ ᾿Ιούδας λέγων· διαμαρτυρίᾳ μεμαρτύρηται ἡμῖν ὁ ἄνθρωπος ὁ κύριος τῆς γῆς λέγων· οὐκ ὄψεσθε τὸ πρόσωπόν μου, ἐὰν μὴ ὁ ἀδελφὸς ὑμῶν ὁ νεώτερος μεθ᾿ ὑμῶν ᾖ·
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

## Genesis 43:3

Greek: εἰ μὲν οὖν ἀποστέλλῃς τὸν ἀδελφὸν ἡμῶν μεθ᾿ ἡμῶν, καταβησόμεθα, καὶ ἀγοράσομέν σοι βρώματα.
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

## Genesis 43:4

Greek: εἰ δὲ μὴ ἀποστέλλῃς τὸν ἀδελφὸν ἡμῶν μεθ᾿ ἡμῶν, οὐ πορευσόμεθα. ὁ γὰρ ἄνθρωπος εἶπεν ἡμῖν, λέγων· οὐκ ὄψεσθέ μου τὸ πρόσωπον, ἐὰν μὴ ὁ ἀδελφὸς ὑμῶν ὁ νεώτερος μεθ᾿ ὑμῶν ᾖ.
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

## Genesis 43:5

Greek: εἶπε δὲ ᾿Ισραήλ· τί ἐκακοποιήσατέ με, ἀναγγείλαντες τῷ ἀνθρώπῳ ὅτι ἐστὶν ὑμῖν ἀδελφός
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

## Genesis 43:6

Greek: οἱ δὲ εἶπαν· ἐρωτῶν ἐπηρώτησεν ἡμᾶς ὁ ἄνθρωπος καὶ τὴν γενεὰν ἡμῶν λέγων· εἰ ἔτι ὁ πατὴρ ὑμῶν ζῇ καὶ εἰ ἔστιν ὑμῖν ἀδελφός; καὶ ἀπηγγείλαμεν αὐτῷ κατὰ τὴν ἐπερώτησιν ταύτην. μὴ ᾔδειμεν ὅτι ἐρεῖ ἡμῖν· ἀγάγετε τὸν ἀδελφὸν ὑμῶν
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

## Genesis 43:7

Greek: εἶπε δὲ ᾿Ιούδας πρὸς ᾿Ισραὴλ τὸν πατέρα αὐτοῦ· ἀπόστειλον τὸ παιδάριον μετ᾿ ἐμοῦ, καὶ ἀναστάντες πορευσόμεθα, ἵνα ζῶμεν καὶ μὴ ἀποθάνωμεν καὶ ἡμεῖς καὶ σὺ καὶ ἡ ἀποσκευὴ ἡμῶν.
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

## Genesis 43:8

Greek: ἐγὼ δὲ ἐκδέχομαι αὐτόν, ἐκ χειρός μου ζήτησον αὐτόν· ἐὰν μὴ ἀγάγω αὐτὸν πρὸς σὲ καὶ στήσω αὐτὸν ἐναντίον σου, ἡμαρτηκὼς ἔσομαι εἰς σὲ πάσας τὰς ἡμέρας.
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

## Genesis 43:9

Greek: εἰ μὴ γὰρ ἐβραδύναμεν, ἤδη ἂν ὑπεστρέψαμεν δίς.
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

## Genesis 43:10

Greek: εἶπε δὲ αὐτοῖς ᾿Ισραὴλ ὁ πατὴρ αὐτῶν· εἰ οὕτως ἐστί, τοῦτο ποιήσατε· λάβετε ἀπὸ τῶν καρπῶν τῆς γῆς ἐν τοῖς ἀγγείοις ὑμῶν καὶ καταγάγετε τῷ ἀνθρώπῳ δῶρα τῆς ρητίνης καὶ τοῦ μέλιτος, θυμίαμά τε καὶ στακτὴν καὶ τερέβινθον καὶ κάρυα.
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

## Genesis 43:11

Greek: καὶ τὸ ἀργύριον δισσὸν λάβετε ἐν ταῖς χερσὶν ὑμῶν· καὶ τὸ ἀργύριον τὸ ἀποστραφὲν ἐν τοῖς μαρσίπποις ὑμῶν ἀποστρέψατε μεθ᾿ ὑμῶν· μή ποτε ἀγνόημά ἐστι.
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

## Genesis 43:12

Greek: καὶ τὸν ἀδελφὸν ὑμῶν λάβετε καὶ ἀναστάντες κατάβητε πρὸς τὸν ἄνθρωπον.
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

## Genesis 43:13

Greek: ὁ δὲ Θεός μου δῴη ὑμῖν χάριν ἐναντίον τοῦ ἀνθρώπου, καὶ ἀποστείλαι τὸν ἀδελφὸν ὑμῶν τὸν ἕνα καὶ τὸν Βενιαμίν· ἐγὼ μὲν γὰρ καθάπερ ἠτέκνωμαι, ἠτέκνωμαι.
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

## Genesis 43:14

Greek: Λαβόντες δὲ οἱ ἄνδρες τὰ δῶρα ταῦτα καὶ τὸ ἀργύριον διπλοῦν ἔλαβον ἐν ταῖς χερσὶν αὐτῶν καὶ τὸν Βενιαμὶν καὶ ἀναστάντες κατέβησαν εἰς Αἴγυπτον καὶ ἔστησαν ἐναντίον ᾿Ιωσήφ.
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

## Genesis 43:15

Greek: εἶδε δὲ ᾿Ιωσὴφ αὐτοὺς καὶ τὸν Βενιαμὶν τὸν ἀδελφὸν αὐτοῦ τὸν ὁμομήτριον καὶ εἶπε τῷ ἐπὶ τῆς οἰκίας αὐτοῦ· εἰσάγαγε τοὺς ἀνθρώπους εἰς τὴν οἰκίαν καὶ σφάξον θύματα καὶ ἑτοίμασον· μετ᾿ ἐμοῦ γὰρ φάγονται οἱ ἄνθρωποι ἄρτους τὴν μεσημβρίαν.
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

## Genesis 43:16

Greek: ἐποίησε δὲ ὁ ἄνθρωπος, καθὰ εἶπεν ᾿Ιωσήφ, καὶ εἰσήγαγε τοὺς ἀνθρώπους εἰς τὸν οἶκον ᾿Ιωσήφ.
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

## Genesis 43:17

Greek: ἰδόντες δὲ οἱ ἄνδρες ὅτι εἰσήχθησαν εἰς τὸν οἶκον τοῦ ᾿Ιωσήφ, εἶπαν· διὰ τὸ ἀργύριον τὸ ἀποστραφὲν ἐν τοῖς μαρσίπποις ἡμῶν τὴν ἀρχὴν ἡμεῖς εἰσαγόμεθα τοῦ συκοφαντῆσαι ἡμᾶς καὶ ἐπιθέσθαι ἡμῖν τοῦ λαβεῖν ἡμᾶς εἰς παῖδας καὶ τοὺς ὄνους ἡμῶν.
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

## Genesis 43:18

Greek: προσελθόντες δὲ πρὸς τὸν ἄνθρωπον τὸν ἐπὶ τοῦ οἴκου τοῦ ᾿Ιωσὴφ ἐλάλησαν αὐτῷ ἐν τῷ πυλῶνι τοῦ οἴκου
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

## Genesis 43:19

Greek: λέγοντες· δεόμεθα, κύριε, κατέβημεν τὴν ἀρχὴν πρίασθαι βρώματα·
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

## Genesis 43:20

Greek: ἐγένετο δὲ ἡνίκα ἤλθομεν εἰς τὸ καταλῦσαι καὶ ἠνοίξαμεν τοὺς μαρσίππους ἡμῶν, καὶ τόδε τὸ ἀργύριον ἑκάστου ἐν τῷ μαρσίππῳ αὐτοῦ· τὸ ἀργύριον ἡμῶν ἐν σταθμῷ ἀπεστρέψαμεν νῦν ἐν ταῖς χερσὶν ἡμῶν
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

## Genesis 43:21

Greek: καὶ ἀργύριον ἕτερον ἠνέγκαμεν μεθ᾿ ἑαυτῶν ἀγοράσαι βρώματα· οὐκ οἴδαμεν, τίς ἐνέβαλε τὸ ἀργύριον εἰς τοὺς μαρσίππους ἡμῶν.
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

## Genesis 43:22

Greek: εἶπε δὲ αὐτοῖς· ἵλεως ὑμῖν, μὴ φοβεῖσθε· ὁ Θεὸς ὑμῶν καὶ ὁ Θεὸς τῶν πατέρων ὑμῶν ἔδωκεν ὑμῖν θησαυροὺς ἐν τοῖς μαρσίπποις ὑμῶν, καὶ τὸ ἀργύριον ὑμῶν εὐδοκιμοῦν ἀπέχω. καὶ ἐξήγαγε πρὸς αὐτοὺς τὸν Συμεὼν
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

## Genesis 43:23

Greek: καὶ ἤνεγκεν ὕδωρ νίψαι τοὺς πόδας αὐτῶν καὶ ἔδωκε χορτάσματα τοῖς ὄνοις αὐτῶν.
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

## Genesis 43:24

Greek: ἡτοίμασαν δὲ τὰ δῶρα ἕως τοῦ ἐλθεῖν τὸν ᾿Ιωσὴφ μεσημβρίας· ἤκουσαν γὰρ ὅτι ἐκεῖ μέλλει ἀριστᾶν.
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

## Genesis 43:25

Greek: Εἰσῆλθε δὲ ᾿Ιωσὴφ εἰς τὴν οἰκίαν, καὶ προσήνεγκαν αὐτῷ τὰ δῶρα, ἃ εἶχον ἐν ταῖς χερσὶν αὐτῶν, εἰς τὸν οἶκον καὶ προσεκύνησαν αὐτῷ ἐπὶ πρόσωπον ἐπὶ τὴν γῆν.
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

## Genesis 43:26

Greek: ἠρώτησε δὲ αὐτούς, πῶς ἔχετε; καὶ εἶπεν αὐτοῖς· εἰ ὑγιαίνει ὁ πατὴρ ὑμῶν ὁ πρεσβύτης, ὃν εἴπατε; ἔτι ζῇ
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

## Genesis 43:27

Greek: οἱ δὲ εἶπαν· ὑγιαίνει ὁ παῖς σου ὁ πατὴρ ἡμῶν, ἔτι ζῇ· καὶ εἶπεν· εὐλογημένος ὁ ἄνθρωπος ἐκεῖνος τῷ Θεῷ. καὶ κύψαντες προσεκύνησαν αὐτῷ.
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

## Genesis 43:28

Greek: ἀναβλέψας δὲ τοῖς ὀφθαλμοῖς αὐτοῦ ᾿Ιωσὴφ εἶδε Βενιαμὶν τὸν ἀδελφὸν αὐτοῦ τὸν ὁμομήτριον καὶ εἶπεν· οὗτος ὁ ἀδελφὸς ὑμῶν ὁ νεώτερος, ὃν εἴπατε πρός με ἀγαγεῖν; καὶ εἶπεν· ὁ Θεὸς ἐλεήσαι σε τέκνον.
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

## Genesis 43:29

Greek: ἐταράχθη δὲ ᾿Ιωσήφ, συνεστρέφετο γὰρ τὰ ἔγκατα αὐτοῦ ἐπὶ τῷ ἀδελφῷ αὐτοῦ, καὶ ἐζήτει κλαῦσαι· εἰσελθὼν δὲ εἰς τὸ ταμεῖον ἔκλαυσεν ἐκεῖ.
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

## Genesis 43:30

Greek: καὶ νιψάμενος τὸ πρόσωπον ἐξελθὼν ἐνεκρατεύσατο καὶ εἶπε· παράθετε ἄρτους.
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

## Genesis 43:31

Greek: καὶ παρέθηκαν αὐτῷ μόνῳ καὶ αὐτοῖς καθ᾿ ἑαυτοὺς καὶ τοῖς Αἰγυπτίοις τοῖς συνδειπνοῦσι μετ᾿ αὐτοῦ καθ᾿ ἑαυτούς· οὐ γὰρ ἐδύναντο οἱ Αἰγύπτιοι συνεσθίειν μετὰ τῶν ῾Εβραίων ἄρτους, βδέλυγμα γάρ ἐστι τοῖς Αἰγυπτίοις.
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

## Genesis 43:32

Greek: ἐκάθισαν δὲ ἐναντίον αὐτοῦ, ὁ πρωτότοκος κατὰ τὰ πρεσβεῖα αὐτοῦ καὶ ὁ νεώτερος κατὰ τὴν νεότητα αὐτοῦ· ἐξίσταντο δὲ οἱ ἄνθρωποι ἕκαστος πρὸς τὸν ἀδελφὸν αὐτοῦ.
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

## Genesis 43:33

Greek: ᾖραν δὲ μερίδας παρ᾿ αὐτοῦ πρὸς αὐτούς· ἐμεγαλύνθη δὲ ἡ μερὶς Βενιαμὶν παρὰ τὰς μερίδας πάντων πενταπλασίως πρὸς τὰς ἐκείνων, ἔπιον δὲ καὶ ἐμεθύσθησαν μετ᾿ αὐτοῦ.
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

# Chapter 44

## Genesis 44:1

Greek: ΚΑΙ ἐνετείλατο ὁ ᾿Ιωσὴφ τῷ ὄντι ἐπὶ τῆς οἰκίας αὐτοῦ λέγων· πλήσατε τοὺς μαρσίππους τῶν ἀνθρώπων βρωμάτων, ὅσα ἐὰν δύνωνται ἆραι, καὶ ἐμβάλετε ἑκάστου τὸ ἀργύριον ἐπὶ τοῦ στόματος τοῦ μαρσίππου
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

## Genesis 44:2

Greek: καὶ τὸ κόνδυ μου τὸ ἀργυροῦν ἐμβάλετε εἰς τὸν μάρσιππον τοῦ νεωτέρου καὶ τὴν τιμὴν τοῦ σίτου αὐτοῦ. ἐγενήθη δὲ κατὰ τὸ ρῆμα ᾿Ιωσήφ, καθὼς εἶπε.
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

## Genesis 44:3

Greek: τὸ πρωΐ διέφαυσε, καὶ οἱ ἄνθρωποι ἀπεστάλησαν, αὐτοὶ καὶ οἱ ὄνοι αὐτῶν.
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

## Genesis 44:4

Greek: ἐξελθόντων δὲ αὐτῶν τὴν πόλιν, οὐκ ἀπέσχον μακράν, καὶ ᾿Ιωσὴφ εἶπε τῷ ἐπὶ τῆς οἰκίας αὐτοῦ· ἀναστὰς ἐπιδίωξον ὀπίσω τῶν ἀνθρώπων καὶ καταλήψῃ αὐτοὺς καὶ ἐρεῖς αὐτοῖς· τί ὅτι ἀνταπεδώκατε πονηρὰ ἀντὶ καλῶν; ἱνατί ἐκλέψατέ μου τὸ κόνδυ τὸ ἀργυροῦν
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

## Genesis 44:5

Greek: οὐ τοῦτό ἐστιν, ἐν ᾧ πίνει ὁ κύριός μου; αὐτὸς δὲ οἰωνισμῷ οἰωνίζεται ἐν αὐτῷ. πονηρὰ συντετελέκατε, ἃ πεποιήκατε.
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

## Genesis 44:6

Greek: εὑρὼν δὲ αὐτοὺς εἶπεν αὐτοῖς κατὰ τὰ ρήματα ταῦτα.
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

## Genesis 44:7

Greek: οἱ δὲ εἶπαν αὐτῷ· ἱνατί λαλεῖ ὁ κύριος κατὰ τὰ ρήματα ταῦτα; μὴ γένοιτο τοῖς παισί σου ποιῆσαι κατὰ τὸ ρῆμα τοῦτο.
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

## Genesis 44:8

Greek: εἰ τὸ μὲν ἀργύριον, ὁ εὕρομεν ἐν τοῖς μαρσίπποις ἡμῶν, ἀπεστρέψαμεν πρὸς σὲ ἐκ γῆς Χαναάν, πῶς ἂν κλέψαιμεν ἐκ τοῦ οἴκου τοῦ κυρίου σου ἀργύριον ἢ χρυσίον
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

## Genesis 44:9

Greek: παρ᾿ ᾧ ἂν εὕρῃς τὸ κόνδυ τῶν παίδων σου, ἀποθνησκέτω· καὶ ἡμεῖς δὲ ἐσόμεθα παῖδες τῷ κυρίῳ ἡμῶν.
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

## Genesis 44:10

Greek: ὁ δὲ εἶπε· καὶ νῦν ὡς λέγετε, οὕτως ἔσται· παρ᾿ ᾧ ἂν εὑρεθῇ τὸ κόνδυ, ἔσται μου παῖς, ὑμεῖς δὲ ἔσεσθε καθαροί.
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

## Genesis 44:11

Greek: καὶ ἔσπευσαν καὶ καθεῖλαν ἕκαστος τὸν μάρσιππον αὐτοῦ ἐπὶ τὴν γῆν καὶ ἤνοιξαν ἕκαστος τὸν μάρσιππον αὐτοῦ.
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

## Genesis 44:12

Greek: ἠρεύνησε δὲ ἀπὸ τοῦ πρεσβυτέρου ἀρξάμενος, ἕως ἦλθεν ἐπὶ τὸν νεώτερον, καὶ εὗρε τὸ κόνδυ ἐν τῷ μαρσίππῳ τοῦ Βενιαμίν.
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

## Genesis 44:13

Greek: καὶ διέρρηξαν τὰ ἱμάτια αὐτῶν καὶ ἐπέθηκαν ἕκαστος τὸν μάρσιππον αὐτοῦ ἐπί τὸν ὄνον αὐτοῦ, καὶ ἐπέστρεψαν εἰς τὴν πόλιν.
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

## Genesis 44:14

Greek: εἰσῆλθε δὲ ᾿Ιούδας καὶ οἱ ἀδελφοὶ αὐτοῦ πρὸς ᾿Ιωσήφ, ἔτι αὐτοῦ ὄντος ἐκεῖ, καὶ ἔπεσον ἐναντίον αὐτοῦ ἐπὶ τὴν γῆν.
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

## Genesis 44:15

Greek: εἶπε δὲ αὐτοῖς ᾿Ιωσήφ· τί τὸ πρᾶγμα τοῦτο ἐποιήσατε; οὐκ οἴδατε ὅτι οἰωνισμῷ οἰωνιεῖται ὁ ἄνθρωπος, οἷος ἐγώ
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

## Genesis 44:16

Greek: εἶπε δὲ ᾿Ιούδας· τί ἀντεροῦμεν τῷ κυρίῳ, ἢ τί λαλήσομεν, ἢ τί δικαιωθῶμεν; ὁ Θεὸς δὲ εὗρε τὴν ἀδικίαν τῶν παίδων σου. ἰδού ἐσμεν οἰκέται τῷ κυρίῳ ἡμῶν, καὶ ἡμεῖς καὶ παρ᾿ ᾧ εὑρέθη τὸ κόνδυ.
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

## Genesis 44:17

Greek: εἶπε δὲ ᾿Ιωσήφ· μή μοι γένοιτο ποιῆσαι τὸ ρῆμα τοῦτο· ὁ ἄνθρωπος, παρ᾿ ᾧ εὑρέθη τὸ κόνδυ αὐτὸς ἔσται μου παῖς. ὑμεῖς δὲ ἀνάβητε μετὰ σωτηρίας πρὸς τὸν πατέρα ὑμῶν.
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

## Genesis 44:18

Greek: ᾿Εγγίσας δὲ αὐτῷ ᾿Ιούδας εἶπε· δέομαι, κύριε· λαλησάτω ὁ παῖς σου ρῆμα ἐναντίον σου, καὶ μὴ θυμωθῇς τῷ παιδί σου, ὅτι σὺ εἶ μετὰ Φαραώ.
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

## Genesis 44:19

Greek: κύριε, σὺ ἠρώτησας τοὺς παῖδάς σου, λέγων· εἰ ἔχετε πατέρα ἢ ἀδελφόν
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

## Genesis 44:20

Greek: καὶ εἴπαμεν τῷ κυρίῳ· ἔστιν ἡμῖν πατὴρ πρεσβύτερος καὶ παιδίον γήρους νεώτερον αὐτῷ, καὶ ὁ ἀδελφὸς αὐτοῦ ἀπέθανεν, αὐτὸς δὲ μόνος ὑπελείφθη τῇ μητρὶ αὐτοῦ, ὁ δὲ πατὴρ αὐτὸν ἠγάπησεν.
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

## Genesis 44:21

Greek: εἶπας δὲ τοῖς παισί σου· καταγάγετε αὐτὸν πρός με, καὶ ἐπιμελοῦμαι αὐτοῦ.
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

## Genesis 44:22

Greek: καὶ εἴπαμεν τῷ κυρίῳ· οὐ δυνήσεται τὸ παιδίον καταλιπεῖν τὸν πατέρα αὐτοῦ· ἐὰν δὲ καταλίπῃ τὸν πατέρα, ἀποθανεῖται.
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

## Genesis 44:23

Greek: σὺ δὲ εἶπας τοῖς παισί σου· ἐὰν μὴ καταβῇ ὁ ἀδελφὸς ὑμῶν ὁ νεώτερος μεθ᾿ ὑμῶν, οὐ προσθήσεσθε ἰδεῖν τὸ πρόσωπόν μου.
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

## Genesis 44:24

Greek: ἐγένετο δὲ ἡνίκα ἀνέβημεν πρὸς τὸν παῖδά σου πατέρα ἡμῶν, ἀπηγγείλαμεν αὐτῷ τὰ ρήματα τοῦ κυρίου ἡμῶν.
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

## Genesis 44:25

Greek: εἶπε δὲ ὁ πατὴρ ἡμῶν· βαδίσατε πάλιν καὶ ἀγοράσατε ἡμῖν μικρὰ βρώματα.
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

## Genesis 44:26

Greek: ἡμεῖς δέ εἴπομεν· οὐ δυνησόμεθα καταβῆναι. ἀλλ᾿ εἰ μὲν ὁ ἀδελφὸς ἡμῶν ὁ νεώτερος καταβαίνει μεθ᾿ ἡμῶν, καταβησόμεθα· οὐ γὰρ δυνησόμεθα ἰδεῖν τὸ πρόσωπον τοῦ ἀνθρώπου, τοῦ ἀδελφοῦ ἡμῶν τοῦ νεωτέρου μὴ ὄντος μεθ᾿ ἡμῶν.
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

## Genesis 44:27

Greek: εἶπε δὲ ὁ παῖς σου, ὁ πατὴρ ἡμῶν πρὸς ἡμᾶς· ὑμεῖς γινώσκετε ὅτι δύο ἔτεκέ μοι ἡ γυνή·
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

## Genesis 44:28

Greek: καὶ ἐξῆλθεν ὁ εἷς ἀπ᾿ ἐμοῦ, καὶ εἴπατε ὅτι θηριόβρωτος γέγονε, καὶ οὐκ εἶδον αὐτὸν ἄχρι νῦν·
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

## Genesis 44:29

Greek: ἐὰν οὖν λάβητε καὶ τοῦτον ἐκ τοῦ προσώπου μου καὶ συμβῇ αὐτῷ μαλακία ἐν τῇ ὁδῷ, καὶ κατάξετέ μου τὸ γῆρας μετὰ λύπης εἰς ᾅδου.
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

## Genesis 44:30

Greek: νῦν οὖν ἐὰν εἰσπορεύωμαι πρὸς τὸν παῖδά σου, πατέρα δὲ ἡμῶν, καὶ τὸ παιδίον μὴ ᾖ μεθ᾿ ἡμῶν, ἡ δὲ ψυχὴ αὐτοῦ ἐκκρέμαται ἐκ τῆς τούτου ψυχῆς,
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

## Genesis 44:31

Greek: καὶ ἔσται ἐν τῷ ἰδεῖν αὐτὸν μὴ ὂν τὸ παιδίον μεθ᾿ ἡμῶν, τελευτήσει, καὶ κατάξουσιν οἱ παῖδές σου τὸ γῆρας τοῦ παιδός σου, πατρὸς δὲ ἡμῶν, μετὰ λύπης εἰς ᾅδου.
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

## Genesis 44:32

Greek: ὁ γὰρ παῖς σου παρὰ τοῦ πατρὸς ἐκδέδεκται τὸ παιδίον λέγων· ἐὰν μὴ ἀγάγω αὐτὸν πρὸς σὲ καὶ στήσω αὐτὸν ἐνώπιόν σου, ἡμαρτηκὼς ἔσομαι εἰς τὸν πατέρα πάσας τάς ἡμέρας.
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

## Genesis 44:33

Greek: νῦν οὖν παραμενῶ σοι παῖς ἀντὶ τοῦ παιδίου, οἰκέτης τοῦ κυρίου· τὸ δὲ παιδίον ἀναβήτω μετὰ τῶν ἀδελφῶν αὐτοῦ.
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

## Genesis 44:34

Greek: πῶς γὰρ ἀναβήσομαι πρὸς τὸν πατέρα, τοῦ παιδίου μὴ ὄντος μεθ᾿ ἡμῶν; ἵνα μὴ ἴδω τὰ κακά, ἃ εὑρήσει τὸν πατέρα μου.
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

# Chapter 45

## Genesis 45:1

Greek: ΚΑΙ οὐκ ἠδύνατο ᾿Ιωσὴφ ἀνέχεσθαι πάντων τῶν παρεστηκότων αὐτῷ, ἀλλ᾿ εἶπεν· ἐξαποστείλατε πάντας ἀπ᾿ ἐμοῦ. καὶ οὐ παρειστήκει οὐδεὶς τῷ ᾿Ιωσήφ, ἡνίκα ἀνεγνωρίζετο τοῖς ἀδελφοῖς αὐτοῦ.
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

## Genesis 45:2

Greek: καὶ ἀφῆκε φωνὴν μετὰ κλαυθμοῦ· ἤκουσαν δὲ πάντες οἱ Αἰγύπτιοι, καὶ ἀκουστὸν ἐγένετο εἰς τὸν οἶκον Φαραώ.
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

## Genesis 45:3

Greek: εἶπε δὲ ᾿Ιωσὴφ πρὸς τοὺς ἀδελφοὺς αὐτοῦ· ἐγώ εἰμι ᾿Ιωσήφ. ἔτι ὁ πατήρ μου ζῇ; καὶ οὐκ ἠδύναντο οἱ ἀδελφοὶ ἀποκριθῆναι αὐτῷ· ἐταράχθησαν γάρ.
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

## Genesis 45:4

Greek: εἶπε δὲ ᾿Ιωσὴφ πρὸς τούς ἀδελφοὺς αὐτοῦ· ἐγγίσατε πρός με, καὶ ἤγγισαν. καὶ εἶπεν· ἐγώ εἰμι ᾿Ιωσὴφ ὁ ἀδελφὸς ὑμῶν, ὃν ἀπέδοσθε εἰς Αἴγυπτον.
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

## Genesis 45:5

Greek: νῦν οὖν μὴ λυπεῖσθε, μηδὲ σκληρὸν ὑμῖν φανήτω, ὅτι ἀπέδοσθέ με ὧδε· εἰς γὰρ ζωὴν ἀπέστειλέ με ὁ Θεὸς ἔμπροσθεν ὑμῶν·
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

## Genesis 45:6

Greek: τοῦτο γὰρ δεύτερον ἔτος λιμὸς ἐπὶ τῆς γῆς, καὶ ἔτι λοιπὰ πέντε ἔτη, ἐν οἷς οὐκ ἔστιν ἀροτρίασις οὐδὲ ἄμητος·
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

## Genesis 45:7

Greek: ἀπέστειλε γάρ με ὁ Θεὸς ἔμπροσθεν ὑμῶν, ὑπολείπεσθαι ὑμῖν κατάλειμμα ἐπὶ τῆς γῆς καὶ ἐκθρέψαι ὑμῶν κατάλειψιν μεγάλην.
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

## Genesis 45:8

Greek: νῦν οὐχ ὑμεῖς με ἀπεστάλκατε ὧδε, ἀλλ᾿ ἢ ὁ Θεός, καὶ ἐποίησέ με ὡς πατέρα Φαραὼ καὶ κύριον παντὸς τοῦ οἴκου αὐτοῦ καὶ ἄρχοντα πάσης γῆς Αἰγύπτου.
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

## Genesis 45:9

Greek: σπεύσαντες οὖν ἀνάβητε πρὸς τὸν πατέρα μου καὶ εἴπατε αὐτῷ· τάδε λέγει ὁ υἱός σου ᾿Ιωσήφ· ἐποίησέ με ὁ Θεὸς κύριον πάσης γῆς Αἰγύπτου· κατάβηθι οὖν πρός με καὶ μὴ μείνῃς·
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

## Genesis 45:10

Greek: καὶ κατοικήσεις ἐν γῇ Γεσὲμ ᾿Αραβίας καὶ ἔσῃ ἐγγύς μου σὺ καὶ οἱ υἱοί σου καὶ οἱ υἱοὶ τῶν υἱῶν σου, τὰ πρόβατά σου καὶ οἱ βόες σου καὶ ὅσα σοι ἐστί,
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

## Genesis 45:11

Greek: καὶ ἐκθρέψω σε ἐκεῖ· ἔτι γὰρ πέντε ἔτη λιμός· ἵνα μὴ ἐκτριβῇς σὺ καὶ οἱ υἱοί σου καὶ πάντα τὰ ὑπάρχοντά σου.
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

## Genesis 45:12

Greek: ἰδοὺ οἱ ὀφθαλμοὶ ὑμῶν βλέπουσι καὶ οἱ ὀφθαλμοὶ Βενιαμὶν τοῦ ἀδελφοῦ μου, ὅτι τὸ στόμα μου τὸ λαλοῦν πρὸς ὑμᾶς.
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

## Genesis 45:13

Greek: ἀπαγγείλατε οὖν τῷ πατρί μου πᾶσαν τὴν δόξαν μου τὴν ἐν Αἰγύπτῳ καὶ ὅσα εἴδετε, καὶ ταχύναντες καταγάγετε τὸν πατέρα μου ὧδε.
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

## Genesis 45:14

Greek: καὶ ἐπιπεσὼν ἐπὶ τὸν τράχηλον Βενιαμὶν τοῦ ἀδελφοῦ αὐτοῦ ἔκλαυσεν ἐπ᾿ αὐτῷ, καὶ Βενιαμὶν ἔκλαυσεν ἐπὶ τῷ τραχήλῳ αὐτοῦ.
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

## Genesis 45:15

Greek: καὶ καταφιλήσας πάντας τοὺς ἀδελφοὺς αὐτοῦ ἔκλαυσεν ἐπ᾿ αὐτοῖς, καὶ μετὰ ταῦτα ἐλάλησαν οἱ ἀδελφοὶ αὐτοῦ πρὸς αὐτόν.
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

## Genesis 45:16

Greek: Καὶ διεβοήθη ἡ φωνὴ εἰς τὸν οἶκον Φαραὼ λέγοντες· ἥκασιν οἱ ἀδελφοὶ ᾿Ιωσήφ. ἐχάρη δὲ Φαραὼ καὶ ἡ θεραπεία αὐτοῦ.
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

## Genesis 45:17

Greek: εἶπε δὲ Φαραὼ πρὸς ᾿Ιωσήφ· εἰπὸν τοῖς ἀδελφοῖς σου, τοῦτο ποιήσατε· γεμίσατε τὰ φορεῖα ὑμῶν καὶ ἀπέλθετε εἰς γῆν Χαναὰν
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

## Genesis 45:18

Greek: καὶ ἀναλαβόντες τὸν πατέρα ὑμῶν καὶ τὰ ὑπάρχοντα ὑμῶν ἥκετε πρός με, καὶ δώσω ὑμῖν πάντων τῶν ἀγαθῶν Αἰγύπτου, καὶ φάγεσθε τὸν μυελὸν τῆς γῆς.
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

## Genesis 45:19

Greek: σὺ δὲ ἔντειλαι ταῦτα, λαβεῖν αὐτοῖς ἁμάξας ἐκ γῆς Αἰγύπτου τοῖς παιδίοις ὑμῶν καὶ ταῖς γυναιξὶν ὑμῶν. καὶ ἀναλαβόντες τὸν πατέρα ὑμῶν παραγίνεσθε·
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

## Genesis 45:20

Greek: καὶ μὴ φείσησθε τοῖς ὀφθαλμοῖς τῶν σκευῶν ὑμῶν, τὰ γὰρ πάντα ἀγαθὰ Αἰγύπτου ὑμῖν ἔσται.
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

## Genesis 45:21

Greek: ἐποίησαν δὲ οὕτως οἱ υἱοὶ ᾿Ισραήλ· ἔδωκε δὲ ᾿Ιωσὴφ αὐτοῖς ἁμάξας κατὰ τὰ εἰρημένα ὑπὸ Φαραὼ τοῦ βασιλέως καὶ ἔδωκεν αὐτοῖς ἐπισιτισμὸν εἰς τὴν ὁδόν,
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

## Genesis 45:22

Greek: καὶ πᾶσιν ἔδωκε δισσὰς στολάς, τῷ δὲ Βενιαμὶν ἔδωκε τριακοσίους χρυσοῦς καὶ πέντε ἐξαλλασσούσας στολάς,
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

## Genesis 45:23

Greek: καὶ τῷ πατρὶ αὐτοῦ ἀπέστειλε κατὰ τὰ αὐτὰ καὶ δέκα ὄνους αἴροντας ἀπὸ πάντων τῶν ἀγαθῶν Αἰγύπτου καὶ δέκα ἡμιόνους αἰρούσας ἄρτους τῷ πατρὶ αὐτοῦ εἰς ὁδόν.
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

## Genesis 45:24

Greek: ἐξαπέστειλε δὲ τοὺς ἀδελφοὺς αὐτοῦ καὶ ἐπορεύθησαν· καὶ εἶπεν αὐτοῖς· μὴ ὀργίζεσθε ἐν τῇ ὁδῷ.
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

## Genesis 45:25

Greek: Καὶ ἀνέβησαν ἐξ Αἰγύπτου καὶ ἦλθον εἰς γῆν Χαναὰν πρὸς ᾿Ιακὼβ τὸν πατέρα αὐτῶν,
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

## Genesis 45:26

Greek: καὶ ἀνήγγειλαν αὐτῷ λέγοντες· ὅτι ὁ υἱός σου ᾿Ιωσὴφ ζῇ, καὶ αὐτὸς ἄρχει πάσης γῆς Αἰγύπτου. καὶ ἐξέστη τῇ διανοίᾳ ᾿Ιακώβ· οὐ γὰρ ἐπίστευσεν αὐτοῖς.
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

## Genesis 45:27

Greek: ἐλάλησαν δὲ αὐτῷ πάντα τὰ ρηθέντα ὑπὸ ᾿Ιωσήφ, ὅσα εἶπεν αὐτοῖς. ἰδὼν δὲ τὰς ἁμάξας, ἃς ἀπέστειλεν ᾿Ιωσὴφ ὥστε ἀναλαβεῖν αὐτόν, ἀνεζωπύρησε τὸ πνεῦμα ᾿Ιακὼβ τοῦ πατρὸς αὐτῶν.
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

## Genesis 45:28

Greek: εἶπε δὲ ᾿Ισραήλ· μέγα μοί ἐστιν, εἰ ἔτι ᾿Ιωσὴφ ὁ υἱός μου ζῇ· πορευθεὶς ὄψομαι αὐτὸν πρὸ τοῦ ἀποθανεῖν με.
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

# Chapter 46

## Genesis 46:1

Greek: ΑΠΑΡΑΣ δὲ ᾿Ισραήλ, αὐτὸς καὶ πάντα τὰ αὐτοῦ, ἦλθεν ἐπὶ τὸ φρέαρ τοῦ ὅρκου καὶ ἔθυσε θυσίαν τῷ Θεῷ τοῦ πατρὸς αὐτοῦ ᾿Ισαάκ.
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

## Genesis 46:2

Greek: εἶπε δὲ ὁ Θεὸς τῷ ᾿Ισραὴλ ἐν ὁράματι τῆς νυκτός, εἰπών· ᾿Ιακώβ, ᾿Ιακώβ, ὁ δὲ εἶπε· τί ἐστιν
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

## Genesis 46:3

Greek: ὁ δὲ λέγει αὐτῷ· ἐγώ εἰμι ὁ Θεὸς τῶν πατέρων σου· μὴ φοβοῦ καταβῆναι εἰς Αἴγυπτον· εἰς γὰρ ἔθνος μέγα ποιήσω σε ἐκεῖ,
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

## Genesis 46:4

Greek: καὶ ἐγὼ καταβήσομαι μετὰ σοῦ εἰς Αἴγυπτον, καὶ ἐγὼ ἀναβιβάσω σε εἰς τέλος, καὶ ᾿Ιωσὴφ ἐπιβαλεῖ τὰς χεῖρας αὐτοῦ ἐπὶ τοὺς ὀφθαλμούς σου.
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

## Genesis 46:5

Greek: ἀνέστη δὲ ᾿Ιακὼβ ἀπὸ τοῦ φρέατος τοῦ ὅρκου, καὶ ἀνέλαβον οἱ υἱοὶ ᾿Ισραὴλ τὸν πατέρα αὐτῶν καὶ τὴν ἀποσκευὴν καὶ τὰς γυναῖκας αὐτῶν ἐπὶ τὰς ἁμάξας ἃς ἀπέστειλεν ᾿Ιωσὴφ ἆραι αὐτόν,
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

## Genesis 46:6

Greek: καὶ ἀναλαβόντες τὰ ὑπάρχοντα αὐτῶν καὶ πᾶσαν τὴν κτῆσιν, ἣν ἐκτήσαντο ἐν γῇ Χαναάν, εἰσῆλθον εἰς Αἴγυπτον, ᾿Ιακὼβ καὶ πᾶν τὸ σπέρμα αὐτοῦ μετ᾿ αὐτοῦ,
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

## Genesis 46:7

Greek: υἱοὶ καὶ υἱοὶ τῶν υἱῶν αὐτοῦ μετ᾿ αὐτοῦ, θυγατέρες καὶ θυγατέρες τῶν θυγατέρων αὐτοῦ· καὶ πᾶν τὸ σπέρμα αὐτοῦ ἤγαγεν εἰς Αἴγυπτον.
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

## Genesis 46:8

Greek: Ταῦτα δὲ τὰ ὀνόματα τῶν υἱῶν ᾿Ισραὴλ τῶν εἰσελθόντων εἰς Αἴγυπτον ἅμα ᾿Ιακὼβ τῷ πατρὶ αὐτῶν. ᾿Ιακὼβ καὶ υἱοὶ αὐτοῦ· πρωτότοκος ᾿Ιακὼβ Ρουβήν.
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

## Genesis 46:9

Greek: υἱοὶ δὲ Ρουβήν· ᾿Ενὼχ καὶ Φαλλούς, ᾿Ασρὼν καὶ Χαρμί.
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

## Genesis 46:10

Greek: υἱοὶ δὲ Συμεών· ᾿Ιεμουὴλ καὶ ᾿Ιαμεὶν καὶ ᾿Αὼδ καὶ ᾿Ιαχεὶν καὶ Σαὰρ καὶ Σαοὺλ υἱὸς τῆς Χανανίτιδος.
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

## Genesis 46:11

Greek: υἱοὶ δὲ Λευΐ· Γηρσών, Καὰθ καὶ Μεραρί.
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

## Genesis 46:12

Greek: υἱοὶ δὲ ᾿Ιούδα· ῍Ηρ καὶ Αὐνὰν καὶ Σηλὼμ καὶ Φαρὲς καὶ Ζαρά· ἀπέθανε δὲ ῍Ηρ καὶ Αὐνὰν ἐν γῇ Χαναάν· ἐγένοντο δὲ υἱοὶ Φαρές· ᾿Εσρὼν καὶ ᾿Ιεμουήλ.
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

## Genesis 46:13

Greek: υἱοὶ δὲ ᾿Ισσάχαρ· Θωλὰ καὶ Φουὰ καὶ ᾿Ιασοὺβ καὶ Ζαμβράμ.
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

## Genesis 46:14

Greek: υἱοὶ δὲ Ζαβουλών· Σερὲδ καὶ ᾿Αλλὼν καὶ ᾿Αχοήλ.
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

## Genesis 46:15

Greek: οὗτοι υἱοὶ Λείας, οὓς ἔτεκε τῷ ᾿Ιακὼβ ἐν Μεσοποταμίᾳ τῆς Συρίας, καὶ Δείναν τὴν θυγατέρα αὐτοῦ· πᾶσαι αἱ ψυχαί, υἱοὶ καὶ θυγατέρες, τριάκοντα τρεῖς.
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

## Genesis 46:16

Greek: υἱοὶ δὲ Γάδ· Σαφὼν καὶ ᾿Αγγὶς καὶ Σαυνὶς καὶ Θασοβὰν καὶ ᾿Αηδεὶς καὶ ᾿Αροηδεὶς καὶ ᾿Αρεηλείς.
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

## Genesis 46:17

Greek: υἱοὶ δὲ ᾿Ασήρ· ᾿Ιεμνά, ᾿Ιεσσουὰ καὶ ᾿Ιεοὺλ καὶ Βαριὰ καὶ Σάρα ἀδελφὴ αὐτῶν. υἱοὶ δὲ Βαριά· Χοβόρ καὶ Μελχιίλ.
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

## Genesis 46:18

Greek: οὗτοι υἱοὶ Ζελφᾶς, ἣν ἔδωκε Λάβαν Λείᾳ τῇ θυγατρὶ αὐτοῦ, ἣ ἔτεκε τούτους τῷ ᾿Ιακὼβ δεκαὲξ ψυχάς.
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

## Genesis 46:19

Greek: υἱοὶ δὲ Ραχὴλ γυναικὸς ᾿Ιακώβ· ᾿Ιωσὴφ καὶ Βενιαμίν.
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

## Genesis 46:20

Greek: ἐγένοντο δὲ υἱοὶ ᾿Ιωσὴφ ἐν γῇ Αἰγύπτου, οὓς ἔτεκεν αὐτῷ ᾿Ασεννὲθ θυγάτηρ Πετεφρῆ ἱερέως ῾Ηλιουπόλεως, τὸν Μανασσῆ καὶ τὸν ᾿Εφραΐμ. ἐγένοντο δὲ υἱοὶ Μανασσῆ, οὓς ἔτεκεν αὐτῷ ἡ παλλακὴ ἡ Σύρα, τὸν Μαχίρ· Μαχὶρ δὲ ἐγέννησε τὸν Γαλαάδ. υἱοὶ δὲ ᾿Εφραΐμ ἀδελφοῦ Μανασσῆ· Σουταλαὰμ καὶ Ταάμ. υἱοὶ δὲ Σουταλαάμ· ᾿Εδέμ.
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

## Genesis 46:21

Greek: υἱοὶ δὲ Βενιαμίν· Βαλὰ καὶ Χοβὼρ καὶ ᾿Ασβήλ· ἐγένοντο δὲ υἱοὶ Βαλά· Γηρὰ καὶ Νεομὰν καὶ ᾿Αγχὶς καὶ Ρὼς καὶ Μαμφὶμ καὶ ᾿Οφιμίν. Γηρὰ δὲ ἐγέννησε τὸν ᾿Αράδ.
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

## Genesis 46:22

Greek: οὗτοι υἱοὶ Ραχήλ, οὓς ἔτεκε τῷ ᾿Ιακώβ· πᾶσαι αἱ ψυχαὶ δεκαοκτώ.
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

## Genesis 46:23

Greek: υἱοὶ δὲ Δάν· ᾿Ασόμ.
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

## Genesis 46:24

Greek: καὶ υἱοὶ Νεφθαλείμ· ᾿Ασιὴλ καὶ Γωυνὶ καὶ ᾿Ισσάαρ καὶ Συλλήμ.
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

## Genesis 46:25

Greek: οὗτοι υἱοὶ Βαλᾶς, ἣν ἔδωκε Λάβαν Ραχὴλ τῇ θυγατρὶ αὐτοῦ, ἣ ἔτεκε τούτους τῷ ᾿Ιακώβ· πᾶσαι αἱ ψυχαὶ ἑπτά.
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

## Genesis 46:26

Greek: πᾶσαι δέ αἱ ψυχαὶ αἱ εἰσελθοῦσαι μετὰ ᾿Ιακὼβ εἰς Αἴγυπτον, οἱ ἐξελθόντες ἐκ τῶν μηρῶν αὐτοῦ, χωρὶς τῶν γυναικῶν υἱῶν ᾿Ιακώβ, πᾶσαι ψυχαὶ ἑξηκονταέξ.
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

## Genesis 46:27

Greek: υἱοὶ δὲ ᾿Ιωσὴφ οἱ γενόμενοι αὐτῷ ἐν γῇ Αἰγύπτῳ ψυχαὶ ἐννέα. πᾶσαι ψυχαὶ οἴκου ᾿Ιακὼβ αἱ εἰσελθοῦσαι μετὰ ᾿Ιακὼβ εἰς Αἴγυπτον ψυχαὶ ἑβδομηκονταπέντε.
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

## Genesis 46:28

Greek: Τὸν δὲ ᾿Ιούδαν ἀπέστειλεν ἔμπροσθεν αὐτοῦ πρὸς ᾿Ιωσὴφ συναντῆσαι αὐτῷ καθ᾿ ῾Ηρώων πόλιν, εἰς γῆν Ραμεσσῆ.
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

## Genesis 46:29

Greek: ζεύξας δὲ ᾿Ιωσὴφ τὰ ἅρματα αὐτοῦ ἀνέβη εἰς συνάντησιν ᾿Ισραὴλ τῷ πατρὶ αὐτοῦ καθ᾿ ῾Ηρώων πόλιν καὶ ὀφθεὶς αὐτῷ ἐπέπεσεν ἐπὶ τὸν τράχηλον αὐτοῦ καὶ ἔκλαυσε κλαυθμῷ πίονι.
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

## Genesis 46:30

Greek: καὶ εἶπεν ᾿Ισραὴλ πρὸς ᾿Ιωσήφ· ἀποθανοῦμαι ἀπὸ τοῦ νῦν, ἐπεὶ ἑώρακα τὸ πρόσωπόν σου· ἔτι γὰρ σὺ ζῇς.
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

## Genesis 46:31

Greek: εἶπε δὲ ᾿Ιωσὴφ πρὸς τοὺς ἀδελφοὺς αὐτοῦ· ἀναβὰς ἀπαγγελῶ τῷ Φαραὼ καὶ ἐρῶ αὐτῷ· οἱ ἀδελφοί μου καὶ ὁ οἶκος τοῦ πατρός μου, οἳ ἦσαν ἐν γῇ Χαναάν, ἥκασι πρός με·
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

## Genesis 46:32

Greek: οἱ δὲ ἄνδρες εἰσὶ ποιμένες· ἄνδρες γὰρ κτηνοτρόφοι ἦσαν· καὶ τὰ κτήνη καὶ τοὺς βόας καὶ πάντα τὰ αὐτῶν ἀγηόχασιν.
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

## Genesis 46:33

Greek: ἐὰν οὖν καλέσῃ ὑμᾶς Φαραὼ καὶ εἴπῃ ὑμῖν· τί τὸ ἔργον ὑμῶν ἐστίν
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

## Genesis 46:34

Greek: ἐρεῖτε· ἄνδρες κτηνοτρόφοι ἐσμὲν οἱ παῖδές σου ἐκ παιδὸς ἕως τοῦ νῦν, καὶ ἡμεῖς καὶ οἱ πατέρες ἡμῶν, ἵνα κατοικήσητε ἐν γῇ Γεσὲμ ᾿Αραβίας· βδέλυγμα γάρ ἐστιν Αἰγυπτίοις πᾶς ποιμὴν προβάτων.
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

# Chapter 47

## Genesis 47:1

Greek: ΕΛΘΩΝ δὲ ᾿Ιωσὴφ ἀπήγγειλε τῷ Φαραὼ λέγων· ὁ πατήρ μου καὶ οἱ ἀδελφοί μου καὶ τὰ κτήνη καὶ οἱ βόες αὐτῶν καὶ πάντα τὰ αὐτῶν ἦλθον ἐκ γῆς Χαναὰν καὶ ἰδού εἰσιν ἐν γῇ Γεσέμ.
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

## Genesis 47:2

Greek: ἀπὸ δὲ τῶν ἀδελφῶν αὐτοῦ παρέλαβε πέντε ἄνδρας καὶ ἔστησεν αὐτοὺς ἐναντίον Φαραώ.
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

## Genesis 47:3

Greek: καὶ εἶπε Φαραὼ τοῖς ἀδελφοῖς ᾿Ιωσήφ· τί τὸ ἔργον ὑμῶν; οἱ δὲ εἶπαν τῷ Φαραώ· ποιμένες προβάτων οἱ παῖδές σου, καὶ ἡμεῖς καὶ οἱ πατέρες ἡμῶν.
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

## Genesis 47:4

Greek: εἶπαν δὲ τῷ Φαραώ· παροικεῖν ἐν τῇ γῇ ἥκαμεν· οὐ γάρ ἐστι νομὴ τοῖς κτήνεσι τῶν παίδων σου, ἐνίσχυσε γὰρ ὁ λιμὸς ἐν γῇ Χαναάν· νῦν οὖν κατοικήσωμεν οἱ παῖδές σου ἐν γῇ Γεσέμ.
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

## Genesis 47:5

Greek: εἶπε δὲ Φαραὼ τῷ ᾿Ιωσήφ· κατοικείτωσαν ἐν γῇ Γεσέμ· εἰ δὲ ἐπίστῃ ὅτι εἰσὶν ἐν αὐτοῖς ἄνδρες δυνατοί, κατάστησον αὐτοὺς ἄρχοντας τῶν ἐμῶν κτηνῶν. ῏Ηλθον δὲ εἰς Αἴγυπτον πρὸς ᾿Ιωσὴφ ᾿Ιακὼβ καὶ οἱ υἱοὶ αὐτοῦ, καὶ ἤκουσε Φαραὼ βασιλεὺς Αἰγύπτου.
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

## Genesis 47:6

Greek: καὶ εἶπε Φαραὼ πρὸς ᾿Ιωσὴφ λέγων· ὁ πατήρ σου καὶ οἱ ἀδελφοί σου ἥκασι πρὸς σέ· ἰδοὺ ἡ γῆ Αἰγύπτου ἐναντίον σου ἐστίν· ἐν τῇ βελτίστῃ γῇ κατοίκισον τὸν πατέρα σου καὶ τοὺς ἀδελφούς σου.
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

## Genesis 47:7

Greek: εἰσήγαγε δὲ ᾿Ιωσὴφ ᾿Ιακὼβ τὸν πατέρα αὐτοῦ καὶ ἔστησεν αὐτὸν ἐναντίον Φαραώ, καὶ ηὐλόγησεν ᾿Ιακὼβ τὸν Φαραώ.
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

## Genesis 47:8

Greek: εἶπε δὲ Φαραὼ τῷ ᾿Ιακώβ· πόσα ἔτη ἡμερῶν τῆς ζωῆς σου
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

## Genesis 47:9

Greek: καὶ εἶπεν ᾿Ιακὼβ τῷ Φαραώ· αἱ ἡμέραι τῶν ἐτῶν τῆς ζωῆς μου, ἃς παροικῶ, ἑκατὸν τριάκοντα ἔτη· μικραὶ καὶ πονηραὶ γεγόνασιν αἱ ἡμέραι τῶν ἐτῶν τῆς ζωῆς μου, οὐκ ἀφίκοντο εἰς τὰς ἡμέρας τῶν ἐτῶν τῆς ζωῆς τῶν πατέρων μου, ἃς ἡμέρας παρῴκησαν.
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

## Genesis 47:10

Greek: καὶ εὐλογήσας ᾿Ιακὼβ τὸν Φαραὼ ἐξῆλθεν ἀπ᾿ αὐτοῦ.
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

## Genesis 47:11

Greek: καὶ κατῴκισεν ᾿Ιωσὴφ τὸν πατέρα αὐτοῦ καὶ τοὺς ἀδελφοὺς αὐτοῦ καὶ ἔδωκεν αὐτοῖς κατάσχεσιν ἐν γῇ Αἰγύπτῳ ἐν τῇ βελτίστῃ γῇ, ἐν γῇ Ραμεσσῆ, καθὰ προσέταξε Φαραώ.
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

## Genesis 47:12

Greek: καὶ ἐσιτομέτρει ᾿Ιωσὴφ τῷ πατρὶ αὐτοῦ καὶ τοῖς ἀδελφοῖς καὶ παντὶ τῷ οἴκῳ τοῦ πατρὸς αὐτοῦ σῖτον κατὰ σῶμα.
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

## Genesis 47:13

Greek: Σῖτος δὲ οὐκ ἦν ἐν πάσῃ τῇ γῇ· ἐνίσχυσε γὰρ ὁ λιμὸς σφόδρα. ἐξέλιπε δὲ ἡ γῆ Αἰγύπτου καὶ ἡ γῆ Χαναὰν ἀπὸ τοῦ λιμοῦ.
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

## Genesis 47:14

Greek: συνήγαγε δὲ ᾿Ιωσὴφ πᾶν τὸ ἀργύριον τὸ εὑρεθὲν ἐν γῇ Αἰγύπτου καὶ ἐν γῇ Χαναὰν τοῦ σίτου, οὗ ἠγόραζον, καὶ ἐσιτομέτρει αὐτοῖς, καὶ εἰσήνεγκεν ᾿Ιωσὴφ πᾶν τὸ ἀργύριον εἰς τὸν οἶκον Φαραώ.
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

## Genesis 47:15

Greek: καὶ ἐξέλιπε πᾶν τὸ ἀργύριον ἐκ γῆς Αἰγύπτου καὶ ἐκ γῆς Χαναάν. ἦλθον δὲ πάντες οἱ Αἰγύπτιοι πρὸς ᾿Ιωσήφ, λέγοντες· δὸς ἡμῖν ἄρτους, καὶ ἱνατί ἀποθνήσκομεν ἐναντίον σου; ἐκλέλοιπε γὰρ τὸ ἀργύριον ἡμῶν.
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

## Genesis 47:16

Greek: εἶπε δὲ αὐτοῖς ᾿Ιωσήφ· φέρετε τὰ κτήνη ὑμῶν, καὶ δώσω ὑμῖν ἄρτους ἀντὶ τῶν κτηνῶν ὑμῶν, εἰ ἐκλέλοιπε τὸ ἀργύριον ὑμῶν.
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

## Genesis 47:17

Greek: ἤγαγον δὲ τὰ κτήνη αὐτῶν πρὸς ᾿Ιωσήφ, καὶ ἔδωκεν αὐτοῖς ᾿Ιωσὴφ ἄρτους ἀντὶ τῶν ἵππων καὶ ἀντὶ τῶν προβάτων καὶ ἀντὶ τῶν βοῶν καὶ ἀντὶ τῶν ὄνων καὶ ἐξέθρεψεν αὐτοὺς ἐν ἄρτοις ἀντὶ πάντων τῶν κτηνῶν αὐτῶν ἐν τῷ ἐνιαυτῷ ἐκείνῳ.
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

## Genesis 47:18

Greek: ἐξῆλθε δὲ τὸ ἔτος ἐκεῖνο, καὶ ἦλθον πρὸς αὐτὸν ἐν τῷ ἔτει τῷ δευτέρῳ καὶ εἶπαν αὐτῷ· μή ποτε ἐκτριβῶμεν ἀπὸ τοῦ κυρίου ἡμῶν; εἰ γὰρ ἐκλέλοιπε τὸ ἀργύριον ἡμῶν καὶ τὰ ὑπάρχοντα καὶ τὰ κτήνη πρὸς σὲ τὸν κύριον, καὶ οὐχ ὑπολέλειπται ἡμῖν ἐναντίον τοῦ κυρίου ἡμῶν ἀλλ᾿ ἢ τὸ ἴδιον σῶμα καὶ ἡ γῆ ἡμῶν.
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

## Genesis 47:19

Greek: ἵνα οὖν μὴ ἀποθάνωμεν ἐναντίον σου καὶ ἡ γῆ ἐρημωθῇ, κτῆσαι ἡμᾶς καὶ τὴν γῆν ἡμῶν ἀντὶ ἄρτων, καὶ ἐσόμεθα ἡμεῖς καὶ ἡ γῆ ἡμῶν παῖδες τῷ Φαραώ· δὸς σπέρμα, ἵνα σπείρωμεν καὶ ζῶμεν καὶ μὴ ἀποθάνωμεν καὶ ἡ γῆ οὐκ ἐρημωθήσεται.
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

## Genesis 47:20

Greek: καὶ ἐκτήσατο ᾿Ιωσὴφ πᾶσαν τὴν γῆν τῶν Αἰγυπτίων τῷ Φαραώ· ἀπέδοντο γὰρ οἱ Αἰγύπτιοι τὴν γῆν αὐτῶν τῷ Φαραώ, ἐπεκράτησε γὰρ αὐτῶν ὁ λιμός· καὶ ἐγένετο ἡ γῇ τῷ Φαραώ,
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

## Genesis 47:21

Greek: καὶ τὸν λαὸν κατεδουλώσατο αὐτῷ εἰς παῖδας ἀπ᾿ ἄκρων ὁρίων Αἰγύπτου ἕως τῶν ἄκρων,
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

## Genesis 47:22

Greek: χωρὶς τῆς γῆς τῶν ἱερέων μόνον· οὐκ ἐκτήσατο ταύτην ᾿Ιωσήφ, ἐν δόσει γὰρ ἔδωκε δόμα τοῖς ἱερεῦσι Φαραώ, καὶ ἤσθιον τὴν δόσιν, ἣν ἔδωκεν αὐτοῖς Φαραώ· διὰ τοῦτο οὐκ ἀπέδοντο τὴν γῆν αὐτῶν.
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

## Genesis 47:23

Greek: εἶπε δὲ ᾿Ιωσὴφ πᾶσι τοῖς Αἰγυπτίοις· ἰδοὺ κέκτημαι ὑμᾶς καὶ τὴν γῆν ὑμῶν σήμερον τῷ Φαραώ· λάβετε ἑαυτοῖς σπέρμα καὶ σπείρατε τὴν γῆν,
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

## Genesis 47:24

Greek: καὶ ἔσται τὰ γεννήματα αὐτῆς καὶ δώσετε τὸ πέμπτον μέρος τῷ Φαραώ, τὰ δὲ τέσσαρα μέρη ἔσται ὑμῖν αὐτοῖς εἰς σπέρμα τῇ γῇ καὶ εἰς βρῶσιν ὑμῖν καὶ πᾶσι τοῖς ἐν τοῖς οἴκοις ὑμῶν.
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

## Genesis 47:25

Greek: καὶ εἶπαν· σέσωκας ἡμᾶς, εὕρομεν χάριν ἐναντίον τοῦ κυρίου ἡμῶν καὶ ἐσόμεθα παῖδες τῷ Φαραώ.
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

## Genesis 47:26

Greek: καὶ ἔθετο αὐτοῖς ᾿Ιωσὴφ εἰς πρόσταγμα ἕως τῆς ἡμέρας ταύτης, ἐπὶ γῆς Αἰγύπτου τῷ Φαραὼ ἀποπεμπτοῦν, χωρὶς τῆς γῆς τῶν ἱερέων μόνον· οὐκ ἦν τῷ Φαραώ.
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

## Genesis 47:27

Greek: Κατῴκησε δὲ ᾿Ισραὴλ ἐν γῇ Αἰγύπτῳ ἐπὶ γῆς Γεσὲμ καὶ ἐκληρονόμησαν ἐπ᾿ αὐτῆς καὶ ηὐξήθησαν καὶ ἐπληθύνθησαν σφόδρα.
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

## Genesis 47:28

Greek: ἐπέζησε δὲ ᾿Ιακὼβ ἐν γῇ Αἰγύπτῳ δεκαεπτὰ ἔτη· καὶ ἐγένοντο αἱ ἡμέραι ᾿Ιακὼβ ἐνιαυτῶν τῆς ζωῆς αὐτοῦ ἑκατὸν τεσσαρακονταεπτὰ ἔτη.
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

## Genesis 47:29

Greek: ἤγγισαν δὲ αἱ ἡμέραι ᾿Ισραὴλ τοῦ ἀποθανεῖν, καὶ ἐκάλεσε τὸν υἱὸν αὐτοῦ ᾿Ιωσὴφ καὶ εἶπεν αὐτῷ· εἰ εὕρηκα χάριν ἐναντίον σου, ὑπόθες τὴν χεῖρά σου ὑπὸ τὸν μηρόν μου καὶ ποιήσεις ἐπ᾿ ἐμὲ ἐλεημοσύνην καὶ ἀλήθειαν τοῦ μή με θάψαι ἐν Αἰγύπτῳ,
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

## Genesis 47:30

Greek: ἀλλὰ κοιμηθήσομαι μετὰ τῶν πατέρων μου, καὶ ἀρεῖς με ἐξ Αἰγύπτου καὶ θάψεις με ἐν τῷ τάφῳ αὐτῶν. ὁ δὲ εἶπεν· ἐγὼ ποιήσω κατὰ τὸ ρῆμά σου.
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

## Genesis 47:31

Greek: εἶπε δέ· ὄμοσόν μοι. καὶ ὤμοσεν αὐτῷ. καὶ προσεκύνησεν ᾿Ισραὴλ ἐπὶ τὸ ἄκρον τῆς ράβδου αὐτοῦ.
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

# Chapter 48

## Genesis 48:1

Greek: ΕΓΕΝΕΤΟ δὲ μετὰ τὰ ρήματα ταῦτα καὶ ἀπηγγέλη τῷ ᾿Ιωσήφ, ὅτι ὁ πατήρ σου ἐνοχλεῖται. καὶ ἀναλαβὼν τοὺς δύο υἱοὺς αὐτοῦ, τὸν Μανασσῆ καὶ τὸν ᾿Εφραΐμ, ἦλθε πρὸς ᾿Ιακώβ.
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

## Genesis 48:2

Greek: ἀπηγγέλη δὲ τῷ ᾿Ιακὼβ λέγοντες· ἰδοὺ ὁ υἱός σου ᾿Ιωσὴφ ἔρχεται πρὸς σέ. καὶ ἐνισχύσας ᾿Ισραὴλ ἐκάθησεν ἐπὶ τὴν κλίνην.
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

## Genesis 48:3

Greek: καὶ εἶπεν ᾿Ιακὼβ τῷ ᾿Ιωσήφ· ὁ Θεός μου ὤφθη μοι ἐν Λουζᾷ ἐν γῇ Χαναὰν καὶ εὐλόγησέ με
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

## Genesis 48:4

Greek: καὶ εἶπέ μοι· ἰδοὺ ἐγὼ αὐξανῶ σε καὶ πληθυνῶ σε καὶ ποιήσω σε εἰς συναγωγὰς ἐθνῶν καὶ δώσω σοι τὴν γῆν ταύτην καὶ τῷ σπέρματί σου μετὰ σὲ εἰς κατάσχεσιν αἰώνιον.
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

## Genesis 48:5

Greek: νῦν οὖν οἱ δύο υἱοί σου οἱ γενόμενοί σοι ἐν γῇ Αἰγύπτῳ πρὸ τοῦ με ἐλθεῖν πρὸς σὲ εἰς Αἴγυπτον, ἐμοί εἰσιν, ᾿Εφραΐμ καὶ Μανασσῆ, ὡς Ρουβὴν καὶ Συμεὼν ἔσονταί μοι·
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

## Genesis 48:6

Greek: τὰ δέ ἔκγονα, ἃ ἐὰν γεννήσῃς μετὰ ταῦτα, ἔσονται ἐπὶ τῷ ὀνόματι τῶν ἀδελφῶν αὐτῶν· κληθήσονται ἐπὶ τοῖς ἐκείνων κλήροις.
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

## Genesis 48:7

Greek: ἐγὼ δὲ ἡνίκα ἠρχόμην ἐκ Μεσοποταμίας τῆς Συρίας, ἀπέθανε Ραχὴλ ἡ μήτηρ σου ἐν γῇ Χαναάν, ἐγγίζοντός μου κατὰ τὸν ἱππόδρομον Χαβραθὰ τῆς γῆς τοῦ ἐλθεῖν ᾿Εφραθά, καὶ κατώρυξα αὐτὴν ἐν τῇ ὁδῷ τοῦ ἱπποδρόμου (αὕτη ἐστὶ Βηθλεέμ).
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

## Genesis 48:8

Greek: ἰδὼν δὲ ᾿Ισραὴλ τοὺς υἱοὺς ᾿Ιωσὴφ εἶπε· τίνες σοι οὗτοι
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

## Genesis 48:9

Greek: εἶπε δὲ ᾿Ιωσὴφ τῷ πατρὶ αὐτοῦ· υἱοί μου εἰσιν, οὓς ἔδωκέ μοι ὁ Θεὸς ἐνταῦθα. καὶ εἶπεν ᾿Ιακώβ· προσάγαγέ μοι αὐτούς, ἵνα εὐλογήσω αὐτούς.
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

## Genesis 48:10

Greek: οἱ ὀφθαλμοὶ δὲ ᾿Ισραὴλ ἐβαρυώπησαν ἀπὸ τοῦ γήρως, καὶ οὐκ ἠδύνατο βλέπειν· καὶ ἤγγισεν αὐτοὺς πρὸς αὐτόν, καὶ ἐφίλησεν αὐτοὺς καὶ περιέλαβεν αὐτούς.
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

## Genesis 48:11

Greek: καὶ εἶπεν ᾿Ισραὴλ πρὸς ᾿Ιωσήφ· ἰδοὺ τοῦ προσώπου σου οὐκ ἐστερήθην, καὶ ἰδοὺ ἔδειξέ μοι ὁ Θεὸς καὶ τὸ σπέρμα σου.
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

## Genesis 48:12

Greek: καὶ ἐξήγαγε αὐτοὺς ᾿Ιωσὴφ ἀπὸ τῶν γονάτων αὐτοῦ, καὶ προσεκύνησαν αὐτῷ ἐπὶ πρόσωπον ἐπὶ τῆς γῆς.
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

## Genesis 48:13

Greek: λαβὼν δὲ ᾿Ιωσὴφ τοὺς δύο υἱοὺς αὐτοῦ, τόν τε ᾿Εφραΐμ ἐν τῇ δεξιᾷ, ἐξ ἀριστερῶν δὲ ᾿Ισραήλ, τὸν δὲ Μανασσῆ ἐξ ἀριστερῶν, ἐκ δεξιῶν δὲ ᾿Ισραήλ, ἤγγισεν αὐτοὺς αὐτῷ.
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

## Genesis 48:14

Greek: ἐκτείνας δὲ ᾿Ισραὴλ τὴν χεῖρα τὴν δεξιὰν ἐπέβαλεν ἐπὶ τὴν κεφαλὴν ᾿Εφραΐμ, οὗτος δὲ ἦν ὁ νεώτερος, καὶ τὴν ἀριστερὰν ἐπὶ τὴν κεφαλὴν Μανασσῆ, ἐναλλὰξ τὰς χεῖρας.
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

## Genesis 48:15

Greek: καὶ εὐλόγησεν αὐτοὺς καὶ εἶπεν· ὁ Θεός, ᾧ εὐηρέστησαν οἱ πατέρες μου ἐνώπιον αὐτοῦ, ῾Αβραὰμ καὶ ᾿Ισαάκ, ὁ Θεὸς ὁ τρέφων με ἐκ νεότητος ἕως τῆς ἡμέρας ταύτης,
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

## Genesis 48:16

Greek: ὁ ἄγγελος ὁ ρυόμενός με ἐκ πάντων τῶν κακῶν εὐλογήσαι τὰ παιδία ταῦτα, καὶ ἐπικληθήσεται ἐν αὐτοῖς τὸ ὄνομά μου καὶ τὸ ὄνομα τῶν πατέρων μου ῾Αβραὰμ καὶ ᾿Ισαάκ, καὶ πληθυνθείησαν εἰς πλῆθος πολὺ ἐπὶ τῆς γῆς.
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

## Genesis 48:17

Greek: ἰδὼν δὲ ᾿Ιωσὴφ ὅτι ἐπέβαλεν ὁ πατὴρ αὐτοῦ τὴν χεῖρα τὴν δεξιὰν αὐτοῦ ἐπὶ τὴν κεφαλὴν ᾿Εφραΐμ, βαρὺ αὐτῷ κατεφάνη, καὶ ἀντελάβετο ᾿Ιωσὴφ τῆς χειρὸς τοῦ πατρὸς αὐτοῦ ἀφελεῖν αὐτὴν ἀπὸ τῆς κεφαλῆς ᾿Εφραΐμ ἐπὶ τὴν κεφαλὴν Μανασσῆ.
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

## Genesis 48:18

Greek: εἶπε δὲ ᾿Ιωσὴφ τῷ πατρὶ αὐτοῦ· οὐχ οὕτως, πάτερ, οὗτος γὰρ ὁ πρωτότοκος· ἐπίθες τὴν δεξιάν σου ἐπὶ τὴν κεφαλὴν αὐτοῦ.
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

## Genesis 48:19

Greek: καὶ οὐκ ἠθέλησεν, ἀλλὰ εἶπεν· οἶδα, τέκνον, οἶδα· καὶ οὗτος ἔσται εἰς λαόν, καὶ οὗτος ὑψωθήσεται· ἀλλὰ ὁ ἀδελφὸς αὐτοῦ ὁ νεώτερος μείζων αὐτοῦ ἔσται, καὶ τὸ σπέρμα αὐτοῦ ἔσται εἰς πλῆθος ἐθνῶν.
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

## Genesis 48:20

Greek: καὶ εὐλόγησεν αὐτοὺς ἐν τῇ ἡμέρᾳ ἐκείνῃ λέγων· ἐν ὑμῖν εὐλογηθήσεται ᾿Ισραὴλ λέγοντες· ποιήσαι σε ὁ Θεὸς ὡς ᾿Εφραΐμ καὶ ὡς Μανασσῆ. καὶ ἔθηκε τὸν ᾿Εφραΐμ ἔμπροσθεν τοῦ Μανασσῆ.
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

## Genesis 48:21

Greek: εἶπε δὲ ᾿Ισραὴλ τῷ ᾿Ιωσήφ· ἰδοὺ ἐγὼ ἀποθνήσκω, καὶ ἔσται ὁ Θεὸς μεθ᾿ ὑμῶν καὶ ἀποστρέψει ὑμᾶς εἰς τὴν γῆν τῶν πατέρων ὑμῶν·
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

## Genesis 48:22

Greek: ἐγὼ δὲ δίδωμί σοι Σίκιμα ἐξαίρετον ὑπὲρ τοὺς ἀδελφούς σου, ἣν ἔλαβον ἐκ χειρὸς ᾿Αμορραίων ἐν μαχαίρᾳ μου καὶ τόξῳ.
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

# Chapter 49

## Genesis 49:1

Greek: ΕΚΑΛΕΣΕ δὲ ᾿Ιακὼβ τοὺς υἱοὺς αὐτοῦ καὶ εἶπεν αὐτοῖς· συνάχθητε, ἵνα ἀναγγείλω ὑμῖν, τί ἀπαντήσει ὑμῖν ἐπ᾿ ἐσχάτων τῶν ἡμερῶν·
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

## Genesis 49:2

Greek: ἀθροίσθητε καὶ ἀκούσατέ μου, υἱοὶ ᾿Ιακώβ, ἀκούσατε ᾿Ισραὴλ τοῦ πατρὸς ὑμῶν.
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

## Genesis 49:3

Greek: Ρουβήν, πρωτότοκός μου, σὺ ἰσχύς μου καὶ ἀρχὴ τέκνων μου, σκληρὸς φέρεσθαι καὶ σκληρὸς αὐθάδης.
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

## Genesis 49:4

Greek: ἐξύβρισας ὡς ὕδωρ, μὴ ἐκζέσῃς· ἀνέβης γὰρ ἐπὶ τὴν κοίτην τοῦ πατρός σου· τότε ἐμίανας τὴν στρωμνήν, οὗ ἀνέβης.
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

## Genesis 49:5

Greek: Συμεὼν καὶ Λευΐ ἀδελφοί· συνετέλεσαν ἀδικίαν ἐξ αἱρέσεως αὐτῶν.
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

## Genesis 49:6

Greek: εἰς βουλὴν αὐτῶν μὴ ἔλθοι ἡ ψυχή μου, καὶ ἐπὶ τῇ συστάσει αὐτῶν μὴ ἐρείσαι τὰ ἥπατά μου, ὅτι ἐν τῷ θυμῷ αὐτῶν ἀπέκτειναν ἀνθρώπους καὶ ἐν τῇ ἐπιθυμίᾳ αὐτῶν ἐνευροκόπησαν ταῦρον.
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

## Genesis 49:7

Greek: ἐπικατάρατος ὁ θυμὸς αὐτῶν, ὅτι αὐθάδης, καὶ ἡ μῆνις αὐτῶν, ὅτι ἐσκληρύνθη· διαμεριῶ αὐτοὺς ἐν ᾿Ιακὼβ καὶ διασπερῶ αὐτοὺς ἐν ᾿Ισραήλ.
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

## Genesis 49:8

Greek: ᾿Ιούδα, σὲ αἰνέσαισαν οἱ ἀδελφοί σου· αἱ χεῖρές σου ἐπὶ νώτου τῶν ἐχθρῶν σου· προσκυνήσουσί σοι οἱ υἱοὶ τοῦ πατρός σου.
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

## Genesis 49:9

Greek: σκύμνος λέοντος ᾿Ιούδα· ἐκ βλαστοῦ, υἱέ μου, ἀνέβης· ἀναπεσὼν ἐκοιμήθης ὡς λέων καὶ ὡς σκύμνος· τίς ἐγερεῖ αὐτόν
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

## Genesis 49:10

Greek: οὐκ ἐκλείψει ἄρχων ἐξ ᾿Ιούδα καὶ ἡγούμενος ἐκ τῶν μηρῶν αὐτοῦ, ἕως ἐὰν ἔλθῃ τὰ ἀποκείμενα αὐτῷ, καὶ αὐτὸς προσδοκία ἐθνῶν.
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

## Genesis 49:11

Greek: δεσμεύων πρὸς ἄμπελον τὸν πῶλον αὐτοῦ καὶ τῇ ἕλικι τὸν πῶλον τῆς ὄνου αὐτοῦ· πλυνεῖ ἐν οἴνῳ τὴν στολὴν αὐτοῦ καὶ ἐν αἵματι σταφυλῆς τὴν περιβολὴν αὐτοῦ·
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

## Genesis 49:12

Greek: χαροποιοὶ οἱ ὀφθαλμοὶ αὐτοῦ ἀπὸ οἴνου, καὶ λευκοὶ οἱ ὀδόντες αὐτοῦ ἢ γάλα.
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

## Genesis 49:13

Greek: Ζαβουλὼν παράλιος κατοικήσει, καὶ αὐτὸς παρ᾿ ὅρμον πλοίων, καὶ παρατενεῖ ἕως Σιδῶνος.
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

## Genesis 49:14

Greek: ᾿Ισσάχαρ τὸ καλὸν ἐπεθύμησεν ἀναπαυόμενος ἀνὰ μέσον τῶν κλήρων·
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

## Genesis 49:15

Greek: καὶ ἰδὼν τὴν ἀνάπαυσιν ὅτι καλή, καὶ τὴν γῆν ὅτι πίων, ὑπέθηκε τὸν ὦμον αὐτοῦ εἰς τὸ πονεῖν καὶ ἐγενήθη ἀνὴρ γεωργός.
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

## Genesis 49:16

Greek: Δὰν κρινεῖ τὸ λαὸν αὐτοῦ, ὡσεὶ καὶ μία φυλὴ ἐν ᾿Ισραήλ.
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

## Genesis 49:17

Greek: καὶ γενηθήτω Δὰν ὄφις ἐφ᾿ ὁδοῦ, ἐγκαθήμενος ἐπὶ τρίβου, δάκνων πτέρναν ἵππου, καὶ πεσεῖται ὁ ἱππεὺς εἰς τὰ ὀπίσω,
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

## Genesis 49:18

Greek: τὴν σωτηρίαν περιμένων Κυρίου.
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

## Genesis 49:19

Greek: Γάδ, πειρατήριον πειρατεύσει αὐτόν, αὐτὸς δὲ πειρατεύσει αὐτὸν κατὰ πόδας.
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

## Genesis 49:20

Greek: ᾿Ασήρ, πίων αὐτοῦ ὁ ἄρτος, καὶ αὐτὸς δώσει τρυφὴν ἄρχουσι.
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

## Genesis 49:21

Greek: Νεφθαλεὶμ στέλεχος ἀνειμένον, ἐπιδιδοὺς ἐν τῷ γεννήματι κάλλος.
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

## Genesis 49:22

Greek: υἱὸς ηὐξημένος ᾿Ιωσήφ, υἱὸς ηὐξημένος μου ζηλωτός, υἱός μου νεώτατος· πρός με ἀνάστρεψον.
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

## Genesis 49:23

Greek: εἰς ὃν διαβουλευόμενοι ἐλοιδόρουν, καὶ ἐνεῖχον αὐτῷ κύριοι τοξευμάτων·
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

## Genesis 49:24

Greek: καὶ συνετρίβη μετὰ κράτους τὰ τόξα αὐτῶν, καὶ ἐξελύθη τὰ νεῦρα βραχιόνων χειρὸς αὐτῶν διά χεῖρα δυνάστου ᾿Ιακώβ, ἐκεῖθεν ὁ κατισχύσας ᾿Ισραήλ· παρὰ Θεοῦ τοῦ πατρός σου,
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

## Genesis 49:25

Greek: καὶ ἐβοήθησέ σοι ὁ Θεὸς ὁ ἐμὸς καὶ εὐλόγησέ σε εὐλογίαν οὐρανοῦ ἄνωθεν καὶ εὐλογίαν γῆς ἐχούσης πάντα· εἵνεκεν εὐλογίας μαστῶν καὶ μήτρας,
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

## Genesis 49:26

Greek: εὐλογίας πατρός σου καὶ μητρός σου· ὑπερίσχυσεν ὑπὲρ εὐλογίας ὀρέων μονίμων καὶ ἐπ᾿ εὐλογίαις θινῶν ἀενάων· ἔσονται ἐπὶ κεφαλὴν ᾿Ιωσὴφ καὶ ἐπὶ κορυφῆς ὧν ἡγήσατο ἀδελφῶν.
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

## Genesis 49:27

Greek: Βενιαμὶν λύκος ἅρπαξ· τὸ πρωϊνὸν ἔδεται ἔτι καὶ εἰς τὸ ἑσπέρας δίδωσι τροφήν.
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

## Genesis 49:28

Greek: Πάντες οὗτοι υἱοὶ ᾿Ιακὼβ δώδεκα, καὶ ταῦτα ἐλάλησεν αὐτοῖς ὁ πατὴρ αὐτῶν καὶ εὐλόγησεν αὐτούς, ἕκαστον κατὰ τὴν εὐλογίαν αὐτοῦ εὐλόγησεν αὐτούς.
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

## Genesis 49:29

Greek: καὶ εἶπεν αὐτοῖς· ἐγὼ προστίθεμαι πρὸς τὸν ἐμὸν λαόν· θάψατέ με μετὰ τῶν πατέρων μου ἐν τῷ σπηλαίῳ, ὅ ἐστιν ἐν τῷ ἀγρῷ ᾿Εφρὼν τοῦ Χετταίου,
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

## Genesis 49:30

Greek: ἐν τῷ σπηλαίῳ τῷ διπλῷ, τῷ ἀπέναντι Μαμβρῆ, ἐν γῇ Χαναάν, ὃ ἐκτήσατο ῾Αβραὰμ τὸ σπήλαιον παρὰ ᾿Εφρὼν τοῦ Χετταίου ἐν κτήσει μνημείου·
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

## Genesis 49:31

Greek: ἐκεῖ ἔθαψαν ῾Αβραὰμ καὶ Σάρραν τὴν γυναῖκα αὐτοῦ, ἐκεῖ ἔθαψαν ᾿Ισαὰκ καὶ Ρεβέκκαν τὴν γυναῖκα αὐτοῦ, ἐκεῖ ἔθαψα Λείαν
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

## Genesis 49:32

Greek: ἐν κτήσει τοῦ ἀγροῦ καὶ τοῦ σπηλαίου τοῦ ὄντος ἐν αὐτῷ παρὰ τῶν υἱῶν Χέτ.
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

## Genesis 49:33

Greek: καὶ κατέπαυσεν ᾿Ιακὼβ ἐπιτάσσων τοῖς υἱοῖς αὐτοῦ καὶ ἐξάρας τοὺς πόδας αὐτοῦ ἐπὶ τὴν κλίνην ἐξέλιπε καὶ προσετέθη πρὸς τὸν λαὸν αὐτοῦ.
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

# Chapter 50

## Genesis 50:1

Greek: ΚΑΙ ἐπιπεσὼν ᾿Ιωσὴφ ἐπὶ πρόσωπον τοῦ πατρὸς αὐτοῦ, ἔκλαυσεν αὐτὸν καὶ ἐφίλησεν αὐτόν.
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

## Genesis 50:2

Greek: καὶ προσέταξεν ᾿Ιωσὴφ τοῖς παισὶν αὐτοῦ τοῖς ἐνταφιασταῖς ἐνταφιάσαι τὸν πατέρα αὐτοῦ, καὶ ἐνεταφίασαν οἱ ἐνταφιασταὶ τὸν ᾿Ισραήλ.
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

## Genesis 50:3

Greek: καὶ ἐπλήρωσαν αὐτοῦ τεσσαράκοντα ἡμέρας· οὕτω γὰρ καταριθμοῦνται αἱ ἡμέραι τῆς ταφῆς. καὶ ἐπένθησεν αὐτὸν Αἴγυπτος ἑβδομήκοντα ἡμέρας.
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

## Genesis 50:4

Greek: ᾿Επεὶ δὲ παρῆλθον αἱ ἡμέραι τοῦ πένθους, ἐλάλησεν ᾿Ιωσὴφ πρὸς τοὺς δυνάστας Φαραὼ λέγων· εἰ εὗρον χάριν ἐναντίον ὑμῶν λαλήσατε περὶ ἐμοῦ εἰς τὰ ὦτα Φαραὼ λέγοντες·
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

## Genesis 50:5

Greek: ὁ πατήρ μου ὥρκισέ με λέγων· ἐν τῷ μνημείῳ ᾧ ὤρυξα ἐμαυτῷ ἐν γῇ Χαναάν, ἐκεῖ με θάψεις· νῦν οὖν ἀναβὰς θάψω τὸν πατέρα μου καὶ ἐπανελεύσομαι.
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

## Genesis 50:6

Greek: καὶ εἶπε Φαραὼ τῷ ᾿Ιωσήφ· ἀνάβηθι, θάψον τὸν πατέρα σου, καθάπερ ὥρκισέ σε.
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

## Genesis 50:7

Greek: καὶ ἀνέβη ᾿Ιωσὴφ θάψαι τὸν πατέρα αὐτοῦ, καὶ συνανέβησαν μετ᾿ αὐτοῦ πάντες οἱ παῖδες Φαραὼ καὶ οἱ πρεσβύτεροι τοῦ οἴκου αὐτοῦ καὶ πάντες οἱ πρεσβύτεροι τῆς γῆς Αἰγύπτου.
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

## Genesis 50:8

Greek: καὶ πᾶσα ἡ πανοικία ᾿Ιωσὴφ καὶ οἱ ἀδελφοὶ αὐτοῦ καὶ πᾶσα ἡ οἰκία ἡ πατρικὴ αὐτοῦ, καὶ τὴν συγγένειαν αὐτοῦ καὶ τὰ πρόβατα καὶ τοὺς βόας ὑπελίποντο ἐν γῇ Γεσέμ.
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

## Genesis 50:9

Greek: καὶ συνανέβησαν μετ᾿ αὐτοῦ καὶ ἅρματα καὶ ἱππεῖς, καὶ ἐγένετο ἡ παρεμβολὴ μεγάλη σφόδρα.
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

## Genesis 50:10

Greek: καὶ παρεγένοντο εἰς ἅλωνα ᾿Ατάδ, ὅ ἐστι πέραν τοῦ ᾿Ιορδάνου, καὶ ἐκόψαντο αὐτὸν κοπετὸν μέγαν καὶ ἰσχυρὸν σφόδρα· καὶ ἐποίησε τὸ πένθος τῷ πατρὶ αὐτοῦ ἑπτὰ ἡμέρας.
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

## Genesis 50:11

Greek: καὶ εἶδον οἱ κάτοικοι τῆς γῆς Χαναὰν τὸ πένθος ἐπὶ ἅλωνι ᾿Ατὰδ καὶ εἶπαν· πένθος μέγα τοῦτό ἐστι τοῖς Αἰγυπτίοις· διὰ τοῦτο ἐκάλεσε τὸ ὄνομα αὐτοῦ Πένθος Αἰγύπτου, ὅ ἐστι πέραν τοῦ ᾿Ιορδάνου.
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

## Genesis 50:12

Greek: καὶ ἐποίησαν αὐτῷ οὕτως οἱ υἱοὶ αὐτοῦ
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

## Genesis 50:13

Greek: καὶ ἀνέλαβον αὐτὸν οἱ υἱοὶ αὐτοῦ εἰς γῆν Χαναὰν καὶ ἔθαψαν αὐτὸν εἰς τὸ σπήλαιον τὸ διπλοῦν, ὃ ἐκτήσατο ῾Αβραὰμ τὸ σπήλαιον ἐν κτήσει μνημείου παρὰ ᾿Εφρὼν τοῦ Χετταίου, κατέναντι Μαμβρῆ.
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

## Genesis 50:14

Greek: καὶ ὑπέστρεψεν ᾿Ιωσὴφ εἰς Αἴγυπτον, αὐτὸς καὶ οἱ ἀδελφοὶ αὐτοῦ καὶ οἱ συναναβάντες θάψαι τὸν πατέρα αὐτοῦ.
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

## Genesis 50:15

Greek: ᾿Ιδόντες δὲ οἱ ἀδελφοὶ ᾿Ιωσὴφ ὅτι τέθνηκεν ὁ πατὴρ αὐτῶν, εἶπαν· μή ποτε μνησικακήσῃ ἡμῖν ᾿Ιωσὴφ καὶ ἀνταπόδομα ἀνταποδῷ ἡμῖν πάντα τὰ κακά, ἃ ἐνεδειξάμεθα εἰς αὐτόν.
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

## Genesis 50:16

Greek: καὶ παραγενόμενοι πρὸς ᾿Ιωσὴφ εἶπαν· ὁ πατήρ σου ὥρκισε πρὸ τοῦ τελευτῆσαι αὐτὸν λέγων·
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

## Genesis 50:17

Greek: οὕτως εἴπατε ᾿Ιωσήφ· ἄφες αὐτοῖς τὴν ἀδικίαν καί τὴν ἁμαρτίαν αὐτῶν, ὅτι πονηρά σοι ἐνεδείξαντο· καὶ νῦν δέξαι τὴν ἀδικίαν τῶν θεραπόντων τοῦ Θεοῦ τοῦ πατρός σου. καὶ ἔκλαυσεν ᾿Ιωσὴφ λαλούντων αὐτῶν πρὸς αὐτόν.
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

## Genesis 50:18

Greek: καὶ ἐλθόντες πρὸς αὐτὸν εἶπαν· οἵδε ἡμεῖς σοὶ ἱκέται.
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

## Genesis 50:19

Greek: καὶ εἶπεν αὐτοῖς ᾿Ιωσήφ· μὴ φοβεῖσθε, τοῦ γὰρ Θεοῦ εἰμι ἐγώ.
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

## Genesis 50:20

Greek: ὑμεῖς ἐβουλεύσασθε κατ᾿ ἐμοῦ εἰς πονηρά, ὁ δὲ Θεὸς ἐβουλεύσατο περὶ ἐμοῦ εἰς ἀγαθά, ὅπως ἂν γενηθῇ ὡς σήμερον καὶ τραφῇ λαὸς πολύς.
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

## Genesis 50:21

Greek: καὶ εἶπεν αὐτοῖς· μὴ φοβεῖσθε· ἐγὼ διαθρέψω ὑμᾶς καὶ τὰς οἰκίας ὑμῶν. καὶ παρεκάλεσεν αὐτοὺς καὶ ἐλάλησεν αὐτῶν εἰς τὴν καρδίαν.
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

## Genesis 50:22

Greek: Καὶ κατῴκησεν ᾿Ιωσὴφ ἐν Αἰγύπτῳ, αὐτὸς καὶ οἱ ἀδελφοὶ αὐτοῦ καὶ πᾶσα ἡ πανοικία τοῦ πατρὸς αὐτοῦ. καὶ ἔζησεν ᾿Ιωσὴφ ἔτη ἑκατὸν δέκα.
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

## Genesis 50:23

Greek: καὶ εἶδεν ᾿Ιωσὴφ ᾿Εφραΐμ παιδία ἕως τρίτης γενεᾶς, καὶ οἱ υἱοὶ Μαχεὶρ τοῦ υἱοῦ Μανασσῆ ἐτέχθησαν ἐπὶ μηρῶν ᾿Ιωσήφ.
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

## Genesis 50:24

Greek: καὶ εἶπεν ᾿Ιωσήφ τοῖς ἀδελφοῖς αὐτοῦ λέγων· ἐγὼ ἀποθνήσκω· ἐπισκοπῇ δὲ ἐπισκέψεται ὁ Θεὸς ὑμᾶς καὶ ἀνάξει ὑμᾶς ἐκ τῆς γῆς ταύτης εἰς τὴν γῆν, ἣν ὤμοσεν ὁ Θεὸς τοῖς πατράσιν ἡμῶν, ῾Αβραάμ, ᾿Ισαὰκ καὶ ᾿Ιακώβ.
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

## Genesis 50:25

Greek: καὶ ὥρκισεν ᾿Ιωσὴφ τοὺς υἱοὺς ᾿Ισραὴλ λέγων· ἐν τῇ ἐπισκοπῇ, ᾗ ἐπισκέψηται ὁ Θεὸς ὑμᾶς, καὶ συνανοίσετε τὰ ὀστᾶ μου ἐντεῦθεν μεθ᾿ ὑμῶν.
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

## Genesis 50:26

Greek: καὶ ἐτελεύτησεν ᾿Ιωσὴφ ἐτῶν ἑκατὸν δέκα· καὶ ἔθαψαν αὐτὸν καὶ ἔθηκαν ἐν τῇ σορῷ ἐν Αἰγύπτῳ.
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
