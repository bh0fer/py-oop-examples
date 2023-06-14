from player import Player
from human import HumanPlayer
from bot import ComputerPlayer
from copy import deepcopy
class TicTacToe():
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.players: list[Player] = []

    def print_board(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    print('.', end=' ')
                else:
                    print(cell, end=' ')
            print()

    def played_cells(self):
        count = 0
        for row in self.board:
            for cell in row:
                if cell is not None:
                    count += 1
        return count

    def get_winner(self):
        played = self.played_cells()
        if played < 5:
            return None
        board = self.board

        for i in range(3):
            # gleiche Zeile?
            if board[i][0] is not None \
               and board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
            # gleiche Spalte?
            if board[i][0] is not None \
               and board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]
        # diagonal?
        if board[1][1] is not None \
           and board[0][2] == board[1][1] == board[2][0] or \
           board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]

        if played == 9:
            return 'tie'

    def has_winner(self):
        return self.get_winner() is not None

    def game_over(self):
        winner = self.get_winner()
        return winner is not None

    def print_winner(self):
        winner = self.get_winner()
        if winner == 'tie':
            print('Unentschieden!')
        else:
            print('\nPlayer', winner, 'gewinnt :)\n')


    def play(self):
        # Board konfigurieren
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        # Spieler:innen vorbereiten
        self.players.clear()
        self.players.append(ComputerPlayer('X'))
        self.players.append(ComputerPlayer('O'))

        current = 0
        while not self.game_over():
            self.print_board()
            player = self.players[current]
            print(player.token, ' am Zug')
            [move_x, move_y] = player.get_move(deepcopy(self.board))
            if self.board[move_y][move_x] is None:
                self.board[move_y][move_x] = player.token
            else:
                raise Exception('invalid input')
            current = (current + 1) % 2

        self.print_board()
        self.print_winner()


game = TicTacToe()
x_wins = 0
for i in range(100):
    game.play()
    if game.get_winner() == 'X':
        x_wins += 1

print('x gewinnt', x_wins)
