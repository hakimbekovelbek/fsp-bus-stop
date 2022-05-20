from math import sin, radians as rad

class Parallelogram:
    def __init__(self, a,b, angle):
        self.a=a
        self.b=b
        self.angle = angle
    def area(self):
        return self.a*self.b* sin(rad(self.angle))

class Rhombus(Parallelogram):
    def __init__ (self, a, angle):
        self.a = a
        self.angle = angle

    def area(self):
       return self.a**2*sin(rad(self.angle))

class Square(Rhombus):
    def __init__(self, a):
        self.a=a
    def area(self):
        return self.a**2

class Rectangle(Parallelogram):
    def __init__(self, a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b


rhombus= Rhombus(6, 30)
print(rhombus.area())
square = Square(5)
print(square.area())
rectangle= Rectangle(2,4)
print(rectangle.area())
p1=Parallelogram(10,10, 90)
print(p1.area())



