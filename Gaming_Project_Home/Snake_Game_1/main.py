# In this file, main.py becomes is the coordinator with the creation of the classes
# It creates the game objects, handles the game loop, processes input, updates game state, and renders everything to the screen.
import pygame
import sys

# Import game components (separation of responsibilities)
# Each class manages its own behavior:
# Snake -> player movement and body
# Food -> food placement
# GameManager -> score and game state
# Settings -> constant values
from game_manager import GameManager
from snake import Snake
from food import Food
from settings import WIDTH, HEIGHT

pygame.init()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake_Eater_Game")

# Controls the game speed and frame timing
clock = pygame.time.Clock()

# Creates font object used for displaying text on screen
font = pygame.font.Font(None, 30)

# Create objects: creates instances of each class that work together to form the game system.
snake = Snake()
food = Food()
game = GameManager()

# Controls whether the main game loop continues running
running = True

# Main Game Loop:
# Repeatedly handles input, updates game logic, and redraws the screen.
while running and not game.game_over:

    # input handling by user
    # Checks for player actions such as keyboard presses or closing the window.
    for event in pygame.event.get():

        # Allows the player to close the game window safely.
        if event.type == pygame.QUIT:
            running = False

        # Detects keyboard input and sends the direction request to the Snake object.
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                snake.change_direction("UP")

            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")

            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")

            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

     # ---------------- GAME UPDATE ----------------
    # Updates the snake position based on the current direction.
    snake.move()

    # Check if the snake leaves the game window (wall check)
    head = snake.body[0]

    if (
        head.left < 0 or
        head.right > WIDTH or
        head.top < 0 or
        head.bottom > HEIGHT
    ):
        game.game_over = True

    # Check if the snake head collides with it's body
    for block in snake.body[1:]:                          # snake.body[1:] = body and tail ///  snake.body[0] = Head 
        if head.colliderect(block):                      # Thus, this 'for' loop features a game over for Head touching every other body segment.
            game.game_over = True
    

     # Collusion detection, in other words, checks if the snake head overlaps/touches the food object.
    if snake.body[0].colliderect(food.rect):
        game.score += 100 # Score increase when snake eats/touches food
        snake.grow = True # Snake grows
        food.relocate() # New food generates

     # Check win condition
    game.check_win()

     # Drawing of the screen
    screen.fill((0,0,0))

     # Draw snake
    for block in snake.body:
        pygame.draw.rect(screen, (0,255,0), block)
        
     # Draw food
    pygame.draw.rect(screen,(255,165,0), food.rect)

    # Converts the current score into display text for the game window
    score_text = font.render("Score: " + str(game.score), True, (255,255,255))

    # Positions and draws the score text at the top center of the game window
    screen.blit(
        score_text, ((WIDTH - score_text.get_width()) // 2, 10)
    )

    # Updates the display so the newly drawn frame appears.
    pygame.display.flip()

    # Limits the game loop to 10 frames per second.
    clock.tick(10)

# Properly shuts down Pygame and exits the program.
pygame.quit()
sys.exit()
    
