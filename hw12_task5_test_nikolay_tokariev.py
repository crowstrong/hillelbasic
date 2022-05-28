"""
Задача 5. 20 баллов. Пройти тест
https://holypython.com/advanced-python-exercises/exercise-4-classes/
Exercise 4-c: Jet Fighter Instances
C Баглом. Пропустить.

"""


# 1. A class regarding an imaginary jet inventory is already defined for you.
# Also an instant of this Jet class is created and assigned to variable first_item.
# Print the name of the first_item.

# class Jets:
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
# first_item = Jets("F16", "USA")
#
# a = first_item.name
# print(a)
#
#
# # 2. This time print the origin of the first_item.
#
#
# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
# first_item = Jets("F16", "USA")
#
# a = first_item.name
# b = first_item.origin
#
# print(a, b)


# 3. Create new instances until the sixth item following this order:
# F14, SU33, AJS37, Mirage2000, Mig29, A10. You can check Hint 1 for the origins.
# Выдал ошибку


# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
# first_item = Jets('F14', 'USA')
# second_item = Jets('SU33', 'Russia')
# third_item = Jets('AJS37', 'Sweden')
# fourth_item = Jets('Mirage2000', 'France')
# fifth_item = Jets('Mig29', 'USSR')
# sixth_item = Jets('A10', 'USA')
#
# first_army = [first_item.name, second_item.name, third_item.name, fourth_item.name, fifth_item.name, sixth_item.name]
#
# print(first_army)


# 4 Add another attribute called "quantity" to the initialization method
# (usually referred to as constructor or __init__).
# Then define assign this attribute to self.quantity attribute inside the constructor.
# Then create 2 instances for: F14 and Mirage2000 with quantities 87 and 35.

#
# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country, quantity):
#         self.name = name
#         self.origin = country
#         self.quantity = quantity
#
#
# first_item = Jets("F14", "USA", 87)
# second_item = Jets("Mirage2000", "France", 35)
#
# total = first_item.quantity + second_item.quantity
# print(total)
#
#
# # 5 Pass
#
#
# # 6. Let's practice using string representation method to represent the data in previous exercise
# # in a much "classier" way, no pun intended!.
# # __str__ function can be used to return a string representation for the class when needed.
#
#
# class Nobel:
#
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#
#     def __str__(self):
#         return "{} was the winner of Nobel {} Prize in {}".format(self.winner, self.category, self.year)
#
#
# np2005 = Nobel("Peace", 2005, "Muhammad Yunus")
# print(np2005)
#
#
# # 7. We have seen multiple examples of class usage in Python. Let's build something from ground up.
# # In this exercise create a class named myfunc and inside it place a very simple function named "fifth"
# # which takes x and returns fifth power of x. No __init__ or class attributes needed.
# # Finally call your function with number 5 and assign it to variable ans.
#
# class myfunc:
#
#     def fifth(x):
#         return x ** 5
#
#
# ans = myfunc.fifth(5)
#
# print(ans)


# 8
#
# class myfunc:
#
#     def power(x, y):
#         return x ** y
#
#     def __str__(self):
#         return "Ok"
#
#
# ans1 = myfunc.power(5, 6)
# ans2 = myfunc()
#
# print(ans1)
# print(ans2)
