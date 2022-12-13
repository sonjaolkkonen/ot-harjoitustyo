# Arkkitehtuurikuvaus

## Rakenne
Ohjelman rakenne tulee noudattamaan kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne tulee olemaan seuraava:

![image](https://user-images.githubusercontent.com/117500758/207262820-0d906bd9-5a4a-45e5-9d0d-8a239035c2f2.png)

Pakkaus *ui* sisältää käyttöliittymästä, *services* sovelluslogiikasta ja *repositories* (tämä puuttuu vielä) tietojen pysyväistallennuksesta vastaavan koodin.

## Käyttöliittymä

Käyttöliittymä sisältää 8 erilaista näkymää:

- Tervetuloa-näkymä
- Aloitusvalikko
- Pelitilastot
- Vaikeustason valinta
- Kirjautuminen
- Uuden käyttäjän luominen
- Pelinäkymä
- Loppunäkymä

Näistä kirjautuminen ja uuden käyttäjän luominen on toteutettu omana luokkanaan, muut on toteutettu omina metodeinaan osana Ui-luokkaa. Näkymien näyttämisestä vastaa Ui-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta, ja se ainoastaan kutsuu pelinäkymässä GameLoop-luokkaa.

## Sovelluslogiikka

Sovelluksen toiminnallisista kokonaisuuksista vastaa GameLoop-luokka. Luokka tarjoaa kaikille käyttöliittymän toiminnoille oman metodin. Näitä ovat esimerkiksi: 

- ```generate_solution```
- remove_numbers
- insert
- handle_events

GameLoop-luokan vastuulla on Sudoku-ruudukon mallintaminen, luominen ja pelitilanteiden luominen. 

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka yhden päätoiminnalisuuden osalta sekvenssikaaviona.

### Vaikeustason valinta

![image](https://user-images.githubusercontent.com/117500758/207268321-0148907f-0b8f-463d-838d-0bc354fee25f.png)




