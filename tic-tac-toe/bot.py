from player import Player
from random import randint

class ComputerPlayer(Player):
    def __init__(self, token):
        super().__init__(token)

    def get_move(self, board):
        valid = False
        row = 0
        col = 0
        while not valid:
            row = randint(0, 2)
            col = randint(0, 2)
            valid = board[row][col] is None

        return [col, row]