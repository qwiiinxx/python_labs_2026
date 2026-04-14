from .base import Property

class Apartment(Property):
    def __init__(
        self,
        price: float,
        area: float,
        adress,
        for_rent: bool,
        rent_terms: int | None,
        floor: int,
        balcony: bool,
        rooms: int
    ):
        super().__init__(price, area, adress, for_rent, rent_terms)

        self._floor = floor
        self._balcony = balcony
        self._rooms = rooms

    def __str__(self) -> str:
        part1 = super().__str__()

        part2 = (
        f"Этаж: {self._floor}\n"
        f"Комнаты: {self._rooms}\n"
        f"Балкон: {'Да' if self._balcony else 'Нет'}\n"
    )
        return part1 + part2

    def calculate(self) -> float:
        return self.tax_price(5)


class House(Property):
    def __init__(
        self,
        price: float,
        area: float,
        adress,
        for_rent: bool,
        rent_terms: int | None,
        own_floors: int,
        elevator: bool,
        ground_area: float,
        rooms: int
    ):
        super().__init__(price, area, adress, for_rent, rent_terms)

        self._own_floors = own_floors
        self._elevator = elevator
        self._ground_area = ground_area
        self._rooms = rooms

    def __str__(self) -> str:
        part1 = super().__str__()

        part2 = (
            f"Этажей в доме: {self._own_floors}\n"
        f"Участок: {self._ground_area} м^2\n"
        f"Лифт: {'Есть' if self._elevator else 'Нет'}\n"
        f"Комнаты: {self._rooms}\n"
    )
        return part1 + part2

    def calculate(self) -> float:
        return self.tax_price(10)


class PentHouse(Property):
    def __init__(
        self,
        price: float,
        area: float,
        adress,
        for_rent: bool,
        rent_terms: int | None,
        rooms: int,
        balcony: bool,
        own_floors: int = 2
    ):
        super().__init__(price, area, adress, for_rent, rent_terms)

        self._own_floors = own_floors
        self._balcony = balcony
        self._rooms = rooms

    def __str__(self) -> str:
        part1 = super().__str__()
        part2 = (
            f"Пентхаус!\n"
        f"Этажей: {self._own_floors}\n"
        f"Комнаты: {self._rooms}\n"
        f"Балкон: {'Да' if self._balcony else 'Нет'}\n"
    )
        return part1 + part2

    def calculate(self) -> float:
        return self.tax_price(15)

