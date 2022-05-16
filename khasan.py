class Car:
    def __init__(self, value, oil, consumtion):
        self.value = value
        self.oil = oil
        self.consumtion = consumtion
    def avaible_distance(self):
        c = (self.oil / self.consumtion) * 100
        print('avaible_distance with ',self.oil, 'litr', c)
    def avaible_distance2(self):
        s = (self.oil - self.consumtion) 
        a = (s / self.consumtion) * 100
        print('avaible_distance with ',s,'litr', a)
    def fill_tank(self):
        s = self.oil == self.oil
        print('bezine tank full', s)

captiva = Car(75,20,15)
captiva.avaible_distance()
captiva.avaible_distance2()
captiva.fill_tank()