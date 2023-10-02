# Testausdokumentti

Ohjelmaa on testattu perusteellisesti automatisoiduilla yksikkö- ja järjestelmätesteillä sekä manuaalisilla käyttöliittymätesteillä. Tämä on varmistanut SoteriaReitti-sovelluksen vakaan ja virheettömän toiminnan erilaisissa tilanteissa ja käyttöympäristöissä.

Päivitetty 29.09.2023

## Yksikkötestit

[![Coverage Report](/docs/images/coverage.svg "Coverage Badge")](https://htmlpreview.github.io/?https://github.com/3nd3r1/soteriareitti/blob/main/docs/coverage/index.html)
(Badgea voi klikata.)

Yksikkötestauksen kattavuusraportissa on testattu SoteriaReitti-sovelluksen yksittäisiä komponentteja kuten Emergency, Station ja Utils. Testit kattavat kaikki keskeiset toiminnot, kuten hätätilanteiden reitityksen, stationeiden ja responderien hallinnan.

Testit tehtiin hyödyntäen Pythonin unittest-kirjastoa, joka mahdollisti automatisoitujen testien kirjoittamisen jokaiselle komponentille. Jokainen komponentti testattiin erikseen varmistaen, että jokainen osa-alue toimii oikein ja odotetulla tavalla.

Yksikkötestit voidaan suorittaa seuraavasti:

1. Navigoi projektin juureen.
2. Lataa projektin riippuvuudet komennolla:
   `poetry install`
3. Suorita testit komennolla:
   `poetry run invoke test`

### Emergency

_Emergency_-luokan toimintaa on testattu _TestEmergency_-luokalla. Testit kattavat hätätilanteiden hallinnan, reittien laskennan ja responderien oikeanlaisen kohdentamisen. Testitapaukset varmistavat, että hätätilanteiden reititys ja lähimmän responderin valinta toimivat oikein.

### Station-luokka

_Station_-luokan (sairaala, paloasema jne.) toimintaa on testattu _TestStation_-luokalla. Testit varmistavat, että stationit voidaan lisätä kartalle ja reitin löytäminen hätätilanteisiin ja hätätilanteista toimii oikein.

### Responder

_Responders_-luokan (ambulanssit, poliisit autot jne.) toimintaa on testattu _TestResponder_-luokalla. Testit varmistavat, että responderit voidaan lisätä kartalle oikein, ~~ja niiden liikkuminen~~ ja reittien laskenta toimivat sujuvasti.

### Utils

_utils.geo_-moduulin toimintaa on perusteellisesti testattu _TestUtilsGeo_-luokalla. Testitapaukset kattavat kaikki maantieteelliset laskelmat, kuten etäisyyksien laskemisen karttapisteiden välillä ja sijaintien konversion koordinaattimuodoista. Testit varmistavat, että _utils.geo_-moduuli toimii tarkasti ja tarkoituksenmukaisesti.

_utils.graph_-moduulin toimintaa on testattu _TestUtilsGraph_-luokalla. Testitapaukset varmistavat, että kaikki graafitoiminnot, kuten lyhimmän reitin laskenta Dijkstran algoritmilla ja liikkuvien kohteiden reittien optimointi IDA\*-algoritmilla, toimivat oikein ja tehokkaasti. Testit takaavat, että _utils.graph_-moduuli vastaa tarkasti tarpeitaan.

## Suorituskykytestaus

Suorituskykytestaus on vielä kesken, mutta olen luonut yksinkertaisia testejä vertaillaksemme IDA\*-algoritmin ja Dijkstran algoritmin suorituskykyä eri kokoisilla verkoilla.

Suorituskykytestauksen voi suorittaa seuraavasti:

1. Siirry projektin juureen.
2. Lataa projektin riippuvuudet komennolla: `poetry install`
3. Suorita testit komennolla: `poetry run invoke benchmark`

## Järjestelmätestaus

Järjestelmätestauksessa sovellus on testattu kokonaisuutena varmistaen, että kaikki luokat ja niiden väliset vuorovaikutukset toimivat oikein.

## Käyttöliittymätestaus

Manuaalisissa käyttöliittymätesteissä on varmistettu, että käyttöliittymä reagoi oikein erilaisiin käyttäjän interaktioihin. Testitapaukset kattavat erilaiset hätätilanteiden lisäykset, responderien valinnat ja reittien näyttämisen käyttöliittymässä.

## Jääneet Ongelmat ja Parannusehdotukset

Sovellus on testattu laajasti, mutta tietyissä ääritilanteissa tai epätyypillisissä käyttäytymisskenaarioissa voi esiintyä odottamattomia ongelmia. Yksi potentiaalinen parannuskohde on lisätä vielä laajempi joukko manuaalisia käyttöliittymätestejä, erityisesti käyttäjän vuorovaikutusta testaavia skenaarioita.

Lisäksi voitaisiin harkita automatisoitujen integraatiotestien lisäämistä mahdollisten integraatio-ongelmien välttämiseksi eri komponenttien välillä.

Tässä testausdokumentissa mainitut testaukset ja testikattavuus ovat ajantasaisia tähän hetkeen asti, ja jatkotestauksia tehdään aina sovelluksen uusien versioiden ja päivitysten yhteydessä.
