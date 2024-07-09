# AI_TicTacToe
This repository implements a Tic-Tac-Toe game with an unbeatable AI opponent using the Minimax algorithm.

## Features
1.Play against a challenging AI opponent.
2.Minimax algorithm ensures optimal play for the AI.
3.Clean and well-documented code.

## Getting Started
1.Clone the repository: git clone https://github.com/HarsheetT/AI_TicTacToe.git
2.Once in the directory for the project, run pip3 install -r requirements.txt to install the required Python package (pygame) for this project.

## Understanding
There are two main files in this project: runner.py and tictactoe.py. tictactoe.py contains all of the logic for playing the game, and for making optimal moves. runner.py contains all of the code to run the graphical interface for the game. 

## How it Works
The Minimax algorithm explores all possible future game states by simulating every move a player could make. It then assigns a score to each state based on how favorable it is for the AI (maximizing score) and the human player (minimizing score). Finally, the AI chooses the move that leads to the state with the best score.

### Description
Python is used as the programming language and pygame as the GUI for the game
This Project is a part of the CS50's Introduction to Artificial Intelligence with Python.