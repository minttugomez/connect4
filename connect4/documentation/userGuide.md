# User guide

## Installation

Clone the repository:

```bash
git clone git@github.com:minttugomez/connect4.git
```

Install dependencies:

```bash
poetry install
```

## Starting the game

Run the application:

```bash
poetry run invoke start
```

## How to play

- The game starts with player 1 (you).
- On your turn, enter a column number (1-7) to place your marker. Your marker will drop all the way down to the bottom of that column.
- The AI plays its turn automatically. This may take up to 5 seconds.
- After the AI has played its turn, the turn will go back to you.
- The game ends when:
    - A player wins by getting four markers in a row (horizontal, vertical or diagonal)
    - The grid is full, resulting in a draw

## Commands

"exit": lets you exit the game in the middle of it. Can only be done on your own turn.
"yes": to verify you want to exit (anything else counts as a "no")

## Trobleshooting

- Invalid input: you'll be prompted to retry
- Performance issues: if the AI takes too long, try reducing its time limit in AI.py