import pygame, time
from settings import *
from sys import exit
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Magnet Maze')
        self.clock = pygame.time.Clock()
        # self.previous_time = time.time()
        
        self.level = Level()

    def run(self):
        while True:
            dt = 1
            # dt = time.time() - self.previous_time
            # self.previous_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill('black')
            self.level.update(dt)

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
