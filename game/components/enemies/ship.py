import pygame
import random
import math


from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ALIEN, SCREEN_WIDTH, SCREEN_HEIGHT,FPS

class ship(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)

        
class AlienEnemy(Enemy):
    WIDTH = 40
    HEIGHT = 60
    ANGLE_SPEED = 0.06
    RADIUS = 150

    def __init__(self):
        self.image = ALIEN
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.angle = 0
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 0

    def move(self):
        self.angle += self.ANGLE_SPEED
        new_x = self.center_x + int(self.RADIUS * math.cos(self.angle))
        new_y = self.center_y + int(self.RADIUS * math.sin(self.angle))
        self.rect.center = (new_x, new_y)

    def update(self):
        self.move()
        super().update()





    


        

        


     
    


        


    

        

      

     

        