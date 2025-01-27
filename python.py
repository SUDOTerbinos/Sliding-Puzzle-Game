import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game settings
WINDOW_SIZE = 400
GRID_SIZE = 4
TILE_SIZE = WINDOW_SIZE // GRID_SIZE
FONT = pygame.font.Font(None, 80)
BG_COLOR = (50, 50, 50)
TILE_COLOR = (100, 200, 200)
EMPTY_COLOR = BG_COLOR
TEXT_COLOR = (0, 0, 0)

# Create the grid
def create_grid():
    numbers = list(range(1, GRID_SIZE ** 2)) + [None]
    random.shuffle(numbers)
    grid = [numbers[i:i + GRID_SIZE] for i in range(0, len(numbers), GRID_SIZE)]
    return grid

# Draw the grid
def draw_grid(screen, grid):
    screen.fill(BG_COLOR)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = grid[row][col]
            if value is not None:
                tile_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, TILE_COLOR, tile_rect)
                text = FONT.render(str(value), True, TEXT_COLOR)
                text_rect = text.get_rect(center=tile_rect.center)
                screen.blit(text, text_rect)
            else:
                tile_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, EMPTY_COLOR, tile_rect)

# Find the empty tile
def find_empty_tile(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] is None:
                return row, col

# Move the tile
def move_tile(grid, row, col):
    empty_row, empty_col = find_empty_tile(grid)
    if abs(empty_row - row) + abs(empty_col - col) == 1:
        grid[empty_row][empty_col], grid[row][col] = grid[row][col], grid[empty_row][empty_col]

# Check if the puzzle is solved
def is_solved(grid):
    expected = list(range(1, GRID_SIZE ** 2)) + [None]
    flat_grid = [cell for row in grid for cell in row]
    return flat_grid == expected

# Main game loop
def main():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Sliding Puzzle")
    clock = pygame.time.Clock()
    grid = create_grid()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                row, col = mouse_y // TILE_SIZE, mouse_x // TILE_SIZE
                move_tile(grid, row, col)

        # Draw everything
        draw_grid(screen, grid)
        pygame.display.flip()

        # Check for win
        if is_solved(grid):
            print("You solved the puzzle!")
            pygame.time.delay(2000)
            running = False

        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
