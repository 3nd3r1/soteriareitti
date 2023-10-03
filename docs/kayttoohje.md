# SoteriaReitti - Sovelluksen Käyttäminen

SoteriaReitti-sovelluksen käyttäminen on suoraviivaista ja intuitiivista. Seuraavassa on vaiheittainen ohje sovelluksen käyttöön:

## Sovelluksen Konfigurointi
Sovellusta voi konfiguroida .env-tiedoston avulla. Tämä tiedosto mahdollistaa erilaisten asetusten määrittämisen, jolloin voit räätälöidä sovelluksen toimintaa tarpeidesi mukaan. Tässä muutamia keskeisiä asetuksia:

_APP\_PLACE_: Tämä asetus määrittää paikan, jonka perusteella sovellus toimii. Voit muuttaa tätä arvoa vaihtamalla paikan nimen tai koordinaatit. Esimerkiksi voit asettaa sen "Töölö, Helsinki" tai muihin koordinaatteihin, jotka vastaavat aluetta, jolla haluat testata sovellusta.

_CACHING_: Tämä asetus määrittää, tallennetaanko verkkotiedot kovamuistiin vai ei. Jos tämä asetus on `True`, sovellus tallentaa verkon (graph) kovamuistiin, mikä parantaa suorituskykyä toistuvissa käynnistyksissä. Jos asetus on `False`, verkkoa ei tallenneta kovamuistiin, ja se lasketaan uudelleen joka kerta, kun sovellus käynnistetään.

Esimerkki .env tiedosto:

```
APP_PLACE="Töölö, Helsinki"
CACHING=True
```

Muista, että .env-tiedosto on herkkä tiedosto, ja siinä ei tulisi olla ylimääräisiä välilyöntejä tai kommentteja. Varmista, että asetusnimet ovat oikein kirjoitettuja ja niiden arvot vastaavat haluamiasi asetuksia. Sovellus lukee nämä asetukset automaattisesti käynnistyessään, joten kun .env-tiedostoa muutetaan, sovellus ottaa nämä muutokset huomioon seuraavalla käynnistyskerralla.

## Sovelluksen Käynnistäminen:

1. Asenna Riippuvuudet:
   Ennen kuin aloitat, varmista, että olet asentanut sovelluksen riippuvuudet komennolla `poetry install`.

2. Käynnistä Sovellus:
   Käynnistä sovellus komennolla `poetry run invoke start`.

## Responderien ja Stationeiden Lisääminen:

-   Lisää responderi tai station kartalle klikkaamalla haluttua sijaintia hiiren oikealla painikkeella. Valitse avautuvasta valikosta "Add Responder" tai "Add Station".

-   Avautuvassa ikkunassa valitse responderin tai stationin tyyppi, ja vahvista valinta. Responderi tai station ilmestyy kartalle kyseiseen sijaintiin.

### Hätätilanteen Luominen:

-   Valitse kartalta hätätilanteen sijainti klikkaamalla sitä hiiren vasemmalla painikkeella.
-   Syötä hätätilanteen tiedot sovelluksen vasemmalla olevaan valikkoon.
-   Luo hätätilanne klikkaamalla 'Create Emergency' vasemmalla.

Näiden ohjeiden avulla voit hyödyntää SoteriaReitti-sovelluksen tarjoamia reittisuunnittelutoimintoja hätätilanteiden hallinnassa!