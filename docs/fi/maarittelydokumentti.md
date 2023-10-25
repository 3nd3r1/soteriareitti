# SoteriaReitti - Määrittelydokumentti

SoteriaReitti on Pythonilla toteutettava sovellus, joka on suunniteltu hätätyöntekijöille. Sovellus auttaa heitä löytämään parhaat mahdolliset reitit hätätilanteissa ja ruuhkaisilla teillä. SoteriaReitti tulee kreikasta ja tarkoittaa pelastuksen tietä, mikä kuvastaa projektin ydintavoitetta: tarjota pelastava reitti niille, jotka sitä tarvitsevat.

## Ohjelmointikieli ja Muut Kielet
### Ohjelmointikieli:
SoteriaReitti-projekti toteutetaan pääasiassa Python-ohjelmointikielellä. Python tarjoaa monipuolisen valikoiman kirjastoja ja työkaluja datan käsittelyyn, verkkorakenteiden rakentamiseen ja reitinhakuun, mikä tekee siitä ihanteellisen kielen tähän projektiin. 

Projektin alkuvaiheessa keskitytään komentorivitoiminnallisuuteen, ja myöhemmin toteutetaan Tkinter-pohjainen tai Django-pohjainen graafinen käyttöliittymä (GUI).

Jos käytössä on Tkinter-pohjainen käyttöliittymä voidaan käyttää [TkinterMapViewtä](https://github.com/TomSchimansky/TkinterMapView)

**Muut ohjelmointikielet joita hallitsen:** Javascript, Python

### Kirjakielet:
Projektissa keskitytään pääasiassa suomen kieleen dokumentaation osalta. Koodi ja siihen liittyvät nimet, kuten muuttujat ja funktiot, kirjoitetaan pääosin englanniksi. Koodin kommentit kirjoitetaan myös englanniksi varmistaen näin hyvän yhteistyön ja avoimen kommunikaation projektin eri vaiheissa.

## Algoritmit ja Tietorakenteet
### Algoritmit
Pääasiallisina reittinhakualgoritmeina käytetään Dijkstra'n algoritmia ja IDA* (Iterative Deepening A*). Näiden kahden algoritmin valinta perustuu seuraaviin perusteluihin:

- **Dijkstra'n algoritmi**: Dijkstra'n algoritmi on laajalti käytetty lyhimmän polun etsintäalgoritmi, joka toimii painotetussa verkossa. Tämä algoritmi soveltuu erityisesti tilanteisiin, joissa tarvitaan tarkan ja optimaalisen reitin etsintää. Dijkstra'n algoritmi pystyy laskemaan lyhimmän reitin kaikille mahdollisille kohteille lähtöpisteestä. [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

- **IDA\* (Iterative Deepening A\*)**: IDA\* on tehokas algoritmi, joka löytää lyhimmän reitin lähtöpisteestä määränpäähän, mutta se tekee sen iteratiivisesti ja käyttää vähemmän muistia kuin perinteinen A\* algoritmi. IDA\* on hyvä valinta, kun tarvitaan nopeita reittihakuja reaaliajassa, ja muistin käyttö on rajoitettua. [Wikipedia](https://en.wikipedia.org/wiki/Iterative_deepening_A*)

### Tietorakenteet
SoteriaReitti-sovelluksessa hyödynnetään kekorakenteita ja erilaisia verkkorakenteita, jotka perustuvat liikennetietoihin ja reitinetsintään. Kekorakenteet ovat keskeinen osa Dijkstra'n algoritmin toimintaa, kun taas verkkorakenteet auttavat tehokkaassa reitinetsinnässä.

## Aika- ja tilavaativuudet:

Dijkstra'n algoritmin aikavaativuus riippuu verkoston koosta ja rakenteesta, mutta se voi olla $O(V^2)$ tai $O(E + V \cdot log(V))$, missä $V$ on solmujen määrä ja $E$ on kaarten määrä verkossa.

IDA* algoritmi perustuu A* algoritmiin, ja sen aikavaativuus riippuu heuristiikan laadusta ja tilavaativuus riippuu rekursiivisten kutsujen syvyydestä. Tyypillisesti IDA* on tilavaativuudeltaan parempi kuin A*, mutta se voi olla hitaampi, koska se tekee saman työn iteratiivisesti useaan otteeseen.

Lisäksi OSM (OpenStreetMap) datan lukeminen view jonkin verran aikaa ja muistia.

## Syötteet:

SoteriaReitti-sovelluksessa on useita syötteitä, jotka auttavat määrittämään hätätilanteen parametrit ja reitinetsintäparametrit. Syötteet sisältävät seuraavat tiedot:

- Hätätilanteen sijainti: Käyttäjä antaa hätätilanteen sijainnin, joko koordinaatteina tai osoitteena. Tämä on lähtöpiste, josta reitinetsintä alkaa.

- Hätätilanteen tyyppi: Käyttäjä määrittelee hätätilanteen tyypin, esimerkiksi sydänkohtaus, onnettomuus, tulipalo jne. Jokaiselle hätätilanteelle voi olla erilaiset reitinetsintäparametrit.

- Reitinoptimointi: Käyttäjä voi valita haluamansa reitinoptimointialgoritmin (esimerkiksi Dijkstra, IDA*). Jokaisella algoritmilla voi olla erilaiset tulokset ja parametrit.

Sovellus ottaa nämä syötteet huomioon ja käyttää niitä reitinetsinnän aloittamiseen. Hätätilanteen luonteen ja hätäajoneuvon tyyppi vaikuttavat siihen, miten reitti optimoidaan. Sovelluksen tehtävänä on etsiä nopein ja tehokkain reitti hätätilanteen sijaintiin sekä hätätilanteen sijainnista eteenpäin, esimerkiksi sairaalaan, mikäli kyseessä on ambulanssi. Tavoitteena on tarjota mahdollisimman nopea ja sujuva reittiohje hätätilanteiden hoitohenkilöstölle, jotta he voivat saapua kohteeseen nopeasti ja turvallisesti.

### Ulkoista dataa

SoteriaReitti-sovelluksen kehityksen alkuvaiheessa keskitytään Helsingin kaupunkiin, ja se hyödyntää erityisesti Helsingissä sijaitsevia palveluja ja tietolähteitä. Tämä mahdollistaa tehokkaan reittien suunnittelun ja optimoinnin hätätilanteissa Helsingin alueella. Tässä on joitakin keskeisiä ulkoisen datan lähteitä:

- Liikennetietojen Lähde: Sovellus saa ajantasaista liikennetietoa eri reittiosuuksilta. Tämä tieto voi tulla erilaisista liikennevirastoista tai palveluntarjoajista, kuten kaupungin liikennetietopalveluista tai liikennedataa tarjoavista yrityksistä. Esimerkiksi [Helsingin kaupunki](https://hri.fi/data/fi/dataset/liikennemaarat-helsingissa) voi tarjota liikennetietojaan avoimen datan rajapinnan kautta. 

- Karttatietojen Lähde: Karttatiedot ovat olennainen osa reittien suunnittelua. Sovellus voi käyttää karttatietoja, jotka tulevat avoimen karttadatan lähteistä, kuten [OpenStreetMap](https://www.openstreetmap.org) (OSM). OSM tarjoaa laajan tietokannan karttatietoja, kuten katujen sijainnit, liikennemerkit ja maantieteelliset piirteet. 

- Reittidata ja Osoitetiedot: Saadakseen tietoa reittiosuuksista ja osoitteista, sovellus voi hyödyntää julkisia reittidataa tarjoavia rajapintoja, kuten [Nominatim](https://nominatim.openstreetmap.org/ui/search.html). Näitä tietoja voidaan käyttää reittien suunnitteluun ja osoitteiden tunnistamiseen.

- Hätäpalvelujen Tiedot: Tietoja eri hätäpalveluista, kuten sairaaloista, paloasemista ja poliisiasemista, voidaan saada suoraan virallisilta hätäpalvelujen organisaatioilta. Sovellus voi hyödyntää näitä tietoja tarjotakseen käyttäjille reittejä näihin tärkeisiin kohteisiin hätätilanteissa. Lisäksi on mahdollista harkita reaaliaikaisen hälytysajoneuvojen sijainnin seuraamista tulevaisuudessa. Projektin alkuvaiheessa suurin osa tiedoista syötetään manuaalisesti, kunnes automatisoidut tiedonkeruujärjestelmät voidaan integroida osaksi sovellusta.

Nämä ulkoisen datan lähteet ja rajapinnat ovat keskeisiä SoteriaReitti-sovelluksen toiminnassa. Ne mahdollistavat reaaliaikaisen ja tarkan reittien optimoinnin hätätilanteissa ottaen huomioon liikennetiedot, karttatiedot ja tarvittavat kohteet.

## Muuta

- **Opinto-ohjelma:** tietojenkäsittelytieteen kandidaatti (TKT)
- **Muut ohjelmointikielet joita hallitsen:** Javascript, Python
