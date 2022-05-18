class Item:
    def __init__(self, price, name) -> None:
        self.price = price
        self.name =  name 
    


class Cart:
    items = []

    def add_to_cart(self, item):
        self.items.append(item)

    def show_product(self):
        for item in self.items:
            print(f'Name: {item.name} Price: {item.price}')

    def remove_item(self, item, amount = 1):
        try:
            for i in range(amount):
                self.items.remove(item)
        except: print('Choose right product and amount')


        
    def total_cost(self):
        total = 0
        for i in self.items:
            total += i.price
        print(f'Total cost: {total}')

milk = Item(12000, "Lactel")
red_bull = Item(20000, 'Red Bull')
cart = Cart()
cart.add_to_cart(milk)
cart.add_to_cart(red_bull)
cart.show_product()
cart.remove_item(milk)

cart.total_cost()

    
