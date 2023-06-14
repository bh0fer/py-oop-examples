from math import sqrt
from shape import Shape

class Triangle(Shape):
    def __init__(self, size):
        super().__init__('Triangle', size)

    def ascii(self):
        if self.size == 0:
            return '.'
        elif self.size == 1:
            return '△'
        else:
            buff = []
            sz2 = self.size // 2
            for i in range(sz2):
                left = ' ' * (sz2 - i - 1)
                if i == 0:
                    buff.append(left + '^')
                else:
                    buff.append(left + '/' + ' ' * i * 2 + '\\')
            buff.append('―' * self.size)
            return '\n'.join(buff)

    def area(self):
        return sqrt(3) / 4 * self.size ** 2



s1 = Triangle(0) # s1 ist eine Instanz von Square
s2 = Triangle(1)
s3 = Triangle(10)

for s in [s1,s2,s3]:
    print(s)
    s.draw()
    print('------------------------------------')