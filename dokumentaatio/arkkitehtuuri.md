# Arkkitehtuurikuvaus

## Rakenne
Ohjelman rakenne tulee noudattamaan kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne on seuraava:

![image](https://user-images.githubusercontent.com/117500758/207262820-0d906bd9-5a4a-45e5-9d0d-8a239035c2f2.png)

Pakkaus *ui* sisältää käyttöliittymästä, *services* sovelluslogiikasta ja *repositories* tietojen pysyväistallennuksesta vastaavan koodin.

## Käyttöliittymä

Käyttöliittymä sisältää 4 erilaista näkymää:

- Aloitusvalikko
- Vaikeustason valinta
- Pelinäkymä
- Loppunäkymä

Kaikki näkymät on toteutettu omina metodeinaan osana Ui-luokkaa. Näkymien näyttämisestä vastaa Ui-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta, ja se ainoastaan kutsuu pelinäkymässä GameLoop-luokkaa. 

## Sovelluslogiikka

Sovelluksen toiminnallisista kokonaisuuksista vastaa GameLoop-luokka. Luokka tarjoaa kaikille käyttöliittymän toiminnoille oman metodin. Näitä ovat esimerkiksi: 

- ```generate_solution```
- ```remove_numbers```
- ```insert```
- ```handle_events```

GameLoop-luokan vastuulla on Sudoku-ruudukon mallintaminen, luominen ja pelitilanteiden luominen.

## Tietojen pysyväistallennus

Pakkauksen *repositories* luokka ```ScoreRepository``` huolehtii tietojen tallentamisesta. Luokka tallentaa tietoa CSV-tiedostoon ja se noudattaa Repository-suunnittelumallia. 

Pelaajan saamat pisteet tallennetaan oikeaan järjestykseen tiedostoon score.txt. Samaisesta tiedostosta saadaan myös TOP 5 parhaimmat pisteet loppunäkymän tilastoja varten.

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka yhden päätoiminnalisuuden osalta sekvenssikaaviona.

### Uuden pelin aloitus

![image](https://user-images.githubusercontent.com/117500758/209475501-aaa942c6-05d9-4fa8-8170-1db63c864316.png)







