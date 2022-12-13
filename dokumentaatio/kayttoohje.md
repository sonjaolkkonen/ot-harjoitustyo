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
 
![image](https://user-images.githubusercontent.com/117500758/207294228-88c3f8b7-019e-4d76-ac84-eedede00bb94.png)

## Uuden käyttäjän luominen

Alkunäkymästä on mahdollisuus siirtyä luomaan uusi käyttäjätunnus. Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Luo tunnus" -painiketta: 

![image](https://user-images.githubusercontent.com/117500758/207294302-ffa73e16-562d-4e4c-a122-26595561bf8b.png)

 ## Kirjautuminen
 
 Mikäli käyttäjällä on jo tunnus, voi hän siirtyä suoraan kirjautumaan sovellukseen sisään. Kirjautuminen onnistuu kirjoittamalla olemassa oleva käyttäjätunnus sekä salasana syötekenttiin, ja painamalla "Kirjaudu" -painiketta: 
 
![image](https://user-images.githubusercontent.com/117500758/207294761-29bca31e-8d20-486c-a9b8-c9df9c2cb264.png)

## Aloitusvalikko

Kirjautumisen, rekisteröinnin tai kirjautumatta jatkamisen jälkeen pelaaja voi valita aloittavansa uuden pelin tai katsoa pelitilastoja painamalla kyseisiä painikkeita: 

![image](https://user-images.githubusercontent.com/117500758/207294387-40659e5c-a3c9-4a50-a317-fe8e685c4a42.png)

## Vaikeustason valinta

Mikäli pelaaja valitsee edellisessä näkymässä aloittaa uuden pelin, aukeaa hänelle näkymä, jossa pelaaja voi määritellä uuden pelin vaikeustason painamalla kyseisen tason painiketta:

![image](https://user-images.githubusercontent.com/117500758/207294441-20d54f12-1786-499c-8a0b-0bf168e3f920.png)

## Sudoku-peli

Vaikeustason valittuaan pelajaalle aukeaa vaikeustason mukainen uusi Sudoku-peli. Pelaaja voi lisätä numeroita ruudukkoon klikkaamalla tyhjää ruutua ja syöttämällä numero 1-9 välillä. Jo laitettuja numeroita voi vaihtaa klikkaamalla ruutua uudestaan ja syöttämällä uuden numeron. Syötetyn numeron voi myös poistaa kokonaan klikkaamalla kyseistä ruutua ja painamalla 0-näppäintä. Alussa annettuja numeroita ei voi muokata eikä poistaa. Mustat numerot on alussa valmiiksi annettuja numeroita ja siniset numerot ovat pelaajan itse syöttämiä numeroita. Peli jatkuu niin kauan kunnes kaikki numerot on syötetty oikein Sudokun sääntöjä noudattamalla. 

![image](https://user-images.githubusercontent.com/117500758/207294549-b432e723-8d1b-475f-bd55-24fac83d6347.png)

## Loppunäkymä

Pelaajan ratkaistua Sudoku-peli oikein, avautuu hänelle loppunäkymä. Loppunäkymästä voi aloittaa uuden pelin tai siirtyä aloitusvalikkoon: 

![image](https://user-images.githubusercontent.com/117500758/207294691-7ac8372a-5c98-4224-954b-d9b817904fe8.png)




