import pygame
from game.components.impacts.impact import Rock

class RockHandler:
    def __init__(self):
        self.rocks = []

    def update(self, game_speed):
        for rock in self.rocks:
            rock.update()

    def draw(self, screen):
        for rock in self.rocks:
            rock.draw(screen)

    def add_rock(self, center, speed):
        rock = Rock(center)
        self.rocks.append(rock)

    def remove_off_screen(self):
        self.rocks = [rock for rock in self.rocks if not rock.check_out_of_screen()]
