import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """

    ...  # TODO определить конструктор и перегрузить метод area


class Circle(Figure):
    """ Производный класс. Круг. """

    ...  # TODO определить конструктор и перегрузить метод area


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
