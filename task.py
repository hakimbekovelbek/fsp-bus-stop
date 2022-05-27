from tabnanny import check


class KgToPounds:
    def __init__(self , kg): # конструктор принимает 1 аргумент
        self.__kg = kg
    def to_pounds(self): # метод переводящий в футы 
        return self.__kg * 2.205
    @property # тут set_kg получивший свойство изменять пожход деалет set_kg setter 
    def get_kg(self):
        return self.__kg
    @get_kg.setter
    def set_kg(self , new_kg):# декоратор property изменят подход метода делая его setter
        if (isinstance(new_kg , (int , float))):
            self.__kg = new_kg
        else:
            raise TypeError('Килограммы задаются только числами')

    
kg = KgToPounds(12)
kg = 'a' # тут setter
print(kg) # тут у нас getter
# ! Решение 1й задачи
class Country:
    @property
    def get_population(self):
        return self.population
    get_population.setter
    def set_population(self , new_population):
        try:
            if (isinstance(new_population , (int , float))):
                self.population = new_population
                return
            else:
                raise ValueError('Population must be  a number')
        except  Exception as err:
            return err
class Russia(Country):
    population = 0
class Canada(Country):
    population = 100
class Germany(Country):
    population = 200
rus = Russia()
rus = 150
print(rus)
def show_me(first = 0, second  = 0,third = 0 , fourth = 0, *nums):
    sum = first + second + third + fourth
    for i in nums:
        sum += i
    print( sum)
show_me(10 , 20 , 30)
show_me(10 , second = 20 , third = 30)
class TriangleChacker:
    def is_triangle(self ,angle1 , angle2 , angle3):
        angles = [angle1 , angle2 , angle3]
        for i in angles:
            if isinstance(i , (int , float)):
                pass
            else:
                return 'Нужно вводить только числа!'
        for i in angles:
            if i <0:
                return 'С отрицательными числами ничего не выйдет'
        if angle1 + angle2 <= angle3:
            return 'Жаль, но из этого треугольник не сделать'
        if angle2 + angle3<=angle1:
            return 'Жаль, но из этого треугольник не сделать'
        if angle1 +angle3 <= angle2:
            return 'Жаль, но из этого треугольник не сделать'
        return 'Ура, можно построить треугольник'
check = TriangleChacker()    
print(check.is_triangle(-1 , 2 , 3))
print(check.is_triangle(1 , 2 , 3))
print(check.is_triangle('a' , 2 , 3))



