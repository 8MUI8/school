import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
segment_margin = 3

# Set the dimensions of the game window
display_width = 800
display_height = 600

# Set the initial speed of the snake
snake_speed = 15

# Create the game window
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Function to draw the snake
def draw_snake(snake_segments):
    for segment in snake_segments:
        pygame.draw.rect(game_display, GREEN, [segment[0], segment[1], segment_width, segment_height])

# Function to generate a random position for the food
def generate_food_position(snake_segments):
    while True:
        food_x = round(random.randrange(0, display_width - segment_width) / 15.0) * 15.0
        food_y = round(random.randrange(0, display_height - segment_height) / 15.0) * 15.0
        if (food_x, food_y) not in snake_segments:
            return food_x, food_y

# Main game loop
def game_loop():
    game_over = False
    game_exit = False

    # Initialize the snake's initial position
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snake_segments = []
    snake_length = 1

    # Generate initial food position
    food_x, food_y = generate_food_position(snake_segments)

    while not game_exit:
        while game_over:
            # Game over screen
            game_display.fill(BLACK)
            font = pygame.font.SysFont(None, 25)
            text = font.render("Game Over! Press Q to quit or C to play again", True, WHITE)
            game_display.blit(text, (display_width / 2 - text.get_width() / 2, display_height / 2 - text.get_height() / 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_exit = True
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -segment_width - segment_margin
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = segment_width + segment_margin
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -segment_height - segment_margin
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = segment_height + segment_margin
                    lead_x_change = 0

        # Check for collision with boundaries or self
        if (
            lead_x >= display_width
            or lead_x < 0
            or lead_y >= display_height
            or lead_y < 0
            or (lead_x, lead_y) in snake_segments[1:]
        ):
            game_over = True

        # Update snake's position
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Clear the game window
        game_display.fill(BLACK)

        # Draw the food
        pygame.draw.rect(game_display, RED, [food_x, food_y, segment_width, segment_height])

        # Update snake_segments and check for food collision
        snake_segments.append((lead_x, lead_y))
        if len(snake_segments) > snake_length:
            del snake_segments[0]

        for segment in snake_segments[:-1]:
            if segment == (lead_x, lead_y):
                game_over = True

        # Draw the snake
        draw_snake(snake_segments)

        # Update the game display
        pygame.display.update()

        # Check for food collision
        if (lead_x, lead_y) == (food_x, food_y):
            snake_length += 1
            food_x, food_y = generate_food_position(snake_segments)

        # Set the game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
game_loop()
