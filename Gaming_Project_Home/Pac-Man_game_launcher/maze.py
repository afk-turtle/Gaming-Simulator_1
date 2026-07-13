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
from tempsettings import WIDTH, HEIGHT, TILE_SIZE, BLUE, YELLOW, RED

class Maze:

    def __init__(self):

        # Stores every wall in the maze
        self.walls = []

        # Stores ghost house walls separately
        self.ghost_house = []

        # Stores every pellet inside the maze, Pac-Man will remove the pellets when collected, the maze only generates/stores pellets
        self.pellets = []

        # Build maze structures
        self.create_border() # Wall border
        self.create_ghost_house() # Ghost house
        self.create_pellets() # Pellet creation in maze

    def create_border(self):

        # Create the top and bottom border walls.
        for x in range (0, WIDTH, TILE_SIZE):

            # Top wall
            self.walls.append(
                pygame.Rect(x, 0, TILE_SIZE, TILE_SIZE)
            )

            # Bottom wall
            self.walls.append(
                pygame.Rect(x, HEIGHT - TILE_SIZE, TILE_SIZE, TILE_SIZE)
            )
        # Why written like this? Notice that range(0, WIDTH, TILE_SIZE) moves across 
        # the screen 20 pixels at a time, creating one wall tile for each position.

        # Create the left and right border walls
        for y in range(TILE_SIZE, HEIGHT - TILE_SIZE, TILE_SIZE):

            # Left wall
            self.walls.append(
                pygame.Rect(0, y, TILE_SIZE, TILE_SIZE)
            )

            # Right wall
            self.walls.append(
                pygame.Rect(WIDTH - TILE_SIZE, y, TILE_SIZE, TILE_SIZE)
            )

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

        # Checks normal maze walls.
        for wall in self.walls:

            if object_rect.colliderect(wall):
                return True
            
        # Checks ghost house walls
        for wall in self.ghost_house:
            if object_rect.colliderect(wall):
                return True
            
        return False


    # Draws every maze object
    def draw(self, screen):

        # Draw maze walls
        for wall in self.walls:
            pygame.draw.rect(screen, BLUE, wall)

        # Draw ghost house
        for wall in self.ghost_house:
            pygame.draw.rect(screen, YELLOW, wall)

        # Draw pellets
        for pellet in self.pellets:
            pygame.draw.circle(screen, RED, pellet.center, 3) # pygame.draw.circle() requires this format -> pygame.draw.circle(screen, color, center_position, radius)


