# *args  * значит неограниченное количество параметров!
# class Point:
#     def __init_(self , x , y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f'({self.x} , {self.y})'
#     def __add__(self,other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x , y)
# p1 = Point(1 , 3)
# p2 = Point(5 , 2)
# print(p1+p2)
# def area(a =0, b=None):
#     if b == None:
#         return a**2
#     else:
#         return a*b
# print(area())
# print(area(2 , 3))

# from typing import overload


# @overload
# def sum(a,b):
#     return a+b
# @overload
# def sum(a , b , c):
#     return a+b+c
# sum(1 , 2)
# sum(1 , 2 , 3)
#  не правильно в питон 3
class Matrix:
    size = 2
    def __init__(self):
        self.matrix = []
        for row_num in range(1 , self.size+1):
            row = []
            for colm_num in range(1 , self.size+1):
                num = int(input(f'Enter {row_num}.{colm_num}: '))
                row.append(num)
            self.matrix.append(row)
    # def __str__(self):
    #     return f'{self.matrix}'
    def __mul__(self , k):
        for row in range(self.size):
            for colm in range(self.size):
                self.matrix[row][colm] = self.matrix[row][colm]*k
        return self.matrix

m1 = Matrix()
m2 = Matrix()
print(m1 * 2)
# print(m1.matrix)