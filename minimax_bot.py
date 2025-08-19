import chess
from helper.piece_values import PIECE_VALUES

def evaluate_board(board):
    """Enhanced evaluation function with material, center control, mobility, and king safety."""

    # Terminal state handling
    if board.is_checkmate():
        return float('-inf') if board.turn == chess.WHITE else float('inf')
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    # Score Evaluation Criteria
    # The higher the evaluation, the better the position for White. Conversely, the lower the evaluation, the better the position for Black
    #
    # 1. Material Evaluation
    #   This evaluates the material balance on the board. All the pieces on the board are added and subtracted based on their type and color
    #
    # 2. Center Control
    #   This evaluates control over the center squares (D4, D5, E4, E5). A piece on these squares gives a slight bonus
    #
    # 3. Mobility
    #   This evaluates the number of legal moves available. More moves generally indicate a better position
    #
    # 4. King Safety
    #   This evaluates the safety of the kings. If a king is attacked, it incurs a penalty

    score = 0

    # Material evaluation
    for piece_type in PIECE_VALUES:
        score += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]

    # Center control bonus
    center_squares = [chess.D4, chess.D5, chess.E4, chess.E5]
    for square in center_squares:
        piece = board.piece_at(square)
        if piece:
            if piece.color == chess.WHITE:
                score += 0.5
            else:
                score -= 0.5

    # Mobility (number of legal moves)
    white_mobility = len(list(board.legal_moves)) if board.turn == chess.WHITE else 0
    board.push(chess.Move.null())  # Switch turn
    black_mobility = len(list(board.legal_moves)) if board.turn == chess.BLACK else 0
    board.pop()

    score += 0.1 * (white_mobility - black_mobility)

    # King safety
    white_king_sq = board.king(chess.WHITE)
    black_king_sq = board.king(chess.BLACK)

    for square in chess.SquareSet(chess.SQUARES):
        if board.is_attacked_by(chess.BLACK, square) and square == white_king_sq:
            score -= 0.5
        if board.is_attacked_by(chess.WHITE, square) and square == black_king_sq:
            score += 0.5

    return score

def minimax(board, depth, is_maximizing):
    """Minimax recursive function."""
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if is_maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval

def choose_minimax_move(board, depth=5):
    """Choose the best move using the minimax algorithm"""

    # Save whose turn it is (True for White, False for Black)
    is_white_turn = board.turn

    best_move = None
    best_value = float('-inf') if is_white_turn else float('inf')

    for move in board.legal_moves:
        board.push(move)
        board_value = minimax(board, depth - 1, not is_white_turn)
        board.pop()

        if is_white_turn:
            if board_value > best_value:
                best_value = board_value
                best_move = move
        else:
            if board_value < best_value:
                best_value = board_value
                best_move = move

    return best_move