# Viikko 6
[Tuntikirjanpito](./tunnit.md)

## Miten ohjelma on edistynyt:
- IDA* algoritmi toimii iteratiivisesti, jotta vältetään Pythonin rekursion raja.
- Lisätty Responderien simulointitoiminnallisuus. Siitä lisää täällä [Käyttöohje](./kayttoohje.md)
- Olen parantanut dokumentaatiota merkittävästi.

## Mitä opin tällä viikolla:

- Kehitin tietämystäni neuroverkoista. Tein vertaisarvion projektista, joka käsitteli neuroverkkoja, vaikka aihe ei ollutkaan aiemmin tuttu. Yhden päivän opiskelun jälkeen ymmärsin riittävästi antaakseni hyvää palautetta, mikä oli erittäin mielenkiintoista.
- Olen nyt perehtynyt syvällisesti IDA*-algoritmiin. Tulin kuitenkin siihen tulokseen, että kaupunkisuunnistuksessa se ei ehkä ole optimaalisin vaihtoehto. Parhain vaihtoehto olisi ollut luultavasti A\* tai Branch Pruning, jos pyritään optimoimaan muistinkäyttöä.


## Mikä jäi epäselväksi tai tuotti vaikeuksia:

- Mielestäni heuristiikkafunktion antaminen argumenttina funktiolle on parempi vaihtoehto kuin monien heuristiikkafunktioiden määrittely suoraan IDA\*-luokassa. Useimmat IDA\*-toteutukset, joita löysin verkosta, antoivat heuristiikkafunktion algoritmille argumenttina. Tällöin ohjelmakoodi pysyy modulaarisena, sillä IDA\*-algoritmia voidaan käyttää täysin eri verkoissa eri heuristiikoilla.
- En ole täysin varma, onko nykyinen suorituskykytestaukseni riittävä. En keksinyt parempaa vertailukohtaa kuin algoritmien käyttämä aika eri kokoisilla verkoilla. Voisi olla järkevää verrata myös muistinkäyttöä, mutta en ole täysin varma, miten sen voisi parhaiten toteuttaa.


## Mitä teen seuraavaksi:

- Yksikkötestauksen on edettävä. Kattavuus on tällä hetkellä melko matala (~70%). Uusien lisäysten yhteydessä en ole muistanut päivittää yksikkötestejä aktiivisesti, joten kattavuus on laskenut.
- Sovelluksen viimeistelyt. Sovellus täytyy viimeistellä palautusta varten.