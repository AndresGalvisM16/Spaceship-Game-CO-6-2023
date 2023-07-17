import pygame
import random
import time
from game.utils.constants import ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, BACKGROUND_IMAGES, BACKGROUND_IMAGE_PURPLE,BOSS
from game.components.spaceship import spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.enemies.ship import AlienEnemy
from game.components.impacts.impact import Impact
from game.components.enemies.Boss import Boss



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = spaceship()
        self.ship = AlienEnemy()
        self.enemy_handler = EnemyHandler()
        self.impact = Impact()
        self.elapsed_time = 0
        self.current_bg_index = 0
        self.current_bg = BACKGROUND_IMAGES[self.current_bg_index]
        self.next_bg_index = (self.current_bg_index + 1) % len(BACKGROUND_IMAGES)
        self.next_bg = BACKGROUND_IMAGES[self.next_bg_index]
        
       

    def run(self):
        self.playing = True
        self.start_time = time.time()  # Almacenar el tiempo de inicio del juego
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
        user_input = pygame.key.get_pressed()
        self.player.update(self.game_speed, user_input)
        self.player.check_bounds(SCREEN_WIDTH)
        self.enemy_handler.update()
        self.elapsed_time = time.time() - self.start_time  # Calcular el tiempo transcurrido
        self.y_pos_bg += self.game_speed
        self.change_background()
        self.ship.update()
        self.impact.update()
        
     
       

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.impact.draw(self.screen)
        self.player.draw(self.screen)
        self.enemy_handler.draw(self.screen)
        pygame.display.update()

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

    def reset_elapsed_time(self):
        self.elapsed_time = 0





        
    
    
            
