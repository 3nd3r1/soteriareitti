# Viikko 3

[Tuntikirjanpito](./tunnit.md)

## Miten ohjelma on edistynyt:

- Toinen Prototyyppi Valmis: Toisen prototyypin kehitys on nyt saatu päätökseen. Tällä prototyypillä voi lisätä sairaaloita ja ambulansseja kartalle helposti hiiren oikealla klikkauksella. Lisäksi voi luoda uusia hätätapauksia käyttöliittymän avulla. Sovellus kykenee piirtämään kartalle lyhimmän reitin lähimmästä ambulanssista tai sairaalasta hätätapauksen sijaintiin. On kuitenkin huomattava, että tällä hetkellä voi valita ainoastaan ambulanssin responderiksi, koska muun tyyppisten responderien lisääminen kartalle ei vielä ole mahdollista käyttöliittymän kautta. Tärkeää on myös mainita, että tämä prototyyppi rajoittuu toistaiseksi Töölön alueelle, koska pysyvien tietojen tallentamista kovalevylle ei ole vielä toteutettu.

- Testien Laajentaminen: Olen jatkanut testien kehittämistä, vaikkakin testikattavuus on noussut vain vähän ja on tällä hetkellä 78%. Tämä johtuu siitä, että olen panostanut enemmän toisen prototyypin rakentamiseen aikaresurssien tehokkaan käytön vuoksi. Tulemme kuitenkin jatkamaan testien laajentamista ja parantamista.

- Algoritmien Toteutus: Olen implementoinut sekä IDA*- että Dijkstran algoritmit. IDA*-algoritmi on erityisen hyödyllinen liikkuvien responderien, kuten ambulanssien ja poliisien, reittien etsimisessä, koska se vaatii vähän muistia. Dijkstran algoritmia käytetään stationeiden reittien hakemiseen hätätapausten luo. Sovellus laskee valmiiksi lyhyimmät reitit stationeista (kuten sairaaloista) kaikkiin muihin kartan pisteisiin sekä reitit kaikista pisteistä stationin luo. Tämä mahdollistaa erittäin nopean lyhimmän reitin löytämisen, koska tarvittavat tiedot ovat jo käytettävissä. Koska stationit eivät liiku ja niitä ei ole paljon, tämä ei aiheuta suurta muistinkäyttöä.

## Mitä opin tällä viikolla:

Tämän viikon aikana olen hankkinut arvokasta tietoa seuraavista aiheista:

- Algoritmien Toteutus: Tutustuminen IDA*-algoritmin toteuttamiseen oli haastavaa, mutta samalla opettavaista. Olen saanut syvempää ymmärrystä algoritmien toteutuksesta ja niiden tehokkaasta hyödyntämisestä projektissani.

- Tkinter Käyttöliittymä: Olen perehtynyt Pythonin tkinter-kirjaston käyttöön käyttöliittymän luomiseksi. Tutkin erityisesti customtkinter-nimistä moduulia, jonka avulla voi luoda hienostuneita käyttöliittymiä.

- Testien Laadinta: Testien laatiminen on tullut minulle sujuvammaksi tutkimalla suuria Python-projekteja ja niiden testejä. Olen oppinut tehokkaita testauskäytäntöjä.


## Mikä jäi epäselväksi tai tuottanut vaikeuksia:

Olen myös kohdannut muutamia haasteita viikon aikana:

- IDA-algoritmin Vähäinen Materiaali:* IDA*-algoritmin osalta huomasin, että saatavilla oli vähän verkkomateriaalia. Vaikka ymmärrän, miten IDA* toimii, en löytänyt paljon esimerkkejä sen käytöstä karttareittien hakemiseen. Tämän takia minulla on epävarmuutta siitä, mikä olisi tehokas heuristiikkafunktio tässä projektissa. Tällä hetkellä käytän suoraa etäisyyttä kahden karttapisteen välillä. Harkitsen myös, olisiko A* mahdollisesti parempi vaihtoehto.

- Ohjelmointikielen Valinta: Olen tajunnut, että minulle sopisi paremmin enemmän Olio-orientoitu ohjelmointikieli, kuten C# tai Java, jotka tarjoavat myös parempaa tyyppiturvallisuutta. Python tarjoaa paljon vapautta, mutta olen huomannut, että olen käyttänyt paljon aikaa projektin tyyppiturvallisuuden varmistamiseen ja koodin organisointiin. Päätin kuitenkin jatkaa projektiani Pythonissa.

## Mitä teen seuraavaksi:

Seuraavaksi suunnitelmiini kuuluu seuraavat vaiheet:

- Laajennan testien kattavuutta ja varmistan ohjelman luotettavuuden.

- Aloitan seuraavan prototyypin kehityksen ja lähestyn lopullisen sovelluksen toteuttamista.

Nämä ovat viikon päivitykset SoteriaReitti-sovelluksen kehityksessä. Jatkan tiivistä työtä projektin parissa ja pyrin saavuttamaan asetetut tavoitteet aikataulussa.
