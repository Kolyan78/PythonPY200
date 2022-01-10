from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod


class LinkedListWithDriver(...):  # TODO наследовать класс LinkedList
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        ...  # TODO расширяем конструктор, чтобы в связном списке был driver

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        ...  # TODO считать данные из драйвера

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        ...  # TODO записать данные с помощью драйвера


if __name__ == '__main__':
    ll = ...  # TODO инициализировать пустой LinkedListWithDriver
    print("Считать данные из файла input.txt")
    # TODO инициализировать драйвер и считать данные
    print(ll)

    print("Записать данные в файл по умолчанию")
    # TODO заменить драйвер и записать данные
