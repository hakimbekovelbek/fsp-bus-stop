from math import sin, radians as rad 
class Parallelogram:
    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle
    
    def area(self):
        return self.a * self.b*sin(rad(self.angle))
        




class Rhombus(Parallelogram):
    def __init__(self, a):
        self.a = a

class Square(Rhombus):
    pass

class Rectangle(Parallelogram):
    def __init__(self, a, b):
        Parallelogram.__init__(self, a, b)


# rhombus = Rhombus(5)


p1 = Parallelogram(10, 10, 90)

print(p1.area())