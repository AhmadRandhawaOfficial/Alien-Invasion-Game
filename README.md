# Alien Invasion Game

Welcome to **Alien Invasion**, a simple 2D space shooter game built using **Python** and **Pygame**. In this game, the player controls a spaceship to shoot and eliminate waves of alien invaders while avoiding collisions.

## Table of Contents
- [Game Description](#game-description)
- [Features](#features)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [File Structure](#file-structure)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [Credits](#credits)

## Game Description

In **Alien Invasion**, players control a spaceship, moving it left, right, up, or down while firing bullets to shoot the incoming alien fleet. The game increases in difficulty as the player advances through levels, with aliens moving faster and becoming more challenging to eliminate.

---

# Project Preview

## Start Game

![Start game](docs/screenshots/start_game.png)

---

## Play Game

![Play game](docs/screenshots/play_game.png)

---

## Start Again

![Start again](docs/screenshots/start_again.png)

---


## Features

- **Dynamic gameplay**: The game's speed increases after each level, making it progressively harder.
- **Scoring system**: Keep track of your score, high score, and level progression.
- **Lives system**: You start with 3 lives (ships), and the game ends when all are lost.
- **Graphical effects**: Simple 2D sprites and graphics enhance the gaming experience.
- **Responsive controls**: Control the ship with arrow keys and shoot with the space bar.

## How to Play

1. Use the **arrow keys** to move the spaceship.
2. Press the **spacebar** to shoot bullets.
3. Destroy all the aliens before they reach the bottom of the screen.
4. Avoid getting hit by the aliens or letting them touch the bottom, or you will lose a life.
5. Earn points for every alien destroyed, and advance to the next level after clearing all aliens.

## Installation

To install and play the game, ensure you have **Python** installed and follow these steps:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/AhmadRandhawaOfficial/AlienInvasion.git
   
2. Install the required dependencies using pip:
   ````bash
   pip install pygame
   
## How to Run
1. After installation, navigate to the game directory:

   ```bash
   cd AlienInvasion

2. Run the main game file:
   ````bash
   python main.py
## File Structure
The main files in this repository are:

- **main.py**: The entry point to the game, containing the game loop and control structure.
- **settings.py**: Handles all the game settings like screen size, speed adjustments, and colors.
- **ship.py**: Contains the ship (player) class for movement and collision detection.
- **alien.py**: Manages alien behavior, movement, and collisions.
- **bullet.py**: Handles bullet behavior and interactions.
- **game_functions.py**: Manages game events, updates, and interactions between objects.
- **scoreboard.py**: Displays the player's score, level, and remaining ships.
- **game_stats.py**: Tracks game statistics such as score and levels.
- **button.py**: Manages button creation and drawing for the game interface.
- **life_ship.py**: Displays a life indicator for the player in the top-right corner, reducing when hit by aliens.

## Technologies Used

- **Python**: Core programming language.
- **Pygame**: Library used for handling graphics, input, and game mechanics.

## Future Plans

- **Power-ups**: Add power-ups like shields or multi-shot capabilities.
- **New enemy types**: Introduce more challenging enemies with different abilities.
- **Multiplayer mode**: Enable two-player mode with split screen or network play.
 

# License

MIT License

---

# Contact 💀 

[<img src="https://img.icons8.com/3d-fluency/30/secured-letter.png" alt="Email" style="vertical-align: middle;"/> official.ahmadrandhawa@gmail.com](mailto:official.ahmadrandhawa@gmail.com)   
[<img src="https://icon.icepanel.io/Technology/svg/LinkedIn.svg" width="26" alt="LinkedIn"/>  LinkedIn Profile](https://www.linkedin.com/in/ahmad-hussain-randhawa/)  
[<img src="https://icon.icepanel.io/Technology/svg/GitHub.svg" width="26" alt="GitHub"/>  GitHub Profile](https://github.com/AhmadHussainRandhawa)   

---

> *"If you have any questions or want to collaborate on something, feel free to email me (without any hesitation)... I might be a little busy sometimes, but I’ll definitely reply."*
