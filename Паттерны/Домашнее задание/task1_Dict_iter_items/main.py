from typing import Iterator, Tuple, Hashable, Any


class MyDict(...):  # TODO Наследование от класса dict
    ...  # TODO переопределить метод __iter__


if __name__ == "__main__":
    my_dict = MyDict({
        1: "a",
        2: "b",
        3: "c"
    })
    for key, value in my_dict:
        print(key, value)
