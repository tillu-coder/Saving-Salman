
---

# SAVING SALMAN

## Overview

"SAVING SALMAN" is a fun and engaging 2D game developed using Pygame. In this game, players must help the character Salman avoid obstacles falling from the top of the screen. The goal is to score points by dodging obstacles while keeping Salman safe. The game ends when the player's score falls below zero or when they reach the target score of 5000 points.

## Features

- **Simple Controls**: Move Salman using the W, A, S, and D keys.
- **Obstacle Avoidance**: Dodge falling obstacles to maintain your score.
- **Scoring System**: Earn points by successfully dodging obstacles and lose points upon collision.
- **Win/Loss Conditions**: Reach 5000 points to win, or lose if the score drops below zero.
- **Background Music**: Enjoy background music while playing.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. **Clone the repository** (if applicable) or download the source code.
2. Install Pygame if you haven't already:

   ```bash
   pip install pygame
   ```

3. Ensure the following files are in the `assets` directory:
   - `salman.png`: Image of the character Salman.
   - `obstacle1.png`, `obstacle2.png`, ..., `obstacle6.png`: Images of the obstacles.
   - `background_start.png`: Background image for the start screen.
   - `background_game.png`: Background image for the game screen.
   - `background_win.png`: Background image for the win screen.
   - `background_end.png`: Background image for the end screen.
   - `background_music.mp3`: Background music file.

## Usage

1. Run the game using Python:

   ```bash
   python main.py
   ```

2. Click the "START" button on the start screen to begin playing.
3. Use the W, A, S, and D keys to move Salman and avoid falling obstacles.
4. The game will display "SALMAN DIED" when your score drops below zero, and "SALMAN LIVES" when you reach 5000 points.

## Controls

- **W**: Move up
- **A**: Move left
- **S**: Move down
- **D**: Move right

## License

This project is open source. Feel free to modify and distribute it as you wish.

---