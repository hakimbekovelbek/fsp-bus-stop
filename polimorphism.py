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


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        x = self.x +other.x
        y = self.y + other.y
        return Point(x,y)
    def __str__(self):
        return f'{self.x},{self.y}'
    
p1=Point(1,10)
p2=Point(5,2)
print(p1+p2)