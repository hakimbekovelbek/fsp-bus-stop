
#  ! oybek -> 10 to Sebzar
#  ! sebzar -> 3 to Ations friendship
#  ! Nations friendship -> 5 to novza
#  ! novza -> 4 
#  working time from 5:00 to 23:00 


from datetime import datetime

hour = datetime.now()
hrs = int(hour.strftime("%H"))

min = datetime.now()
mins= int(min.strftime("%M"))

get_time = int(hrs * 60 + mins) 

def bus_coming_time():
    while True :
        station = input(str.lower("please enter your current station: "))
        print(f"time: {hrs}:{mins} ")
        
        if station == "oybek":
            if 180 < get_time < 1380:
                time = get_time-(get_time%10)
                print(f"{85}, station ' oybek', {time}")
            else :
                print("buses are not availale")
        
        if station == "sebzor":
            if 180 < get_time < 1380:
                time = 18 - (get_time%10)
                print(f"{85}, station 'sebzor', {time}")            
            else :
                print("buses are not availale")
        
        if station == "nations friendship":
            if 180<get_time<1380:
                time = 21 -(get_time%10)
                print(f"{85}, station 'antions friendship', {time}")
            else:
                print("Sorry buses are not available")  
        if station == "novza":
            if 180<get_time<1380:
                time = 26 - (get_time%10)
                print(f"{85}, station 'novza', {time}")
            else :
                print("Sorry buses are not available")



bus_coming_time()                              

                



