# from cgi import print_exception
# from turtle import title


# gas_types={
#     80:6400,
#     92:9000,
#     95:10000
# }
# class Car:
#     def __init__(self,amount,oil,consumption):
#         self.amount=amount
#         self.oil=oil
#         self.consumption=consumption

#     def fill_tank(self,fuel_type):
#         if self.amount >= self.oil and fuel_type in gas_types:
#             filled=self.amount-self.oil
#             bill =filled * gas_types[fuel_type]
#             return f'you filled to {self.amount-self.oil} L and total cost is {bill} sums'
#         else:
#             self.amount <= self.oil and fuel_type not in gas_types
#             print("U can not fill your tank more than capacity or you choosed incorrect type!")
    
#     def available_distance(self):
#         return f'your available distance is {self.oil} L for {round(self.oil / 0.15,1)} km'
#     def ride(self,distance):
#         time = distance / 70
#         consumed = distance * 0.15
#         balance=self.oil - consumed
#         return f'''
#         Time: {round(time,1)} Hrs
#         Consumed oil: {consumed}
#         Remaining fuel: {balance}'''
#     def calc_gas_costs(self,type,litres):
#         pass
        

# # class Person:
# #     def __init__(self, money):
# #         self.money = money

# #     def pay_money(self, amount):
# #         self.money -= self.amount

# # iskandar = Person(300_000)
# # money_to_pay = matiz.calc_gas_costs()
# # iskandar.pay_money(money_to_pay)       
        

# Lacetti =Car(75,55,15)
# # print(Lacetti.available_distance())
# print(Lacetti.fill_tank(80))
# # print(Lacetti.ride(100))

class item:
    def __init__(self,title,price):
        self.title = title
        self.price=price

class Cart:
    list = []
    def __init__(self,title,price):
        self.title = title
        self.price=price
    def add_item(self,item):
        self.list.append(item)
    def show_items(self):
        print(f''' name ; {self.title}
price; {self.price}''')
    def total_price(self):
        total = 0
        for i in self.title:
            total += i.price
            print(f'total price is ; {total}')
    def remove_item(self,title,amount):
        try:
            for i in range(amount):
                self.list.remove(title)
        except:
            print('Incorrect item')
            return
milk=Cart('Milk',10000)
Coke=Cart('Coke',5000)
snak=Cart('Snickers',7000)

print(milk.show_items())
print(Coke.show_items())
print(Coke.show_items())
