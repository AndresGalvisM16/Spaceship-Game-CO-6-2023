import random
import pygame
import math
from game.utils.constants import OBSTACLE, SCREEN_WIDTH

class Impact:
    WIDTH = 110
    HEIGHT = 110
    SPEED = 3

    def __init__(self):
        super().__init__()
        self.image = OBSTACLE
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.y = -self.HEIGHT
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.WIDTH)

    def move(self):
        self.rect.y += self.SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.move()
