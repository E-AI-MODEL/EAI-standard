# EAI Standard

**Status:** Candidate 0.1.0  
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

## Repository

- [`standard/`](standard/) bevat de normatieve definities en regels.
- [`docs/`](docs/) legt de standaard uit.
- [`profiles/`](profiles/) beschrijft docent/professional en leerling.
- [`registries/`](registries/) bevat skills, microstructures en interventies.
- [`adapters/`](adapters/) koppelt bestaande onderwijs- en begeleidingsmodellen zonder die modellen te herschrijven.
- [`schemas/`](schemas/) beschrijft de machineleesbare structuur.
- [`examples/`](examples/) bevat uitgewerkte cases.
- [`tests/`](tests/) bevat conformance-cases.

## Wat de standaard niet doet

De EAI Standard:

- kiest geen voorkeursdidactiek;
- schrijft geen pedagogische theorie voor;
- bepaalt niet welke tool of welk taalmodel gebruikt moet worden;
- gebruikt geen totaalscore voor "goed" of "fout" AI-gebruik;
- koppelt de basis niet aan één leeftijd, onderwijsniveau, vak of curriculum;
- behandelt een geproduceerd eindproduct niet als vanzelfsprekend bewijs van leren.

Niveau, leeftijd, vak, curriculum en specifieke onderwijsmodellen worden als uitbreidbare context of adapter toegevoegd.

## Eerste referentiecase

`Argumenteren` wordt gebruikt als eerste volledige microstructure-case. Daarmee wordt getest of de standaard voldoende precies onderscheid maakt tussen bijvoorbeeld een standpunt kiezen, argumenten formuleren, relevantie beoordelen, tegenargumenten herkennen, weerleggen, structureren en concluderen.

## Versie

De repository gebruikt semantische versies. Tot versie 1.0 kan de structuur nog wijzigen.

Huidige versie: **0.1.0-candidate**.
