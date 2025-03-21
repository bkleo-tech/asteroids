import pygame
from circleshape import *
from constants import *


class Shot(CircleShape):
    
    def __init__(self, x , y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (252,252,252), self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt