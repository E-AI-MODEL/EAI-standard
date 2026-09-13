# Edustandaard-readiness

Dit document is **geen normatief onderdeel** van de EAI Standard. Het beschrijft de ontwikkelrichting waarmee de repository wordt voorbereid op mogelijke aanmelding bij Edustandaard.

De ontwikkeling gebruikt vijf beoordelingsgebieden als doorlopende kwaliteitscheck: toegevoegde waarde, draagvlak, open standaardisatieproces, aansluiting op architectuur en toekomstbestendigheid.

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

Huidige relevante artifacts:

- `docs/04-use-cases.md`;
- `docs/10-standard-publication-model.md`;
- `standard/public-interface.yaml`;
- source-preserving adapters en conformance-cases.

Nog nodig:

- expliciete problem statement;
- alternatives analysis;
- praktijkbewijs dat meerdere partijen hetzelfde interoperabiliteitsprobleem ervaren.

## 2. Draagvlak

Doel: aantonen dat aanbieders en gebruikers voldoende praktijkervaring hebben en dat de standaard niet alleen door de initiatiefnemer wordt gedragen.

Voor EAI Standard betekent dit validatie met minimaal:

- onderwijsprofessionals;
- onderwijsorganisaties;
- leveranciers van AI- of leertechnologie;
- experts in didactiek/pedagogiek;
- experts in onderwijsarchitectuur en interoperabiliteit;
- waar passend onderzoekers en publieke organisaties.

Draagvlak wordt niet gelijkgesteld aan instemming met elke ontwerpkeuze. Het gaat om aantoonbare deelname, gebruikservaring, feedback en transparante verwerking daarvan.

Benodigde bewijslast:

- publieke issues en wijzigingsvoorstellen;
- pilotimplementaties;
- implementatieverslagen;
- deelnemende organisaties/rollen, voor zover openbaar;
- gedocumenteerde besluiten over ontvangen feedback;
- meerdere onafhankelijke implementaties vóór een 1.0-kandidaat.

Dit is op dit moment nog een belangrijk open onderdeel.

## 3. Open standaardisatieproces

Doel: ontwikkeling en beheer open, eerlijk, duidelijk, duurzaam en toegankelijk organiseren.

De repository heeft inmiddels:

- een autoritatief canoniek manifest in `standard/public-interface.yaml`;
- formele normatieve taal via BCP 14;
- publieke governance en contribution guidance;
- expliciete versie- en identifierregels;
- een scheiding tussen canonieke standaard, evidence, adapters, registries en implementaties;
- traceerbare breaking candidate changes in `CHANGELOG.md`.

Nog nodig vóór stabiele positionering als open standaard:

- expliciete licentie en IPR/contribution-policy;
- formele multi-party besluitvorming;
- aantoonbare externe participatie;
- gedocumenteerde lifecycle- en deprecationprocedures die ook in de praktijk worden gebruikt.

Publiek leesbaar op GitHub is niet hetzelfde als juridisch herbruikbaar onder een open licentie. Dat verschil moet vóór 1.0 zijn opgelost.

## 4. Aansluiting op architectuur

Edustandaard toetst aansluiting op de sectorarchitectuur via een ROSA-scan.

EAI Standard moet daarom helder positioneren:

- welk interoperabiliteitsprobleem wordt opgelost;
- op welke architectuurlagen de standaard werkt;
- welke actoren en informatieobjecten betrokken zijn;
- welke bestaande standaarden of begrippen worden hergebruikt;
- welke overlap met bestaande afspraken bestaat;
- welke onderdelen semantisch, technisch of organisatorisch zijn;
- wat expliciet buiten scope blijft.

De kandidaatstandaard heeft nu een duidelijker publicatie- en lagenmodel, maar de formele architectuurpositionering is nog niet voltooid.

Benodigde toekomstige artifacts:

- `architecture/positioning.md`;
- `architecture/information-model.md`;
- `architecture/rosa-crosswalk.md`;
- gerichte crosswalks naar relevante internationale standaarden waar dat duplicatie voorkomt.

Belangrijk ontwerpprincipe: EAI moet generieke AI-systeem-, risk-, governance- of identity-standaarden niet opnieuw uitvinden wanneer bestaande standaarden dat probleem al oplossen.

## 5. Toekomstbestendigheid

Doel: voorkomen dat de standaard gekoppeld raakt aan één product, modelleverancier, AI-generatie, didactisch model of tijdelijk beleidsbegrip.

Huidige ontwerpkeuzes ondersteunen dit door:

- AI-acties functioneel te beschrijven, niet per merk of product;
- onderwijsmodellen via source-preserving adapters te koppelen;
- leeftijd, niveau, vak en curriculum als contextlagen te behandelen;
- technische system profiles buiten de canonieke human-action semantiek te houden;
- identifiers los te koppelen van repositorybestandspaden;
- extensies te namespacen;
- conformance en informatie-onzekerheid niet te vermengen;
- één canoniek manifest te gebruiken voor de publieke interface.

Nog nodig:

- persistente URI-resolutie vóór 1.0;
- geautomatiseerde versie- en referentiechecks;
- executable conformance suite;
- onafhankelijke implementaties;
- compatibility/deprecationbeleid bewezen in releases.

## Huidige readiness per kandidaat 0.4.0

**Semantische basis:** gevorderd, nog candidate.  
**Machineleesbaarheid:** aanwezig, verdere consistency checks nodig.  
**Conformance:** semantisch aangescherpt; executable suite en reference validator nog te bouwen.  
**Identifiers/versioning:** contract aanwezig; persistente publicatie en automatisering nog nodig.  
**Wetenschappelijke onderbouwing:** aanwezig als gescheiden evidence-laag; directe validatie van EAI-constructen blijft nodig.  
**Draagvlak/pilots:** onvoldoende voor registratie.  
**Architectuur/ROSA:** nog uit te werken.  
**Governance:** publieke basis aanwezig; multi-party beheer nog nodig.  
**Licentie/IPR:** open beslissing en daarmee een registratie-/open-standard blocker.

## Wanneer is een Edustandaard-intake zinvol?

Niet bij een inhoudelijk mooi model alleen. Een intake wordt pas logisch zodra ten minste het volgende aanwezig is:

- stabiele scope en probleemdefinitie;
- een werkende machineleesbare specificatie;
- executable conformance suite;
- minimaal twee onafhankelijke implementatie- of pilotcontexten;
- aantoonbare gebruikers- en leveranciersbetrokkenheid;
- publiek wijzigings- en beheerproces;
- expliciete licentie/IPR-voorwaarden;
- eerste architectuurpositionering en ROSA-verkenning;
- concrete businesscase voor sectorbrede interoperabiliteit;
- duidelijk onderscheid tussen canonieke standaard, implementation guidance, adapters, registries en contextprofielen.

## Ontwikkelprincipe

Edustandaard-readiness is geen laatste documentatieronde. De beoordelingscriteria worden gebruikt als doorlopende ontwerpcheck, maar mogen niet leiden tot inhoudelijke toevoegingen die het eigen interoperabiliteitsprobleem van EAI niet dienen.
