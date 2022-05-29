"""

Сделать примеры в файлике.
__call__
__repr__
@classmethod &@staticmethod
@property, setter, deleter

"""


# __call__
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs) -> int:  # Можно прописывать любые аргументы и указывать их в вызове.
        print('__call__')
        self.__counter += step
        return self.__counter


if __name__ == '__main__':
    c1: Counter = Counter()
    c2: Counter = Counter()  # Тем самым можно вызвать n количество независимых счетчиков.
    c1()  # с помощью метода __call__ можно вызывать экземпляры класса подобно функциям
    # (классы которые себя так ведут, называются - функторы)
    c1()
    c1(2)
    res_1 = c1(10)
    res_2 = c2(-5)
    print(res_1, res_2)


# dunder method __call__ можно применять в случаях если необходимо отредактировать текст по необходимым критериям.

class Text_Changer:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs) -> str:
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')
        return args[0].strip(self.__chars)


if __name__ == '__main__':
    text1 = Text_Changer(':,.!?;')  # Удаляет указанные символы в конце и начале текста
    text2 = Text_Changer(' ')  # Или же, удалять ненужные пробелы.
    res1 = text1('????Hello World!!!!!')
    res2 = text2('     Python          ')
    print(res1, res2, sep='\n')


#  __repr__
# Source link: https://www.youtube.com/watch?v=82-c43wE5nM
class Point:
    x: float = 0.0
    y: float = 0.0

    def __repr__(self) -> str:
        """ __repr__ - предоставляет строку объекта """
        # print('__repr__ WAS CALLED!')
        return f'({self.x}, {self.y})'


if __name__ == '__main__':
    p0: Point = Point()
    p0.x = 1.0
    p1: Point = Point()
    print(f'{p0} - {p1}')
    print(type(f'{p0} - {p1}'))  # соответственно, магический метод __repr__ конвертирует объекты в строки.


#  @classmethod & @staticmethod

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return f'({self.name},{self.email})'

    @classmethod
    def get_info_class(cls, data):  # cls - ссылается на сам класс User
        name, email = data
        return cls(name, email)

    @staticmethod  # этот метод не может обращаться к классу
    def get_info_static(self):
        return f'({self.name},{self.email})'
    # @staticmethod - изолирован от свойств и методов класса User


if __name__ == '__main__':
    user_list: list = ['Mark', 'mark@gmail.com']
    user_info: User = User.get_info_class(user_list)
    print(user_info.get_info())
    # для того чтобы @staticmethod отработал, необходимо передать в него - user_info
    print(user_info.get_info_static(user_info))


# @property, setter, deleter
# Source link: https://www.youtube.com/watch?v=d2m07ENg-tA&t=916s
# Source link: https://www.youtube.com/watch?v=H323khQJL40


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name  # Max
        self.last_name = last_name  # Mad

    @property  # getter
    def email(self) -> str:
        return f"{self.first_name}{self.last_name}@gmail.com".lower()  # madmax@gmail.com

    @property
    def fullname(self) -> str:
        return f'{self.first_name} {self.last_name}'  # Mad Max

    @fullname.setter  # setter
    def fullname(self, name) -> str:  # для строки 133 - personalisation.fullname = 'Calm Max'
        self.first_name, self.last_name = name.split()

    @fullname.deleter  # deleter
    def fullname(self) -> None:
        self.first_name = None
        self.last_name = None
        print('Full name was deleted')


if __name__ == '__main__':
    personalisation: Person = Person('Mad', 'Max')
    print(personalisation.fullname)
    print(personalisation.email)
    personalisation.first_name = 'Maximilian'
    print(personalisation.fullname)
    print(personalisation.email)
    personalisation.fullname = 'Calm Max'  # Используется для setter
    print(personalisation.fullname)
    print(personalisation.email)
    del personalisation.fullname  # Созданное имя 'Calm Max', будет удаленно с помощью декоратора @fullname.deleter
    print(personalisation.fullname)  # Данные по Calm Max и имеил calmmax@gmail.com были удалены -> None None
