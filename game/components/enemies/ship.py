import pygame
import random
import math


from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ALIEN, SCREEN_WIDTH, SCREEN_HEIGHT,FPS, OVNI, SHIP_EAT, BOSS

class ship(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)

        
class AlienEnemy(Enemy):
    WIDTH = 120
    HEIGHT = 160
    ANGLE_SPEED = 0.04
    RADIUS = 150


    def __init__(self):
        self.image = ALIEN
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.angle = 0
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 0

    def move(self, bullet_handler):
        self.angle += self.ANGLE_SPEED
        new_x = self.center_x + int(self.RADIUS * math.cos(self.angle))
        new_y = self.center_y + int(self.RADIUS * math.sin(self.angle))
        self.rect.center = (new_x, new_y)

    def update(self, bullet_handler):
        self.move(bullet_handler)
        super().update(bullet_handler)



class Onvi(Enemy):
    WIDTH = 60
    HEIGHT = 80
    SPEED = 3

    def __init__(self):
        self.image = OVNI
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.rect.y = 0
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.WIDTH)

        self.direction = random.choice([-1, 1])
        self.speed_x = self.SPEED * self.direction

    def move(self, bullet_handler):
        self.rect.x += self.speed_x

        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0

    def update(self, bullet_handler):
        self.move(bullet_handler)
        super().update(bullet_handler)


    

class Ship_eat(Enemy):
    WIDTH = 40
    HEIGHT = 60
    SPEED = 10

    def __init__(self):
        self.image = SHIP_EAT
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.rect.y = -self.HEIGHT
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.WIDTH)

    def move(self, bullet_handler):
        self.rect.y += self.SPEED

    def update(self, bullet_handler):
        self.move(bullet_handler)
        super().update(bullet_handler)
      

     

        