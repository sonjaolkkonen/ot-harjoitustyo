# Käyttöohje

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla: 

```
 poetry install
 ```
 Tämän jälkeen voit käynnistää ohjelman komennolla: 
 
 ```
 poetry run invoke start
 ```
 ## Alkunäkymä
 
Sovellus käynnistyy näkymään, josta käyttäjä voi luoda uuden käyttäjätunnuksen, kirjautua sisään jo olemassaolevalla tunnuksella tai jatkaa pelaamaan kirjautumatta: 
 
 ![image](https://user-images.githubusercontent.com/117500758/207288975-a0765074-6346-45e5-b745-db7153e8b0db.png)

## Uuden käyttäjän luominen

Alkunäkymästä on mahdollisuus siirtyä luomaan uusi käyttäjätunnus. Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Luo tunnus" -painiketta: 

![image](https://user-images.githubusercontent.com/117500758/207289314-db56b6c9-d9e5-4a98-8ea1-45a45380c321.png)


 ## Kirjautuminen
 
 Mikäli käyttäjällä on jo tunnus, voi hän siirtyä suoraan kirjautumaan sovellukseen sisään. Kirjautuminen onnistuu kirjoittamalla olemassa oleva käyttäjätunnus sekä salasana syötekenttiin, ja painamalla "Kirjaudu" -painiketta: 
 
 ![image](https://user-images.githubusercontent.com/117500758/207289934-cc341b38-a6cd-4e96-bb1b-316f88eb01a1.png)

## Aloitusvalikko

Kirjautumisen, rekisteröinnin tai kirjautumatta jatkamisen jälkeen pelaaja voi valita aloittavansa uuden pelin tai katsoa pelitilastoja painamalla kyseisiä painikkeita: 

![image](https://user-images.githubusercontent.com/117500758/207290386-854f8793-f06d-49bc-a0b8-7de92b63c648.png)

## Vaikeustason valinta

Mikäli pelaaja valitsee edellisessä näkymässä aloittaa uuden pelin, aukeaa hänelle näkymä, jossa pelaaja voi määritellä uuden pelin vaikeustason painamalla kyseisen tason painiketta:

![image](https://user-images.githubusercontent.com/117500758/207290626-677b8051-11ae-4f4a-bdb2-ff3e01bebc1e.png)

## Sudoku-peli

Vaikeustason valittuaan pelajaalle aukeaa vaikeustason mukainen uusi Sudoku-peli. Pelaaja voi lisätä numeroita ruudukkoon klikkaamalla tyhjää ruutua ja syöttämällä numero 1-9 välillä. Jo laitettuja numeroita voi vaihtaa klikkaamalla ruutua uudestaan ja syöttämällä uuden numeron. Syötetyn numeron voi myös poistaa kokonaan klikkaamalla kyseistä ruutua ja painamalla 0-näppäintä. Alussa annettuja numeroita ei voi muokata eikä poistaa. Mustat numerot on alussa valmiiksi annettuja numeroita ja siniset numerot ovat pelaajan itse syöttämiä numeroita. Peli jatkuu niin kauan kunnes kaikki numerot on syötetty oikein Sudokun sääntöjä noudattamalla. 

## Loppunäkymä

Pelaajan ratkaistua Sudoku-peli oikein, avautuu hänelle loppunäkymä. Loppunäkymästä voi aloittaa uuden pelin tai siirtyä aloitusvalikkoon: 
![image](https://user-images.githubusercontent.com/117500758/207293802-68ba5b51-9f6a-4011-8224-d21baca8fd4f.png)
![image](https://user-images.githubusercontent.com/117500758/207293558-f2b10c38-8376-4b7c-a432-2fe7c7025a9e.png)


![image](https://user-images.githubusercontent.com/117500758/207291441-3e93d590-9154-4919-96a5-0cd85fa2d829.png)



