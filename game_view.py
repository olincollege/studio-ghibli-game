"""
Display home/start screen, background of game, win/death screen, scores.
"""
import pygame
import constants
from game_objects import Objects, Packages, Player

pygame.init()


class GraphicsView:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def display_sprite(self, img, rect):
        self.screen.blit(img, rect)

    def fill_background(self, Color):
        #Color = (135, 206, 236)
        self.screen.fill(Color)

    def draw_group(self, group):
        group.draw(self.screen)

    def draw_groups(self, groups):
        for group in groups:
            self.draw_group(group)

    def display_text(self, text, size, x_pos, y_pos):
        font_name = pygame.font.match_font('sarai')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        self.screen.blit(text_surface, text_rect)

    def game_display(self, lives, score, groups):
        self.fill_background((135, 206, 236))
        self.display_text(f"Lives: {lives}", 50,
                          constants.SCREEN_WIDTH - 100, 25)
        self.display_text(f"Score: {score}", 50,
                          constants.SCREEN_WIDTH - 100, 75)
        self.draw_groups(groups)

    def end_display(self, score):
        self.fill_background((135, 206, 236))
        self.display_text(f"Final Score: {score}", 50,
                          constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
        self.display_text(f"Press SPACE To Play Again", 50,
                          constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-50)

    def welcome_display(self):
        self.fill_background((135, 206, 236))
        self.display_text(f"Press Space To Start", 50,
                          constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
