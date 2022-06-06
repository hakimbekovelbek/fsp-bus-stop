from datetime import datetime

current_datetime = datetime.now()

class Time:
    @property
    def time(self):
        current_time = current_datetime.strftime("%H:%M")
        return current_time  

    def time_in_minutes(self):
        h = current_datetime.strftime("%H")
        m = current_datetime.strftime("%M")
        return int(h) * 60 + int(m)
               

class Bus:
    def __init__(self, number_bus):
        self.number_bus = number_bus
    
    def stops(self, a, b, c):
        self.stop_a = a
        self.stop_b = b
        self.stop_c = c

    def work_mode(self, fr, to):
        fr_t = (int(fr[:2]) * 60) + int(fr[3:])
        to_t = (int(to[:2]) * 60) + int(to[3:])
        self.fr_t = fr_t
        self.to_t = to_t    

    def distance_between_stops(self, ab, bc):
        self.ab = int(ab)
        self.bc = int(bc)
        self.ac = int(ab) + int(bc)

    def show_bus(self, stop):
        t = int(time.time_in_minutes())
        if stop == self.stop_a:
            if t % 10 == 0:
                bus_loc = self.stops[0]
                m = 0
            elif t % 10 <= self.ab:
                bus_loc = self.stops[1]
                m = self.ab - t % 10
            else:
                bus_loc = self.stops[2]
                m = 10 - t % 10
            
        elif stop == self.stop_b:
            if t % 10 == 0:
                bus_loc = self.stops[0]
                m = self.ab
            elif t % 10 <= self.ab:
                bus_loc = self.stops[1]
                m = self.ab - t % 10
            
            else:
                bus_loc = self.stops[2]
                m = self.ac - t % 10
        
        elif stop == self.stop_c:
            if t % 10 == 0:
                bus_loc = self.stops[0]
                m = self.ac
            elif t % 10 <= self.ab:
                bus_loc = self.stops[1]
                m = self.ac - t % 10
            
            else:
                bus_loc = self.stops[2]
                m = self.ac - t % 10
        

        if t > self.to_t and t > self.fr_t:
            return  [m,f"{self.number_bus}, destination {bus_loc}, {m} min"]


def bus_stop():
    while True:
        try:
            stop = input("Enter stop: ")
            print(f"Current time: {time.time}")
            print("Schedule:")
            busses = [bus1.show_bus(stop), bus2.show_bus(stop), bus3.show_bus(stop)]
            busses.sort()
            for i in busses:
                print(i[1])
        except:
            print("No such stop")
            continue


def read():
    with open('data.txt', 'r', encoding='utf-8') as file:
        line = file.readlines()
    
    for i in range(len(line)):
        line[i] = line[i].strip().split(';')
    
    return line


time = Time()
l = read()

bus1 = Bus(l[0][0])
bus2 = Bus(l[1][0])
bus3 = Bus(l[2][0])

bus1.work_mode(l[0][4], l[0][5])
bus2.work_mode(l[1][4], l[1][5])
bus3.work_mode(l[2][4], l[2][5])

bus1.stops(l[0][1], l[0][2], l[0][3])
bus2.stops(l[1][1], l[1][2], l[1][3])
bus3.stops(l[2][1], l[2][2], l[2][3])

bus1.distance_between_stops(l[0][6], l[0][7])
bus2.distance_between_stops(l[1][6], l[1][7])
bus3.distance_between_stops(l[2][6], l[2][7])

bus_stop()