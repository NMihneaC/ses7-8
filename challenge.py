import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WHITE = (253, 245, 201)
BLACK = (75, 56, 50)


# Load piece images
def load_images():
    pieces = ['bp', 'bk', 'bb', 'bq', 'br', 'bn', 'wp', 'wk', 'wb', 'wq', 'wr', 'wn']
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(
            pygame.image.load(f'assets/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE)
        )
    return images


# Draw board
def draw_board(win):
    colors = [WHITE, BLACK]
    for row in range(ROWS):
        for col in range(COLS):
            color = colors[(row + col) % 2]
            pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


starting_position = [
    ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
]


def draw_pieces(win, board, images):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                win.blit(images[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))


def is_check(board, turn):
    king_pos = None
    for r in range(8):
        for c in range(8):
            if board[r][c] == turn + 'k':
                king_pos = (r, c)
                break
    if not king_pos:
        return False  # Should never happen

    opponent = 'b' if turn == 'w' else 'w'
    for r in range(8):
        for c in range(8):
            if board[r][c] and board[r][c][0] == opponent:
                if king_pos in get_legal_moves(board, r, c, board[r][c]):
                    return True
    return False


def is_checkmate(board, turn):
    if not is_check(board, turn):
        return False
    for r in range(8):
        for c in range(8):
            if board[r][c] and board[r][c][0] == turn:
                legal_moves = get_legal_moves(board, r, c, board[r][c])
                for move in legal_moves:
                    temp_board = [row[:] for row in board]
                    move_piece(temp_board, (r, c), move)
                    if not is_check(temp_board, turn):
                        return False
    return True


def move_piece(board, start, end):
    start_row, start_col = start
    end_row, end_col = end
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = None


def main():
    global selected_piece, dragging
    turn = 'w'  # White starts

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess Game')
    images = load_images()
    board = [row[:] for row in starting_position]  # Ensure board is a mutable copy

    running = True
    while running:
        draw_board(win)
        draw_pieces(win, board, images)

        if is_checkmate(board, turn):
            print(f"Checkmate! {turn.upper()} loses.")
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                if board[row][col] and board[row][col][0] == turn:
                    selected_piece = (row, col)
                    dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    x, y = pygame.mouse.get_pos()
                    new_row, new_col = y // SQUARE_SIZE, x // SQUARE_SIZE

                    piece = board[selected_piece[0]][selected_piece[1]]
                    if piece and piece[0] == turn:
                        legal_moves = get_legal_moves(board, selected_piece[0], selected_piece[1], piece)
                        if (new_row, new_col) in legal_moves:
                            move_piece(board, selected_piece, (new_row, new_col))
                            turn = 'b' if turn == 'w' else 'w'

                    selected_piece = None
                    dragging = False

        pygame.display.update()


if __name__ == '__main__':
    main()
