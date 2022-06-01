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

a = datetime.datetime.now()
x =  int(a.strftime("%H"))

hrs= datetime.datetime.now()
hours=int(hrs.strftime("%H"))

min= datetime.datetime.now()
minutes=int(min.strftime("%M"))

gettingtime=int((hours * 60) + minutes)

def get_time():
    name = input("Enter your station:")
    if name  == "Drujba":
        if x > 1:
            if gettingtime > 60:
                overall= 25-(gettingtime - (gettingtime//10)*10)
                print (f'{"100"},destination "Chorsu",{overall}')
                time = gettingtime-((gettingtime //10)*10)
                print (f'{"100"},destination "Drujba",{time}')
            else:
                print("Blyat")
        else:
            print("Buses are not available now!")

    if name  == "Samarqand Darvoza":
        if x > 1:
            if gettingtime > 60:
                overall= 20-(gettingtime - (gettingtime//10)*10)
                print (f'{"100"},destination "Chorsu",{overall}')
                time = 15-((gettingtime //10)*10)
                print (f'{"100"},destination "Drujba",{time}')
            else:
                print("Blyat")
        else:
            print("Buses are not available now!")

    elif name  == "Chorsu":
        if x > 1:
            if gettingtime > 60:
                overall= 23-(gettingtime - (gettingtime//10)*10)
                print (f'{"104"},destination "Chorsu",{overall}')
                time = gettingtime-((gettingtime //10)*10)
                print (f'{"104"},destination "Medgorodok",{time}')
                new_line= 25 -(gettingtime-((gettingtime //10)*10))
                print (f'{100},destination "Chorsu",{new_line}')
                newline=gettingtime-((gettingtime //10)*10)
                print(f'{100},destination "Drujba",{newline}')

            else:
                print("Blyat")
        else:
            print("Buses are not available now!")

    elif name  == "Tinchlik":
        if x > 1:
            if gettingtime > 60:
                overall= 18-(gettingtime - (gettingtime//10)*10)
                print (f'{"104"},destination "Chorsu",{overall}')
                time = 15-(gettingtime-((gettingtime //10)*10))
                print (f'{"104"},destination "Medgorodok",{time}')
                new_line= 20 -(gettingtime-((gettingtime //10)*10))
                print (f'{100},destination "Chorsu",{new_line}')
                newline=15-(gettingtime-((gettingtime //10)*10))
                print(f'{100},destination "Drujba",{newline}')
            else:
                print("Blyat")
        else:
            print("Buses are not available now!")

    elif name  == "Beruniy":
        if x > 1:            
            if gettingtime > 60:
                overall= 18-(gettingtime - (gettingtime//10)*10)
                print (f'{"104"},destination "Chorsu",{overall}')
                time = 15-(gettingtime-((gettingtime //10)*10))
                print (f'{"104"},destination "Medgorodok",{time}')
            else:
                print("Blyat")
        else:
            print("Buses are not available now!")

    elif name  == "Medgorodok":
        if x > 1:
            if gettingtime > 60:
                overall= 23-(gettingtime - (gettingtime//10)*10)
                print (f'{"104"},destination "Medgorodok",{overall}')
                time = gettingtime-((gettingtime //10)*10)
                print (f'{"104"},destination "Chorsu",{time}')
            else:
                print("Blyat")
        else:
            print("Buses are not available now!")
    else:
        print("You entered incorect name !")

get_time()  

                
            

            

