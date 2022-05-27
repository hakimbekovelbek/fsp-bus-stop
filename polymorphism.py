# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):
#         x = self.x +other.x
#         y = self.y + other.x
#         return Point(x, y)
    
#     def __str__(self):
#         return f'Point({self.x},{self.y})'


# p1 = Point(1, 10)
# p2 = Point(5, 2)
# print(p1+p2)

# перегрузка ф-и, перегружена 1 способ
# def  sum(a, b,c=None):
#     if c == None:
#         print(a + b)
#     else:
#         print(a+b+c)

# sum(1, 3, 4)
# sum(1, 3)

# оптимизированный
# def  sum(a, b, c=0):
#     print(a+b+c)

# sum(1, 3, 4)
# sum(1, 3)

# def area (a=0, b=None):
#     if b == None:
#         print(a**2)
#     else:
#         print(a*b)                                      

# area()

# from inspect import signature
# from typing import overload

# @overload(int)
# def sum(a, b, c):
#         print(a + b + c)


# def sum(a, b):
#         print(a+b)
    
# sum(1, 2)
# sum(1,2,10)

from sqlite3 import Row


class Matrix:
    size = 2
    
    def __init__(self):
        self.matrix= []
        for row_num in range(1, self.size+1):
            row=[]
            for col_num in range(self.size):
                num = int(input(f'enter {row_num},{col_num}: '))
                row.append(num)
            self.matrix.append(row)

    def __mul__(self, C):
        for row in range(self.size):
            for col in range(self.size):
                self.matrix[row][col] = self.matrix[row][col] ** C
        return self.matrix

m1 = Matrix()
# print(m1.matrix)
print(m1 * 2)
