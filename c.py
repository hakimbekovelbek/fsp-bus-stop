from math import *
from tkinter import S
class Parallelogram:
    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle

    def area(self):
        return self.a * self.b * sin(radians(self.angle))

class Square(Parallelogram):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2 

        

class Rectangle(Parallelogram):
    def __init__(self, a, b):
        Parallelogram.__init__(self, a, b)

    def area(self):
        return self.a * self.b


class Rhombus(Parallelogram):
    def __init__(self, a, angle):
        self.a = a
        self.angle = angle
    
    def area(self):
        return (self.a ** 2) * sin(radians(self.angle))

