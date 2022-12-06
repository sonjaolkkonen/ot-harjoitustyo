## Viikko 3

- Lisätty Sudoku-luokka, joka luo uuden pelin ja täyttää siihen ennalta annetut numerot.
- Lisätty UI hakemisto, joka sisältää luokat UI, HelloView ja Menu.
- Lisätty toiminnallisuus, joka mahdollistaa käyttäjän siirtymisen Menu- ja HelloView-näkymien välillä painamalla näkymien painikkeita.

## Viikko 4
- Eriytetty GameLoop-luokka Sudoku-luokasta.
- Lisätty toiminnallisuus, joka mahdollistaa numeroiden syöttämisen peliruudukkoon.
- Poistettu entinen Ui-luokka, joka oli tehty Tkinterillä ja tilalle luotu Pygamella tehdyt menu- ja button-luokat.
- Lisätty toiminnallisuus, joka mahdollistaa uuden pelin aloittamisen aloitusvalikosta.

## Viikko 5
- Projektissa ollut API lopetti toimintansa, joten koodattu tilalle sudoku-generaattori käyttäen backtracking-algoritmia.
- Lisätty pelitilastot-nappi aloitusvalikkoon, josta pääsee tilasto-näkymään. Näkymästä voi palata takaisin alkuun. 
- Lisätty toiminnallisuus, joka mahdollistaa vaikeustason valinnan. Sudoku generoituu käyttäjän valitseman vaikeustason mukaan eli mitä vaikeampi taso, sitä enemmän numeroita puuttuu pelin alussa. 
- Lisätty toiminnallisuus, joka tarkistaa onko pelaajan tekemä sudoku oikein, kun tämä on täyttänyt kaikki ruudut. Mikäli sudoku ei ole oikein, ei tapahdu mitään. Mikäli sudoku on oikein, siirtyy pelaaja loppunäkymään.
- Lisätty loppunäkymä, jossa ilmoitetaan pelin menneen läpi. Näkymässä pelaaja voi aloittaa uuden pelin tai palata aloitusvalikkoon. 
