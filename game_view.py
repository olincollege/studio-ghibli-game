"""
Display home/start screen, background of game, win/death screen, scores.
"""
import pygame
from game_objects import Objects, Packages, Player

pygame.init()


class GraphicsView:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def display_sprite(self, img, rect):
        self.screen.blit(img, rect)

    def fill_background(self):
        Color = (135, 206, 236)
        self.screen.fill(Color)

    def draw_group(self, group):
        group.draw(self.screen)

    def display_text(self, text, size, x_pos, y_pos):
        font_name = pygame.font.match_font('sarai')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        self.screen.blit(text_surface, text_rect)
