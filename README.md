# Connect Four Game

## Overview

This Python script implements a text-based version of the classic Connect Four game, a two-player connection board game. Players take turns dropping colored discs from the top into a vertically suspended grid, and the goal is to connect four of one's own discs of the same color in a row, vertically, horizontally, or diagonally, before the opponent.

## Features

- **Interactive Gameplay:** Players take turns to input their moves, selecting a column to drop their disc into the grid.

- **Win Conditions:** The game checks for win conditions after each move, determining if a player has successfully connected four discs in a row.

- **Dynamic Board Display:** The game displays the current state of the game board after each move, providing a visual representation of the disc placement.

- **Randomized Starting Player:** The starting player is randomly determined at the beginning of the game.

## How to Play

1. **Board Representation:** The game board is represented by a grid with rows and columns.

2. **Player Turns:** Players take turns entering a column (designated by uppercase letters) to drop their disc.

3. **Winning:** The game continues until a player connects four discs vertically, horizontally, or diagonally. The winning player is then announced.

4. **Invalid Moves:** The game ensures that players enter a valid and unoccupied column for their move. If an invalid move is entered, the player is prompted to input a valid column.

5. **Game Termination:** The game terminates after a player wins, and the final state of the board is displayed.

## Game Configuration

- **Rows and Columns:** The dimensions of the game board are configured with `ROWS` and `COLS` constants.

- **Players:** The number of players is configured with the `PLAYERS` constant.

- **Markers:** Different markers ("X", "O", "V", "H", "M") are used for each player, and they rotate based on the turn.

## Getting Started

1. **Run the Script:** Execute the script in a Python environment.

2. **Follow Prompts:** Enter column letters when prompted to make your move.

3. **Winning:** Connect four discs in a row vertically, horizontally, or diagonally to win the game.

4. **Game End:** The game ends when a player wins, and the final state of the board is displayed.
