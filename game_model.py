"""
This file contains all the code to run an instance of the game
"""
import pygame
from game_objects import Geese, Packages, Player
from game_view import GraphicsView
from game_controller import KeyController
import constants


def main():
    """
    This function runs a instance of the full game
    """
    pygame.init()

    # intialize the screen, contorller, and player
    screen = GraphicsView(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    controller = KeyController()
    player = Player()

    # create groups to store different kinds of sprites
    player_group = pygame.sprite.Group()
    player_group.add(player)
    packages_group = pygame.sprite.Group()
    geese_group = pygame.sprite.Group()

    # create variables to handle time
    fps_clock = pygame.time.Clock()
    package_time = pygame.time.get_ticks()
    goose_time = pygame.time.get_ticks()

    # create variabels to store score and lives
    lives = 3
    score = 0

    # create variables to control which game screen the user sees
    run = True
    welcome_screen = True
    game_screen = False
    end_screen = False

    while run:

        while welcome_screen:
            # display the welcome screen and update it
            screen.welcome_display()
            pygame.display.flip()

            # if space is pressed, move to game screen. if exit is pressed, quit
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                welcome_screen = False
                game_screen = True
                break
            controller.check_exit()

        while game_screen:
            # make the clock tick
            fps_clock.tick(constants.FPS)

            # check if you need to quit
            controller.check_exit()

            # spawn a package or a goose depending on the time
            if pygame.time.get_ticks() - package_time >= 1500:
                package = Packages()
                packages_group.add(package)
                package_time = pygame.time.get_ticks()
            if pygame.time.get_ticks() - goose_time >= 1100:
                goose = Geese()
                geese_group.add(goose)
                goose_time = pygame.time.get_ticks()

            # check which keys are pressed and move the charecter
            pressed_keys = controller.get_move()
            player.move(pressed_keys)

            # check if the charecter has colided with objects
            if player.collide(player_group, packages_group):
                score += 1
            if player.collide(player_group, geese_group):
                lives -= 1

            # draw the screen display
            screen.game_display(
                lives, score, [packages_group, geese_group, player_group])

            # check if player has died
            if lives == 0:
                game_screen = False
                end_screen = True

            # update everything
            geese_group.update()
            packages_group.update()
            pygame.display.update()

        while end_screen:
            # display the end screen
            screen.end_display(score)
            pygame.display.flip()

            # if space is pressed, reset the game and go back to game screen
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                lives = 3
                score = 0
                player.rect.y = constants.SCREEN_HEIGHT/2
                geese_group.empty()
                packages_group.empty()
                game_screen = True
                end_screen = False
                break
            # if exit is pressed, quit
            controller.check_exit()

    pygame.quit()


if __name__ == '__main__':
    main()
