class Country:
    def init (self, population):
        self.population = population

class Russia (Country):
    def __init__(self, population ) :
        Country.__init__(self, population)

    def setPopulation(self):
        return self._population

    
    def getPopulation(self, set_population):
        if set_population <= 0 or isinstance(set_population, str):
            print('ошибка')
        else:
            self._population = set_population

    
class Canada(Country):
    def __init__(self, population ) :
        Country.__init__(self, population)

    def setPopulation(self):
        return self._population

    
    def getPopulation(self, set_population):
        if set_population <= 0 or isinstance(set_population, str):
            print('ошибка')
        else:
            self._population = set_population

class Germany(Country):
    def __init__(self, population ) :
        Country.__init__(self, population)

    def setPopulation(self):
        return self._population

    
    def getPopulation(self, set_population):
        if set_population <= 0 or isinstance(set_population, str):
            print('ошибка')
        else:
            self._population = set_population


german = Germany(83_240_000)
russia= Russia(144_100_000)
canada = Canada(38_010_000)
print(german.population)
print(russia.population)
print(canada.population)