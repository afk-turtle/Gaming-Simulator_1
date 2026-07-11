# This python file controls the game state

class GameManager:

    def __init__(self):
        self.score = 0 # Game starts at score 0
        self.game_over = False # This game_over, win and later on grow = False are all examples of State managment. A SWE concept about state machines.
        self.win = False # When game starts, the player has not won yet.

    def check_win(self):

        if self.score >= 1000:
            self.win = True
            self.game_over = True

    