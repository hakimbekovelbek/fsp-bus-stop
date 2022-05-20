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
    
    def perimetr(self):
        p = (self.a + self.b) * 2
        return 'perimetr paralillogram - ', p


class Rectangle(Parallelogram):
    def __init__(self, a, b,angle):
        Parallelogram.__init__(self, a, b , angle)

    def area(self):
        a = self.a * self.b
        return 'rectangle area - ', a
        

    def perimetr(self):
        p = (self.a + self .b) * 2
        return 'perimeter of rectangle', p
        



class Rombus(Parallelogram):
    def __init__(self, a,angle):
        self.a = a
        self.angle = angle
    def perimetr(self):
        p = self.a * 4
        return'area romb', p
        
    def area(self):
        from math import sin, radians
        a = (self.a ** 2) * sin(radians(self.angle))
        return'area rombus', a
        

class Square(Parallelogram):
    def __init__(self, a):
        self.a = a
        

    def area(self):
        a = self.a ** 2
        return'area - ', a
         

    def perimtr(self):
       c = (self.a + self.a ) * 2
       return 'perimetr - ',c
       



parallelogram = Parallelogram(10,10,90)
print('area of parallelogram - ',parallelogram.area())
print(parallelogram.perimetr())


rect = Rectangle(2,3 ,90)
print(rect.area())
print(rect.perimetr())


rombus = Rombus(2,30)
print(rombus.area())
print(rombus.perimetr())


square = Square(4)
print(square.area())
print(square.perimtr())