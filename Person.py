class Person:
    def __init__(self, money, amount) -> None:
        self.money = money
    def pay_money(self, amount):
        if amount > self.money:
            print('You do not have enough money!!')
        else: 
            self.money -= amount  
        return self.money
