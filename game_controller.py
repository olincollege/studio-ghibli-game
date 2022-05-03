"""

"""
import pygame

pygame.init()


class KeyController():
    """
    Controls sprite with arrow keys and track state of arrow keys.
    """

    def __init__(self):
        pass

    def get_move(self):
        pressed_keys = pygame.key.get_pressed()
        return pressed_keys

    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
