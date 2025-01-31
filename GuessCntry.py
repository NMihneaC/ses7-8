import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

selected_piece = None  # Stores (row, col) of selected piece
dragging = False  # Tracks if the piece is being moved

# Main function
def main():
    global selected_piece, dragging

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess Game')
    images = load_images()
    board = starting_position  # Use the initial board setup

    running = True
    while running:
        draw_board(win)
        draw_pieces(win, board, images)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                if board[row][col]:  # Check if a piece is there
                    selected_piece = (row, col)
                    dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    x, y = pygame.mouse.get_pos()
                    new_row, new_col = y // SQUARE_SIZE, x // SQUARE_SIZE
                    move_piece(board, selected_piece, (new_row, new_col))
                    selected_piece = None
                    dragging = False

        pygame.display.update()
def move_piece(board, start, end):
    start_row, start_col = start
    end_row, end_col = end

    if board[start_row][start_col]:  # Make sure a piece exists
        board[end_row][end_col] = board[start_row][start_col]  # Move piece
        board[start_row][start_col] = None  # Remove from old spot




if __name__ == '__main__':
    main()