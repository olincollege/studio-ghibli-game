"""
Display home/start screen, background of game, win/death screen, scores.
"""
import pygame
import constants

pygame.init()


class GraphicsView:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def fill_background(self, Color):
        #Blue = (135, 206, 236)
        self.screen.fill(Color)

    def draw_background(self, image, dims):
        self.rect = image.get_rect()
        self.image = pygame.transform.scale(image, dims)
        self.screen.blit(self.image, self.rect)

    def draw_group(self, group):
        group.draw(self.screen)

    def draw_groups(self, groups):
        for group in groups:
            self.draw_group(group)

    def display_text(self, text, size, x_pos, y_pos, color=(255, 255, 255)):
        font_name = pygame.font.match_font('sarai')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        self.screen.blit(text_surface, text_rect)

    def game_display(self, lives, score, groups):
        self.fill_background((135, 206, 236))
        self.display_text(f"Lives: {lives}", 50,
                          constants.SCREEN_WIDTH - 100, 25, (0, 0, 0))
        self.display_text(f"Score: {score}", 50,
                          constants.SCREEN_WIDTH - 100, 75, (0, 0, 0))
        self.draw_groups(groups)

    def end_display(self, score):
        self.fill_background((135, 206, 236))
        self.draw_background('images/End_screen.png',
                             constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.display_text(f"Final Score: {score}", 50,
                          constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-50)
        self.display_text(f"Press SPACE To Play Again", 50,
                          constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    def welcome_display(self):
        self.fill_background((135, 206, 236))
        self.draw_background('images/Welcome_screen.png',
                             constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.display_text(f"Welcome to Kiki's Delivery Game", 50,
                          constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-50)
        self.display_text(f"Press Space To Start", 50,
                          constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
