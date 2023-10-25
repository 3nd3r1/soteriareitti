# Viikko 5
[Tuntikirjanpito](./tunnit.md)

## Miten ohjelma on edistynyt:
- Tällä viikolla dokumentaatio on edennyt paljon. 
- Tärkeä päivitys oli muutos tiemerkintöjen käsittelyssä: nyt aika toimii kaarten painoina etäisyyksien sijaan, mikä parantaa reitinhakualgoritmien tarkkuutta. 
- Lisäksi testausprosessi eteni merkittävästi.

## Mitä opin tällä viikolla:
- Viikon aikana perehdyin syvällisesti reitinhakualgoritmeihin karttaolosuhteissa. Erityisesti Liping Fu'n artikkelin ["Real-time vehicle routing and scheduling in dynamic and stochastic traffic networks"](https://scholar.google.com/scholar?q=Fu%20L.%20Real-time%20vehicle%20routing%20and%20scheduling%20in%20dynamic%20and%20stochastic%20traffic%20networks.%20Unpublished%20Ph.D.%20Dissertation%2C%20University%20of%20Alberta%2C%20Edmonton%2C%20Alberta%2C%201996) lukeminen avasi uusia näkökulmia heuristiikan hyödyntämiseen reitinhaussa.

- Olen myös oppinut arvioimaan ja tulkitsemaan koodia tehokkaammin. Tämän viikon vertaisarvioinnit olivat erityisen hyödyllisiä, sillä toisten koodin lukeminen auttoi ymmärtämään omien ratkaisujen kehittämistä.

## Mikä jäi epäselväksi tai tuotti vaikeuksia:
IDA*-algoritmi on edelleen hyvin hidas Helsingin laajuisissa verkoissa. Pahimmillaan reitinhaku kestää jopa 4 minuuttia. Vaikka olen tyytyväinen siihen, että 95% haut suoritetaan erittäin nopeasti ja tehokkaasti, jatkossa keskityn IDA*-algoritmin optimointiin suurissa kartta-alueissa.

## Mitä teen seuraavaksi:
Ensi viikolla suunnitelmissa on projektin viimeistely ja viimeisten parannusten tekeminen. Tavoitteena on myös viimeistellä dokumentaatio ja luoda ohjelmasta release .exe-tiedosto. Lisäksi aion laajentaa testikattavuutta varmistaakseni sovelluksen luotettavuuden erilaisissa tilanteissa.