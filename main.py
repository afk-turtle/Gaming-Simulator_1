import pygame
import sys
import random

pygame.init()

Width = 600
Height = 600

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake_Eater_Game")


clock = pygame.time.Clock()

# Create the snake only once
# This is the list data structure[], like arrays but with the difference of list being highly flexible in python.
# Lists are dynamically resized and can hold mixed data types.
### Snake structure ###
# snake[0] = Head
# snake[1:] = Body + Tail
#
# Body segments are added when food is eaten.
snake = [
pygame.Rect(100, 100, 20, 20)
]

# Food creation
food = pygame.Rect(300, 300, 20, 20) # 300, 300 is the center for the first food piece

score = 0
font = pygame.font.Font(None, 30) # This prints score to the game window instead of just terminal, The 30 font size and also parameter value, More specifcally, an arguement passed to the function. 
speed = 20
game_over = False # This game_over, win and later on grow = False are all examples of State managment. A SWE concept about state machines.
win = False

dx = 0 # Horizontal Movement
dy = 0 # Vertical Movement
grow = False # Controls wheather snake grows after eating food.

running = True

# This is called a game loop, in which it's a programming pattern that takes input, update game, render graphics, then repeat.
while running and not game_over:

# Start of event loop
    for event in pygame.event.get(): # (Keyboard input)
        if event.type == pygame.QUIT:
            running = False
        
        # Listen for arrowkeys for movement 
        if event.type == pygame.KEYDOWN:

            # so x-axis is the same with math and computer graphics but the y direction is opposite.
            # In computer graphics (0,0) starts at the top left corner and thus increases in size with increasing y-axis and x-axis.
            # Resulting in y-axis increasing but the direction is going down on the computer graphics coordinate plane.
            # Increasing y means moving downward.

            if event.key == pygame.K_UP:
                dx = 0
                dy = -speed
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = speed
            elif event.key == pygame.K_LEFT:
                dx = -speed
                dy = 0 
            elif event.key == pygame.K_RIGHT:
                dx = speed
                dy = 0 

    # Create a new head position
    new_head = snake[0].copy()

    # Move the new head, movement direction
    new_head.x += dx
    new_head.y += dy

    # Add new head to the front of the snake
    snake.insert(0, new_head)

    # Remove tail unless food was eaten
    if not grow:
        snake.pop()

    # Reset growth
    grow = False

    # Check if snake hits Wall
    head = snake [0]
    if head.left < 0 or head.right > Width: 
        game_over = True
    if head.top < 0 or head.bottom > Height:
        game_over = True

    # Check if snake eats itself, the program checks if object A crossed over with object B.
    # This is a basic collision algorithm, detects when two shapes overlap
    for block in snake[1:]:
        if head.colliderect(block):
            game_over = True

    # If statement to check if the snake ate the food.
    if snake[0].colliderect(food):
        score += 100
        print("Score:", score) # Techincally Debugging and Testing, since it checks variable values, logic errors, and behavior. 
                               # Usage of logging systems, unit testing, and debuggers was not necessarily 
        
        # Grow snake
        grow = True
        
         # Move food to a new location (Creation of food generation algorithm)
         # Usage of random number generation. 
        food.x = random.randrange(0, Width - 20, 20)
        food.y = random.randrange(0, Height - 20, 20)

    # Win condition
    # Usage of Boolean logic explicitly here (AND, OR, NOT, conditional execution, are used here and sprinkled elsewhere in program).
    if score >= 1000:
        game_over = True
        win = True


    # This is the drawing Section ---
    # This is Graphics programming with pygame.draw.rect(), this renders objects, colors, frames, and screen refresing in the drawing Section.
    screen.fill ((0, 0, 0)) # Black background
    for block in snake: 
        pygame.draw.rect(screen, (0,255,0), block)
    pygame.draw.rect(screen, (255,165,0), food) # Draw food. The numbers (255, 165, 0) are the RGB values for the color orange.

    # Display game over
    if game_over: 
        if win:
            win_text = font.render("YOU WIN!", True, (255,255,255))
            screen.blit(win_text, ((Width - win_text.get_width()) // 2, 250))
            
        else:
            end_text = font.render("Game Over!", True, (255,255,255))
            screen.blit(end_text, ((Width - end_text.get_width()) // 2, 250))

    # Create and display score text
    score_text = font.render("Score: " + str(score), True, (255,255,255)) # 255,255,255 is the RGB color for white
    screen.blit(score_text, ((Width - score_text.get_width()) // 2, 10))

    pygame.display.flip()

    clock.tick(10)


# This is Error Handling / Program Termination by cleaning resources, and proper program shutdown.
pygame.quit()
sys.exit()


