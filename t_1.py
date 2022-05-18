class Parallelogram:
    def __init__(self , a , b):
        self.a = a
        self.b = b
class Square(Parallelogram):
    def area(self):
        return self.a ** 2
class Rectangle(Parallelogram):
    def area(self):
        return self.a * self.b
class Rhombus(Parallelogram):
    def area(self):
        return self.a ** 2
pr = Parallelogram(3 , 2)
sq = Square(3 , 3)
rc = Rectangle(5 ,4)
rh = Rhombus(1 , 1)
print(sq.area() , rc.area() , rh.area())