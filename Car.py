gas_price = {
    80: 6400,
    92: 9000,
    95: 10000,
    100: 14000

}

class Car:
    def __init__(self, capacity, rate, consumption, fill_gas, type_gas) -> None:
        self.capacity = capacity
        self.rate = rate
        self.consumption = consumption
        self.fill_gas = fill_gas
        self.type_gas = type_gas
        
    
    def fill_tank(self):
        # try:
        #     if not isinstance(self.fill_gas, (float, int)):
        #         raise ValueError('You should input number to define how much do you want fill tank!!!')
        # except ValueError as err:
        #     print(err)
        #     return err
        self.fill_gas = int(input("How much liters do you want pour: "))
        empty = self.capacity - self.rate
        if self.fill_gas > empty:
            print('Your tank are not able to fill this amount')
        else:
            filled = self.rate + self.fill_gas
        self.rate = filled
        return f''
    def calc_gas_cost(self):
        litres = self.fill_gas
        type = gas_price[100]
        cost = type * litres
        return f'Cost {cost}'

    def available_distance(self):
        distance = (self.rate * 100) / self.consumption
        return f'{round(distance, 1)} km'

    def ride(self, distance):
        # try:
        #     if not isinstance(distance, (float, int)):
        #         raise ValueError('Distance should be a number')
        # except ValueError as err:
        #     print(err)
        #     return err
        consumed = distance * (self.consumption / 100)
        if consumed < self.rate:
            self.rate -= consumed
            return f'''
            Consumed oil: {round(consumed, 1)}
            Remaining fuel: {self.rate}'''
        # else: 
        #     try:
        #         raise ValueError('You do not have enough fuel. Please fill in your tank')
        #     except ValueError as err:
        #         print(err)
        #         return err
lc_300 = Car(90, 60, 14, 25, 100)