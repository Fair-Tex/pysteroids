import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, 'white', self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += (self.velocity * dt)