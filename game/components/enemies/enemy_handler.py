import pygame
import random
from game.components.enemies.ship import Ship, AlienEnemy, Onvi, Ship_eat
from game.components.enemies.Boss import Boss 
from game.utils.constants import SCREEN_HEIGHT

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies_destroyed = 0
        self.onvi_added = False
        self.alien_added = False
        self.boss_added = False
        self.alienemy_spawn_time = 40 * 1000  
        self.ship_eat_spawn_time = 15 * 1000 
        self.ship_spawn_time = 25 * 1000
        self.onvi_spawn_time = 35 * 1000  
        self.boss_spawn_time = 60 * 1000  
        self.start_time = pygame.time.get_ticks() 

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_visible or not enemy.is_alive:
                self.remove_enemy(enemy)
            if not enemy.is_alive:
                self.enemies_destroyed += 1

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time

        if len(self.enemies) < 10:
            if not self.alien_added and elapsed_time >= self.alienemy_spawn_time:
                self.enemies.append(AlienEnemy())
                self.alien_added = True

            if not self.onvi_added and elapsed_time >= self.onvi_spawn_time:
                self.enemies.append(Onvi())
                self.onvi_added = True

            ship_count = sum(1 for enemy in self.enemies if isinstance(enemy, Ship))
            if ship_count < 3 and elapsed_time >= self.ship_spawn_time:
                self.enemies.append(Ship())

            ship_eat_count = sum(1 for enemy in self.enemies if isinstance(enemy, Ship_eat))
            if ship_eat_count < 2 and elapsed_time >= self.ship_eat_spawn_time:
                self.enemies.append(Ship_eat())

            if not self.boss_added and elapsed_time >= self.boss_spawn_time:
                self.enemies.append(Boss())
                self.boss_added = True

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []
        self.enemies_destroyed = 0