import datetime

list = ['A', 'B', 'C', 'D']
times = [3, 5, 4]

class Show_Time:
    def __init__(self, station):
        self.station = station

    def current_time(self):
        current_time = datetime.datetime.now()
        print(f'Current time: {current_time.hour}:{current_time.minute}')
        
    def destinations(self):
        current_time = datetime.datetime.now()
        if 300> current_time.hour * 60 > 60:
            print('There is no bus at this time')
        else:
            for st in list:
                if not st == self.station:
                    try:
                        ValueError('Enter only existing stations')
                    except ValueError as err:
                        return err
                else:
                    if self.station == list[-1]:
                        index = list.index(self.station) - (list.index(self.station) + 1 )
                        left_time = times[-1] - ((((current_time.hour * 60) + current_time.minute)% 10) % times[index - 1]) 
                        return f'Destination: {list[index - 1]}: {left_time}min'
                    elif self.station == list[0]:
                        index = list.index(self.station)
                        current_time = datetime.datetime.now()
                        left_time = times[0] - ((((current_time.hour * 60) + current_time.minute)% 10) % times[index]) 
                        return f'Destination: {list[index + 1]}: {left_time}min'
                    else:
                        index = list.index(self.station)
                        current_time = datetime.datetime.now()
                        left_time_c = (times[index] + times[index - 1]) - ((((current_time.hour * 60) + current_time.minute)% 10) % times[index]) 
                        left_time_b = (times[index] + times[index + 1]) - ((((current_time.hour * 60) + current_time.minute)% 10) % times[index -1]) 
                        return f'Destination: {list[index - 1]}:{left_time_b}min;\nDestination: {list[index + 1]}:{left_time_c}min'



a = input('Enter station: ')
left_time = Show_Time(a)
print(left_time.destinations())
