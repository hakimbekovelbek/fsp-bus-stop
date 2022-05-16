# This line from Umarjon's laptop
# This is test message

class Car:
    def __init__(self, volume, filled, consuption):
        self.volume = volume
        self.filled = filled
        self.consuption = consuption

    def fill_tank(self):
        self.filled = self.volume
        print('Tank is filled!')
    
    def available_distance(self):
        av_distance = round(self.filled / self.consuption * 100)
        print(f'{round(self.filled)}, {av_distance} km')

    def ride(self, distance):
        if self.filled - (distance / 100 * self.consuption) < 0:
            print('You cannot ride, because you need more fuel')
        else: self.filled -= distance / 100 * self.consuption
        
        

lacetti = Car(75, 55, 15)
lacetti.fill_tank()
lacetti.available_distance()
lacetti.ride(100)
lacetti.available_distance()
phantom = Car(150, 60, 40)
phantom.available_distance()
phantom.ride(200)
phantom.available_distance()
phantom.fill_tank()
phantom.ride(200)
phantom.available_distance()

