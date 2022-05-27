class Country:
    def __init__(self, population):
        self.population = population
    
class Russia(Country):
    def __init__(self, population):
         Country.__init__(self, population)
         
        
    def setPopulation(self, set_population):
        self._population = set_population


    def getPopulation(self):
        return self._population


    

class Canada(Country):
    def __init__(self, population):
         Country.__init__(self, population)
        
    
    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, set_population):
        self._population = set_population

class Germany(Country):
    def __init__(self, population):
         Country.__init__(self, population)
        
    
    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, set_population):
        self._population = set_population

german = Germany(83_240_000)    
russian= Russia(144_100_000)
canadian = Canada(38_010_000)
print(russian.population)
print(canadian.population)
print(german.population)