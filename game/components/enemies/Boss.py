import pygame
import random
import math


from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ALIEN, SCREEN_WIDTH, SCREEN_HEIGHT,FPS, OVNI, SHIP_EAT, BOSS


class Boss(Enemy):
    WIDTH = 550
    HEIGHT = 450
    SPEED = 1

    def __init__(self):
        self.image = BOSS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.rect.y = -self.HEIGHT
        self.rect.x = (SCREEN_WIDTH - self.WIDTH) // 2  

    def move(self):
        self.rect.y += self.SPEED

    def update(self):
        self.move()
        super().update()
