import random
import pygame

from game.utils.constants import BG_1, BG_2, BG_3, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, BACKGROUND_IMAGES
from game.components.spaceship import spaceship
from game.components.enemies.enemy_handler import EnemyHandler

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = spaceship()
        self.enemy_handler = EnemyHandler()
        self.elapsed_time = 0
        self.current_bg_index = 0
        self.current_bg = BACKGROUND_IMAGES[self.current_bg_index]
        self.next_bg_index = (self.current_bg_index + 1) % len(BACKGROUND_IMAGES)
        self.next_bg = BACKGROUND_IMAGES[self.next_bg_index]
        self.transition_alpha = 0
        self.transition_speed = 2


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_inpunt = pygame.key.get_pressed()
        self.player.update(self.game_speed, user_inpunt)
        self.player.check_bounds(SCREEN_WIDTH)
        self.enemy_handler.update()
        self.elapsed_time += self.clock.tick(FPS) / 1000
        self.y_pos_bg += self.game_speed
        self.change_background()
        

        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_handler.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image1 = pygame.transform.scale(self.current_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image2 = pygame.transform.scale(self.next_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(image1, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image2, (self.x_pos_bg, self.y_pos_bg - SCREEN_HEIGHT))

       


    def change_background(self):
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.y_pos_bg = 0
            self.current_bg_index = self.next_bg_index
            self.current_bg = BACKGROUND_IMAGES[self.current_bg_index]
            self.next_bg_index = (self.current_bg_index + 1) % len(BACKGROUND_IMAGES)
            self.next_bg = BACKGROUND_IMAGES[self.next_bg_index]
         

        

       
       
        

        
    
    
            
