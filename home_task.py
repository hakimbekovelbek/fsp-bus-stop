def fill_tank(full):
    return full
def avaible_distance(have , perhour):
    dist = (have//perhour)
    not_full = (have - dist*perhour)/perhour * 100
    return f'{dist * 100} + {not_full} km'
def ride(how_many , have , perhour):
    have = how_many / 100 * perhour - have
    # global have 
    # have = how_many / 100 * perhour - have надо было сделать! так как тут локальное!
    return f'You have {have} fuil and you arrived {how_many} km'
have = 55
full = 75
have = fill_tank(full)

class Car:
    def __init__(self , full_b , have_b , perhour):
        self.full_b = full_b
        self.have_b = have_b
        self.perhour = perhour
    def info(self):
        return f'Full_fuil{self.full_b}  , You have {self.have_b} , You spend for hour {self.perhour}'
    def change_values(this , full_b ,have_b , perhour):
        this.perhour = perhour
        this.have_b = have_b
        this.full_b = full_b
class Car_Func:
    def __init__(self , info , arrived_distance = 0):
        self.info = info
        self.arrived_distance = arrived_distance
    def fill_tank(self):
        self.info.have_b = self.info.full_b
    def avaible_distance(this):
        dist = (this.info.have_b//this.info.perhour)
        not_full = (this.info.have_b - dist*this.info.perhour)/this.info.perhour * 100
        return f'{dist * 100 + not_full} km'
    def ride(self , how_many):
        self.info.have_b -= how_many / 100 * self.info.perhour
        self.arrived_distance += how_many
        return f'You have {self.info.have_b} fuil and you arrived {self.arrived_distance} km'

car1 = Car(75 , 55 , 15)
info_car = Car_Func(car1)
print(info_car.avaible_distance())
info_car.fill_tank()
print(info_car.avaible_distance())
print(info_car.ride(100))
print(info_car.ride(100))
print(info_car.ride(100))