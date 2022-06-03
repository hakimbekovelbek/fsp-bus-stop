import datetime

class Station:
    start_time = 18000
    end_time  = 3600
    koef = 10
    def get_time(self , time , start_time , end_time , koef , spend_time):
        hour = time.split(':')
        timess = (int(hour[0]) * 3600 + int(hour[1]))
        if timess < start_time and timess > 3600:
            return f"Sorry but we don't work"
        else:
            times = timess % koef 
            all_time = koef - times  + spend_time
            return all_time
class A(Station):
    number = 1
    spend_time = 3
class B(Station):
    number = 2
    spend_time = 4
class D(Station):
    number = 3
    spend_time = 5
class E(Station):
    number = 1
    koef = 5
    spend_time = 5
class F(Station):
    number = 2
    koef = 5
    spend_time = 2
class G(Station):
    number = 3
    koef = 5
    spend_time = 4
class TimeTable():
    def __init__(self , station1 , station2 , station3 , time):
        self.station1 = station1
        self.station2 = station2
        self.station3 = station3
        self.time = time
    def get_table(self):
        time = self.time
        start_working = self.station1.start_time 
        end_working = self.station1.end_time
        bus_arrive_for = self.station1.koef
        if self.station1.number== 1 or self.station1.number == 3:
            spend_time = self.station1.spend_time
            spend_time2 = self.station2.spend_time + self.station3.spend_time
        else:
            spend_time = self.station1.spend_time + self.station2.spend_time
            spend_time2 = self.station1.spend_time+self.station3.spend_time
        times = [self.station1.get_time(time , start_working , end_working , bus_arrive_for , spend_time)]
        times.append(self.station1.get_time(time , start_working , end_working , bus_arrive_for , spend_time2))
        return times

a = A()
b = B()
d = D()
e = E()
f = F()
g = G()
while True:
    date = datetime.datetime.today()
    time = date.strftime('%H:%M')
    station = input('Enter a station: ')
    if station == 'A':
        timetable = TimeTable(a, b , d , time)
        print(f"1 ,destination D , {timetable.get_table()[0]}min")
        print(f"1 , destination A , {timetable.get_table()[1]}min")
    elif station == 'B':
        timetable = TimeTable(b, a , d , time)
        print(f"destination D , {timetable.get_table()[0]}min")
        print(f"destination A , {timetable.get_table()[1]}min")
    elif station == 'D':
        timetable = TimeTable(d, a , b , time)
        print(f"destination D , {timetable.get_table()[0]}min")
        print(f"destination A , {timetable.get_table()[1]}min")
    elif station == 'E':
        timetable = TimeTable(e, f , g , time)
        print(f"2 , destination G , {timetable.get_table()[0]}min")
        print(f"2 , destination E , {timetable.get_table()[1]}min") 
    elif station == 'F':
        timetable = TimeTable(f, e , g , time)
        print(f"2 , destination G , {timetable.get_table()[0]}min")
        print(f"2 , destination E , {timetable.get_table()[1]}min")
    elif station == 'G':
        timetable = TimeTable(g, e , f , time)
        print(f"2 , destination G , {timetable.get_table()[0]}min")
        print(f"2 , destination E , {timetable.get_table()[1]}min")
    else:
        print('You entered incorrect station please try again!')
