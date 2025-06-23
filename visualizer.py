import pygame

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

def draw_array(array, colors):
    screen.fill(WHITE)
    bar_width = WIDTH // len(array)
    for i, height in enumerate(array):
        x = i * bar_width
        y = HEIGHT - height
        pygame.draw.rect(screen, colors[i], (x, y, bar_width, height))
    pygame.display.flip()

def display_menu():
    screen.fill(WHITE)
    font = pygame.font.SysFont("Arial", 28)
    options = [
        "1. Bubble Sort",
        "2. Selection Sort",
        "3. Insertion Sort",
        "4. Merge Sort",
        "5. Quick Sort",
        "Press 'R' to reset the array",
        "Press 'Q' to quit"
    ]
    for i, option in enumerate(options):
        text = font.render(option, True, BLACK)
        screen.blit(text, (WIDTH // 4, 50 + i * 40))
    pygame.display.flip()
