import pygame
from game_objects import Geese, Packages, Player
from game_view import GraphicsView
from game_controller import KeyController
import constants
import random

pygame.init()

screen = GraphicsView(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
controller = KeyController()
player = Player()
objects_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player_group.add(player)
packages_group = pygame.sprite.Group()
geese_group = pygame.sprite.Group()

fps_clock = pygame.time.Clock()
lives = 3
score = 0
start_time = pygame.time.get_ticks()
current_time = pygame.time.get_ticks()

run = True
welcome_screen = True
game_screen = False
end_screen = False

while run:

    while welcome_screen:
        screen.fill_background((135, 206, 236))
        screen.display_text(f"Press Space To Start", 50,
                            constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
        pygame.display.flip()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            welcome_screen = False
            game_screen = True
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    while game_screen:
        fps_clock.tick(constants.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill_background((135, 206, 236))
        if pygame.time.get_ticks() - current_time >= 3000:
            if random.randint(0, 1) == 0:
                package = Packages(2)
                packages_group.add(package)
            else:
                goose = Geese(2)
                geese_group.add(goose)
            current_time = pygame.time.get_ticks()

        screen.draw_group(packages_group)
        screen.draw_group(geese_group)
        screen.draw_group(player_group)

        pressed_keys = controller.get_move()
        player.move(pressed_keys)

        if pygame.sprite.groupcollide(player_group, packages_group, False, True):
            score += 1
        if pygame.sprite.groupcollide(player_group, geese_group, False, True):
            lives -= 1

        screen.display_text(f"Lives: {lives}", 50,
                            constants.SCREEN_WIDTH - 100, 25)
        screen.display_text(f"Score: {score}", 50,
                            constants.SCREEN_WIDTH - 100, 75)

        if lives == 0:
            game_screen = False
            end_screen = True

        geese_group.update()
        packages_group.update()

        pygame.display.update()

        # if pygame.time.get_ticks() >= 5000:
        #    run = False

    while end_screen:
        screen.fill_background((135, 206, 236))
        screen.display_text(f"end screen", 50,
                            constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

pygame.quit()
