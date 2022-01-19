"""
Описать с помощью ООП любую геометрическиую фигуру.
Установку значений производить или при инициализации экземпляра (через конструктор)
или через специальные методы (сеттеры).
Предусмотреть возможность получения различных параметров фигуры
(периметр, площадь, радиус, длина сектора окружности и т.д) через методы (геттеры).
Все типы устанавливаемых значений должны проверяться.
Для класса реализовать метод repr.
Создать несколько экземпляров класса вашей фигуры и напечатать их repr.
"""
from math import pi
class Circle:
    count = 0
    def __init__(self, radius):
        type(self).count += 1
        self.radius = None
        """
        Установить значение переменной None
        (кстати, а зачем это надо делать, если она после проверки будет установлена в заданное значение?)
        Может быть здесь можно обойтись без этой строки?
        """
        self.__check_value(radius)
        self.radius = radius
        self.diametr = self.radius * 2

    @staticmethod
    def __check_value(value):
        """
        Функция проверяет тип значения и величину значения. Это внутренний метод, поэтому вне класса он недоступен
        :param value: значение, тип которого нужно проверить
        :return: ничего
        """
        if not isinstance(value, (int, float)): # если это не число целое или дробное, то выдать ошибку
            raise TypeError("Ошибка типа данных")
        if value <= 0: # если величина меньше или равна нулю, то выдать ошибку
            raise ValueError("Значение не может быть меньше или равно нулю")

    def __repr__(self):
        return f"Радиус круга - {self.radius}\n" \
               f"Площадь круга - {self.get_square()}\n" \
               f"Длина круга - {self.get_length()}\n" \
               f"Площадь сектора {angle} градусов - {self.get_sector_square(angle)}\n" \
               f"Длина сектора {angle} градусов - {self.get_arc_length(angle)}\n"

    def set_radius(self, value):
        """
        Функция установки радиуса экземпляра (круга)
        :param value: значение радиуса
        :return: ничего
        """
        self.__check_value(value) # проверка типа
        self.radius = value

    def get_square(self):
        """
        :return: площадь круга, округленная до 3 знаков после запятой
        """
        return round(pi * pow(self.radius, 2), 3)

    def get_length(self):
        """
        :return: длина окружности, округленная до 3 знаков после запятой
        """
        return round(pi * 2 * self.radius, 3)

    def get_sector_square(self, angle):
        """
        :param angle: градусная мера сектора
        :return: площадь сектора заданной градусной меры, округленная до 3 знаков после запятой
        """
        self.__check_value(angle)
        return round(pi * pow(self.radius, 2) * (angle / 360), 3)

    def get_arc_length(self, angle):
        """
        :param angle: градусная мера дуги
        :return: длина дуги заданной градусной меры, округленная до 3 знаков после запятой
        """
        self.__check_value(angle)
        return round(((pi * self.radius) / 180) * angle, 3)

angle = 20 # зададим угол сектора и дуги
circle = Circle(6.3) # создадим экземпляр круга радиусом 6.3
print(circle) # выведем значения на экран
circle.set_radius(4.8) # изменим значение этого экземпляра на 4.8
print(circle) # и выведем на экран новые значения
angle = 48 # зададим новое значение угла сектора и дуги
print(circle) # также выведем на экран новые значения
circle2 = Circle(2.5) # создадим второй экзепляр с другим значением радиуса
circle3 = Circle(1.2) # и третий экземпляр, также с другми значением радиуса
print(circle2) # выведем на экран второй экземпляр
print(circle3) # выведем на экран третий экземпляр
print(Circle.count)