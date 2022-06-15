from turtle import title


class Car:
    def __init__(self, max_s, left, cons):
        self.max_s = max_s 
        self.left = left
        self.cons = cons
        self.s = 0


    def fill_tank(self):
        self.left = self.max_s
        print(self.left)
    

    def ride(self, ride):
        self.s = self.s + ride
        self.left -= self.cons / 100 * ride
        print(int(self.left))
    

    def available_distant(self):
        a = self.left / self.cons * 100
        print(f"{int(self.left)}, {int(a)}км")


def car(max_s, left, cons):
    a = input("1.Fill tank, 2.Ride, 3.Available distant: ")
    if a == '1':
        left = max_s
        print(left)
    elif a == '2':
        ride = int(input(": "))
        s = 0
        s = s + ride
        left -= cons / 100 * ride
        print(int(left), ',', s)
    elif a == '3':
        b = left / cons * 100
        print(f"{int(left)}, {int(b)}км")



class Item():
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Cart():
    def __init__(self):
        self.titles = []
        self.price = []

    def add_item(self, item):
        self.titles.append(item.title)
        self.price.append(item.price)
    
    def show_items(self):
        for i in set(self.titles):
            print(i, self.titles.count(i))
    
    def total_price(self):
        price = 0
        for i in self.price:
            price += i
        print(price)
    
    def remove_item(self, item):
        self.titles.remove(item.title)
        self.price.remove(item.price)



milk = Item('milk', 10_000)
cart = Cart()
cart.add_item(milk)
cart.add_item(milk)
cart.show_items()
cart.total_price()
cart.remove_item(milk)
cart.show_items()
cart.total_price()



