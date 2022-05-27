# 1
class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205
    
    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError("Килограммы задаются только числами")

d = KgToPounds(15)
d.kg = 1
#print(d.kg)

# 2
class Country:
    pass

class Russia(Country):
    def __init__(self, population):
        self.__population = population

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, new_population):
        if isinstance(new_population, (int, float)):
            self.__population = new_population
        else:
            raise ValueError()

class Canada(Country):
    def __init__(self, population):
        self.__population = population

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, new_population):
        if isinstance(new_population, (int, float)):
            self.__population = new_population
        else:
            raise ValueError()

class Germany(Country):
    def __init__(self, population):
        self.__population = population

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, new_population):
        if isinstance(new_population, (int, float)):
            self.__population = new_population
        else:
            raise ValueError()

germany = Germany(150)
germany.population = 156
print(germany.population)

# 3
def show_me(*args, **kwargs):
    return sum(kwargs.values()) + sum(args)

#print(show_me(10,20,30,40,50, 1, second = 20, first = 10))

# 4
class TraingleChekker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_traingle(self):
        if isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c, (int, float)):
            pass
        else:
            return "Нужно вводить только числа"

        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет"
        
        elif  self.b < self.a > self.c or self.a < self.b + self.c or self.b < self.a + self.c or self.c < self.a + self.c:
            return "Ура, можно построить треугольник."
        
        else:
            return "Жаль, из этого треугольник не сделать"
        

a = TraingleChekker(5,5,8)
#print(a.is_traingle())