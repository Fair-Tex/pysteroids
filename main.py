import pygame
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *

def main():
    game = pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    
    player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    asteroidfield = AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return

        surface.fill('black')

        updatable.update(dt)

        for a in asteroids:
            if player.collides(a):
                print("GAME OVER!")
                return
        
        for i in drawable:
            i.draw(surface)


        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()