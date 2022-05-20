class Parallelogram:
    def __init__(self , a , b , angle):
        self.a = a
        self.b = b
        self.angle = angle
    def area(self):
        import math 
        return self.a * self.b * math.sin(math.radians(self.angle))
        
class Rectangle(Parallelogram):
    def __init__(self , a , b ):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
class Rhombus(Parallelogram):
    def __init__(self, a , h):
        self.a = a
        self.h = h
    def area(self):
        return self.a * self.h
class Square(Rhombus):
    def __init__(self , a ):
        self.a = a
    def area(self):
        return self.a ** 2
pr = Parallelogram(10 , 10 , 90)
sq = Square(3)
rc = Rectangle(5 ,4)
rh = Rhombus(10 , 3)
objects = [pr , sq , rc , rh]
for object in objects:
    print(object.area())
