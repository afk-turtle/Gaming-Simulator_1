import pygame


# Import Snake classes
from Snake_Game_Folder.snake import Snake
from Snake_Game_Folder.food import Food


# Import Pac-Man classes
from PacMan_Game_Folder.pacman import PacMan
from PacMan_Game_Folder.maze import Maze
from PacMan_Game_Folder.ghost import Ghost



class GameManager:


    def __init__(self, screen):

        self.screen = screen


        # Game states
        self.SNAKE = 0
        self.PACMAN = 1
        self.current_game = self.SNAKE


        # ----------------
        # Snake setup
        # ----------------

        self.snake = Snake()

        self.food = Food()

        self.snake_score = 0



        # ----------------
        # Pac-Man setup
        # ----------------

        self.current_level = 1

        self.maze = Maze(self.current_level)

        self.pacman = PacMan()


        self.ghosts = [

            Ghost(260,220),
            Ghost(280,220),
            Ghost(300,220),
            Ghost(320,220)

        ]



    # ============================
    # INPUT HANDLING
    # ============================

    def handle_events(self,event):


        if event.type != pygame.KEYDOWN:
            return



        # Snake controls

        if self.current_game == self.SNAKE:


            if event.key == pygame.K_UP:

                self.snake.change_direction("UP")


            elif event.key == pygame.K_DOWN:

                self.snake.change_direction("DOWN")


            elif event.key == pygame.K_LEFT:

                self.snake.change_direction("LEFT")


            elif event.key == pygame.K_RIGHT:

                self.snake.change_direction("RIGHT")



        # Pac-Man controls

        elif self.current_game == self.PACMAN:


            if event.key == pygame.K_UP:

                self.pacman.change_direction("UP")


            elif event.key == pygame.K_DOWN:

                self.pacman.change_direction("DOWN")


            elif event.key == pygame.K_LEFT:

                self.pacman.change_direction("LEFT")


            elif event.key == pygame.K_RIGHT:

                self.pacman.change_direction("RIGHT")



    # ============================
    # UPDATE
    # ============================

    def update(self):


        # Snake game

        if self.current_game == self.SNAKE:


            self.update_snake()



        # Pac-Man game

        elif self.current_game == self.PACMAN:


            self.update_pacman()



    # ----------------------------
    # Snake Update
    # ----------------------------

    def update_snake(self):


        self.snake.move()



        if self.snake.body[0].colliderect(self.food.rect):

            self.snake_score += 100

            self.snake.grow = True

            self.food.relocate()



        # Example win condition
        if self.snake_score >= 1000:

            self.start_pacman()



    # ----------------------------
    # Pac-Man Update
    # ----------------------------

    def update_pacman(self):


        self.pacman.move(self.maze)


        self.pacman.eat_pellets(self.maze)



        for ghost in self.ghosts:

            ghost.move(self.maze)



        # Level 1 complete

        if self.maze.level_complete():

            if self.current_level == 1:

                self.current_level = 2


                self.maze = Maze(2)

                self.pacman = PacMan()



    # ============================
    # SWITCH GAME
    # ============================

    def start_pacman(self):


        self.current_game = self.PACMAN



    # ============================
    # DRAW
    # ============================

    def draw(self):


        self.screen.fill((0,0,0))



        if self.current_game == self.SNAKE:


            self.draw_snake()



        elif self.current_game == self.PACMAN:


            self.draw_pacman()



    # ----------------------------
    # Draw Snake
    # ----------------------------

    def draw_snake(self):


        for block in self.snake.body:

            pygame.draw.rect(
                self.screen,
                (0,255,0),
                block
            )



        pygame.draw.rect(

            self.screen,
            (255,165,0),
            self.food.rect

        )



    # ----------------------------
    # Draw Pac-Man
    # ----------------------------

    def draw_pacman(self):


        self.maze.draw(self.screen)


        self.pacman.draw(self.screen)



        for ghost in self.ghosts:

            ghost.draw(self.screen)