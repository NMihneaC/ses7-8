import pygame
print(pygame.__version__)



def move_piece(board, start, end):
    start_row, start_col = start
    end_row, end_col = end

    # Ensure the start square is not empty
    if board[start_row][start_col] is None:
        return  # No piece to move

    piece = board[start_row][start_col]  # The piece to move

    # Get the legal moves for the piece
    legal_moves = get_legal_moves(board, start_row, start_col, piece)

    # Prevent moving out of bounds or to an illegal square
    if (end_row, end_col) not in legal_moves:
        return  # Illegal move, so don't move the piece

    # Ensure the destination is either empty or has an enemy piece
    if board[end_row][end_col] is None or board[end_row][end_col][0] != piece[0]:
        board[end_row][end_col] = piece  # Move the piece
        board[start_row][start_col] = None  # Clear the old position

def move_piece(board, start, end):
    start_row, start_col = start
    end_row, end_col = end

    # ✅ Prevent moving out of bounds
    if not (0 <= end_row < 8 and 0 <= end_col < 8):
        return  # Ignore invalid moves

    # ✅ Ensure there is a piece to move
    if board[start_row][start_col] is None:
        return

    # ✅ Move the piece only if the destination is empty or an enemy piece
    if board[end_row][end_col] is None or board[end_row][end_col][0] != board[start_row][start_col][0]:
        board[end_row][end_col] = board[start_row][start_col]  # Move piece
        board[start_row][start_col] = None  # Clear old position