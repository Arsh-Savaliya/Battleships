# Battleships



## 🎮 Overview
Battleships is a two-player strategy game implemented in Python.
Each player places ships on a grid and takes turns guessing coordinates to hit the opponent’s ships.
The first player to sink all enemy ships wins.

This project demonstrates:

- Object-Oriented Programming (OOP)
- File organization in Python
- User input handling
- Board representation and validation logic
- Random ship placement
- ASCII and ANSII

```
Battleships/
│
├── newboard.py       # Board class: grid, placement validation, hit checks
├── ships.py          # Ship and Fleet classes
├── player.py         # Player class, manual ship placing
├── gameManager.py    # Game flow controller (turns, win condition)
├── filemanager.py    # Save/load functionality
├── main.py           # Entry point to start the game
└── README.md         # Project documentation
```

## ▶️ How to Run the Game

1. **Install Python 3.x**
2. **Install Colorama library**
3. **Open a terminal inside the project folder**
4. **Run:** `python3 main.py`

The game will then:
- Ask for player names
- Let players place ships (or place randomly)
- Start the turn-by-turn battle

## 🧩 Game Rules
- Each player has a board (default 10×10).
- Each has a fleet of ships (sizes may vary).
- Ships can be placed horizontal or vertical.
- Players take turns entering coordinates like 3 5.

- The board prints:

  - `~` = Water 
  - `@` = Ship
  - `!` = Hit
  - `S` = Destroyed Ship
  - `M` = Miss
- First player to sink all ships wins.

## 🛠️ Features
- Manual or random ship placement
- Validity checks on ship placement
- Hit/miss detection
- Repeated attack prevention
- Complete turn-based flow
- Clear terminal UI
- Save/load game