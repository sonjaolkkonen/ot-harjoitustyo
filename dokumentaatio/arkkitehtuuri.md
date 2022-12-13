# Arkkitehtuurikuvaus

## Rakenne
Koodin tämänhetkinen pakkausrakenne on seuraava:

![image](https://user-images.githubusercontent.com/117500758/207214017-bf8e42a6-eda9-47d7-8f67-c61c89ff8a83.png)

Pakkaus *ui* sisältää käyttöliittymästä ja *services* sovelluslogiikasta vastaavan koodin. 


## Sovelluslogiikka

Sovelluksen toiminnallisista kokonaisuuksista vastaa GameLoop-luokka. Luokka tarjoaa kaikille käyttöliittymän toiminnoille oman metodin. Näitä ovat esimerkiksi: 

- generate_solution
- remove_numbers
- insert
- handle_events

## Esimerkkikaavio vaikeustason valinnasta
![image](https://user-images.githubusercontent.com/117500758/205943711-a89407cd-2c71-429d-98b5-5f845ce641f8.png)




