from pygame.font import Font
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

def get_message(message, size, color, width = SCREEN_WIDTH//2, height = SCREEN_HEIGHT//2):
    font = Font(FONT_STYLE,size)
