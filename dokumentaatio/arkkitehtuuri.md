# Arkkitehtuurikuvaus

## Rakenne
Ohjelman rakenne tulee noudattamaan kolmitasoista kerrosarkkitehtuuria, ja koodin pakkausrakenne tulee olemaan seuraava:

![image](https://user-images.githubusercontent.com/117500758/207262820-0d906bd9-5a4a-45e5-9d0d-8a239035c2f2.png)

Pakkaus *ui* sisältää käyttöliittymästä, *services* sovelluslogiikasta ja *repositories* (tämä puuttuu vielä) tietojen pysyväistallennuksesta vastaavan koodin.

## Käyttöliittymä



## Sovelluslogiikka

Sovelluksen toiminnallisista kokonaisuuksista vastaa GameLoop-luokka. Luokka tarjoaa kaikille käyttöliittymän toiminnoille oman metodin. Näitä ovat esimerkiksi: 

- generate_solution
- remove_numbers
- insert
- handle_events

## Esimerkkikaavio vaikeustason valinnasta
![image](https://user-images.githubusercontent.com/117500758/205943711-a89407cd-2c71-429d-98b5-5f845ce641f8.png)




