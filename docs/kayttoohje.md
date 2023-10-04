# SoteriaReitti - Sovelluksen Käyttäminen

SoteriaReitti-sovelluksen käyttäminen on suoraviivaista ja intuitiivista. Seuraavassa on vaiheittainen ohje sovelluksen käyttöön:

## Sovelluksen Konfigurointi
Sovellusta voi konfiguroida .env-tiedoston avulla. Tämä tiedosto mahdollistaa erilaisten asetusten määrittämisen, jolloin voit räätälöidä sovelluksen toimintaa tarpeidesi mukaan. Tässä muutamia keskeisiä asetuksia:

_APP\_PLACE_: Tämä asetus määrittää paikan, jonka perusteella sovellus toimii. Voit muuttaa tätä arvoa vaihtamalla paikan nimen tai koordinaatit. Esimerkiksi voit asettaa sen "Töölö, Helsinki" tai muihin koordinaatteihin, jotka vastaavat aluetta, jolla haluat testata sovellusta.

_CACHING_: Tämä asetus määrittää, tallennetaanko verkkotiedot kovamuistiin vai ei. Jos tämä asetus on `True`, sovellus tallentaa verkon (graph) kovamuistiin, mikä parantaa suorituskykyä toistuvissa käynnistyksissä. Jos asetus on `False`, verkkoa ei tallenneta kovamuistiin, ja se lasketaan uudelleen joka kerta, kun sovellus käynnistetään.

Esimerkki .env tiedosto:

```
APP_PLACE=Töölö
CACHING=True
```

Muista, että .env-tiedosto on herkkä tiedosto, ja siinä ei tulisi olla ylimääräisiä välilyöntejä tai kommentteja. Varmista, että asetusnimet ovat oikein kirjoitettuja ja niiden arvot vastaavat haluamiasi asetuksia. Sovellus lukee nämä asetukset automaattisesti käynnistyessään, joten kun .env-tiedostoa muutetaan, sovellus ottaa nämä muutokset huomioon seuraavalla käynnistyskerralla.

## Sovelluksen Käynnistäminen:

1. Asenna Riippuvuudet:
   Ennen kuin aloitat, varmista, että olet asentanut sovelluksen riippuvuudet komennolla `poetry install`.

2. Käynnistä Sovellus:
   Käynnistä sovellus komennolla `poetry run invoke start`.

**HUOM**: Jos olet konfiguroinnut sovelluksen paikaksi suuren alueen kuten `Helsinki`, sovelluksen käynnistämisessä voi kestää kauan (noin 3 minuuttia).

## Responderien ja Stationeiden Lisääminen:


**Responderit** ovat liikkuvia hätätilanteisiin vastaavia yksiköitä, kuten ambulansseja ja poliisiautoja, jotka voivat reagoida nopeasti ja liikkua paikasta toiseen tarvittaessa. 

**Stationit** ovat paikallaan pysyviä hätätilanteiden vastaajia, kuten sairaaloita ja poliisiasemia, jotka eivät liiku vaan pysyvät tietyissä ennalta määrätyissä paikoissa. Tämä staattinen sijoittuminen tekee niistä tärkeitä tukipisteitä hätätilanteiden hallinnassa ja avunsaannissa.

-   Lisää responderi tai station kartalle klikkaamalla haluttua sijaintia hiiren oikealla painikkeella. Valitse avautuvasta valikosta "Add Responder" tai "Add Station".

-   Avautuvassa ikkunassa valitse responderin tai stationin tyyppi, ja vahvista valinta. Responderi tai station ilmestyy kartalle kyseiseen sijaintiin.

### Hätätilanteen Luominen:

-   Valitse kartalta hätätilanteen sijainti klikkaamalla sitä hiiren vasemmalla painikkeella.
-   Syötä hätätilanteen tiedot sovelluksen vasemmalla olevaan valikkoon.
-   Luo hätätilanne klikkaamalla 'Create' vasemmalla.

Näiden ohjeiden avulla voit hyödyntää SoteriaReitti-sovelluksen tarjoamia reittisuunnittelutoimintoja hätätilanteiden hallinnassa!
