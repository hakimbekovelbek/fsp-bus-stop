class Car:
    def __init__(self,volume,oil,consumtion):
        self.volume = volume
        self.oil = oil
        self.consumtion = consumtion
        
    def remaining_distance(self):
        s = (self.oil - 15)
        a = (s / 15) * 100
        print('оставшаяся дистанция ', self.oil, 'литр', a)

    def fill_tank(self):
        i = 100
        print('Бак полон на', i)

car = Car(50,40,15)
car.remaining_distance()
car.fill_tank()