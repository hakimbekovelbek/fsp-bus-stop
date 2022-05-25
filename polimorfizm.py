

class Sky_object:
    def __init__(self, name):
        self.name = name

class Star(Sky_object):
    def __init__(self,name, color):
        Sky_object.__init__(name)
        self.color = color

class Planet(Sky_object):
    def __init__(self,name, type, mass):
        Sky_object.__init__(self, name)
        self.type = type
        self._mass = mass

    def rotate(self):
        print(f'{self.name} is rotating ... ')

    @property
    def mass(self):
        return self._mass
    @mass.setter
    def mass(self,new_mass):
        if not(isinstance(new_mass, int)):
            raise ValueError('Mass ought to be int')
        self._mass = new_mass   
    
class Satelitte(Sky_object):
    def __init__(self,name):
        Sky_object.__init__(self,name)
        self.name = name
        
earth = Planet('earth', 'solid', int(5.97e21))      
print(earth.mass)
class EarthPlsnet(Sky_object):
    def __init__(self,name):
        Sky_object.__init__(self,name)



earth = Planet('Earth', 'solid')
earth.rotate()


