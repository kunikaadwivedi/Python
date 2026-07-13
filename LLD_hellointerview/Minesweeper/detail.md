# What is Minesweeper?

Minesweeper is a classic single-player puzzle game where the player’s objective is to reveal all non-mine cells on a grid without triggering a mine. The game requires logic, deduction, and careful strategy.

## Game Overview

The game board is a 2D grid of hidden cells, some of which contain mines.
The player interacts with the board by clicking on cells.
If the revealed cell contains a mine, the game ends in a loss.
If the cell is safe, it reveals a number from 0 to 8 indicating how many of its adjacent cells contain mines.
If the number is 0, all adjacent cells are automatically revealed recursively.
The player can also flag a cell if they suspect it contains a mine.
The game ends in a win when all non-mine cells are revealed.


## Functional Requirements

- Support configurable board sizes and mine counts through difficulty presets (easy, medium, hard)
- The first click is always safe (never a mine)
- Revealing a cell with zero adjacent mines triggers a cascade reveal of neighboring cells
- Players can flag and unflag cells to mark suspected mines
- Flagged cells cannot be revealed until unflagged
- The game detects a win when all non-mine cells are revealed
- The game detects a loss when a mine is revealed
- The system tracks statistics (games played, wins, losses) across multiple games


### Non-Functional Requirements
- The design should follow object-oriented principles with clear separation of concerns
- The system should be modular and extensible to support future features
- As an optional extension, the core game actions can be made thread-safe for concurrent access (a bonus, since the game is single-player)
- The components should be testable in isolation