import pygame
import requests 


class Sudoku:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((550,550))
        pygame.display.set_caption("Sudoku")
        self.font = pygame.font.SysFont('Arial', 30)

        self.draw_screen()
        self.draw_lines()

        self.new_game()

        self.gameloop()



    def gameloop(self):
        while True:
            self.events()

    #going through the game events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    #drawing the screen
    def draw_screen(self):
       self.screen.fill((255,250,240))

    #drawing the grid & 9x9 boxes
    def draw_lines(self):
        
        for i in range(0,10):
            #9x9 boxes
            if (i%3 == 0):
                pygame.draw.line(self.screen, (0,0,0), (50+50*i, 50), (50+50*i, 500), 5)
                pygame.draw.line(self.screen, (0,0,0), (50, 50+50*i), (500, 50+50*i), 5)
        
            #vertical lines
            pygame.draw.line(self.screen, (0,0,0), (50+50*i, 50), (50+50*i, 500), 2)
            #horizontal lines
            pygame.draw.line(self.screen, (0,0,0), (50, 50+50*i), (500, 50+50*i), 2)
        pygame.display.update()
    
    #creating new game using API        
    def new_game(self):
        response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
        self.grid = response.json()['board']
        self.grid_original = [[self.grid[x][y] for y in range(len(self.grid[0]))] for x in range(len(self.grid))]
        self.draw_numbers()
        

    #drawing the numbers into the grid
    def draw_numbers(self):
        for i in range(0, len(self.grid[0])):
            for j in range(0, len(self.grid[0])):
                if self.grid[i][j]>0 and self.grid[i][j]<10:
                    self.number = self.font.render(str(self.grid[i][j]), True, (0,0,0))
                    self.screen.blit(self.number, ((j+1)*50+15, (i+1)*50+10))
        pygame.display.update()





if __name__ == "__main__":
    Sudoku()
    

