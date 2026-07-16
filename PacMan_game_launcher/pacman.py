# This file contains everything related to the Pac-Man player
# Since the Snake class is already working, the simplest way to begin is to make a PacMan class that has the same basic structure.

import pygame
from settings import SPEED

class PacMan:

    # Create a new Pac-Man object.
    def __init__(self):

        # Starting position of Pac-Man.
        self.rect = pygame.Rect(100, 100, 20, 20)

        # Starting movement direction.
        self.direction = "RIGHT"

    # Updates Pac-Man's position.
    def move(self, maze):

        old_position = self.rect.copy()

        if self.direction == "UP":
            self.rect.y -= SPEED

        elif self.direction == "DOWN":
            self.rect.y += SPEED

        elif self.direction == "RIGHT":
            self.rect.x += SPEED

        elif self.direction == "LEFT":
            self.rect.x -= SPEED

        # Check collision with maze
        if maze.is_wall(self.rect):

            # Undo movement
            self.rect = old_position

    # Changes Pac-Man's movement direction
    def change_direction(self, new_direction):

        self.direction = new_direction

    def eat_pellets(self, maze):

        for pellet in maze.pellets[:]:

            if self.rect.colliderect(pellet):

                maze.pellets.remove(pellet)

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255,255,0),
            self.rect.center,
            10
        )