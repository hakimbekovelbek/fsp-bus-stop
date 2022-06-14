# velocity = 70

class VehicleBio:
    def __init__(self, capacity, presence, oilExpenditure):
        self.a = capacity
        self.b = presence
        self.c = oilExpenditure
    # def fillTank(self):
    #     self.b = int(input('fill tank '))
    #     return(self.b)
    def availableDistamce(self):
        if self.b>=self.c:
         print(self.b, self.b*100/self.c)
         if self.b>75:
             print("too much oil, it won't ride")
        else:
         print('need more oil')
       
    

lacceti = VehicleBio(75, 65, 15)
# lacceti.fillTank()
print(lacceti.availableDistamce())