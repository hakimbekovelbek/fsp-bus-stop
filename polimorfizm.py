

class Sky_object:
    def __init__(self, name):
        self.name = name

class Star(Sky_object):
    def __init__(self,name, color):
        Sky_object.__init__(name)
        self.color = color

class Planet(Sky_object):
    def __init__(self,name, type):
        Sky_object.__init__(self, name)
        self.type = type

    def rotate(self):
        print(f'{self.name} is rotating ... ')

class Satelitte(Sky_object):
    def __init__(self,name):
        Sky_object.__init__(self,name)
        self.name = name

    def get_mass(self):
        pass

class EarthPlsnet(Sky_object):
    def __init__(self,name):
        Sky_object.__init__(self,name)



# earth = Planet('Earth', 'solid')
# earth.rotate()


