import random
import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 120
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BACKGROUND_IMAGES = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track12.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track13.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track14.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track15.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track16.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track17.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track18.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track19.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track120.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track121.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track122.png'))
]

BACKGROUND_IMAGE_PURPLE = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track21.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track22.png'))
]

BG_1 = random.choice(BACKGROUND_IMAGES)
BG_2 = random.choice(BACKGROUND_IMAGE_PURPLE)
BG_3 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track3.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ALIEN = pygame.image.load(os.path.join(IMG_DIR, "Enemy/Alien.png"))
OVNI = pygame.image.load(os.path.join(IMG_DIR, "Enemy/Ovni.png"))
SHIP_EAT = pygame.image.load(os.path.join(IMG_DIR, "Enemy/naveeat.png"))
BOSS =  pygame.image.load(os.path.join(IMG_DIR, "Enemy/Boss.png")) 

FONT_STYLE = 'freesansbold.ttf'

LEFT = "left"
RIGHT = "right"

OBSTACLE = pygame.image.load(os.path.join(IMG_DIR, "Obstacle/rock.1.png"))


