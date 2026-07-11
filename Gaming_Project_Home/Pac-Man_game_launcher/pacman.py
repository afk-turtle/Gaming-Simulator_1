# This file contains everything related to the Pac-Man player
# Since the Snake class is already working, the simplest way to begin is to make a PacMan class that has the same basic structure.

import pygame
from tempsettings import SPEED

class PacMan:

    # Create a new Pac-Man object.
    def __init__(self):

        # Starting position of Pac-Man.
        self.rect = pygame.Rect(100, 100, 20, 20)

        # Starting movement direction.
        self.direction = "RIGHT"

    # Updates Pac-Man's position.
    def move(self):

        if self.direction == "UP":
            self.rect.y -= SPEED

        if self.direction == "DOWN":
            self.rect.y += SPEED

        if self.direction == "RIGHT":
            self.rect.x += SPEED

        if self.direction == "LEFT":
            self.rect.x -= SPEED

    # Changes Pac-Man's movement direction
    def change_direction(self, new_direction):

        self.direction = new_direction

# /////////////////////////////////////////////////////////
# This class gives

# ✅ Constructor (__init__)
# ✅ Position (self.rect)
# ✅ Direction (self.direction)
# ✅ Movement (move())
# ✅ Direction changes (change_direction())

# How it compares to your Snake class
# The biggest difference is:

# For Snake, 

# self.body = [
#    pygame.Rect(100,100,20,20)
# ]

# because the snake has multiple body segments.

# For Pac-Man,

# self.rect = pygame.Rect(100,100,20,20)

# Because Pac-Man is just one object.