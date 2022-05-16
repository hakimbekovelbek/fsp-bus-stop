from calendar import c


class Car:
    def __init__(self, value, oil, consumtion):
        self.value = value
        self.oil = oil
        self.consumtion = consumtion
    def avaible_distance(self):
        c = (self.oil / self.consumtion) * 100
        print('avaible_distance with ',self.oil, 'litr', c)
    def avaible_distance2(self):
        s = (self.oil - 15) 
        a = (s / 15) * 100
        print('avaible_distance with ',s,'litr', a)
    def fill_tank(self):
        c= self.oil = self.oil
        return c

captiva = Car(75,20,15)
print(captiva.avaible_distance())
print(captiva.avaible_distance2())
print('your tank is full', captiva.fill_tank())