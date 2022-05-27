

class Kg_to_pouds:

    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg


    def to_pounds(self):
        return self.__kg * 2.20462

        
    @kg.setter
    def set_kg(self, new_kg):
        if not(isinstance(new_kg, (int, float))):
            raise ValueError("kilogramms must be numbers")
        else:
            self.__kg = new_kg
    def get_kg(self):
        return self.__kg

m = Kg_to_pouds(15)
m.set_kg()
print(m.get_kg())








