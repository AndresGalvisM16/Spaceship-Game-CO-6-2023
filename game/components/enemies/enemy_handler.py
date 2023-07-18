import pygame
import random
from game.components.enemies.ship import ship, AlienEnemy, Onvi, Ship_eat
from game.components.enemies.Boss import Boss 
from game.utils.constants import SCREEN_HEIGHT


class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.onvi_added = False
        self.alien_added = False
        self.boss_added = False
        self.boss_spawn_time = 30 * 1000  # 10 segundos en milisegundos
        self.start_time = pygame.time.get_ticks()  # Tiempo en el que se inició el juego

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_visible:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 10:
            if not self.alien_added:
                self.enemies.append(AlienEnemy())
                self.alien_added = True

            if not self.onvi_added:
                self.enemies.append(Onvi())
                self.onvi_added = True

            ship_count = sum(1 for enemy in self.enemies if isinstance(enemy, ship))
            if ship_count < 5:
                self.enemies.append(ship())

            ship_eat_count = sum(1 for enemy in self.enemies if isinstance(enemy, Ship_eat))
            if ship_eat_count < 2:
                self.enemies.append(Ship_eat())

            elapsed_time = pygame.time.get_ticks() - self.start_time
            if not self.boss_added and elapsed_time >= self.boss_spawn_time:
                self.enemies.append(Boss())
                self.boss_added = True

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)