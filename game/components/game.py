import pygame
import random
import time
from game.utils.constants import ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, BACKGROUND_IMAGES, BACKGROUND_IMAGE_PURPLE,BOSS, WHITE, BULLET_ENEMY_TYPE, FUND, FUND2
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.enemies.ship import AlienEnemy
from game.components.enemies.Boss import Boss
from game.components.bullets.bullet_handler import BulletHandler
from game.utils import text_utils
from game.components.spaceship import Spaceship
from game.components.impacts.impact_handler import RockHandler
from game.components.impacts.impact import Rock
from game.components.power_ups.power_up_handler import PowerUpHandler



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.ship = AlienEnemy()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.rock_handler = RockHandler()
        self.power_up_handler = PowerUpHandler()
        self.elapsed_time = 0
        self.current_bg_index = 0
        self.current_bg = BACKGROUND_IMAGES[self.current_bg_index]
        self.next_bg_index = (self.current_bg_index + 1) % len(BACKGROUND_IMAGES)
        self.next_bg = BACKGROUND_IMAGES[self.next_bg_index]
        self.score = 0
        self.number_deaths = 0
        self.total_score = 0
        self.max_score = 0
        self.record_score = 0
        self.start_time = 0 
        self.invulnerability_time = 2 
        self.invulnerable = False
        self.invulnerable_start_time = 0 
        self.collided_rocks = set()

    def run(self):
        self.running = True
        self.start_time = time.time() 
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.restart_game()
                self.playing = True
                self.start_time = time.time()
        


    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()

            if self.invulnerable:
                elapsed_invulnerable_time = time.time() - self.invulnerable_start_time
                if elapsed_invulnerable_time >= self.invulnerability_time:
                    self.invulnerable = False

            if not self.playing:
                self.invulnerable = False

            if not self.invulnerable:
                self.player.update(self.game_speed, user_input, self.bullet_handler)
                self.player.check_bounds(SCREEN_WIDTH)
                self.enemy_handler.update(self.bullet_handler)
                self.rock_handler.update(self.game_speed)
                self.power_up_handler.update(self.player)
                self.elapsed_time = time.time() - self.start_time
                self.y_pos_bg += self.game_speed
                self.change_background()
                self.bullet_handler.update(self.player, self.enemy_handler.enemies)
                self.score = self.enemy_handler.enemies_destroyed

                
                if random.random() < 0.02:
                    x_pos = random.randint(0, SCREEN_WIDTH - Rock.WIDTH)
                    y_pos = 0
                    speed = random.randint(2, 6)
                    self.rock_handler.add_rock((x_pos, y_pos), speed)


                self.rock_handler.remove_off_screen()



                if not self.invulnerable:
                    for rock in self.rock_handler.rocks:
                        if rock not in self.collided_rocks and self.player.rect.colliderect(rock.rect):
                            self.collided_rocks.add(rock)  
                            self.player.invulnerable = True
                            self.invulnerable_start_time = time.time()
                            self.player.lives -= 1
                            if self.player.lives <= 0:
                                self.playing = False
                                self.number_deaths += 1
                                self.last_score = self.score
                                self.total_score += self.last_score
                                if self.last_score > self.max_score:
                                    self.max_score = self.last_score
                                if self.last_score > self.record_score:
                                  self.record_score = self.last_score

                                self.draw_menu()
                                self.invulnerable = True
                                self.invulnerable_start_time = time.time()
                            else:
                                self.reset_player_position()
                                self.score = 0
                                self.invulnerable = True
                                self.invulnerable_start_time = time.time()
         

                self.player.handle_collision(self.rock_handler.rocks)
                if not self.player.is_alive:
                    pygame.time.delay(300)
                    self.player.lives -= 1

                    if self.player.lives <= 0:
                        self.playing = False
                        self.number_deaths += 1
                        self.last_score = self.score
                        self.total_score += self.last_score
                        if self.last_score > self.max_score:
                            self.max_score = self.last_score
                        if self.last_score > self.record_score:
                            self.record_score = self.last_score

                        self.draw_menu()
                        self.invulnerable = True
                        self.invulnerable_start_time = time.time()
                    else:
                        self.reset_player_position()
                        self.score = 0
                        self.invulnerable = True
                        self.invulnerable_start_time = time.time()

        else:
            self.draw_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.restart_game()
                    self.playing = True
                    self.start_time = time.time()

       


    def restart_game(self):
        self.player.lives = 20 
        self.reset()

    def reset_player_position(self):
        self.player.reset()

    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.rock_handler.draw(self.screen)
            self.power_up_handler.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()    
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



    def draw_menu(self):
        if self.number_deaths == 0:
            menu_image = pygame.transform.scale(FUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(menu_image, (0, 0))
        else:
            menu_image = pygame.transform.scale(FUND2, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(menu_image, (0, 0))
            score, score_rect = text_utils.get_message(f"Your score is: {self.last_score}", 30, WHITE, height=SCREEN_HEIGHT // 2 + 50)
            total_score, total_score_rect = text_utils.get_message(f"Total score: {self.total_score}", 30, WHITE, height=SCREEN_HEIGHT // 2 + 100)
            record_score, record_score_rect = text_utils.get_message(f"Record Score: {self.get_record_score()}", 30, WHITE, height=SCREEN_HEIGHT // 2 + 150)
            time_text, time_rect = text_utils.get_message(f"Time: {int(self.elapsed_time)} s", 30, WHITE, height=SCREEN_HEIGHT // 2 + 200)
            max_score_text, max_score_rect = text_utils.get_message(f"Max Score: {self.max_score}", 30, WHITE, height=SCREEN_HEIGHT // 2 + 350)
            self.screen.blit(record_score, record_score_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(total_score, total_score_rect)
            self.screen.blit(time_text, time_rect)
            self.screen.blit(max_score_text, max_score_rect)

  



          

        
    def draw_score(self):
        score, score_rect = text_utils.get_message(f"Your score is: {self.score}", 20, WHITE, 1000, 40)
        time_text, time_rect = text_utils.get_message(f"Time: {int(self.elapsed_time)} s", 20, WHITE, 60, 40)
        lives_text, lives_rect = text_utils.get_message(f"Lives: {self.player.lives}", 20, WHITE, 60, 70) 
        self.screen.blit(time_text, time_rect)
        self.screen.blit(score, score_rect)
        self.screen.blit(lives_text, lives_rect) 
    

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_up_handler.reset()
        self.score = 0
    

    def reset_elapsed_time(self):
        self.elapsed_time = 0

    
    def get_record_score(self):
        return self.record_score