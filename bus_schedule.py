from cgi import print_form
import datetime

import datetime
import datetime
from time import strftime

# !Plan
# ?            [baza]->{Drujba}--
# ?                            -- 5 min
# ?                            --
# ?                            -{samarqand darvoza} -
# ?                                                --
# ?                                                -- 15 min
# ?                                                --
# ?                                                --
# ? schedule in plan [baza]-{Chorsu}<-->5min<-->{Tinchlik}<--10min-->{Beruniy}<--8min-->{Medgorodok}-[baza]

# ! Working time- 5:00 ; 00:00

hrs= datetime.datetime.now()
hours=int(hrs.strftime("%H"))

min= datetime.datetime.now()
minutes=int(min.strftime("%M"))

gettingtime=int((hours * 60) + minutes)

def get_time():
    while True:
        name = input("Enter your station:")
        print (f'Now is {hours} : {minutes} ')
        if name  == "Drujba":
            if 300<gettingtime<0:
                overall= 25-(gettingtime - (gettingtime//10)*10)
                print (f'{"100"},destination "Chorsu",{overall}')
                time = gettingtime-((gettingtime //10)*10)
                print (f'{"100"},destination "Drujba",{time}')   
            else:
                print("Buses are not available now!")

        elif name  == "Samarqand Darvoza":
            if 300<gettingtime<0:
                overall= 20-(gettingtime - (gettingtime//10)*10)
                print (f'{"100"},destination "Chorsu",{overall}')
                time = 15-((gettingtime //10)*10)
                print (f'{"100"},destination "Drujba",{time}')
            else:
                print("Buses are not available now!")

        elif name  == "Chorsu":
            if 300<gettingtime<0:
                overall= 23-(gettingtime - (gettingtime//10)*10)
                print (f'{"104"},destination "Chorsu",{overall}')
                time = gettingtime-((gettingtime //10)*10)
                print (f'{"104"},destination "Medgorodok",{time}')
                new_line= 25 -(gettingtime-((gettingtime //10)*10))
                print (f'{"100"},destination "Chorsu",{new_line}')
                newline=gettingtime-((gettingtime //10)*10)
                print(f'{"100"},destination "Drujba",{newline}')
            else:
                print("Buses are not available now!")

        elif name  == "Tinchlik":
            if 300<gettingtime<0:
                overall= 18-(gettingtime - (gettingtime//10)*10)
                print (f'{"104"},destination "Chorsu",{overall}')
                time = 15-(gettingtime-((gettingtime //10)*10))
                print (f'{"104"},destination "Medgorodok",{time}')
                new_line= 20 -(gettingtime-((gettingtime //10)*10))
                print (f'{100},destination "Chorsu",{new_line}')
                newline=15-(gettingtime-((gettingtime //10)*10))
                print(f'{100},destination "Drujba",{newline}')
            else:
                print("Buses are not available now!")

        elif name  == "Beruniy":
            if 300<gettingtime<0:            
                overall= 18-(gettingtime - (gettingtime//10)*10)
                print (f'{"104"},destination "Chorsu",{overall}')
                time = 15-(gettingtime-((gettingtime //10)*10))
                print (f'{"104"},destination "Medgorodok",{time}')
            else:
                print("Buses are not available now!")

        elif name  == "Medgorodok":

            if 300<gettingtime<0:
                overall= 23-(gettingtime - (gettingtime//10)*10)
                print (f'{"104"},destination "Medgorodok",{overall}')
                time = gettingtime-((gettingtime //10)*10)
                print(f'{"104"},destination "Chorsu",{time}')
            else:
                print("Buses are not available now!")
        else:
            print("You entered incorect name !")

get_time()  