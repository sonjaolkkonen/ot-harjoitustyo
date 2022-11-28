# Vaatimusmäärittely
## Sovelluksen tarkoitus

Sovellus on klassinen sudoku-peli, jota pelataan 9x9 ruudukossa. Sovellusta on mahdollista käyttää useampi käyttäjä, ja he voivat luoda käyttäjätunnuksen sovellukseen pistetilastojen tallentamista varten. Sovellus myös tarjoaa eri vaikeustasoja. 

## Käyttäjät

Sovelluksella on ainoastaan yksi käyttäjärooli eli normaali käyttäjä.

## Perusversion tarjoamat toiminnallisuudet

### Sovelluksen avaaminen

- Kun käyttäjä avaa sovelluksen, käyttäjä voi luoda käyttäjätunnuksen, kirjautua sisään jo olemassaolevalla käyttäjätunnuksella tai jatkaa luomatta käyttäjätunnusta. Jotta pelaajan pisteet tallentuvat pistetilastoihin, tulee hänen luoda käyttäjätunnus. Mikäli pelaaja ei luo käyttäjätunnusta, siirtyy hän suoraan aloitusvalikkoon.
- Mikäli käyttäjä valitsee käyttäjätunnuksen luomisen, tulee hänen luoda käyttäjätunnus, joka ei ole vielä muilla käytössä, ja joka on 3-10 merkkiä pitkä. 
- Käyttäjätunnuksen luomisen jälkeen käyttäjä voi kirjautua sovellukseen. Mikäli käyttäjälle oli jo luotuna käyttäjätunnus, siirtyy hän tähän kohtaan. Kirjautuminen onnistuu syöttämällä käyttäjätunnus ja salasana kirjautumislomakkeelle. Jos käyttäjää ei ole olemassa tai salasana on virheellinen, herjaa järjestelmä tästä.
- Kirjautumisen jälkeen käyttäjä siirtyy aloitusvalikkoon. 

### Aloitusvalikko

- Aloitusvalikossa käyttäjä voi valita haluaako aloittaa uuden pelin vai katsoa pistetilastoja. (TEHTY näkymä) 
- Mikäli käyttäjä on kirjautuneena sisään, voi hän aloitusvalikossa kirjautua ulos sovelluksesta.

### Pistetilastot

- Jos käyttäjä valitsee pistelistan, näytetään käyttäjälle listana top10 eniten pisteitä saanutta pelaajaa per vaikeustaso.
- Käyttäjä näkee pistetilastosta myös omien peliensä tilastoja. Nämä tiedot näkyvät myös kirjautumattomille käyttäjille. 
- Pistetilastosta voi palata takaisin aloitusvalikkoon.

### Uuden pelin aloittaminen

- Uutta peliä aloittaessa käyttäjä voi valita pelin vaikeustason: helppo, keskivaikea, vaikea. 

### Pelinäkymä

- Sovellus luo käyttäjälle pelattavaksi hänen antamansa vaikeustason mukaisen sudokun. Valmiiksi annettujen numeroiden määrä riippuu vaikeustasosta. (TEHTY) 
- Pelin aloittaminen käynnistää myös ajanoton, ja pelaamiseen kulunut aika on näkyvillä ruudulla koko pelin ajan. Ajanottoa käytetään pistetilastojen luomiseen, mitä nopeammin käyttäjä ratkaisee pelin, sitä enemmän hän saa pisteitä.
- Pelaaja syöttää numeroita ruudukkoon, kunnes kaikissa ruuduissa on numero. (TEHTY)
- Kun pelaaja on saanut ratkaistua ruudukon oikein, ilmoittaa sovellus tästä sekä ajanotto pysäytetään. Pelaaja näkee saamansa pisteet, ja ne talletetaan pistetaulukkoon. 
- Pelaaja voi myös lopettaa sudokun kesken ja palata aloitusvalikkoon tai aloittaa uuden pelin suoraan pelinäkymästä. 

## Jatkokehitysideat

-   Käyttäjä voi käyttää tietyn määrän vinkkejä per peli, esimerkiksi 3. Vinkki paljastaa kyseiseen ruutuun tulevan oikean numeron.
-   Käyttäjä voi tallentaa kesken jääneen pelin ja palata seuraavalla kerralla siihen mihin jäi. 
-   Jos käyttäjä ei saa sudokua valmiiksi, sovellus tarjoaa mahdollisuuden nähdä oikean ratkaisun.
