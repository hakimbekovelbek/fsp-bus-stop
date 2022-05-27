# class KgToPounds:
#     def __init__(self, kg) -> None:
#         self.__kg = kg
   
#     def to_pounds(self):
#         return self.__kg * 2.205

#     @property
#     def new_kg(self):
#         return self.__kg
#     @new_kg.setter
#     def new_kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             raise ValueError('Kilograms should be a numbers')

# mass = KgToPounds(20)
# mass1 = KgToPounds(20.5)

# print(mass.to_pounds())
# print(mass1.to_pounds())

class Country:
    pass
class Russia(Country):
    
    def __init__(self, population =140) -> None:
        self.__population = population
    def get_population(self):
        return self.__population

    def set_population(self, new_population):
        if isinstance(new_population, (int, float)):
            self.__population = new_population
        else:
            raise ValueError("Population should be a number")

class Canada(Country):
    
    def __init__(self, population = 120) -> None:
        self.__population = population
    
    def get_population(self):
        return self.__population

    def set_population(self, new_population):
        if isinstance(new_population, (int, float)):
            self.__population = new_population
        else:
            raise ValueError("Population should be a number")
    

class Germany(Country):
   
    def __init__(self, population = 80) -> None:
        self.__population = population
    
    def get_population(self):
        return self.__population

    def set_population(self, new_population):
        if isinstance(new_population, (int, float)):
            self.__population = new_population
        else:
            raise ValueError("Population should be a number")

    

rus = Russia()
rus.set_population(120)
print(rus.get_population())


can = Canada()

can.set_population(149)
print(can.get_population())

ger = Germany()

ger.set_population(50)
print(ger.get_population())

# def show_me(first = 0, second = 0, third = 0, fourth = 0, *nums):
#     sum = first + second + third + fourth
#     for i in nums:
#         sum += i
#     return sum

# print(show_me(10, 12, 14, 15, 16, 17))
# # print(show_me(10, 12, 14, 15, 16, third = 17, fourth = 18))
# print(show_me(second = 2, fourth = 12))
# print(show_me(10, 12, third = 14, fourth = 15))
# print(show_me(first = 10, second = 12, third = 14, fourth = 15))


# class TriangleChecker:
#     def __init__(self, a, b, c) -> None:
#         self.a = a
#         self.b = b
#         self.c = c

#     def is_tiangle(self):
#         if not isinstance(self.a, (int, float)):
#                raise ValueError('Sides of triangle should be integer or float!!!')
#         if not isinstance(self.b, (int, float)):
#                raise ValueError('Sides of triangle should be integer or float!!!')
#         if not isinstance( self.c, (int, float)):
#                raise ValueError('Sides of triangle should be integer or float!!!')
#         if not self.a  >= 0:
#             raise ValueError('Sides of trangle should be only positive!!!')
#         if not self.b >= 0:
#             raise ValueError('Sides of trangle should be only positive!!!')
#         if not self.c >= 0:
#             raise ValueError('Sides of trangle should be only positive!!!')   
#         if self.a + self.b < self.c:
#             print('With these values triangle could not be created' )

#         elif self.c + self.b < self.a:
#             print('With these values triangle could not be created' )
        
#         elif self.a + self.c < self.b:
#             print('With these values triangle could not be created' )
#         else:
#             print('Yeah we can build triangle with this ')

# tr = TriangleChecker(3, 4, 5)

# print(tr.is_tiangle())
        




