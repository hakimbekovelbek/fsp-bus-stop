# This line is from Abduvali's laptop
# This is new file in abduvali.py file
import math
class paralelogram:
    def __init__(self,a_side,b_side,angle):
        self.a=a_side
        self.b=b_side
        self.angle=angle
    def area(self):
        return self.a * self.b * math.sin(self.angle)
class square(paralelogram):
    def __init__(self,a):
        self.a= a

class rectangular(paralelogram):
    def __init__(self):
        square = self.a * self.b
        print(square)
class rhombus(paralelogram):
    def __init__(self,a):
        self.a=a

class rectangle(paralelogram):
    def __init__(self,a,b):
        paralelogram.__init__

parallelogram=paralelogram(5,8)
Rhombus=rhombus(4)
print(Rhombus.a)