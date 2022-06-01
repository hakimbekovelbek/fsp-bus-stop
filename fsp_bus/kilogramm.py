
# ! task 1 
# ? may 27.05.2022 
# ! fucking task work but i do not know it is correct or eroor


class KgToPounts:
    def __init__(self, kg):
        self.__kg = kg

    
    def pounds(self):
        return self.__kg * 2.205 , 'in pounds'

    
    
    @property
    def kilogram1(self):
        return self.__kg    
    
    @kilogram1.setter
    def kilogram1(self,new_kg):
        if not(isinstance(new_kg,(int, float))):
            raise ValueError('kilogram should be int ')
        else:
            self.__kg = new_kg


conventer  = KgToPounts(5)
print(conventer.pounds())
print(conventer.kilogram1 == 0)


# ! task 2
# ? may 27.05.2022
# ! work

# class Country:
#     def __init__(self,population):
#         self.population=population
#     def get(self):
#         return (self.population)
#     def set(self, a):
#         self.population= a

# class Russia(Country):
#     pass

# class Canada(Country):
#     pass

# class Germany(Country):
#     pass




# ! task 3
# ? may 27.05.2022 
# ! fucking task work

# def fuck(a = 0, b = 0, c = 0,d = 0, f = 0, j = 0, h= 0, i = 0, *numb):
#     sum_all = (a + b + c + d + f + j + h + i)
#     for num in numb:
#         sum_all += num
#         return sum_all
# print(fuck(1,2,3,4,5,6,7,8,9))


# ! task 4
# ? may 27.05.2022
# ! fucking task work


# class TriangleCheker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def is_triangle(self):
#         if not isinstance(self.a, (int,float)) or not isinstance(self.b, (int,float)) or not isinstance(self.c, (int,float)):
#             raise TypeError('you should enter correct symbol ')
        
#         elif self.a < 0 or self.b < 0 or self.c < 0:
#             print('please enter positive number') 
         
#         elif (self.a + self.b) <= self.c or (self.a + self.c) <= self.b or (self.c + self.b) <= self.a:
#             raise ValueError('triangle side cannat be more one side than two-other ')
#         elif self.a == self.b == self.c:
#             print('it is triangle with equal side ')

#         else:
#             print('yes you can got fucking tiangle ')

# romb = TriangleCheker(4,4,4)
# print(romb.is_triangle())


