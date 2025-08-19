# Chess Project

This is a Python-based chess project that includes a chess engine capable of playing games using a minimax algorithm with an evaluation function. The project also supports saving games in PGN format.

## Features

- **Minimax Bot**: A chess bot that uses the minimax algorithm to make decisions.
- **Evaluation Function**: Evaluates board positions based on material and positional factors.
- **PGN Support**: Saves completed games in PGN format for analysis.
- **Random Move Bot**: A simple bot that makes random legal moves (for testing purposes).

## Installation

1. Clone the repository:
   git clone https://github.com/<your-username>/CHESSPROJECT.git
   cd CHESSPROJECT

2. Install the required dependencies
    pip install python-chess

## Usage

Run the main script to play a game:
    python engine_interface.py

## How It Works

The game alternates between players (or bots) until a checkmate, stalemate, or draw occurs.
The minimax bot evaluates moves up to a specified depth to determine the best move.
The game is saved in PGN format as game_output.pgn after completion.

## File Structure

engine_interface.py: Main script to play a chess game.
minimax_bot.py: Contains the minimax algorithm and evaluation function.
pgn_helper.py: Handles PGN game creation and saving.