from datetime import datetime
dt = datetime.now()


class Time:
    current_time = f'{dt.hour}:{dt.minute}'
    @staticmethod
    def default_info():
        return f'Current time: {Time.current_time}'
    
    def current_time_in_minutes(self):
        return int(dt.hour)*60 + int(dt.minute)

    
        
your_station = input('Enter station: ') 
print(Time.default_info())      
print('Schedule: ')

class BusRoute:
    def __init__(self, route_num, station1, station2, station3, station4):
        self.route_num = route_num
        self.station1 = station1
        self.station2 = station2
        self.station3 = station3
        self.station4 = station4
    
    def work_time(self, hour_start, minute_start, hour_end, minute_end, frequency):
        self.hour_start = hour_start
        self.minute_start = minute_start
        self.hour_end = hour_end
        self.minute_end = minute_end
        self.frequency = frequency

    def work_hours(self):
        self.work_time = ((24*60)-1 - ((self.hour_start*60 + self.minute_start)- (self.hour_end*60 + (self.minute_end+self.frequency))))

        if (self.hour_end*60 + (self.minute_end+self.frequency)) < Time.current_time_in_minutes(self) <= (self.hour_start*60 + self.minute_start):
            return 'It is too late. Buses do not work now'
        


    def intervals(self, st1_st2: int, st2_st3: int, st3_st4: int):
        self.st1_st2 = st1_st2
        self.st2_st3 = st2_st3
        self.st3_st4 = st3_st4
        self.st1_st3 = self.st1_st2 + self.st2_st3
        self.st2_st4 = self.st2_st3 + self.st3_st4
        self.st1_st4 = self.st1_st2 + self.st2_st3 + self.st3_st4

    def schedule(self):
        if your_station == self.station1:
            
            if time % 10 == 0:
                minutes_left = 0
            elif time % 10 > 0 and time % 10 <= self.st1_st2:
                # minutes_left = time - (time % 10) + self.frequency
                minutes_left = self.st1_st2 - time % 10
            elif time % 10 > self.st1_st2 and time % 10 <= self.st2_st4:
                minutes_left = self.st2_st4 - time % 10
            elif time % 10 > self.st1_st3 and time % 10 <= self.st1_st4:
                minutes_left = self.st1_st4 - time % 10

        if your_station == self.station2:
            
            if time % 10 == 0:
                minutes_left = 0
            elif time % 10 > 0 and time % 10 <= self.st1_st2:
                minutes_left = self.st1_st2 - time % 10
            elif time % 10 > self.st1_st2 and time % 10 <= self.st2_st4:
                minutes_left = self.st2_st4 - time % 10
            elif time % 10 > self.st1_st3 and time % 10 <= self.st1_st4:
                minutes_left = self.st1_st4 - time % 10

        if your_station == self.station3:
            
            if time % 10 == 0:
                minutes_left = 0
            elif time % 10 > 0 and time % 10 <= self.st1_st2:
                minutes_left = self.st1_st2 - time % 10
            elif time % 10 > self.st1_st2 and time % 10 <= self.st2_st4:
                minutes_left = self.st2_st4 - time % 10
            elif time % 10 > self.st1_st3 and time % 10 <= self.st1_st4:
                minutes_left = self.st1_st4 - time % 10
        
        if your_station == self.station4:
            
            if time % 10 == 0:
                minutes_left = 0
            elif time % 10 > 0 and time % 10 <= self.st1_st2:
                minutes_left = self.st1_st2 - time % 10
            elif time % 10 > self.st1_st2 and time % 10 <= self.st2_st4:
                minutes_left = self.st2_st4 - time % 10
            elif time % 10 > self.st1_st3 and time % 10 <= self.st1_st4:
                minutes_left = self.st1_st4 - time % 10

        return f'{self.route_num}, destination {self.station4}, {minutes_left} min'

t = Time()
time = t.current_time_in_minutes()


route437_stations = BusRoute(437, 'E', 'A', 'B', 'F') 
route104_stations = BusRoute(104, 'A', 'B', 'C', 'D')

route104_stations.work_time(5, 00, 1, 00, 10)
route437_stations.work_time(5, 10, 1, 30, 5)


route104_stations.intervals(3, 5, 4)
route437_stations.intervals(6, 3, 5)

print(route104_stations.schedule())
print(route437_stations.schedule())
