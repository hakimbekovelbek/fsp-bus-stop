# class Point:
#     def __init__(self, x, y) :
#         self.x= x
#         self.y = y

#     def __str__(self) :
#         return f'Point({self.x}, {self.y})'

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x,y)

# p1 = Point(1,10)
# p2 = Point(5,2)
# print(p1+p2)

# def area(a=0, b=None):
    

#     if b ==None:
#         print(a**2)
#     else:
#         print(a*b)

# area(5)





# class Math:
#     @overload
#     def sum( a, b, c):
#         print(a+b+c)

# @overload
# def sum ( a, b,):
#     print(a + b)

# a = Math()

# a.sum(1,2)
# a.sum(1,2,10)

class Matrix:
    size = 2
    size2=[]
    def __init__(self):
        self.matrix = []
        for row_num in range(1, self.size + 1):
            row = []
            for col_num in range(self.size):
                num = int(input(f'Enter {row_num},{col_num}: '))
                row.append(num)
            self.matrix.append(row)

    def __mul__(self, C):
        for row in range(self.size):
            for col in range(self.size):
                self.matrix[row][col] = self.matrix[row][col] * C
        return self.matrix
            
m1 = Matrix()
print(m1.matrix)
print(m1*3)
