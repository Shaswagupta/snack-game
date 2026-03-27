# Snack Game

A classic snake game built with Python using the Turtle graphics library.

## Description

This is a fun implementation of the classic Snake game where the player controls a snake that moves around the screen eating food and growing longer. The game ends if the snake hits the wall or collides with itself.

## Features

- Classic snake gameplay mechanics
- Real-time score tracking
- Food spawning at random locations
- Collision detection (walls and self)
- Snake growth on food consumption
- Game over screen

## Requirements

- Python 3.x
- turtle (built-in with Python)

## How to Run Locally

### Prerequisites
- Python 3.x installed on your computer
- Clone or download this repository

### Setup & Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shaswagupta/snack-game.git
   cd snack-game
   ```

2. **Run the game:**
   ```bash
   python main.py
   ```

The game window will open and you can start playing immediately!

### Running from PyCharm (if using PyCharm IDE)
1. Open the project in PyCharm
2. Right-click on `main.py`
3. Select "Run 'main.py'"

## Controls

- **Up Arrow** - Move Up
- **Down Arrow** - Move Down
- **Right Arrow** - Move Right
- **Left Arrow** - Move Left

## Game Rules

1. Use the arrow keys to control the snake
2. Eat the red food to grow and increase your score
3. Don't hit the walls or yourself!
4. Game ends when the snake hits a boundary or itself

## 🌐 Hosting & Online Play

This game is built with Python's **Turtle library**, which is a **desktop application** that runs locally on your computer. It cannot be played directly in a web browser without major modifications.

### Want to play online?
The easiest way is to **clone and run locally** (see instructions above). This requires Python installed on your machine.

### Want to convert to web-based?
To make this a web game, you could:
- Rewrite it using **Pygame** + **Pygame Web** or **Pygbag**
- Use **JavaScript** with canvas libraries like **p5.js** or **Phaser**
- Use **Python + Flask/Django** with **Pygame** for backend rendering

Currently, this project is optimized for **local desktop play**. No hosting link is available, but the game runs smoothly once you clone and run it!

## Files

- `main.py` - Main game loop
- `snake.py` - Snake class and logic
- `food.py` - Food class and spawning logic
- `scoreBoard.py` - Score tracking and display

## Author

Shaswat Gupta

## License

MIT

