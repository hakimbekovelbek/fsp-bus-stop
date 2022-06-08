

class Country:
    def __init__(self):
        pass

class Russia(Country):
    def __init__(self, population):
        self._population = population

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, new_population):
        if not(isinstance(new_population, int)):
            raise ValueError("population must be integer!!!")
        else:    
            self.population = new_population
            
class Germany(Russia):
    def __init__(self, population):
        self.population = population


class Canada(Russia):
    def __init__(self, population):
        self.population = population




        