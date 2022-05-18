# This line is from Abduvali's laptop
# This is new file in abduvali.py file

class paralelogram:
    def __init__(self,a_side,b_side):
        self.a=a_side
        self.b=b_side
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

parallelogram=paralelogram(5,8)
Rhombus=rhombus(4)
print(Rhombus.a)