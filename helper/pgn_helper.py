import chess.pgn
import datetime

def create_pgn_game():
    """Creates and returns a new PGN game with default headers."""
    game = chess.pgn.Game()
    game.headers["Event"] = "Random Bot Match"
    game.headers["Site"] = "Local"
    game.headers["Date"] = datetime.datetime.now().strftime("%Y.%m.%d")
    game.headers["White"] = "White Knight"
    game.headers["Black"] = "Black Knight"
    return game