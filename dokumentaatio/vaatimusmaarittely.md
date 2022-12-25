# Vaatimusmäärittely
## Sovelluksen tarkoitus

Sovellus on klassinen sudoku-peli, jota pelataan 9x9 ruudukossa. Ruudukko on jaettu vielä 3x3 aliruudukoihin. Pelin alkaessa osa ruudukon numeroista on annettu valmiiksi, ja tavoitteena on täyttää loput ruudut numeroilla 1-9 mahdollisimman nopeasti. Kukin numero saa esiintyä vain kerran sekä vaaka- että pystyrivillä. Lisäksi kukin numero saa esiintyä vain kerran jokaisessa 3x3 aliruudukossa. Sovellus myös tarjoaa eri vaikeustasoja, ja alussa annettujen numeoroiden määrä riippuu valitusta vaikeustasosta.  

## Käyttäjät

Sovelluksella on ainoastaan yksi käyttäjärooli eli normaali käyttäjä.

## Perusversion tarjoamat toiminnallisuudet

### Aloitusvalikko

- Sovellus avautuu aloitusvalikkoon, josta käyttäjä voi aloittaa uuden pelin.  

### Uuden pelin aloittaminen

- Uutta peliä aloittaessa käyttäjä voi valita pelin vaikeustason: helppo, keskivaikea, vaikea. Mitä vaikeampi taso, sitä vähemmän on annettu numeroita valmiiksi pelin alkaessa. 

### Pelinäkymä

- Sovellus luo käyttäjälle pelattavaksi hänen antamansa vaikeustason mukaisen sudokun. Valmiiksi annettujen numeroiden määrä riippuu vaikeustasosta eli mitä vaikeampi taso, sitä vähemmän numeroita on annettu valmiiksi. 
- Pelin aloittaminen käynnistää myös ajanoton, jota käytetään pistetilastojen luomiseen. Mitä nopeammin käyttäjä ratkaisee pelin, sitä vähemmän hän saa pisteitä. Tavoitteena on saada mahdollisimman alhaiset pisteet. 
- Pelaaja syöttää numeroita ruudukkoon, kunnes kaikissa ruuduissa on numero.
- Kun pelaaja on saanut ratkaistua ruudukon oikein, ilmoittaa sovellus tästä ja pelaaja näkee saamansa pisteet. Pelaajan saamat pisteet talletetaan pistetilasoihin.
- Loppunäkymässä pelaaja näkee myös TOP 5 parhaimmat pisteet sekä hän voi aloittaa uuden pelin. 

## Jatkokehitysideat

-   Valittu ruutu korostuu taustavärillä.
-   Ajanotto on näkyvillä pelaajalle pelin aikana. Lisäksi pelin aikana pelaajalla on mahdollisuus aloittaa uusi peli tai sama peli alusta. 
-   Käyttäjä voi käyttää tietyn määrän vinkkejä per peli, esimerkiksi 3. Vinkki paljastaa kyseiseen ruutuun tulevan oikean numeron.
-   Käyttäjä voi tallentaa kesken jääneen pelin ja palata seuraavalla kerralla siihen mihin jäi. 
-   Jos käyttäjä ei saa sudokua valmiiksi, sovellus tarjoaa mahdollisuuden nähdä oikean ratkaisun.
