board = [
    [None,  'O',  'X'],
    [None,  'O',  'X'],
    [ 'X', None, None]
]

def print_board():
    for row in board:
        for cell in row:
            if cell is None:
                print('.', end=' ')
            else:
                print(cell, end=' ')
        print()

def played_cells():
    count = 0
    for row in board:
        for cell in row:
            if cell is not None:
                count += 1
    return count

def get_winner():
    played = played_cells()
    if played < 5:
        return None
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][2] == board[1][1] == board[2][0] or \
       board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    
    if played == 9:
        return 'tie'

def has_winner():
    return get_winner() is not None

def game_over():
    winner = get_winner()
    return winner is not None

def play(row, col, player):
    if board[row][col] is not None:
        raise ValueError('Feld bereits gespielt')
    board[row][col] = player

def get_next_player():
    played = played_cells()
    if played % 2 == 0:
        return 'X'
    return 'O'

def print_winner():
    winner = get_winner()
    if winner == 'tie':
        print('Unentschieden!')
    else:
        print('\nPlayer', winner, 'gewinnt :)\n')

def player_play(player):
    try:
        print('Player', player, 'is am Zug')
        row = int(input('Zeile: '))
        col = int(input('Spalte: '))
        play(row, col, player)
        return True
    except Exception: # Fängt alle Fehler ab, muss nicht verändert werden. Der Fehler liegt nicht hier...
        return False

def reset():
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

def game_loop():
    while not game_over():
        player = get_next_player()
        print_board()
        while not player_play(player):
            print_board()
            print('\n!! Ungültige Eingabe !!\n')
    print_winner()


action = 'play'
while action != 'quit':
    action = input('Was wollen Sie tun? (play [p] / Spiel verlassen [x]): ')
    if action.strip() in ['p', 'play']:
        reset()
        game_loop()
    else:
        action = 'quit'
        print('Fertig')