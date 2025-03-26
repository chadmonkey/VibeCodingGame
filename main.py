import pygame

pygame.init()

# Define screen details
WIDTH, HEIGHT = 500, 500
ROWS, COLS = 10, 10
CELL_SIZE = WIDTH // ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Outer Ring Gameboard")


# Function to draw the outer ring board
def draw_board():
    screen.fill((0, 0, 0))  # Black background
    for row in range(ROWS):
        for col in range(COLS):
            # Only draw cells in the outer ring (row or col is 0 or max)
            if row == 0 or row == COLS - 1 or col == 0 or col == ROWS - 1:
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, (255, 255, 255), rect, 2)  # White border with thickness = 2


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board()
    pygame.display.flip()

pygame.quit()
