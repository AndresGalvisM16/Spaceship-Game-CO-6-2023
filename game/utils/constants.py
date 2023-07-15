import random
import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 60
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))




SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))


BACKGROUND_IMAGES = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track11.png'))
]


BG_1 = random.choice(BACKGROUND_IMAGES)



BG_2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track2.png'))
BG_3 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track3.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))

FONT_STYLE = 'freesansbold.ttf'

LEFT = "left"
RIGHT = "right"
