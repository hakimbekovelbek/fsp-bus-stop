import datetime

a = datetime.datetime.now()
z = int(a.strftime('%H'))

hour = datetime.datetime.now()
hrs = int(hour.strftime('%H'))

minute = datetime.datetime.now()
min = int(minute.strftime('%M'))

gt = int((hrs*60) + min)

def bus_stop():

    loc = input('enter station - ')

    if loc == 'beruniy':
        if z > 1:
            if gt>60:
                o = 29 - ((gt - (gt//10) * 10 ))
                print((f'{"104"}, destination "beruniy" {o}'))
                t =  gt - (gt//10) * 10 
                print((f'{"434"}, destination "beruniy" {o}'))
            else:
                print('nothing found')
        else:
            print('nothing')

    elif loc == 'buyuk ipak yoli':
            
            if z > 1:
                if gt>60:
                    o = 26 - ((gt - (gt//10) * 10 ))
                    print((f'{"1"}, destination "beruniy" {o}'))
                    t = ((gt - (gt//10) * 10 ))
                    print((f'{"58"}, destination "beruniy" {o}'))
                else:
                    print('nothing found')
    elif loc == 'alisher navoiy':
            
        if z > 1:
            if gt>60:
                o = 23 - ((gt - (gt//10) * 10 ))
                print((f'{"84"}, destination "beruniy" {o}'))
                t = ((gt - (gt//10) * 10 ))
                print((f'{"48"}, destination "beruniy" {o}'))
            else:
                print('nothing found')
    elif loc == 'ozbekiston':
            
        if z > 1:
            if gt>60:
                o = 20 - ((gt - (gt//10) * 10 ))
                print((f'{"95"}, destination "beruniy" {o}'))
                t = ((gt - (gt//10) * 10 ))
                print((f'{"15"}, destination "beruniy" {o}'))
            else:
                print('nothing found')

bus_stop()

