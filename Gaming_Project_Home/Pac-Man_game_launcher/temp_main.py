# temporary main.py file to just show map generation 
# Creation of initial progress checker

# The actual main.py file will be outside of Pac-Man_game_launcher and in the Gaming_Project_Home

import pygame 
import sys
from maze import Maze
from tempsettings import WIDTH, HEIGHT
from pacman import PacMan
from ghost import Ghost

pygame.init()

# Create game window

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Maze Test")

clock = pygame.time.Clock()

# Create Maze object
maze = Maze(1)
pacman = PacMan()
ghosts = [Ghost(260,220), Ghost(280,220), Ghost(300,220), Ghost(320,220)]

running = True

while running: 

    # Event handling
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                pacman.change_direction("UP")

            elif event.key == pygame.K_DOWN:
                pacman.change_direction("DOWN")

            elif event.key == pygame.K_LEFT:
                pacman.change_direction("LEFT")

            elif event.key == pygame.K_RIGHT:
                pacman.change_direction("RIGHT")

        if event.type == pygame.QUIT:
            running = False
    
    # Update pacman movement
    pacman.move(maze)

    # Pacman eats pellets
    pacman.eat_pellets(maze)

    # The 4 Ghosts movement
    for ghost in ghosts:
        ghost.move(maze)

    #///////////////////////////////////
    # Draw background
    screen.fill ((0,0,0))

    # Draw maze objects
    maze.draw(screen)

    # Draw pacman
    pacman.draw(screen)

    # Draw the 4 ghosts
    for ghost in ghosts:
        ghost.draw(screen)

    # Update display
    pygame.display.flip()

    # Limit FPS
    clock.tick(20)

pygame.quit()
sys.exit()

# PAC-MAN MAZE SYSTEM STATUS

# Completed:

# 1. Grid System, includes game window 600 x 600 pixels, Tile Size -> 20 x 20 pixels, and map using 30 x 30 tiles
# 2. Border wall Generation, includes wall around entire game window, prevent ghost/pacman from leaving screen, stores walls inside the maze
# 3. Ghost house Generation, includes centered ghost area, ghost house stored sepeartely from normal maze walls
# 4. Pellet Generation, includes creation of pellets throughout maze, stores pellets in pellet list, in the future, Pac-Man will remove pellets when collected.
# 5. Maze Collusion System, includes Maze handling collusion check by using is_wall(). Pac-Man does not directly check every wall, 
#    this keeps seperation and ease dynamic map generation later.