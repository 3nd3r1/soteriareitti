# Viikko 1

[Tuntikirjanpito](./tunnit.md)

## Mitä olen tehnyt tällä viikolla:

Tällä viikolla SoteriaReitti-sovelluksen parissa on edistytty seuraavasti:

- Algoritmin valinta: Pohdimme aktiivisesti sopivia reitinhakualgoritmeja, jotka soveltuvat parhaiten hätäpalvelujen reittien hakemiseen Helsingin kaupungin liikenteessä. Olemme päätyneet keskittymään Dijkstran algoritmiin ja IDA*-algoritmiin, koska ne vaikuttavat soveltuvan hyvin tähän tarkoitukseen.

- Liikennetiedon keruu: Tutkimme erilaisia liikennetiedon lähteitä ja rajapintoja, joita voimme käyttää reittien optimoinnissa. Pohdimme myös, kuinka voimme integroida reaaliaikaista liikennetietoa osaksi sovellusta tulevaisuudessa.


## Miten ohjelma on edistynyt:

Vaikka suuri osa työstä on ollut suunnittelua ja valmistelua, olemme edistyneet kohti selkeää suunnitelmaa siitä, miten ohjelmaa rakennetaan. Algoritmien valinta on edennyt, ja olemme aloittaneet pohjatiedon keruun liikenteestä.

## Mitä opin tällä viikolla:

Opin tällä viikolla useita kiinnostavia asioita, jotka liittyvät projektimme kehitykseen. Erityisesti olen oppinut:

Karttatietojen käsittelystä: Olen syventynyt siihen, miten karttatietoja voidaan lukea ja muuntaa käyttökelpoiseksi verkkorakenteeksi. Olen tutustunut erilaisiin tiedonhankintamenetelmiin ja datalähteisiin, jotka voivat olla hyödyllisiä hätäreittien optimoinnissa.

Navigaattoreiden toimintaperiaatteista: Olen tutkinut navigaattoreiden toimintaa ja niiden käyttämiä reitinhakualgoritmeja. Tämä tieto auttaa meitä suunnittelemaan ja toteuttamaan tehokkaan reitinhakualgoritmin SoteriaReitti-sovellukseemme.

VRP-ongelmasta: Olen perehtynyt VRP-ongelman (Vehicle Routing Problem) perusteisiin ja ymmärtänyt, miten se liittyy ajoneuvojen reitityksen optimointiin. Vaikka VRP ei ole suoraan osa projektiamme, se antoi minulle syvemmän käsityksen reititysongelmista ja niiden ratkaisemisesta.

Nämä oppimiskokemukset ovat auttaneet minua hahmottamaan projektimme vaatimuksia ja antaneet selkeämmän suunnan siitä, mitä meidän tulee saavuttaa seuraavien viikkojen aikana.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia:

Yksi keskeinen haaste, joka jäi osittain epäselväksi, liittyy OSM-tietojen (OpenStreetMap) muuntamiseen tehokkaaksi ja realistiseksi tieliikenteen verkkorakenteeksi. Vaikka olemme edistyneet asiassa, meidän täytyy vielä harkita, miten voimme tehdä tämän nopeasti ja optimaalisesti. OSM-tietojen, erityisesti "nodes" ja "ways," käsittelyssä on tullut vastaan monimutkaisia tietorakenteita, ja niiden tehokas muuntaminen verkoksi vaatii edelleen lisäpohdintaa.

## Mitä teen seuraavaksi:

Seuraavalla viikolla tavoitteenamme on tehdä konkreettista ohjelmointityötä ja saada aikaan toimiva sovellus, joka perustuu valittuihin algoritmeihin ja kerättyihin tietoihin. Erityisesti keskitymme siihen, että olemme luoneet Helsingin tieliikenteestä verkkorakenteen ja pystymme löytämään lyhyimmän reitin pisteestä A pisteeseen B. Tämä on kriittinen askel projektissamme, ja tavoitteena on saavuttaa toimiva perusta, jota voimme edelleen kehittää ja laajentaa.

Lisäksi suunnitelmiin kuuluu tehdä tarkempi suunnitelma itse koodin rakenteesta ja luoda luokkakaavio (class diagram), joka auttaa hahmottamaan sovelluksen arkkitehtuuria. Tämä auttaa meitä pitämään projektin hallinnassa ja varmistamaan, että koodi on järjestelmällistä ja helposti ymmärrettävää. 