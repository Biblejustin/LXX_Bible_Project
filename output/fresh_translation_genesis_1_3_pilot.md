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

## Genesis 1:5

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

## Genesis 1:6

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

## Genesis 1:7

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

## Genesis 1:8

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

## Genesis 1:9

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

## Genesis 1:10

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

## Genesis 1:11

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

## Genesis 1:12

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

## Genesis 1:13

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

## Genesis 1:14

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

## Genesis 1:15

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

## Genesis 1:16

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

## Genesis 1:17

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

## Genesis 1:18

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

## Genesis 1:19

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

## Genesis 1:20

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

## Genesis 1:21

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

## Genesis 1:22

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

## Genesis 1:23

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

## Genesis 1:24

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

## Genesis 1:25

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

## Genesis 1:26

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

## Genesis 1:27

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

## Genesis 1:28

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

## Genesis 1:29

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

## Genesis 1:30

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

## Genesis 1:31

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

# Chapter 2

## Genesis 2:1

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

## Genesis 2:2

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

## Genesis 2:3

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

## Genesis 2:4

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

## Genesis 2:5

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

## Genesis 2:6

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

## Genesis 2:7

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

## Genesis 2:8

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

## Genesis 2:9

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

## Genesis 2:10

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
