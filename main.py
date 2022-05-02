import pygame
from game_objects import Geese, Packages, Player
from game_view import GraphicsView
from game_controller import KeyController
import constants

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

run = True

while run:
    fps_clock.tick(constants.FPS)
    screen.fill_background()
    print(pygame.time.get_ticks())
    if pygame.time.get_ticks() % 100 == 0:
        package = Packages(2)
        packages_group.add(package)
        goose = Geese(2)
        geese_group.add(goose)

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
        run = False

    print(score)
    print(lives)

    geese_group.update()
    packages_group.update()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
