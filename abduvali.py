# This line is from Abduvali's laptop
# This is new file in abduvali.py file
class Car:
    def __init__(self,amount,oil,consumption,distance):
        self.amount=amount
        self.oil=oil
        self.consumption=consumption
        self.distance=distance
    def fill_tank(self):
        a=self.oil=75 
        print( f'your tank is filled to {a} L')
    def available_distance(self):
        return f'your available distance is {self.oil} L for {self.oil / 0.15} km'
    def ride(self):
        time = self.distance / 70
        consumed = self.distance * 0.15
        balance=self.oil - consumed
        return f'''
        Time: {round(time,1)} Hrs
        Consumed oil: {consumed}
        Remaining fuel: {balance}'''
        
        
        

Lacetti =Car(75,55,15,100)
# print(Lacetti.available_distance())
# print(Lacetti.fill_tank())
print(Lacetti.ride())