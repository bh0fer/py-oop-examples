class Player():
    def __init__(self, token):
        self.token = token

    def get_move(self, board):
        raise NotImplementedError('Not implemented')