

# class Sky_object:
#     def __init__(self, name):
#         self.name = name

# class Star(Sky_object):
#     def __init__(self,name, color):
#         Sky_object.__init__(name)
#         self.color = color

# class Planet(Sky_object):
#     def __init__(self,name, type, mass):
#         Sky_object.__init__(self, name)
#         self.type = type
#         self._mass = mass

#     def rotate(self):
#         print(f'{self.name} is rotating ... ')

#     @property
#     def mass(self):
#         return self._mass
#     @mass.setter
#     def mass(self,new_mass):
#         if not(isinstance(new_mass, int)):
#             raise ValueError('Mass ought to be int')
#         self._mass = new_mass   
    
# class Satelitte(Sky_object):
#     def __init__(self,name):
#         Sky_object.__init__(self,name)
#         self.name = name
        
# earth = Planet('earth', 'solid', int(5.97e21))      
# print(earth.mass)
# class EarthPlsnet(Sky_object):
#     def __init__(self,name):
#         Sky_object.__init__(self,name)



# earth = Planet('Earth', 'solid')
# earth.rotate()

# !
# def sum (a,b,c,d):
#     print(a+b+c+d)

# sum(1,2,3,4)

# sum(1, c=10,b=1,d=4)

# def sum(*nums):
#     acc = 0
#     for num in nums:
#          acc += num
#     print(acc)

# sum(1,9)



# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f'Point({self.x}, {self.y})'

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)

    
# p1 = Point(1, 3)
# p2 = Point(1, 2)
# print(p1 + p2)


# def sum(a,b,c=None):
#     if c == None:
#         print(a + b)
#     else:
#         print(a+b+c)

# sum(1,2)

# def area(a=0 ,b=0):
#     if b == 0:
#         print(a ** 2)
#     else:
#         print(a * b)
# area(2)
# area(2,6)
# area()






from typing import overload

class Math:
    @overload

    def sum(self, a,b):
        print(a + b)

    def sum(self, a, b, c):
        print(a + b + c)


sum(1,2)
sum(1,2,3)
