from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)
        

    def init_capacity_volume(self, capacity_volume: [int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

    def init_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def add_water(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if (value < 0) or ((self.occupied_volume + value) > self.capacity_volume):
            raise ValueError
        self.occupied_volume += value

    def remove_water(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        if (value < 0) or (value > self.occupied_volume):
            raise ValueError
        self.occupied_volume -= value


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
    glass.add_water(100)
    print(glass.capacity_volume, glass.occupied_volume)
    glass.remove_water(150)
    print(glass.capacity_volume, glass.occupied_volume)
