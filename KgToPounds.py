
# !1st
class KgToPounds:
    def __init__(self,kg):
        self.__kg=kg
    def to_pounds(self):
        return self.__kg * 2.205
    @property
    def get_kg(self):
        return self.__kg
    @get_kg.setter
    def set_kg(self,new_kg):
        if not(isinstance(new_kg,(int,float))):
            raise ValueError('Kg should be given only in numbers ! ')
        else:
            self.__kg=new_kg
    def get_kg(self):
        return self.__kg

# !2nd
class Country:
    def __init__(self,population):
        self.population=population
    def get(self):
        return self.population
    def set(self,new):
        self.population= new

class Russia(Country):
    pass
class Canada(Country):
    pass
class Germany(Country):
    pass


# !3rd
def show_me(first = 0, second = 0, third = 0, fourth = 0, fifth = 0, sixth = 0, seventh = 0, eighth = 0, ninth = 0, tenth = 0,*nums):
    sum = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + tenth
    for num in nums:
        sum += num
    return sum


# !4th
class TriangleCheker:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    def check_trngl(self):
        if not(isinstance(self.num1,(int,float)) or not isinstance(self.num2,(int,float)) or not isinstance(self.num3,(int,float))):
            raise TypeError('You should enter correct symbols!')
        elif self.num1 or self.num2 or self.num3 < 0:
            raise ValueError('Enter positive numbers!')
        elif (self.num1 + self.num2) <= self.num3 or (self.num1 + self.num3) <= self.num2 or (self.num3 + self.num2) <= self.num1:
            raise ValueError('One side can not be more than sum of two others!')
        else:
            print ('This triangle is possible!')







class Geek:
    def __init__(self, age = 0):
         self._age = age
      
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x
  
raj = Geek()
  
# setting the age using setter
raj.set_age(21)
  
# retrieving age using getter
print(raj.get_age())
  
print(raj._age)