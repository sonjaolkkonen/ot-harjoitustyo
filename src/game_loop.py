import sys
import pygame
import requests


class GameLoop:
    def __init__(self, position, screen, font, number, grid):
        self.position = position
        self.screen = screen
        self.font = font
        self.number = number
        self.grid = grid
        self.grid_original = None
        self.buffer = None
        self.pos = None

    # creating new game using API
    def new_game(self):
        response = requests.get(
            "https://sugoku.herokuapp.com/board?difficulty=easy")
        self.grid = response.json()['board']
        self.grid_original = [[self.grid[x][y] for y in range(
            len(self.grid[0]))] for x in range(len(self.grid))]
        self.draw_numbers()

    # drawing the numbers into the grid

    def draw_numbers(self):
        for i in range(0, len(self.grid[0])):
            for j in range(0, len(self.grid[0])):
                if self.grid[i][j] > 0 and self.grid[i][j] < 10:
                    self.number = self.font.render(
                        str(self.grid[i][j]), True, (0, 0, 0))
                    self.screen.blit(self.number, ((j+1)*50+15, (i+1)*50+10))
        pygame.display.update()

    # inserting numbers into the grid
    def insert(self, screen, position):
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
                    # checking if the the cell already has a number when launching the game
                    if self.grid_original[i-1][j-1] != 0:
                        return
                    # user can change or erase the already inputted number with 0
                    if event.key == 48:
                        self.grid[i-1][j-1] = event.key - 48
                        pygame.draw.rect(self.screen, (255, 250, 240), (
                            self.position[0]*50+self.buffer,self.position[1]*50+
                            self.buffer, 50 - 2*self.buffer, 50 - 2*self.buffer))
                        pygame.display.update()
                        return
                    # checking if the inputted number is valid
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
                        return
                    return

    #going throug the game events
    def handle_events(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.pos = pygame.mouse.get_pos()
                    self.insert(
                        self.screen, (self.pos[0]//50, self.pos[1]//50))
                if event.type == pygame.QUIT:
                    sys.exit()
