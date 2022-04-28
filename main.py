import pygame
from game_objects import GhibliGameObstacle, GhibliGamePackage, GhibliGameSprite
from game_view import GraphicsView
from game_controller import KeyController

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = GraphicsView(SCREEN_WIDTH, SCREEN_HEIGHT)
player = GhibliGameSprite()
package = GhibliGamePackage(500, 0.25, 2)
obstacle = GhibliGameObstacle(300, 0.25, 2)
controller = KeyController()

fps_clock = pygame.time.Clock()

run = True

while run:
    fps_clock.tick(60)
    screen.fill_background()

    screen.display_sprite(player.img, player.rect)
    screen.display_sprite(package.img, package.rect)
    screen.display_sprite(obstacle.img, obstacle.rect)

    pressed_keys = controller.get_move()
    player.move(pressed_keys)
    package.move()
    obstacle.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
