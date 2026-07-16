import pygame
from settings import SPEED

class Ghost:

    def __init__(self, x, y):

        # Starting position
        self.rect = pygame.Rect(
            x,
            y,
            20,
            20
        )

        # Starting direction
        self.direction = "LEFT"


    def move(self, maze):

        old_position = self.rect.copy()


        if self.direction == "UP":
            self.rect.y -= SPEED

        elif self.direction == "DOWN":
            self.rect.y += SPEED

        elif self.direction == "LEFT":
            self.rect.x -= SPEED

        elif self.direction == "RIGHT":
            self.rect.x += SPEED


        # Collision with walls
        if maze.is_wall(self.rect):

            # Undo movement
            self.rect = old_position

            # Change direction randomly later
            self.change_direction()


    def change_direction(self):

        directions = [
            "UP",
            "DOWN",
            "LEFT",
            "RIGHT"
        ]

        import random

        self.direction = random.choice(directions)


    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255,0,0),
            self.rect.center,
            10
        )