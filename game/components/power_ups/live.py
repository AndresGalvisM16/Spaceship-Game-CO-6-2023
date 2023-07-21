from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART_RED

class Heart(PowerUp):
    def __init__(self):
        self.image = HEART_RED
        super().__init__(self.image) 

    def apply_power_up(self, player):
        player.lives += 1