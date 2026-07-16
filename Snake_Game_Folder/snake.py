# This python file contains everything about the snake.
# Do this by creating a snake class

import pygame
from settings_snake import SPEED

class Snake: 
    
    # def → defines a function (called a method when it's inside a class).
    # In Python, __init__ is a special method used to initialize a newly created object's attributes. 
    # __init__  acts as a constructor, meaning it runs automatically every single time you create a new instance of a class
    #  Python automatically uses its default __new__ method to create the blank object container before your __init__ method fills it with data.
    # The __init__ method is like a setup wizard that automatically runs to fill a brand-new object with its starting traits (like giving a new character name and health stats).
    # The __init__ method ultimately comes from a hidden master class in Python called object.

    # Starting value for every new Snake
    def __init__(self):

        # Snake starting with one body segment
        self.body = [ 
            pygame.Rect(100,100,20,20)
        ]

        # The snake doesn't start moving untill user moves
        self.direction = "NONE"

        # The snake has not grown yet
        self.grow = False

    def move(self):

        new_head = self.body[0].copy()

        if self.direction == "UP":
            new_head.y = new_head.y - SPEED

        elif self.direction == "DOWN":
            new_head.y = new_head.y + SPEED

        elif self.direction == "LEFT":
            new_head.x -= SPEED     # Can do this because it's a shortcut, '-=' Python treats it as a shortcut for updating the current value.

        elif self.direction == "RIGHT":
            new_head.x += SPEED     # += and -= are shortcuts that update a variable using its current value, instead of replacing the value completely.

        self.body.insert(0,new_head)

        if not self.grow:
            self.body.pop()

        self.grow = False

    def change_direction(self, new_direction):
        
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
            
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
            
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    