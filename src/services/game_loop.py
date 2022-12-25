from random import shuffle
import copy
import os
import sys
import pygame
import time
from repositories.score_repository import ScoreRepository

dirname = os.path.dirname(__file__)


class GameLoop():
    """Sovelluksen logiikasta vastaava luokka.
    """

    def __init__(self, position, screen, font, number, grid, level):
        """Konstruktori, joka alustaa peliloopin.

        Args:
            position: Numeroiden piirtämiseen käytettävä fontti.
            screen: Näyttö, johon peli piirretään.
            font: Numeoriden piirtämiseen käytettävä fontti.
            number: Pelissä käytettävä numero.
            grid: 9x9 ruudukko, joka sisältää sudokussa käytettävän peliruudukon ja sen numerot.
            level: Pelaajan valitsema pelin vaikeustaso.
        """

        self.position = position
        self.screen = screen
        self.font = font
        self.number = number
        self.grid = grid
        self.level = level
        self.buffer = None
        self.start = None
        self.end = None
        self.scores = None
        self.top_five = None
        self.image = pygame.image.load(os.path.join(
            dirname, "../", "assets", "button.png"))

        self.grid = [[0 for i in range(9)] for j in range(9)]

        self.draw_screen()
        self.draw_lines()
        self.generate_solution(self.grid)
        print(self.grid)
        self.solution = copy.deepcopy(self.grid)
        self.remove_numbers()
        self.draw_numbers()
        self.grid_original = copy.deepcopy(self.grid)
        self.handle_events()

    def draw_screen(self):
        """Täyttää näytön valkoisella taustavärillä.
        """
        self.screen.fill((250, 250, 250))

    def draw_lines(self):
        """Piirtää ruudukon ulkoviivat, 3x3 ruudukoiden viivat sekä yksittäisten ruutujen viivat.
        """

        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (50+50*i, 50), (50+50*i, 500), 5)
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (50, 50+50*i), (500, 50+50*i), 5)

            pygame.draw.line(self.screen, (0, 0, 0),
                             (50+50*i, 50), (50+50*i, 500), 2)

            pygame.draw.line(self.screen, (0, 0, 0),
                             (50, 50+50*i), (500, 50+50*i), 2)
        pygame.display.update()

    def test_solution(self, grid):
        """Testaa onko saatu ratkaisu oikein eli jokaisella pysty-
        ja vaakarivillä on vain yksi numero väliltä 1-9.

        Args:
            grid: Testattava 9x9 ruudukko, jonka jokainen ruutu sisältää numeron.

        Returns:
            True, mikäli ruudukko on Sudokun sääntöjen mukainen, muussa tapauksessa False.
        """
        for row in range(9):
            for col in range(9):
                number = grid[row][col]
                grid[row][col] = 0
                if not self.valid_location(grid, row, col, number):
                    return False
                grid[row][col] = number
        return True

    @classmethod
    def number_already_in_row(cls, grid, row, number):
        """Kertoo onko kyseisellä vaakarivillä jo kyseinen numero.

        Args:
            grid: Peliruudukko.
            row: Vaakarivi, josta tarkistetaan onko kyseistä numeroa jo olemassa.
            number: Ruudukkoon lisättävä numero.

        Returns:
            True, mikäli kyseinen numero jo löytyy kyseiseltä vaakariviltä.
            Muussa tapauksessa False.
        """
        if number in grid[row]:
            return True
        return False

    @classmethod
    def number_already_in_col(cls, grid, col, number):
        """Kertoo onko kyseisellä pystyrivillä jo kyseinen numero.

        Args:
            grid: Peliruudukko.
            col: Pystyrivi, josta tarkistetaan onko kyseistä numeroa jo olemassa.
            number: Ruudukkoon lisättävä numero.

        Returns:
            True, mikäli kyseinen numero jo löytyy kyseiseltä pystyriviltä.
            Muussa tapauksessa False.
        """
        for i in range(9):
            if grid[i][col] == number:
                return True
        return False

    @classmethod
    def number_already_in_subgrid(cls, grid, row, col, number):
        """Kertoo onko kyseisessä 3x3 ruudukossa jo kyseinen numero.

        Args:
            grid: Peliruudukko.
            row: Vaakarivi, jota käytetään määrittelemään tarkistettavan 3x3 ruudukon vaakarivi.
            col: Pystyrivi, jota käytetään määrittelemään tarkistettavan 3x3 ruudukon pystyrivi.
            number: Ruudukkoon lisättävä numero.

        Returns:
            True, mikäli kyseinen numero jo löytyy kyseisestä 3x3 ruudukosta.
            Muussa tapauksessa False.
        """
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        for i in range(sub_row, (sub_row + 3)):
            for j in range(sub_col, (sub_col + 3)):
                if grid[i][j] == number:
                    return True
        return False

    def valid_location(self, grid, row, col, number):
        """Testaa ylläolevien metodien avulla onko paikka,
            johon numeroa ollaan lisäämässä validi paikka sille.
            Eli vaaka- ja pystyriveillä ei ole toista samaa numeroa 1-9 välillä eikä 3x3 ruudukossa.

        Args:
            grid: Peliruudukko.
            row: Vaakarivi, johon numero ollaan lisäämässä.
            col: Pystyrivi, johon numero ollaan lisäämässä.
            number: Lisäämässä oleva numero.

        Returns:
            True, mikäli lisättävää numeroa ei jo löydy vaaka- ja pystyriveiltä
            tai 3x3 ruudukosta. Muussa tapauksessa False.
        """
        if self.number_already_in_row(grid, row, number):
            return False
        if self.number_already_in_col(grid, col, number):
            return False
        if self.number_already_in_subgrid(grid, row, col, number):
            return False
        return True

    @classmethod
    def find_empty_cell(cls, grid):
        """Etsii peliruudukosta seuraavan tyhjän ruudun, johon voidaan lisätä numero.

        Args:
            grid: Peliruudukko.

        Returns:
            Seuraavan tyhjän ruudun sijainnin. Mikäli tyhjiä ruutuja ei enää ole, palautetaan None.
        """
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def generate_solution(self, grid):
        """Luo oikein ratkaistun Sudoku-ruudukon eli ruudukon, jossa jokaisella
            vaaka- ja pystyrivillä on vain yksi numero väliltä 1-9
            sekä myös jokaisessa 3x3 ruudukossa on vain yksi numero väliltä 1-9.
            Ruudukon luomisessa käytetään apuna ylläolevia metodeja.

        Args:
            grid: Peliruudukko.

        Returns:
            Palauttaa False.
        """
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 81):
            row = i//9
            col = i % 9

            if grid[row][col] == 0:
                shuffle(numbers)
                for number in numbers:
                    if self.valid_location(grid, row, col, number):
                        grid[row][col] = number
                        if not self.find_empty_cell(grid):
                            return True
                        if self.generate_solution(grid):
                            return True
                break
        grid[row][col] = 0
        return False

    @classmethod
    def get_filled_cells(cls, grid):
        """Listaa ne ruudut, joissa on jo numero.

        Args:
            grid: Peliruudukko.

        Returns:
            Palauttaa listan täytetyistä ruuduista.
        """
        filled_cells = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    filled_cells.append((i, j))
        shuffle(filled_cells)
        return filled_cells

    def remove_numbers(self):
        """Poistaa numeroita ratkaistusta Sudoku-ruudukosta,
        jotta saadaan luotua aloitusruudukko pelille.
        Poistettujen numeroiden määrä määritellään vaikeustason mukaan,
        mitä vaikeampi taso, sitä useampi numero poistetaan.
        """
        filled_cells = self.get_filled_cells(self.grid)
        filled_cells_amount = len(filled_cells)
        if self.level == "easy":
            while filled_cells_amount >= 70:
                row, col = filled_cells.pop()
                filled_cells_amount -= 1
                self.grid[row][col] = 0
            return
        if self.level == "medium":
            while filled_cells_amount >= 60:
                row, col = filled_cells.pop()
                filled_cells_amount -= 1
                self.grid[row][col] = 0
            return
        if self.level == "hard":
            while filled_cells_amount >= 50:
                row, col = filled_cells.pop()
                filled_cells_amount -= 1
                self.grid[row][col] = 0
            return

    def draw_numbers(self):
        """Piirtää numerot peliruudukkoon.
        """
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    self.number = self.font.render(
                        str(self.grid[i][j]), 1, (0, 0, 0))
                    self.screen.blit(self.number, ((j+1)*50+15, (i+1)*50+10))
        self.start_time = time.time()
        pygame.display.update()

    def insert(self, screen, position):
        """Lisää numeroita ruudukkoon pelaajan syötteen perusteella.
            Mahdollistaa numeroiden lisäämisen tyhjään ruutuun,
            sekä myös numeron vaihtamisen ja poistamisen.
            Pelin alussa annettuja numeroita ei pysty muuttamaan.

        Args:
            screen: Näyttö, johon numerot piirretään.
            position: Ruudun, johon numero lisätään, sijainti.
        """
        from ui.ui import Ui
        self.screen = screen
        self.position = position
        self.buffer = 5
        i, j = self.position[1], self.position[0]
        self.font = pygame.font.SysFont('Arial', 30)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if self.grid_original[i-1][j-1] != 0:
                        return
                    if event.key == 48:
                        self.grid[i-1][j-1] = event.key - 48
                        pygame.draw.rect(self.screen, (255, 250, 240), (
                            self.position[0]*50+self.buffer, self.position[1]*50 +
                            self.buffer, 50 - 2*self.buffer, 50 - 2*self.buffer))
                        pygame.display.update()
                        return
                    if 0 < event.key - 48 < 10:
                        pygame.draw.rect(self.screen, (255, 250, 240), (
                            self.position[0]*50 + self.buffer, self.position[1]*50 +
                            self.buffer, 50 - 2*self.buffer, 50 - 2*self.buffer))
                        self.number = self.font.render(
                            str(event.key-48), True, (24, 116, 205))
                        self.screen.blit(
                            self.number, (self.position[0]*50+15, self.position[1]*50+10))
                        self.grid[i-1][j-1] = event.key
                        pygame.display.update()
                        if not self.find_empty_cell(self.grid):
                            if self.test_solution(self.grid):
                                self.end_time = time.time()
                                time_lapsed = self.end_time - self.start_time
                                self.count_scores(time_lapsed)
                                self.top_scores()
                                Ui.end_screen(self, self.scores, self.top_five)
                        return
                    return

    def count_scores(self, sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        self.scores = hours*1000+100*mins+sec
        self.scores = (round(self.scores))

    def top_scores(self):
        top_scores = ScoreRepository.add_new_score(self, self.scores)
        self.top_five = ', '.join(top_scores)


    def handle_events(self):
        """Käsittelee pelitapahtumat.
        """

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.pos = pygame.mouse.get_pos()
                    self.insert(
                        self.screen, (self.pos[0]//50, self.pos[1]//50))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
