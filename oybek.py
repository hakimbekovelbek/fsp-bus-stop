# Oybek
# This is new line in oybek.py file.

# def calcLengthOfSlice(x1, y1, x2, y2):
#     c = (x2 - x1)**2 + (y2 - y1)**2
#     return c ** 0.5



class Car:
    def __init__(self, объем, топливо, расход):
        self.объем = объем
        self.топливо = топливо
        self.расход = расход
    def доступное_дистанция(self):
        a = (self.топливо/self.расход*100)
        print("100 литр", a)
    def доступное_дистанция2(self):
        b = (self.топливо - self.расход)
        c = (b / self.расход)
        print("1 литр",c)
    def пополнение_бака(self):
        d = 100
        print("Бак",d)

Malibu = Car(100, 100, 18)
Malibu.доступное_дистанция()
Malibu.доступное_дистанция2()
Malibu.пополнение_бака()   