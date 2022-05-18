

# ! this file created by Sardor
#? this new line added by Sardor
import Car
import Person

gas_price = {
    80: 6400,
    92: 9000,
    95: 10000,
    100: 14000

}

lc_300 = Car(90, 60, 14, 25, 100)
print(lc_300.fill_tank())
print(lc_300.calc_gas_cost())
print(lc_300.available_distance())
print(lc_300.ride(100))    
customer = Person(300000)
print(customer.pay_money(150000))

