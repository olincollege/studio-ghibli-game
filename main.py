import pygame
from game_objects import Obstacles, Packages, Player
from game_view import GraphicsView
from game_controller import KeyController
import constants

pygame.init()

screen = GraphicsView(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
obstacle = Obstacles(2)
controller = KeyController()
player = Player()
objects_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
packages_group = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()

fps_clock = pygame.time.Clock()

run = True

while run:
    fps_clock.tick(constants.FPS)
    screen.fill_background()

    if pygame.time.get_ticks() % 300 == 0:
        package = Packages(2)
        packages_group.add(package)

    screen.draw_group(packages_group)

    screen.display_sprite(player.image, player.rect)
    screen.display_sprite(obstacle.image, obstacle.rect)

    pressed_keys = controller.get_move()
    player.move(pressed_keys)
    obstacle.update()
    packages_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
