class Car:
    v = 70
    def __init__(self,capacity, presence, oilExpenditure):
        self.capacity = capacity
        self.presence = presence
        self.oilExpenditure = oilExpenditure

    def fill_tank(self):
        self.presence = int(input('наполнять'))
        return(self.presence)

    def available_distance(self):
        if self.capacity >= self.oilExpenditure:
            print(self.presence * 100/self.oilExpenditure)
            if self.presence > 75:
                print('много')
            else:
                print('мало')

lacceti = Car(75, 55, 15)
lacceti.fill_tank()
print(lacceti.available_distance())
    