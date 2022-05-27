# def sum(a, b, *nums):
#     acc = a + b
#     for num in nums:
#         acc += num
#     print(acc)


# sum(1,2)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f'Point({self.x}, {self.y})'

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)

# p1 = Point(1, 10)
# p2 = Point(5, 2)
# print(p1 + p2)

# def sum(a, b, c=0):
#         print(a + b + c)

# sum(1, 2)
# sum(1, 2, 3)
# from typing import overload

# @overload
# def sum(a, b, c):
#     print(a + b + c)

# def sum(a, b):
#     print(a + b)

# sum(1, 2)
# sum(1, 2, 10)


class Matrix:
    size = 2
    # matrix = []
    def __init__(self):
        self.matrix = []
        for row_num in range(1, self.size + 1):
            row = []
            for col_num in range(1, self.size + 1):
                num = int(input(f'Enter {row_num}.{col_num}:'))
                row.append(num)
            self.matrix.append(row)

    def __mul__(self, C):
        pass


m1 = Matrix()
# m2 = Matrix()
print(m1 * 2)
# print(m2.matrix)