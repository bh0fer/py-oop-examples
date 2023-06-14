from shape import Shape

class Square(Shape):
    def __init__(self, size):
        super().__init__('Square', size)
        self.name = 'Quadrat'

    def ascii(self):
        if self.size == 0:
            return '.'
        elif self.size == 1:
            return '▢'
        
        buff = []
        top = '+' + '―' * (self.size - 2) + '+'
        middle = '|' + ' ' * (self.size - 2) + '|'
        buff.append(top)
        for _ in range(self.size - 2):
            buff.append(middle)
        buff.append(top)
        return '\n'.join(buff)

    def area(self):
        return self.size ** 2


s1 = Square(0) # s1 ist eine Instanz von Square
s2 = Square(1)
s2.name = 'Quadrat Grösse Eins'
s3 = Square(10)

for s in [s1,s2,s3]:
    print(s)
    s.draw()
    print('------------------------------------')