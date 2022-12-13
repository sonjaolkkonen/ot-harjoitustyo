import sys
import pygame
import os

from ui.button import Button
from services.game_loop import GameLoop
from ui.register_view import RegisterView
from ui.login_view import LoginView

dirname = os.path.dirname(__file__)


class Ui:
    """Sovelluksen käyttöliittymästä vastaava luokka.
    """
    def __init__(self):
        """Luokan konstruktori, joka luo uuden käyttöliittymästä vastaavan luokan. 
        """
        pygame.init()

        self.screen = pygame.display.set_mode((550, 550))
        self.font = pygame.font.SysFont('Arial', 30)

        self.position = None
        self.number = None
        self.grid = None

        self.image = pygame.image.load(os.path.join(dirname, "../", "assets", "button.png"))

        self.main_screen()

    def main_screen(self):
        """Luo ensimmäisen näkymän, jossa käyttäjä voi valita rekisteröityykö, kirjautuuko vai jatkaako kirjautumatta
        """

        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Tervetuloa!")
        self.font = pygame.font.SysFont('Arial', 30)

        while True:
            self.screen.fill((250, 250, 250))

            button_image = self.image
            button_image = pygame.transform.scale(button_image, (350, 100))
            login_button = Button(button_image, 275, 150, "Kirjaudu sisään")
            register_button = Button(button_image, 275, 250, "Rekisteröidy")
            menu_button = Button(button_image, 275, 350, "Jatka kirjautumatta")

            for button in [login_button, register_button, menu_button]:
                button.change_color(pygame.mouse.get_pos())
                button.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if register_button.is_pressed(pygame.mouse.get_pos()):
                        RegisterView()
                    if login_button.is_pressed(
                        pygame.mouse.get_pos()):
                        LoginView()
                    if menu_button.is_pressed(pygame.mouse.get_pos()):
                        Ui.menu(self)


            pygame.display.update()

    def play_screen(self, level):
        """Luo pelinäkymän, josta käynnistyy uusi pelaajan valitsemalla vaikeustasolla. 

        Args:
            level: Pelaajan valitsema vaikeustaso
        """
        self.screen = pygame.display.set_mode((550,550))
        pygame.display.set_caption("Sudoku")
        self.font = pygame.font.SysFont('Arial', 30)

        position = self.position
        screen = self.screen
        font = self.font
        number = self.number
        grid = self.grid

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if level == "easy":
                GameLoop(position, screen, font, number, grid, level="easy")
            if level == "medium":
                GameLoop(position, screen, font, number, grid, level="medium")
            if level == "hard":
                GameLoop(position, screen, font, number, grid, level="hard")
            
            pygame.display.update()



    def choose_level(self):
        """Luo näkymän, jossa pelajaa valitsee uuden pelin vaikeustason.
        """

        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Vaikeustaso")
        self.font = pygame.font.SysFont('Arial', 30)

        while True:
            self.screen.fill((250, 250, 250))
            statistics_screen_text = self.font.render(
                "Valitse vaikeustaso", True, (0, 0, 0))
            statistics_screen_text_rect = statistics_screen_text.get_rect(
                center=(275, 100))
            self.screen.blit(statistics_screen_text,
                             statistics_screen_text_rect)

            button_image = self.image
            button_image = pygame.transform.scale(button_image, (250, 100))
            easy_button = Button(button_image, 275, 200, "Helppo")
            medium_button = Button(button_image, 275, 300, "Keskivaikea")
            hard_button = Button(button_image, 275, 400, "Vaikea")

            for button in [easy_button, medium_button, hard_button]:
                button.change_color(pygame.mouse.get_pos())
                button.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.is_pressed(pygame.mouse.get_pos()):
                        Ui.play_screen(self, level="easy")
                    if medium_button.is_pressed(
                        pygame.mouse.get_pos()):
                        Ui.play_screen(self, level="medium")
                    if hard_button.is_pressed(pygame.mouse.get_pos()):
                        Ui.play_screen(self, level="hard")


            pygame.display.update()

    def menu(self):
        """Luo aloitusvalikon, josta pelaaja voi aloittaa uuden pelin tai katsoa pelitilastoja.
        """
        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Aloitusvalikko")
        self.font = pygame.font.SysFont('Arial', 30)

        button_image = self.image
        button_image = pygame.transform.scale(button_image, (250, 100))
        new_game_button = Button(button_image, 275, 200, "Aloita uusi peli")
        statistics_button = Button(button_image, 275, 300, "Pelitilastot")
        
        while True:
            self.screen.fill((250, 250, 250))

            for button in [new_game_button, statistics_button]:
                button.change_color(pygame.mouse.get_pos())
                button.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_button.is_pressed(
                        pygame.mouse.get_pos()):
                        Ui.choose_level(self)
                    if statistics_button.is_pressed(
                        pygame.mouse.get_pos()):
                        Ui.statistics_screen(self)

            pygame.display.update()

    def end_screen(self):
        """Luo loppunäkymän, joka ilmestyy pelaajan ratkaistua sudoku oikein. Näkymästä pelaaja voi aloittaa uuden pelin tai palata aloitusvalikkoon
        """
        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Pelitilastot")
        self.font = pygame.font.SysFont('Arial', 30)

        while True:
            self.screen.fill((250, 250, 250))
            end_screen_text = self.font.render(
                "Peli läpi, onneksi olkoon!", True, (0, 0, 0))
            end_screen_text_rect = end_screen_text.get_rect(center=(275, 100))
            self.screen.blit(end_screen_text, end_screen_text_rect)

            button_image = self.image
            button_image = pygame.transform.scale(button_image, (250, 100))
            new_game_button = Button(
                button_image, 275, 200, "Aloita uusi peli")
            menu_button = Button(button_image, 275, 300, "Palaa alkuun")

            for button in [new_game_button, menu_button]:
                button.change_color(pygame.mouse.get_pos())
                button.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_button.is_pressed(
                        pygame.mouse.get_pos()):
                        Ui.choose_level(self)
                    if menu_button.is_pressed(pygame.mouse.get_pos()):
                        Ui.menu(self)

            pygame.display.update()

    def statistics_screen(self):
        """Luo pelitilastot-näkymän, josta pelaaja voi katsoa pelitilastoja.
        """
        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Pelitilastot")
        self.font = pygame.font.SysFont('Arial', 30)

        while True:

            self.screen.fill((250, 250, 250))
            statistics_screen_text = self.font.render(
                "Tähän tulee pelitilastot-näkymä", True, (0, 0, 0))
            statistics_screen_text_rect = statistics_screen_text.get_rect(
                center=(275, 100))
            self.screen.blit(statistics_screen_text,
                             statistics_screen_text_rect)

            button_image = self.image
            button_image = pygame.transform.scale(button_image, (250, 100))
            menu_button = Button(button_image, 275, 200, "Palaa alkuun")

            menu_button.change_color(pygame.mouse.get_pos())
            menu_button.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_button.is_pressed(pygame.mouse.get_pos()):
                        Ui.menu(self)

            pygame.display.update()
