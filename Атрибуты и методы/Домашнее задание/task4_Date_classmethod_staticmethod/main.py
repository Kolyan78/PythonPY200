class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __repr__(self) -> str:
        return f"Date({self.day}, {self.month}, {self.year})"

    def __str__(self) -> str:
        return f"{str(self.day).rjust(2, '0')}/{str(self.month).rjust(2, '0')}/{str(self.year).rjust(4, '0')}"

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным
        Если год високосный, то возвращается True, если обычный, то False"""
        if year % 4 == 0:
            return True
        return False

    @staticmethod
    def get_max_day(month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        return Date.DAY_OF_MONTH[Date.is_leap_year(year)][month - 1]

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not isinstance(self.day or self.month or self.year, int):
            raise TypeError ("Неверный тип аргумента")
        if self.year == 0:
            raise ValueError("Неверно указан год")
        if not 0 < self.month <= 12:
            raise ValueError("Неверно указан месяц")
        if not 0 < self.day <= self.get_max_day(self.month, self.year):
            raise ValueError("Неверно указан день")


if __name__ == "__main__":
    """Создаем экземпля класса"""
    date = Date(17, 11, 1979)
    """Методы is_leap_year и get_max_day статические
    для того, чтобы можно было определить некоторые параметры, не создавая экземпляр класса
    например високосный год или нет, указав при этом только сам год,
    или максимальное количество дней в месяце, указав только лишь месяц и год.
    Для создания экземпляра, необходимо указывать полностью дату, включая день,
    который в вышеперечисленных случаях роли не играет.
    Также есть вопрос - для чего используется метод __slots__?
    Он определен в этом задании, но я так и не понял что с ним надо делать.
    Если его закомментировать, ничего не происходит, но ведь раз его здесь указали,
    то значит не просто так?"""
    print(Date.is_leap_year(2002)) # проверка високосного года
    print(Date.get_max_day(2, 2000)) # сколько дней в феврале 2001 года
