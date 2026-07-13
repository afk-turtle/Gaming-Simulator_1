# Creation of custom maze that: 
# Uses a 30 × 30 grid (This is because, If each tile is 20 × 20 pixels, then 600 / 20 = 30)
# Thus, this becomes, 30 columns, 30 rows
# (Not the original 28 columns and 31 rows game due to different screen resolution of this system, which is 600 x 600 pixels currently)

# The Pac-Man game keeps the wraparound tunnel on the left and right, meaning,
# when moving Pac-Man off one side of the screen, he instantly reappears on the opposite side.

# Has a central ghost house
# Has pellets throughout the maze
# Has four power pellets in the corners

# The first thing to write is the border walls for the window screen
# This will ensure that the Pac-Man/ghost do not go off screen.

import pygame
import random
from tempsettings import WIDTH, HEIGHT, TILE_SIZE, BLUE, YELLOW, RED

class Maze:

    def __init__(self, level):
       
       self.level = level # Stores Pac-Man level
       
       # Store maze objects
       self.border_walls = []
       self.interior_walls = []
       self.ghost_house = []
       self.pellets = []

       # Builds the correct maze based on the current level.
       if self.level == 1:
           self.create_static_maze()

       elif self.level == 2:
           self.create_dynamic_maze()
        

    # Level 1:
    def create_static_maze(self):
        
        # Builds the fixed Level 1 maze:
        self.create_border()
        self.create_ghost_house()
        self.create_static_walls()
        self.create_pellets()

    def create_dynamic_maze(self):

        # Builds the procedural Level 2 maze:
        self.create_border()
        self.create_ghost_house()
        self.create_dynamic_walls()
        self.create_pellets()

    def create_border(self):
    # Create the top and bottom border walls
        for x in range(0, WIDTH, TILE_SIZE):

        # Top wall
            self.border_walls.append(
            pygame.Rect(
                x,
                0,
                TILE_SIZE,
                TILE_SIZE
            )
        )

        # Bottom wall
            self.border_walls.append(
            pygame.Rect(
                x,
                HEIGHT - TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            )
        )
            # Create the left and right border walls
        for y in range(TILE_SIZE, HEIGHT - TILE_SIZE, TILE_SIZE):

            # Left wall
            self.border_walls.append(
                pygame.Rect(0, y, TILE_SIZE, TILE_SIZE)
            )

            # Right wall
            self.border_walls.append(
                pygame.Rect(WIDTH - TILE_SIZE, y, TILE_SIZE, TILE_SIZE)
            )

    # Helper method #1 helps create horizontal wall
    def add_horizontal_wall(self, start_x, start_y, length):

    # Creates one horizontal wall made of multiple tiles.
        for i in range(length):

            self.interior_walls.append(
            pygame.Rect(
                start_x + (i * TILE_SIZE),
                start_y,
                TILE_SIZE,
                TILE_SIZE
            )
        )
            
    # Helper method 2: Horizontal wall
    def add_vertical_wall(self, start_x, start_y, length):

    # Creates one vertical wall made of multiple tiles.
        for i in range(length):

            self.interior_walls.append(
            pygame.Rect(
                start_x,
                start_y + (i * TILE_SIZE),
                TILE_SIZE,
                TILE_SIZE
            )
        )
        
    def create_static_walls(self):
           # ---------------- Top Section ----------------

        self.add_horizontal_wall(80, 80, 6)
        self.add_horizontal_wall(400, 80, 6)

        self.add_vertical_wall(80, 80, 4)
        self.add_vertical_wall(500, 80, 4)

    # ---------------- Upper Middle ----------------

        self.add_horizontal_wall(180, 180, 4)
        self.add_horizontal_wall(340, 180, 4)

    # ---------------- Left Side ----------------

        self.add_vertical_wall(140, 260, 6)

    # ---------------- Right Side ----------------

        self.add_vertical_wall(440, 260, 6)

    # ---------------- Bottom ----------------

        self.add_horizontal_wall(80, 460, 6)
        self.add_horizontal_wall(400, 460, 6)

        self.add_vertical_wall(80, 400, 4)
        self.add_vertical_wall(500, 400, 4)



    def create_dynamic_walls(self):

        # Number of wall segments to generate
        wall_count = 12

    # Define ghost house area so walls do not spawn inside it.
        house_width = TILE_SIZE * 8
        house_height = TILE_SIZE * 4

        house_x = (WIDTH - house_width) // 2
        house_y = (HEIGHT - house_height) // 2


        ghost_area = pygame.Rect(
            house_x,
            house_y,
            house_width,
            house_height
    )

        for i in range(wall_count):

            # Randomly choose horizontal or vertical wall
            direction = random.choice(["horizontal", "vertical"])

         # Random starting position
            x = random.randrange(
                TILE_SIZE,
                WIDTH - TILE_SIZE,
                TILE_SIZE
        )

            y = random.randrange(
                TILE_SIZE,
                HEIGHT - TILE_SIZE,
                TILE_SIZE
        )

            length = random.randint(3, 6)

        # Create horizontal wall segment
            if direction == "horizontal":
                wall = pygame.Rect(
                    x,
                    y,
                    TILE_SIZE * length,
                    TILE_SIZE
            )

        # Create vertical wall segment
            else:
                wall = pygame.Rect(
                    x,
                    y,
                    TILE_SIZE,
                    TILE_SIZE * length
            )

        # Prevent walls from spawning inside ghost house
            if wall.colliderect(ghost_area):
                continue

        # Prevent touching border walls
        # ------------------------------
            invalid_border = False

            for border in self.border_walls:

                if wall.colliderect(border):
                    invalid_border = True
                    break

            if invalid_border:
                continue

        # Prevent walls from overlapping existing walls
            overlap = False

            for existing_wall in self.interior_walls:

                if wall.colliderect(existing_wall):
                    overlap = True
                    break


            # Add wall only if it passes all checks
            if overlap:
                continue
            
            # Add valid wall
            self.interior_walls.append(wall)


        # Notice the loop starts at TILE_SIZE instead of 0. 
        # That's because the four corner tiles were already created by the top and bottom loops, so this avoids adding duplicate corner walls.
        # This completes the borders.
        # When calling upon -> maze.draw(screen) -> the draw() method loops through self.walls and draws every border tile.
        # * //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// *
    
    def create_ghost_house(self):

        # Center the ghost house in the middle of the screen.
        house_width = TILE_SIZE * 8
        house_height = TILE_SIZE * 4

        start_x = (WIDTH - house_width) // 2 # usage of '//' because this returns an integer, the usage of single '/' returns a float
        start_y = (HEIGHT - house_height) // 2

        # Top wall of the ghost house
        self.ghost_house.append(
            pygame.Rect(
                start_x,
                start_y,
                house_width,
                TILE_SIZE
            )
        )

        # Bottom wall of ghost house
        self.ghost_house.append(
            pygame.Rect(
                start_x,
                start_y + house_height - TILE_SIZE,
                house_width,
                TILE_SIZE
            )
        )

        # Left wall of ghost house
        self.ghost_house.append(
            pygame.Rect(
                start_x,
                start_y,
                TILE_SIZE,
                house_height
            )
        )

        # Right wall of ghost house
        self.ghost_house.append(
            pygame.Rect(
                start_x + house_width - TILE_SIZE,
                start_y,
                TILE_SIZE,
                house_height
            )
        )

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

    def create_pellets(self):
        # Creates pellets through the maze
        # Pellets cannot spawn inside walls or the ghost house.

         for x in range(TILE_SIZE, WIDTH - TILE_SIZE, TILE_SIZE):

            for y in range(TILE_SIZE, HEIGHT - TILE_SIZE, TILE_SIZE):
                pellet = pygame.Rect(
                    x + TILE_SIZE // 2,
                    y + TILE_SIZE // 2,
                    5,
                    5
                )

                # Check if pellet location is blocked by a wall

                if not self.is_wall(pellet):
                    self.pellets.append(pellet)

    # /////////////////////////
    # new method of is_wall() is created here, checks if an object is touching any maze wall.
    # Maze handles collision checks through is_wall() to keep responsibilities separated. 
    # Similar to GameManager managing game states, Maze owns maze logic while Pac-Man only requests collision information.
    # This prevents Pac-Man from depending on the internal structure of the maze and improves scalability for dynamic map generation.

    def is_wall(self, object_rect):

        # Checks bprder maze walls.
        for wall in self.border_walls:

            if object_rect.colliderect(wall):
                return True
            
        # Checks interior walls.
        for wall in self.interior_walls:
            if object_rect.colliderect(wall):
                return True
            
        # Checks ghost house walls
        for wall in self.ghost_house:
            if object_rect.colliderect(wall):
                return True
            
        return False


    def reset_maze(self):

    # Removes all existing maze objects.
    # Used when switching between levels.

        self.border_walls.clear()

        self.interior_walls.clear()

        self.ghost_house.clear()

        self.pellets.clear()

    # ///////////////////////////////////////////
    # Draws every maze object
    def draw(self, screen):

        # Draw border maze walls
        for wall in self.border_walls:
            pygame.draw.rect(screen, BLUE, wall)

        # Draw interior walls
        for wall in self.interior_walls:
            pygame.draw.rect(screen, BLUE, wall)

        # Draw ghost house
        for wall in self.ghost_house:
            pygame.draw.rect(screen, YELLOW, wall)

        # Draw pellets
        for pellet in self.pellets:
            pygame.draw.circle(screen, RED, pellet.center, 3) # pygame.draw.circle() requires this format -> pygame.draw.circle(screen, color, center_position, radius)


