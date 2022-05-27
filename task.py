class KgToPounds:

    def __init__(self, kg) -> None:
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg * 2.205 
    
    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            raise ValueError('киллограмы задаются только числами')
        self.__kg = new_kg
           



weight = KgToPounds(4)
print(weight.kg)