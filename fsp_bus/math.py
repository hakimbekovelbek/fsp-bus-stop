# def abs(x):
#     if x >= 0: return x
#     else: return -x

# def factorial(x):
#     if x == 1: return 1
#     return factorial(x - 1) * x


class Card:
    item = []
    # def __init__(self, item):
    
        # self.item = item.append()

    def add_item(self, item):
        self.item.append(item)

    
    def remove_item(self, title, amount = 1):
        try:
            for i in range(amount):
                self.items.remove(title)
        except:
            print('Error, enter correct titlle or amount')
            return
        

    def show_item(self):
        for item in self.item:
            print('Name' + item.title, 'Price' + str(item.price))

    

    def total_item(self):
        pass

milk = Card
print(milk.add_item(milk,))
print(milk.remove_item(milk,))

