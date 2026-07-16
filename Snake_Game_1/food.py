# Python file containing food info

import pygame
import random
from settings_snake import WIDTH, HEIGHT

class Food:

    def __init__(self): 
        self.rect = pygame.Rect(300,300,20,20)

    def relocate(self):

        self.rect.x = random.randrange(0, WIDTH -20, 20)
        self.rect.y = random.randrange(0, HEIGHT -20, 20)
        