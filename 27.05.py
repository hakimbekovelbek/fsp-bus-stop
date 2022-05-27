## First Exercise
# class KgToPounds:
#     def __init__(self, kg = None):
#         self.__kg = kg

#     def get_kg(self):
#         return self.__kg

#     def to_pounds(self):
#         return self.__kg * 2.205

#     def set_kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             raise ValueError('Enter only numbers')

# weight = KgToPounds()
# weight.set_kg(35)
# print(weight.get_kg())



## Third exercise
# def show_me(*numbers, **nums):
#     sum = 0
#     for key, value in nums.items():
#         sum += value
#     for sums in numbers:
#         sum += sums
#     return sum

# print(show_me(2, 5, 9, 7, first = 3, second = 5))



# # Fourth Exercise
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def is_triangle(self):
#         if not isinstance(self.a, (int, float)) or not isinstance(self.b , (int, float)) or not isinstance(self.c , (int, float)):
#             try:
#                 raise ValueError('Enter only numbers')
#             except ValueError as err:
#                 return err
#         elif self.a < 0 or self.b < 0 or self.c < 0:
#             try:
#                 raise ValueError('Enter only positive numbers')
#             except ValueError as err:
#                 return err
#         elif self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a:
#             try:
#                 raise ValueError('You cant build a triangle with this numbers')
#             except ValueError as err:
#                 return err
#         else:
#             print('Congratulations, you can build a triangle')

# triangle = TriangleChecker(-1, 2, 3)

# print(triangle.is_triangle())
