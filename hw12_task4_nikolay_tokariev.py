"""

Задача 4. 30 баллов: Создать класс с методом которого можно будет возвращать область
видимости созданного экземпляра класса.
В конструкторе(__init__) вашего класса пускай будут те параметры которые вы захотите.

"""


# Пример может быть не очень, хотел сделать, то чего нет и попробовать использовать методы сравнения.

class Cargo:
    """ Данный класс проверяет - влезет ли груз в прицеп грузовика """
    trailer_length: float = 13.6  # Длина прицепа
    trailer_width: float = 2.5  # Ширина прицепа
    trailer_height: float = 2.6  # Высота прицепа

    def __init__(self, cargo_length: float, cargo_width: float, cargo_height: float):
        self.cargo_length = cargo_length
        self.cargo_width = cargo_width
        self.cargo_height = cargo_height
        print(locals())
        if not isinstance(cargo_length, float):
            raise TypeError('Value must be float')
        if not isinstance(cargo_width, float):
            raise TypeError('Value must be float')
        if not isinstance(cargo_height, float):
            raise TypeError('Value must be float')

    def __lt__(self, trailer_length):
        """ Сравнение помещается ли груз в прицеп, по длине - True (поместился)"""
        if not isinstance(trailer_length, (float, Cargo)):
            raise TypeError('Value must be float or used operand from Cargo class.')
        return self.cargo_length < trailer_length

    def __gt__(self, trailer_length):
        """ Сравнение помещается ли груз в прицеп, по длине - False (не поместился)"""
        if not isinstance(trailer_length, (float, Cargo)):
            raise TypeError('Value must be float or used operand from Cargo class.')
        return self.cargo_length > trailer_length

    def __le__(self, trailer_width):
        """ Сравнение помещается ли груз по ширине - True """
        if not isinstance(trailer_width, (float, Cargo)):
            raise TypeError('Value must be float or used operand from Cargo class.')
        return self.cargo_width <= trailer_width

    def __ge__(self, trailer_width):
        """ Сравнение помещается ли груз по ширине - False """
        if not isinstance(trailer_width, (float, Cargo)):
            raise TypeError('Value must be float or used operand from Cargo class.')
        return self.cargo_width >= trailer_width

    def __eq__(self, trailer_height):
        """ Высокий ли груз, если False - помещается по высоте, если True - то слишком высокий """
        if not isinstance(trailer_height, (float, Cargo)):
            raise TypeError('Value must be float or used operand from Cargo class.')
        return self.cargo_height == trailer_height


if __name__ == '__main__':
    trailer: Cargo = Cargo(13.6, 2.5, 2.6)  # Размеры прицепа
    goods: Cargo = Cargo(13.2, 2.2, 2.3)  # Размеры груза
    # Варианты сравнения
    print(goods < trailer)  # True
    print(goods > trailer)  # False
    print(goods <= trailer)  # True
    print(goods >= trailer)  # False
    print(goods == trailer)  # False
