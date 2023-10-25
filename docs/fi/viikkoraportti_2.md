# Viikko 2

[Tuntikirjanpito](./tunnit.md)

## Miten ohjelma on edistynyt:

Ohjelma on edistynyt merkittävästi viikon aikana. Olen saavuttanut useita tärkeitä osa-alueita:

-   Projektin alustus: Projekti on nyt alustettu huolellisesti käyttäen Pylint-tarkistusta ja testausta ensisijaisena tavoitteena. Tämä auttaa varmistamaan koodin laadun ja vähentää mahdollisia virheitä tulevaisuudessa.

-   Prototyypin valmistuminen: Olen luonut ensimmäisen toimivan prototyypin SoteriaReitti-sovelluksesta. Prototyyppi mahdollistaa kahden pisteen välisen lyhimmän reitin hakemisen Töölön alueella. Tätä varten olen hyödyntänyt valmiita tietorakenteita ja algoritmeja.

-   Unit-testit: Olen kirjoittanut kattavat yksikkötestit GraphUtils-moduulille. Tämä auttaa varmistamaan, että tietorakenteet ja algoritmit toimivat oikein ja tuottavat odotetut tulokset. Testien lisääminen on tärkeä askel kohti luotettavaa ohjelmistoa.

-   Käyttöliittymän suunnittelu: Olen tehnyt suunnittelutyötä käyttöliittymän parissa ja hahmotellut, kuinka käyttäjät voivat valita kaksi pistettä kartalta, joiden välisen reitin haluavat nähdä. Tämä on tärkeä osa sovelluksen käytettävyyttä.

Tulevina viikkoina keskityn prototyypin laajentamiseen ja kehittämiseen, liikennetiedon integrointiin ja edistyneempien reitinhakualgoritmien implementointiin. Lisäksi jatkan käyttöliittymän parissa työskentelyä ja huolehdin siitä, että ohjelma on helppokäyttöinen ja intuitiivinen.

## Mitä opin tällä viikolla:

Viime viikolla sain mahdollisuuden syventää osaamistani useilla tärkeillä osa-alueilla:

-   Overpass API:n käyttö: Opin käyttämään Overpass API:a ja luomaan Overpass-kyselyjä. Tämä taito on olennainen osa projektiamme, koska se mahdollistaa liikennetietojen hakemisen ja käsittelyn reittien optimoinnissa. Overpass API:n käytön ymmärtäminen auttaa minua saamaan tarvittavat tiedot tehokkaasti ja tarkasti.

-   Python-luokkien syvemmät ominaisuudet: Kävin läpi python-luokkien erilaisia ominaisuuksia, kuten **iter**-metodin käytön ja attribuuttien käsittelyn. Tämä auttaa minua rakentamaan selkeärakenteista ja helposti ylläpidettävää koodia projektissamme.

-   Python-projektistandardit: Tutkin erilaisia isoja Python-projekteja ja niiden käyttämiä standardeja, kuten kansioiden rakennetta ja hyvien käytäntöjen noudattamista. Olen saanut käsityksen siitä, kuinka laadukas Python-projekti organisoidaan ja kuinka se noudattaa yleisiä standardeja, kuten kattavuusbadgen käyttöä.

Nämä oppimiskokemukset ovat arvokkaita, kun pyrin kehittämään SoteriaReitti-sovellusta ja pitämään sen korkealla laadulla ja standardien mukaisena. Olen innokas soveltamaan näitä oppeja projektissamme ja auttamaan sen kehittämisessä.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia:

Viime viikolla kohtasin useita haasteita, joista osa jäi osittain epäselväksi tai vaativat lisäselvitystä:

-   Type safety Pythonissa: Olen pohtinut, miten varmistaa type safety Pythonissa ilman kovakoodausta, kuten isinstance-metodia. Haluaisin varmistaa, että koodissani tietotyypit ovat oikein ja että argumentit vastaavat odotettuja tietotyyppejä, mutta en ole vielä keksinyt täydellistä ratkaisua tähän.

-   Koodin jakaminen luokkiin ja tiedostoihin: Olen huomannut, että koodin jakaminen useisiin luokkiin ja tiedostoihin voi olla haastavaa, erityisesti kun tietyt tiedostot, kuten utils_graph ja utils_geo, kasvavat suuriksi. Mietin, miten voisin organisoida koodin paremmin ja pitää tiedostot hallittavina.

-   Testien suunnittelu: Olen kohdannut haasteita hyvien testien suunnittelussa. Osa testeistä saattaa tuntua tarpeettomilta, kun taas toiset ovat erittäin monimutkaisia tilanteita varten. Haluan varmistaa, että testit kattavat olennaiset osat koodista, mutta tasapainon löytäminen yksinkertaisuuden ja kattavuuden välillä voi olla hankalaa.

Nämä ovat asioita, joita aion edelleen tutkia ja ratkaista projektin edetessä. Pyrin löytämään parhaita käytäntöjä ja ratkaisuja näihin haasteisiin, jotta voin kehittää SoteriaReitti-sovellusta laadukkaasti ja tehokkaasti.

## Mitä teen seuraavaksi:

Seuraavalla viikolla tavoitteena on jatkaa prototyypin kehittämistä ja laajentamista. Haluan parantaa sovelluksen toiminnallisuutta ja lisätä testien kattavuutta varmistaakseni, että se toimii luotettavasti.

Lisäksi suunnitelmiin kuuluu tarkempi suunnitelma itse koodin rakenteesta ja luokkakaavio (class diagram), joka auttaa hahmottamaan sovelluksen arkkitehtuuria. Tavoitteena on saada vahva perusta, jotta voin edetä kohti lopullista sovellusta.
