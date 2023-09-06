# TransitXpert - Määrittelydokumentti

TransitXpert on joukkoliikenteen reittien optimointisovellus, jonka avulla kaupunkien omistajat ja joukkoliikennepalvelujen tarjoajat voivat suunnitella tehokkaita bussireittejä. Sovellus yhdistää käyttäjien tarpeet, matkustusvaatimukset ja joukkoliikenteen resurssit tarjoten älykkään reittien optimoinnin.

## Ohjelmointikieli

Tämän projektin pääasiallinen ohjelmointikieli on Python. Projektin alkuvaiheessa keskitytään komentorivitoiminnallisuuteen, ja myöhemmin toteutetaan Tkinter-pohjainen graafinen käyttöliittymä (GUI).

## Muut kielet

Dokumentaatiomme pääkieli on suomi. Koodi ja siihen liittyvät nimet, kuten muuttujat ja funktiot, kirjoitetaan pääosin englanniksi, ja kommentit koodissa kirjoitetaan myös englanniksi.

## Algoritmit ja tietorakenteet:

Projektin tavoitteena on suunnitella ja kehittää ohjelmisto kaupunkien bussireittien suunnitteluun ja optimointiin.

Projektissa käytetään useita algoritmeja ja tietorakenteita, mukaan lukien heuristisia ratkaisuja ja lähes optimoituja ratkaisuja VRP-ongelman (Vehicle Routing Problem) ratkaisemiseen.

VRP on lyhenteenä Vehicle Routing Problem, ja se on NP-vaikea ongelma, joka esiintyy monissa käytännön tilanteissa, kuten joukkoliikenteen suunnittelussa. Ongelma liittyy siihen, miten joukkoliikennevälineitä, kuten busseja, käytetään tehokkaasti ja taloudellisesti reittien suunnittelussa. Tavoitteena on löytää optimaaliset reitit kaikille liikennevälineille kattamaan kaikki matkasuunnitelmat.

VRP Ongelmasta lisää tietoa [Wikipediasta](https://en.wikipedia.org/wiki/Vehicle_routing_problem)

### Projektissa käytettävät päätösalgoritmit ja tietorakenteet sisältävät seuraavat:

-   Clarke-Wright -säästöalgoritmi (Clark & Wright Savings Algorithm) reittien alustavaan luomiseen. Lisää [täältä](https://iopscience.iop.org/article/10.1088/1742-6596/2421/1/012045/pdf)
-   Lähimmän naapurin algoritmi reittien optimointiin. Lisää [Wikipediasta](https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm)
-   Geneettinen algoritmi. Lisää [Wikipediasta](https://en.wikipedia.org/wiki/Genetic_algorithm)

## Aika- ja Tilavaativuudet:

Projektin tavoitteena on luoda tehokas ja nopea reittien optimointiohjelma. Aikavaativuuksien ja tilavaativuuksien tarkempi analyysi suoritetaan projektin edetessä.

## Syötteet

Ohjelma saa syötteenä tietoja kaupunkien bussireiteistä, kuten pysäkit ja niihin liittyvät matkat. Tietoja voidaan antaa tekstitiedostojen tai käyttöliittymän kautta.

### Käyttäjän valinta ja tulosten vertailu:

Ohjelmiston käyttäjälle tarjotaan mahdollisuus valita erilaisia algoritmeja ja asettaa erilaisia tavoitteita reittien optimoinnille. Käyttäjä voi esimerkiksi valita Clarke-Wright -algoritmin ja asettaa tavoitteeksi minimoida kuljetuskustannuksia, tai valita lähimmän naapurin -algoritmin ja asettaa tavoitteeksi minimoida reittien pituutta.

Ohjelmisto tuottaa käyttäjän valintojen perusteella erilaisia reittiehdotuksia, ja käyttäjä voi vertailla näitä ehdotuksia eri algoritmien ja tavoitteiden perusteella. Tämä mahdollistaa eri reittien ja ratkaisujen vertailun ja auttaa käyttäjää valitsemaan parhaiten tarpeisiinsa sopivan ratkaisun.

## Lähteitä

-   https://en.wikipedia.org/wiki/Vehicle_routing_problem
