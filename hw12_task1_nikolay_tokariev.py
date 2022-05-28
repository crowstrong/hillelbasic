"""
Задача 1 10 баллов написать 3 примера генераторных функций с различными последовательностями.

"""


# 1. Как работает yield?

def test_foo() -> int:
    for i in range(3):
        yield i


a = test_foo()  # объект функции
print(next(a))  # next используется для того, чтобы перейти на следующий шаг в использовании yield / -> 0
print(next(a))  # вызывается следующая итерация / -> 1
print(next(a))  # / -> 2

# print(next(a))  # Когда заканчиваются значения, интерпретатор выводит ошибку StopIteration
# yield - не сохраняет значения в памяти.
print(type(a))


# 2.

def square_numbers(nums) -> int:
    for i in nums:
        yield (i * i)


my_nums = square_numbers([1, 2, 3, 4, 5])
for num in my_nums:  # Чтобы не выписывать постоянно print(next(my_nums))
    print(num)
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
print(type(my_nums))


# 3. Поочередный вывод yield

def generator_test() -> str:
    """ Функция выводит три разных текстовых значения """
    yield "Hello World"
    yield "I love Python"
    yield "And yield too"


text_test = generator_test()
print(next(text_test))
print(next(text_test))
print(next(text_test))
print(type(text_test))
