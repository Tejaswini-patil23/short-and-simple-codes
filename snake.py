# import pygame
# import random
# import sys

# # Initialize Pygame
# pygame.init()

# # Window size
# WIDTH, HEIGHT = 600, 400
# CELL_SIZE = 20

# # Colors
# WHITE = (255, 255, 255)
# GREEN = (0, 200, 0)
# RED = (200, 0, 0)
# BLACK = (0, 0, 0)

# # Set up display
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("🐍 Snake Game")

# # Clock and font
# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 24)

# # Snake initialization
# snake = [(100, 100), (80, 100), (60, 100)]
# direction = (CELL_SIZE, 0)

# # Food
# def spawn_food():
#     while True:
#         food = (
#             random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
#             random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
#         )
#         if food not in snake:
#             return food

# food = spawn_food()
# score = 0

# # Game loop
# running = True
# while running:
#     screen.fill(BLACK)

#     # Event Handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Key Presses
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
#         direction = (0, -CELL_SIZE)
#     if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
#         direction = (0, CELL_SIZE)
#     if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
#         direction = (-CELL_SIZE, 0)
#     if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
#         direction = (CELL_SIZE, 0)

#     # Move snake
#     new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
#     snake.insert(0, new_head)

#     # Check collision
#     if (
#         new_head[0] < 0 or new_head[0] >= WIDTH or
#         new_head[1] < 0 or new_head[1] >= HEIGHT or
#         new_head in snake[1:]
#     ):
#         print("Game Over! Score:", score)
#         pygame.quit()
#         sys.exit()

#     # Food eaten
#     if new_head == food:
#         score += 1
#         food = spawn_food()
#     else:
#         snake.pop()

#     # Draw snake
#     for segment in snake:
#         pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

#     # Draw food
#     pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

#     # Display score
#     score_text = font.render(f"Score: {score}", True, WHITE)
#     screen.blit(score_text, (10, 10))

#     pygame.display.flip()
#     clock.tick(10)

import pygame
import random
import sys

pygame.init()

# Window size
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
BUTTON_GREEN = (0, 150, 0)
BUTTON_RED = (150, 0, 0)
BUTTON_BLUE = (0, 0, 150)
BUTTON_YELLOW = (200, 200, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
instr_font = pygame.font.SysFont("Arial", 18)

def spawn_food():
    while True:
        food = (
            random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        )
        if food not in snake:
            return food

def game_over_screen(score):
    while True:
        screen.fill(BLACK)
        over_text = font.render("Game Over!", True, RED)
        score_text = font.render(f"Your Score: {score}", True, WHITE)

        play_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 40)
        exit_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 40)

        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 100))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 50))

        pygame.draw.rect(screen, BUTTON_GREEN, play_button)
        pygame.draw.rect(screen, BUTTON_RED, exit_button)

        play_label = font.render("Play Again", True, WHITE)
        exit_label = font.render("Exit", True, WHITE)

        screen.blit(play_label, (play_button.x + 40, play_button.y + 5))
        screen.blit(exit_label, (exit_button.x + 80, exit_button.y + 5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if play_button.collidepoint((mx, my)):
                    return True  # Play again
                elif exit_button.collidepoint((mx, my)):
                    pygame.quit()
                    sys.exit()

def start_screen():
    teleport_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 50, 300, 50)
    crash_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 20, 300, 50)

    while True:
        screen.fill(BLACK)
        title = font.render("Select Game Mode", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 120))

        pygame.draw.rect(screen, BUTTON_GREEN, teleport_button)
        pygame.draw.rect(screen, BUTTON_RED, crash_button)

        teleport_label = font.render("Teleport Through Walls", True, WHITE)
        crash_label = font.render("Crash On Walls", True, WHITE)

        screen.blit(teleport_label, (teleport_button.x + 20, teleport_button.y + 10))
        screen.blit(crash_label, (crash_button.x + 90, crash_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if teleport_button.collidepoint((mx, my)):
                    return True  # teleport_mode = True
                elif crash_button.collidepoint((mx, my)):
                    return False  # teleport_mode = False

def difficulty_screen():
    easy_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 80, 300, 50)
    medium_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 10, 300, 50)
    hard_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 60, 300, 50)

    while True:
        screen.fill(BLACK)
        title = font.render("Select Difficulty", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 140))

        pygame.draw.rect(screen, BUTTON_GREEN, easy_button)
        pygame.draw.rect(screen, BUTTON_BLUE, medium_button)
        pygame.draw.rect(screen, BUTTON_RED, hard_button)

        easy_label = font.render("Easy", True, WHITE)
        medium_label = font.render("Medium", True, WHITE)
        hard_label = font.render("Hard", True, WHITE)

        screen.blit(easy_label, (easy_button.x + 120, easy_button.y + 10))
        screen.blit(medium_label, (medium_button.x + 105, medium_button.y + 10))
        screen.blit(hard_label, (hard_button.x + 120, hard_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if easy_button.collidepoint((mx, my)):
                    return 7   # FPS for Easy
                elif medium_button.collidepoint((mx, my)):
                    return 10  # FPS for Medium
                elif hard_button.collidepoint((mx, my)):
                    return 15  # FPS for Hard

# -------- MAIN PROGRAM --------

# Show start screen and get selected mode
teleport_mode = start_screen()

# Show difficulty screen and get selected speed
fps = difficulty_screen()

# Initial game state
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
food = spawn_food()
score = 0

running = True
while running:
    screen.fill(BLACK)

    # Display mode info and difficulty
    mode_text = "Mode: Teleport through walls" if teleport_mode else "Mode: Crash on walls"
    mode_render = instr_font.render(mode_text, True, WHITE)
    screen.blit(mode_render, (10, HEIGHT - 50))

    diff_text = f"Difficulty FPS: {fps}"
    diff_render = instr_font.render(diff_text, True, WHITE)
    screen.blit(diff_render, (10, HEIGHT - 30))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)

    # Move snake head
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Handle teleport mode
    if teleport_mode:
        new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)
    else:
        # If crash mode and snake hits wall, game over
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT
        ):
            play_again = game_over_screen(score)
            if play_again:
                snake = [(100, 100), (80, 100), (60, 100)]
                direction = (CELL_SIZE, 0)
                food = spawn_food()
                score = 0
                teleport_mode = start_screen()
                fps = difficulty_screen()
                continue
            else:
                pygame.quit()
                sys.exit()

    snake.insert(0, new_head)

    # Check self collision (both modes)
    if new_head in snake[1:]:
        play_again = game_over_screen(score)
        if play_again:
            snake = [(100, 100), (80, 100), (60, 100)]
            direction = (CELL_SIZE, 0)
            food = spawn_food()
            score = 0
            teleport_mode = start_screen()
            fps = difficulty_screen()
            continue
        else:
            pygame.quit()
            sys.exit()

    # Check food eaten
    if new_head == food:
        score += 1
        food = spawn_food()
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
