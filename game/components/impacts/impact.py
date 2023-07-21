import pygame
from game.utils.constants import ROCK, SCREEN_HEIGHT, SCREEN_WIDTH
class Rock:
    WIDTH = 80
    HEIGHT = 80
    SPEED = 4

    def __init__(self, center):
        self.image = ROCK
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.rect.y += self.SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_out_of_screen(self):
        return self.rect.top >= SCREEN_HEIGHT
        

    