import math
class Paralelogram:
    def __init__(self, a, b, angle) -> None:
        self.a = a
        self.b = b
        self.angle = angle
    def area(self):
        return self.a * self.b * math.sin(math.radians(self.angle))
class Rectangle:
    def __init__(self, a, b) -> None:
        Paralelogram.__init__(self, a, b)
    
    def area(self):
        return self.a * self.b

class Rhombus(Paralelogram):
    def __init__(self, a, angle) -> None:
        self.a = a
        self.angle = angle 
    def area(self):
        return (self.a**2) * math.sin(math.radians(self.angle))
class Squere(Rhombus):
    def __init__(self, a) -> None:
        self.a = a
    
    def area(self):
        return self.a ** 2
sq = Squere(10)

pr = Paralelogram(10, 10, 90)
rh = Rhombus(4, 90)

print(pr.area())
print(sq.area())
print(rh.area())



        
