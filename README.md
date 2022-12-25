# Sudoku

Sovellus on klassinen sudoku-peli, jota pelataan 9x9 ruudukossa. Ruudukko on jaettu vielä 3x3 aliruudukoihin. Pelin alkaessa osa ruudukon numeroista on annettu valmiiksi, ja tavoitteena on täyttää loput ruudut numeroilla 1-9 mahdollisimman nopeasti. Kukin numero saa esiintyä vain kerran sekä vaaka- että pystyrivillä. Lisäksi kukin numero saa esiintyä vain kerran jokaisessa 3x3 aliruudukossa. Sovellus myös tarjoaa eri vaikeustasoja, ja alussa annettujen numeoroiden määrä riippuu valitusta vaikeustasosta.

## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/testaus.md)
- [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)

## Releaset
[Viikko 5](https://github.com/sonjaolkkonen/ot-harjoitustyo/releases/tag/viikko5)

[Viikko 6](https://github.com/sonjaolkkonen/ot-harjoitustyo/releases/tag/viikko6)

[Loppupalautus](https://github.com/sonjaolkkonen/ot-harjoitustyo/releases/tag/loppupalautus)

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
