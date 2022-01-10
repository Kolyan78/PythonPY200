class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = None
        self.init_day(day)

        self.month = None
        self.init_month(month)

        self.year = None
        self.init_year(year)

    def __repr__(self) -> str:
        return f"Date({self.day}, {self.month}, {self.year})"

    def __str__(self) -> str:
        return f"{str(self.day).rjust(2, '0')}/{str(self.month).rjust(2, '0')}/{str(self.year).rjust(4, '0')}"

    def check_type(self, value):
        if not isinstance(value, int):
            raise TypeError("Ошибка типа")

    def init_day(self, day):
        self.check_type(day)
        self.day = day

    def init_month(self, month):
        self.check_type(month)
        if not (0 < month <= 12):
            raise ValueError
        self.month = month

    def init_year(self, year):
        self.check_type(year)
        self.year = year


date = Date(7, 2, 1979)
print(date.day, date.month, date.year)
print(date)
print(repr(date))
print(str(date))
