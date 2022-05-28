"""

Задача 2 10 баллов: написать свою реализацию функции reduce() с описанием в инлайновых и многострочных комментариях
ее работы.
def my_reduce(): моя реализация. (постарайтесь по памяти реализовать.)

"""

# Source link: https://www.youtube.com/watch?v=ugj03y6sRVo
# reduce () работает иначе, чем map () и filter ().
# Он не возвращает новый список на основе переданной нами функции и итерации.
# Вместо этого он возвращает одно значение.

from functools import reduce


def my_reduce(x, y) -> int:
    return x + y


my_list: list = [4, 5, 1, 3, 8, 9]  # Output sum of my_list = 30
print(reduce(my_reduce, my_list))
