# def sum(a,b,c,d):
#     print(a+b+c+d)


# sum(1,2,3,4)
# sum(1,c=3,b=5,d=10)

# def sum(a,b, *nums):
#     acc=a+b
#     for num in nums:
#         acc +=num
#     print(acc)
# sum(1,2,3,4,5,6,7,8)


# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         x = self.x +other.x
#         y = self.y + other.y
#         return Point(x,y)
#     def __str__(self):
#         return f'{self.x},{self.y}'
    
# p1=Point(1,10)
# p2=Point(5,2)
# print(p1+p2)

# def sum(a,b,c=None):
#     if c ==None:
#         print(a+b)
#     else:
#         print(a+b+c)

# sum(12,67)

# def area(a=None,b=None):
#     if a==None and b ==None:
#         print(0)
#     elif b ==None:
#         print(a*a)
#     else:
#         print(a*b)
# area()
# area(2)
# area(2,6)


# from inspect import signature
# from typing import overload

# class Math:
#     @overload
#     # @signature
#     def sum(self,a,b):
#         print(a+b)
    
#     @sum.overload
#     # @signature("three")
#     def sum(self,a,b,c):
#         print(a+b+c)

# a = Math()
# a.sum(1,2)
# a.sum(1,210)
# class Matrix:
#     size=3
#     matrix=[]
#     def __init__(self):
#         for row in range(1,self.size+1):
#             row=[]
#             for column_num in range(1,self.size+1):
#                 num = int(input(f'Enter {row}.{column_num}: '))
#                 row.append(num)
#             self.matrix.append(row)
# m1=Matrix()
# print(m1.matrix)





