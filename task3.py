
def show_me(first= 0, second= 0, third = 0, fourth=0, *others, **nums):
    ac = first +second+third+fourth 
    for num in others:
        
        ac += num
    print(ac)

show_me(10, 20, 30, 40, 50, 60, 70, 80)

show_me(10, 20, third = 30, fourth =40)

show_me(second=20, first=10)

show_me(10,20,50,60,70, third=30, fourth=40 )