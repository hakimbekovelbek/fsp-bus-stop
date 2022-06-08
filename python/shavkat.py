class Vehicle:
    def init(self, capacity, presence, oilExpenditure):
        self.a = capacity
        self.b = presence
        self.c = oilExpenditure
    def availableDistance(self):
        if self.b>=self.c:
         print(self.b, self.b*100/self.c)
         if self.b>75:
             print("too much oil, it won't ride")
        else:
         print('need more oil')
       
    

lacceti = Vehicle(75, 65, 15)
print(lacceti.availableDistamce())