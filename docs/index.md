## Kiki's Delivery Game

Welcome to Kiki’s Delivery Game! The goal of this project was to create an interactive program. Inspired by Kiki’s Delivery Service from Studio Ghibli, our team created a game where the player plays as Kiki. Your goal is to collect as many packages as possible while flying and avoiding geese.

## Game Overview

Kiki’s Delivery Game starts with Kiki (the player) on the left side of the screen.

<p align="center">
  <img src="kiki.png" width="50%" height="50%"/>
</p>

The player uses the up and down arrow keys to move Kiki vertically in order to avoid geese and collect packages moving horizontally across the screen.

<p align="center">
  <img src="Goose.png" width="50%" height="50%"/>
</p>
<p align="center">
  <img src="Package.png" width="50%" height="50%"/>
</p>

The game ends when the player loses all three of their lives. All artwork is obtained from the movie Kiki’s Delivery Service.

### Game Demo

### Gameplay

Our game has three main screens: a start screen, the gameplay screen, and an end screen. At any point in the game, the player can close the window to close the screen.

The start screen welcomes the player and prompts them to press the spacebar to start the game.

<p align="center">
  <img src="Start_screen.PNG" width="50%" height="50%"/>
</p>

The game screen starts with the player at the horizontal center of the left side of the screen. The lives (which starts at 3) and score (which starts at 0) are displayed in the top right of the screen.

<p align="center">
  <img src="Gameplay_1.PNG" width="50%" height="50%"/>
</p>

After a short pause, packages and geese are generated at random positions on the right side of the screen and move across the screen towards the player. If the player hits a goose, they lose a life, and if they hit a package, they gain a point towards their score.

<p align="center">
  <img src="Gameplay_2.PNG" width="50%" height="50%"/>
</p>

When the player loses all three of their lives, the game transitions to the end screen, which displays the player’s final score and prompts the player to press the spacebar if they wish to play again.

<p align="center">
  <img src="End_screen.PNG" width="50%" height="50%"/>
</p>

## Installation

A detailed installation guide can be found [here](https://github.com/olincollege/studio-ghibli-game#readme).

To play this game, you must have python and pygame installed. You will also need to download all the files in the [studio-ghibli-game repository](https://github.com/olincollege/studio-ghibli-game). Then, navigate to the repository folder and run the following command in the terminal to start playing:

`python game_model.py'

## About Us

## Attribution

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
