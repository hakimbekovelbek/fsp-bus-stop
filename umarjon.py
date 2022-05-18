# This line from Umarjon's laptop
# This is test message

fuel_types = {
    80 : 6400,
    92 : 9000,
    95 : 1000,
    100 : 1100
}
class Car:
    def __init__(self, volume, filled, consuption):
        self.volume = volume
        self.filled = filled
        self.consuption = consuption

    def fill_tank(self, fuel_volume, fuel_type):
        try:
            if not(isinstance(fuel_volume, (float, int))) or not(isinstance(fuel_volume, (float, int))):
                raise ValueError("Enter a number")
        except ValueError as err:
            print(err)
            return err
        if self.filled + fuel_volume < self.volume and fuel_type in fuel_types:
            self.filled += fuel_volume
            cost = fuel_volume * fuel_types[fuel_type]
            print(f'It costs {cost} sums')
            return cost
        else:
            try:
                if self.filled + fuel_volume > self.volume:
                    raise ValueError('Fuel volume over than tank volume')
                else: raise TypeError('Please select correct type of fuel')
            except ValueError as err:
                print(err)
                return err
            except TypeError as err:
                print(err)
                return err

    def available_distance(self):
        av_distance = round(self.filled / self.consuption * 100)
        print(f'{round(self.filled)}, {av_distance} km')

    def ride(self, distance):
        if self.filled - (distance / 100 * self.consuption) < 0:
            print('You cannot ride, because you need more fuel')
        else: self.filled -= distance / 100 * self.consuption
        
        

# lacetti = Car(75, 55, 15)
# lacetti.fill_tank(10)
# lacetti.available_distance()
# lacetti.ride(100)
# # lacetti.available_distance()
# phantom = Car(150, 60, 40)
# phantom.available_distance()
# money_to_pay = phantom.fill_tank(80, 92)
# phantom.ride(200)
# phantom.available_distance()

class Person:
    def __init__(self, money):
        self.money = money

    def pay_money(self, amount):
        if amount > self.money:
            print("You don't have much money")
        else: 
            self.money -= amount

# iskandar = Person(300_000)
# iskandar.pay_money(money_to_pay)




class Item:

    def __init__(self, title, price):
        self.title = title
        self.price = price


class Cart:
    items = []
    # def __init__(self):
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, title, amount = 1):
        try:
            for i in range(amount):
                self.items.remove(title)
        except:
            print('Enter correct title or amount')
            return
    def show_items(self):
        for item in self.items:
            print("Name: " + item.title,"Price: " + str(item.price))

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        print(f'Total cost: {total} UZS')
        return total

milk = Item('Milk', 11000)
meat = Item('Beef', 70000)
pepsi = Item('Pepsi', 10000)
red_bull = Item('Red Bull', 25000)

cart = Cart()
cart.add_item(milk)
cart.add_item(meat)
cart.add_item(red_bull)
cart.add_item(pepsi)
cart.show_items()
cart.remove_item(pepsi)
cart.show_items()
cart.total_price()


