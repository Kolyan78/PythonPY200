from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.capacity_volume}, {self.occupied_volume})"


if __name__ == "__main__":
    glass = Glass(200, 100)
    print(glass)

