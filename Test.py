# Task 1
# class KgToPounds:
    
#     def __init__(self, kg):
#         self.kg = kg

#     def to_pounds(self):
#         return round(self.__kg * 2.205, 1)

#     @property
#     def kg(self):
#         return self.__kg
    
#     @kg.setter
#     def set_kg(self, new_kg):
#         if not(isinstance(new_kg, (int, float))):
#             raise ValueError('Килограммы задаются только числами')
#         else:
#             self.__kg = new_kg
   


# kg = KgToPounds
# print(kg.to_pounds())
# kg.kg = 5151
# print(kg.kg)
# print(kg.to_pounds())



# Task 2
# class Country:
#     def __init__(self, population):
#         self.population = population
      



#     def __init__(self, population):
#         Country



#     @property
#     def population(self):
#         return( self.__population)
    
#     @population.setter
#     def population(self, new_population):
#         self.population = new_population

# class Russia(Country):
#     pass

# class Canada(Country):
#     pass

# class Germany(Country):
#     def __init__(self):
#        pass 



# Task 3
# def sum(first = 0, second = 0, third = 0, fourth = 0, fifth = 0, sixth = 0, seventh = 0, eight = 0, nine = 0, *nums):
#     sum = first + second + third + fourth + fifth + sixth + seventh + eight + nine
#     for num in nums:
#         sum += num
#     return sum

# print(sum(10, 20, third = 30, fifth = 50))   

# Task 4
# class TriangleChecker:
#     def __init__(self, num1, num2, num3):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3

#     def is_triangle(self):
#         if not(isinstance(self.num1, (int, float))) or not(isinstance(self.num1, (int, float))) or not(isinstance(self.num1, (int, float))):
#             raise TypeError('Введите значение в int или float')
        
#         elif self.num1 < 0 or self.num2 < 0 or self.num3 < 0:
#             return ('С минусом нельзя')
#         elif (self.num1 + self.num2) <= self.num3 or (self.num1 + self.num3) <= self.num2 or (self.num3 + self.num2) <= self.num1:
#             return ('Это невозможно')
#         else: return ('Да, ты можешь это сделать ')
# tri = TriangleChecker(1, 2, 3)        
# print(tri.is_triangle())