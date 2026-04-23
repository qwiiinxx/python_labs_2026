from src.lab01.model import Property
from src.lab04.interfaces import Printable, Calculatable

class Apartments(Property, Printable, Calculatable):
    def __init__(self, price, area, adress, for_rent, rent_terms,
                 floor, balcony, rooms):
        super().__init__(price, area, adress, for_rent, rent_terms)

        self._floor = floor
        self._balcony = balcony
        self._rooms = rooms

    # реализация интерфейса Printable
    def to_str(self) -> str:
        return (
            f"Квартира: {self.adress}, {self._rooms} комнат, "
            f"{self.area} м², {self.price} руб."
        )

    # реализация интерфейса Calculatable
    def calculate(self) -> float:
        return self.tax_price(5)


class House(Property, Printable, Calculatable):

    def __init__(self, price, area, adress, for_rent, rent_terms,
                 own_floors, elevator, ground_area, rooms):
        super().__init__(price, area, adress, for_rent, rent_terms)

        self._own_floors = own_floors
        self._elevator = elevator
        self._ground_area = ground_area
        self._rooms = rooms

    # интерфейc Printable
    def to_str(self) -> str:
        return (
            f"Дом: {self.adress}, {self._rooms} комнат, "
            f"участок {self._ground_area} м², {self.price} руб."
        )

    # интерфейс Calculatable
    def calculate(self) -> float:
        return self.tax_price(10)


class PentHouse(Property, Printable, Calculatable):

    def __init__(self, price, area, adress, for_rent, rent_terms,
                 rooms, balcony, own_floors=2):
        super().__init__(price, area, adress, for_rent, rent_terms)

        self._own_floors = own_floors
        self._balcony = balcony
        self._rooms = rooms

    # интерфейc Printable
    def to_str(self) -> str:
        return (
            f"Пентхаус: {self.adress}, {self._rooms} комнат, "
            f"{self.area} м², {self.price} руб."
        )

    # интерфейс Calculatable
    def calculate(self) -> float:
        return self.tax_price(15)