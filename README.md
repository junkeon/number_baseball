# Number Baseball Game

This project implements a number baseball game. Users can set the number of rounds, the length of the target number, and the game mode.

## Class: Game

This class represents a number baseball game. It has attributes for the number of rounds, the length of the target number, the target number itself, the game mode, and the game's history.

### Methods

- `set_rounds()`: Sets the number of rounds in the game.
- `set_length()`: Sets the length of the target number.
- `set_mode()`: Sets the game mode.
- `play_alone()`: Plays the game in Alone mode.
- `play_auto()`: Plays the game in Auto mode.
- `play_compete()`: Plays the game in Compete mode.

## Game Modes

- Alone: The user plays the game alone.
- Auto: The computer plays the game automatically.
- Compete: The user and the computer compete against each other.

## How to Run

This project is written in Python 3. You can run it in a Python 3 environment as follows:

```bash
from number_baseball import *

Game().start()
```

When you start the game, you will be prompted to enter the number of rounds, the length of the target number, and the game mode. Enter these values to start the game.