
class Car:
    def __init__(self, value, oil, consumtion):
        self.value = value
        self.oil = oil
        self.consumtion = consumtion

    def avaible_distance(self):
        c = (self.oil / self.consumtion) * 100
        print('avaible_distance with ',self.oil, 'litr', c)
    
    def avaible_distance2(self):
        s = (self.oil - self.consumtion) 
        a = (s / self.consumtion) * 100
        print('avaible_distance with ',s,'litr', a)
    
    def fill_tank(self):
        c= self.oil = self.oil
        print('tank is full',c)
        return 
    
    def price_gas(self, type, litres):
        if type == 80:
            print(litres * 6400)
        elif type == 91 or 92:
            print(litres * 9000)
        return 
        

captiva = Car(75,20,15)
print(captiva.avaible_distance())
print(captiva.avaible_distance2())
print(captiva.fill_tank())
print(captiva.price_gas(92,20))
    

   
# class Card:

#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
