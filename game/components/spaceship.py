import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE
from game.components.bullets.bullet_spaceship import BulletSpaceship
class Spaceship(pygame.sprite.Sprite):
    WIDTH = 60
    HEIGHT = 90
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.speed = 10
        self.is_alive = True
        self.spacebar_pressed = False  
        
    def update(self, game_speed, user_input, bullet_handler):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        if self.spacebar_pressed and not keys[pygame.K_SPACE]:
            self.spacebar_pressed = False
        if keys[pygame.K_SPACE] and not self.spacebar_pressed:
            self.shoot(bullet_handler)
            self.spacebar_pressed = True
               
    def draw(self, screen):
        screen.blit(self.image, self.rect)

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






    def shoot(self, bullet_handler):
            bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)
         






        
    

