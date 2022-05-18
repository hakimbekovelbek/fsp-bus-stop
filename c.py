class Parallelogram:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Square(Parallelogram):
    def __init__(self, a):
        self.a = a
        

class Rectangle(Parallelogram):
    def __init__(self, a, b):
        Parallelogram.__init__(self, a, b)


class Rhombus(Parallelogram):
    def __init__(self, a):
        self.a = a

par = Parallelogram(5, 6)
sqr = Square(4)