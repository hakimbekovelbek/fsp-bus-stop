class Car:
    def __init__(self,amount,oil,consumption):
        self.amount=amount
        self.oil=oil
        self.consumption=consumption
    def fill_tank(self):

        if self.amount >= self.oil:
            return f'you filled to {self.amount-self.oil} L'
        else:
            self.amount <= self.oil
            print("U can not fill your tank more than capacity")
    def available_distance(self):
        return f'your available distance is {self.oil} L for {round(self.oil / 0.15,1)} km'
    def ride(self,distance):
        time = distance / 70
        consumed = distance * 0.15
        balance=self.oil - consumed
        return f'''
        Time: {round(time,1)} Hrs
        Consumed oil: {consumed}
        Remaining fuel: {balance}'''
        
        
        

Lacetti =Car(75,55,15)
print(Lacetti.available_distance())
print(Lacetti.fill_tank())
print(Lacetti.ride(100))