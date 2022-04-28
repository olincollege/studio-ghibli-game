"""
Display home/start screen, background of game, win/death screen, scores.
"""
import pygame
from game_objects import GhibliGameObject, GhibliGamePackage, GhibliGameSprite

pygame.init()


class GraphicsView:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def display_sprite(self, img, rect):
        self.screen.blit(img, rect)

    def fill_background(self):
        Color = (135, 206, 236)
        self.screen.fill(Color)
