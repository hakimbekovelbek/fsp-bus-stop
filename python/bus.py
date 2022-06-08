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
                o = 24 - ((gt - (gt//10) * 10 ))
                print((f'{"104"}, destination "beruniy" {o}'))
                t = ((gt - (gt//10) * 10 ))
                print((f'{"434"}, destination "beruniy" {o}'))
            else:
                print('nothing found')
        else:
            print('nothing')

    