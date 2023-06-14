

class Shape():
    def __init__(self, name, size):
        self.size = size
        self.name = name

    def area(self):
        raise NotImplementedError('This method is not implemented')
    
    def volume_prisma(self, height):
        return self.area() * height

    def ascii(self):
        raise NotImplementedError('This method is not implemented')

    def draw(self):
        print(self.ascii())

    def __str__(self):
        return f'{self.name}: {self.size}, Fläche: {self.area()}'