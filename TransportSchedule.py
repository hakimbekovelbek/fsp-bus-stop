import datetime
a = datetime.datetime.now()
b =  int(a.strftime("%H"))
c = datetime.datetime.now()
hours = int(c.strftime("%H"))
d = datetime.datetime.now()
minutes=int(d.strftime("%M"))
gettingtime=int((hours * 60) + minutes)

def get_time():
    while True:
        name = input("Enter your station:")
        print (f'Now is the time - {hours} : {minutes} ')
        if name  == "Toshkent":
            if b > 1:
                overall = 15 - (gettingtime - (gettingtime//10)*10)
                print (f'Route - 437, station - "Kosmonavtlar", {overall} minutes')
                time = gettingtime-((gettingtime //10)*10)
                print (f'Route - 437, station - "Toshkent", {time} minutes')   
            else:
                print("No buses yet!")

        if name  == "Oybek":
            if b > 1:
                overall = 18 - (gettingtime - (gettingtime//10)*10)
                print (f'Route - 437, station - "Kosmonavtlar", {overall} minutes')
                time = 16 - ((gettingtime //10)*10)
                print (f'Route - 437, station - "Toshkent", {time} minutes')
            else:
                print("No buses yet!")

        elif name  == "Kosmonavtlar":
            if b > 1:
                overall = 19 - (gettingtime - (gettingtime//10)*10)
                print (f'Route - 104, station - "Kosmonavtlar", {overall} minutes')
                time = gettingtime-((gettingtime //10)*10)
                print (f'Route - 104, station -"Gafur Gulom", {time} minutes')
                new_line = 20 - (gettingtime-((gettingtime //10)*10))
                print (f'Route - 437, station - "Kosmonavtlar", {new_line} minutes')
                new_line = gettingtime-((gettingtime //10)*10)
                print(f'route - 437, station - "Toshkent", {new_line} minutes')
            else:
                print("No buses yet!")

        elif name  == "Ozbekiston":
            if b > 1:
                overall = 20 - (gettingtime - (gettingtime//10)*10)
                print (f'Route - 104, station - "Kosmonavtlar", {overall} minutes')
                time = 25 - (gettingtime-((gettingtime //10)*10))
                print (f'Route - 104, station - "Gafur Gulom", {time} minutes')
                new_line = 15 - (gettingtime-((gettingtime //10)*10))
                print (f'Route - 437, station - "Kosmonavtlar", {new_line} minutes')
                new_line = 17 - (gettingtime-((gettingtime //10)*10))
                print(f'Route - 437, station - "Toshkent", {new_line} minutes')
            else:
                print("No buses yet!")

        elif name  == "Alisher Navoi":
            if b > 1:            
                overall = 20 - (gettingtime - (gettingtime//10)*10)
                print (f'Route - 104, station - "Alisher Navoi", {overall} minutes')
                time = 17 - (gettingtime-((gettingtime //10)*10))
                print (f'Route - 104, station - "Gafur Gulom", {time} minutes')
            else:
                print("No buses yet!")

        elif name  == "Gafur Gulom":
            
            if b > 1:
                overall = 20 - (gettingtime - (gettingtime//10)*10)
                print (f'Route - 104, station - "Alisher navoi", {overall} minutes')
                time = 15 - (gettingtime - ((gettingtime //10)*10))
                print (f'Route - 104, station "Gafur Gulom", {time} minutes')
            else:
                print("No buses yet!")
        else:
            print("You entered the wrong station!")

get_time()