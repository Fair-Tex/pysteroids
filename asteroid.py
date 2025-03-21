import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vect_velocity1 = self.velocity.rotate(random_angle)
            vect_velocity2 = self.velocity.rotate(random_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)

            asteroid_1.velocity = vect_velocity1 * 1.2
            asteroid_2.velocity = vect_velocity2 * 1.2
            
