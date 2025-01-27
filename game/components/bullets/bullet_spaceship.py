import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET

class BulletSpaceship(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 5

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, center)
        self.can_shoot = True

    def update(self, player):
        self.rect.y -= self.SPEED
        super().update(player)




