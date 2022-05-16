class Car:
    v = 70
    def __init__(self,capacity, presence, oilExpenditure):
        self.capacity = capacity
        self.presence = presence
        self.oilExpenditure = oilExpenditure

    def fill_tank(self):
        self.presence = int(input('fill tank'))
        return(self.presence)

    def available_distance(self):
        if self.capacity >= self.oilExpenditure:
            print(self.presence * 100/self.oilExpenditure)
            if self.presence > 75:
                print('too much oil')
            else:
                print('need more')

lacceti = Car(75, 55, 15)
lacceti.fill_tank()
print(lacceti.available_distance())
    