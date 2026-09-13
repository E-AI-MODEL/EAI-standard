# EAI Standard

**Status:** Candidate 0.3.0  
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
10. Een onderwijsmodel mag de standaard verfijnen, maar de betekenis van de kernbegrippen niet wijzigen.

## Architectuur

De repository is bewust gelaagd:

- [`standard/`](standard/) bevat de normatieve publieke interface: definities, relaties, regels, AI-acties, bewijssemantiek, diagnostics en conformance-profielen;
- [`registries/`](registries/) bevat uitbreidbare skills, microstructures en interventies;
- [`adapters/`](adapters/) bevat **source-preserving** mappings naar bestaande didactische, pedagogische en professionele modellen;
- [`context/`](context/) is gereserveerd voor overlays zoals leeftijd, niveau, vak, curriculum en jurisdictie;
- [`evidence/`](evidence/) bevat de wetenschappelijke onderbouwing en claim-source mappings;
- [`schemas/`](schemas/) bevat de machineleesbare contracten;
- [`examples/`](examples/) bevat uitgewerkte cases;
- [`tests/`](tests/) bevat conformance-fixtures;
- [`implementations/`](implementations/) bevat niet-normatieve implementatieafspraken.

De canonieke interoperability surface staat in [`standard/public-interface.yaml`](standard/public-interface.yaml).

## Source-preserving adapters

Een adapter herschrijft een bestaand onderwijsmodel niet naar EAI. Eerst wordt de oorspronkelijke bronstructuur bewaard. Daarna worden EAI-mappings toegevoegd. Een brononderdeel zonder goede mapping blijft dus gewoon bestaan en wordt als unmapped gemarkeerd.

Dit voorkomt dat bijvoorbeeld EDI, Direct Instruction, expliciete instructie of een pedagogisch model ongemerkt worden versimpeld om in de standaard te passen.

De eerste instructie-adapters zijn nu operationeel als candidates:

- [`adapters/explicit-instruction-archer-hughes/`](adapters/explicit-instruction-archer-hughes/): Archer & Hughes Explicit Instruction;
- [`adapters/edi-2.0/`](adapters/edi-2.0/): Expliciete Directe Instructie 2.0;
- [`adapters/direct-instruction-engelmann/`](adapters/direct-instruction-engelmann/): capital-D Direct Instruction in de Engelmann-traditie.

De modellen worden bewust niet samengevoegd. De familie-index in [`adapters/direct-explicit-instruction-family/`](adapters/direct-explicit-instruction-family/) maakt overlap en structurele verschillen zichtbaar. [`adapters/index.yaml`](adapters/index.yaml) is de machineleesbare adapter-index.

## Menselijk handelen en microstructures

Naast de brede docent- en leerlingskills zijn nu diepere, herbruikbare registries toegevoegd voor:

- argumenteren;
- professioneel diagnosticeren en interpreteren van leerlingbewijs;
- scaffolding, feedback en het afbouwen van ondersteuning;
- pedagogisch en relationeel professioneel oordeel;
- retrieval, zelfstandige heruitvoering, retentie en transfer.

De actuele registry-index staat in [`registries/index.yaml`](registries/index.yaml).

## Conformance

Conformance is profielspecifiek en gebruikt drie toestanden:

- `valid`;
- `unknown`;
- `invalid`.

Validators geven gestructureerde diagnostics terug in plaats van alleen `true` of `false`. Canonieke codes staan in [`standard/diagnostics.yaml`](standard/diagnostics.yaml). Profielen staan in [`standard/conformance-profiles.yaml`](standard/conformance-profiles.yaml).

De testset bevat inmiddels zowel didactische als pedagogische situaties. De EDI-cases testen guided practice, een evidence-beslispunt en AI-overname bij een zelfstandigheidsclaim. De pedagogische cases testen directe menselijke betekenisgeving, nominale goedkeuring van een AI-oordeel en een situatie waarin relevante informatie expliciet `unknown` blijft.

Dat is bewust: de standaard moet ook buiten een lesmodel kunnen beschrijven wat bij de mens moet blijven wanneer professioneel pedagogisch oordeel centraal staat.

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
- presenteert structurele conformance niet als bewijs van onderwijskwaliteit of effectiviteit.

Niveau, leeftijd, vak, curriculum en specifieke onderwijsmodellen worden als uitbreidbare context of adapter toegevoegd.

## Wetenschappelijke onderbouwing

De evidence-laag staat los van de normatieve standaard. Voor AI-specifieke claims ligt de prioriteit op recent onderzoek uit 2025-2026. Claims worden expliciet gekoppeld aan bronnen en krijgen een voorlopige evidence strength. Een bron creëert niet automatisch een normatieve regel, en wetenschappelijke aansluiting is niet hetzelfde als validatie van de standaard zelf.

Bij modeladapters wordt daarnaast onderscheid gemaakt tussen **model-definition sources** en **effectiveness evidence**. Een actuele modelbron kan oud onderzoek bevatten of een oudere traditie beschrijven; dat maakt modelbeschrijving niet automatisch effectiviteitsbewijs. Omgekeerd wordt bewijs voor capital-D Direct Instruction niet gebruikt alsof het bewijs is voor EDI of elke vorm van expliciete instructie.

[`evidence/construct-map.yaml`](evidence/construct-map.yaml) maakt bovendien omgekeerd zichtbaar welke wetenschappelijke claims een EAI-regel, begrip of registry ondersteunen, begrenzen of alleen conceptueel ondersteunen.

## Eerste referentiecases

`Argumenteren` is de eerste uitgebreide leerling-microstructure-case. De instructie-adapters voegen daar docentdiagnose, support regulation en onafhankelijke heruitvoering aan toe. De pedagogische cases testen dezelfde standaardgrammatica zonder een didactisch fasemodel.

## Versie

De repository gebruikt semantische versies. Tot versie 1.0 kan de structuur nog wijzigen.

Huidige versie: **0.3.0-candidate**.
