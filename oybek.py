# Oybek
# This is new line in oybek.py file.

# def calcLengthOfSlice(x1, y1, x2, y2):
#     c = (x2 - x1)**2 + (y2 - y1)**2
#     return c ** 0.5



# class Car:
#     def __init__(self, объем, топливо, расход):
#         self.объем = объем
#         self.топливо = топливо
#         self.расход = расход
#     def доступное_дистанция(self):
#         a = (self.топливо/self.расход*100)
#         print("100 литр", a)
#     def доступное_дистанция2(self):
#         b = (self.топливо - self.расход)
#         c = (b / self.расход)
#         print("1 литр",c)
#     def пополнение_бака(self):
#         d = 100
#         print("Бак",d)

# Malibu = Car(100, 100, 18)
# Malibu.доступное_дистанция()
# Malibu.доступное_дистанция2()
# Malibu.пополнение_бака()   


class Car:
    def __init__(self, volume, gas_left, consumption):
        self.volume = volume
        self.gas_left = gas_left
        self.consumption = consumption

    def ride(self, distance):
        try:
            if not isinstance(distance, (float, int)):
                raise ValueError('Distance should be a number')
        except ValueError as err:
            print(err)
            return err
        
        gas_use = (distance * self.consumption) / 100
        if gas_use < self.gas_left:
            self.gas_left -= gas_use
        else:
            try:
                raise ValueError('You do not have enough fuel. Please fill in your tank')
            except ValueError as err: 
                print(err)
                return err

    def fill_tank(self , quantity):
        try:
            if not isinstance(quantity , (float , int)):
                raise ValueError("Enter a number!")
        except Exception as err:
            print(err)
            return err
        if self.gas_left + quantity < self.volume:
            self.gas_left += quantity
        else:
            try:
                raise ValueError("Too much fuil")
            except Exception as err:
                print(err)
                return err 

    def available(self):
        available_dist = (self.gas_left * 100) / self.consumption
        return (self.gas_left, available_dist)

matiz = Car(35, 25, 8)

print(matiz.gas_left)
matiz.ride(300)
print(matiz.gas_left)
matiz.ride(200)
matiz.fill_tank(19)
print(matiz.available())