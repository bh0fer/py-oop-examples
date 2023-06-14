'''
board= [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
'''
from square import Square
from triangle import Triangle

class Paper():
    def __init__(self, width, height):
        self.board = [
            [' ' for x in range(width)] for y in range(height)
        ]

    def draw(self):
        lines = [''.join(line) for line in self.board]
        print('\n'.join(lines))

    def add(self, shape, x, y):
        ascii = shape.ascii()
        shape_lines = ascii.split('\n')
        pos_y = y
        for line in shape_lines:
            pos_x = x
            for chr in line:
                valid_x = pos_x < len(self.board[0]) and pos_x >= 0
                valid_y = pos_y < len(self.board) and pos_y >= 0
                if valid_x and valid_y and chr != ' ':
                    self.board[pos_y][pos_x] = chr
                pos_x += 1
            pos_y += 1



paper = Paper(20, 20)
s1 = Square(5)
paper.add(s1, 4, 4)
paper.draw()
paper.add(Square(20), 0, 0)
paper.add(Triangle(8), 10, 10)

paper.draw()