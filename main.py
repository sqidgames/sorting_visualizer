import pygame
import random
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from visualizer import draw_array, display_menu, HEIGHT, GREEN
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

def main():
    # Initialize Pygame and create a resizable window
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Sorting Algorithm Visualizer")

    # Initialize Variables
    array_size = 50
    delay = 0.05
    array = [random.randint(10, HEIGHT) for _ in range(array_size)]
    running = True
    selected_algorithm = None

    print("Initializing the program....")

    # Add Sliders and Text Boxes
    size_slider = Slider(screen, 50, 500, 300, 20, min=10, max=200, step=1)
    size_text = TextBox(screen, 400, 490, 120, 40, fontSize=24)
    size_text.setText(f"Size: {array_size}")

    speed_slider = Slider(screen, 50, 550, 300, 20, min=0.01, max=1, step=0.01)
    speed_text = TextBox(screen, 400, 540, 120, 40, fontSize=24)
    speed_text.setText(f"Speed: {delay:.2f}")

    print("Sliders initialized successfully")

    while running:
        screen.fill((255, 255, 255))  # Clear screen with white background
        display_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Listen for slider interactions
            size_slider.listen(event)
            speed_slider.listen(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_algorithm = bubble_sort
                elif event.key == pygame.K_2:
                    selected_algorithm = selection_sort
                elif event.key == pygame.K_3:
                    selected_algorithm = insertion_sort
                elif event.key == pygame.K_4:
                    selected_algorithm = merge_sort
                elif event.key == pygame.K_5:
                    selected_algorithm = quick_sort
                elif event.key == pygame.K_r:
                    array = [random.randint(10, HEIGHT) for _ in range(array_size)]
                    selected_algorithm = None
                elif event.key == pygame.K_q:
                    running = False

        # Update array size from slider
        new_array_size = size_slider.getValue()
        if array_size != new_array_size:
            array_size = new_array_size
            array = [random.randint(10, HEIGHT) for _ in range(array_size)]
            print(f"Array regenerated with size {array_size}")
        size_text.setText(f"Size: {array_size}")

        # Update speed from slider
        delay = speed_slider.getValue()
        speed_text.setText(f"Speed: {delay:.2f}")

        # Run selected algorithm
        if selected_algorithm:
            selected_algorithm(array, draw_array, delay)
            selected_algorithm = None

        # Draw sliders, text boxes, and array
        size_slider.draw()
        size_text.draw()
        speed_slider.draw()
        speed_text.draw()

        draw_array(array, [GREEN] * len(array))
        pygame.display.flip()

        print(f"Size slider value: {size_slider.getValue()}")
        print(f"Speed slider value: {speed_slider.getValue()}")

    pygame.quit()
    print("Program terminated successfully")

if __name__ == "__main__":
    main()
