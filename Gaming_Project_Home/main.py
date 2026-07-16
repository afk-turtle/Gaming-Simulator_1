# main.py
#
# Entry point for the entire game application.
# GameManager controls:
# - pygame setup
# - window creation
# - game loop
# - game states
# - switching between Snake and Pac-Man


from game_manager import GameManager


def main():

    # Create the main game controller
    game = GameManager()

    # Start the application
    game.run()


# Runs only when this file is executed directly
if __name__ == "__main__":
    main()