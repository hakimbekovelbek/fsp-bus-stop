class Geometry:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def sqare(self):
        a = self.side_a ** 2
        b = (self.side_a + self.side_b) * 2

        print('it is square - ', a)
        print('it is perimetr - ', b)

        return
    def rectangle(self):
        a = self.side_a * self.side_b
        c = (self.side_a + self.side_b) * 2

        print('it is square - ', a)
        print('it is perimetr - ', c)

        return
f = Geometry(4, 5)  
print(f.sqare())
print(f.rectangle())

