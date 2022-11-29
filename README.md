# Sudoku

Sovellus on klassinen sudoku-peli, jota pelataan 9x9 ruudukossa. Sovellusta on mahdollista käyttää useampi käyttäjä, ja he voivat luoda käyttäjätunnuksen sovellukseen pistetilastojen tallentamista varten. Sovellus myös tarjoaa eri vaikeustasoja.

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)


## Asennus
1. Asenna riippuvuudet komennolla:
 
```
poetry install
```  

2. Käynnistä sovellus komennolla: 
```
poetry run invoke start
```  
## Komentorivitoiminnot
### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla: 
```
poetry run invoke start
```
### Testaus
Testit suoritetaan komennolla: 
```
poetry run invoke test
```
### Testikattavuus
Testikattavuus raportin voi generoida komennolla: 
```
poetry run invoke coverage-report
```
### Pylint
Tiedoston [pylintrc](.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:
```
poetry run invoke lint
```
