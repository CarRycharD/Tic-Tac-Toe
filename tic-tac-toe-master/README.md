# Tic Tac Toe

## Story

In this project your job is to implement [Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) for two players.
You also can try writing some AI to play the game. If you find it easy, try to make it unbeatable!

## What are you going to learn?

You will learn and practice how to do the following things in Python:
 - variables
 - functions,
 - loops and conditionals,
 - nested lists,
 - print formatting,
 - using external modules,
 - handling user input,
 - error handling.

## Tasks


1. Implement `init_board()` to return an empty 3-by-3 board, i.e. a list of lists filled with zeros. The inner lists are rows.

    - A list of lists is returned, representing a list of rows
    - Every cell of the returned value is `0`
    - The rows of the returned value are independent (changing one row doesn't affect the others)

2. Implement `get_move()` that asks for user input and returns the coordinates of a valid move on board.

    - The player specifies coordinates as letter and number: `A2` is first row and second column, `C1` is third row and first column, etc.
    - The function returns a tuple of two integers: (row, col)
    - The returned coordinates start from 0
    - The integers indicate a valid (empty) position on the board
    - If the user provides coordinates that are outside of board, keep asking
    - If the user provides coordinates for a place that is taken, keep asking
    - If the user provides input that doesn't look like coordinates, keep asking

3. Implement `mark()` that writes the value of `player` (a `1` or `2`) into the `row` & `col` element of `board`.

    - If the cell at `row` and `col` is empty, it is marked with `player`
    - It does not do anything if the coordinates are out of bounds
    - It does not do anything if the cell is already marked

4. Implement `has_won()` that returns `True` if `player` (of value `1` or `2`) has a three-in-a-row on `board`.

    - Returns `True` if `player` has a three-in-a-row on `board`.
    - Returns `False` if `player` doesn't have a three-in-a-row on `board`

5. Implement `is_full()` that returns `True` if the board is full.

    - Returns `True` if there are no empty fields on the board
    - Returns `False` otherwise

6. Implement `print_board()` that prints the board to the screen.

    - Players 1 and 2 are indicated with `X` and `O`, and empty fields are indicated with dots (`.`)
    - There are coordinates displayed around the board
    - The board is displayed in this format:
```
   1   2   3

A  . | . | .
  ---+---+---
B  . | . | .
  ---+---+---
C  . | . | .
```

7. Implement `print-result()` that displays the result of the game.

    - If player 1 wins, print "X won!"
    - If player 2 wins, print "O won!"
    - If nobody wins, print "It's a tie!"

8. Use the implemented functions to write a `tictactoe_game()` function that will run a whole 2-players game.

    - Player 1 starts the game
    - Players alternate their moves (1, 2, 1, 2...)
    - The board is displayed before each move, and at the end of game
    - The game ends when someone wins or the board is full
    - The game handles bad input (wrong coordinates) without crashing

9. [OPTIONAL] Allow players to quit the game anytime by typing `quit`.

    - When the player types `quit` instead of coordinates, the program exits.

10. Implement player-against-AI mode. The AI can drive one of the players, and the game is fully playable against the computer.

    - When `tictactoe_game()` is called with the argument `'HUMAN-AI'` then it calls `get_ai_move()` instead of `get_move()` when it's Player 2's turn
    - When `tictactoe_game()` is called with the argument `'AI-HUMAN'` then it calls `get_ai_move()` instead of `get_move()` when it's Player 1's turn
    - Function `get_ai_move()` returns a valid move (if possible) without asking for any input
    - Function `get_ai_move()` returns `None` if board is full
    - Function `main_menu()` is implemented as a menu for between choosing 2-player mode and against-AI mode by pressing 1 or 2, respectively

11. [OPTIONAL] AI is capable of recognizing the opportunity to win the game with one move.

    - Function `get_ai_move()` picks the winning move if there is one on the board

12. [OPTIONAL] AI is capable of recognizing if its enemy could win the game with the next move, and (supposing there is no direct winning move) moves against it.

    - Function `get_ai_move()` (when there is no winning move in one step) picks a move which prevents a certain winning move for its enemy
    - When there is a direct winning move, function `get_ai_move()` still picks that
    - When there are multiple one-step options for the enemy, `get_ai_move()` tries to prevent one of them

13. [OPTIONAL] AI is unbeatable in all cases.

    - There is no strategy or combination of steps that could win the game aginst the AI

14. [OPTIONAL] AI can play against itself

    - When `tictactoe_game()` is called with the argument `'AI-AI'` then it calls `get_ai_move` for both players
    - The game comes to an end without any user input
    - Game play is easy to follow as there is a 1 seconds delay between the moves


## General requirements


None

## Hints

- You don't have to come up with an AI strategy by yourself, you can search the internet
  for strategy descriptions. But, for your own good, please don't use external code,
  implement written instructions instead.
- You don't have to implement a general playing strategy, Tic-Tac-Toe has a rather
  easy unbeatable strategy that can be expressed as a sequence of conditionals.

## Starting repository

Click here to clone your own Git repository:
<https://classroom.github.com/g/OolWvWl8>

## Background materials

None


## Acceptance review

You will need this only at review time, **after** completing the project.
[Use this form](https://forms.gle/DPiNni5eoxn7uarZ7) to record the review you provide for your peer.