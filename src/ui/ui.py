import sys
import pygame
import os

from ui.button import Button
from services.game_loop import GameLoop
from repositories.score_repository import ScoreRepository

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

        self.image = pygame.image.load(os.path.join(
            dirname, "../", "assets", "button.png"))
        

        self.menu()

    def play_screen(self, level):
        """Luo pelinäkymän, josta käynnistyy uusi pelaajan valitsemalla vaikeustasolla. 

        Args:
            level: Pelaajan valitsema vaikeustaso
        """
        self.screen = pygame.display.set_mode((550, 550))
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
        new_game_button = Button(button_image, 275, 275, "Aloita uusi peli")


        while True:
            self.screen.fill((250, 250, 250))

            menu_screen_text = self.font.render(
                "Tervetuloa pelaamaan Sudokua!", True, (0, 0, 0))
            menu_screen_text_rect = menu_screen_text.get_rect(center=(275, 150))

            self.screen.blit(menu_screen_text, menu_screen_text_rect)

            new_game_button.change_color(pygame.mouse.get_pos())
            new_game_button.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_button.is_pressed(
                            pygame.mouse.get_pos()):
                        Ui.choose_level(self)

            pygame.display.update()

    def end_screen(self, score):
        """Luo loppunäkymän, joka ilmestyy pelaajan ratkaistua sudoku oikein. Näkymästä pelaaja voi aloittaa uuden pelin tai palata aloitusvalikkoon
        """
        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_caption("Sudoku läpi!")
        self.big_font = pygame.font.SysFont('Arial', 30)
        self.small_font = pygame.font.SysFont('Arial', 22)

        self.score = score
        top_scores = ScoreRepository.add_new_score(self, score)
        top_five = ', '.join(top_scores)

        while True:
            self.screen.fill((250, 250, 250))
            end_screen_text = self.big_font.render(
                "Peli läpi, onneksi olkoon!", True, (0, 0, 0))
            end_screen_text_rect = end_screen_text.get_rect(center=(275, 150))

            player_score_text = self.big_font.render(f"Pisteesi: {self.score}", True, (0,0,0))
            player_score_text_rect = player_score_text.get_rect(center=(275, 200))

            top_five_scores_text = self.small_font.render("TOP 5 pistetulokset:", True, (0,0,0))
            top_five_scores_text_rect = top_five_scores_text.get_rect(center=(275, 275))

            top_scores_text = self.small_font.render(f"{top_five}", True, (0,0,0))
            top_scores_text_rect = top_scores_text.get_rect(center=(275, 310))

            self.screen.blit(end_screen_text, end_screen_text_rect)
            self.screen.blit(player_score_text, player_score_text_rect)
            self.screen.blit(top_five_scores_text, top_five_scores_text_rect)
            self.screen.blit(top_scores_text, top_scores_text_rect)

            button_image = self.image
            button_image = pygame.transform.scale(button_image, (250, 100))
            new_game_button = Button(
                button_image, 275, 400, "Aloita uusi peli")

            new_game_button.change_color(pygame.mouse.get_pos())
            new_game_button.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_button.is_pressed(
                            pygame.mouse.get_pos()):
                        Ui.choose_level(self)

            pygame.display.update()

