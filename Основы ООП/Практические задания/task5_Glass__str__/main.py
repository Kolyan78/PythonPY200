from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def __repr__(self) -> str:
        return f"Glass({self.capacity_volume}, {self.occupied_volume})"

    def __str__(self) -> str:
        return f"Стакан объёмом {self.capacity_volume}. Объём жидкости = {self.occupied_volume}"


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса

    print(glass)  # Стакан объёмом 200. Объём жидкости = 100
    print([Glass(i, i) for i in range(50, 251, 50)])  # [Glass(50, 50), Glass(100, 100), Glass(150, 150), Glass(200, 200), Glass(250, 250)]
