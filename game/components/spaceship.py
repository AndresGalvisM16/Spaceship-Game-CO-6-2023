import pygame
import time
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE, SPACESHIP_SHIELD
from game.components.impacts.impact import Rock
from game.components.power_ups.shield import Shield
class Spaceship:
    WIDTH = 60
    HEIGHT = 90
    X_POS = (SCREEN_WIDTH // 2) - WIDTH
    Y_POS = 500
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.speed = 10
        self.is_alive = True
        self.spacebar_pressed = False
        self.lives = 20
        self.invulnerable = False
        self.invulnerability_time = 2000
        self.has_shield = False
        self.time_up = 0

    
    def update(self, game_speed, user_input, bullet_handler):
        keys = pygame.key.get_pressed()
        if user_input[pygame.K_LEFT]:
            self.move_left(game_speed)
        if user_input[pygame.K_RIGHT]:
            self.move_right(game_speed)
        if user_input[pygame.K_UP]:
            self.move_up(game_speed)
        if user_input[pygame.K_DOWN]: 
            self.move_down(game_speed)
        
        if self.spacebar_pressed and not keys[pygame.K_SPACE]:
            self.spacebar_pressed = False
        if keys[pygame.K_SPACE] and not self.spacebar_pressed:
            self.shoot(bullet_handler)
            self.spacebar_pressed = True
        if self.has_shield:
            time_to_show = round((self.time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0:
                self.deactivate_power_up()



    def move_left(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

    def move_right(self, game_speed):
        self.rect.x += game_speed
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0


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




    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self, bullet_handler):
        bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)
         

    def handle_collision(self, rocks):
        if self.is_alive and not self.invulnerable:
            for rock in rocks:
                if self.rect.colliderect(rock.rect):
                    self.lives -= 1
                    self.is_alive = False
                    self.invulnerable = True
                    self.invulnerability_start_time = pygame.time.get_ticks()  # Marcar el tiempo de inicio de invulnerabilidad
                    break

    def handle_invulnerability(self):
        elapsed_invulnerable_time = pygame.time.get_ticks() - self.invulnerability_start_time
        if elapsed_invulnerable_time >= self.invulnerability_time:
            self.invulnerable = False

    def reset_invulnerability(self):
        self.invulnerable = False




    def activate_power_up(self, power_up):
        self.time_up = power_up.time_up
        if isinstance(power_up, Shield):
            self.image = SPACESHIP_SHIELD
            self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
            self.has_shield = True



    def deactivate_power_up(self):
        self.has_shield = False
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
        



    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.speed = 10
        self.is_alive = True
        self.spacebar_pressed = False
        self.invulnerable = False
        self.has_shield = False
    





    
      



        
    

