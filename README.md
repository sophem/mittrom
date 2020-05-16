# MittRom

MittRom er et prosjekt for å kunne sjekke status på lys på rommet mitt, og styre dette via internett.

Per i dag er det mulig å se om lys er av eller på, og også skru det av og på.

Plan videre er å utvide med mulighet for å styre lysstyrke, og også farge på lyset.

Prosjektet kan sees her:

https://mitt.rom.sophi.es/$kode/

Men man må ha riktig kode for å komme inn på siden, vi vil jo ikke at hele verden skal kunne styre lyset mitt.

## Valg av hovedspråk

Prosjektet er utviklet i hovedsak som et Python-prosjekt, med flask som rammeverk.
I tillegg er det brukt HTML for nettsiden, sammen med Bootstrap for bedre design, og noe Javascript i nettsiden.

## Arbeidsform

Prosjektet er hovedsakelig gjennomført som peer-programming, hvor ca. 70% av koden er laget i fellesskap med pappa, ca. 25% av koden er skrevet av meg alene, og ca. 5% er skrevet av ham (javascript i nettsiden, kode for å ikke være helt åpent på nett).

## Annen teknologi

Styringen gjøres via et JSON-API mot Philips Hue kontroller, som tyrer lyspærene.

## Involvert kode

`lights.py` inneholder kode som lager klassen for lysene, og som lager de individuele lysene, den gjør også sånn at vi kan hente informasjonen fra lysene. 
`webfun.py` inneholder kode som henter statusen av lysene, viser nettsiden og lar nettsiden styre lysene.
`index.html` gjør at siden ser ut sånn som den gjør, den lager også knappene på nettsiden. 
