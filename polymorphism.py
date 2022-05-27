
# def sum(a, b, c, d):
#     print(a + b + c + d)

# sum(1, a = 3, b = 5, d = 10)

# def sum(a, b, *nums):
#     acc = a + b
#     for num in nums:
#         acc += num
#     print(acc)
# sum(1, 2, 4, 5, 6, 7, 8)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f'({self.x}, {self.y})'

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)


# p1 = Point(1, 10)
# p2 = Point(5, 2)
# print(p1 + p2)



# def sum(a, b, c = 0):
#     print(a + b + c)


# def area(a = None, b = None):
#     if a == None and b == None:
#         print(0)
#     elif b == None:
#         print(a * a)
#     else:
#         print(a * b)

# area()
# area(2)
# area(2, 6)




# @overload
# def sum(a, b, c):
#     print(a + b + c)
    

# def sum(a, b):
#     print(a + b)


# sum(1, 2)
# sum(1, 2, 10)





class Matrix:
    size = 3
    def __init__(self):
        self.matrix = []
        for row_num in range(1, self.size + 1):
            row = []
            for col_num in range(1, self.size + 1):
                num = int(input(f'Enter {row_num}.{col_num}: '))
                row.append(num)
            self.matrix.append(row)

    def __mul__(self, C):
        new_matrix = []
        for row in self.matrix:
            new_row = []
            for num in row:
                new_num = num * C
                new_row.append(new_num)
            new_matrix.append(new_row)
            self.matrix = new_matrix
        return self

    def __str__(self):
                return f'''
    {self.matrix[0]}
    {self.matrix[1]}
    {self.matrix[2]}
                '''

m1 = Matrix()
m1 *= 2
print(m1)
