from math import *
class Parallelogramm:
    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle

    def area(self):
        from math import sin
        return self.a * self.b * sin(radians(self.angle))



class Rectangle(Parallelogramm):
    def __init__(self, a, b):
        Parallelogramm.__init__(self, a, b)

    def area(self):
        return self.a * self.b


class Rhombus(Parallelogramm):
    def __init__(self, a, angle):
        self.a = a
        self.angle = angle

    def area(self):
        return (self.a ** 2) * sin(radians(self.angle))


class Square(Rhombus):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a 

p1 = Parallelogramm(10, 10, 90)
print(p1.area())