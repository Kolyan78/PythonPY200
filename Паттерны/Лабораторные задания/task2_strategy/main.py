from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod, JsonFileDriverFactoryMethod


class LinkedListWithDriver(LinkedList):
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self.driver = driver

    # TODO свойство для driver (getter + setter)

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        data_from_driver = self.driver.read()

        for value in data_from_driver:
            self.append(value)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self.driver.write(self)


if __name__ == '__main__':
    ll = LinkedListWithDriver()
    ll.driver = ...  # TODO инициализировать SimpleFileDriver
    ll.read()
    print(ll)

    ll.driver = ...  # TODO инициализировать JsonFileDriver
    ll.write()
