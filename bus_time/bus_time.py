


# ?   beruniy -- A
# ?               tinchli --B
# ?                           chorsu --C
# ?                                      abdulla_qodiriy --D








import datetime
a = datetime.datetime.now()
z = int(a.strftime('%H'))


hour = datetime.datetime.now()
hrs = int(hour.strftime('%H'))

minute = datetime.datetime.now()
min = int(minute.strftime('%M'))

gt = int((hrs * 60) + min)


def bus_stop():

    location = input('enter a location - ')

    if location == 'beruniy':

        if z > 1:
            if gt > 60:
                o = 28 - ((gt - (gt // 10) * 10 ))
                print(f'{"104"}, destination "tinchli" {o}')
                t = (gt - ((gt // 10) * 10))
                print(f'{"434"} destination "beruniu" {t}')
            
            else:
                print('blin')

        else:
            print('fuck off')

    elif location == 'tinchli':

        if z > 1:
            if gt > 60:
                o = 23 - (gt - ((gt // 10) * 10))
                print(f'{"104"} destination "tinchli" {o}')
                t = 18 - (gt - ((gt // 10) * 10))
                print(f'{"434"} destination "beruniy" {t}')
            else:
                print('blin')
        else:
            print('fuck off')

    elif location == 'chorsu':

        if z > 1:
            if gt > 60:
                o = 23 - (gt - ((gt // 10) * 10))
                print(f'{"104"} destination "chorsu" {o}')
                t = (gt - ((gt // 10) * 10))
                print(f'{"104"} destination "abdulla_qodiriy" {t}')
                nl = 28 - (gt - ((gt // 10) * 10))
                print(f'{"434"} destination "chorsu" {nl}')
                nl = (gt - ((gt // 10) * 10))
                print(f'{"434"} destination  "beruniy" {nl}')
            else:
                print('blin')
        else:
            print('fuck off')

    elif location == 'beruniy':
        if z > 1:
            if gt > 60:
                o = 28 - (gt - (gt // 10) * 10)
                print(f'{"104"} destination  "chorsu" {o}')
                t = 14 - (gt - ((gt // 10) * 10))
                print(f'{"104"} destination "abdulla_qodiriy" {t}')
            else:
                print('blin')
        else:
            print('fuck off')
    elif location == 'abdulla_qodiriy':
        if z > 1:
            if gt > 60:
                o = 28 - (gt - (gt // 10) * 10)
                print(f'{"104"} destination "abdulla_qodiriy" {o}')
                t = 14 - (gt - (gt // 10) * 10)
                print(f'{"104"} destination "chorsu" {t}')

            else:
                print('blin')
        else:
            print('fuck off')
bus_stop()

