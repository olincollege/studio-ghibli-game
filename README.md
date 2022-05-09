# studio-ghibli-game

This repository contains Kiki's Delivery Service, a game created by Anusha and Liv.

## Game Overview

The goal of this game is for the player (playing as Kiki) to collect as many packages as possible while flying and avoiding geese. The game ends when the player loses all three of their lives by running into geese.

## Installation and Setup

To play this game, in addition to python, pygame must be installed. If not already installed, run `$ pip install pygame`. The testing framework uses pytest, which can be installed by running `$ pip install pytest`.

To play the game, run the command `python game_model.py` from the command line.

## File Structure

The file struction consists of the following `.py` files:
* `game_model.py`: Contains the main functionality of the game.
* `constants.py`: Stores constant values, such as the width and height of the game display.
* `game_objects.py`: Contains classes and attributes for the objects of the game (player, geese, and packages).
* `game_view.py`: Contains a display class to create and display the start, game, and end screens.
* `game_controller.py`: Contains a controller class to translate user key and exit inputs into actions.

### Static Files

The `/images` folder houses the graphics files for game objects and screens.

## Attribution

All images were obtained from the movie Kiki's Delivery Service by Studio Ghibli.

We used a [series of tutorials](https://www.youtube.com/watch?v=DHgj5jhMJKg&list=PLjcN1EyupaQm20hlUE11y9y8EY2aXLpnv) by [Coding with Russ](https://www.youtube.com/channel/UCPrRY0S-VzekrJK7I7F4-Mg) to learn some of the basics of pygame when starting this project.
