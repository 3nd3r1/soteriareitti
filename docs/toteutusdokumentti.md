# Testausdokumentti (kesken)

## Ohjelman Yleisrakenne

SoteriaReitti-sovellus on suunniteltu modulaariseksi ja selkeäksi, mikä mahdollistaa eri komponenttien tehokkaan toiminnan yhdessä. Sovellus koostuu useista pääkomponenteista, kuten Emergency, Responders, Station, UtilsGeo ja UtilsGraph. Jokainen komponentti vastaa tietystä osa-alueesta hätätilanteiden hallinnassa, reittien laskennassa ja sijaintien käsittelyssä.

Tähän kohtaan lisätään luokka-diagrammi.

## Saavutetut Aika- ja Tilavaativuudet

### Dijkstra - analyysi

Tähän dijkstran pseudokoodi ja sen analysointi

### IDA\* - analyysi

Tähän idan pseudokoodi ja sen analysointi

### Suorituskyky

Suorituskyky testausta ei ole vielä toteutettu.

**HUOM**
IDA\*-algoritmin toteutus ei ole vielä lopullisessa muodossaan ja on tällä hetkellä varsin hidas. Verkko on painotettu vain etäisyyksillä, mutta se tullaan päivittämään huomioimaan myös matkustamiseen vaadittua aikaa.

## Työn Mahdolliset Puutteet ja Parannusehdotukset

Sovelluksen käytettävyydessä ja tehokkuudessa voi olla vielä parantamisen varaa tietyissä tilanteissa, erityisesti suurilla kartta-alueilla. Lisäksi käyttöliittymää voisi kehittää tarjoamaan enemmän visuaalista informaatiota käyttäjälle, kuten reittien näyttämisen animoituna kartalla.

## Lähteet

Sovelluksen kehityksessä on hyödynnetty seuraavia lähteitä:

-   Pythonin virallinen dokumentaatio: [python.org](https://python.org)
-   Tkinterin dokumentaatio: [tkdocs.com](https://tkdocs.com)
-   Customtkiner dokumentaatio: [customtkinter.com](https://customtkinter.tomschimansky.com/)
-   IDA* Wikipedia: [wikipedia.com](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
-   OSM Wiki: [wiki.openstreetmap.org](https://wiki.openstreetmap.org/)
-   Overpy Docs: [readthedocs.io](https://python-overpy.readthedocs.io/en/latest/)
