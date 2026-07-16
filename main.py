import pygame
import sys

from GameManager.game_manager import GameManager


pygame.init()


# Create window
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake + Pac-Man")


clock = pygame.time.Clock()


# Create the main controller
game_manager = GameManager(screen)


running = True


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        # Send keyboard input to GameManager
        game_manager.handle_events(event)


    # Update current game
    game_manager.update()


    # Draw current game
    game_manager.draw()


    pygame.display.flip()


    clock.tick(20)



pygame.quit()
sys.exit()