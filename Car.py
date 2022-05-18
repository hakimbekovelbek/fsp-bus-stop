# макс. объем бака (л)
# объем заполненности (л)
# расход (л) за 100 км

# ездить()
# заполнить бензобак
# показать сколько мы можем проехать км и остаток бензина

from msilib.schema import Error

gas_types={
        80: 6400,
        91:7500,
        90:7200
    }
class Car:
    gas_types={
        80: 6400,
        91:7500,
        90:7200
    }
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

    def fill_tank(self , quantity , type):
        try:
            if not isinstance(quantity , (float , int)):
                raise ValueError("Enter a number!")
        except Exception as err:
            print(err)
            return err
        if self.gas_left + quantity < self.volume:
            self.gas_left += quantity
            return self.calc(type , quantity , self.gas_types)
        else:
            try:
                raise ValueError("Too much fuil")
            except Exception as err:
                print(err)
                return err 
    def calc(self , type , litres , types):
        try:
            if not isinstance(type , (int)):
                raise TypeError("They all should be numbers")
        except Exception as err:
            print(err)
            return err
        if type in types:
            return types[type] * litres 
        else:
            print( "We do not have this type!" +"\n Our types")
            for i in types:
                print(i)

    def available(self):
        available_dist = (self.gas_left * 100) / self.consumption
        return (self.gas_left, available_dist)
    # def pour_gas(self , quantity):
    #     try:
    #         if not isinstance(quantity , (float , int)):
    #             raise ValueError("Enter a number!")
    #     except Exception as err:
    #         print(err)
    #         return err
    #     if self.gas_left + quantity < self.volume:
    #         self.gas_left += quantity
    #     else:
    #         try:
    #             raise ValueError("Too much fuil")
    #         except Exception as err:
    #             print(err)
    #             return err
            

matiz = Car(35, 25, 8)

print(matiz.gas_left)
matiz.ride(300)
print(matiz.gas_left)
matiz.ride(2)
# matiz.fill_tank()
print(matiz.available())
print(matiz.gas_left)
print(matiz.fill_tank(12 , 91))


class Person:
    def __init__(self, money):
        self.money = money
    def pay_money(self , amount):
        try:
            if not isinstance(amount , (int , float)):
                raise TypeError("Sorry but you can pay for this!")
        except Exception as err:
            print(err)
            return err
        if self.money - amount >0:
            self.money -= amount
            return "Successfull!"
        else:
            return f"You can't pay for this because you do not have enough money!"
        self.money -= amount


iskandar = Person(300_00)


# !
class Item:
    def __init__(self , title , price):
        self.title = title
        self.price = price
class Cart:
    products = []
    products_total_price = 0
    # def __init__(self , product):
    #     self.products.append(product)
    def add_item(self , new_product):
        self.products.append(new_product)
    def show_items(self):
        for product in self.products:
            print("Name: " + product.title , "Price: " + str(product.price))
    def total_price(self):
        for product_price in self.products:
            self.products_total_price += product_price.price
        print( self.products_total_price)
    def remove_item(self , product , count):
        try:
            for i in range(count):
                self.products.remove(product)
        except Exception as err:
            print(err)
            return err
milk  = Item('Milk' , 10_000)
cart = Cart()
cart.add_item(milk)
cart.add_item(milk)
cart.show_items()
cart.total_price()
cart.remove_item(milk , 5)

