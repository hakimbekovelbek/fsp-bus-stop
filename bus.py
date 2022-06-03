class BusStation:
    def __init__(self, bus, place, time):
        self.bus = bus
        self.place = place 
        self.time = time

class B(BusStation):
    def __init__(self, bus, place, time):
        BusStation.__init__(self, bus, place, time)

    def st(self):
        return f'437, destination E, 0 min'

class A(BusStation):
    def __init__(self, bus, place, time):
        BusStation.__init__(self, bus, place, time)

    def st(self): 
        return f'437, destination E, 1 min'
