class Car:
    def __init__(self,b, c):
        self.b = b
        self.c = c
class Avaib_dist:
    def __init__(self, fill_fuel, spend_for):
        self.fill_fuel = fill_fuel
        self.spend_for = spend_for

    def avai_dist(self):
        a = (100 / self.spend_for.c) * self.fill_fuel.b
        return a

d = Car(55, 15)
e = Car(55, 15)
avaib_dist = Avaib_dist(d, e)
print(avaib_dist.avai_dist())


