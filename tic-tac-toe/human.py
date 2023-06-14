from player import Player

class HumanPlayer(Player):
    def __init__(self, token):
        super().__init__(token)

    def get_move(self, board):
        valid = False
        row = 0
        col = 0
        while not valid:
            row = int(input('Zeile: ')) - 1
            col = int(input('Spalte: ')) - 1
            valid = board[row][col] is None

        return [col, row]