import chess
from helper.pgn_helper import create_pgn_game
import random
from minimax_bot import choose_minimax_move

def choose_random_move(board):
    """Very basic bot: randomly chooses one of the legal moves."""
    return random.choice(list(board.legal_moves))

def play_game():
    board = chess.Board()

    # Create the root PGN game node
    game = create_pgn_game()

    node = game

    while not board.is_game_over():
        print(board)
        print("Turn:", "White" if board.turn == chess.WHITE else "Black")

        #move = choose_random_move(board) #Literally chooses a random move
        move = choose_minimax_move(board, depth=3) # This is an improvement over random moves. Evaluates on several criteria to a selected depth
        print("Chosen move:", move)

        board.push(move)

        # Add move to PGN
        node = node.add_variation(move)

    print("\nGame over!")
    print("Result:", board.result())
    print(board)

    # Set result in PGN
    game.headers["Result"] = board.result()

    # Save to PGN file
    with open("game_output.pgn", "w") as pgn_file:
        print(game, file=pgn_file)

    print("Game saved to game_output.pgn")

if __name__ == "__main__":
    play_game()