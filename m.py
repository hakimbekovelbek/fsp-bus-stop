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
            raise ValueError('Килограммы задаются только числами')
 
 
class Country:
    def __init__(self, name, population, area, coastline = 0):
        self.name = name
        self.population = population
        self.area = area
        self.coastline = coastline

    def __repr__(self):
        return (
          f"Country(name={self.name!r}, population={self.population!r},"
          f" coastline={self.coastline!r})"
        )

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return  (
                (self.name, self.population, self.coastline)
                == (other.name, other.population, other.coastline)
            )
        return NotImplemented

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return ((self.name, self.population, self.coastline) < (
                other.name, other.population, other.coastline
            ))
        return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return ((self.name, self.population, self.coastline) <= (
                other.name, other.population, other.coastline
            ))
        return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return ((self.name, self.population, self.coastline) > (
                other.name, other.population, other.coastline
            ))
        return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return ((self.name, self.population, self.coastline) >= (
                other.name, other.population, other.coastline
            ))
        return NotImplemented

    def beach_per_person(self):
        """Meters of coastline per person"""
        return (self.coastline * 1000) / self.population


class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'
 
triangle1 = TriangleChecker([2, 3, 4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([77, 3, 4])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())


class Num:
    def __init__(self, num):
        self.num = num

    def show_my_drink(self):
        if self.num:
            print(f'First={self.num}')
        else:
            print('None')
num1 = Num()
num1 = Num('first')
num1 - Num(1)


 

