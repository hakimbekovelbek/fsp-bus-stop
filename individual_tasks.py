

from typing import Type


class KgToPounds:

    def __init__(self, kg):
        self.kg = kg    
    
    def to_pounds(self):
        return round(self._kg * 2.205, 1)

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, new_kg):
        if not(isinstance(new_kg, (int, float))):
            raise TypeError('Kg must be in int or float')
        else:
            self._kg = new_kg


# pound = KgToPounds(32)
# print(pound.to_pounds())
# pound.kg = 58943242
# print(pound.kg)
# print(pound.to_pounds())



class Country:
    def __init__(self, ppl):
        self.ppl = ppl
    @property
    def ppl(self):
        return self._ppl

    @ppl.setter
    def ppl(self, new_ppl):
        self._ppl = new_ppl

class Russia(Country):
    pass

class Canada(Country):
    pass


class Germany(Country):
    pass


# rus = Russia(140000000)
# print(rus.ppl)
# rus.ppl = 150000000
# print(rus.ppl)




def sum(first = 0, second = 0, third = 0, fourth = 0, fifth = 0, sixth = 0, seventh = 0, eighth = 0, ninth = 0, tenth = 0, *nums,):
    sum = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + tenth
    for num in nums:
        sum += num
    return sum

# print(sum(second = 20, first = 8987))


class TriangleChecker:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def is_triangle(self):
        if not(isinstance(self.num1, (int, float))) or not(isinstance(self.num1, (int, float))) or not(isinstance(self.num1, (int, float))):
            raise TypeError('Enter values in int or float')
        
        elif self.num1 < 0 or self.num2 < 0 or self.num3 < 0:
            return ('It is not possible with negatives')
        elif (self.num1 + self.num2) <= self.num3 or (self.num1 + self.num3) <= self.num2 or (self.num3 + self.num2) <= self.num1:
            return ('It is not possible')
        else: return ('Yeah you can do it')

tr = TriangleChecker(3, -4, 4)
print(tr.is_triangle())

