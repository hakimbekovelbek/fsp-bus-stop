# class Geometry:
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b

#     def sqare(self):
#         a = self.side_a ** 2
#         b = (self.side_a + self.side_b) * 2

#         print('it is square - ', a)
#         print('it is perimetr - ', b)

#         return
#     def rectangle(self):
#         a = self.side_a * self.side_b
#         c = (self.side_a + self.side_b) * 2

#         print('it is square - ', a)
#         print('it is perimetr - ', c)

#         return
# f = Geometry(4, 5)  
# print(f.sqare())
# print(f.rectangle())
class Parallelogram:
    def __init__(self,a,b, angle):
        self.a = a
        self.b = b
        self.angle  = angle

    def area(self):
        from math import sin, radians
        return self.a * self.b * sin(radians(self.angle))

class Rectangle(Parallelogram):
    def __init__(self, a, b):
        Parallelogram.__init__(self,a,b)

class Rombus(Parallelogram):
    def __init__(self, a):
        self.a = a

class Square(Parallelogram):
    pass




# rect = Rectangle(2,3)
# print('rect',rect.a, rect.b)

# rombus = Rombus(5)
# print('rombus',rombus.a)


p1 = Parallelogram(10,10,90)
print(p1.area())