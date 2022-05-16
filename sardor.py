# 

# ! this file created by Sardor
#? this new line added by Sardor

V = 70
C = 100 # ! this const number is km 
class Car:
    def __init__(self, capacity, rate, consumption) -> None:
        self.capacity = capacity
        self.rate = rate
        self.consumption = consumption
    
    def fill_tank(self):
        empty = self.capacity - self.rate
        full = self.rate + empty
        self.rate = full
        if full == self.capacity: return f'Yor tank filled to {self.rate}'

    def available_distance(self):
        distance = (self.rate * C) / self.consumption
        return f'{round(distance, 1)} km'

    def ride(self, distance):
        
        time = distance / 70
        consumed = distance * (self.consumption / 100)
        balance = self.rate - consumed
        return f'''
        Time: {round(time,1)} Hrs
        Consumed oil: {consumed}
        Remaining fuel: {balance}'''


                         
laccetti = Car(75, 55, 15)
audi_q7 = Car(100, 75, 10)
lc_300 = Car(90, 60, 14)
print(lc_300.fill_tank())
print(lc_300.available_distance())
print(lc_300.ride(100))    