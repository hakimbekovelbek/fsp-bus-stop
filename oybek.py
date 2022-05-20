# Oybek
# This is new line in oybek.py file.

# def calcLengthOfSlice(x1, y1, x2, y2):
#     c = (x2 - x1)**2 + (y2 - y1)**2
#     return c ** 0.5



# class Car:
#     def __init__(self, объем, топливо, расход):
#         self.объем = объем
#         self.топливо = топливо
#         self.расход = расход
#     def доступное_дистанция(self):
#         a = (self.топливо/self.расход*100)
#         print("100 литр", a)
#     def доступное_дистанция2(self):
#         b = (self.топливо - self.расход)
#         c = (b / self.расход)
#         print("1 литр",c)
#     def пополнение_бака(self):
#         d = 100
#         print("Бак",d)

# Malibu = Car(100, 100, 18)
# Malibu.доступное_дистанция()
# Malibu.доступное_дистанция2()
# Malibu.пополнение_бака()   


# gas_types = {
#     80: 6400,
#     92: 9000,
#     98: 13000
    
# }


# class Car:
#     def __init__(self, volume, gas_left, consumption):
#         self.volume = volume
#         self.gas_left = gas_left
#         self.consumption = consumption

#     def ride(self, distance):
#         try:
#             if not isinstance(distance, (float, int)):
#                 raise ValueError('Distance should be a number')
#         except ValueError as err:
#             print(err)
#             return err
        
#         gas_use = (distance * self.consumption) / 100
#         if gas_use < self.gas_left:
#             self.gas_left -= gas_use
#         else:
#             try:
#                 raise ValueError('You do not have enough fuel. Please fill in your tank')
#             except ValueError as err: 
#                 print(err)
#                 return err

#     def fill_tank(self , quantity, fuel_type):
#         try:
#             if not(isinstance(quantity , (float , int))) or not(isinstance(quantity, (float, int))):
#                 raise ValueError("Enter a number!")
#         except Exception as err:
#             print(err)
#             return err
#         if self.gas_left + quantity < self.volume and fuel_type in fuel_type:
#             self.gas_left += quantity
#             cost = quantity * fuel_type[fuel_type]
#             print(f'It costs {cost} sums')
#             return cost 
#         else:
#             try:
#                 if self.filled + quantity > self.volume:
#                     raise ValueError("Too much fuil")
#                 else: raise TypeError ("Please select correct type of fuel!")    
#             except Exception as err:
#                 print(err)
#                 return err 

#     def calc_gas_costs(self, type, litres):
#         if type == 80:
#             print(litres * 6400)
#         if type == 92:
#             print(litres * 9000)
#         if type == 98:
#             print(litres * 13000)    
#         return   


#     def available(self):
#         available_dist = (self.gas_left * 100) / self.consumption
#         return (self.gas_left, available_dist)

# matiz = Car(35, 25, 8)

# print(matiz.gas_left)
# matiz.ride(300)
# print(matiz.gas_left)
# matiz.ride(200)
# print(matiz.available()) 
# print(matiz.calc_gas_costs(80, 20*6400))
# matiz.fill_tank(20, 80)

# class Person:
#     def __init__(self, money):
#         self.money = money

#     def pay_money(self, amount):
#         if amount > self.money:
#             print("")
#         else:    
#             self.money -= self.amount
    

# person = Person(300_000)
# money_to_pay = matiz.calc_gas_costs()
# person.pay_money(money_to_pay)            

from cgi import print_form
import math
class Parallelogramm:
    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle 

    def area(self):
        import math
        return self.a * self.b * math.sin(math.radians(self.angle))        

class Rectangle(Parallelogramm):
    def __init__(self, a, b):
        Parallelogramm.__init__(self, a, b,)
    def area(self):
        return self.a * self.b

class Rhombus(Parallelogramm):
    def __init__(self, a, angle):
        self.a = a
        self.angle = angle
    def area(self):
        return (self.a**2) * math.sin(math.radians(self.angle))

class Square(Parallelogramm):
    def __init__(self, a):
        self.a = a 
    
    def area(self):
        return self.a ** 2
# rect1 = Rectangle(2, 3)
# print(rect1.a, rect1.b)

# rhombus = Rhombus(5)
# print(rhombus.a)

# square = Square(4)
# print(square.a)
sq = Square(10)
pr = Parallelogramm(10,10,90)
rh = Rhombus(4, 90)

print(pr.area())
print(sq.area())
print(rh.area())