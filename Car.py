# макс. объем бака (л)
# объем заполненности (л)
# расход (л) за 100 км
# ездить()
# заполнить бензобак
# показать сколько мы можем проехать км и остаток бензина


from msilib.schema import Error

fuel_type = {
    80: 6500,
    90: 7600,
    91: 8000,
    92: 9600
}

class Car:
    def __init__(self, volume, gas_left, consumption):
        self.volume = volume
        self.gas_left = gas_left
        self.consumption = consumption
    def ride(self, distance):
        try:
            if not isinstance(distance, (float, int)):
                raise ValueError('Distance should be a number')
        except ValueError as err:
            print(err)
            return err
        
        gas_use = (distance * self.consumption) / 100
        if gas_use < self.gas_left:
            self.gas_left -= gas_use
        else:
            try:
                raise ValueError('You do not have enough fuel. Please fill in your tank')
            except ValueError as err: 
                print(err)
                return err


    def fill_tank(self, added_fuel):
        if added_fuel < self.volume:
            self.gas_left = added_fuel
        else:
            try:
                raise ValueError('You dont have enough space in your fuel_bank try to decrease the amount of fuel')
            except ValueError as err:
                print(err)
                return err

    def cal_gas_costs(self, type, litres):
        pass

    def available(self):
        available_dist = (self.gas_left * 100) / self.consumption

matiz = Car(35, 25, 8)
matiz.ride(300)
print(matiz.gas_left)
matiz.ride(200)
matiz.fill_tank()
matiz.fill_tank(40)
print(matiz.available())