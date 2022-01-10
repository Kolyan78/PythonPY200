from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):

        self.__capacity_volume = self.__check_capacity_volume(capacity_volume)
        self.__occupied_volume = self.__check_occupied_volume(occupied_volume)
        self.__check_overflow(self.__capacity_volume, self.__occupied_volume)

    @staticmethod
    def __check_capacity_volume(value: Union[int, float]) -> Union[int, float]:
        if not isinstance(value, (int, float)):
            raise TypeError
        if not value > 0:
            raise ValueError
        return value

    @staticmethod
    def __check_occupied_volume(value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        return value

    @staticmethod
    def __check_overflow(capacity, occupied):
        if capacity < occupied:
            raise OverflowError("Стакан не резиновый")

    def get_capacity_volume(self):
        return self.__capacity_volume

    def get_occupied_volume(self):
        return self.__occupied_volume

    def add_water(self, value):
        self.__check_occupied_volume(value)
        self.__check_overflow(self.__capacity_volume, self.__occupied_volume + value)
        self.__occupied_volume += value


if __name__ == "__main__":
    g1 = Glass(200, 100)  # TODO инициализировать экземпляр класса Glass
    print(g1.get_capacity_volume())  # TODO распечатать атрибут capacity_volume
    print(g1.get_occupied_volume())  # TODO распечатать атрибут occupied_volume
