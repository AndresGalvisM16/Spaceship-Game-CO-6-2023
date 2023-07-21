import pygame
import random
import math

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ALIEN, SCREEN_WIDTH, SCREEN_HEIGHT,FPS, OVNI, SHIP_EAT, BOSS


class Boss(Enemy):
    WIDTH = 550
    HEIGHT = 450
    SPEED = 10

    def __init__(self):
        self.image = BOSS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.lives = 100
        super().__init__(self.image)
        self.rect.y = -self.HEIGHT
        self.rect.x = (SCREEN_WIDTH - self.WIDTH) // 2  
        

    def move(self, bullet_handler):
        self.rect.y += self.SPEED
 

    def update(self, bullet_handler):
        self.move(bullet_handler)
        super().update(bullet_handler)


        if not self.is_alive:
            self.lives -= 1
            if self.lives > 0:
                self.reset()
            else:
                self.is_visible = False


    def reset(self):
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 0
        self.angle = 0
