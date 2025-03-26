import pygame

pygame.init()

# Define screen details
WIDTH, HEIGHT = 576, 576
ROWS, COLS = 9, 9
CELL_SIZE = WIDTH // ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Outer Ring Gameboard")


# Function to draw the outer ring board
def draw_board():
    board_surface = pygame.Surface((WIDTH, HEIGHT))  # Create a separate surface for the board
    board_surface.fill((0, 0, 0))  # Black background
    for row in range(ROWS):
        for col in range(COLS):
            # Draw cells in the outer ring (row or col is 0 or max) or the middle ring (rows and cols 2-6)
            if row == 0 or row == COLS - 1 or col == 0 or col == ROWS - 1 or (
                    2 <= row <= 6 and (col == 2 or col == 6)) or (2 <= col <= 6 and (row == 2 or row == 6)):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(board_surface, (255, 255, 255), rect, 2)  # White border with thickness = 2

    # Add 16x16 red square in the middle of the top center cell
    top_center_x = (COLS // 2) * CELL_SIZE + (CELL_SIZE - 16) // 2  # Horizontal center of top cell
    top_center_y = (CELL_SIZE - 16) // 2  # Vertical center of top cell
    red_square = pygame.Rect(top_center_x, top_center_y, 16, 16)
    pygame.draw.rect(board_surface, (255, 0, 0), red_square)  # Red square
    return board_surface


# Cache the board and draw it once
board = draw_board()
screen.blit(board, (0, 0))
pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
