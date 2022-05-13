def calcLengthOfSlice(x1, y1, x2, y2):
    c = (x2 - x1)**2 + (y2 - y1)**2
    return c ** 0.5

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

    def set_coors(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class Slice:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def calcLengthOfSlice(self):
        c = (self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2
        return c ** 0.5

a = Point(2, 5)
b = Point(0, 7)
slice = Slice(a, b)
print(slice.calcLengthOfSlice())

