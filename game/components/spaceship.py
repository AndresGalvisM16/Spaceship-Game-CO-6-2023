import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class spaceship:
    WIDTH = 60
    HEIGHT = 90
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x =  self.X_POS 
        self.rect.y = self.Y_POS 
        self.speed = 40
        self.is_alive = True
        
        

    def update(self, game_speed, user_input):
        if user_input[pygame.K_LEFT]:
            self.rect.x -= game_speed 
        if user_input[pygame.K_RIGHT]:
            self.rect.x += game_speed
        if user_input[pygame.K_UP]:
            self.move_up(game_speed)
        if user_input[pygame.K_DOWN]: 
            self.move_down(game_speed)
               
       
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def move_left(self, game_speed):
        if self.rect.left >0:
            self.rect.x -= game_speed  

    def move_right(self, game_speed):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += game_speed 


    def move_up(self, game_speed):
        if self.rect.top > 0:
            self.rect.y -= game_speed


    def move_down(self, game_speed):
        if self.rect.bottom < SCREEN_HEIGHT: 
            self.rect.y += game_speed 


    def check_bounds(self, screen_width):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
    




           


    
 


