# Edustandaard-readiness

Dit document is **geen normatief onderdeel** van de EAI Standard. Het beschrijft de ontwikkelrichting waarmee de repository wordt voorbereid op mogelijke aanmelding bij Edustandaard.

Edustandaard toetst een nieuwe standaard op vijf criteria. De ontwikkeling van EAI Standard gebruikt deze criteria vanaf het begin als kwaliteitsrichtlijn.

## 1. Toegevoegde waarde

Doel: aantonen dat gebruik van de standaard meerwaarde heeft ten opzichte van lokale, niet-uitwisselbare afspraken en dat de voordelen groter zijn dan mogelijke nadelen.

Voor EAI Standard betekent dit dat we aantoonbaar moeten maken dat meerdere partijen dezelfde semantiek nodig hebben voor het beschrijven van menselijk handelen en AI-handelen in onderwijsprocessen.

Benodigde bewijslast:

- concrete use cases met meerdere partijen;
- beschrijving van het probleem zonder standaard;
- aantoonbare vermindering van lokale interpretatieverschillen;
- vergelijking met bestaande standaarden en kaders;
- expliciete risico- en nadelenanalyse;
- voorbeelden waarin dezelfde beschrijving door verschillende systemen kan worden gelezen of toegepast.

Repo-artifacts:

- `docs/04-use-cases.md`
- toekomstige `docs/problem-statement.md`
- toekomstige `docs/alternatives-analysis.md`

## 2. Draagvlak

Doel: aantonen dat aanbieders en gebruikers voldoende praktijkervaring hebben en dat de standaard niet alleen door de initiatiefnemer wordt gedragen.

Voor EAI Standard betekent dit dat validatie nodig is met minimaal:

- onderwijsprofessionals;
- onderwijsorganisaties;
- leveranciers van AI- of leertechnologie;
- experts in didactiek/pedagogiek;
- experts in onderwijsarchitectuur en interoperabiliteit;
- waar passend onderzoekers en publieke organisaties.

Draagvlak wordt niet gelijkgesteld aan instemming met elke ontwerpkeuze. Het gaat om aantoonbare deelname, gebruikservaring, feedback en een transparante verwerking daarvan.

Benodigde bewijslast:

- publieke issues en wijzigingsvoorstellen;
- pilotimplementaties;
- implementatieverslagen;
- lijst van deelnemende organisaties/rollen, voor zover openbaar;
- gedocumenteerde besluiten over ontvangen feedback;
- meerdere onafhankelijke implementaties vóór een 1.0-kandidaat.

## 3. Open standaardisatieproces

Doel: ontwikkeling en beheer open, eerlijk, duidelijk, duurzaam en toegankelijk organiseren.

Voor deze repository gelden daarom de volgende ontwikkelregels:

- normatieve bestanden zijn publiek leesbaar;
- wijzigingen aan normatieve semantiek zijn traceerbaar via Git;
- wijzigingsvoorstellen bevatten probleem, voorgestelde wijziging, impact en voorbeelden;
- besluiten en breaking changes worden vastgelegd;
- wetenschappelijke onderbouwing en normatieve keuzes blijven van elkaar onderscheiden;
- deelnemers kunnen via publieke issues en pull requests voorstellen doen;
- governance en releasebeleid zijn openbaar;
- belangen van gebruikers, aanbieders en publieke partijen worden zichtbaar meegewogen;
- beheer na 1.0 moet vooraf georganiseerd zijn en niet afhankelijk zijn van één persoon.

Zie `GOVERNANCE.md` en `CONTRIBUTING.md`.

## 4. Aansluiting op architectuur

Edustandaard toetst aansluiting op de sectorarchitectuur via een ROSA-scan.

EAI Standard moet daarom niet alleen inhoudelijk begrijpelijk zijn, maar ook helder positioneren:

- welk interoperabiliteitsprobleem wordt opgelost;
- op welke architectuurlagen de standaard werkt;
- welke actoren en informatieobjecten betrokken zijn;
- welke bestaande standaarden of begrippen worden hergebruikt;
- welke overlap met bestaande afspraken bestaat;
- welke onderdelen semantisch, technisch of organisatorisch zijn;
- hoe de standaard zich verhoudt tot ROSA-principes en -begrippen.

De huidige candidate-versie is hiervoor nog niet gereed. ROSA-mapping wordt pas normatief relevant nadat de semantische basis voldoende stabiel is.

Benodigde toekomstige artifacts:

- `architecture/positioning.md`
- `architecture/rosa-crosswalk.md`
- `architecture/information-model.md`
- machineleesbare schemas en identifiers.

## 5. Toekomstbestendigheid

Doel: voorkomen dat de standaard gekoppeld raakt aan één product, modelleverancier, AI-generatie, didactisch model of tijdelijk beleidsbegrip.

Dit leidt tot de volgende ontwerpregels:

- AI-acties worden functioneel beschreven, niet per merk of product;
- onderwijsmodellen worden via adapters gekoppeld en niet in de basis ingebouwd;
- leeftijd, niveau, vak en curriculum blijven contextlagen;
- identifiers blijven stabiel over tekstuele herformuleringen heen;
- uitbreidingen mogen de betekenis van bestaande begrippen niet stilzwijgend wijzigen;
- versiebeheer en deprecatie worden expliciet geregeld;
- normatieve data moet machineleesbaar zijn;
- implementaties moeten zonder één specifieke leverancier mogelijk zijn.

## Wanneer is een Edustandaard-intake zinvol?

Niet bij een inhoudelijk mooi model alleen. Een intake wordt pas logisch zodra ten minste het volgende aanwezig is:

- stabiele scope en probleemdefinitie;
- een werkende machineleesbare specificatie;
- minimaal twee onafhankelijke implementatie- of pilotcontexten;
- aantoonbare gebruikers- en leveranciersbetrokkenheid;
- publiek wijzigings- en beheerproces;
- eerste architectuurpositionering en ROSA-verkenning;
- concrete businesscase voor sectorbrede interoperabiliteit;
- duidelijk onderscheid tussen standaard, implementatieprofiel en modeladapter.

## Ontwikkelprincipe

Edustandaard-readiness is geen laatste documentatieronde. De vijf toetsingscriteria worden gebruikt als doorlopende ontwerpcheck tijdens de ontwikkeling van de standaard.
