class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg
    
    @property
    def kg(self):
        return self.__kg * 2.205
    

    @kg.setter
    def kg(self, new_kg):
        if not isinstance(new_kg, (int, float)):
            raise ValueError('Килограммы задаются только числами')
        self.__kg = new_kg
   

weight = KgToPounds(45)
print(weight.kg)
