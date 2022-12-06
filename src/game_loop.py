from random import shuffle
import copy
import sys
import pygame


class GameLoop():
    def __init__(self, position, screen, font, number, grid, level):

        self.position = position
        self.screen = screen
        self.font = font
        self.number = number
        self.grid = grid
        self.level = level
        self.buffer = None

        self.grid = [[0 for i in range(9)] for j in range(9)]

        self.draw_screen()
        self.draw_lines()
        self.generate_solution(self.grid)
        self.solution = copy.deepcopy(self.grid)
        self.remove_numbers()
        self.draw_numbers()
        self.grid_original = copy.deepcopy(self.grid)
        self.handle_events()

    # drawing the screen

    def draw_screen(self):
        self.screen.fill((255, 250, 240))

    # drawing the grid & 9x9 boxes
    def draw_lines(self):

        for i in range(0, 10):
            # 9x9 boxes
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (50+50*i, 50), (50+50*i, 500), 5)
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (50, 50+50*i), (500, 50+50*i), 5)

            # vertical lines
            pygame.draw.line(self.screen, (0, 0, 0),
                             (50+50*i, 50), (50+50*i, 500), 2)
            # horizontal lines
            pygame.draw.line(self.screen, (0, 0, 0),
                             (50, 50+50*i), (500, 50+50*i), 2)
        pygame.display.update()

    def test_solution(self, grid):
        for row in range(9):
            for col in range(9):
                number = grid[row][col]
                grid[row][col] = 0
                if not self.valid_location(grid, row, col, number):
                    return False
                grid[row][col] = number
        return True

    def number_already_in_row(self, grid, row, number):
        if number in grid[row]:
            return True
        return False

    def number_already_in_col(self, grid, col, number):
        for i in range(9):
            if grid[i][col] == number:
                return True
        return False

    def number_already_in_subgrid(self, grid, row, col, number):
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        for i in range(sub_row, (sub_row + 3)):
            for j in range(sub_col, (sub_col + 3)):
                if grid[i][j] == number:
                    return True
        return False

    def valid_location(self, grid, row, col, number):
        if self.number_already_in_row(grid, row, number):
            return False
        if self.number_already_in_col(grid, col, number):
            return False
        if self.number_already_in_subgrid(grid, row, col, number):
            return False
        return True

    def find_empty_cell(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def generate_solution(self, grid):
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

    def get_filled_cells(self, grid):
        filled_cells = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    filled_cells.append((i, j))
        shuffle(filled_cells)
        return filled_cells

    def remove_numbers(self):
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
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    self.number = self.font.render(
                        str(self.grid[i][j]), 1, (0, 0, 0))
                    self.screen.blit(self.number, ((j+1)*50+15, (i+1)*50+10))
        pygame.display.update()

    def insert(self, screen, position):
        from ui.menu import Ui
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
                            self.position[0]*50+self.buffer, self.position[1]*50 +
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
                        if not self.find_empty_cell(self.grid):
                            if self.test_solution(self.grid):
                                Ui.end_screen(self)
                        return
                    return

    def handle_events(self):

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
