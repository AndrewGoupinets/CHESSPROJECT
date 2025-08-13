import chess
import chess.pgn
import random
import datetime

def choose_random_move(board):
    """Very basic bot: randomly chooses one of the legal moves."""
    return random.choice(list(board.legal_moves))

def play_game():
    board = chess.Board()

    # Create the root PGN game node
    game = chess.pgn.Game()
    game.headers["Event"] = "Random Bot Match"
    game.headers["Site"] = "Local"
    game.headers["Date"] = datetime.datetime.now().strftime("%Y.%m.%d")
    game.headers["White"] = "RandomBot"
    game.headers["Black"] = "RandomBot"

    node = game

    while not board.is_game_over():
        print(board)
        print("Turn:", "White" if board.turn == chess.WHITE else "Black")

        move = choose_random_move(board)
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