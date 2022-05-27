class SkyObject:
    def __init__(self, name):
        self.name = name

class Star:
    def __init__(self, name, color):
        SkyObject.__init__(self, name)
        self.color = color

class Planet(SkyObject):
    def __init__(self, name, type, mass):
        SkyObject.__init__(self, name)
        self.type =type
        self.mass = mass

    def rotate(self):
        print(f'{self.name} is rotating...')

    #getter
    @property #decorator
    def get_mass(self):
        return self.mass

    # setter
    @mass.setter #decorator
    def mass(self, new_mass):
        if not(isinstance(new_mass, int)):
            raise ValueError('Mass should be integer')
        self._mass = new_mass

class Satellite(SkyObject):
    def __init__(self, name):
        SkyObject.__init__(name)


earth = Planet('Earth', 'solid', int(5.97e21))
print(earth.mass)

# class EarthPlanet(Planet):
#     def __init__(self, name, type, mass):
#         Planet.__init__(self, name, type, mass)