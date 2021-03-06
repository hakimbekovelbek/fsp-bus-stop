# макс. объем бака (л)
# объем заполненности (л)
# расход (л) за 100 км

# ездить()
# заполнить бензобак
# показать сколько мы можем проехать км и остаток бензина

gas_types = {
    80: 6400,
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

    def fill_tank(self , quantity):
        try:
            if not isinstance(quantity , (float , int)):
                raise ValueError("Enter a number!")
        except Exception as err:
            print(err)
            return err
        if self.gas_left + quantity < self.volume:
            self.gas_left += quantity
            # return ...
        else:
            try:
                raise ValueError("Too much fuil")
            except Exception as err:
                print(err)
                return err 

    def calc_gas_costs(self, type, litres):
        pass            

    def available(self):
        available_dist = (self.gas_left * 100) / self.consumption
        return (self.gas_left, available_dist)

matiz = Car(35, 25, 8)

print(matiz.gas_left)
matiz.ride(300)
print(matiz.gas_left)
matiz.ride(200)
matiz.fill_tank()
print(matiz.available())


class Person:
    def __init__(self, money):
        self.money = money

    def pay_money(self, amount):
        self.money -= self.amount

iskandar = Person(300_000)
money_to_pay = matiz.calc_gas_costs()
iskandar.pay_money(money_to_pay)


