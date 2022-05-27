

class Triangle_checker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if self.a <0 or self.b < 0 or self.c<0:
            print("Sides of triangle must be  number ")
        elif not(isinstance(self.a , int)) or not(isinstance(self.b , int)) or not(isinstance(self.c , int)):
            raise ValueError("Sides of traingle must be number")
        elif self.a + self.b > self.c and self.a + self.c >self.b and self.b + self.c > self.a:
            print("triangle exisctances")
        else:
            print("triangle is not exixtance")        

            
            



triangle = Triangle_checker(10, 20, 15)
triangle.is_triangle()
