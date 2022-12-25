# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin testein unittestilla että manuaalisesti järjestelmätasolla ohjelmaa käyttäen. 

## Yksikkötestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaava ```GameLoop```-luokkaa testataan TestSudoku-testiluokalla. Testejä varten on alustettu kaksi Sudoku-ruudukkoa, toinen, joka on ratkaistu täysin oikein, ja toinen, josta puuttuu pari numeroa. Näin on voitu testata tuottavatko ruudukon oikeellisuuteen liittyvät metodit oikean tuloksen.

### Repositorio-luokka

Repositorio-luokka ```ScoreRepository``` testataan TestScoreRepository-testiluokalla. Testiluokassa poistetaan aluksi tiedoston kaikki mahdolliset tiedot, jotta voidaan sitten testata, että luokan metodit lisäävät pisteet tiedostoon oikein. 

### Testauskattavuus 

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haaraumakattavuus on 39%

![image](https://user-images.githubusercontent.com/117500758/209475944-996f7c5f-e718-4162-b6f7-8c9ac1d65961.png)

Testaamatta jäi GameLoop-luokan metodit, jotka sisälsivät pygamea vaativat metodit. Myös metodit, jotka sisälsivät yhden tai useamman toisen metodin (esim. valid_location) jäivät testaamatta.

## Järjestelmätestaus

Sovellus on haettu ja testattu käyttöohjeen kuvaamalla tavalla Linux-ympäristössä.

## Jääneet laatuongelmat

- Ensimmäisen numeron syöttäminen onnistuu joskus vasta toisella klikkauksella. 
