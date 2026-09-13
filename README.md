# EAI Standard

**Status:** Candidate 0.4.0  
**Scope:** modeloverstijgende beschrijving van menselijk handelen wanneer AI deelneemt aan onderwijsprocessen.

De EAI Standard schrijft geen didactisch of pedagogisch model voor. De standaard maakt zichtbaar welke menselijke handelingen in een concrete onderwijs- of leersituatie bedoeld zijn, welke rol AI daarin krijgt, welk menselijk bewijs nodig blijft en wat er gebeurt wanneer AI een bedoelde menselijke handeling overneemt.

Dezelfde grammatica geldt voor twee actoren:

- **docent/professional**: didactisch handelen, pedagogisch handelen en professioneel oordelen;
- **leerling**: cognitief, metacognitief, sociaal en zelfregulerend handelen.

## Basiseenheid

Elke beschrijving volgt dezelfde keten:

`context -> goal -> actor -> process position -> core human action -> microstructures -> AI action -> human evidence -> handback -> remediation -> re-demonstration`

Een **core human action** is contextafhankelijk. Een handeling is niet op zichzelf beschermd of onbeschermd. De betekenis wordt bepaald door het doel, de actor, de plaats in het gebruikte proces en de concrete situatie.

## Ontwerpregels

1. De standaard definieert geen universele onderwijsfasen. Een bestaand onderwijsmodel behoudt zijn eigen fasen en terminologie via een adapter.
2. Een kernhandeling hoort altijd bij een actor, doel en concrete procespositie.
3. Een kernhandeling kan uit meerdere microstructures bestaan.
4. Menselijke uitvoering en AI-uitvoering worden apart vastgelegd.
5. De hoeveelheid AI-output is geen maat voor taakovername. De relevante vraag is welke bedoelde menselijke handeling AI uitvoert.
6. AI-output is niet automatisch bewijs van menselijk handelen of leren.
7. Prestatie, zelfstandige beheersing, retentie en transfer zijn verschillende soorten bewijs.
8. Onbekende informatie blijft `unknown`; ontbrekende informatie wordt niet stilzwijgend ingevuld.
9. Wanneer AI een kernhandeling uitvoert en een claim over menselijke beheersing of professioneel handelen nodig is, moet de handeling worden teruggegeven aan de mens en opnieuw zichtbaar worden gemaakt.
10. Een onderwijsmodel mag de standaard verfijnen, maar de betekenis van de canonieke begrippen niet wijzigen.
11. Een andere presentatie van dezelfde semantiek is geen reden om het canonieke informatiemodel te wijzigen.

## Canonieke standaard en ondersteunende lagen

De repository is bewust gelaagd:

- [`standard/`](standard/) bevat de canonieke publieke interface: definities, relaties, regels, AI-acties, bewijssemantiek, identifiers, diagnostics, conformance-profielen en normatieve taal;
- [`schemas/`](schemas/) bevat machineleesbare contracten die bij die interface horen;
- [`registries/`](registries/) bevat uitbreidbare skills, microstructures en interventies;
- [`adapters/`](adapters/) bevat **source-preserving** mappings naar bestaande didactische, pedagogische en professionele modellen;
- [`context/`](context/) is gereserveerd voor overlays zoals leeftijd, niveau, vak, curriculum en jurisdictie;
- [`evidence/`](evidence/) bevat wetenschappelijke onderbouwing en claim-source mappings;
- [`system-profiles/`](system-profiles/) is een **niet-normatieve technische add-on** voor de systeemconfiguratie rond de observeerbare AI-action;
- [`examples/`](examples/) bevat uitgewerkte cases;
- [`tests/`](tests/) bevat conformance-fixtures;
- [`implementations/`](implementations/) bevat niet-normatieve implementatiematerialen.

De **enige autoritatieve lijst** van canonieke artifacts staat in [`standard/public-interface.yaml`](standard/public-interface.yaml). Andere documenten verwijzen daarnaar en onderhouden geen concurrerende lijst.

## Publicatievorm

EAI onderscheidt vier publicatieproducten die dezelfde semantiek moeten behouden:

1. **Specification**: wat de begrippen en regels betekenen;
2. **Machine contract**: hoe die betekenis machineleesbaar wordt uitgewisseld;
3. **Conformance**: wanneer een artefact of implementatie de standaard correct toepast;
4. **Implementation guidance**: hoe de standaard in concrete systemen en onderwijscontexten kan worden gebruikt zonder nieuwe canonieke semantiek te introduceren.

Zie [`docs/10-standard-publication-model.md`](docs/10-standard-publication-model.md).

## Mens en systeem zijn verschillende analyselagen

De standaard maakt drie vragen expliciet verschillend:

1. **Wat kan en hoe is het technische systeem geconfigureerd?** Dit kan optioneel in een system profile worden beschreven.
2. **Wat doet het systeem daadwerkelijk in deze taak?** Dit wordt beschreven met de canonieke AI-actions.
3. **Wat betekent die AI-action voor de bedoelde menselijke handeling en het beschikbare menselijke bewijs?** Dit is de EAI-analyse.

```text
SYSTEM PROFILE
model + inference + orchestration + context + tools + autonomy
                         |
                         v
OBSERVABLE AI ACTION
question / hint / classify / recommend / perform / execute
                         |
                         v
EAI STANDARD
human action / allocation / evidence / handback / remediation
```

De centrale grensregel luidt:

> **Functionele overeenkomst betekent geen constructgelijkheid.**

Een systeem kan bijvoorbeeld informatie persistent bewaren, een nieuwe taak oplossen of een interventie aanbevelen. Dat maakt systeemgeheugen niet hetzelfde construct als menselijke retentie, nieuwe-taakprestatie niet automatisch menselijke transfer en een systeemadvies niet hetzelfde als professioneel oordeel.

Zie [`docs/09-human-system-boundary.md`](docs/09-human-system-boundary.md) en [`system-profiles/human-system-boundary.yaml`](system-profiles/human-system-boundary.yaml).

## Source-preserving adapters

Een adapter herschrijft een bestaand onderwijsmodel niet naar EAI. Eerst wordt de oorspronkelijke bronstructuur bewaard. Daarna worden EAI-mappings toegevoegd. Een brononderdeel zonder goede mapping blijft bestaan en wordt als unmapped gemarkeerd.

Dit voorkomt dat bijvoorbeeld EDI, Direct Instruction, expliciete instructie of een pedagogisch model ongemerkt worden versimpeld om in de standaard te passen.

De eerste instructie-adapters zijn candidates:

- [`adapters/explicit-instruction-archer-hughes/`](adapters/explicit-instruction-archer-hughes/): Archer & Hughes Explicit Instruction;
- [`adapters/edi-2.0/`](adapters/edi-2.0/): Expliciete Directe Instructie 2.0;
- [`adapters/direct-instruction-engelmann/`](adapters/direct-instruction-engelmann/): capital-D Direct Instruction in de Engelmann-traditie.

De modellen worden bewust niet samengevoegd. De familie-index in [`adapters/direct-explicit-instruction-family/`](adapters/direct-explicit-instruction-family/) maakt overlap en structurele verschillen zichtbaar.

## Menselijk handelen en microstructures

Naast de brede docent- en leerlingskills zijn diepere, herbruikbare registries aanwezig voor onder meer:

- argumenteren;
- professioneel diagnosticeren en interpreteren van leerlingbewijs;
- scaffolding, feedback en het afbouwen van ondersteuning;
- pedagogisch en relationeel professioneel oordeel;
- retrieval, zelfstandige heruitvoering, retentie en transfer.

De registry-index staat in [`registries/index.yaml`](registries/index.yaml).

## System profile add-on

[`system-profiles/`](system-profiles/) maakt het mogelijk om een concrete AI-configuratie technisch te beschrijven zonder technische eigenschappen in de normatieve EAI-semantiek te trekken.

De bestaande achtlaagse structuur blijft bewust stabiel. Nieuwe weergaven worden als projecties van dezelfde gegevens behandeld, niet als reden om het informatiemodel opnieuw te ontwerpen.

De add-on onderscheidt bovendien:

- wat een systeem **ondersteunt**;
- wat in een deployment **ingeschakeld** is;
- wat in een concrete case daadwerkelijk **geobserveerd** is;
- op welke **evidence basis** een technische uitspraak rust.

Ook worden interne modelchecks, bronverificatie, externe verificatie en menselijke verificatie onderscheiden.

## Conformance

Conformance en informatie-onzekerheid zijn vanaf 0.4.0 twee aparte resultaatsassen.

**Conformance:**

- `conformant`;
- `non_conformant`.

**Information state:**

- `complete`;
- `contains_unknowns`;
- `incomplete`.

Een artefact kan dus correct volgens de standaard zijn opgebouwd en tegelijk expliciet onbekende informatie bevatten. Het bewaren van onzekerheid is geen fout. Het stilzwijgend omzetten van die onzekerheid in een sterkere conclusie kan dat wel zijn.

Validators geven gestructureerde diagnostics terug. Iedere diagnostic heeft een `severity` en een afzonderlijk `effect`. Zie [`docs/03-conformance.md`](docs/03-conformance.md), [`standard/diagnostics.yaml`](standard/diagnostics.yaml) en [`standard/conformance-profiles.yaml`](standard/conformance-profiles.yaml).

## Identifiers en versies

Canonieke concepten gebruiken stabiele identifiers zoals `EAI-R007`, `EV-03` en `AIA-09`. [`standard/identifiers.yaml`](standard/identifiers.yaml) definieert daarnaast een kandidaatstrategie voor wereldwijd identificeerbare HTTP-URI's zonder JSON-LD of RDF verplicht te stellen.

`standard_version` identificeert de release van de EAI Standard. Een eventueel `artifact_version`, `source_version` of `profile_version` heeft een smallere betekenis. Een generiek top-level `version`-veld wordt voor canonieke artifacts niet langer gebruikt.

Normatieve termen zoals `MUST`, `SHOULD` en `MAY` volgen BCP 14. Zie [`standard/normative-language.md`](standard/normative-language.md).

## Extensies

Lokale of leverancier-specifieke data mag worden toegevoegd via expliciet genamespace-de extensions. Een extensie mag een canoniek begrip niet herdefiniëren. Implementaties die een extensie niet begrijpen mogen die informatie bewaren zonder haar te interpreteren.

## Wat de standaard niet doet

De EAI Standard:

- kiest geen voorkeursdidactiek;
- schrijft geen pedagogische theorie voor;
- bepaalt niet welke tool of welk taalmodel gebruikt moet worden;
- gebruikt geen totaalscore voor "goed" of "fout" AI-gebruik;
- koppelt de basis niet aan één leeftijd, onderwijsniveau, vak of curriculum;
- behandelt een geproduceerd eindproduct niet als vanzelfsprekend bewijs van leren;
- presenteert structurele conformance niet als bewijs van onderwijskwaliteit of effectiviteit;
- stelt technische AI-capability niet gelijk aan menselijke kennis, leren, oordeel of verantwoordelijkheid;
- probeert geen algemene AI-risk-, governance- of systeemstandaard te vervangen.

Niveau, leeftijd, vak, curriculum en specifieke onderwijsmodellen worden als uitbreidbare context of adapter toegevoegd.

## Wetenschappelijke onderbouwing

De evidence-laag staat los van de normatieve standaard. Voor AI-specifieke claims ligt de prioriteit op recent onderzoek uit 2025-2026. Claims worden expliciet gekoppeld aan bronnen en krijgen een voorlopige evidence strength. Een bron creëert niet automatisch een normatieve regel, en wetenschappelijke aansluiting is niet hetzelfde als validatie van de standaard zelf.

Bij modeladapters wordt onderscheid gemaakt tussen **model-definition sources** en **effectiveness evidence**. [`evidence/construct-map.yaml`](evidence/construct-map.yaml) maakt omgekeerd zichtbaar welke wetenschappelijke claims een EAI-regel, begrip of registry ondersteunen, begrenzen of alleen conceptueel ondersteunen.

## Governance en open-standardstatus

De repository is publiek en het wijzigingsproces wordt verder ingericht voor open standaardisatie. Een expliciete licentie/IPR-keuze is nog vereist vóór de standaard als stabiele herbruikbare open standaard kan worden gepositioneerd. Deze keuze wordt niet stilzwijgend gemaakt.

Zie [`GOVERNANCE.md`](GOVERNANCE.md) en [`docs/05-edustandaard-readiness.md`](docs/05-edustandaard-readiness.md).

## Versie

De repository gebruikt semantische versies. Tot versie 1.0 kunnen breaking candidate changes nog voorkomen, mits expliciet gedocumenteerd.

Huidige versie: **0.4.0-candidate**.
