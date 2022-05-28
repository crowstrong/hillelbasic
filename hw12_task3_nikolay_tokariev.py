"""
Задача 3 30 баллов: написать функцию которая с помощью assert будет тестировать ваш самописный reduce

"""
# Source link 1: https://www.youtube.com/watch?v=WGfosDXSjZ0
# Source link 2: https://arshovon.com/snippets/python-reduce-example/

from functools import reduce


def get_list_multiplication(ar) -> int:
    result = 1
    for i in ar:
        result *= i
    return result


def get_list_multiplication_using_reduce(ar) -> int:
    return reduce(lambda x, y: x * y, ar, 1)


if __name__ == '__main__':
    ar_1: list = [3, 1, 4, 5, 2]
    ar_2: list = [3, 1, 4, 5, 1]
    var_1: int = get_list_multiplication(ar_1)
    var_2: int = get_list_multiplication_using_reduce(ar_2)
    # ar_1 is equal al_2 -> AssertionError
    # assert get_list_multiplication(ar_1) == get_list_multiplication_using_reduce(ar_2)
    # ar_1 isn't equal al_2 -> will be no errors
    assert get_list_multiplication(ar_1) != get_list_multiplication_using_reduce(ar_2)
    print(var_1)
    print(var_2)



