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

## Aloitusvalikko

Sovellus aukeaa aloitusvalikkoon, jossa pelaaja voi valita aloittavansa uuden pelin painamalla kyseistä painiketta: 

![image](https://user-images.githubusercontent.com/117500758/209474635-2308f177-5add-4c95-b20f-9c5d7dc6074d.png)
 
## Vaikeustason valinta

Mikäli pelaaja valitsee edellisessä näkymässä aloittaa uuden pelin, aukeaa hänelle näkymä, jossa pelaaja voi määritellä uuden pelin vaikeustason painamalla kyseisen tason painiketta:

![image](https://user-images.githubusercontent.com/117500758/207294441-20d54f12-1786-499c-8a0b-0bf168e3f920.png)

## Sudoku-peli

Vaikeustason valittuaan pelajaalle aukeaa vaikeustason mukainen uusi Sudoku-peli. Pelaaja voi lisätä numeroita ruudukkoon klikkaamalla tyhjää ruutua ja syöttämällä numero 1-9 välillä. Jo laitettuja numeroita voi vaihtaa klikkaamalla ruutua uudestaan ja syöttämällä uuden numeron. Syötetyn numeron voi myös poistaa kokonaan klikkaamalla kyseistä ruutua ja painamalla 0-näppäintä. Alussa annettuja numeroita ei voi muokata eikä poistaa. Mustat numerot on alussa valmiiksi annettuja numeroita ja siniset numerot ovat pelaajan itse syöttämiä numeroita. Peli jatkuu niin kauan kunnes kaikki numerot on syötetty oikein Sudokun sääntöjä noudattamalla. 

Tavoitteena on täyttää tyhjät ruudut oikeilla numeroilla mahdollisimman nopeasti. Pelaajan saamat pisteet määräytyvät käytetyn peliajan mukaan, eli mitä vähemmän pelaaja käyttää sudokun ratkaisemiseen aikaa, sitä alhaisemmat hänen pisteet ovat. Tavoitteena on saada mahdollisimman alhaiset pisteet. 

![image](https://user-images.githubusercontent.com/117500758/207294549-b432e723-8d1b-475f-bd55-24fac83d6347.png)

## Loppunäkymä

Pelaajan ratkaistua Sudoku-peli oikein, avautuu hänelle loppunäkymä, josta hän näkee saamansa pisteet sekä TOP 5 -pisteet. Loppunäkymästä voi myös aloittaa uuden pelin: 

![image](https://user-images.githubusercontent.com/117500758/209474686-fa1a7121-48be-41dc-a92f-39bc3a816795.png)



