
import datetime
time = datetime.datetime.now()

def cur_time(datetime):
    hours = int(datetime.strftime("%H"))
    mins = int(datetime.strftime('%M'))
    if hours == 0 or hours == 1:    
        return (hours + 24) * 60 + mins
    else:
        return hours * 60 + mins


def get_stations(file):
    stations = {}
    with open(file, 'r', encoding='utf-8') as rf:
        while True:
            line = rf.readline().strip().split(';')
            if len(line) < 2:
                break
            stations.update({line[0] : int(line[1])})
        return stations



def bus_arrive(station, cur_time, stations):
    print(f'Now is {time.strftime("%H")} : {time.strftime("%M")} ')
    interval_81 = 15
    interval_93 = 10
    if 1500 > cur_time > 60:
        if station == "E":
            arrive_time = interval_81 - (cur_time % interval_81)
            print(f'81, destination "F", {arrive_time} min')

        elif station == "F":
            arrive_time = interval_81 - (cur_time % interval_81)
            print(f'81, destination "E", {arrive_time} min')
        
        elif station == "A":
            spend_time_to_E = stations['F'] + stations['A']
            spend_time_to_F = stations['E']
            arrive_time = interval_93 - (cur_time % interval_93)
            print(f'93, destination "D", {arrive_time} min')
            arrive_time = interval_81 - (cur_time % interval_81) + spend_time_to_E
            if arrive_time >= interval_81:
                arrive_time -= interval_81
            print(f'81, destination "E", {arrive_time} min')
            arrive_time = interval_81 - (cur_time % interval_81) + spend_time_to_F
            if arrive_time >= interval_81:
                arrive_time -= interval_81
            print(f'81, destination "F", {arrive_time} min')
        
        elif station == "B":
            spend_time_to_E = stations['F']
            spend_time_to_F = stations['E'] + stations['A']
            spend_time_to_A = stations['C'] + stations['B']
            spend_time_to_D = stations['A']
            arrive_time = interval_93 - (cur_time % interval_93) + spend_time_to_D
            if arrive_time >= interval_93:
                arrive_time -= interval_93
            print(f'93, destination "D", {arrive_time} min')
            arrive_time = interval_93 - (cur_time % interval_93) + spend_time_to_A
            if arrive_time >= interval_93:
                arrive_time -= interval_93
            print(f'93, destination "A", {arrive_time} min')
            arrive_time = interval_81 - (cur_time % interval_81) + spend_time_to_E
            if arrive_time >= interval_81:
                arrive_time -= interval_81
            print(f'81, destination "E", {arrive_time} min')
            arrive_time = interval_81 - (cur_time % interval_81) + spend_time_to_F
            if arrive_time >= interval_81:
                arrive_time -= interval_81
            print(f'81, destination "F", {arrive_time} min')
        
        elif station == "C":
            spend_time_to_A = stations['D']
            spend_time_to_D = stations['A'] + stations['B']
            arrive_time = interval_93 - (cur_time % interval_93) + spend_time_to_A
            if arrive_time >= interval_93:
                arrive_time -= interval_93
            print(f'93, destination "A", {arrive_time} min')
            arrive_time = interval_93 - (cur_time % interval_93) + spend_time_to_D
            if arrive_time >= interval_93:
                arrive_time -= interval_93
            print(f'93, destination "D", {arrive_time} min')

        elif station == "D":
            arrive_time = interval_93 - (cur_time % 10)
            print(f'93, destination "A", {arrive_time} min')
        
        else:
            print('Please enter correct station!')
            return

    else:
        print("Buses are not available now!")
        return


def start_programm():
    stations = get_stations('stations.txt')
    while True:
        station = input("Enter your station:")
        current_time = cur_time(time)
        if station in stations.keys():
            bus_arrive(station, current_time, stations)
        else:
            print('Please enter correct station')
start_programm()
