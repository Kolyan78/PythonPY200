from typing import Iterable
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Iterable:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Iterable) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    ...  # TODO реализовать драйвер работы с текстовым файлом

    # TODO реализовать метод чтения данных из файла

    # TODO реализовать метод записи в файл построчно

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


if __name__ == '__main__':
    write_data = [1, 2, 3]
    driver = SimpleFileDriver('output.txt')
    driver.write(write_data)

    read_data = driver.read()
    print(read_data)
