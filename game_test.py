"""
Test functions for the studio ghibli game.
"""
import operator
import pytest
import pygame
from game_objects import Player, Geese, Packages, collide

pygame.init()

test_player = Player()
test_goose = Geese()
test_package = Packages()

player_group = pygame.sprite.Group()
player_group.add(test_player)
packages_group = pygame.sprite.Group()
packages_group.add(test_package)
geese_group = pygame.sprite.Group()
geese_group.add(test_goose)

update_cases = [
    # test that geese and pacakges move to the left when updated
    test_goose,
    test_package
]

Up_dictionary = {
    pygame.K_UP: True
}
Down_dictionary = {
    pygame.K_DOWN: True,
    pygame.K_UP: False
}
Both_dictionary = {
    pygame.K_UP: True,
    pygame.K_DOWN: True
}
Space_dictionary = {
    pygame.K_SPACE: True,
    pygame.K_UP: False,
    pygame.K_DOWN: False
}
move_cases = [
    # test that the player moves up when up is pressed
    (test_player, Up_dictionary, operator.lt),
    # test that the player moves down when down is pressed
    (test_player, Down_dictionary, operator.gt),
    # test that the player moves up when both pressed
    (test_player, Both_dictionary, operator.lt),
    # test that the player does not move when none are pressed
    (test_player, Space_dictionary, operator.eq)
]

collision_player = Player()
collision_group = pygame.sprite.Group()
collision_group.add(collision_player)
collide_cases = [
    # test that the player collides with a coincident sprite
    (player_group, collision_group, {test_player: [collision_player]}),
    # test that the player does not colide with a non-coincident sprite
    (player_group, geese_group, {}),
]

test_package_2 = Packages()


def test_create():
    """
    Test that randomly generated packages generate with different y values.
    """
    package_1_y = test_package.rect.y
    package_2_y = test_package_2.rect.y
    assert package_1_y != package_2_y


@pytest.mark.parametrize("sprite", update_cases)
def test_update(sprite):
    """
    Test that packages and geese correctly move to the left when updated.

    Args:
        sprite: the sprite to update
    """
    current_x = sprite.rect.x
    sprite.update()
    assert current_x > sprite.rect.x


@pytest.mark.parametrize("sprite, dictionary, relate", move_cases)
def test_move(sprite, dictionary, relate):
    """
    Test that the player moves correctly when different keys are pressed.

    Args:
        sprite: the player sprite
        dictionary: a dictionary of pressed keys
        relate: an operator to tell if the sprite has moved in the
            right direction
    """
    current_y = sprite.rect.y
    sprite.move(dictionary)
    assert relate(sprite.rect.y, current_y) is True


@pytest.mark.parametrize("group_1, group_2, dictionary", collide_cases)
def test_collide(group_1, group_2, dictionary):
    """
    Test that collisions are correctly detected between the player and objects.

    Args:
        group_1: a pygame group with one type of sprite to check collision
        group_2: a pygame group with one type of sprite to check collision
        dictionary: a dictionary containing the list of sprites that collide
    """
    assert collide(group_1, group_2) == dictionary
