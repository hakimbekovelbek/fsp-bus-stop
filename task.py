from socket import PACKET_BROADCAST


class Parallelogram:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


    def S_square(self):
        surface_area = self.a ** 2
        return surface_area

    def S_rectangle(self):
        surface_area = self.a * self.b
        return surface_area    

    def S_rhombus(self):
        surface_area = 4 * (self.c / 2 + self.d / 2)
        return surface_area



class Square(Parallelogram):
    def S_square(self):
        x = Parallelogram.S_square(self)
        return x

class Rectangle(Parallelogram):
    def S_rectangle(self):
        x = Parallelogram.S_rectangle(self)
        return x


class Rhombus(Parallelogram):
    def S_rhombus(self):
        x = Parallelogram.S_rhombus(self)
        return x

sas = Parallelogram(3, 5)
sar = Parallelogram(3, 5)
sarr = Parallelogram(4, 6, 8, 4)
print(sas.S_square())
print(sar.S_rectangle())
print(sarr.S_rhombus())