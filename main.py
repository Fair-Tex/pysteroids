import pygame
from constants import *

def main():
    game = pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        surface.fill('black')
        pygame.display.flip()



if __name__ == "__main__":
    main()