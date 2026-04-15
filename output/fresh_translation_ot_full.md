# Fresh Translation Worksheet

Scope: Genesis-Malachi (39 books)

Display: drafted verses only

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

# Genesis

## Chapter 1

### Genesis 1:1

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

### Genesis 1:2

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

### Genesis 1:3

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

### Genesis 1:4

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

### Genesis 1:5

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

### Genesis 1:6

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

### Genesis 1:7

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

### Genesis 1:8

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

### Genesis 1:9

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

### Genesis 1:10

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

### Genesis 1:11

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

### Genesis 1:12

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

### Genesis 1:13

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

### Genesis 1:14

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

### Genesis 1:15

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

### Genesis 1:16

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

### Genesis 1:17

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

### Genesis 1:18

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

### Genesis 1:19

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

### Genesis 1:20

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

### Genesis 1:21

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

### Genesis 1:22

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

### Genesis 1:23

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

### Genesis 1:24

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

### Genesis 1:25

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

### Genesis 1:26

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

### Genesis 1:27

Greek: καὶ ἐποίησεν ὁ Θεὸς τὸν ἄνθρωπον, κατ᾿ εἰκόνα Θεοῦ ἐποίησεν αὐτόν, ἄρσεν καὶ θῆλυ ἐποίησεν αὐτούς.
Transliteration: kai epoiesen ho Theos ton anthropon, kat eikona Theou epoiesen auton, arsen kai thely epoiesen autous.
Literal gloss: And God made the human, according to image of God he made him, male and female he made them.
Syntax notes: Singular and plural forms alternate within the verse. The line is tightly patterned and poetic.
Draft translation: And God made humankind; according to God's image he made humankind. Male and female he made them.

Decision rows:
- greek_phrase: ἄρσεν καὶ θῆλυ | lemma: ἄρσην | θῆλυ | morphology: paired predicates | chosen_rendering: male and female | alternate_renderings: man and woman | rationale: Closer to the paired sex terms used in the Greek line. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Singular-plural rendering may shift after close review | decision: Keep humankind wording provisional | status: pending

### Genesis 1:28

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

### Genesis 1:29

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

### Genesis 1:30

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

### Genesis 1:31

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

## Chapter 2

### Genesis 2:1

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

### Genesis 2:2

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

### Genesis 2:3

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

### Genesis 2:4

Greek: Αὕτη ἡ βίβλος γενέσεως οὐρανοῦ καὶ γῆς, ὅτε ἐγένετο· ᾗ ἡμέρᾳ ἐποίησε Κύριος ὁ Θεὸς τὸν οὐρανὸν καὶ τὴν γῆν
Transliteration: Haute he biblos geneseōs ouranou kai gēs, hote egeneto; hē hēmera epoiese Kyrios ho Theos ton ouranon kai tēn gēn
Literal gloss: This the book of genesis of heaven and earth, when it came to be; in the day Lord God made heaven and earth.
Syntax notes: The heading formula marks a new section. βίβλος γενέσεως may signal account, record, or origin-narrative.
Draft translation: This is the book of the origin of Heaven and Earth, when they came to be, on the day the Lord God made Heaven and Earth.

Decision rows:
- greek_phrase: βίβλος γενέσεως | lemma: βίβλος | γένεσις | morphology: nominative heading phrase | chosen_rendering: the book of the origin | alternate_renderings: the book of the genesis; the record of origins; the account of becoming | rationale: Origin reads more naturally in English while still preserving the heading's source-language force. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: book of the origin | footnote_text: Greek literally uses genesis-language here. This draft now reads 'origin' in the main line for smoother English, while preserving the heading's source-language force in the note. | source_basis: lexical + discourse | status: drafted

Logos research:
- greek_phrase: βίβλος γενέσεως | lemma: βίβλος | γένεσις | resource: LLS:FBLXXLEX | usage_note: Check how this heading formula functions in Greek Genesis and whether genesis here leans toward origins, generations, or becoming. | next_action: verify book of genesis wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Heading wording may shift with lexical review | decision: Keep book of genesis wording provisional | status: pending

### Genesis 2:5

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

### Genesis 2:6

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

### Genesis 2:7

Greek: καὶ ἔπλασεν ὁ Θεὸς τὸν ἄνθρωπον, χοῦν ἀπὸ τῆς γῆς, καὶ ἐνεφύσησεν εἰς τὸ πρόσωπον αὐτοῦ πνοὴν ζωῆς, καὶ ἐγένετο ὁ ἄνθρωπος εἰς ψυχὴν ζῶσαν.
Transliteration: kai eplasen ho Theos ton anthrōpon, choun apo tēs gēs, kai enephysēsen eis to prosōpon autou pnoēn zōēs, kai egeneto ho anthrōpos eis psychēn zōsan.
Literal gloss: And God formed the human, dust from the earth, and breathed into his face breath of life, and the human became into a living being.
Syntax notes: πλάσσω gives shaping imagery. πνοὴ ζωῆς and ψυχὴ ζῶσα tightly link breath and animate life.
Draft translation: And God formed the human from dust of the earth and breathed into his face the breath of life, and the human became a living being.

Decision rows:
- greek_phrase: ἔπλασεν | lemma: πλάσσω | morphology: aorist active indicative 3 singular | chosen_rendering: formed | alternate_renderings: fashioned; shaped | rationale: Formed keeps the hands-on shaping image clear. | status: drafted
- greek_phrase: πνοὴν ζωῆς | lemma: πνοή | ζωή | morphology: accusative noun phrase | chosen_rendering: the breath of life | alternate_renderings: breath of living; life-breath | rationale: Classic phrase but still direct and concrete. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: formed | footnote_text: The Greek verb suggests shaping or molding, not merely making in a general sense. The line narrows creation imagery from broad making to formed craftsmanship. | source_basis: lexical + imagery | status: drafted

Logos research:
- greek_phrase: πλάσσω / πνοὴ ζωῆς | lemma: πλάσσω | πνοή | ζωή | resource: LLS:FBLXXLEX | usage_note: Check shaping imagery and relation between breath-of-life phrase here and similar Greek expressions elsewhere. | next_action: verify formed breath wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Formation and breath wording may shift after lexical review | decision: Keep formed wording provisional | status: pending

### Genesis 2:8

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

### Genesis 2:9

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

### Genesis 2:10

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

### Genesis 2:11

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

### Genesis 2:12

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

### Genesis 2:13

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

### Genesis 2:14

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

### Genesis 2:15

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

### Genesis 2:16

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

### Genesis 2:17

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

### Genesis 2:18

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

### Genesis 2:19

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

### Genesis 2:20

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

### Genesis 2:21

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

### Genesis 2:22

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

### Genesis 2:23

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

### Genesis 2:24

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

### Genesis 2:25

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

## Chapter 3

### Genesis 3:1

Greek: Οδὲ ὄφις ἦν φρονιμώτατος πάντων τῶν θηρίων τῶν ἐπὶ τῆς γῆς, ὧν ἐποίησε Κύριος ὁ Θεός. καὶ εἶπεν ὁ ὄφις τῇ γυναικί· τί ὅτι εἶπεν ὁ Θεός, οὐ μὴ φάγητε ἀπὸ παντὸς ξύλου τοῦ παραδείσου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now the serpent was the most shrewd of all the beasts on the earth that the Lord God had made. And the serpent said to the woman, 'Why is it that God said, "You shall not eat from every tree of the garden"?'

Decision rows:
- greek_phrase: φρονιμώτατος | lemma: φρόνιμος | morphology: superlative adjective | chosen_rendering: the most shrewd | alternate_renderings: the most prudent; the most crafty | rationale: Shrewd keeps the intelligence sense while fitting the serpent's adversarial role better than prudent. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: most shrewd | footnote_text: Greek phronimos can suggest practical intelligence, shrewdness, or craft. This draft uses 'shrewd' because it keeps the serpent's mental sharpness in view without sounding approving. | source_basis: lexical | status: drafted

Logos research:
- greek_phrase: φρονιμώτατος | lemma: φρόνιμος | resource: LLS:FBLXXLEX | usage_note: Check whether phronimos here leans prudent, shrewd, intelligent, or crafty in comparable Greek usage. | next_action: verify prudent wording

Variant notes:
- witnesses: Rahlfs-Hanhart / Göttingen / Logos morphology | reading: No apparatus decision entered yet | translation_impact: Serpent adjective wording may shift with lexical review | decision: Keep prudent wording provisional | status: pending

### Genesis 3:2

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

### Genesis 3:3

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

### Genesis 3:4

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

### Genesis 3:5

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

### Genesis 3:6

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

### Genesis 3:7

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

### Genesis 3:8

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

### Genesis 3:9

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

### Genesis 3:10

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

### Genesis 3:11

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

### Genesis 3:12

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

### Genesis 3:13

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

### Genesis 3:14

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

### Genesis 3:15

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

### Genesis 3:16

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

### Genesis 3:17

Greek: τῷ δὲ ᾿Αδὰμ εἶπεν· ὅτι ἤκουσας τῆς φωνῆς τῆς γυναικός σου καὶ ἔφαγες ἀπὸ τοῦ ξύλου, οὗ ἐνετειλάμην σοι τούτου μόνου μὴ φαγεῖν, ἀπ᾿ αὐτοῦ ἔφαγες, ἐπικατάρατος ἡ γῆ ἐν τοῖς ἔργοις σου· ἐν λύπαις φαγῇ αὐτὴν πάσας τὰς ἡμέρας τῆς ζωῆς σου·
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And to Adam he said that because you listened to the voice of your wife and ate from the tree from which alone he commanded you not to eat, the ground is cursed in your labors. In pains you will eat from it all the days of your life.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Genesis 3:18

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

### Genesis 3:19

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

### Genesis 3:20

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

### Genesis 3:21

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

### Genesis 3:22

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

### Genesis 3:23

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

### Genesis 3:24

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

# Exodus

## Chapter 1

### Exodus 1:1

Greek: ταυτα τα ονοματα των υιων ισραηλ των εισπεπορευμενων εις αιγυπτον αμα ιακωβ τω πατρι αυτων εκαστος πανοικια αυτων εισηλθοσαν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: These are the names of the sons of Israel who entered into Egypt with Jacob their father; each entered with his whole household.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:2

Greek: ρουβην συμεων λευι ιουδας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Reuben, Simeon, Levi, Judah,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:3

Greek: ισσαχαρ ζαβουλων και βενιαμιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Issachar, Zebulun, and Benjamin,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:4

Greek: δαν και νεφθαλι γαδ και ασηρ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Dan and Naphtali, Gad and Asher.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:5

Greek: ιωσηφ δε ην εν αιγυπτω ησαν δε πασαι ψυχαι εξ ιακωβ πεντε και εβδομηκοντα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But Joseph was in Egypt. And all the persons from Jacob were seventy-five.

Decision rows:
- greek_phrase: πᾶσαι ψυχαί | lemma: ψυχή | morphology: nominative plural noun | chosen_rendering: persons | alternate_renderings: souls; lives | rationale: Persons fits headcount language here without forcing later metaphysical weight onto the census line. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: persons | footnote_text: Greek says 'souls,' but here the phrase functions as a headcount of living persons descending from Jacob. This draft avoids importing later metaphysical overtones into a census line. | source_basis: lexical + context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:6

Greek: ετελευτησεν δε ιωσηφ και παντες οι αδελφοι αυτου και πασα η γενεα εκεινη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Joseph died, and all his brothers, and all that generation.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:7

Greek: οι δε υιοι ισραηλ ηυξηθησαν και επληθυνθησαν και χυδαιοι εγενοντο και κατισχυον σφοδρα σφοδρα επληθυνεν δε η γη αυτους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But the sons of Israel increased and multiplied and became numerous, and they grew exceedingly, exceedingly strong; and the land multiplied them.

Decision rows:
- greek_phrase: χυδαῖοι ἐγένοντο | lemma: χυδαῖος | γίνομαι | morphology: aorist middle indicative 3 plural | chosen_rendering: became numerous | alternate_renderings: became common; became many | rationale: Numerous keeps the population-growth sense without the pejorative drift common can carry in English. | status: drafted
- greek_phrase: ἐπληθύνεν δὲ ἡ γῆ αὐτούς | lemma: γῆ | πληθύνω | morphology: aorist active indicative 3 singular + accusative | chosen_rendering: the land multiplied them | alternate_renderings: the land filled up with them; the land was full of them | rationale: Keeps the startling active Greek while leaving room for a smoother contextual rendering later if needed. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: the land multiplied them | footnote_text: The final clause is strikingly active in Greek, literally 'the land multiplied them.' This draft keeps that rough force for now rather than smoothing it away too quickly. | source_basis: syntax + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:8

Greek: ανεστη δε βασιλευς ετερος επ' αιγυπτον ος ουκ ηδει τον ιωσηφ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then another king arose over Egypt who did not know Joseph.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:9

Greek: ειπεν δε τω εθνει αυτου ιδου το γενος των υιων ισραηλ μεγα πληθος και ισχυει υπερ ημας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said to his people, 'Look, the race of the sons of Israel is a great multitude and stronger than we are.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:10

Greek: δευτε ουν κατασοφισωμεθα αυτους μηποτε πληθυνθη και ηνικα αν συμβη ημιν πολεμος προστεθησονται και ουτοι προς τους υπεναντιους και εκπολεμησαντες ημας εξελευσονται εκ της γης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Come then, let us deal shrewdly with them, lest they multiply, and whenever war comes upon us, they too will be added to our enemies and fight against us and depart from the land.

Decision rows:
- greek_phrase: κατασοφισώμεθα αὐτούς | lemma: κατασοφίζομαι | morphology: aorist middle subjunctive 1 plural | chosen_rendering: deal shrewdly with them | alternate_renderings: deal craftily with them; outwit them | rationale: Preserves the wisdom-root while making the hostile policy unmistakable. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: deal shrewdly with them | footnote_text: Greek uses a wisdom-root verb here. Pharaoh proposes not open argument but calculated cunning against Israel. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:11

Greek: και επεστησεν αυτοις επιστατας των εργων ινα κακωσωσιν αυτους εν τοις εργοις και ωκοδομησαν πολεις οχυρας τω φαραω την τε πιθωμ και ραμεσση και ων η εστιν ηλιου πολις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: So he set over them overseers of labor to afflict them in their labors; and they built fortified cities for Pharaoh: Pithom, Ramesses, and On, which is Heliopolis.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:12

Greek: καθοτι δε αυτους εταπεινουν τοσουτω πλειους εγινοντο και ισχυον σφοδρα σφοδρα και εβδελυσσοντο οι αιγυπτιοι απο των υιων ισραηλ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But as much as they humbled them, so much more they became many and grew exceedingly, exceedingly strong, and the Egyptians were disgusted by the sons of Israel.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:13

Greek: και κατεδυναστευον οι αιγυπτιοι τους υιους ισραηλ βια
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Egyptians oppressed the sons of Israel by force.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:14

Greek: και κατωδυνων αυτων την ζωην εν τοις εργοις τοις σκληροις τω πηλω και τη πλινθεια και πασι τοις εργοις τοις εν τοις πεδιοις κατα παντα τα εργα ων κατεδουλουντο αυτους μετα βιας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they made their life bitter with hard labors, in clay and in brick-making and in every field-labor, according to all the work by which they enslaved them with violence.

Decision rows:
- greek_phrase: κατωδύνων αὐτῶν τὴν ζωήν | lemma: κατωδυνάω | ζωή | morphology: present active participle + accusative | chosen_rendering: made their life bitter | alternate_renderings: embittered their life | rationale: Keeps the bittering image explicit and concrete. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: made their life bitter | footnote_text: The Greek phrase frames oppression as embittering life itself, not merely assigning hard tasks. This draft keeps that emotional and bodily force. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:15

Greek: και ειπεν ο βασιλευς των αιγυπτιων ταις μαιαις των εβραιων τη μια αυτων η ονομα σεπφωρα και το ονομα της δευτερας φουα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the king of Egypt spoke to the Hebrew midwives; the name of the one was Sepphora, and the name of the second, Phua.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:16

Greek: και ειπεν οταν μαιουσθε τας εβραιας και ωσιν προς τω τικτειν εαν μεν αρσεν η αποκτεινατε αυτο εαν δε θηλυ περιποιεισθε αυτο
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said, 'When you serve as midwives for the Hebrew women and they are at the time of giving birth, if it is a male, kill it; but if a female, keep it alive.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:17

Greek: εφοβηθησαν δε αι μαιαι τον θεον και ουκ εποιησαν καθοτι συνεταξεν αυταις ο βασιλευς αιγυπτου και εζωογονουν τα αρσενα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But the midwives feared God and did not do as the king of Egypt ordered them, and they kept the male children alive.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:18

Greek: εκαλεσεν δε ο βασιλευς αιγυπτου τας μαιας και ειπεν αυταις τι οτι εποιησατε το πραγμα τουτο και εζωογονειτε τα αρσενα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: So the king of Egypt called the midwives and said to them, 'Why have you done this thing and kept the male children alive?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:19

Greek: ειπαν δε αι μαιαι τω φαραω ουχ ως γυναικες αιγυπτου αι εβραιαι τικτουσιν γαρ πριν η εισελθειν προς αυτας τας μαιας και ετικτον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the midwives said to Pharaoh, 'The Hebrew women are not like the women of Egypt, for before the midwives can go in to them, they give birth.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:20

Greek: ευ δε εποιει ο θεος ταις μαιαις και επληθυνεν ο λαος και ισχυεν σφοδρα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God did well to the midwives, and the people multiplied and grew very strong.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:21

Greek: επειδη εφοβουντο αι μαιαι τον θεον εποιησαν εαυταις οικιας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And because the midwives feared God, they established households for themselves.

Decision rows:
- greek_phrase: ἐποίησαν ἑαυταῖς οἰκίας | lemma: ποιέω | οἰκία | morphology: aorist active indicative 3 plural + accusative | chosen_rendering: established households for themselves | alternate_renderings: made houses for themselves; established families for themselves | rationale: Reads as household-establishment rather than literal construction while preserving the reflexive Greek. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: established households for themselves | footnote_text: Greek literally speaks of making houses for themselves. In context the line likely points to settled households or families, not merely buildings. | source_basis: lexical + context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 1:22

Greek: συνεταξεν δε φαραω παντι τω λαω αυτου λεγων παν αρσεν ο εαν τεχθη τοις εβραιοις εις τον ποταμον ριψατε και παν θηλυ ζωογονειτε αυτο
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Pharaoh charged all his people, saying, 'Every male that is born to the Hebrews, throw it into the river; but keep every female alive.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 2

### Exodus 2:1

Greek: ην δε τις εκ της φυλης λευι ος ελαβεν των θυγατερων λευι και εσχεν αυτην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now a certain man from the tribe of Levi went and took one of the daughters of Levi.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:2

Greek: και εν γαστρι ελαβεν και ετεκεν αρσεν ιδοντες δε αυτο αστειον εσκεπασαν αυτο μηνας τρεις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And she conceived and bore a male child, and seeing that he was beautiful, they hid him three months.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:3

Greek: επει δε ουκ ηδυναντο αυτο ετι κρυπτειν ελαβεν αυτω η μητηρ αυτου θιβιν και κατεχρισεν αυτην ασφαλτοπισση και ενεβαλεν το παιδιον εις αυτην και εθηκεν αυτην εις το ελος παρα τον ποταμον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But when they could no longer hide him, his mother took for him a basket and coated it with bitumen and pitch, and she put the child into it and set it in the reeds by the river.

Decision rows:
- greek_phrase: θίβιν | lemma: θίβις | morphology: accusative singular noun | chosen_rendering: basket | alternate_renderings: ark; box | rationale: Basket reads naturally while leaving room to note the unusual loanword rather than forcing a heavier symbolic term into the line. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: basket | footnote_text: Greek uses an uncommon loanword here, not the ordinary word for boat or chest. 'Basket' keeps the small, portable object in view while leaving room to explore intertextual echoes later. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:4

Greek: και κατεσκοπευεν η αδελφη αυτου μακροθεν μαθειν τι το αποβησομενον αυτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And his sister kept watch from a distance to learn what would happen to him.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:5

Greek: κατεβη δε η θυγατηρ φαραω λουσασθαι επι τον ποταμον και αι αβραι αυτης παρεπορευοντο παρα τον ποταμον και ιδουσα την θιβιν εν τω ελει αποστειλασα την αβραν ανειλατο αυτην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Pharaoh's daughter came down to bathe at the river, and her young women were walking along beside the river. Seeing the basket in the reeds, she sent her maid and took it.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:6

Greek: ανοιξασα δε ορα παιδιον κλαιον εν τη θιβει και εφεισατο αυτου η θυγατηρ φαραω και εφη απο των παιδιων των εβραιων τουτο
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And when she opened it, she sees a child crying in the basket. And Pharaoh's daughter had compassion on him and said, 'This is one of the Hebrews' children.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:7

Greek: και ειπεν η αδελφη αυτου τη θυγατρι φαραω θελεις καλεσω σοι γυναικα τροφευουσαν εκ των εβραιων και θηλασει σοι το παιδιον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then his sister said to Pharaoh's daughter, 'Do you want me to call a nursing woman from the Hebrews, and she will nurse the child for you?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:8

Greek: η δε ειπεν αυτη η θυγατηρ φαραω πορευου ελθουσα δε η νεανις εκαλεσεν την μητερα του παιδιου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh's daughter said to her, 'Go.' So the young woman went and called the child's mother.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:9

Greek: ειπεν δε προς αυτην η θυγατηρ φαραω διατηρησον μοι το παιδιον τουτο και θηλασον μοι αυτο εγω δε δωσω σοι τον μισθον ελαβεν δε η γυνη το παιδιον και εθηλαζεν αυτο
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh's daughter said to her, 'Keep this child for me and nurse him for me, and I will give you your wages.' So the woman took the child and nursed him.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:10

Greek: αδρυνθεντος δε του παιδιου εισηγαγεν αυτο προς την θυγατερα φαραω και εγενηθη αυτη εις υιον επωνομασεν δε το ονομα αυτου μωυσην λεγουσα εκ του υδατος αυτον ανειλομην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And when the child grew strong, she brought him to Pharaoh's daughter, and he became her son. And she called his name Moses, saying, 'For I drew him out of the water.'

Decision rows:
- greek_phrase: ἐκ τοῦ ὕδατος αὐτὸν ἀνειλόμην | lemma: ὕδωρ | ἀναιρέω | morphology: prepositional phrase + verb | chosen_rendering: I drew him out of the water | alternate_renderings: I took him up out of the water | rationale: Keeps Pharaoh's daughter's naming explanation explicit and concrete. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: drew him out of the water | footnote_text: The naming explanation turns on drawing up from water. This draft keeps the etymological play explicit even if the exact wordplay does not map neatly into English. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:11

Greek: εγενετο δε εν ταις ημεραις ταις πολλαις εκειναις μεγας γενομενος μωυσης εξηλθεν προς τους αδελφους αυτου τους υιους ισραηλ κατανοησας δε τον πονον αυτων ορα ανθρωπον αιγυπτιον τυπτοντα τινα εβραιον των εαυτου αδελφων των υιων ισραηλ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now in those many days, when Moses had grown great, he went out to his brothers, the sons of Israel. And observing their hardship, he saw an Egyptian striking a certain Hebrew, one of his own brothers from the sons of Israel.

Decision rows:
- greek_phrase: μέγας γενόμενος | lemma: μέγας | γίνομαι | morphology: aorist middle participle | chosen_rendering: grown great | alternate_renderings: grown up; become great | rationale: Grown great keeps both age and stature in view, not merely physical adulthood. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: grown great | footnote_text: Greek may suggest more than simple aging. This draft keeps both maturity and emerging stature in view. | source_basis: lexical + context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:12

Greek: περιβλεψαμενος δε ωδε και ωδε ουχ ορα ουδενα και παταξας τον αιγυπτιον εκρυψεν αυτον εν τη αμμω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And looking this way and that way, he saw no one, so he struck the Egyptian and hid him in the sand.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:13

Greek: εξελθων δε τη ημερα τη δευτερα ορα δυο ανδρας εβραιους διαπληκτιζομενους και λεγει τω αδικουντι δια τι συ τυπτεις τον πλησιον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And going out on the second day, he saw two Hebrew men fighting, and he says to the one doing wrong, 'Why are you striking your neighbor?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:14

Greek: ο δε ειπεν τις σε κατεστησεν αρχοντα και δικαστην εφ' ημων μη ανελειν με συ θελεις ον τροπον ανειλες εχθες τον αιγυπτιον εφοβηθη δε μωυσης και ειπεν ει ουτως εμφανες γεγονεν το ρημα τουτο
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But he said, 'Who made you ruler and judge over us? Do you mean to kill me as you killed the Egyptian yesterday?' Then Moses became afraid and said, 'So then this matter has become known.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:15

Greek: ηκουσεν δε φαραω το ρημα τουτο και εζητει ανελειν μωυσην ανεχωρησεν δε μωυσης απο προσωπου φαραω και ωκησεν εν γη μαδιαμ ελθων δε εις γην μαδιαμ εκαθισεν επι του φρεατος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh heard this matter and sought to kill Moses. But Moses withdrew from Pharaoh's face and lived in the land of Midian. And when he came into the land of Midian, he sat by the well.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:16

Greek: τω δε ιερει μαδιαμ ησαν επτα θυγατερες ποιμαινουσαι τα προβατα του πατρος αυτων ιοθορ παραγενομεναι δε ηντλουν εως επλησαν τας δεξαμενας ποτισαι τα προβατα του πατρος αυτων ιοθορ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now the priest of Midian had seven daughters, tending the flock of their father Jothor. And when they came, they drew water until they filled the troughs to water the flock of their father Jothor.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:17

Greek: παραγενομενοι δε οι ποιμενες εξεβαλον αυτας αναστας δε μωυσης ερρυσατο αυτας και ηντλησεν αυταις και εποτισεν τα προβατα αυτων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But when the shepherds came, they drove them away. Then Moses rose and rescued them, and he drew water for them and watered their flock.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:18

Greek: παρεγενοντο δε προς ραγουηλ τον πατερα αυτων ο δε ειπεν αυταις τι οτι εταχυνατε του παραγενεσθαι σημερον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then they came to Raguel their father, and he said to them, 'Why have you come so quickly today?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:19

Greek: αι δε ειπαν ανθρωπος αιγυπτιος ερρυσατο ημας απο των ποιμενων και ηντλησεν ημιν και εποτισεν τα προβατα ημων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they said, 'An Egyptian man rescued us from the shepherds, and he also drew water for us and watered our flock.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:20

Greek: ο δε ειπεν ταις θυγατρασιν αυτου και που εστι και ινα τι ουτως καταλελοιπατε τον ανθρωπον καλεσατε ουν αυτον οπως φαγη αρτον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said to his daughters, 'Then where is he? And why have you left the man like this? Call him then, so that he may eat bread.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:21

Greek: κατωκισθη δε μωυσης παρα τω ανθρωπω και εξεδοτο σεπφωραν την θυγατερα αυτου μωυση γυναικα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses settled with the man, and he gave Sepphora his daughter to Moses as a wife.

Decision rows:
- greek_phrase: κατῳκίσθη...παρὰ τῷ ἀνθρώπῳ | lemma: κατοικίζω | morphology: aorist passive indicative 3 singular | chosen_rendering: settled with the man | alternate_renderings: was established with the man; dwelt with the man | rationale: Settled keeps the durable placement sense without sounding overly formal. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: settled with the man | footnote_text: The Greek verb points to settled placement or establishment. This draft emphasizes Moses taking up durable residence rather than merely staying overnight. | source_basis: lexical + context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:22

Greek: εν γαστρι δε λαβουσα η γυνη ετεκεν υιον και επωνομασεν μωυσης το ονομα αυτου γηρσαμ λεγων οτι παροικος ειμι εν γη αλλοτρια
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the woman conceived and bore a son, and Moses called his name Gersam, saying, 'Because I am a sojourner in a foreign land.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:23

Greek: μετα δε τας ημερας τας πολλας εκεινας ετελευτησεν ο βασιλευς αιγυπτου και κατεστεναξαν οι υιοι ισραηλ απο των εργων και ανεβοησαν και ανεβη η βοη αυτων προς τον θεον απο των εργων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now after those many days the king of Egypt died, and the sons of Israel groaned from the labors and cried out, and their cry went up to God from the labors.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:24

Greek: και εισηκουσεν ο θεος τον στεναγμον αυτων και εμνησθη ο θεος της διαθηκης αυτου της προς αβρααμ και ισαακ και ιακωβ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God heard their groaning, and God remembered his covenant with Abraham and Isaac and Jacob.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 2:25

Greek: και επειδεν ο θεος τους υιους ισραηλ και εγνωσθη αυτοις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God saw the sons of Israel and was made known to them.

Decision rows:
- greek_phrase: ἐγνώσθη αὐτοῖς | lemma: γινώσκω | morphology: aorist passive indicative 3 singular | chosen_rendering: was made known to them | alternate_renderings: was known to them; took notice of them | rationale: The passive Greek is striking and may imply manifestation rather than only inward awareness. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: was made known to them | footnote_text: Greek does not simply say that God knew them; it uses a passive form, literally 'was made known to them.' This draft keeps that striking formulation visible for review. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 3

### Exodus 3:1

Greek: και μωυσης ην ποιμαινων τα προβατα ιοθορ του γαμβρου αυτου του ιερεως μαδιαμ και ηγαγεν τα προβατα υπο την ερημον και ηλθεν εις το ορος χωρηβ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now Moses was shepherding the flock of Jothor his father-in-law, the priest of Midian, and he led the flock into the wilderness and came to Mount Horeb.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:2

Greek: ωφθη δε αυτω αγγελος κυριου εν φλογι πυρος εκ του βατου και ορα οτι ο βατος καιεται πυρι ο δε βατος ου κατεκαιετο
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then a messenger of the Lord appeared to him in a flame of fire out of the bush. And he sees that the bush burns with fire, but the bush was not being consumed.

Decision rows:
- greek_phrase: ἄγγελος κυρίου | lemma: ἄγγελος | κύριος | morphology: nominative noun phrase | chosen_rendering: messenger of the Lord | alternate_renderings: angel of the Lord | rationale: Messenger keeps the base sense of angelos in view and leaves later angelological conclusions open. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: messenger of the Lord | footnote_text: Greek angelos can mean messenger as well as angel. This draft keeps the more basic term visible at the start of the scene. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:3

Greek: ειπεν δε μωυσης παρελθων οψομαι το οραμα το μεγα τουτο τι οτι ου κατακαιεται ο βατος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said, 'I will go over now and see this great sight, why the bush is not burned up.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:4

Greek: ως δε ειδεν κυριος οτι προσαγει ιδειν εκαλεσεν αυτον κυριος εκ του βατου λεγων μωυση μωυση ο δε ειπεν τι εστιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And when the Lord saw that he was coming near to see, the Lord called to him from the bush, saying, 'Moses, Moses.' And he said, 'What is it?'

Decision rows:
- greek_phrase: τί ἐστιν | lemma: τίς | εἰμί | morphology: interrogative phrase | chosen_rendering: what is it | alternate_renderings: here I am | rationale: The Greek here reads like a question rather than the usual readiness formula, so the draft preserves the strangeness. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: what is it | footnote_text: Many readers expect a response like 'Here I am,' but the Greek here reads as a question. This draft preserves that sharper and more surprising wording. | source_basis: syntax + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:5

Greek: και ειπεν μη εγγισης ωδε λυσαι το υποδημα εκ των ποδων σου ο γαρ τοπος εν ω συ εστηκας γη αγια εστιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said, 'Do not come near here. Untie your sandals from your feet, for the place on which you stand is holy ground.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:6

Greek: και ειπεν αυτω εγω ειμι ο θεος του πατρος σου θεος αβρααμ και θεος ισαακ και θεος ιακωβ απεστρεψεν δε μωυσης το προσωπον αυτου ευλαβειτο γαρ κατεμβλεψαι ενωπιον του θεου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said to him, 'I am the God of your father, the God of Abraham and the God of Isaac and the God of Jacob.' Then Moses turned away his face, for he feared to gaze before God.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:7

Greek: ειπεν δε κυριος προς μωυσην ιδων ειδον την κακωσιν του λαου μου του εν αιγυπτω και της κραυγης αυτων ακηκοα απο των εργοδιωκτων οιδα γαρ την οδυνην αυτων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, 'I have surely seen the affliction of my people in Egypt, and I have heard their cry from the taskmasters, for I know their pain.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:8

Greek: και κατεβην εξελεσθαι αυτους εκ χειρος αιγυπτιων και εξαγαγειν αυτους εκ της γης εκεινης και εισαγαγειν αυτους εις γην αγαθην και πολλην εις γην ρεουσαν γαλα και μελι εις τον τοπον των χαναναιων και χετταιων και αμορραιων και φερεζαιων και γεργεσαιων και ευαιων και ιεβουσαιων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I have come down to take them out from the hand of the Egyptians and to bring them out of that land into a good and broad land, into a land flowing with milk and honey, into the place of the Canaanites and Hittites and Amorites and Perizzites and Girgashites and Hivites and Jebusites.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:9

Greek: και νυν ιδου κραυγη των υιων ισραηλ ηκει προς με καγω εωρακα τον θλιμμον ον οι αιγυπτιοι θλιβουσιν αυτους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And now, look, the cry of the sons of Israel has come to me, and I have seen the oppression with which the Egyptians oppress them.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:10

Greek: και νυν δευρο αποστειλω σε προς φαραω βασιλεα αιγυπτου και εξαξεις τον λαον μου τους υιους ισραηλ εκ γης αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And now come, I will send you to Pharaoh king of Egypt, and you shall bring out my people, the sons of Israel, from the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:11

Greek: και ειπεν μωυσης προς τον θεον τις ειμι οτι πορευσομαι προς φαραω βασιλεα αιγυπτου και οτι εξαξω τους υιους ισραηλ εκ γης αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said to God, 'Who am I, that I should go to Pharaoh king of Egypt and that I should bring out the sons of Israel from the land of Egypt?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:12

Greek: ειπεν δε ο θεος μωυσει λεγων οτι εσομαι μετα σου και τουτο σοι το σημειον οτι εγω σε εξαποστελλω εν τω εξαγαγειν σε τον λαον μου εξ αιγυπτου και λατρευσετε τω θεω εν τω ορει τουτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God said to Moses, saying, 'For I will be with you, and this will be the sign for you that I am the one sending you: when you bring out my people from Egypt, you will serve God on this mountain.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:13

Greek: και ειπεν μωυσης προς τον θεον ιδου εγω ελευσομαι προς τους υιους ισραηλ και ερω προς αυτους ο θεος των πατερων υμων απεσταλκεν με προς υμας ερωτησουσιν με τι ονομα αυτω τι ερω προς αυτους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said to God, 'Look, I will come to the sons of Israel and say to them, The God of your fathers has sent me to you. And they will ask me, What is his name? What should I say to them?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:14

Greek: και ειπεν ο θεος προς μωυσην εγω ειμι ο ων και ειπεν ουτως ερεις τοις υιοις ισραηλ ο ων απεσταλκεν με προς υμας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God said to Moses, 'I am the One who is.' And he said, 'Thus shall you say to the sons of Israel: The One who is has sent me to you.'

Decision rows:
- greek_phrase: ἐγώ εἰμι ὁ ὤν | lemma: εἰμί | ὁ ὤν | morphology: pronoun + verb + articular participle | chosen_rendering: I am the One who is | alternate_renderings: I am the Existing One; I am Being | rationale: Keeps the participial force visible without flattening it into an abstract title alone. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: The One who is | footnote_text: Greek uses the article with the participle of 'to be,' yielding something like 'the one who is.' This draft keeps the phrase concrete and verbal rather than replacing it with a purely abstract label. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:15

Greek: και ειπεν ο θεος παλιν προς μωυσην ουτως ερεις τοις υιοις ισραηλ κυριος ο θεος των πατερων υμων θεος αβρααμ και θεος ισαακ και θεος ιακωβ απεσταλκεν με προς υμας τουτο μου εστιν ονομα αιωνιον και μνημοσυνον γενεων γενεαις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God said again to Moses, 'Thus shall you say to the sons of Israel: The Lord, the God of your fathers, the God of Abraham and the God of Isaac and the God of Jacob, has sent me to you. This is my eternal name and my memorial from generation to generation.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:16

Greek: ελθων ουν συναγαγε την γερουσιαν των υιων ισραηλ και ερεις προς αυτους κυριος ο θεος των πατερων υμων ωπται μοι θεος αβρααμ και θεος ισαακ και θεος ιακωβ λεγων επισκοπη επεσκεμμαι υμας και οσα συμβεβηκεν υμιν εν αιγυπτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Go then, gather the elders of the sons of Israel and say to them, 'The Lord, the God of your fathers, has appeared to me, the God of Abraham and the God of Isaac and the God of Jacob, saying, I have surely visited you and the things that have happened to you in Egypt.'

Decision rows:
- greek_phrase: ἐπισκοπῇ ἐπεσκέμμαι ὑμᾶς | lemma: ἐπισκοπή | ἐπισκέπτομαι | morphology: dative noun + perfect middle/passive | chosen_rendering: have surely visited you | alternate_renderings: have surely attended to you; have surely looked in on you | rationale: Preserves the doubled visitation language, which carries both care and intervention. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: have surely visited you | footnote_text: Greek doubles the visitation idea. This draft keeps the repeated root because the line suggests active intervention, not mere observation. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:17

Greek: και ειπον αναβιβασω υμας εκ της κακωσεως των αιγυπτιων εις την γην των χαναναιων και χετταιων και αμορραιων και φερεζαιων και γεργεσαιων και ευαιων και ιεβουσαιων εις γην ρεουσαν γαλα και μελι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I said, I will bring you up out of the affliction of the Egyptians into the land of the Canaanites and Hittites and Amorites and Perizzites and Girgashites and Hivites and Jebusites, into a land flowing with milk and honey.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:18

Greek: και εισακουσονται σου της φωνης και εισελευση συ και η γερουσια ισραηλ προς φαραω βασιλεα αιγυπτου και ερεις προς αυτον ο θεος των εβραιων προσκεκληται ημας πορευσωμεθα ουν οδον τριων ημερων εις την ερημον ινα θυσωμεν τω θεω ημων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they will listen to your voice, and you and the elders of Israel shall go in to Pharaoh king of Egypt, and you shall say to him, 'The God of the Hebrews has summoned us. Let us go then a journey of three days into the wilderness so that we may sacrifice to our God.'

Decision rows:
- greek_phrase: προσκέκληται ἡμᾶς | lemma: προσκαλέω | morphology: perfect middle/passive indicative 3 singular | chosen_rendering: has summoned us | alternate_renderings: has called us; has called us to himself | rationale: Summoned gives the line formal force and movement without overstating intimacy. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: has summoned us | footnote_text: The verb can mean call or summon. This draft stresses formal divine commissioning before Pharaoh. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:19

Greek: εγω δε οιδα οτι ου προησεται υμας φαραω βασιλευς αιγυπτου πορευθηναι εαν μη μετα χειρος κραταιας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But I know that Pharaoh king of Egypt will not let you go, except under a mighty hand.

Decision rows:
- greek_phrase: ἐὰν μὴ μετὰ χειρὸς κραταιᾶς | lemma: χείρ | κραταιός | morphology: prepositional phrase | chosen_rendering: except under a mighty hand | alternate_renderings: unless by a mighty hand; unless compelled by a mighty hand | rationale: Keeps the image of overpowering force without adding extra words not present in the Greek. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: except under a mighty hand | footnote_text: The Greek phrase is compact and image-rich. This draft preserves the hand-language rather than immediately paraphrasing it as mere force or coercion. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:20

Greek: και εκτεινας την χειρα παταξω τους αιγυπτιους εν πασι τοις θαυμασιοις μου οις ποιησω εν αυτοις και μετα ταυτα εξαποστελει υμας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And stretching out my hand, I will strike the Egyptians with all my wonders that I will do among them, and after these things he will send you out.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:21

Greek: και δωσω χαριν τω λαω τουτω εναντιον των αιγυπτιων οταν δε αποτρεχητε ουκ απελευσεσθε κενοι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I will give favor to this people before the Egyptians, and when you depart, you will not depart empty.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 3:22

Greek: αιτησει γυνη παρα γειτονος και συσκηνου αυτης σκευη αργυρα και χρυσα και ιματισμον και επιθησετε επι τους υιους υμων και επι τας θυγατερας υμων και σκυλευσετε τους αιγυπτιους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Each woman shall ask from her neighbor and her fellow-dweller articles of silver and gold and clothing, and you shall put them on your sons and on your daughters, and you shall plunder the Egyptians.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 4

### Exodus 4:1

Greek: απεκριθη δε μωυσης και ειπεν εαν ουν μη πιστευσωσιν μοι μηδε εισακουσωσιν της φωνης μου ερουσιν γαρ οτι ουκ ωπται σοι ο θεος τι ερω προς αυτους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses answered and said, 'What if they do not believe me or listen to my voice? For they will say, God has not appeared to you. What shall I say to them?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:2

Greek: ειπεν δε αυτω κυριος τι τουτο εστιν το εν τη χειρι σου ο δε ειπεν ραβδος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to him, 'What is this in your hand?' And he said, 'A staff.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:3

Greek: και ειπεν ριψον αυτην επι την γην και ερριψεν αυτην επι την γην και εγενετο οφις και εφυγεν μωυσης απ' αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said, 'Throw it on the ground.' And he threw it on the ground, and it became a serpent, and Moses fled from it.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:4

Greek: και ειπεν κυριος προς μωυσην εκτεινον την χειρα και επιλαβου της κερκου εκτεινας ουν την χειρα επελαβετο της κερκου και εγενετο ραβδος εν τη χειρι αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, 'Stretch out your hand and seize its tail.' So stretching out his hand, he seized its tail, and it became a staff in his hand.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:5

Greek: ινα πιστευσωσιν σοι οτι ωπται σοι κυριος ο θεος των πατερων αυτων θεος αβρααμ και θεος ισαακ και θεος ιακωβ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: So that they may believe you that the Lord, the God of their fathers, the God of Abraham and the God of Isaac and the God of Jacob, has appeared to you.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:6

Greek: ειπεν δε αυτω κυριος παλιν εισενεγκε την χειρα σου εις τον κολπον σου και εισηνεγκεν την χειρα αυτου εις τον κολπον αυτου και εξηνεγκεν την χειρα αυτου εκ του κολπου αυτου και εγενηθη η χειρ αυτου ωσει χιων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to him again, 'Put your hand into your bosom.' And he put his hand into his bosom, and he brought his hand out of his bosom, and his hand became like snow.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:7

Greek: και ειπεν παλιν εισενεγκε την χειρα σου εις τον κολπον σου και εισηνεγκεν την χειρα εις τον κολπον αυτου και εξηνεγκεν αυτην εκ του κολπου αυτου και παλιν απεκατεστη εις την χροαν της σαρκος αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said again, 'Put your hand into your bosom.' And he put his hand into his bosom and brought it out of his bosom, and it was restored again to the color of his flesh.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:8

Greek: εαν δε μη πιστευσωσιν σοι μηδε εισακουσωσιν της φωνης του σημειου του πρωτου πιστευσουσιν σοι της φωνης του σημειου του εσχατου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And if they do not believe you or listen to the voice of the first sign, they will believe the voice of the last sign.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:9

Greek: και εσται εαν μη πιστευσωσιν σοι τοις δυσι σημειοις τουτοις μηδε εισακουσωσιν της φωνης σου λημψη απο του υδατος του ποταμου και εκχεεις επι το ξηρον και εσται το υδωρ ο εαν λαβης απο του ποταμου αιμα επι του ξηρου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it will be, if they do not believe you by these two signs and do not listen to your voice, you shall take from the water of the river and pour it on the dry ground, and the water that you take from the river will become blood on the dry ground.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:10

Greek: ειπεν δε μωυσης προς κυριον δεομαι κυριε ουχ ικανος ειμι προ της εχθες ουδε προ της τριτης ημερας ουδε αφ' ου ηρξω λαλειν τω θεραποντι σου ισχνοφωνος και βραδυγλωσσος εγω ειμι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said to the Lord, 'I beg you, Lord, I have not been adequate before, neither yesterday nor the day before, nor since you began speaking to your servant. I am weak-voiced and slow-tongued.'

Decision rows:
- greek_phrase: ἰσχνόφωνος καὶ βραδύγλωσσος | lemma: ἰσχνόφωνος | βραδύγλωσσος | morphology: paired adjectives | chosen_rendering: weak-voiced and slow-tongued | alternate_renderings: weak in speech and slow-tongued; poor speaker | rationale: Keeps the bodily and vocal imagery sharper than a generalized 'not eloquent.' | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: weak-voiced and slow-tongued | footnote_text: Greek describes Moses with bodily speech-language, not merely a lack of polish. This draft keeps the physical and vocal feel of the complaint. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:11

Greek: ειπεν δε κυριος προς μωυσην τις εδωκεν στομα ανθρωπω και τις εποιησεν δυσκωφον και κωφον βλεποντα και τυφλον ουκ εγω ο θεος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, 'Who gave a mouth to a human being? And who made one speechless and deaf, seeing and blind? Is it not I, God?'

Decision rows:
- greek_phrase: δυσκώφον καὶ κωφόν | lemma: δυσκώφος | κωφός | morphology: paired adjectives | chosen_rendering: speechless and deaf | alternate_renderings: hard of hearing and deaf; mute and deaf | rationale: The Greek pair is difficult and overlapping, so the draft preserves the bodily disability language without over-resolving it. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: speechless and deaf | footnote_text: The Greek pair is difficult and may overlap in meaning. This draft keeps both terms visible rather than collapsing them into one generic category. | source_basis: lexical + disability language | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:12

Greek: και νυν πορευου και εγω ανοιξω το στομα σου και συμβιβασω σε ο μελλεις λαλησαι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And now go, and I will open your mouth and instruct you in what you are about to say.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:13

Greek: και ειπεν μωυσης δεομαι κυριε προχειρισαι δυναμενον αλλον ον αποστελεις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said, 'I beg you, Lord, appoint another capable one whom you will send.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:14

Greek: και θυμωθεις οργη κυριος επι μωυσην ειπεν ουκ ιδου ααρων ο αδελφος σου ο λευιτης επισταμαι οτι λαλων λαλησει αυτος σοι και ιδου αυτος εξελευσεται εις συναντησιν σοι και ιδων σε χαρησεται εν εαυτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord, angered with wrath against Moses, said, 'Look, is not Aaron the Levite your brother? I know that speaking he will speak for you. And look, he himself will come out to meet you, and seeing you, he will rejoice within himself.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:15

Greek: και ερεις προς αυτον και δωσεις τα ρηματα μου εις το στομα αυτου και εγω ανοιξω το στομα σου και το στομα αυτου και συμβιβασω υμας α ποιησετε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And you shall speak to him and put my words into his mouth, and I will open your mouth and his mouth, and I will instruct you what you shall do.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:16

Greek: και αυτος σοι προσλαλησει προς τον λαον και αυτος εσται σου στομα συ δε αυτω εση τα προς τον θεον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he himself will speak for you to the people, and he will be your mouth, but you will be for him in the things toward God.

Decision rows:
- greek_phrase: σὺ δὲ αὐτῷ ἔσῃ τὰ πρὸς τὸν θεόν | lemma: πρός | θεός | morphology: prepositional phrase | chosen_rendering: you will be for him in the things toward God | alternate_renderings: you will be for him in matters concerning God; you will be as God to him | rationale: This draft keeps the Greek's more oblique phrasing instead of jumping straight to a stronger interpretive paraphrase. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: in the things toward God | footnote_text: Greek is less direct here than the stronger paraphrase 'as God to him.' This draft keeps the unusual wording visible for later theological review. | source_basis: syntax + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:17

Greek: και την ραβδον ταυτην την στραφεισαν εις οφιν λημψη εν τη χειρι σου εν η ποιησεις εν αυτη τα σημεια
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And this staff, the one turned into a serpent, you shall take in your hand, with it you shall do the signs.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:18

Greek: επορευθη δε μωυσης και απεστρεψεν προς ιοθορ τον γαμβρον αυτου και λεγει πορευσομαι και αποστρεψω προς τους αδελφους μου τους εν αιγυπτω και οψομαι ει ετι ζωσιν και ειπεν ιοθορ μωυση βαδιζε υγιαινων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses went and returned to Jothor his father-in-law and said, 'I will go now and return to my brothers in Egypt and see whether they are still alive.' And Jothor said to Moses, 'Go in health.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:19

Greek: μετα δε τας ημερας τας πολλας εκεινας ετελευτησεν ο βασιλευς αιγυπτου ειπεν δε κυριος προς μωυσην εν μαδιαμ βαδιζε απελθε εις αιγυπτον τεθνηκασιν γαρ παντες οι ζητουντες σου την ψυχην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now after those many days the king of Egypt died. And the Lord said to Moses in Midian, 'Go, depart into Egypt, for all seeking your life have died.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:20

Greek: αναλαβων δε μωυσης την γυναικα και τα παιδια ανεβιβασεν αυτα επι τα υποζυγια και επεστρεψεν εις αιγυπτον ελαβεν δε μωυσης την ραβδον την παρα του θεου εν τη χειρι αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses, taking his wife and his children, mounted them on the pack animals and returned to Egypt. And Moses took the staff from God in his hand.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:21

Greek: ειπεν δε κυριος προς μωυσην πορευομενου σου και αποστρεφοντος εις αιγυπτον ορα παντα τα τερατα α εδωκα εν ταις χερσιν σου ποιησεις αυτα εναντιον φαραω εγω δε σκληρυνω την καρδιαν αυτου και ου μη εξαποστειλη τον λαον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, 'When you go and return to Egypt, see that you do all the wonders that I gave into your hands before Pharaoh. But I will harden his heart, and he will certainly not send out the people.'

Decision rows:
- greek_phrase: τὰ τέρατα...ἃ ἔδωκα ἐν ταῖς χερσίν σου | lemma: τέρας | δίδωμι | morphology: accusative plural + verb | chosen_rendering: gave into your hands | alternate_renderings: put in your hands; charged you with | rationale: Keeps the concrete hand-language attached to the entrusted wonders. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: gave into your hands | footnote_text: The line speaks of wonders given into Moses' hands. This draft preserves the entrusted-in-hand imagery rather than converting it immediately into a looser expression like 'assigned.' | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:22

Greek: συ δε ερεις τω φαραω ταδε λεγει κυριος υιος πρωτοτοκος μου ισραηλ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And you shall say to Pharaoh, 'These things says the Lord: Israel is my firstborn son.'

Decision rows:
- greek_phrase: υἱὸς πρωτότοκός μου Ἰσραήλ | lemma: υἱός | πρωτότοκος | morphology: nominative noun phrase | chosen_rendering: Israel is my firstborn son | alternate_renderings: Israel is my firstborn; Israel my firstborn child | rationale: The explicit son-language is theologically weighty and should stay audible. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: firstborn son | footnote_text: The Greek is explicit: Israel is addressed as God's firstborn son. This draft keeps both kinship and rank language in place. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:23

Greek: ειπα δε σοι εξαποστειλον τον λαον μου ινα μοι λατρευση ει μεν ουν μη βουλει εξαποστειλαι αυτους ορα ουν εγω αποκτενω τον υιον σου τον πρωτοτοκον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I said to you, Send out my people so that they may serve me. But if you refuse to send them out, look then, I will kill your firstborn son.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:24

Greek: εγενετο δε εν τη οδω εν τω καταλυματι συνηντησεν αυτω αγγελος κυριου και εζητει αυτον αποκτειναι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it happened on the way, at the lodging place, that a messenger of the Lord met him and sought to kill him.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:25

Greek: και λαβουσα σεπφωρα ψηφον περιετεμεν την ακροβυστιαν του υιου αυτης και προσεπεσεν προς τους ποδας και ειπεν εστη το αιμα της περιτομης του παιδιου μου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Sepphora, taking a stone, circumcised the foreskin of her son and fell at his feet and said, 'The blood of my child's circumcision stands.'

Decision rows:
- greek_phrase: ἔστη τὸ αἷμα τῆς περιτομῆς τοῦ παιδίου μου | lemma: ἵστημι | αἷμα | περιτομή | morphology: aorist verb + noun phrase | chosen_rendering: the blood of my child's circumcision stands | alternate_renderings: the blood of my child's circumcision is staunched; here is the blood of my child's circumcision | rationale: The line is obscure, so the draft keeps the strange standing-language visible instead of smoothing it too quickly. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: the blood of my child's circumcision stands | footnote_text: This line is notoriously difficult. The draft keeps the strange 'stands' language visible so the problem remains reviewable rather than hidden under a smoother but more interpretive translation. | source_basis: textual + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:26

Greek: και απηλθεν απ' αυτου διοτι ειπεν εστη το αιμα της περιτομης του παιδιου μου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he departed from him, because she said, 'The blood of my child's circumcision stands.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:27

Greek: ειπεν δε κυριος προς ααρων πορευθητι εις συναντησιν μωυσει εις την ερημον και επορευθη και συνηντησεν αυτω εν τω ορει του θεου και κατεφιλησαν αλληλους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Aaron, 'Go into the wilderness to meet Moses.' And he went and met him at the mountain of God, and they kissed one another.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:28

Greek: και ανηγγειλεν μωυσης τω ααρων παντας τους λογους κυριου ους απεστειλεν και παντα τα σημεια α ενετειλατο αυτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses reported to Aaron all the words of the Lord with which he had sent him, and all the signs that he had commanded him.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:29

Greek: επορευθη δε μωυσης και ααρων και συνηγαγον την γερουσιαν των υιων ισραηλ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses and Aaron went and gathered the elders of the sons of Israel.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:30

Greek: και ελαλησεν ααρων παντα τα ρηματα ταυτα α ελαλησεν ο θεος προς μωυσην και εποιησεν τα σημεια εναντιον του λαου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Aaron spoke all these words that God had spoken to Moses, and he did the signs before the people.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 4:31

Greek: και επιστευσεν ο λαος και εχαρη οτι επεσκεψατο ο θεος τους υιους ισραηλ και οτι ειδεν αυτων την θλιψιν κυψας δε ο λαος προσεκυνησεν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the people believed and rejoiced because God had visited the sons of Israel and because he had seen their affliction. And bowing down, the people worshiped.

Decision rows:
- greek_phrase: ἐπεσκέψατο ὁ θεός | lemma: ἐπισκέπτομαι | morphology: aorist middle indicative 3 singular | chosen_rendering: God had visited | alternate_renderings: God visited; God looked in on | rationale: Keeps continuity with the visitation language already used in the commission scene. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: God had visited | footnote_text: The same visitation language used earlier returns here. This draft preserves that verbal link between promise and fulfillment. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 5

### Exodus 5:1

Greek: και μετα ταυτα εισηλθεν μωυσης και ααρων προς φαραω και ειπαν αυτω ταδε λεγει κυριος ο θεος ισραηλ εξαποστειλον τον λαον μου ινα μοι εορτασωσιν εν τη ερημω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And after these things Moses and Aaron went in to Pharaoh and said to him, 'These things says the Lord, the God of Israel: Send out my people so that they may hold a feast to me in the wilderness.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:2

Greek: και ειπεν φαραω τις εστιν ου εισακουσομαι της φωνης αυτου ωστε εξαποστειλαι τους υιους ισραηλ ουκ οιδα τον κυριον και τον ισραηλ ουκ εξαποστελλω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh said, 'Who is this, whose voice I should listen to so as to send out the sons of Israel? I do not know the Lord, and I will not send Israel out.'

Decision rows:
- greek_phrase: οὐκ οἶδα τὸν κύριον | lemma: οἶδα | κύριος | morphology: verb + accusative | chosen_rendering: I do not know the Lord | alternate_renderings: I do not acknowledge the Lord; I do not recognize the Lord | rationale: Keeps Pharaoh's defiant refusal pointed and personal. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: I do not know the Lord | footnote_text: Pharaoh's response is not mere ignorance but defiance. The line rejects the Lord's claim on him and on Israel. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:3

Greek: και λεγουσιν αυτω ο θεος των εβραιων προσκεκληται ημας πορευσομεθα ουν οδον τριων ημερων εις την ερημον οπως θυσωμεν τω θεω ημων μηποτε συναντηση ημιν θανατος η φονος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they say to him, 'The God of the Hebrews has summoned us. Let us go then a journey of three days into the wilderness so that we may sacrifice to our God, lest death or slaughter meet us.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:4

Greek: και ειπεν αυτοις ο βασιλευς αιγυπτου ινα τι μωυση και ααρων διαστρεφετε τον λαον μου απο των εργων απελθατε εκαστος υμων προς τα εργα αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the king of Egypt said to them, 'Why, Moses and Aaron, do you turn my people away from their works? Go away, each of you, to his work.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:5

Greek: και ειπεν φαραω ιδου νυν πολυπληθει ο λαος μη ουν καταπαυσωμεν αυτους απο των εργων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh said, 'Look now, the people are numerous. Should we then give them rest from their works?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:6

Greek: συνεταξεν δε φαραω τοις εργοδιωκταις του λαου και τοις γραμματευσιν λεγων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh commanded the taskmasters of the people and the scribes, saying,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:7

Greek: ουκετι προστεθησεται διδοναι αχυρον τω λαω εις την πλινθουργιαν καθαπερ εχθες και τριτην ημεραν αυτοι πορευεσθωσαν και συναγαγετωσαν εαυτοις αχυρα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: You shall no longer continue giving straw to the people for brick-making as yesterday and the day before. Let them go and gather straw for themselves.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:8

Greek: και την συνταξιν της πλινθειας ης αυτοι ποιουσιν καθ' εκαστην ημεραν επιβαλεις αυτοις ουκ αφελεις ουδεν σχολαζουσιν γαρ δια τουτο κεκραγασιν λεγοντες πορευθωμεν και θυσωμεν τω θεω ημων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the quota of brick that they make each day, you shall impose on them; you shall not take away anything, for they are idle. Because of this they cry out, saying, Let us go and sacrifice to our God.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:9

Greek: βαρυνεσθω τα εργα των ανθρωπων τουτων και μεριμνατωσαν ταυτα και μη μεριμνατωσαν εν λογοις κενοις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Let the works of these men be made heavy, and let them attend to these things, and let them not attend to empty words.

Decision rows:
- greek_phrase: λόγοις κενοῖς | lemma: λόγος | κενός | morphology: dative plural phrase | chosen_rendering: empty words | alternate_renderings: vain words; empty talk | rationale: Empty words preserves Pharaoh's contempt for Moses' message without softening the insult. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: empty words | footnote_text: Pharaoh labels Moses' message 'empty words.' This draft keeps that contemptuous wording visible rather than replacing it with a flatter expression. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:10

Greek: κατεσπευδον δε αυτους οι εργοδιωκται και οι γραμματεις και ελεγον προς τον λαον λεγοντες ταδε λεγει φαραω ουκετι διδωμι υμιν αχυρα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the taskmasters and the scribes hurried them and spoke to the people, saying, 'These things says Pharaoh: I no longer give you straw.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:11

Greek: αυτοι υμεις πορευομενοι συλλεγετε εαυτοις αχυρα οθεν εαν ευρητε ου γαρ αφαιρειται απο της συνταξεως υμων ουθεν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: You yourselves go gather straw for yourselves wherever you can find it, for nothing is taken away from your quota.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:12

Greek: και διεσπαρη ο λαος εν ολη αιγυπτω συναγαγειν καλαμην εις αχυρα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: So the people were scattered through all Egypt to gather stubble for straw.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:13

Greek: οι δε εργοδιωκται κατεσπευδον αυτους λεγοντες συντελειτε τα εργα τα καθηκοντα καθ' ημεραν καθαπερ και οτε το αχυρον εδιδοτο υμιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the taskmasters hurried them, saying, 'Finish the works assigned each day, just as when the straw was being given to you.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:14

Greek: και εμαστιγωθησαν οι γραμματεις του γενους των υιων ισραηλ οι κατασταθεντες επ' αυτους υπο των επιστατων του φαραω λεγοντες δια τι ου συνετελεσατε τας συνταξεις υμων της πλινθειας καθαπερ εχθες και τριτην ημεραν και το της σημερον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the scribes from the race of the sons of Israel, those appointed over them by Pharaoh's overseers, were beaten, saying, 'Why have you not completed your quotas of brick-making as yesterday and the day before, and now today as well?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:15

Greek: εισελθοντες δε οι γραμματεις των υιων ισραηλ κατεβοησαν προς φαραω λεγοντες ινα τι ουτως ποιεις τοις σοις οικεταις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the scribes of the sons of Israel went in and cried out to Pharaoh, saying, 'Why do you act this way toward your servants?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:16

Greek: αχυρον ου διδοται τοις οικεταις σου και την πλινθον ημιν λεγουσιν ποιειν και ιδου οι παιδες σου μεμαστιγωνται αδικησεις ουν τον λαον σου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Straw is not given to your servants, and they tell us, Make bricks. And look, your servants are being beaten. But you do wrong to your people.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:17

Greek: και ειπεν αυτοις σχολαζετε σχολασται εστε δια τουτο λεγετε πορευθωμεν θυσωμεν τω θεω ημων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said to them, 'You are idle; you are idlers. Because of this you say, Let us go sacrifice to our God.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:18

Greek: νυν ουν πορευθεντες εργαζεσθε το γαρ αχυρον ου δοθησεται υμιν και την συνταξιν της πλινθειας αποδωσετε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now then, go work. For straw will not be given to you, yet you must deliver the quota of bricks.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:19

Greek: εωρων δε οι γραμματεις των υιων ισραηλ εαυτους εν κακοις λεγοντες ουκ απολειψετε της πλινθειας το καθηκον τη ημερα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the scribes of the sons of Israel saw themselves in trouble, as it was said, 'You shall not leave off from the bricks assigned each day.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:20

Greek: συνηντησαν δε μωυση και ααρων ερχομενοις εις συναντησιν αυτοις εκπορευομενων αυτων απο φαραω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then they met Moses and Aaron, who were standing to meet them as they came out from Pharaoh.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:21

Greek: και ειπαν αυτοις ιδοι ο θεος υμας και κριναι οτι εβδελυξατε την οσμην ημων εναντιον φαραω και εναντιον των θεραποντων αυτου δουναι ρομφαιαν εις τας χειρας αυτου αποκτειναι ημας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they said to them, 'May God look upon you and judge, because you have made our smell abhorrent before Pharaoh and before his servants, putting a sword into his hands to kill us.'

Decision rows:
- greek_phrase: ἐβδελύξατε τὴν ὀσμὴν ἡμῶν | lemma: βδελύσσω | ὀσμή | morphology: aorist verb + noun phrase | chosen_rendering: you have made our smell abhorrent | alternate_renderings: you have made our odor hateful; you have made us stink | rationale: The Greek is deliberately visceral, so the draft keeps the smell-language instead of abstracting it away. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: made our smell abhorrent | footnote_text: The Greek is bodily and social at once: Israel's representatives say Moses and Aaron have made them stink before Pharaoh. This draft keeps the offensive smell-image instead of converting it into a safer abstraction. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:22

Greek: επεστρεψεν δε μωυσης προς κυριον και ειπεν κυριε δια τι εκακωσας τον λαον τουτον και ινα τι απεσταλκας με
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses turned back to the Lord and said, 'Lord, why have you afflicted this people, and why have you sent me?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 5:23

Greek: και αφ' ου πεπορευμαι προς φαραω λαλησαι επι τω σω ονοματι εκακωσεν τον λαον τουτον και ουκ ερρυσω τον λαον σου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: For from the time I went to Pharaoh to speak in your name, he has afflicted this people, and you have certainly not rescued your people.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 6

### Exodus 6:1

Greek: και ειπεν κυριος προς μωυσην ηδη οψει α ποιησω τω φαραω εν γαρ χειρι κραταια εξαποστελει αυτους και εν βραχιονι υψηλω εκβαλει αυτους εκ της γης αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, 'Now you will see what I will do to Pharaoh. For with a mighty hand he will send them out, and with a high arm he will cast them out of his land.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:2

Greek: ελαλησεν δε ο θεος προς μωυσην και ειπεν προς αυτον εγω κυριος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God spoke to Moses and said to him, 'I am the Lord.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:3

Greek: και ωφθην προς αβρααμ και ισαακ και ιακωβ θεος ων αυτων και το ονομα μου κυριος ουκ εδηλωσα αυτοις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I appeared to Abraham and Isaac and Jacob as their God, but my name Lord I did not make known to them.

Decision rows:
- greek_phrase: τὸ ὄνομά μου κύριος οὐκ ἐδήλωσα αὐτοῖς | lemma: ὄνομα | κύριος | δηλόω | morphology: accusative phrase | chosen_rendering: my name Lord I did not make known to them | alternate_renderings: I did not reveal my name Lord to them | rationale: Preserves the tension of the Greek wording without prematurely solving the theological problem. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: my name Lord I did not make known to them | footnote_text: This Greek wording creates a real interpretive problem because the divine name appears earlier in the narrative. The draft keeps the tension visible for later theological and textual review. | source_basis: theology + textual | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:4

Greek: και εστησα την διαθηκην μου προς αυτους ωστε δουναι αυτοις την γην των χαναναιων την γην ην παρωκηκασιν εν η και παρωκησαν επ' αυτης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I also established my covenant with them, to give them the land of the Canaanites, the land where they sojourned, in which they also lived as strangers.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:5

Greek: και εγω εισηκουσα τον στεναγμον των υιων ισραηλ ον οι αιγυπτιοι καταδουλουνται αυτους και εμνησθην της διαθηκης υμων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I also heard the groaning of the sons of Israel, whom the Egyptians enslave, and I remembered the covenant with you.

Decision rows:
- greek_phrase: ἐμνήσθην τῆς διαθήκης ὑμῶν | lemma: μιμνήσκομαι | διαθήκη | morphology: aorist passive/middle verb + genitive | chosen_rendering: I remembered the covenant with you | alternate_renderings: I remembered your covenant; I remembered the covenant | rationale: Keeps the odd second-person Greek alive for later textual review. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: the covenant with you | footnote_text: Greek here reads oddly, literally something like 'the covenant with you.' This draft preserves the strangeness rather than hiding it too early. | source_basis: textual + syntax | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:6

Greek: βαδιζε ειπον τοις υιοις ισραηλ λεγων εγω κυριος και εξαξω υμας απο της δυναστειας των αιγυπτιων και ρυσομαι υμας εκ της δουλειας και λυτρωσομαι υμας εν βραχιονι υψηλω και κρισει μεγαλη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Go, say to the sons of Israel, I am the Lord, and I will bring you out from the tyranny of the Egyptians, and I will rescue you from slavery, and I will redeem you with a high arm and with great judgment.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:7

Greek: και λημψομαι εμαυτω υμας λαον εμοι και εσομαι υμων θεος και γνωσεσθε οτι εγω κυριος ο θεος υμων ο εξαγαγων υμας εκ της καταδυναστειας των αιγυπτιων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I will take you to myself as a people for me, and I will be your God, and you will know that I am the Lord your God, the one bringing you out from the oppression of the Egyptians.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:8

Greek: και εισαξω υμας εις την γην εις ην εξετεινα την χειρα μου δουναι αυτην τω αβρααμ και ισαακ και ιακωβ και δωσω υμιν αυτην εν κληρω εγω κυριος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I will bring you into the land into which I stretched out my hand to give it to Abraham and Isaac and Jacob, and I will give it to you as an inheritance. I am the Lord.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:9

Greek: ελαλησεν δε μωυσης ουτως τοις υιοις ισραηλ και ουκ εισηκουσαν μωυση απο της ολιγοψυχιας και απο των εργων των σκληρων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses spoke thus to the sons of Israel, but they did not listen to Moses because of shortness of spirit and because of the hard labors.

Decision rows:
- greek_phrase: ἀπὸ τῆς ὀλιγοψυχίας | lemma: ὀλιγοψυχία | morphology: genitive singular noun | chosen_rendering: because of shortness of spirit | alternate_renderings: because of faint-heartedness; because of discouragement | rationale: Shortness of spirit preserves the compressed inner-life image of the Greek. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: shortness of spirit | footnote_text: Greek does not merely say the people were discouraged; it speaks of a kind of shortened or constricted spirit. This draft keeps that inner-pressure image visible. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:10

Greek: ειπεν δε κυριος προς μωυσην λεγων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, saying,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:11

Greek: εισελθε λαλησον φαραω βασιλει αιγυπτου ινα εξαποστειλη τους υιους ισραηλ εκ της γης αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Go in, speak to Pharaoh king of Egypt, so that he may send out the sons of Israel from his land.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:12

Greek: ελαλησεν δε μωυσης εναντι κυριου λεγων ιδου οι υιοι ισραηλ ουκ εισηκουσαν μου και πως εισακουσεται μου φαραω εγω δε αλογος ειμι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But Moses spoke before the Lord, saying, 'Look, the sons of Israel did not listen to me; so how will Pharaoh listen to me? And I am without speech.'

Decision rows:
- greek_phrase: ἐγὼ δὲ ἄλογός εἰμι | lemma: ἄλογος | morphology: predicate adjective | chosen_rendering: I am without speech | alternate_renderings: I am ineloquent; I am wordless | rationale: Keeps Moses' self-description close to the Greek rather than smoothing it into later idiom too quickly. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: without speech | footnote_text: Greek uses a stronger and less idiomatic self-description than simple 'not eloquent.' This draft keeps Moses' complaint abrupt and awkward. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:13

Greek: ειπεν δε κυριος προς μωυσην και ααρων και συνεταξεν αυτοις προς φαραω βασιλεα αιγυπτου ωστε εξαποστειλαι τους υιους ισραηλ εκ γης αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord spoke to Moses and Aaron, and he charged them concerning Pharaoh king of Egypt, that he should send out the sons of Israel from the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:14

Greek: και ουτοι αρχηγοι οικων πατριων αυτων υιοι ρουβην πρωτοτοκου ισραηλ ενωχ και φαλλους ασρων και χαρμι αυτη η συγγενεια ρουβην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And these are the heads of the houses of their families: sons of Reuben, firstborn of Israel: Enoch and Phallus, Asron and Charmi. This is the kindred of Reuben.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:15

Greek: και υιοι συμεων ιεμουηλ και ιαμιν και αωδ και ιαχιν και σααρ και σαουλ ο εκ της φοινισσης αυται αι πατριαι των υιων συμεων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And sons of Simeon: Jemuel and Jamin and Aod and Jachin and Saar and Saul, the one from the Phoenician woman. These are the families of the sons of Simeon.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:16

Greek: και ταυτα τα ονοματα των υιων λευι κατα συγγενειας αυτων γεδσων κααθ και μεραρι και τα ετη της ζωης λευι εκατον τριακοντα επτα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And these are the names of the sons of Levi according to their kinships: Gedson, Caath, and Merari. And the years of Levi's life were one hundred thirty-seven.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:17

Greek: και ουτοι υιοι γεδσων λοβενι και σεμει οικοι πατριας αυτων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And these are the sons of Gedson: Lobeni and Semei, houses of their families.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:18

Greek: και υιοι κααθ αμβραμ και ισσααρ χεβρων και οζιηλ και τα ετη της ζωης κααθ εκατον τριακοντα ετη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And sons of Caath: Ambram and Issaar, Chebron, and Oziel. And the years of Caath's life were one hundred thirty years.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:19

Greek: και υιοι μεραρι μοολι και ομουσι ουτοι οικοι πατριων λευι κατα συγγενειας αυτων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And sons of Merari: Mooli and Omousi. These are the houses of Levi according to their kinships.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:20

Greek: και ελαβεν αμβραμ την ιωχαβεδ θυγατερα του αδελφου του πατρος αυτου εαυτω εις γυναικα και εγεννησεν αυτω τον τε ααρων και μωυσην και μαριαμ την αδελφην αυτων τα δε ετη της ζωης αμβραμ εκατον τριακοντα δυο ετη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Ambram took Jochabed, daughter of his father's brother, as wife to himself, and she bore to him Aaron and Moses and Mariam their sister. And the years of Ambram's life were one hundred thirty-two years.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:21

Greek: και υιοι ισσααρ κορε και ναφεκ και ζεχρι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And sons of Issaar: Core and Naphec and Zechri.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:22

Greek: και υιοι οζιηλ ελισαφαν και σετρι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And sons of Oziel: Elisaphan and Setri.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:23

Greek: ελαβεν δε ααρων την ελισαβεθ θυγατερα αμιναδαβ αδελφην ναασσων αυτω γυναικα και ετεκεν αυτω τον τε ναδαβ και αβιουδ και ελεαζαρ και ιθαμαρ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Aaron took Elisabeth daughter of Aminadab, sister of Naasson, as wife to himself, and she bore to him Nadab and Abiud and Eleazar and Ithamar.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:24

Greek: υιοι δε κορε ασιρ και ελκανα και αβιασαφ αυται αι γενεσεις κορε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And sons of Core: Asir and Elkana and Abiasaph. These are the generations of Core.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:25

Greek: και ελεαζαρ ο του ααρων ελαβεν των θυγατερων φουτιηλ αυτω γυναικα και ετεκεν αυτω τον φινεες αυται αι αρχαι πατριας λευιτων κατα γενεσεις αυτων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Eleazar son of Aaron took for himself as wife one of the daughters of Phutiel, and she bore to him Phinees. These are the heads of the fathers of the Levites according to their generations.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:26

Greek: ουτος ααρων και μωυσης οις ειπεν αυτοις ο θεος εξαγαγειν τους υιους ισραηλ εκ γης αιγυπτου συν δυναμει αυτων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: This is Aaron and Moses, to whom God told them to bring out the sons of Israel from the land of Egypt with their forces.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:27

Greek: ουτοι εισιν οι διαλεγομενοι προς φαραω βασιλεα αιγυπτου και εξηγαγον τους υιους ισραηλ εξ αιγυπτου αυτος ααρων και μωυσης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: These are the ones speaking to Pharaoh king of Egypt and bringing out the sons of Israel from Egypt: this Aaron and Moses.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:28

Greek: η ημερα ελαλησεν κυριος μωυση εν γη αιγυπτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now it happened on the day the Lord spoke to Moses in the land of Egypt,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:29

Greek: και ελαλησεν κυριος προς μωυσην λεγων εγω κυριος λαλησον προς φαραω βασιλεα αιγυπτου οσα εγω λεγω προς σε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: that the Lord spoke to Moses, saying, 'I am the Lord. Speak to Pharaoh king of Egypt all that I speak to you.'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 6:30

Greek: και ειπεν μωυσης εναντιον κυριου ιδου εγω ισχνοφωνος ειμι και πως εισακουσεται μου φαραω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said before the Lord, 'Look, I am weak-voiced, and how will Pharaoh listen to me?'

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 7

### Exodus 7:1

Greek: και ειπεν κυριος προς μωυσην λεγων ιδου δεδωκα σε θεον φαραω και ααρων ο αδελφος σου εσται σου προφητης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, saying, 'See, I have given you as god to Pharaoh, and Aaron your brother shall be your prophet.'

Decision rows:
- greek_phrase: δέδωκά σε θεὸν φαραώ | lemma: δίδωμι | θεός | morphology: perfect active indicative + accusative phrase | chosen_rendering: given you as god to Pharaoh | alternate_renderings: made you a god to Pharaoh; given you as divine authority to Pharaoh | rationale: Keeps the startling designation visible rather than softening it into mere representation. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: as god to Pharaoh | footnote_text: Greek bluntly says Moses is given as god to Pharaoh. This draft keeps the striking wording visible instead of paraphrasing it into a safer expression of authority. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:2

Greek: συ δε λαλησεις αυτω παντα οσα σοι εντελλομαι ο δε ααρων ο αδελφος σου λαλησει προς φαραω ωστε εξαποστειλαι τους υιους ισραηλ εκ της γης αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: You shall speak to him all that I command you, and Aaron your brother shall speak to Pharaoh so that he may send out the sons of Israel from his land.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:3

Greek: εγω δε σκληρυνω την καρδιαν φαραω και πληθυνω τα σημεια μου και τα τερατα εν γη αιγυπτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But I will harden Pharaoh's heart, and I will multiply my signs and wonders in the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:4

Greek: και ουκ εισακουσεται υμων φαραω και επιβαλω την χειρα μου επ' αιγυπτον και εξαξω συν δυναμει μου τον λαον μου τους υιους ισραηλ εκ γης αιγυπτου συν εκδικησει μεγαλη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh will not listen to you, and I will lay my hand upon Egypt, and with my power I will bring out my people, the sons of Israel, from the land of Egypt with great vengeance.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:5

Greek: και γνωσονται παντες οι αιγυπτιοι οτι εγω ειμι κυριος εκτεινων την χειρα επ' αιγυπτον και εξαξω τους υιους ισραηλ εκ μεσου αυτων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And all the Egyptians shall know that I am the Lord, stretching out my hand upon Egypt, when I bring out the sons of Israel from their midst.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:6

Greek: εποιησεν δε μωυσης και ααρων καθαπερ ενετειλατο αυτοις κυριος ουτως εποιησαν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses and Aaron did just as the Lord commanded them; so they did.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:7

Greek: μωυσης δε ην ετων ογδοηκοντα ααρων δε ο αδελφος αυτου ετων ογδοηκοντα τριων ηνικα ελαλησεν προς φαραω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now Moses was eighty years old, and Aaron his brother was eighty-three years old, when he spoke to Pharaoh.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:8

Greek: και ειπεν κυριος προς μωυσην και ααρων λεγων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses and Aaron, saying,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:9

Greek: και εαν λαληση προς υμας φαραω λεγων δοτε ημιν σημειον η τερας και ερεις ααρων τω αδελφω σου λαβε την ραβδον και ριψον αυτην επι την γην εναντιον φαραω και εναντιον των θεραποντων αυτου και εσται δρακων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And if Pharaoh speaks to you, saying, Give us a sign or a wonder, then you shall say to Aaron your brother, Take the staff and throw it on the ground before Pharaoh and before his servants, and it will become a dragon.

Decision rows:
- greek_phrase: ἔσται δράκων | lemma: δράκων | morphology: future middle indicative 3 singular | chosen_rendering: it will become a dragon | alternate_renderings: it will become a serpent | rationale: Greek uses drakon rather than the more ordinary snake-word, so the draft preserves the stronger creature term. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: dragon | footnote_text: Greek uses drakon here rather than the more ordinary word for snake. This draft keeps the stronger creature term visible for review. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:10

Greek: εισηλθεν δε μωυσης και ααρων εναντιον φαραω και των θεραποντων αυτου και εποιησαν ουτως καθαπερ ενετειλατο αυτοις κυριος και ερριψεν ααρων την ραβδον εναντιον φαραω και εναντιον των θεραποντων αυτου και εγενετο δρακων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses and Aaron went in before Pharaoh and his servants, and they did so, just as the Lord had commanded them. And Aaron threw down his staff before Pharaoh and before his servants, and it became a dragon.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:11

Greek: συνεκαλεσεν δε φαραω τους σοφιστας αιγυπτου και τους φαρμακους και εποιησαν και οι επαοιδοι των αιγυπτιων ταις φαρμακειαις αυτων ωσαυτως
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Pharaoh called together the wise men of Egypt and the sorcerers, and the enchanters of the Egyptians also did likewise with their sorceries.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:12

Greek: και ερριψαν εκαστος την ραβδον αυτου και εγενοντο δρακοντες και κατεπιεν η ραβδος η ααρων τας εκεινων ραβδους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And each one threw down his staff, and they became dragons, but Aaron's staff swallowed up their staffs.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:13

Greek: και κατισχυσεν η καρδια φαραω και ουκ εισηκουσεν αυτων καθαπερ ελαλησεν αυτοις κυριος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh's heart grew strong, and he did not listen to them, just as the Lord had spoken to them.

Decision rows:
- greek_phrase: κατίσχυσεν ἡ καρδία φαραώ | lemma: κατισχύω | καρδία | morphology: aorist active indicative 3 singular | chosen_rendering: Pharaoh's heart grew strong | alternate_renderings: Pharaoh's heart prevailed; Pharaoh's heart hardened | rationale: Keeps this verb distinct from the later heavy and harden language in the plague cycle. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: heart grew strong | footnote_text: The Greek verb here differs from the later language of heaviness and hardening. This draft keeps the distinction so the pattern of heart-language remains visible. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:14

Greek: ειπεν δε κυριος προς μωυσην βεβαρηται η καρδια φαραω του μη εξαποστειλαι τον λαον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, 'Pharaoh's heart has become heavy, so that he will not send out the people.'

Decision rows:
- greek_phrase: βεβάρηται ἡ καρδία φαραώ | lemma: βαρέω | καρδία | morphology: perfect passive/middle indicative 3 singular | chosen_rendering: Pharaoh's heart has become heavy | alternate_renderings: Pharaoh's heart is weighed down; Pharaoh's heart is stubborn | rationale: Preserves the heaviness metaphor instead of flattening it into a generic stubbornness term. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: heart has become heavy | footnote_text: Greek speaks of heaviness here, not simply hardening. This draft preserves that image instead of merging all the heart verbs into one English term. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:15

Greek: βαδισον προς φαραω το πρωι ιδου αυτος εκπορευεται επι το υδωρ και στηση συναντων αυτω επι το χειλος του ποταμου και την ραβδον την στραφεισαν εις οφιν λημψη εν τη χειρι σου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Go to Pharaoh in the morning. Look, he is going out to the water, and you shall stand to meet him on the bank of the river, and you shall take in your hand the staff that was turned into a snake.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:16

Greek: και ερεις προς αυτον κυριος ο θεος των εβραιων απεσταλκεν με προς σε λεγων εξαποστειλον τον λαον μου ινα μοι λατρευση εν τη ερημω και ιδου ουκ εισηκουσας εως τουτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And you shall say to him, The Lord, the God of the Hebrews, has sent me to you, saying, Send out my people so that they may serve me in the wilderness, and look, until now you have not listened.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:17

Greek: ταδε λεγει κυριος εν τουτω γνωση οτι εγω κυριος ιδου εγω τυπτω τη ραβδω τη εν τη χειρι μου επι το υδωρ το εν τω ποταμω και μεταβαλει εις αιμα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: These things says the Lord: By this you shall know that I am the Lord. Look, I strike with the staff in my hand upon the water in the river, and it will turn into blood.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:18

Greek: και οι ιχθυες οι εν τω ποταμω τελευτησουσιν και εποζεσει ο ποταμος και ου δυνησονται οι αιγυπτιοι πιειν υδωρ απο του ποταμου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the fish in the river will die, and the river will stink, and the Egyptians will not be able to drink water from the river.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:19

Greek: ειπεν δε κυριος προς μωυσην ειπον ααρων τω αδελφω σου λαβε την ραβδον σου και εκτεινον την χειρα σου επι τα υδατα αιγυπτου και επι τους ποταμους αυτων και επι τας διωρυγας αυτων και επι τα ελη αυτων και επι παν συνεστηκος υδωρ αυτων και εσται αιμα και εγενετο αιμα εν παση γη αιγυπτου εν τε τοις ξυλοις και εν τοις λιθοις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, Say to Aaron your brother, Take your staff and stretch out your hand over the waters of Egypt, over their rivers and their canals and their marshes and every standing water of theirs, and it will become blood. And there will be blood in all the land of Egypt, both in the woods and in the stones.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:20

Greek: και εποιησαν ουτως μωυσης και ααρων καθαπερ ενετειλατο αυτοις κυριος και επαρας τη ραβδω αυτου επαταξεν το υδωρ το εν τω ποταμω εναντιον φαραω και εναντιον των θεραποντων αυτου και μετεβαλεν παν το υδωρ το εν τω ποταμω εις αιμα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses and Aaron did so, just as the Lord commanded them, and lifting up his staff, he struck the water in the river before Pharaoh and before his servants, and all the water in the river turned into blood.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:21

Greek: και οι ιχθυες οι εν τω ποταμω ετελευτησαν και επωζεσεν ο ποταμος και ουκ ηδυναντο οι αιγυπτιοι πιειν υδωρ εκ του ποταμου και ην το αιμα εν παση γη αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the fish in the river died, and the river stank, and the Egyptians were not able to drink water from the river, and the blood was in all the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:22

Greek: εποιησαν δε ωσαυτως και οι επαοιδοι των αιγυπτιων ταις φαρμακειαις αυτων και εσκληρυνθη η καρδια φαραω και ουκ εισηκουσεν αυτων καθαπερ ειπεν κυριος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the enchanters of the Egyptians did likewise with their sorceries, and Pharaoh's heart was hardened, and he did not listen to them, just as the Lord had said.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:23

Greek: επιστραφεις δε φαραω εισηλθεν εις τον οικον αυτου και ουκ επεστησεν τον νουν αυτου ουδε επι τουτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh turned and went into his house, and he did not set his mind even on this.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:24

Greek: ωρυξαν δε παντες οι αιγυπτιοι κυκλω του ποταμου ωστε πιειν υδωρ και ουκ ηδυναντο πιειν υδωρ απο του ποταμου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And all the Egyptians dug around the river so that they might drink water, for they were not able to drink water from the river.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:25

Greek: και ανεπληρωθησαν επτα ημεραι μετα το παταξαι κυριον τον ποταμον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And seven days were fulfilled after the Lord struck the river.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:26

Greek: ειπεν δε κυριος προς μωυσην εισελθε προς φαραω και ερεις προς αυτον ταδε λεγει κυριος εξαποστειλον τον λαον μου ινα μοι λατρευσωσιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, Go in to Pharaoh and say to him, These things says the Lord: Send out my people so that they may serve me.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:27

Greek: ει δε μη βουλει συ εξαποστειλαι ιδου εγω τυπτω παντα τα ορια σου τοις βατραχοις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But if you do not want to send them out, look, I strike all your borders with frogs.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:28

Greek: και εξερευξεται ο ποταμος βατραχους και αναβαντες εισελευσονται εις τους οικους σου και εις τα ταμιεια των κοιτωνων σου και επι των κλινων σου και εις τους οικους των θεραποντων σου και του λαου σου και εν τοις φυραμασιν σου και εν τοις κλιβανοις σου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the river will teem with frogs, and they will come up and enter into your houses and into the inner rooms of your bedchambers and upon your beds and into the houses of your servants and your people and into your dough and your ovens.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 7:29

Greek: και επι σε και επι τους θεραποντας σου και επι τον λαον σου αναβησονται οι βατραχοι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And upon you and upon your servants and upon your people the frogs will come up.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 8

### Exodus 8:1

Greek: ειπεν δε κυριος προς μωυσην ειπον ααρων τω αδελφω σου εκτεινον τη χειρι την ραβδον σου επι τους ποταμους και επι τας διωρυγας και επι τα ελη και αναγαγε τους βατραχους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, Say to Aaron your brother, Stretch out your hand with your staff over the rivers and over the canals and over the marshes, and bring up the frogs.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:2

Greek: και εξετεινεν ααρων την χειρα επι τα υδατα αιγυπτου και ανηγαγεν τους βατραχους και ανεβιβασθη ο βατραχος και εκαλυψεν την γην αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Aaron stretched out his hand over the waters of Egypt and brought up the frogs, and the frog came up and covered the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:3

Greek: εποιησαν δε ωσαυτως και οι επαοιδοι των αιγυπτιων ταις φαρμακειαις αυτων και ανηγαγον τους βατραχους επι γην αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the enchanters of the Egyptians did likewise with their sorceries, and they brought up the frogs upon the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:4

Greek: και εκαλεσεν φαραω μωυσην και ααρων και ειπεν ευξασθε περι εμου προς κυριον και περιελετω τους βατραχους απ' εμου και απο του εμου λαου και εξαποστελω τον λαον και θυσωσιν κυριω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh called Moses and Aaron and said, Pray concerning me to the Lord, and let him take away the frogs from me and from my people, and I will send out the people, and they will sacrifice to the Lord.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:5

Greek: ειπεν δε μωυσης προς φαραω ταξαι προς με ποτε ευξωμαι περι σου και περι των θεραποντων σου και περι του λαου σου αφανισαι τους βατραχους απο σου και απο του λαου σου και εκ των οικιων υμων πλην εν τω ποταμω υπολειφθησονται
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said to Pharaoh, Set for me when I should pray concerning you and concerning your servants and concerning your people, to wipe out the frogs from you and from your people and from your houses; only in the river will they be left.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:6

Greek: ο δε ειπεν εις αυριον ειπεν ουν ως ειρηκας ινα ειδης οτι ουκ εστιν αλλος πλην κυριου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said, Tomorrow. Then he said, As you have spoken, so that you may know that there is no other besides the Lord.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:7

Greek: και περιαιρεθησονται οι βατραχοι απο σου και εκ των οικιων υμων και εκ των επαυλεων και απο των θεραποντων σου και απο του λαου σου πλην εν τω ποταμω υπολειφθησονται
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the frogs will be taken away from you and from your houses and from the courtyards and from your servants and from your people; only in the river will they be left.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:8

Greek: εξηλθεν δε μωυσης και ααρων απο φαραω και εβοησεν μωυσης προς κυριον περι του ορισμου των βατραχων ως εταξατο φαραω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses and Aaron went out from Pharaoh, and Moses cried out to the Lord concerning the appointed matter of the frogs, as Pharaoh had set it.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:9

Greek: εποιησεν δε κυριος καθαπερ ειπεν μωυσης και ετελευτησαν οι βατραχοι εκ των οικιων και εκ των επαυλεων και εκ των αγρων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord did just as Moses said, and the frogs died out of the houses and out of the courtyards and out of the fields.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:10

Greek: και συνηγαγον αυτους θιμωνιας θιμωνιας και ωζεσεν η γη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they gathered them in heaps upon heaps, and the land stank.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:11

Greek: ιδων δε φαραω οτι γεγονεν αναψυξις εβαρυνθη η καρδια αυτου και ουκ εισηκουσεν αυτων καθαπερ ελαλησεν κυριος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh, seeing that there had come relief, made his heart heavy, and he did not listen to them, just as the Lord had spoken.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:12

Greek: ειπεν δε κυριος προς μωυσην ειπον ααρων εκτεινον τη χειρι την ραβδον σου και παταξον το χωμα της γης και εσονται σκνιφες εν τε τοις ανθρωποις και εν τοις τετραποσιν και εν παση γη αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, Say to Aaron, Stretch out your hand with your staff and strike the dust of the earth, and there will be gnats both on human beings and on the four-footed animals and in all the land of Egypt.

Decision rows:
- greek_phrase: σκνῖφες | lemma: σκνίψ | morphology: nominative plural noun | chosen_rendering: gnats | alternate_renderings: lice; gnats/gnats-like insects | rationale: The Greek points more naturally to a tiny flying pest than to lice, so gnats fits better. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: gnats | footnote_text: Greek likely points to a tiny biting or flying pest. This draft uses gnats rather than lice to keep closer to that sense. | source_basis: lexical | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:13

Greek: εξετεινεν ουν ααρων τη χειρι την ραβδον και επαταξεν το χωμα της γης και εγενοντο οι σκνιφες εν τε τοις ανθρωποις και εν τοις τετραποσιν και εν παντι χωματι της γης εγενοντο οι σκνιφες εν παση γη αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: So Aaron stretched out his hand with the staff and struck the dust of the earth, and the gnats came on human beings and on the four-footed animals, and in all the dust of the earth there were gnats in all the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:14

Greek: εποιησαν δε ωσαυτως και οι επαοιδοι ταις φαρμακειαις αυτων εξαγαγειν τον σκνιφα και ουκ ηδυναντο και εγενοντο οι σκνιφες εν τοις ανθρωποις και εν τοις τετραποσιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the enchanters did likewise with their sorceries, trying to bring out the gnat, and they were not able, and the gnats were on the human beings and on the four-footed animals.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:15

Greek: ειπαν ουν οι επαοιδοι τω φαραω δακτυλος θεου εστιν τουτο και εσκληρυνθη η καρδια φαραω και ουκ εισηκουσεν αυτων καθαπερ ελαλησεν κυριος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the enchanters said to Pharaoh, This is the finger of God. And Pharaoh's heart was hardened, and he did not listen to them, just as the Lord had spoken.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:16

Greek: ειπεν δε κυριος προς μωυσην ορθρισον το πρωι και στηθι εναντιον φαραω και ιδου αυτος εξελευσεται επι το υδωρ και ερεις προς αυτον ταδε λεγει κυριος εξαποστειλον τον λαον μου ινα μοι λατρευσωσιν εν τη ερημω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, Rise early in the morning and stand before Pharaoh, and look, he goes out to the water, and you shall say to him, These things says the Lord: Send out my people so that they may serve me in the wilderness.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:17

Greek: εαν δε μη βουλη εξαποστειλαι τον λαον μου ιδου εγω επαποστελλω επι σε και επι τους θεραποντας σου και επι τον λαον σου και επι τους οικους υμων κυνομυιαν και πλησθησονται αι οικιαι των αιγυπτιων της κυνομυιης και εις την γην εφ' ης εισιν επ' αυτης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But if you do not want to send out my people, look, I send upon you and upon your servants and upon your people and upon your houses the dog-fly, and the houses of the Egyptians will be filled with the dog-fly, and even the land on which they are.

Decision rows:
- greek_phrase: κυνομυίαν | lemma: κυνομυία | morphology: accusative singular collective noun | chosen_rendering: dog-fly | alternate_renderings: fly swarm; gadfly | rationale: Keeps the specific Greek compound visible instead of replacing it with a generic swarm term. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: dog-fly | footnote_text: Greek uses a specific compound term here rather than a generic word for flies. This draft keeps the unusual wording visible. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:18

Greek: και παραδοξασω εν τη ημερα εκεινη την γην γεσεμ εφ' ης ο λαος μου επεστιν επ' αυτης εφ' ης ουκ εσται εκει η κυνομυια ινα ειδης οτι εγω ειμι κυριος ο κυριος πασης της γης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I will distinguish wondrously on that day the land of Goshen, on which my people dwell, where the dog-fly will not be there, so that you may know that I am the Lord, the Lord of all the earth.

Decision rows:
- greek_phrase: κύριος ὁ κύριος πάσης τῆς γῆς | lemma: κύριος | γῆ | morphology: nominative phrase | chosen_rendering: the Lord, the Lord of all the earth | alternate_renderings: the Lord of all the earth | rationale: Retains the doubled lord-language that intensifies the claim over the whole land. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: the Lord, the Lord of all the earth | footnote_text: The Greek doubles the lord-language here. This draft preserves that intensified claim over the whole earth rather than trimming it down too quickly. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:19

Greek: και δωσω διαστολην ανα μεσον του εμου λαου και ανα μεσον του σου λαου εν δε τη αυριον εσται το σημειον τουτο επι της γης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I will put a distinction between my people and between your people. Tomorrow this sign will be upon the land.

Decision rows:
- greek_phrase: δώσω διαστολήν | lemma: δίδωμι | διαστολή | morphology: future active indicative 1 singular + accusative noun | chosen_rendering: I will put a distinction | alternate_renderings: I will set apart; I will make a separation | rationale: Keeps the separation language explicit in the plague contrast between Israel and Egypt. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: put a distinction | footnote_text: Greek uses explicit separation language between God's people and Pharaoh's people. This draft keeps that dividing line audible. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:20

Greek: εποιησεν δε κυριος ουτως και παρεγενετο η κυνομυια πληθος εις τους οικους φαραω και εις τους οικους των θεραποντων αυτου και εις πασαν την γην αιγυπτου και εξωλεθρευθη η γη απο της κυνομυιης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord did so, and the dog-fly came in abundance into the houses of Pharaoh and into the houses of his servants and into all the land of Egypt, and the land was ruined by the dog-fly.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:21

Greek: εκαλεσεν δε φαραω μωυσην και ααρων λεγων ελθοντες θυσατε τω θεω υμων εν τη γη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Pharaoh called Moses and Aaron, saying, Go, sacrifice to your God in the land.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:22

Greek: και ειπεν μωυσης ου δυνατον γενεσθαι ουτως τα γαρ βδελυγματα των αιγυπτιων θυσομεν κυριω τω θεω ημων εαν γαρ θυσωμεν τα βδελυγματα των αιγυπτιων εναντιον αυτων λιθοβοληθησομεθα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said, It cannot happen this way, for we shall sacrifice to the Lord our God the abominations of the Egyptians; for if we sacrifice the abominations of the Egyptians before them, we shall be stoned.

Decision rows:
- greek_phrase: τὰ βδελύγματα τῶν αἰγυπτίων | lemma: βδέλυγμα | Αἰγύπτιος | morphology: accusative plural noun phrase | chosen_rendering: the abominations of the Egyptians | alternate_renderings: what the Egyptians abhor; the Egyptians' abhorred things | rationale: Preserves the reciprocal offense built into the sacrifice dispute. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: abominations of the Egyptians | footnote_text: The sacrifice dispute turns on what Egyptians regard as abhorrent. This draft keeps the offense-language direct rather than reducing it to a neutral phrase. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:23

Greek: οδον τριων ημερων πορευσομεθα εις την ερημον και θυσομεν κυριω τω θεω ημων καθαπερ ειπεν ημιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: We will go a journey of three days into the wilderness, and we will sacrifice to the Lord our God, just as he said to us.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:24

Greek: και ειπεν φαραω εγω αποστελλω υμας και θυσατε κυριω τω θεω υμων εν τη ερημω αλλ' ου μακραν αποτενειτε πορευθηναι ευξασθε ουν περι εμου προς κυριον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh said, I send you out, and sacrifice to the Lord your God in the wilderness, only do not cut it too far to go. Pray then concerning me to the Lord.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:25

Greek: ειπεν δε μωυσης οδε εγω εξελευσομαι απο σου και ευξομαι προς τον θεον και απελευσεται η κυνομυια απο σου και απο των θεραποντων σου και του λαου σου αυριον μη προσθης ετι φαραω εξαπατησαι του μη εξαποστειλαι τον λαον θυσαι κυριω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said, Look, I am going out from you, and I will pray to God, and the dog-fly will depart from you and from your servants and your people tomorrow. Only do not add again, Pharaoh, to deceive by not sending out the people to sacrifice to the Lord.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:26

Greek: εξηλθεν δε μωυσης απο φαραω και ηυξατο προς τον θεον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses went out from Pharaoh and prayed to God.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:27

Greek: εποιησεν δε κυριος καθαπερ ειπεν μωυσης και περιειλεν την κυνομυιαν απο φαραω και των θεραποντων αυτου και του λαου αυτου και ου κατελειφθη ουδεμια
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord did just as Moses said, and he removed the dog-fly from Pharaoh and his servants and his people, and not one was left.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 8:28

Greek: και εβαρυνεν φαραω την καρδιαν αυτου και επι του καιρου τουτου και ουκ ηθελησεν εξαποστειλαι τον λαον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh made his heart heavy also at this time, and he did not want to send out the people.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 9

### Exodus 9:1

Greek: ειπεν δε κυριος προς μωυσην εισελθε προς φαραω και ερεις αυτω ταδε λεγει κυριος ο θεος των εβραιων εξαποστειλον τον λαον μου ινα μοι λατρευσωσιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, Go in to Pharaoh, and you shall say to him, These things says the Lord, the God of the Hebrews: Send out my people so that they may serve me.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:2

Greek: ει μεν ουν μη βουλει εξαποστειλαι τον λαον μου αλλ' ετι εγκρατεις αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: If, however, you do not want to send out my people, but still hold them back,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:3

Greek: ιδου χειρ κυριου επεσται εν τοις κτηνεσιν σου τοις εν τοις πεδιοις εν τε τοις ιπποις και εν τοις υποζυγιοις και ταις καμηλοις και βουσιν και προβατοις θανατος μεγας σφοδρα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: look, the hand of the Lord will come upon your livestock in the fields, both on the horses and on the beasts of burden and the camels and oxen and sheep, a very great death.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:4

Greek: και παραδοξασω εγω εν τω καιρω εκεινω ανα μεσον των κτηνων των αιγυπτιων και ανα μεσον των κτηνων των υιων ισραηλ ου τελευτησει απο παντων των του ισραηλ υιων ρητον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And I will make a wondrous distinction at that time between the livestock of the Egyptians and the livestock of the sons of Israel; not one thing from all that belongs to the sons of Israel shall die.

Decision rows:
- greek_phrase: παραδοξάσω...οὐ τελευτήσει...ῥητόν | lemma: παραδοξάζω | τελευτάω | ῥητός | morphology: future active + future verb + adjective | chosen_rendering: make a wondrous distinction / not one thing | alternate_renderings: distinguish marvelously / not a word; not a thing | rationale: Keeps both the striking distinction language and the odd concluding term visible. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: wondrous distinction | footnote_text: Greek uses strong distinction language here, not merely separation. This draft keeps the marvel-like force of the contrast between Egypt and Israel. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:5

Greek: και εδωκεν ο θεος ορον λεγων εν τη αυριον ποιησει κυριος το ρημα τουτο επι της γης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God set a limit, saying, Tomorrow the Lord will do this thing on the land.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:6

Greek: και εποιησεν κυριος το ρημα τουτο τη επαυριον και ετελευτησεν παντα τα κτηνη των αιγυπτιων απο δε των κτηνων των υιων ισραηλ ουκ ετελευτησεν ουδεν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord did this thing on the next day, and all the livestock of the Egyptians died, but from the livestock of the sons of Israel not one died.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:7

Greek: ιδων δε φαραω οτι ουκ ετελευτησεν απο παντων των κτηνων των υιων ισραηλ ουδεν εβαρυνθη η καρδια φαραω και ουκ εξαπεστειλεν τον λαον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh, seeing that not one had died from all the livestock of the sons of Israel, made Pharaoh's heart heavy, and he did not send out the people.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:8

Greek: ειπεν δε κυριος προς μωυσην και ααρων λεγων λαβετε υμεις πληρεις τας χειρας αιθαλης καμιναιας και πασατω μωυσης εις τον ουρανον εναντιον φαραω και εναντιον των θεραποντων αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses and Aaron, saying, Take for yourselves full handfuls of furnace soot, and let Moses scatter it into the sky before Pharaoh and before his servants.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:9

Greek: και γενηθητω κονιορτος επι πασαν την γην αιγυπτου και εσται επι τους ανθρωπους και επι τα τετραποδα ελκη φλυκτιδες αναζεουσαι εν τε τοις ανθρωποις και εν τοις τετραποσιν και εν παση γη αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And let it become dust over all the land of Egypt, and it will be on the human beings and on the four-footed animals sores with blisters boiling up in all the land of Egypt.

Decision rows:
- greek_phrase: ἕλκη φλυκτίδες ἀναζέουσαι | lemma: ἕλκος | φλυκτίς | ἀναζέω | morphology: noun phrase + participle | chosen_rendering: sores with blisters boiling up | alternate_renderings: boils with blains breaking out | rationale: Preserves the layered bodily imagery instead of compressing it into a single medical label. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: sores with blisters boiling up | footnote_text: The Greek piles up bodily plague terms rather than using a single neat label. This draft keeps the rough, eruptive feel of the wording. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:10

Greek: και ελαβεν την αιθαλην της καμιναιας εναντιον φαραω και επασεν αυτην μωυσης εις τον ουρανον και εγενετο ελκη φλυκτιδες αναζεουσαι εν τοις ανθρωποις και εν τοις τετραποσιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: So they took the furnace soot before Pharaoh, and Moses scattered it into the sky, and it became sores with blisters boiling up on the human beings and on the four-footed animals.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:11

Greek: και ουκ ηδυναντο οι φαρμακοι στηναι εναντιον μωυση δια τα ελκη εγενετο γαρ τα ελκη εν τοις φαρμακοις και εν παση γη αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the sorcerers were not able to stand before Moses because of the sores, for the sores came on the sorcerers and in all the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:12

Greek: εσκληρυνεν δε κυριος την καρδιαν φαραω και ουκ εισηκουσεν αυτων καθα συνεταξεν κυριος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord hardened Pharaoh's heart, and he did not listen to them, just as the Lord had commanded.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:13

Greek: ειπεν δε κυριος προς μωυσην ορθρισον το πρωι και στηθι εναντιον φαραω και ερεις προς αυτον ταδε λεγει κυριος ο θεος των εβραιων εξαποστειλον τον λαον μου ινα λατρευσωσιν μοι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, Rise early in the morning and stand before Pharaoh, and you shall say to him, These things says the Lord, the God of the Hebrews: Send out my people so that they may serve me.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:14

Greek: εν τω γαρ νυν καιρω εγω εξαποστελλω παντα τα συναντηματα μου εις την καρδιαν σου και των θεραποντων σου και του λαου σου ιν' ειδης οτι ουκ εστιν ως εγω αλλος εν παση τη γη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: For at this present time I send all my blows into your heart and into the heart of your servants and your people, so that you may know that there is no other like me in all the earth.

Decision rows:
- greek_phrase: πάντα τὰ συναντήματά μου εἰς τὴν καρδίαν σου | lemma: συνάντημα | καρδία | morphology: accusative plural noun phrase | chosen_rendering: all my blows into your heart | alternate_renderings: all my plagues into your heart; all my encounters into your heart | rationale: Blows keeps the force of divine strikes while retaining the inward-targeted imagery. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: blows into your heart | footnote_text: The Greek turns God's strikes inward toward Pharaoh's heart. This draft preserves that invasive image instead of flattening it into a generic reference to plagues. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:15

Greek: νυν γαρ αποστειλας την χειρα παταξω σε και τον λαον σου θανατω και εκτριβηση απο της γης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: For now, sending out my hand, I will strike you and your people with death, and you will be wiped off from the earth.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:16

Greek: και ενεκεν τουτου διετηρηθης ινα ενδειξωμαι εν σοι την ισχυν μου και οπως διαγγελη το ονομα μου εν παση τη γη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And because of this you have been preserved, so that I may display in you my strength and so that my name may be proclaimed in all the earth.

Decision rows:
- greek_phrase: διετηρήθης | lemma: διατηρέω | morphology: aorist passive indicative 2 singular | chosen_rendering: you have been preserved | alternate_renderings: you were kept alive; you were maintained | rationale: Preserved keeps both survival and divine intentionality in view. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: you have been preserved | footnote_text: Greek frames Pharaoh's survival as divinely maintained for a purpose. This draft keeps that sense of being spared in order to display divine power. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:17

Greek: ετι ουν συ εμποιη του λαου μου του μη εξαποστειλαι αυτους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Do you still set yourself against my people so as not to send them out?

Decision rows:
- greek_phrase: ἔτι οὖν σὺ ἐμποιῇ | lemma: ἐμποιέω | morphology: present active indicative/subjunctive 2 singular | chosen_rendering: Do you still set yourself against my people | alternate_renderings: Do you still exalt yourself over my people | rationale: Keeps Pharaoh's resistant self-positioning explicit without forcing a single interpretation too narrowly. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: set yourself against my people | footnote_text: The Greek points to Pharaoh's active stance against Israel, not merely passive delay. This draft keeps that oppositional posture visible. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:18

Greek: ιδου εγω υω ταυτην την ωραν αυριον χαλαζαν πολλην σφοδρα ητις τοιαυτη ου γεγονεν εν αιγυπτω αφ' ης ημερας εκτισται εως της ημερας ταυτης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Look, tomorrow at this hour I will rain a very great hail, such as has not happened in Egypt from the day it was created until this day.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:19

Greek: νυν ουν κατασπευσον συναγαγειν τα κτηνη σου και οσα σοι εστιν εν τω πεδιω παντες γαρ οι ανθρωποι και τα κτηνη οσα αν ευρεθη εν τω πεδιω και μη εισελθη εις οικιαν πεση δε επ' αυτα η χαλαζα τελευτησει
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now then hasten to gather your livestock and all that is yours in the field, for all the human beings and the livestock, as many as may be found in the field and not come into a house, when the hail falls upon them, will die.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:20

Greek: ο φοβουμενος το ρημα κυριου των θεραποντων φαραω συνηγαγεν τα κτηνη αυτου εις τους οικους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: The one fearing the word of the Lord among Pharaoh's servants gathered his livestock into the houses.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:21

Greek: ος δε μη προσεσχεν τη διανοια εις το ρημα κυριου αφηκεν τα κτηνη εν τοις πεδιοις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But whoever did not attend in his mind to the word of the Lord left the livestock in the fields.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:22

Greek: ειπεν δε κυριος προς μωυσην εκτεινον την χειρα σου εις τον ουρανον και εσται χαλαζα επι πασαν γην αιγυπτου επι τε τους ανθρωπους και τα κτηνη και επι πασαν βοτανην την επι της γης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, Stretch out your hand to the sky, and there will be hail on all the land of Egypt, both on the human beings and on the livestock and on every plant on the land.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:23

Greek: εξετεινεν δε μωυσης την χειρα εις τον ουρανον και κυριος εδωκεν φωνας και χαλαζαν και διετρεχεν το πυρ επι της γης και εβρεξεν κυριος χαλαζαν επι πασαν γην αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses stretched out his hand to the sky, and the Lord gave voices and hail, and the fire ran along on the ground, and the Lord rained hail upon all the land of Egypt.

Decision rows:
- greek_phrase: ἔδωκεν φωνὰς καὶ χάλαζαν | lemma: δίδωμι | φωνή | χάλαζα | morphology: aorist active indicative + accusative plurals | chosen_rendering: gave voices and hail | alternate_renderings: sent thunder and hail | rationale: Keeps the literal voice-language visible instead of immediately interpreting it as thunder. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: voices and hail | footnote_text: Greek literally says 'voices' rather than immediately naming thunder. This draft keeps the more direct heavenly-voice language visible. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:24

Greek: ην δε η χαλαζα και το πυρ φλογιζον εν τη χαλαζη η δε χαλαζα πολλη σφοδρα σφοδρα ητις τοιαυτη ου γεγονεν εν αιγυπτω αφ' ου γεγενηται επ' αυτης εθνος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And there was hail, and the fire flaming in the hail, and the hail was very, very great, such as had not happened in Egypt from the time a nation came to be upon it.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:25

Greek: επαταξεν δε η χαλαζα εν παση γη αιγυπτου απο ανθρωπου εως κτηνους και πασαν βοτανην την εν τω πεδιω επαταξεν η χαλαζα και παντα τα ξυλα τα εν τοις πεδιοις συνετριψεν η χαλαζα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the hail struck in all the land of Egypt, from human being to livestock, and the hail struck every plant in the field, and the hail shattered all the trees in the field.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:26

Greek: πλην εν γη γεσεμ ου ησαν οι υιοι ισραηλ ουκ εγενετο η χαλαζα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Only in the land of Goshen, where the sons of Israel were, there was no hail.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:27

Greek: αποστειλας δε φαραω εκαλεσεν μωυσην και ααρων και ειπεν αυτοις ημαρτηκα το νυν ο κυριος δικαιος εγω δε και ο λαος μου ασεβεις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh sent and called Moses and Aaron and said to them, I have sinned this time. The Lord is righteous, but I and my people are ungodly.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:28

Greek: ευξασθε ουν περι εμου προς κυριον και παυσασθω του γενηθηναι φωνας θεου και χαλαζαν και πυρ και εξαποστελω υμας και ουκετι προσθησεσθε μενειν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Pray then concerning me to the Lord, and let there cease from becoming voices of God and hail and fire, and I will send you out, and you shall no longer remain.

Decision rows:
- greek_phrase: φωνὰς θεοῦ | lemma: φωνή | θεός | morphology: accusative plural noun phrase | chosen_rendering: voices of God | alternate_renderings: thunders of God | rationale: Retains the concrete voice-language in Pharaoh's plea and links it with the earlier wording. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: voices of God | footnote_text: Pharaoh asks for the 'voices of God' to cease. This draft preserves the phrasing rather than reducing it to ordinary weather language. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:29

Greek: ειπεν δε αυτω μωυσης ως αν εξελθω την πολιν εκπετασω τας χειρας μου προς κυριον και αι φωναι παυσονται και η χαλαζα και ο υετος ουκ εσται ετι ινα γνως οτι του κυριου η γη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said to him, As soon as I go out from the city, I will spread out my hands to the Lord, and the voices will cease, and the hail and the rain will be no more, so that you may know that the earth belongs to the Lord.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:30

Greek: και συ και οι θεραποντες σου επισταμαι οτι ουδεπω πεφοβησθε τον κυριον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But you and your servants, I know that you do not yet fear the Lord.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:31

Greek: το δε λινον και η κριθη επληγη η γαρ κριθη παρεστηκυια το δε λινον σπερματιζον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the flax and the barley were struck, for the barley was standing, and the flax was seeding.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:32

Greek: ο δε πυρος και η ολυρα ουκ επληγη οψιμα γαρ ην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But the wheat and the rye were not struck, for they were late.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:33

Greek: εξηλθεν δε μωυσης απο φαραω εκτος της πολεως και εξεπετασεν τας χειρας προς κυριον και αι φωναι επαυσαντο και η χαλαζα και ο υετος ουκ εσταξεν ετι επι την γην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses went out from Pharaoh, outside the city, and spread out his hands to the Lord, and the voices ceased and the hail and the rain no longer fell on the earth.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:34

Greek: ιδων δε φαραω οτι πεπαυται ο υετος και η χαλαζα και αι φωναι προσεθετο του αμαρτανειν και εβαρυνεν αυτου την καρδιαν και των θεραποντων αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh, seeing that the rain and the hail and the voices had ceased, added to sin, and he made heavy his heart and the heart of his servants.

Decision rows:
- greek_phrase: προσέθετο τοῦ ἁμαρτάνειν / ἐβάρυνεν | lemma: προστίθημι | ἁμαρτάνω | βαρέω | morphology: aorist verb + infinitive / aorist active | chosen_rendering: added to sin / made heavy | alternate_renderings: continued sinning / hardened | rationale: Keeps both the repeated sin-language and the heaviness metaphor instead of flattening them. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: added to sin | footnote_text: Greek says Pharaoh added to sin and also made his heart heavy. This draft keeps both the repeated rebellion and the heaviness imagery. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 9:35

Greek: και εσκληρυνθη η καρδια φαραω και ουκ εξαπεστειλεν τους υιους ισραηλ καθαπερ ελαλησεν κυριος τω μωυση
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh's heart was hardened, and he did not send out the sons of Israel, just as the Lord had spoken to Moses.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 10

### Exodus 10:1

Greek: ειπεν δε κυριος προς μωυσην λεγων εισελθε προς φαραω εγω γαρ εσκληρυνα αυτου την καρδιαν και των θεραποντων αυτου ινα εξης επελθη τα σημεια ταυτα επ' αυτους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, "Go in to Pharaoh, for I have hardened his heart and the heart of his servants, so that these signs may come in turn upon them,"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:2

Greek: οπως διηγησησθε εις τα ωτα των τεκνων υμων και τοις τεκνοις των τεκνων υμων οσα εμπεπαιχα τοις αιγυπτιοις και τα σημεια μου α εποιησα εν αυτοις και γνωσεσθε οτι εγω κυριος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "so that you may tell your children and your children's children how I mocked the Egyptians and the signs I performed among them, and you will know that I am the Lord."

Decision rows:
- greek_phrase: ὅσα ἐμπέπαιχα τοῖς αἰγυπτίοις | lemma: ἐμπαίζω | Αἰγύπτιος | morphology: perfect active indicative 1 singular + dative plural noun | chosen_rendering: how I mocked the Egyptians | alternate_renderings: how I made sport of the Egyptians; how I toyed with the Egyptians | rationale: Keeps the humiliation motif explicit and avoids softening the verb into mere display language. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: mocked the Egyptians | footnote_text: Greek uses a mockery verb here. This draft keeps the humiliation of Egypt visible rather than reducing the line to a neutral display of power. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:3

Greek: εισηλθεν δε μωυσης και ααρων εναντιον φαραω και ειπαν αυτω ταδε λεγει κυριος ο θεος των εβραιων εως τινος ου βουλει εντραπηναι με εξαποστειλον τον λαον μου ινα λατρευσωσιν μοι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses and Aaron went in before Pharaoh and said to him, "These things says the Lord, the God of the Hebrews: How long will you refuse to humble yourself before me? Send my people away, so that they may serve me."

Decision rows:
- greek_phrase: ἐντραπῆναί με | lemma: ἐντρέπω | morphology: aorist passive infinitive | chosen_rendering: humble yourself before me | alternate_renderings: reverence me; be ashamed before me | rationale: Humble yourself fits the plague context and keeps the call to submission more clearly than a purely emotional shame reading. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: humble yourself before me | footnote_text: Greek can lean toward shame, reverence, or humbled submission. This draft chooses humbled submission because the plague narrative presses Pharaoh toward yielding before God. | source_basis: lexical + context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:4

Greek: εαν δε μη θελης συ εξαποστειλαι τον λαον μου ιδου εγω επαγω ταυτην την ωραν αυριον ακριδα πολλην επι παντα τα ορια σου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "But if you refuse to send my people away, behold, at this hour tomorrow I am bringing a great swarm of locusts upon all your borders."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:5

Greek: και καλυψει την οψιν της γης και ου δυνηση κατιδειν την γην και κατεδεται παν το περισσον της γης το καταλειφθεν ο κατελιπεν υμιν η χαλαζα και κατεδεται παν ξυλον το φυομενον υμιν επι της γης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "They will cover the face of the earth, and you will not be able to see the earth. They will eat every remainder of the land left behind, what the hail left for you, and they will eat every tree growing for you on the land."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:6

Greek: και πλησθησονται σου αι οικιαι και αι οικιαι των θεραποντων σου και πασαι αι οικιαι εν παση γη των αιγυπτιων α ουδεποτε εωρακασιν οι πατερες σου ουδε οι προπαπποι αυτων αφ' ης ημερας γεγονασιν επι της γης εως της ημερας ταυτης και εκκλινας μωυσης εξηλθεν απο φαραω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Your houses will be filled, and the houses of your servants, and all the houses in all the land of the Egyptians, with things your fathers never saw, nor their forefathers, from the day they came to be on the earth until this day." Then Moses turned away and went out from Pharaoh.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:7

Greek: και λεγουσιν οι θεραποντες φαραω προς αυτον εως τινος εσται τουτο ημιν σκωλον εξαποστειλον τους ανθρωπους οπως λατρευσωσιν τω θεω αυτων η ειδεναι βουλει οτι απολωλεν αιγυπτος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh's servants said to him, "How long will this be a snare to us? Send the men away, so that they may serve their God. Do you need to learn that Egypt is ruined?"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:8

Greek: και απεστρεψαν τον τε μωυσην και ααρων προς φαραω και ειπεν αυτοις πορευεσθε και λατρευσατε τω θεω υμων τινες δε και τινες εισιν οι πορευομενοι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they brought Moses and Aaron back to Pharaoh, and he said to them, "Go, serve the Lord your God. But who exactly are the ones going?"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:9

Greek: και λεγει μωυσης συν τοις νεανισκοις και πρεσβυτεροις πορευσομεθα συν τοις υιοις και θυγατρασιν και προβατοις και βουσιν ημων εστιν γαρ εορτη κυριου του θεου ημων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said, "We will go with young and old, with our sons and daughters, with our sheep and cattle, for we have a feast of the Lord our God."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:10

Greek: και ειπεν προς αυτους εστω ουτως κυριος μεθ' υμων καθοτι αποστελλω υμας μη και την αποσκευην υμων ιδετε οτι πονηρια προκειται υμιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said to them, "So be it: may the Lord be with you, just as I send you out, you and your baggage. See, evil lies ahead of you."

Decision rows:
- greek_phrase: τὴν ἀποσκευὴν ὑμῶν / πονηρία προκεῖται ὑμῖν | lemma: ἀποσκευή | πονηρία | πρόκειμαι | morphology: accusative singular noun / nominative singular noun + present middle/passive indicative 3 singular | chosen_rendering: your baggage / evil lies ahead of you | alternate_renderings: your store / evil is attached to you; your belongings / harm is before you | rationale: Retains the Greek baggage-language and the ominous image of evil lying before them instead of harmonizing to the Hebrew wording. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: your baggage ... evil lies ahead of you | footnote_text: Greek speaks of baggage or belongings and then says evil lies before them. This draft keeps both unusual expressions visible instead of smoothing them into a more familiar wording. | source_basis: lexical + textual | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:11

Greek: μη ουτως πορευεσθωσαν δε οι ανδρες και λατρευσατε τω θεω τουτο γαρ αυτοι ζητειτε εξεβαλον δε αυτους απο προσωπου φαραω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Not so. Let the men go and serve God, for this is what you yourselves seek." And they drove them out from Pharaoh's presence.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:12

Greek: ειπεν δε κυριος προς μωυσην εκτεινον την χειρα επι γην αιγυπτου και αναβητω ακρις επι την γην και κατεδεται πασαν βοτανην της γης και παντα τον καρπον των ξυλων ον υπελιπετο η χαλαζα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, "Stretch out your hand over the land of Egypt, and let the locust come up on the land and eat every plant of the land and every fruit of the trees that the hail left."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:13

Greek: και επηρεν μωυσης την ραβδον εις τον ουρανον και κυριος επηγαγεν ανεμον νοτον επι την γην ολην την ημεραν εκεινην και ολην την νυκτα το πρωι εγενηθη και ο ανεμος ο νοτος ανελαβεν την ακριδα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses lifted up the rod toward heaven, and the Lord brought a south wind upon the land all that day and all that night. Morning came, and the south wind brought in the locust.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:14

Greek: και ανηγαγεν αυτην επι πασαν γην αιγυπτου και κατεπαυσεν επι παντα τα ορια αιγυπτου πολλη σφοδρα προτερα αυτης ου γεγονεν τοιαυτη ακρις και μετα ταυτα ουκ εσται ουτως
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it came up over all the land of Egypt, and it settled over all the borders of Egypt in very great abundance. Before it no locust like it had come to be, and after it none will be so.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:15

Greek: και εκαλυψεν την οψιν της γης και εφθαρη η γη και κατεφαγεν πασαν βοτανην της γης και παντα τον καρπον των ξυλων ος υπελειφθη απο της χαλαζης ουχ υπελειφθη χλωρον ουδεν εν τοις ξυλοις και εν παση βοτανη του πεδιου εν παση γη αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it covered the face of the earth, and the land was ruined. And it ate every plant of the earth and every fruit of the trees left by the hail. No green thing was left on the trees or in any plant of the field in all the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:16

Greek: κατεσπευδεν δε φαραω καλεσαι μωυσην και ααρων λεγων ημαρτηκα εναντιον κυριου του θεου υμων και εις υμας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Pharaoh hurried to call Moses and Aaron, saying, "I have sinned before the Lord your God and against you."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:17

Greek: προσδεξασθε ουν μου την αμαρτιαν ετι νυν και προσευξασθε προς κυριον τον θεον υμων και περιελετω απ' εμου τον θανατον τουτον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Forgive, then, my sin just this once, and pray to the Lord your God, and let him take this death away from me."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:18

Greek: εξηλθεν δε μωυσης απο φαραω και ηυξατο προς τον θεον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses went out from Pharaoh and prayed to God.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:19

Greek: και μετεβαλεν κυριος ανεμον απο θαλασσης σφοδρον και ανελαβεν την ακριδα και ενεβαλεν αυτην εις την ερυθραν θαλασσαν και ουχ υπελειφθη ακρις μια εν παση γη αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord changed the wind to a strong wind from the sea, and it took up the locust and cast it into the Red Sea. Not one locust was left in all the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:20

Greek: και εσκληρυνεν κυριος την καρδιαν φαραω και ουκ εξαπεστειλεν τους υιους ισραηλ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord hardened Pharaoh's heart, and he did not send away the sons of Israel.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:21

Greek: ειπεν δε κυριος προς μωυσην εκτεινον την χειρα σου εις τον ουρανον και γενηθητω σκοτος επι γην αιγυπτου ψηλαφητον σκοτος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, "Stretch out your hand to heaven, and let darkness come over the land of Egypt, darkness that can be felt."

Decision rows:
- greek_phrase: ψηλαφητὸν σκότος | lemma: ψηλαφητός | σκότος | morphology: adjective + accusative singular noun | chosen_rendering: darkness that can be felt | alternate_renderings: palpable darkness; touchable darkness | rationale: Keeps the bodily, tangible force of the darkness visible in the English line. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: darkness that can be felt | footnote_text: Greek emphasizes darkness as tangible and bodily, not merely visual absence of light. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:22

Greek: εξετεινεν δε μωυσης την χειρα εις τον ουρανον και εγενετο σκοτος γνοφος θυελλα επι πασαν γην αιγυπτου τρεις ημερας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses stretched out his hand to heaven, and there came darkness, gloom, storm-cloud over all the land of Egypt for three days.

Decision rows:
- greek_phrase: σκότος γνόφος θυέλλα | lemma: σκότος | γνόφος | θυέλλα | morphology: nominative singular noun chain | chosen_rendering: darkness, gloom, storm-cloud | alternate_renderings: darkness, murk, tempest; deep darkness and storm-gloom | rationale: Preserves the piling up of overlapping darkness terms rather than collapsing them into a single adjective. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: darkness, gloom, storm-cloud | footnote_text: The Greek piles up several darkness terms in sequence. This draft preserves the layered imagery rather than compressing it into one descriptor. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:23

Greek: και ουκ ειδεν ουδεις τον αδελφον αυτου τρεις ημερας και ουκ εξανεστη ουδεις εκ της κοιτης αυτου τρεις ημερας πασι δε τοις υιοις ισραηλ ην φως εν πασιν οις κατεγινοντο
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: No one saw his brother for three days, and no one rose from his bed for three days. But all the sons of Israel had light in every place where they lived.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:24

Greek: και εκαλεσεν φαραω μωυσην και ααρων λεγων βαδιζετε λατρευσατε κυριω τω θεω υμων πλην των προβατων και των βοων υπολιπεσθε και η αποσκευη υμων αποτρεχετω μεθ' υμων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Pharaoh called Moses and Aaron, saying, "Go, serve the Lord your God. Only leave the sheep and cattle behind, and let your baggage go along with you."

Decision rows:
- greek_phrase: ἡ ἀποσκευὴ ὑμῶν ἀποτρεχέτω μεθ᾽ ὑμῶν | lemma: ἀποσκευή | ἀποτρέχω | morphology: nominative singular noun + present active imperative 3 singular | chosen_rendering: let your baggage go along with you | alternate_renderings: let your store depart with you; let your belongings run along with you | rationale: Keeps the odd Greek baggage wording visible instead of replacing it with children or households from another textual tradition. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:25

Greek: και ειπεν μωυσης αλλα και συ δωσεις ημιν ολοκαυτωματα και θυσιας α ποιησομεν κυριω τω θεω ημων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said, "But you too will give us whole burnt offerings and sacrifices, and we will offer them to the Lord our God."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:26

Greek: και τα κτηνη ημων πορευσεται μεθ' ημων και ουχ υπολειψομεθα οπλην απ' αυτων γαρ λημψομεθα λατρευσαι κυριω τω θεω ημων ημεις δε ουκ οιδαμεν τι λατρευσωμεν κυριω τω θεω ημων εως του ελθειν ημας εκει
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Our livestock too will go with us, and we will not leave behind a hoof, for from them we will take what we need to serve the Lord our God. But we do not know with what we will serve the Lord our God until we come there."

Decision rows:
- greek_phrase: οὐχ ὑπολείψομεθα ὁπλήν | lemma: ὑπολείπω | ὁπλή | morphology: future active indicative 1 plural + accusative singular noun | chosen_rendering: we will not leave behind a hoof | alternate_renderings: we will not leave a hoof; not a hoof will remain | rationale: The idiom is already vivid in Greek and worth preserving directly. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: not leave behind a hoof | footnote_text: The Greek idiom is concrete and emphatic. This draft keeps the hoof-language instead of generalizing it to livestock in the abstract. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:27

Greek: εσκληρυνεν δε κυριος την καρδιαν φαραω και ουκ εβουληθη εξαποστειλαι αυτους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But the Lord hardened Pharaoh's heart, and he was not willing to send them away.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:28

Greek: και λεγει φαραω απελθε απ' εμου προσεχε σεαυτω ετι προσθειναι ιδειν μου το προσωπον η δ' αν ημερα οφθης μοι αποθανη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh said, "Go away from me. Watch yourself. Do not see my face again, for on the day you appear before me, you will die."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 10:29

Greek: λεγει δε μωυσης ειρηκας ουκετι οφθησομαι σοι εις προσωπον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said, "You have spoken. I will no longer appear before your face."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 11

### Exodus 11:1

Greek: ειπεν δε κυριος προς μωυσην ετι μιαν πληγην επαξω επι φαραω και επ' αιγυπτον και μετα ταυτα εξαποστελει υμας εντευθεν οταν δε εξαποστελλη υμας συν παντι εκβαλει υμας εκβολη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, "Yet one plague I will bring upon Pharaoh and upon Egypt, and after that he will send you out from here. Whenever he sends you out, he will surely drive you out with a complete expulsion."

Decision rows:
- greek_phrase: ἐκβαλεῖ ὑμᾶς ἐκβολῇ | lemma: ἐκβάλλω | ἐκβολή | morphology: future active indicative 3 singular + dative singular noun | chosen_rendering: he will surely drive you out with a complete expulsion | alternate_renderings: he will utterly cast you out; he will drive you out decisively | rationale: Keeps the emphatic doubled expulsion language instead of flattening it to a simple dismissal. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: drive you out with a complete expulsion | footnote_text: Greek doubles the expulsion idea for emphasis. This draft keeps the force of that doubled wording visible. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 11:2

Greek: λαλησον ουν κρυφη εις τα ωτα του λαου και αιτησατω εκαστος παρα του πλησιον και γυνη παρα της πλησιον σκευη αργυρα και χρυσα και ιματισμον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Speak secretly into the ears of the people, and let each man ask from his neighbor, and each woman from her neighbor, silver and gold vessels and clothing."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 11:3

Greek: κυριος δε εδωκεν την χαριν τω λαω αυτου εναντιον των αιγυπτιων και εχρησαν αυτοις και ο ανθρωπος μωυσης μεγας εγενηθη σφοδρα εναντιον των αιγυπτιων και εναντιον φαραω και εναντιον παντων των θεραποντων αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord gave his people favor in the sight of the Egyptians, and they lent to them. And Moses the man became exceedingly great in the sight of the Egyptians and before Pharaoh and before all his servants.

Decision rows:
- greek_phrase: ἐχρήσαν αὐτοῖς | lemma: χράω | morphology: aorist active indicative 3 plural | chosen_rendering: they lent to them | alternate_renderings: they granted to them; they supplied them | rationale: Keeps the Greek lending language visible, even though the context may imply a broader giving or granting. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: they lent to them | footnote_text: Greek uses lending language here. This draft leaves that wording in place even though the larger scene suggests more than a temporary loan. | source_basis: lexical + context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 11:4

Greek: και ειπεν μωυσης ταδε λεγει κυριος περι μεσας νυκτας εγω εισπορευομαι εις μεσον αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said, "These things says the Lord: About midnight I enter into the midst of Egypt,"

Decision rows:
- greek_phrase: ἐγὼ εἰσπορεύομαι εἰς μέσον Αἰγύπτου | lemma: εἰσπορεύομαι | μέσος | Αἴγυπτος | morphology: present middle indicative 1 singular + prepositional phrase | chosen_rendering: I enter into the midst of Egypt | alternate_renderings: I go into Egypt's midst; I pass into the middle of Egypt | rationale: Preserves the inward movement of the Greek rather than changing it to a generic going forth. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: I enter into the midst of Egypt | footnote_text: Greek describes God as entering into Egypt's midst, emphasizing movement into the center of judgment. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 11:5

Greek: και τελευτησει παν πρωτοτοκον εν γη αιγυπτω απο πρωτοτοκου φαραω ος καθηται επι του θρονου και εως πρωτοτοκου της θεραπαινης της παρα τον μυλον και εως πρωτοτοκου παντος κτηνους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "and every firstborn in the land of Egypt will die, from Pharaoh's firstborn who sits on the throne to the firstborn of the female servant by the mill, and to the firstborn of every beast."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 11:6

Greek: και εσται κραυγη μεγαλη κατα πασαν γην αιγυπτου ητις τοιαυτη ου γεγονεν και τοιαυτη ουκετι προστεθησεται
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And there will be a great cry through all the land of Egypt, such as has never happened and will never be added again."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 11:7

Greek: και εν πασι τοις υιοις ισραηλ ου γρυξει κυων τη γλωσση αυτου απο ανθρωπου εως κτηνους οπως ειδης οσα παραδοξασει κυριος ανα μεσον των αιγυπτιων και του ισραηλ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "But among all the sons of Israel not a dog will snarl with its tongue, from man to beast, so that you may know how marvelously the Lord will distinguish between the Egyptians and Israel."

Decision rows:
- greek_phrase: οὐ γρύξει κύων τῇ γλώσσῃ αὐτοῦ / παραδοξάσει κύριος | lemma: γρύζω | κύων | παραδοξάζω | morphology: future active indicative 3 singular + nominative singular noun + future active indicative 3 singular | chosen_rendering: not a dog will snarl ... the Lord will distinguish marvelously | alternate_renderings: not a dog will move its tongue ... the Lord will make a striking distinction | rationale: Keeps both the vivid dog image and the extraordinary character of the distinction the Lord makes. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: not a dog will snarl ... distinguish between | footnote_text: Greek combines a vivid no-dog-will-snarl image with an extraordinary distinction made by the Lord between Egypt and Israel. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 11:8

Greek: και καταβησονται παντες οι παιδες σου ουτοι προς με και προκυνησουσιν με λεγοντες εξελθε συ και πας ο λαος σου ου συ αφηγη και μετα ταυτα εξελευσομαι εξηλθεν δε μωυσης απο φαραω μετα θυμου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And all these servants of yours will come down to me and bow to me, saying, Go out, you and all the people whom you lead, and after that I will go out." Then Moses went out from Pharaoh with anger.

Decision rows:
- greek_phrase: ὁ λαός σου οὗ σὺ ἀφηγῇ | lemma: λαός | ἀφηγέομαι | morphology: nominative singular noun phrase + present middle indicative 2 singular | chosen_rendering: the people whom you lead | alternate_renderings: the people over whom you preside; the people you guide | rationale: Lead is clearer English while still reflecting Moses' guiding role stated in the Greek. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 11:9

Greek: ειπεν δε κυριος προς μωυσην ουκ εισακουσεται υμων φαραω ινα πληθυνων πληθυνω μου τα σημεια και τα τερατα εν γη αιγυπτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, "Pharaoh will not listen to you, so that I may greatly multiply my signs and wonders in the land of Egypt."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 11:10

Greek: μωυσης δε και ααρων εποιησαν παντα τα σημεια και τα τερατα ταυτα εν γη αιγυπτω εναντιον φαραω εσκληρυνεν δε κυριος την καρδιαν φαραω και ουκ ηθελησεν εξαποστειλαι τους υιους ισραηλ εκ γης αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses and Aaron did all these signs and wonders in the land of Egypt before Pharaoh. But the Lord hardened Pharaoh's heart, and he was not willing to send the sons of Israel out of the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 12

### Exodus 12:1

Greek: ειπεν δε κυριος προς μωυσην και ααρων εν γη αιγυπτου λεγων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses and Aaron in the land of Egypt, saying,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:2

Greek: ο μην ουτος υμιν αρχη μηνων πρωτος εστιν υμιν εν τοις μησιν του ενιαυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "This month will be for you the beginning of months; it is first for you among the months of the year."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:3

Greek: λαλησον προς πασαν συναγωγην υιων ισραηλ λεγων τη δεκατη του μηνος τουτου λαβετωσαν εκαστος προβατον κατ' οικους πατριων εκαστος προβατον κατ' οικιαν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Speak to the whole assembly of the sons of Israel, saying, On the tenth day of this month let each take for themselves an animal from the flock according to ancestral houses, each an animal from the flock for the household."

Decision rows:
- greek_phrase: πρόβατον | lemma: πρόβατον | morphology: accusative singular noun | chosen_rendering: animal from the flock | alternate_renderings: lamb; sheep | rationale: Keeps the broader Greek flock-animal term visible before verse 5 narrows the acceptable source animals. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: animal from the flock | footnote_text: Greek uses a broader flock-animal word here. This draft keeps it broader in verse 3 before verse 5 specifies lambs or kids as acceptable sources. | source_basis: lexical + context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:4

Greek: εαν δε ολιγοστοι ωσιν οι εν τη οικια ωστε μη ικανους ειναι εις προβατον συλλημψεται μεθ' εαυτου τον γειτονα τον πλησιον αυτου κατα αριθμον ψυχων εκαστος το αρκουν αυτω συναριθμησεται εις προβατον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "But if those in the house are too few for an animal from the flock, he shall take along his neighbor nearest to him according to the number of persons. Each according to what is enough for him shall be counted toward the animal from the flock."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:5

Greek: προβατον τελειον αρσεν ενιαυσιον εσται υμιν απο των αρνων και των εριφων λημψεσθε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "The animal from the flock shall be for you unblemished, male, a year old. You shall take it from the lambs and from the kids."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:6

Greek: και εσται υμιν διατετηρημενον εως της τεσσαρεσκαιδεκατης του μηνος τουτου και σφαξουσιν αυτο παν το πληθος συναγωγης υιων ισραηλ προς εσπεραν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And it shall be kept by you until the fourteenth day of this month, and the whole multitude of the assembly of the sons of Israel shall slaughter it toward evening."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:7

Greek: και λημψονται απο του αιματος και θησουσιν επι των δυο σταθμων και επι την φλιαν εν τοις οικοις εν οις εαν φαγωσιν αυτα εν αυτοις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And they shall take some of the blood and put it on the two doorposts and on the lintel in the houses where they eat it."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:8

Greek: και φαγονται τα κρεα τη νυκτι ταυτη οπτα πυρι και αζυμα επι πικριδων εδονται
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And they shall eat the flesh on this night, roasted by fire, and unleavened bread. With bitter herbs they shall eat it."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:9

Greek: ουκ εδεσθε απ' αυτων ωμον ουδε ηψημενον εν υδατι αλλ' η οπτα πυρι κεφαλην συν τοις ποσιν και τοις ενδοσθιοις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "You shall not eat any of it raw or boiled in water, but only roasted by fire, the head with the feet and the inner parts."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:10

Greek: ουκ απολειψετε απ' αυτου εως πρωι και οστουν ου συντριψετε απ' αυτου τα δε καταλειπομενα απ' αυτου εως πρωι εν πυρι κατακαυσετε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "You shall not leave any of it until morning, and you shall not break a bone from it. But what remains of it until morning you shall burn with fire."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:11

Greek: ουτως δε φαγεσθε αυτο αι οσφυες υμων περιεζωσμεναι και τα υποδηματα εν τοις ποσιν υμων και αι βακτηριαι εν ταις χερσιν υμων και εδεσθε αυτο μετα σπουδης πασχα εστιν κυριω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And thus you shall eat it: your waists girded, your sandals on your feet, your staffs in your hands, and you shall eat it in haste. It is Passover to the Lord."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:12

Greek: και διελευσομαι εν γη αιγυπτω εν τη νυκτι ταυτη και παταξω παν πρωτοτοκον εν γη αιγυπτω απο ανθρωπου εως κτηνους και εν πασι τοις θεοις των αιγυπτιων ποιησω την εκδικησιν εγω κυριος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And I will pass through the land of Egypt on this night, and I will strike every firstborn in the land of Egypt, from man to beast, and on all the gods of the Egyptians I will execute vengeance. I am the Lord."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:13

Greek: και εσται το αιμα υμιν εν σημειω επι των οικιων εν αις υμεις εστε εκει και οψομαι το αιμα και σκεπασω υμας και ουκ εσται εν υμιν πληγη του εκτριβηναι οταν παιω εν γη αιγυπτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And the blood will be for you as a sign on the houses where you are, and I will see the blood and shelter you, and there shall not be among you a blow of destruction when I strike in the land of Egypt."

Decision rows:
- greek_phrase: σκεπάσω ὑμᾶς | lemma: σκεπάζω | morphology: future active indicative 1 singular | chosen_rendering: I will shelter you | alternate_renderings: I will protect you; I will cover you | rationale: Preserves the covering-sheltering verb in Greek instead of replacing it with pass over language. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: I will shelter you | footnote_text: Greek uses a sheltering or covering verb here. This draft preserves that wording instead of replacing it with a simplified pass-over expression. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:14

Greek: και εσται η ημερα υμιν αυτη μνημοσυνον και εορτασετε αυτην εορτην κυριω εις πασας τας γενεας υμων νομιμον αιωνιον εορτασετε αυτην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And this day will be for you a memorial, and you shall celebrate it as a feast to the Lord throughout your generations. As an age-lasting ordinance you shall celebrate it."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:15

Greek: επτα ημερας αζυμα εδεσθε απο δε της ημερας της πρωτης αφανιειτε ζυμην εκ των οικιων υμων πας ος αν φαγη ζυμην εξολεθρευθησεται η ψυχη εκεινη εξ ισραηλ απο της ημερας της πρωτης εως της ημερας της εβδομης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Seven days you shall eat unleavened bread, and from the first day you shall remove leaven from your houses. Everyone who eats leavened food, that person shall be destroyed from Israel, from the first day until the seventh day."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:16

Greek: και η ημερα η πρωτη κληθησεται αγια και η ημερα η εβδομη κλητη αγια εσται υμιν παν εργον λατρευτον ου ποιησετε εν αυταις πλην οσα ποιηθησεται παση ψυχη τουτο μονον ποιηθησεται υμιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And the first day shall be called holy, and the seventh day shall be a holy assembly for you. No work of service shall you do on them, except what will be made for every person; that alone may be done for you."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:17

Greek: και φυλαξεσθε την εντολην ταυτην εν γαρ τη ημερα ταυτη εξαξω την δυναμιν υμων εκ γης αιγυπτου και ποιησετε την ημεραν ταυτην εις γενεας υμων νομιμον αιωνιον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And you shall keep this command, for on this very day I will bring your hosts out of the land of Egypt, and you shall keep this day throughout your generations as an age-lasting ordinance."

Decision rows:
- greek_phrase: ἐξάξω τὴν δύναμιν ὑμῶν | lemma: ἐξάγω | δύναμις | morphology: future active indicative 1 singular + accusative singular noun phrase | chosen_rendering: I will bring your hosts out | alternate_renderings: I will bring out your force; I will bring out your company | rationale: Hosts keeps the collective organized-force sense of dynamis in this exodus setting. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: your hosts | footnote_text: Greek speaks of Israel in organized force or host language. This draft keeps that corporate, ordered sense visible in the exodus. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:18

Greek: εναρχομενου τη τεσσαρεσκαιδεκατη ημερα του μηνος του πρωτου αφ' εσπερας εδεσθε αζυμα εως ημερας μιας και εικαδος του μηνος εως εσπερας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Beginning on the fourteenth day of the first month at evening, you shall eat unleavened bread until evening of the twenty-first day of the month."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:19

Greek: επτα ημερας ζυμη ουχ ευρεθησεται εν ταις οικιαις υμων πας ος αν φαγη ζυμωτον εξολεθρευθησεται η ψυχη εκεινη εκ συναγωγης ισραηλ εν τε τοις γειωραις και αυτοχθοσιν της γης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "For seven days no leaven shall be found in your houses. Everyone who eats leavened food, that person shall be destroyed from the assembly of Israel, among both the newcomer and the native-born of the land."

Decision rows:
- greek_phrase: ἐν τε τοῖς γειώραις καὶ αὐτόχθοσιν τῆς γῆς | lemma: γειώρας | αὐτόχθων | morphology: dative plural noun pair | chosen_rendering: among both the newcomer and the native-born of the land | alternate_renderings: among resident aliens and natives; among immigrants and locals | rationale: Keeps the law applying across insider-outsider lines without collapsing the social distinction. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: newcomer and native-born | footnote_text: Greek explicitly includes both outsider and native-born within the same rule. This draft preserves that social breadth. | source_basis: lexical + social context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:20

Greek: παν ζυμωτον ουκ εδεσθε εν παντι δε κατοικητηριω υμων εδεσθε αζυμα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "You shall eat nothing leavened. In every dwelling of yours you shall eat unleavened bread."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:21

Greek: εκαλεσεν δε μωυσης πασαν γερουσιαν υιων ισραηλ και ειπεν προς αυτους απελθοντες λαβετε υμιν εαυτοις προβατον κατα συγγενειας υμων και θυσατε το πασχα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses called all the elders of the sons of Israel and said to them, "Go and take for yourselves an animal from the flock according to your families, and sacrifice the Passover."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:22

Greek: λημψεσθε δε δεσμην υσσωπου και βαψαντες απο του αιματος του παρα την θυραν καθιξετε της φλιας και επ' αμφοτερων των σταθμων απο του αιματος ο εστιν παρα την θυραν υμεις δε ουκ εξελευσεσθε εκαστος την θυραν του οικου αυτου εως πρωι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And you shall take a bunch of hyssop, and after dipping it in some of the blood by the door, you shall touch the lintel and both doorposts with some of the blood by the door. But none of you shall go out from the door of his house until morning."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:23

Greek: και παρελευσεται κυριος παταξαι τους αιγυπτιους και οψεται το αιμα επι της φλιας και επ' αμφοτερων των σταθμων και παρελευσεται κυριος την θυραν και ουκ αφησει τον ολεθρευοντα εισελθειν εις τας οικιας υμων παταξαι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And the Lord will pass by to strike the Egyptians, and he will see the blood on the lintel and on both doorposts, and the Lord will pass by the door and will not allow the destroyer to enter your houses to strike."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:24

Greek: και φυλαξεσθε το ρημα τουτο νομιμον σεαυτω και τοις υιοις σου εως αιωνος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And you shall keep this word as an ordinance for you and for your sons forever."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:25

Greek: εαν δε εισελθητε εις την γην ην αν δω κυριος υμιν καθοτι ελαλησεν φυλαξεσθε την λατρειαν ταυτην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And when you enter the land that the Lord will give you, just as he spoke, you shall keep this service."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:26

Greek: και εσται εαν λεγωσιν προς υμας οι υιοι υμων τις η λατρεια αυτη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And it shall be that when your sons say to you, What is this service?"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:27

Greek: και ερειτε αυτοις θυσια το πασχα τουτο κυριω ως εσκεπασεν τους οικους των υιων ισραηλ εν αιγυπτω ηνικα επαταξεν τους αιγυπτιους τους δε οικους ημων ερρυσατο και κυψας ο λαος προσεκυνησεν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "you shall say to them, This Passover is a sacrifice to the Lord, who sheltered the houses of the sons of Israel in Egypt when he struck the Egyptians but rescued our houses." And the people bowed low and worshiped.

Decision rows:
- greek_phrase: ὡς ἐσκέπασεν τοὺς οἴκους | lemma: σκεπάζω | οἶκος | morphology: aorist active indicative 3 singular + accusative plural noun | chosen_rendering: who sheltered the houses | alternate_renderings: who covered the houses; who defended the houses | rationale: Matches the sheltering language already used in verse 13 and keeps the Greek verbal link visible. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: sheltered the houses | footnote_text: The Greek repeats the sheltering verb from verse 13, linking the blood-sign with divine protection over Israelite homes. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:28

Greek: και απελθοντες εποιησαν οι υιοι ισραηλ καθα ενετειλατο κυριος τω μωυση και ααρων ουτως εποιησαν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the sons of Israel went away and did just as the Lord commanded Moses and Aaron; so they did.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:29

Greek: εγενηθη δε μεσουσης της νυκτος και κυριος επαταξεν παν πρωτοτοκον εν γη αιγυπτω απο πρωτοτοκου φαραω του καθημενου επι του θρονου εως πρωτοτοκου της αιχμαλωτιδος της εν τω λακκω και εως πρωτοτοκου παντος κτηνους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it happened at midnight that the Lord struck every firstborn in the land of Egypt, from Pharaoh's firstborn sitting on the throne to the firstborn of the captive woman in the pit, and every firstborn of beast.

Decision rows:
- greek_phrase: τῆς αἰχμαλωτίδος τῆς ἐν τῷ λάκκῳ | lemma: αἰχμαλωτίς | λάκκος | morphology: genitive singular noun phrase | chosen_rendering: the captive woman in the pit | alternate_renderings: the captive maid in the dungeon; the imprisoned woman in the pit | rationale: Retains the harsher captivity-and-pit image of the Greek rather than smoothing it. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: captive woman in the pit | footnote_text: Greek here speaks of a captive woman in a pit, a harsher image than some more familiar retellings. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:30

Greek: και αναστας φαραω νυκτος και παντες οι θεραποντες αυτου και παντες οι αιγυπτιοι και εγενηθη κραυγη μεγαλη εν παση γη αιγυπτω ου γαρ ην οικια εν η ουκ ην εν αυτη τεθνηκως
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh rose by night, and all his servants, and all the Egyptians, and there was a great cry in all the land of Egypt, for there was no house in which there was not one dead.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:31

Greek: και εκαλεσεν φαραω μωυσην και ααρων νυκτος και ειπεν αυτοις αναστητε και εξελθατε εκ του λαου μου και υμεις και οι υιοι ισραηλ βαδιζετε και λατρευσατε κυριω τω θεω υμων καθα λεγετε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh called Moses and Aaron by night and said to them, "Rise up and go out from my people, both you and the sons of Israel. Go and serve the Lord your God, just as you say."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:32

Greek: και τα προβατα και τους βοας υμων αναλαβοντες πορευεσθε ευλογησατε δε καμε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Take your sheep and your cattle and go. But bless me too."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:33

Greek: και κατεβιαζοντο οι αιγυπτιοι τον λαον σπουδη εκβαλειν αυτους εκ της γης ειπαν γαρ οτι παντες ημεις αποθνησκομεν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Egyptians pressed the people in haste to drive them out of the land, for they said, "We are all dying."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:34

Greek: ανελαβεν δε ο λαος το σταις προ του ζυμωθηναι τα φυραματα αυτων ενδεδεμενα εν τοις ιματιοις αυτων επι των ωμων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the people took the dough before it was leavened, their kneaded batches wrapped in their garments on their shoulders.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:35

Greek: οι δε υιοι ισραηλ εποιησαν καθα συνεταξεν αυτοις μωυσης και ητησαν παρα των αιγυπτιων σκευη αργυρα και χρυσα και ιματισμον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the sons of Israel did just as Moses instructed them, and they asked from the Egyptians silver and gold vessels and clothing.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:36

Greek: και κυριος εδωκεν την χαριν τω λαω αυτου εναντιον των αιγυπτιων και εχρησαν αυτοις και εσκυλευσαν τους αιγυπτιους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord gave his people favor in the sight of the Egyptians, and they lent to them, and they plundered the Egyptians.

Decision rows:
- greek_phrase: ἐχρήσαν αὐτοῖς / ἐσκύλευσαν τοὺς αἰγυπτίους | lemma: χράω | σκυλεύω | morphology: aorist active indicative 3 plural / aorist active indicative 3 plural | chosen_rendering: they lent to them / they plundered the Egyptians | alternate_renderings: they granted to them / they spoiled the Egyptians | rationale: Keeps both the lending language and the stronger plunder verb side by side in the Greek sequence. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: lent to them ... plundered the Egyptians | footnote_text: Greek keeps both actions: the Egyptians lend or grant to Israel, and Israel plunders Egypt. This draft preserves both verbs. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:37

Greek: απαραντες δε οι υιοι ισραηλ εκ ραμεσση εις σοκχωθα εις εξακοσιας χιλιαδας πεζων οι ανδρες πλην της αποσκευης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the sons of Israel set out from Rameses to Sokchoth, about six hundred thousand men on foot, besides the baggage.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:38

Greek: και επιμικτος πολυς συνανεβη αυτοις και προβατα και βοες και κτηνη πολλα σφοδρα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And a great mixed company went up with them, and sheep and cattle and very much livestock.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:39

Greek: και επεψαν το σταις ο εξηνεγκαν εξ αιγυπτου εγκρυφιας αζυμους ου γαρ εζυμωθη εξεβαλον γαρ αυτους οι αιγυπτιοι και ουκ ηδυνηθησαν επιμειναι ουδε επισιτισμον εποιησαν εαυτοις εις την οδον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they baked the dough they had brought out from Egypt into unleavened cakes, for it had not been leavened, because the Egyptians had driven them out and they were not able to delay, nor had they prepared provisions for themselves for the journey.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:40

Greek: η δε κατοικησις των υιων ισραηλ ην κατωκησαν εν γη αιγυπτω και εν γη χανααν ετη τετρακοσια τριακοντα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now the dwelling of the sons of Israel, during which they had dwelt in the land of Egypt and in the land of Canaan, was four hundred and thirty years.

Decision rows:
- greek_phrase: ἐν γῇ Αἰγύπτῳ καὶ ἐν γῇ Χαναάν | lemma: γῆ | Αἴγυπτος | Χαναάν | morphology: prepositional phrase chain | chosen_rendering: in the land of Egypt and in the land of Canaan | alternate_renderings: in Egypt and Canaan | rationale: Keeps the longer textual form present in the Greek tradition, which includes Canaan in the total sojourning span. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: in the land of Egypt and in the land of Canaan | footnote_text: The Greek text includes both Egypt and Canaan in the sojourning span, a broader wording than some later textual traditions preserve. | source_basis: textual + chronology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:41

Greek: και εγενετο μετα τα τετρακοσια τριακοντα ετη εξηλθεν πασα η δυναμις κυριου εκ γης αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it happened after the four hundred and thirty years that all the hosts of the Lord went out from the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:42

Greek: νυκτος προφυλακη εστιν τω κυριω ωστε εξαγαγειν αυτους εκ γης αιγυπτου εκεινη η νυξ αυτη προφυλακη κυριω ωστε πασι τοις υιοις ισραηλ ειναι εις γενεας αυτων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: It is a night-watch kept for the Lord, so as to bring them out from the land of Egypt. This same night is a watch kept for the Lord for all the sons of Israel throughout their generations.

Decision rows:
- greek_phrase: νυκτὸς προφυλακή | lemma: νύξ | προφυλακή | morphology: genitive singular noun + nominative singular noun | chosen_rendering: a night-watch kept for the Lord | alternate_renderings: a night of vigil for the Lord; a watch-night for the Lord | rationale: Preserves the vigilance-watch language rather than reducing it to a generic commemorative night. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: night-watch kept for the Lord | footnote_text: Greek emphasizes vigilance and watch-keeping. This draft keeps the night as a vigil, not merely a remembered anniversary. | source_basis: lexical + liturgy | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:43

Greek: ειπεν δε κυριος προς μωυσην και ααρων λεγων ουτος ο νομος του πασχα πας αλλογενης ουκ εδεται απ' αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses and Aaron, "This is the law of the Passover: no foreigner shall eat of it."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:44

Greek: και παν οικετην τινος η αργυρωνητον περιτεμεις αυτον και τοτε φαγεται απ' αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And every household slave or one bought with silver, you shall circumcise him, and then he shall eat of it."

Decision rows:
- greek_phrase: ἀργυρώνητον | lemma: ἀργυρώνητος | morphology: accusative singular adjective/substantive | chosen_rendering: one bought with silver | alternate_renderings: one purchased with money; money-bought slave | rationale: Keeps the silver-purchase wording explicit in the social-legal rule. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:45

Greek: παροικος η μισθωτος ουκ εδεται απ' αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "A settler or a hired worker shall not eat of it."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:46

Greek: εν οικια μια βρωθησεται και ουκ εξοισετε εκ της οικιας των κρεων εξω και οστουν ου συντριψετε απ' αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "In one house it shall be eaten, and you shall not carry any of the flesh out from the house, and you shall not break a bone from it."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:47

Greek: πασα συναγωγη υιων ισραηλ ποιησει αυτο
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "The whole assembly of the sons of Israel shall keep it."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:48

Greek: εαν δε τις προσελθη προς υμας προσηλυτος ποιησαι το πασχα κυριω περιτεμεις αυτου παν αρσενικον και τοτε προσελευσεται ποιησαι αυτο και εσται ωσπερ και ο αυτοχθων της γης πας απεριτμητος ουκ εδεται απ' αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And if any newcomer comes to you to keep Passover to the Lord, you shall circumcise every male of him, and then he shall come near to keep it, and he shall be like the native-born of the land. No uncircumcised person shall eat of it."

Decision rows:
- greek_phrase: προσήλυτος | lemma: προσήλυτος | morphology: nominative singular noun | chosen_rendering: newcomer | alternate_renderings: proselyte; resident alien; sojourner | rationale: Newcomer reads naturally while still marking someone who has attached himself to Israel from outside. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: newcomer | footnote_text: Greek proselytos marks an outsider who has attached himself to Israel. This draft uses newcomer as a readable public term while retaining inclusion by covenant sign. | source_basis: lexical + social context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:49

Greek: νομος εις εσται τω εγχωριω και τω προσελθοντι προσηλυτω εν υμιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "One law shall be for the native-born and for the newcomer who comes among you."

Decision rows:
- greek_phrase: νόμος εἷς | lemma: νόμος | εἷς | morphology: nominative singular noun phrase | chosen_rendering: one law | alternate_renderings: single law; one rule | rationale: Keeps the emphatic unity of legal standard for native-born and newcomer alike. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: one law | footnote_text: Greek stresses a single legal standard for native-born and newcomer alike. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:50

Greek: και εποιησαν οι υιοι ισραηλ καθα ενετειλατο κυριος τω μωυση και ααρων προς αυτους ουτως εποιησαν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the sons of Israel did just as the Lord commanded Moses and Aaron for them; so they did.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 12:51

Greek: και εγενετο εν τη ημερα εκεινη εξηγαγεν κυριος τους υιους ισραηλ εκ γης αιγυπτου συν δυναμει αυτων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it happened on that day that the Lord brought the sons of Israel out from the land of Egypt with their hosts.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 13

### Exodus 13:1

Greek: ειπεν δε κυριος προς μωυσην λεγων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, saying,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:2

Greek: αγιασον μοι παν πρωτοτοκον πρωτογενες διανοιγον πασαν μητραν εν τοις υιοις ισραηλ απο ανθρωπου εως κτηνους εμοι εστιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Set apart to me every firstborn, first issue, opening every womb among the sons of Israel, from man to beast. It is mine."

Decision rows:
- greek_phrase: πρωτογενές | lemma: πρωτογενής | morphology: accusative singular adjective/substantive | chosen_rendering: first issue | alternate_renderings: first produced; first offspring | rationale: Keeps the birth-origin nuance alongside firstborn instead of repeating the same English word twice. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:3

Greek: ειπεν δε μωυσης προς τον λαον μνημονευετε την ημεραν ταυτην εν η εξηλθατε εκ γης αιγυπτου εξ οικου δουλειας εν γαρ χειρι κραταια εξηγαγεν υμας κυριος εντευθεν και ου βρωθησεται ζυμη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses said to the people, "Remember this day on which you came out from the land of Egypt, out of the house of slavery, for with a mighty hand the Lord brought you out from there, and leaven shall not be eaten."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:4

Greek: εν γαρ τη σημερον υμεις εκπορευεσθε εν μηνι των νεων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "For on this day you are going out, in the month of new grain."

Decision rows:
- greek_phrase: ἐν μηνὶ τῶν νέων | lemma: μήν | νέος | morphology: dative singular noun phrase | chosen_rendering: in the month of new grain | alternate_renderings: in the month of new things; in the month of spring growth | rationale: Preserves the Greek newness language rather than importing the later Hebrew month name. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: month of new grain | footnote_text: Greek names this as the month of newness or new grain rather than using a later fixed month-name. | source_basis: lexical + calendar | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:5

Greek: και εσται ηνικα εαν εισαγαγη σε κυριος ο θεος σου εις την γην των χαναναιων και χετταιων και ευαιων και γεργεσαιων και αμορραιων και φερεζαιων και ιεβουσαιων ην ωμοσεν τοις πατρασιν σου δουναι σοι γην ρεουσαν γαλα και μελι και ποιησεις την λατρειαν ταυτην εν τω μηνι τουτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And it shall be that when the Lord your God brings you into the land of the Canaanites and Hittites and Hivites and Girgashites and Amorites and Perizzites and Jebusites, which he swore to your fathers to give you, a land flowing with milk and honey, you shall perform this service in this month."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:6

Greek: εξ ημερας εδεσθε αζυμα τη δε ημερα τη εβδομη εορτη κυριου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "For six days you shall eat unleavened bread, and on the seventh day there shall be a feast to the Lord."

Decision rows:
- greek_phrase: ἓξ ἡμέρας | lemma: ἕξ | ἡμέρα | morphology: accusative plural numeral phrase | chosen_rendering: for six days | alternate_renderings: six days | rationale: Keeps the Greek six-day wording visible, even though readers may expect seven from other textual traditions. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: for six days | footnote_text: The Greek text here says six days before the seventh-day feast, a notable difference from more familiar seven-day formulations. | source_basis: textual + chronology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:7

Greek: αζυμα εδεσθε τας επτα ημερας ουκ οφθησεται σοι ζυμωτον ουδε εσται σοι ζυμη εν πασιν τοις οριοις σου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "For seven days you shall eat unleavened bread. No leavened thing shall be seen among you, nor shall leaven be with you in all your borders."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:8

Greek: και αναγγελεις τω υιω σου εν τη ημερα εκεινη λεγων δια τουτο εποιησεν κυριος ο θεος μοι ως εξεπορευομην εξ αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And you shall tell your son on that day, saying, Because of this the Lord my God dealt with me when I was going out from Egypt."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:9

Greek: και εσται σοι σημειον επι της χειρος σου και μνημοσυνον προ οφθαλμων σου οπως αν γενηται ο νομος κυριου εν τω στοματι σου εν γαρ χειρι κραταια εξηγαγεν σε κυριος ο θεος εξ αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And it shall be for you as a sign on your hand and as a memorial before your eyes, so that the law of the Lord may be in your mouth, for with a mighty hand the Lord God brought you out from Egypt."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:10

Greek: και φυλαξεσθε τον νομον τουτον κατα καιρους ωρων αφ' ημερων εις ημερας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And you shall keep this law at the appointed times, from days to days."

Decision rows:
- greek_phrase: κατὰ καιροὺς ὡρῶν ἀφ᾽ ἡμερῶν εἰς ἡμέρας | lemma: καιρός | ὥρα | ἡμέρα | morphology: prepositional phrase sequence | chosen_rendering: at the appointed times, from days to days | alternate_renderings: at season-times from day to day; at fixed seasons from year to year | rationale: Keeps the layered time-language instead of smoothing it immediately to annual observance. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:11

Greek: και εσται ως αν εισαγαγη σε κυριος ο θεος σου εις την γην των χαναναιων ον τροπον ωμοσεν τοις πατρασιν σου και δωσει σοι αυτην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And it shall be that when the Lord your God brings you into the land of the Canaanites, just as he swore to your fathers, and gives it to you,"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:12

Greek: και αφελεις παν διανοιγον μητραν τα αρσενικα τω κυριω παν διανοιγον μητραν εκ των βουκολιων η εν τοις κτηνεσιν σου οσα εαν γενηται σοι τα αρσενικα αγιασεις τω κυριω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "you shall set apart to the Lord every opener of the womb, the males. Every opener of the womb from the herds or among your livestock, as many as come to you, the males you shall consecrate to the Lord."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:13

Greek: παν διανοιγον μητραν ονου αλλαξεις προβατω εαν δε μη αλλαξης λυτρωση αυτο παν πρωτοτοκον ανθρωπου των υιων σου λυτρωση
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Every opener of the womb of a donkey you shall exchange for a sheep, and if you do not exchange it, you shall redeem it. Every firstborn of man among your sons you shall redeem."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:14

Greek: εαν δε ερωτηση σε ο υιος σου μετα ταυτα λεγων τι τουτο και ερεις αυτω οτι εν χειρι κραταια εξηγαγεν ημας κυριος εκ γης αιγυπτου εξ οικου δουλειας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And if your son asks you after this, saying, What is this? you shall say to him, With a mighty hand the Lord brought us out from the land of Egypt, out of the house of slavery."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:15

Greek: ηνικα δε εσκληρυνεν φαραω εξαποστειλαι ημας απεκτεινεν παν πρωτοτοκον εν γη αιγυπτω απο πρωτοτοκων ανθρωπων εως πρωτοτοκων κτηνων δια τουτο εγω θυω τω κυριω παν διανοιγον μητραν τα αρσενικα και παν πρωτοτοκον των υιων μου λυτρωσομαι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And when Pharaoh hardened himself against sending us away, he killed every firstborn in the land of Egypt, from the firstborn of humans to the firstborn of beasts. Because of this I sacrifice to the Lord every opener of the womb, the males, and every firstborn of my sons I will redeem."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:16

Greek: και εσται εις σημειον επι της χειρος σου και ασαλευτον προ οφθαλμων σου εν γαρ χειρι κραταια εξηγαγεν σε κυριος εξ αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And it shall be as a sign on your hand and fixed before your eyes, for with a mighty hand the Lord brought you out from Egypt."

Decision rows:
- greek_phrase: ἀσάλευτον πρὸ ὀφθαλμῶν σου | lemma: ἀσάλευτος | ὀφθαλμός | morphology: accusative singular adjective phrase | chosen_rendering: fixed before your eyes | alternate_renderings: immovable before your eyes; steadfast before your eyes | rationale: Retains the Greek image of something set firmly before the eyes rather than importing later ritual terminology. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: fixed before your eyes | footnote_text: Greek speaks of something fixed or immovable before the eyes. This draft preserves that image rather than importing later ritual vocabulary. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:17

Greek: ως δε εξαπεστειλεν φαραω τον λαον ουχ ωδηγησεν αυτους ο θεος οδον γης φυλιστιιμ οτι εγγυς ην ειπεν γαρ ο θεος μηποτε μεταμεληση τω λαω ιδοντι πολεμον και αποστρεψη εις αιγυπτον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And when Pharaoh sent the people away, God did not lead them by the way of the land of the Philistines, because it was near. For God said, "Lest perhaps the people change their mind when they see war and turn back to Egypt."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:18

Greek: και εκυκλωσεν ο θεος τον λαον οδον την εις την ερημον εις την ερυθραν θαλασσαν πεμπτη δε γενεα ανεβησαν οι υιοι ισραηλ εκ γης αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: So God led the people around by the road to the wilderness, to the Red Sea. And in the fifth generation the sons of Israel went up out from the land of Egypt.

Decision rows:
- greek_phrase: πέμπτῃ δὲ γενεᾷ | lemma: πέμπτος | γενεά | morphology: dative singular noun phrase | chosen_rendering: in the fifth generation | alternate_renderings: in battle array; five in rank | rationale: Keeps the Greek genealogical wording, a notable difference from more familiar renderings. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: in the fifth generation | footnote_text: Greek here reads fifth generation, a striking difference from renderings that speak of military formation. | source_basis: textual + chronology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:19

Greek: και ελαβεν μωυσης τα οστα ιωσηφ μεθ' εαυτου ορκω γαρ ωρκισεν ιωσηφ τους υιους ισραηλ λεγων επισκοπη επισκεψεται υμας κυριος και συνανοισετε μου τα οστα εντευθεν μεθ' υμων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses took the bones of Joseph with him, for Joseph had solemnly bound the sons of Israel by oath, saying, God will surely visit you, and you shall carry my bones up from here with you.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:20

Greek: εξαραντες δε οι υιοι ισραηλ εκ σοκχωθ εστρατοπεδευσαν εν οθομ παρα την ερημον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the sons of Israel set out from Sokchoth and camped at Othom by the wilderness.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:21

Greek: ο δε θεος ηγειτο αυτων ημερας μεν εν στυλω νεφελης δειξαι αυτοις την οδον την δε νυκτα εν στυλω πυρος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And God led them, by day in a pillar of cloud to show them the way, and by night in a pillar of fire.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 13:22

Greek: ουκ εξελιπεν ο στυλος της νεφελης ημερας και ο στυλος του πυρος νυκτος εναντιον παντος του λαου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: The pillar of cloud by day did not fail, nor the pillar of fire by night, before all the people.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 14

### Exodus 14:1

Greek: και ελαλησεν κυριος προς μωυσην λεγων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord spoke to Moses, saying,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:2

Greek: λαλησον τοις υιοις ισραηλ και αποστρεψαντες στρατοπεδευσατωσαν απεναντι της επαυλεως ανα μεσον μαγδωλου και ανα μεσον της θαλασσης εξ εναντιας βεελσεπφων ενωπιον αυτων στρατοπεδευσεις επι της θαλασσης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Speak to the sons of Israel, and after turning back let them camp opposite the village, between Magdol and the sea. Opposite Beelsepphon, before them, you shall camp by the sea."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:3

Greek: και ερει φαραω τω λαω αυτου οι υιοι ισραηλ πλανωνται ουτοι εν τη γη συγκεκλεικεν γαρ αυτους η ερημος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And Pharaoh will say to his people, These sons of Israel are wandering in the land, for the wilderness has shut them in."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:4

Greek: εγω δε σκληρυνω την καρδιαν φαραω και καταδιωξεται οπισω αυτων και ενδοξασθησομαι εν φαραω και εν παση τη στρατια αυτου και γνωσονται παντες οι αιγυπτιοι οτι εγω ειμι κυριος και εποιησαν ουτως
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And I will harden Pharaoh's heart, and he will pursue after them, and I will be glorified in Pharaoh and in all his army, and all the Egyptians will know that I am the Lord." And they did so.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:5

Greek: και ανηγγελη τω βασιλει των αιγυπτιων οτι πεφευγεν ο λαος και μετεστραφη η καρδια φαραω και των θεραποντων αυτου επι τον λαον και ειπαν τι τουτο εποιησαμεν του εξαποστειλαι τους υιους ισραηλ του μη δουλευειν ημιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it was reported to the king of the Egyptians that the people had fled, and the heart of Pharaoh and of his servants was turned against the people, and they said, "Why have we done this, sending away the sons of Israel so that they need not serve us?"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:6

Greek: εζευξεν ουν φαραω τα αρματα αυτου και παντα τον λαον αυτου συναπηγαγεν μεθ' εαυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: So Pharaoh yoked his chariots, and he gathered all his people with himself.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:7

Greek: και λαβων εξακοσια αρματα εκλεκτα και πασαν την ιππον των αιγυπτιων και τριστατας επι παντων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And taking six hundred chosen chariots and all the cavalry of the Egyptians, he took commanders over all of them.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:8

Greek: και εσκληρυνεν κυριος την καρδιαν φαραω βασιλεως αιγυπτου και των θεραποντων αυτου και κατεδιωξεν οπισω των υιων ισραηλ οι δε υιοι ισραηλ εξεπορευοντο εν χειρι υψηλη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord hardened the heart of Pharaoh king of Egypt and of his servants, and he pursued after the sons of Israel. But the sons of Israel were going out with uplifted hand.

Decision rows:
- greek_phrase: ἐν χειρὶ ὑψηλῇ | lemma: χείρ | ὑψηλός | morphology: dative singular noun phrase | chosen_rendering: with uplifted hand | alternate_renderings: with a high hand; triumphantly | rationale: Preserves the embodied idiom without flattening it to an adverb. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: with uplifted hand | footnote_text: Greek uses a bodily idiom here. This draft keeps the image of Israel going out with raised or uplifted hand. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:9

Greek: και κατεδιωξαν οι αιγυπτιοι οπισω αυτων και ευροσαν αυτους παρεμβεβληκοτας παρα την θαλασσαν και πασα η ιππος και τα αρματα φαραω και οι ιππεις και η στρατια αυτου απεναντι της επαυλεως εξ εναντιας βεελσεπφων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Egyptians pursued after them and found them encamped by the sea, all Pharaoh's cavalry and chariots and horsemen and army, opposite the village, opposite Beelsepphon.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:10

Greek: και φαραω προσηγεν και αναβλεψαντες οι υιοι ισραηλ τοις οφθαλμοις ορωσιν και οι αιγυπτιοι εστρατοπεδευσαν οπισω αυτων και εφοβηθησαν σφοδρα ανεβοησαν δε οι υιοι ισραηλ προς κυριον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Pharaoh drew near, and the sons of Israel lifted up their eyes and saw: the Egyptians had camped behind them. And they feared greatly, and the sons of Israel cried out to the Lord.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:11

Greek: και ειπεν προς μωυσην παρα το μη υπαρχειν μνηματα εν γη αιγυπτω εξηγαγες ημας θανατωσαι εν τη ερημω τι τουτο εποιησας ημιν εξαγαγων εξ αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they said to Moses, "Was it because there were no tombs in the land of Egypt that you brought us out to die in the wilderness? Why have you done this to us, bringing us out from Egypt?"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:12

Greek: ου τουτο ην το ρημα ο ελαλησαμεν προς σε εν αιγυπτω λεγοντες παρες ημας οπως δουλευσωμεν τοις αιγυπτιοις κρεισσον γαρ ημας δουλευειν τοις αιγυπτιοις η αποθανειν εν τη ερημω ταυτη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Was this not the word we spoke to you in Egypt, saying, Leave us alone so that we may serve the Egyptians? For it would be better for us to serve the Egyptians than to die in this wilderness."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:13

Greek: ειπεν δε μωυσης προς τον λαον θαρσειτε στητε και ορατε την σωτηριαν την παρα του θεου ην ποιησει ημιν σημερον ον τροπον γαρ εωρακατε τους αιγυπτιους σημερον ου προσθησεσθε ετι ιδειν αυτους εις τον αιωνα χρονον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses said to the people, "Take courage. Stand and see the salvation from God that he will accomplish for us today. For in the way you have seen the Egyptians today, you shall never again see them through all time."

Decision rows:
- greek_phrase: τὴν σωτηρίαν τὴν παρὰ τοῦ θεοῦ | lemma: σωτηρία | παρά | θεός | morphology: accusative singular noun phrase | chosen_rendering: the salvation from God | alternate_renderings: the deliverance from God; the salvation of God | rationale: Keeps the explicit source phrase from God visible in the line. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:14

Greek: κυριος πολεμησει περι υμων και υμεις σιγησετε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "The Lord will fight for you, and you will be still."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:15

Greek: ειπεν δε κυριος προς μωυσην τι βοας προς με λαλησον τοις υιοις ισραηλ και αναζευξατωσαν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, "Why do you cry out to me? Speak to the sons of Israel, and let them break camp."

Decision rows:
- greek_phrase: ἀναζευξάτωσαν | lemma: ἀναζεύγνυμι | morphology: aorist active imperative 3 plural | chosen_rendering: let them break camp | alternate_renderings: let them set out; let them move on | rationale: Reflects camp-movement language more concretely than a generic proceed. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: let them break camp | footnote_text: Greek uses camp-movement language here, not merely a generic command to go forward. | source_basis: lexical + narrative | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:16

Greek: και συ επαρον τη ραβδω σου και εκτεινον την χειρα σου επι την θαλασσαν και ρηξον αυτην και εισελθατωσαν οι υιοι ισραηλ εις μεσον της θαλασσης κατα το ξηρον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And you, lift up your rod and stretch out your hand over the sea and split it, and let the sons of Israel enter into the midst of the sea on dry ground."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:17

Greek: και ιδου εγω σκληρυνω την καρδιαν φαραω και των αιγυπτιων παντων και εισελευσονται οπισω αυτων και ενδοξασθησομαι εν φαραω και εν παση τη στρατια αυτου και εν τοις αρμασιν και εν τοις ιπποις αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And behold, I am hardening the heart of Pharaoh and of all the Egyptians, and they will go in after them, and I will be glorified in Pharaoh and in all his army and in his chariots and horses."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:18

Greek: και γνωσονται παντες οι αιγυπτιοι οτι εγω ειμι κυριος ενδοξαζομενου μου εν φαραω και εν τοις αρμασιν και ιπποις αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And all the Egyptians will know that I am the Lord when I am glorified in Pharaoh and in his chariots and horses."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:19

Greek: εξηρεν δε ο αγγελος του θεου ο προπορευομενος της παρεμβολης των υιων ισραηλ και επορευθη εκ των οπισθεν εξηρεν δε και ο στυλος της νεφελης απο προσωπου αυτων και εστη εκ των οπισω αυτων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the messenger of God who went before the camp of the sons of Israel moved and went behind them, and the pillar of cloud also moved from before them and stood behind them.

Decision rows:
- greek_phrase: ὁ ἄγγελος τοῦ θεοῦ | lemma: ἄγγελος | θεός | morphology: nominative singular noun phrase | chosen_rendering: the messenger of God | alternate_renderings: the angel of God | rationale: Keeps the broader sense of angelos as messenger without foreclosing how readers construe the figure. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: messenger of God | footnote_text: Greek angelos can mean angel or messenger. This draft keeps the broader messenger sense open. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:20

Greek: και εισηλθεν ανα μεσον της παρεμβολης των αιγυπτιων και ανα μεσον της παρεμβολης ισραηλ και εστη και εγενετο σκοτος και γνοφος και διηλθεν η νυξ και ου συνεμιξαν αλληλοις ολην την νυκτα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it came between the camp of the Egyptians and the camp of Israel, and there it stood. And there came darkness and gloom, and the night passed, and they did not come near one another through all the night.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:21

Greek: εξετεινεν δε μωυσης την χειρα επι την θαλασσαν και υπηγαγεν κυριος την θαλασσαν εν ανεμω νοτω βιαιω ολην την νυκτα και εποιησεν την θαλασσαν ξηραν και εσχισθη το υδωρ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses stretched out his hand over the sea, and the Lord drew back the sea by a violent south wind all night, and he made the sea dry, and the water was split.

Decision rows:
- greek_phrase: ἐν ἀνέμῳ νότῳ βιαίῳ | lemma: ἄνεμος | νότος | βίαιος | morphology: dative singular noun phrase | chosen_rendering: by a violent south wind | alternate_renderings: by a strong south wind; by a violent southern wind | rationale: Preserves the Greek south-wind wording rather than harmonizing to east wind from another textual tradition. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: violent south wind | footnote_text: Greek specifies a south wind here, not an east wind. This draft preserves the Greek directional wording. | source_basis: textual + lexical | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:22

Greek: και εισηλθον οι υιοι ισραηλ εις μεσον της θαλασσης κατα το ξηρον και το υδωρ αυτοις τειχος εκ δεξιων και τειχος εξ ευωνυμων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the sons of Israel entered into the midst of the sea on dry ground, and the water was a wall for them on the right and a wall on the left.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:23

Greek: κατεδιωξαν δε οι αιγυπτιοι και εισηλθον οπισω αυτων πασα η ιππος φαραω και τα αρματα και οι αναβαται εις μεσον της θαλασσης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Egyptians pursued and went in after them into the midst of the sea, all Pharaoh's horses, chariots, and riders.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:24

Greek: εγενηθη δε εν τη φυλακη τη εωθινη και επεβλεψεν κυριος επι την παρεμβολην των αιγυπτιων εν στυλω πυρος και νεφελης και συνεταραξεν την παρεμβολην των αιγυπτιων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And in the morning watch the Lord looked upon the camp of the Egyptians through the pillar of fire and cloud, and he threw the camp of the Egyptians into confusion.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:25

Greek: και συνεδησεν τους αξονας των αρματων αυτων και ηγαγεν αυτους μετα βιας και ειπαν οι αιγυπτιοι φυγωμεν απο προσωπου ισραηλ ο γαρ κυριος πολεμει περι αυτων τους αιγυπτιους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he bound the axles of their chariots and made them drive with difficulty. And the Egyptians said, "Let us flee from before Israel, for the Lord fights for them against the Egyptians."

Decision rows:
- greek_phrase: συνεδήσεν τοὺς ἄξονας | lemma: συνδέω | ἄξων | morphology: aorist active indicative 3 singular + accusative plural noun | chosen_rendering: he bound the axles | alternate_renderings: he jammed the axles; he fastened the axles | rationale: Keeps the concrete mechanical action in the Greek account. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: bound the axles | footnote_text: Greek gives a concrete image of God binding or jamming the chariot axles. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:26

Greek: ειπεν δε κυριος προς μωυσην εκτεινον την χειρα σου επι την θαλασσαν και αποκαταστητω το υδωρ και επικαλυψατω τους αιγυπτιους επι τε τα αρματα και τους αναβατας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, "Stretch out your hand over the sea, and let the water return and cover the Egyptians, both the chariots and the riders."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:27

Greek: εξετεινεν δε μωυσης την χειρα επι την θαλασσαν και απεκατεστη το υδωρ προς ημεραν επι χωρας οι δε αιγυπτιοι εφυγον υπο το υδωρ και εξετιναξεν κυριος τους αιγυπτιους μεσον της θαλασσης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses stretched out his hand over the sea, and the water returned toward day to its place. And the Egyptians fled down into the water, and the Lord shook the Egyptians off into the midst of the sea.

Decision rows:
- greek_phrase: ἐξετίναξεν κύριος τοὺς αἰγυπτίους | lemma: ἐκτινάσσω | Αἰγύπτιος | morphology: aorist active indicative 3 singular + accusative plural noun | chosen_rendering: the Lord shook the Egyptians off | alternate_renderings: the Lord cast off the Egyptians; the Lord flung the Egyptians away | rationale: Preserves the vivid shaking-off image of the Greek. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: shook the Egyptians off | footnote_text: Greek uses a vivid shake-off verb here. This draft keeps that forceful image visible. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:28

Greek: και επαναστραφεν το υδωρ εκαλυψεν τα αρματα και τους αναβατας και πασαν την δυναμιν φαραω τους εισπεπορευμενους οπισω αυτων εις την θαλασσαν και ου κατελειφθη εξ αυτων ουδε εις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the water returned and covered the chariots and the riders and all Pharaoh's force, those who had gone in after them into the sea. Not even one of them was left.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:29

Greek: οι δε υιοι ισραηλ επορευθησαν δια ξηρας εν μεσω της θαλασσης το δε υδωρ αυτοις τειχος εκ δεξιων και τειχος εξ ευωνυμων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But the sons of Israel traveled through dry ground in the midst of the sea, and the water was a wall for them on the right and on the left.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:30

Greek: και ερρυσατο κυριος τον ισραηλ εν τη ημερα εκεινη εκ χειρος των αιγυπτιων και ειδεν ισραηλ τους αιγυπτιους τεθνηκοτας παρα το χειλος της θαλασσης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Thus the Lord rescued Israel on that day from the hand of the Egyptians, and Israel saw the Egyptians lying dead by the shore of the sea.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 14:31

Greek: ειδεν δε ισραηλ την χειρα την μεγαλην α εποιησεν κυριος τοις αιγυπτιοις εφοβηθη δε ο λαος τον κυριον και επιστευσαν τω θεω και μωυση τω θεραποντι αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Israel saw the great hand, the things the Lord had done against the Egyptians, and the people feared the Lord, and they believed God and Moses his attendant.

Decision rows:
- greek_phrase: Μωϋσῇ τῷ θεράποντι αὐτοῦ | lemma: θεράπων | morphology: dative singular noun | chosen_rendering: Moses his attendant | alternate_renderings: Moses his servant; Moses his minister | rationale: Keeps therapon distinct from the more common slave-servant wording and suggests honored service. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: Moses his attendant | footnote_text: Greek uses therapon, a distinct service term with a more honored tone than ordinary slave language. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 15

### Exodus 15:1

Greek: τοτε ησεν μωυσης και οι υιοι ισραηλ την ωδην ταυτην τω θεω και ειπαν λεγοντες ασωμεν τω κυριω ενδοξως γαρ δεδοξασται ιππον και αναβατην ερριψεν εις θαλασσαν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses and the sons of Israel sang this song to God and said, "Let us sing to the Lord, for he has been glorified gloriously; horse and rider he has thrown into the sea."

Decision rows:
- greek_phrase: ἐνδόξως γὰρ δεδόξασται | lemma: ἐνδόξως | δοξάζω | morphology: adverb + perfect passive indicative 3 singular | chosen_rendering: he has been glorified gloriously | alternate_renderings: he is greatly glorified; he has glorified himself gloriously | rationale: Keeps the doubled glory-language of the Greek song rather than reducing it to a single intensifier. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: glorified gloriously | footnote_text: Greek doubles the glory-language here. This draft keeps the repetition visible instead of reducing it to a single intensifier. | source_basis: lexical + poetry | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:2

Greek: βοηθος και σκεπαστης εγενετο μοι εις σωτηριαν ουτος μου θεος και δοξασω αυτον θεος του πατρος μου και υψωσω αυτον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "He became for me a helper and a shelter for salvation. This is my God, and I will glorify him, God of my father, and I will exalt him."

Decision rows:
- greek_phrase: βοηθὸς καὶ σκεπαστὴς | lemma: βοηθός | σκεπαστής | morphology: nominative singular noun pair | chosen_rendering: helper and shelter | alternate_renderings: helper and protector; helper and coverer | rationale: Preserves the paired rescue nouns and keeps the shelter motif visible. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: helper and a shelter | footnote_text: Greek pairs rescue images here: help and sheltering cover. This draft preserves both motifs. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:3

Greek: κυριος συντριβων πολεμους κυριος ονομα αυτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "The Lord shattering wars; the Lord is his name."

Decision rows:
- greek_phrase: κύριος συντρίβων πολέμους | lemma: κύριος | συντρίβω | πόλεμος | morphology: nominative singular noun phrase + present active participle | chosen_rendering: The Lord shattering wars | alternate_renderings: The Lord breaking wars; the Lord bringing wars to nothing | rationale: Greek here speaks of God crushing wars, a notable difference from the more familiar man-of-war wording. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: The Lord shattering wars | footnote_text: The Greek line says the Lord shatters wars, a notable difference from traditions that describe the Lord as a warrior. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:4

Greek: αρματα φαραω και την δυναμιν αυτου ερριψεν εις θαλασσαν επιλεκτους αναβατας τριστατας κατεποντισεν εν ερυθρα θαλασση
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Pharaoh's chariots and his force he threw into the sea; chosen mounted officers he sank in the Red Sea."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:5

Greek: ποντω εκαλυψεν αυτους κατεδυσαν εις βυθον ωσει λιθος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "The deep covered them; they went down into the depth like a stone."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:6

Greek: η δεξια σου κυριε δεδοξασται εν ισχυι η δεξια σου χειρ κυριε εθραυσεν εχθρους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Your right hand, O Lord, has been glorified in strength; your right hand, O Lord, shattered enemies."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:7

Greek: και τω πληθει της δοξης σου συνετριψας τους υπεναντιους απεστειλας την οργην σου και κατεφαγεν αυτους ως καλαμην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And in the abundance of your glory you crushed the adversaries; you sent out your wrath, and it devoured them like stubble."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:8

Greek: και δια πνευματος του θυμου σου διεστη το υδωρ επαγη ωσει τειχος τα υδατα επαγη τα κυματα εν μεσω της θαλασσης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And by the breath of your wrath the water stood apart; the waters congealed like a wall; the waves congealed in the midst of the sea."

Decision rows:
- greek_phrase: δια πνεύματος τοῦ θυμοῦ σου / ἐπάγη | lemma: πνεῦμα | θυμός | πήγνυμι | morphology: genitive singular noun phrase / aorist passive indicative 3 singular | chosen_rendering: by the breath of your wrath ... congealed | alternate_renderings: by the wind of your fury ... froze; by the blast of your anger ... stiffened | rationale: Keeps both the bodily wrath-breath image and the congealing language of the sea. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: breath of your wrath ... congealed | footnote_text: Greek combines wrath-breath imagery with the sea becoming congealed or fixed. This draft keeps both poetic images. | source_basis: lexical + poetry | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:9

Greek: ειπεν ο εχθρος διωξας καταλημψομαι μεριω σκυλα εμπλησω ψυχην μου ανελω τη μαχαιρη μου κυριευσει η χειρ μου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "The enemy said, I will pursue, I will overtake, I will divide spoil, I will fill my soul, I will kill with my sword, my hand will rule."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:10

Greek: απεστειλας το πνευμα σου εκαλυψεν αυτους θαλασσα εδυσαν ωσει μολιβος εν υδατι σφοδρω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "You sent out your wind, the sea covered them; they sank like lead in mighty water."

Decision rows:
- greek_phrase: ἀπέστειλας τὸ πνεῦμά σου | lemma: ἀποστέλλω | πνεῦμα | morphology: aorist active indicative 2 singular + accusative singular noun | chosen_rendering: You sent out your wind | alternate_renderings: You sent out your spirit; You sent out your breath | rationale: In context the sea-response favors wind, while still echoing the earlier breath imagery. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: You sent out your wind | footnote_text: Greek pneuma can mean wind, breath, or spirit. In this sea-crossing context this draft chooses wind. | source_basis: lexical + context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:11

Greek: τις ομοιος σοι εν θεοις κυριε τις ομοιος σοι δεδοξασμενος εν αγιοις θαυμαστος εν δοξαις ποιων τερατα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Who is like you among gods, O Lord? Who is like you, glorified among holy ones, wondrous in glories, doing wonders?"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:12

Greek: εξετεινας την δεξιαν σου κατεπιεν αυτους γη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "You stretched out your right hand; earth swallowed them."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:13

Greek: ωδηγησας τη δικαιοσυνη σου τον λαον σου τουτον ον ελυτρωσω παρεκαλεσας τη ισχυι σου εις καταλυμα αγιον σου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "You guided in your righteousness this people whom you redeemed; by your strength you led them onward to your holy resting-place."

Decision rows:
- greek_phrase: παρεκάλεσας τῇ ἰσχύι σου εἰς κατάλυμα ἅγιόν σου | lemma: παρακαλέω | ἰσχύς | κατάλυμα | morphology: aorist active indicative 2 singular + dative singular noun phrase | chosen_rendering: by your strength you led them onward to your holy resting-place | alternate_renderings: you comforted them into your holy lodging-place; you called them to your holy resting-place | rationale: Aims to keep the movement toward holy lodging-rest without flattening the unusual verb. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:14

Greek: ηκουσαν εθνη και ωργισθησαν ωδινες ελαβον κατοικουντας φυλιστιιμ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Nations heard and grew angry; pangs seized those dwelling among the Philistines."

Decision rows:
- greek_phrase: ὤργισθησαν | lemma: ὀργίζω | morphology: aorist passive indicative 3 plural | chosen_rendering: grew angry | alternate_renderings: were enraged; were disturbed | rationale: Greek says the nations became angry, a sharper reaction than simple fear. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: grew angry | footnote_text: Greek says the nations became angry, not merely afraid. This gives the reaction a more hostile edge. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:15

Greek: τοτε εσπευσαν ηγεμονες εδωμ και αρχοντες μωαβιτων ελαβεν αυτους τρομος ετακησαν παντες οι κατοικουντες χανααν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Then the chiefs of Edom hastened; the rulers of the Moabites, trembling took hold of them; all the inhabitants of Canaan melted away."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:16

Greek: επιπεσοι επ' αυτους φοβος και τρομος μεγεθει βραχιονος σου απολιθωθητωσαν εως αν παρελθη ο λαος σου κυριε εως αν παρελθη ο λαος σου ουτος ον εκτησω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Let fear and trembling fall upon them; by the greatness of your arm let them turn to stone, until your people pass over, O Lord, until this people passes over, whom you acquired."

Decision rows:
- greek_phrase: ἀπολιθωθήτωσαν | lemma: ἀπολιθόω | morphology: aorist passive imperative 3 plural | chosen_rendering: let them turn to stone | alternate_renderings: let them become stone; let them be petrified | rationale: Keeps the stone-image directly in the English line. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: turn to stone | footnote_text: Greek uses a stone-image for the stunned nations. This draft keeps the metaphor explicit. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:17

Greek: εισαγαγων καταφυτευσον αυτους εις ορος κληρονομιας σου εις ετοιμον κατοικητηριον σου ο κατειργασω κυριε αγιασμα κυριε ο ητοιμασαν αι χειρες σου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Bring them in and plant them on the mountain of your inheritance, in your prepared dwelling-place, which you prepared, O Lord, the sanctuary, O Lord, which your hands made ready."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:18

Greek: κυριος βασιλευων τον αιωνα και επ' αιωνα και ετι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "The Lord reigns forever and beyond."

Decision rows:
- greek_phrase: τὸν αἰῶνα καὶ ἐπ᾽ αἰῶνα καὶ ἔτι | lemma: αἰών | ἔτι | morphology: accusative singular noun phrase + adverb | chosen_rendering: forever and beyond | alternate_renderings: forever and ever and still; for the age and beyond the age | rationale: Preserves the piling-up of endless duration without wooden repetition. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: forever and beyond | footnote_text: Greek stacks age-language and adds still more. This draft keeps the sense of unending reign without wooden repetition. | source_basis: lexical + poetry | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:19

Greek: οτι εισηλθεν ιππος φαραω συν αρμασιν και αναβαταις εις θαλασσαν και επηγαγεν επ' αυτους κυριος το υδωρ της θαλασσης οι δε υιοι ισραηλ επορευθησαν δια ξηρας εν μεσω της θαλασσης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: For Pharaoh's horse went in with chariots and riders into the sea, and the Lord brought the water of the sea upon them. But the sons of Israel traveled on dry ground through the midst of the sea.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:20

Greek: λαβουσα δε μαριαμ η προφητις η αδελφη ααρων το τυμπανον εν τη χειρι αυτης και εξηλθοσαν πασαι αι γυναικες οπισω αυτης μετα τυμπανων και χορων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Miriam the prophetess, the sister of Aaron, took the timbrel in her hand, and all the women went out after her with timbrels and dances.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:21

Greek: εξηρχεν δε αυτων μαριαμ λεγουσα ασωμεν τω κυριω ενδοξως γαρ δεδοξασται ιππον και αναβατην ερριψεν εις θαλασσαν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Miriam led them, saying, "Let us sing to the Lord, for he has been glorified gloriously; horse and rider he has thrown into the sea."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:22

Greek: εξηρεν δε μωυσης τους υιους ισραηλ απο θαλασσης ερυθρας και ηγαγεν αυτους εις την ερημον σουρ και επορευοντο τρεις ημερας εν τη ερημω και ουχ ηυρισκον υδωρ ωστε πιειν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses moved the sons of Israel away from the Red Sea and led them into the wilderness of Shur. And they went three days in the wilderness and found no water to drink.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:23

Greek: ηλθον δε εις μερρα και ουκ ηδυναντο πιειν εκ μερρας πικρον γαρ ην δια τουτο επωνομασθη το ονομα του τοπου εκεινου πικρια
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they came to Merra, and they were not able to drink from Merra, for it was bitter. Because of this the name of that place was called Bitterness.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:24

Greek: και διεγογγυζεν ο λαος επι μωυσην λεγοντες τι πιομεθα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the people grumbled against Moses, saying, "What will we drink?"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:25

Greek: εβοησεν δε μωυσης προς κυριον και εδειξεν αυτω κυριος ξυλον και ενεβαλεν αυτο εις το υδωρ και εγλυκανθη το υδωρ εκει εθετο αυτω δικαιωματα και κρισεις και εκει επειρασεν αυτον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses cried out to the Lord, and the Lord showed him a piece of wood, and he cast it into the water, and the water was sweetened. There he set for him ordinances and judgments, and there he tested him.

Decision rows:
- greek_phrase: ξύλον ... ἔθετο αὐτῷ ... ἐπείρασεν αὐτόν | lemma: ξύλον | τίθημι | πειράζω | morphology: accusative singular noun / aorist active indicative 3 singular / aorist active indicative 3 singular | chosen_rendering: a piece of wood ... he set for him ... he tested him | alternate_renderings: wood ... set for them ... tested them | rationale: Keeps both the wood-image and the singular pronouns, which may treat Israel as a collective singular. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: piece of wood ... tested him | footnote_text: Greek specifies wood and then uses singular pronouns for the people, likely treating Israel as a collective singular. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:26

Greek: και ειπεν εαν ακοη ακουσης της φωνης κυριου του θεου σου και τα αρεστα εναντιον αυτου ποιησης και ενωτιση ταις εντολαις αυτου και φυλαξης παντα τα δικαιωματα αυτου πασαν νοσον ην επηγαγον τοις αιγυπτιοις ουκ επαξω επι σε εγω γαρ ειμι κυριος ο ιωμενος σε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he said, "If in hearing you hear the voice of the Lord your God and do the things pleasing before him and give ear to his commands and keep all his ordinances, every sickness that I brought upon the Egyptians I will not bring upon you, for I am the Lord who heals you."

Decision rows:
- greek_phrase: ἐγὼ γάρ εἰμι κύριος ὁ ἰώμενός σε | lemma: κύριος | ἰάομαι | morphology: nominative singular noun phrase + present middle participle | chosen_rendering: I am the Lord who heals you | alternate_renderings: I am the Lord your healer; I am the Lord healing you | rationale: Keeps the divine self-identification in direct healing language. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: the Lord who heals you | footnote_text: Greek presents healing as part of the divine self-description here, not merely a promised action. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 15:27

Greek: και ηλθοσαν εις αιλιμ και ησαν εκει δωδεκα πηγαι υδατων και εβδομηκοντα στελεχη φοινικων παρενεβαλον δε εκει παρα τα υδατα
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they came to Elim, and there were there twelve springs of water and seventy trunks of palm trees, and they camped there by the waters.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 16

### Exodus 16:1

Greek: απηραν δε εξ αιλιμ και ηλθοσαν πασα συναγωγη υιων ισραηλ εις την ερημον σιν ο εστιν ανα μεσον αιλιμ και ανα μεσον σινα τη δε πεντεκαιδεκατη ημερα τω μηνι τω δευτερω εξεληλυθοτων αυτων εκ γης αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they set out from Elim, and the whole assembly of the sons of Israel came into the wilderness of Sin, which is between Elim and Sinai, on the fifteenth day of the second month after they had come out from the land of Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:2

Greek: διεγογγυζεν πασα συναγωγη υιων ισραηλ επι μωυσην και ααρων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the whole assembly of the sons of Israel grumbled against Moses and Aaron,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:3

Greek: και ειπαν προς αυτους οι υιοι ισραηλ οφελον απεθανομεν πληγεντες υπο κυριου εν γη αιγυπτω οταν εκαθισαμεν επι των λεβητων των κρεων και ησθιομεν αρτους εις πλησμονην οτι εξηγαγετε ημας εις την ερημον ταυτην αποκτειναι πασαν την συναγωγην ταυτην εν λιμω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: and the sons of Israel said to them, "If only we had died, struck by the Lord in the land of Egypt, when we sat by the pots of meat and ate bread to fullness. But you have brought us out into this wilderness to kill this whole assembly with hunger."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:4

Greek: ειπεν δε κυριος προς μωυσην ιδου εγω υω υμιν αρτους εκ του ουρανου και εξελευσεται ο λαος και συλλεξουσιν το της ημερας εις ημεραν οπως πειρασω αυτους ει πορευσονται τω νομω μου η ου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, "Behold, I am raining bread for you from heaven, and the people will go out and gather what is needed for the day, day by day, so that I may test them whether they will walk in my law or not."

Decision rows:
- greek_phrase: ἰδοὺ ἐγὼ ὕω ὑμῖν ἄρτους | lemma: ὕω | ἄρτος | morphology: present active indicative 1 singular + accusative plural noun | chosen_rendering: I am raining bread for you | alternate_renderings: I will rain bread for you; I rain loaves for you | rationale: Keeps the weather-verb vivid in the present line of divine action. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: I am raining bread for you | footnote_text: Greek uses a weather-verb here. This draft keeps the image of bread raining from heaven. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:5

Greek: και εσται τη ημερα τη εκτη και ετοιμασουσιν ο εαν εισενεγκωσιν και εσται διπλουν ο εαν συναγαγωσιν το καθ' ημεραν εις ημεραν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And it shall be on the sixth day that they will prepare what they bring in, and it will be double what they gather, day by day."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:6

Greek: και ειπεν μωυσης και ααρων προς πασαν συναγωγην υιων ισραηλ εσπερας γνωσεσθε οτι κυριος εξηγαγεν υμας εκ γης αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses and Aaron said to the whole assembly of the sons of Israel, "At evening you will know that the Lord has brought you out from the land of Egypt,"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:7

Greek: και πρωι οψεσθε την δοξαν κυριου εν τω εισακουσαι τον γογγυσμον υμων επι τω θεω ημεις δε τι εσμεν οτι διαγογγυζετε καθ' ημων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "and in the morning you will see the glory of the Lord, because he has heard your grumbling against God. And what are we, that you grumble against us?"

Decision rows:
- greek_phrase: ἐπὶ τῷ θεῷ | lemma: θεός | morphology: dative singular noun with preposition | chosen_rendering: against God | alternate_renderings: before God; toward God | rationale: Keeps the text explicitly naming God rather than shifting to Lord in this accusation line. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:8

Greek: και ειπεν μωυσης εν τω διδοναι κυριον υμιν εσπερας κρεα φαγειν και αρτους το πρωι εις πλησμονην δια το εισακουσαι κυριον τον γογγυσμον υμων ον υμεις διαγογγυζετε καθ' ημων ημεις δε τι εσμεν ου γαρ καθ' ημων ο γογγυσμος υμων εστιν αλλ' η κατα του θεου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said, "This will be when the Lord gives you meat to eat in the evening and bread in the morning to fullness, because the Lord has heard your grumbling that you grumble against us. And what are we? Your grumbling is not against us but against God."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:9

Greek: ειπεν δε μωυσης προς ααρων ειπον παση συναγωγη υιων ισραηλ προσελθατε εναντιον του θεου εισακηκοεν γαρ υμων τον γογγυσμον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses said to Aaron, "Tell the whole assembly of the sons of Israel, Come near before God, for he has heard your grumbling."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:10

Greek: ηνικα δε ελαλει ααρων παση συναγωγη υιων ισραηλ και επεστραφησαν εις την ερημον και η δοξα κυριου ωφθη εν νεφελη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And when Aaron spoke to the whole assembly of the sons of Israel, they turned toward the wilderness, and the glory of the Lord appeared in a cloud.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:11

Greek: και ελαλησεν κυριος προς μωυσην λεγων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord spoke to Moses, saying,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:12

Greek: εισακηκοα τον γογγυσμον των υιων ισραηλ λαλησον προς αυτους λεγων το προς εσπεραν εδεσθε κρεα και το πρωι πλησθησεσθε αρτων και γνωσεσθε οτι εγω κυριος ο θεος υμων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "I have heard the grumbling of the sons of Israel. Speak to them, saying, Toward evening you shall eat meat, and in the morning you shall be filled with bread, and you shall know that I am the Lord your God."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:13

Greek: εγενετο δε εσπερα και ανεβη ορτυγομητρα και εκαλυψεν την παρεμβολην το πρωι εγενετο καταπαυομενης της δροσου κυκλω της παρεμβολης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it happened at evening that quail came up and covered the camp, and in the morning, as the dew was settling around the camp,

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:14

Greek: και ιδου επι προσωπον της ερημου λεπτον ωσει κοριον λευκον ωσει παγος επι της γης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: behold, over the face of the wilderness was a fine thing, like coriander seed, white like frost upon the earth.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:15

Greek: ιδοντες δε αυτο οι υιοι ισραηλ ειπαν ετερος τω ετερω τι εστιν τουτο ου γαρ ηδεισαν τι ην ειπεν δε μωυσης προς αυτους ουτος ο αρτος ον εδωκεν κυριος υμιν φαγειν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And when the sons of Israel saw it, they said one to another, "What is this?" for they did not know what it was. Then Moses said to them, "This is the bread that the Lord has given you to eat."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:16

Greek: τουτο το ρημα ο συνεταξεν κυριος συναγαγετε απ' αυτου εκαστος εις τους καθηκοντας γομορ κατα κεφαλην κατα αριθμον ψυχων υμων εκαστος συν τοις συσκηνιοις υμων συλλεξατε
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "This is the word the Lord has commanded: Gather from it, each for those assigned to him, a gomor per head, according to the number of your persons. Each with those in your tent shall gather it."

Decision rows:
- greek_phrase: γόμορ | lemma: γόμορ | morphology: indeclinable measure noun | chosen_rendering: gomor | alternate_renderings: omer; homer | rationale: Keeps the Greek measure-form visible instead of normalizing to another traditional form. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: gomor | footnote_text: Greek uses gomor here as the named measure. This draft keeps the Greek form instead of replacing it with a more familiar traditional spelling. | source_basis: lexical + measurement | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:17

Greek: εποιησαν δε ουτως οι υιοι ισραηλ και συνελεξαν ο το πολυ και ο το ελαττον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the sons of Israel did so, and some gathered much and some little.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:18

Greek: και μετρησαντες τω γομορ ουκ επλεονασεν ο το πολυ και ο το ελαττον ουκ ηλαττονησεν εκαστος εις τους καθηκοντας παρ' εαυτω συνελεξαν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And when they measured it by the gomor, the one who had much had nothing left over, and the one who had little had no lack. Each gathered according to those assigned to him.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:19

Greek: ειπεν δε μωυσης προς αυτους μηδεις καταλιπετω απ' αυτου εις το πρωι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses said to them, "Let no one leave any of it until morning."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:20

Greek: και ουκ εισηκουσαν μωυση αλλα κατελιπον τινες απ' αυτου εις το πρωι και εξεζεσεν σκωληκας και επωζεσεν και επικρανθη επ' αυτοις μωυσης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But they did not listen to Moses, and some left from it until morning, and it bred worms and stank, and Moses was embittered against them.

Decision rows:
- greek_phrase: ἐπικράνθη | lemma: πικραίνω | morphology: aorist passive indicative 3 singular | chosen_rendering: Moses was embittered against them | alternate_renderings: Moses was angered with them; Moses was made bitter toward them | rationale: Preserves the bitterness-language rather than flattening it to generic irritation. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: Moses was embittered against them | footnote_text: Greek uses bitterness-language here, not only generic anger. This draft keeps that sharper edge. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:21

Greek: και συνελεξαν αυτο πρωι πρωι εκαστος το καθηκον αυτω ηνικα δε διεθερμαινεν ο ηλιος ετηκετο
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they gathered it morning by morning, each according to what was needed for him. But when the sun grew hot, it melted.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:22

Greek: εγενετο δε τη ημερα τη εκτη συνελεξαν τα δεοντα διπλα δυο γομορ τω ενι εισηλθοσαν δε παντες οι αρχοντες της συναγωγης και ανηγγειλαν μωυσει
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it happened on the sixth day that they gathered what was needed double, two gomors for one person. Then all the rulers of the assembly came in and reported it to Moses.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:23

Greek: ειπεν δε μωυσης προς αυτους τουτο το ρημα εστιν ο ελαλησεν κυριος σαββατα αναπαυσις αγια τω κυριω αυριον οσα εαν πεσσητε πεσσετε και οσα εαν εψητε εψετε και παν το πλεοναζον καταλιπετε αυτο εις αποθηκην εις το πρωι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said to them, "This is the word the Lord spoke: Tomorrow is Sabbath, a holy rest to the Lord. Whatever you will bake, bake, and whatever you will boil, boil, and all that is left over leave stored up until morning."

Decision rows:
- greek_phrase: σάββατα ἀνάπαυσις ἁγία | lemma: σάββατα | ἀνάπαυσις | ἅγιος | morphology: nominative singular/plural noun phrase | chosen_rendering: Sabbath, a holy rest | alternate_renderings: sabbaths, holy resting; sabbath-rest holy | rationale: Captures the sabbath-rest wording in readable English while preserving the holy-rest emphasis. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: Sabbath, a holy rest | footnote_text: Greek stresses both sabbath and rest in the same phrase. This draft keeps both elements visible. | source_basis: lexical + liturgy | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:24

Greek: και κατελιποσαν απ' αυτου εις το πρωι καθαπερ συνεταξεν αυτοις μωυσης και ουκ επωζεσεν ουδε σκωληξ εγενετο εν αυτω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they left some of it until morning, just as Moses commanded them, and it did not stink, nor did a worm appear in it.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:25

Greek: ειπεν δε μωυσης φαγετε σημερον εστιν γαρ σαββατα σημερον τω κυριω ουχ ευρεθησεται εν τω πεδιω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses said, "Eat it today, for today is Sabbath to the Lord. Today it will not be found in the field."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:26

Greek: εξ ημερας συλλεξετε τη δε ημερα τη εβδομη σαββατα οτι ουκ εσται εν αυτη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "For six days you shall gather it, but on the seventh day is Sabbath, because it will not be on that day."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:27

Greek: εγενετο δε εν τη ημερα τη εβδομη εξηλθοσαν τινες εκ του λαου συλλεξαι και ουχ ευρον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it happened on the seventh day that some of the people went out to gather, and they found none.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:28

Greek: ειπεν δε κυριος προς μωυσην εως τινος ου βουλεσθε εισακουειν τας εντολας μου και τον νομον μου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, "How long will you refuse to listen to my commands and my law?"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:29

Greek: ιδετε ο γαρ κυριος εδωκεν υμιν την ημεραν ταυτην τα σαββατα δια τουτο αυτος εδωκεν υμιν τη ημερα τη εκτη αρτους δυο ημερων καθησεσθε εκαστος εις τους οικους υμων μηδεις εκπορευεσθω εκ του τοπου αυτου τη ημερα τη εβδομη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "See, for the Lord has given you this day as the Sabbath. Because of this he has given you on the sixth day bread for two days. Let each stay in his houses. Let no one go out from his place on the seventh day."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:30

Greek: και εσαββατισεν ο λαος τη ημερα τη εβδομη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the people Sabbathed on the seventh day.

Decision rows:
- greek_phrase: ἐσαββάτισεν | lemma: σαββατίζω | morphology: aorist active indicative 3 singular | chosen_rendering: the people Sabbathed | alternate_renderings: the people kept sabbath; the people rested sabbath | rationale: Keeps the verbal sabbath form explicit instead of paraphrasing away the wordplay. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: the people Sabbathed | footnote_text: Greek makes sabbath a verb here. This draft preserves that verbal form. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:31

Greek: και επωνομασαν οι υιοι ισραηλ το ονομα αυτου μαν ην δε ως σπερμα κοριου λευκον το δε γευμα αυτου ως εγκρις εν μελιτι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the sons of Israel called its name Man. It was like white coriander seed, and its taste was like a cake in honey.

Decision rows:
- greek_phrase: μάν | lemma: μάν | morphology: indeclinable noun | chosen_rendering: Man | alternate_renderings: Manna | rationale: Keeps the Greek form of the name visible in this draft tradition. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: Man | footnote_text: Greek preserves the form Man here rather than the later English convention manna. | source_basis: lexical + tradition | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:32

Greek: ειπεν δε μωυσης τουτο το ρημα ο συνεταξεν κυριος πλησατε το γομορ του μαν εις αποθηκην εις τας γενεας υμων ινα ιδωσιν τον αρτον ον εφαγετε υμεις εν τη ερημω ως εξηγαγεν υμας κυριος εκ γης αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses said, "This is the word the Lord commanded: Fill the gomor with Man for storage throughout your generations, so that they may see the bread that you ate in the wilderness when the Lord brought you out from the land of Egypt."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:33

Greek: και ειπεν μωυσης προς ααρων λαβε σταμνον χρυσουν ενα και εμβαλε εις αυτον πληρες το γομορ του μαν και αποθησεις αυτο εναντιον του θεου εις διατηρησιν εις τας γενεας υμων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said to Aaron, "Take one golden jar and put into it a full gomor of Man, and you shall place it before God for preservation throughout your generations,"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:34

Greek: ον τροπον συνεταξεν κυριος τω μωυση και απεθετο ααρων εναντιον του μαρτυριου εις διατηρησιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: just as the Lord commanded Moses, and Aaron placed it before the testimony for preservation.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:35

Greek: οι δε υιοι ισραηλ εφαγον το μαν ετη τεσσαρακοντα εως ηλθον εις γην οικουμενην το μαν εφαγοσαν εως παρεγενοντο εις μερος της φοινικης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the sons of Israel ate Man forty years, until they came into an inhabited land. They ate Man until they came to the region of Phoenicia.

Decision rows:
- greek_phrase: εἰς μέρος τῆς Φοινίκης | lemma: μέρος | Φοινίκη | morphology: accusative singular noun phrase | chosen_rendering: to the region of Phoenicia | alternate_renderings: to the part of Phoenicia; to Phoenicia's border-region | rationale: Preserves the striking Greek geographical wording rather than harmonizing it away. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: region of Phoenicia | footnote_text: The Greek text here reads Phoenicia, a striking geographical wording different from more familiar harmonized renderings. | source_basis: textual + geography | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 16:36

Greek: το δε γομορ το δεκατον των τριων μετρων ην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Now the gomor was the tenth part of three measures.

Decision rows:
- greek_phrase: τὸ δέκατον τῶν τριῶν μέτρων | lemma: δέκατος | τρεῖς | μέτρον | morphology: numerical noun phrase | chosen_rendering: the tenth part of three measures | alternate_renderings: one tenth of three measures | rationale: Keeps the Greek explanatory measure note directly visible. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: tenth part of three measures | footnote_text: Greek closes with a direct explanatory note about the gomor measure. This draft leaves the measure note in its explicit form. | source_basis: lexical + measurement | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 17

### Exodus 17:1

Greek: και απηρεν πασα συναγωγη υιων ισραηλ εκ της ερημου σιν κατα παρεμβολας αυτων δια ρηματος κυριου και παρενεβαλοσαν εν ραφιδιν ουκ ην δε υδωρ τω λαω πιειν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the whole assembly of the sons of Israel set out from the wilderness of Sin, by their encampments, according to the word of the Lord, and they camped in Raphidin. But there was no water for the people to drink.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:2

Greek: και ελοιδορειτο ο λαος προς μωυσην λεγοντες δος ημιν υδωρ ινα πιωμεν και ειπεν αυτοις μωυσης τι λοιδορεισθε μοι και τι πειραζετε κυριον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the people reviled Moses, saying, "Give us water, so that we may drink." And Moses said to them, "Why do you revile me, and why do you test the Lord?"

Decision rows:
- greek_phrase: ἐλοιδορεῖτο ... τί λοιδορεῖσθέ μοι | lemma: λοιδορέω | morphology: imperfect middle/passive indicative 3 singular / present middle-passive indicative 2 plural | chosen_rendering: reviled / revile | alternate_renderings: quarreled with; abused; reproached | rationale: Keeps the sharper insult-language of the Greek rather than softening it to mere dispute. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: reviled Moses | footnote_text: Greek uses insult or abuse language here, not merely disagreement. This draft keeps the sharper edge of the complaint. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:3

Greek: εδιψησεν δε εκει ο λαος υδατι και εγογγυζεν εκει ο λαος προς μωυσην λεγοντες ινα τι τουτο ανεβιβασας ημας εξ αιγυπτου αποκτειναι ημας και τα τεκνα ημων και τα κτηνη τω διψει
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And there the people thirsted for water, and there the people grumbled against Moses, saying, "Why is this? Have you brought us up out from Egypt to kill us and our children and our livestock with thirst?"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:4

Greek: εβοησεν δε μωυσης προς κυριον λεγων τι ποιησω τω λαω τουτω ετι μικρον και καταλιθοβολησουσιν με
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses cried out to the Lord, saying, "What shall I do with this people? A little more and they will stone me."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:5

Greek: και ειπεν κυριος προς μωυσην προπορευου του λαου τουτου λαβε δε μετα σεαυτου απο των πρεσβυτερων του λαου και την ραβδον εν η επαταξας τον ποταμον λαβε εν τη χειρι σου και πορευση
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And the Lord said to Moses, "Go on ahead of this people, and take with yourself some of the elders of the people. And the rod with which you struck the river, take in your hand and go."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:6

Greek: οδε εγω εστηκα προ του σε εκει επι της πετρας εν χωρηβ και παταξεις την πετραν και εξελευσεται εξ αυτης υδωρ και πιεται ο λαος μου εποιησεν δε μωυσης ουτως εναντιον των υιων ισραηλ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Look, I am standing before you there on the rock in Horeb, and you shall strike the rock, and water will come out from it, and my people will drink." And Moses did so before the sons of Israel.

Decision rows:
- greek_phrase: ὅδε ἐγὼ ἕστηκα | lemma: ἵστημι | morphology: perfect active indicative 1 singular | chosen_rendering: I am standing | alternate_renderings: Here I stand; I have stood | rationale: Preserves the vivid παρουσια-like immediacy of the divine stance at the rock. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:7

Greek: και επωνομασεν το ονομα του τοπου εκεινου πειρασμος και λοιδορησις δια την λοιδοριαν των υιων ισραηλ και δια το πειραζειν κυριον λεγοντας ει εστιν κυριος εν ημιν η ου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And he called the name of that place Testing and Reviling, because of the reviling of the sons of Israel and because of their testing the Lord, saying, "Is the Lord among us or not?"

Decision rows:
- greek_phrase: πειρασμός καὶ λοιδόρησις | lemma: πειρασμός | λοιδόρησις | morphology: nominative singular noun pair | chosen_rendering: Testing and Reviling | alternate_renderings: Temptation and Reviling; Trial and Abuse | rationale: Keeps both place-name nouns tied directly to the people's actions against Moses and the Lord. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: Testing and Reviling | footnote_text: The place-name explanation preserves both actions: testing the Lord and reviling in the dispute. This draft keeps both nouns visible. | source_basis: lexical + narrative | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:8

Greek: ηλθεν δε αμαληκ και επολεμει ισραηλ εν ραφιδιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Amalek came and fought with Israel in Raphidin.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:9

Greek: ειπεν δε μωυσης τω ιησου επιλεξον σεαυτω ανδρας δυνατους και εξελθων παραταξαι τω αμαληκ αυριον και ιδου εγω εστηκα επι της κορυφης του βουνου και η ραβδος του θεου εν τη χειρι μου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said to Joshua, "Choose for yourself strong men and go out and draw up in battle array against Amalek tomorrow. And look, I will stand on the top of the hill, and the rod of God will be in my hand."

Decision rows:
- greek_phrase: παράταξαι | lemma: παρατάσσω | morphology: aorist middle infinitive | chosen_rendering: draw up in battle array | alternate_renderings: set in array; line up for battle | rationale: Keeps the military formation sense instead of a generic go fight wording. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: draw up in battle array | footnote_text: Greek uses military formation language here. This draft keeps the battle-array sense rather than a generic fight command. | source_basis: lexical + military context | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:10

Greek: και εποιησεν ιησους καθαπερ ειπεν αυτω μωυσης και εξελθων παρεταξατο τω αμαληκ και μωυσης και ααρων και ωρ ανεβησαν επι την κορυφην του βουνου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Joshua did just as Moses told him, and he went out and drew up in battle array against Amalek. And Moses and Aaron and Hur went up to the top of the hill.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:11

Greek: και εγινετο οταν επηρεν μωυσης τας χειρας κατισχυεν ισραηλ οταν δε καθηκεν τας χειρας κατισχυεν αμαληκ
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it happened that whenever Moses lifted up his hands, Israel prevailed, and whenever he let down his hands, Amalek prevailed.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:12

Greek: αι δε χειρες μωυση βαρειαι και λαβοντες λιθον υπεθηκαν υπ' αυτον και εκαθητο επ' αυτου και ααρων και ωρ εστηριζον τας χειρας αυτου εντευθεν εις και εντευθεν εις και εγενοντο αι χειρες μωυση εστηριγμεναι εως δυσμων ηλιου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: But Moses' hands were heavy, and taking a stone they put it under him, and he sat on it. And Aaron and Hur were supporting his hands, one from this side and one from that side, and Moses' hands became supported until the setting of the sun.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:13

Greek: και ετρεψατο ιησους τον αμαληκ και παντα τον λαον αυτου εν φονω μαχαιρας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Joshua routed Amalek and all his people with the slaughter of the sword.

Decision rows:
- greek_phrase: ἐτρέψατο | lemma: τρέπω | morphology: aorist middle indicative 3 singular | chosen_rendering: routed | alternate_renderings: turned back; put to flight | rationale: Routed expresses the defeat implied by the battle-turning verb in context. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:14

Greek: ειπεν δε κυριος προς μωυσην καταγραψον τουτο εις μνημοσυνον εν βιβλιω και δος εις τα ωτα ιησοι οτι αλοιφη εξαλειψω το μνημοσυνον αμαληκ εκ της υπο τον ουρανον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the Lord said to Moses, "Write this as a memorial in a book, and put it into the ears of Joshua, for in wiping out I will wipe out the memorial of Amalek from under heaven."

Decision rows:
- greek_phrase: ἀλοίφῃ ἐξαλείψω | lemma: ἀλείφω | ἐξαλείφω | morphology: dative/infinitive-like emphatic expression + future active indicative 1 singular | chosen_rendering: in wiping out I will wipe out | alternate_renderings: I will utterly blot out; blotting out I will blot out | rationale: Keeps the emphatic doubled erasure language visible. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: in wiping out I will wipe out | footnote_text: Greek doubles the wipe-out language for emphasis. This draft preserves the force of that repetition. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:15

Greek: και ωκοδομησεν μωυσης θυσιαστηριον κυριω και επωνομασεν το ονομα αυτου κυριος μου καταφυγη
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses built an altar to the Lord and called its name, "The Lord is my refuge,"

Decision rows:
- greek_phrase: κύριος μου καταφυγή | lemma: κύριος | καταφυγή | morphology: nominative singular noun phrase | chosen_rendering: The Lord is my refuge | alternate_renderings: The Lord my refuge; The Lord my shelter | rationale: Makes the altar-name read clearly while preserving the refuge motif. | status: drafted

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 17:16

Greek: οτι εν χειρι κρυφαια πολεμει κυριος επι αμαληκ απο γενεων εις γενεας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: for with hidden hand the Lord wages war against Amalek from generation to generation.

Decision rows:
- greek_phrase: ἐν χειρὶ κρυφαίᾳ | lemma: χείρ | κρυφαῖος | morphology: dative singular noun phrase | chosen_rendering: with hidden hand | alternate_renderings: with secret hand; by concealed hand | rationale: Keeps the strange and important Greek image instead of normalizing it away. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: with hidden hand | footnote_text: Greek here has a difficult hidden-hand expression. This draft keeps the wording visible instead of smoothing it into a more familiar formula. | source_basis: lexical + textual | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

## Chapter 18

### Exodus 18:1

Greek: ηκουσεν δε ιοθορ ο ιερευς μαδιαμ ο γαμβρος μωυση παντα οσα εποιησεν κυριος ισραηλ τω εαυτου λαω εξηγαγεν γαρ κυριος τον ισραηλ εξ αιγυπτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Jethro, priest of Midian, the father-in-law of Moses, heard all that the Lord had done for Israel, his own people, for the Lord had brought Israel out from Egypt.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:2

Greek: ελαβεν δε ιοθορ ο γαμβρος μωυση σεπφωραν την γυναικα μωυση μετα την αφεσιν αυτης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Jethro, the father-in-law of Moses, took Zipporah, the wife of Moses, after her sending away.

Decision rows:
- greek_phrase: μετὰ τὴν ἄφεσιν αὐτῆς | lemma: ἄφεσις | morphology: accusative singular noun phrase | chosen_rendering: after her sending away | alternate_renderings: after her release; after he had sent her away | rationale: Keeps the Greek dismissal/release wording visible without over-deciding the precise marital or logistical nuance. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: after her sending away | footnote_text: Greek uses dismissal or release language here. This draft keeps that wording visible without forcing a narrower explanation. | source_basis: lexical + narrative | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:3

Greek: και τους δυο υιους αυτου ονομα τω ενι αυτων γηρσαμ λεγων παροικος ημην εν γη αλλοτρια
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: and her two sons. The name of one was Gersam, saying, "I was a resident alien in a foreign land,"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:4

Greek: και το ονομα του δευτερου ελιεζερ λεγων ο γαρ θεος του πατρος μου βοηθος μου και εξειλατο με εκ χειρος φαραω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: and the name of the second was Eliezer, saying, "For the God of my father is my helper, and he rescued me from the hand of Pharaoh."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:5

Greek: και εξηλθεν ιοθορ ο γαμβρος μωυση και οι υιοι και η γυνη προς μωυσην εις την ερημον ου παρενεβαλεν επ' ορους του θεου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Jethro, the father-in-law of Moses, and his sons and wife, came out to Moses into the wilderness where he had camped at the mountain of God.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:6

Greek: ανηγγελη δε μωυσει λεγοντες ιδου ο γαμβρος σου ιοθορ παραγινεται προς σε και η γυνη και οι δυο υιοι σου μετ' αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And word was reported to Moses, saying, "Look, your father-in-law Jethro is coming to you, and your wife and your two sons with him."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:7

Greek: εξηλθεν δε μωυσης εις συναντησιν τω γαμβρω αυτου και προσεκυνησεν αυτω και εφιλησεν αυτον και ησπασαντο αλληλους και εισηγαγεν αυτον εις την σκηνην
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses went out to meet his father-in-law and bowed down to him and kissed him, and they greeted one another and brought him into the tent.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:8

Greek: και διηγησατο μωυσης τω γαμβρω παντα οσα εποιησεν κυριος τω φαραω και τοις αιγυπτιοις ενεκεν του ισραηλ και παντα τον μοχθον τον γενομενον αυτοις εν τη οδω και οτι εξειλατο αυτους κυριος εκ χειρος φαραω και εκ χειρος των αιγυπτιων
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses recounted to his father-in-law all that the Lord had done to Pharaoh and the Egyptians for Israel's sake, and all the hardship that had come upon them on the way, and that the Lord had rescued them from the hand of Pharaoh and from the hand of the Egyptians.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:9

Greek: εξεστη δε ιοθορ επι πασι τοις αγαθοις οις εποιησεν αυτοις κυριος οτι εξειλατο αυτους εκ χειρος αιγυπτιων και εκ χειρος φαραω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Jethro was amazed at all the good things that the Lord had done for them, that he had rescued them from the hand of the Egyptians and from the hand of Pharaoh.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:10

Greek: και ειπεν ιοθορ ευλογητος κυριος οτι εξειλατο τον λαον αυτου εκ χειρος αιγυπτιων και εκ χειρος φαραω
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Jethro said, "Blessed be the Lord, because he has rescued his people from the hand of the Egyptians and from the hand of Pharaoh."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:11

Greek: νυν εγνων οτι μεγας κυριος παρα παντας τους θεους ενεκεν τουτου οτι επεθεντο αυτοις
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Now I know that the Lord is great above all the gods, because in this matter they acted arrogantly against them."

Decision rows:
- greek_phrase: ἐνεκεν τούτου ὅτι ἐπέθεντο αὐτοῖς | lemma: ἐπτίθημι/ἐπιτίθημι | morphology: causal phrase + aorist middle indicative 3 plural | chosen_rendering: because in this matter they acted arrogantly against them | alternate_renderings: because they attacked them in this matter; because they dealt proudly against them | rationale: Preserves the morally charged overreaching sense rather than reducing the line to simple hostility. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: acted arrogantly against them | footnote_text: Greek suggests more than simple opposition here; it points to overreaching or arrogant action against Israel. | source_basis: lexical + theology | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:12

Greek: και ελαβεν ιοθορ ο γαμβρος μωυση ολοκαυτωματα και θυσιας τω θεω παρεγενετο δε ααρων και παντες οι πρεσβυτεροι ισραηλ συμφαγειν αρτον μετα του γαμβρου μωυση εναντιον του θεου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Jethro, the father-in-law of Moses, took whole burnt offerings and sacrifices to God. And Aaron and all the elders of Israel came to eat bread with the father-in-law of Moses before God.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:13

Greek: και εγενετο μετα την επαυριον συνεκαθισεν μωυσης κρινειν τον λαον παρειστηκει δε πας ο λαος μωυσει απο πρωιθεν εως εσπερας
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And it happened on the next day that Moses sat to judge the people, and all the people stood by Moses from morning until evening.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:14

Greek: και ιδων ιοθορ παντα οσα εποιει τω λαω λεγει τι τουτο ο συ ποιεις τω λαω δια τι συ καθησαι μονος πας δε ο λαος παρεστηκεν σοι απο πρωιθεν εως δειλης
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And when Jethro saw all that Moses was doing for the people, he said, "What is this that you are doing for the people? Why do you sit alone while all the people stand by you from morning until evening?"

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:15

Greek: και λεγει μωυσης τω γαμβρω οτι παραγινεται προς με ο λαος εκζητησαι κρισιν παρα του θεου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses said to his father-in-law, "Because the people come to me to seek judgment from God."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:16

Greek: οταν γαρ γενηται αυτοις αντιλογια και ελθωσι προς με διακρινω εκαστον και συμβιβαζω αυτους τα προσταγματα του θεου και τον νομον αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "For whenever they have a dispute and come to me, I decide each one and instruct them in the ordinances of God and his law."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:17

Greek: ειπεν δε ο γαμβρος μωυση προς αυτον ουκ ορθως συ ποιεις το ρημα τουτο
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then the father-in-law of Moses said to him, "This thing that you are doing is not right."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:18

Greek: φθορα καταφθαρηση ανυπομονητω και συ και πας ο λαος ουτος ος εστιν μετα σου βαρυ σοι το ρημα τουτο ου δυνηση ποιειν μονος
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "With ruin you will wear away, with unbearable exhaustion, both you and all this people that is with you. This thing is too heavy for you. You will not be able to do it alone."

Decision rows:
- greek_phrase: φθορᾷ καταφθαρήσῃ ἀνυπομονήτῳ | lemma: φθορά | καταφθείρω | ἀνυπομόνητος | morphology: dative singular noun + future middle/passive indicative 2 singular + dative singular adjective | chosen_rendering: With ruin you will wear away, with exhaustion unbearable | alternate_renderings: You will utterly wear out with intolerable strain; you will be ruined with unbearable exhaustion | rationale: Keeps the doubled wear-ruin emphasis and the strong adjective rather than flattening it to simple tiredness. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: wear away, with exhaustion unbearable | footnote_text: Greek doubles the wear-out idea and adds an unbearable-strain term. This draft preserves the severity of Jethro's warning. | source_basis: lexical + rhetoric | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:19

Greek: νυν ουν ακουσον μου και συμβουλευσω σοι και εσται ο θεος μετα σου γινου συ τω λαω τα προς τον θεον και ανοισεις τους λογους αυτων προς τον θεον
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "Now then, listen to me, and I will advise you, and God will be with you. Be for the people in the things toward God, and you shall bring their words to God."

Decision rows:
- greek_phrase: γίνου σὺ τῷ λαῷ τὰ πρὸς τὸν θεόν | lemma: γίνομαι | πρός | θεός | morphology: present middle imperative 2 singular + neuter plural phrase | chosen_rendering: Be for the people in the things toward God | alternate_renderings: Be the people's representative before God; be for the people in matters pertaining to God | rationale: Keeps the slightly awkward but important relational phrasing of the Greek instead of over-interpreting it. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: things toward God | footnote_text: Greek leaves the phrase somewhat open: Moses is to stand for the people in matters directed toward God. This draft keeps that wording rather than narrowing it too quickly. | source_basis: lexical + discourse | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:20

Greek: και διαμαρτυρη αυτοις τα προσταγματα του θεου και τον νομον αυτου και σημανεις αυτοις τας οδους εν αις πορευσονται εν αυταις και τα εργα α ποιησουσιν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And you shall testify to them the ordinances of God and his law, and you shall make known to them the ways in which they shall walk and the works that they shall do."

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:21

Greek: και συ σεαυτω σκεψαι απο παντος του λαου ανδρας δυνατους θεοσεβεις ανδρας δικαιους μισουντας υπερηφανιαν και καταστησεις αυτους επ' αυτων χιλιαρχους και εκατονταρχους και πεντηκονταρχους και δεκαδαρχους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And you, select for yourself from all the people able men, God-fearing men, righteous men, hating arrogance, and you shall appoint them over them as commanders of thousands and hundreds and fifties and tens."

Decision rows:
- greek_phrase: μισοῦντας ὑπερηφανίαν | lemma: μισέω | ὑπερηφανία | morphology: present active participle accusative plural + accusative singular noun | chosen_rendering: hating arrogance | alternate_renderings: hating pride; hating overbearing conduct | rationale: Arrogance captures the social and moral edge of the Greek better than a flatter abstract pride. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: hating arrogance | footnote_text: Greek names arrogance explicitly as a trait these judges must reject. This draft keeps that sharper social vice visible. | source_basis: lexical + ethics | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:22

Greek: και κρινουσιν τον λαον πασαν ωραν το δε ρημα το υπερογκον ανοισουσιν επι σε τα δε βραχεα των κριματων κρινουσιν αυτοι και κουφιουσιν απο σου και συναντιλημψονται σοι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "And they shall judge the people at every hour. The over-large matter they shall bring to you, but the small cases they shall judge themselves, and they shall lighten the load from you and help you."

Decision rows:
- greek_phrase: τὸ ῥῆμα τὸ ὑπέρογκον | lemma: ὑπέρογκος | morphology: accusative singular adjective phrase | chosen_rendering: the over-large matter | alternate_renderings: the overburdensome matter; the weighty matter; the too great matter | rationale: Keeps the sense of something swollen beyond ordinary scale, not merely big in importance. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: over-large matter | footnote_text: Greek uses a swollen or oversized term here. This draft keeps the image of cases too large for ordinary handling. | source_basis: lexical + imagery | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:23

Greek: εαν το ρημα τουτο ποιησης κατισχυσει σε ο θεος και δυνηση παραστηναι και πας ο λαος ουτος εις τον εαυτου τοπον μετ' ειρηνης ηξει
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: "If you do this thing, God will strengthen you, and you will be able to stand, and all this people will come to its own place with peace."

Decision rows:
- greek_phrase: κατισχύσει σε ὁ θεός καὶ δυνήσῃ παραστῆναι | lemma: κατισχύω | δύναμαι | παρίστημι | morphology: future active indicative 3 singular + future middle indicative 2 singular + aorist active infinitive | chosen_rendering: God will strengthen you, and you will be able to stand | alternate_renderings: God will sustain you, and you will endure; God will prevail for you, and you will be able to remain | rationale: Reads the cluster as divine strengthening leading to Moses' endurance in office. | status: drafted

Publishable footnotes:
- note_type: translation | trigger_phrase: God will strengthen you, and you will be able to stand | footnote_text: Greek links divine strengthening with Moses being able to remain standing under the burden. This draft keeps both ideas together. | source_basis: lexical + leadership | status: drafted

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:24

Greek: ηκουσεν δε μωυσης της φωνης του γαμβρου και εποιησεν οσα αυτω ειπεν
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses listened to the voice of his father-in-law and did all that he said to him.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:25

Greek: και επελεξεν μωυσης ανδρας δυνατους απο παντος ισραηλ και εποιησεν αυτους επ' αυτων χιλιαρχους και εκατονταρχους και πεντηκονταρχους και δεκαδαρχους
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And Moses chose able men from all Israel and made them over the people as commanders of thousands and hundreds and fifties and tens.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:26

Greek: και εκρινοσαν τον λαον πασαν ωραν παν δε ρημα υπερογκον ανεφεροσαν επι μωυσην παν δε ρημα ελαφρον εκρινοσαν αυτοι
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: And they judged the people at every hour. Every over-large matter they brought to Moses, but every light matter they judged themselves.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]

### Exodus 18:27

Greek: εξαπεστειλεν δε μωυσης τον εαυτου γαμβρον και απηλθεν εις την γην αυτου
Transliteration: [TODO]
Literal gloss: [TODO]
Syntax notes: [TODO]
Draft translation: Then Moses sent away his father-in-law, and he went to his own land.

Decision rows:
- [TODO add decision rows]

Publishable footnotes:
- [TODO add footnote draft if needed]

Logos research:
- [TODO add Logos note]

Variant notes:
- [TODO add variant note]
