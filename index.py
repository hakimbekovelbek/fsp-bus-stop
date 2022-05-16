class Car:
    def __init__(self, max_s, left, cons):
        self.max_s = max_s 
        self.left = left
        self.cons = cons
        self.s = 0


    def fill_tank(self):
        self.left = self.max_s
        print(self.left)
    

    def ride(self, ride):
        self.s = self.s + ride
        self.left -= self.cons / 100 * ride
        print(int(self.left))
    

    def available_distant(self):
        a = self.left / self.cons * 100
        print(f"{int(self.left)}, {int(a)}км")


def car(max_s, left, cons):
    a = input("1.Fill tank, 2.Ride, 3.Available distant: ")
    if a == '1':
        left = max_s
        print(left)
    elif a == '2':
        ride = int(input(": "))
        s = 0
        s = s + ride
        left -= cons / 100 * ride
        print(int(left), ',', s)
    elif a == '3':
        b = left / cons * 100
        print(f"{int(left)}, {int(b)}км")

