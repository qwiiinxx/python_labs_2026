from src.lab02.collection import Agency
from src.lab03.models import Apartment

from src.lab07.exceptions import (
    DuplicateItemError,
    ItemNotFoundError
)


class RealEstateApp:
    """Бизнес-логика приложения"""

    def __init__(self) -> None:
        self._agency = Agency("WhiteWill Estate Agency")

    @property
    def agency(self) -> Agency:
        return self._agency

    # СОЗДАНИЕ ОБЪЕКТА
    def create_apartment(
        self,
        price: float,
        area: float,
        street: str,
        house_number: int,
        for_rent: bool,
        rent_terms: int | None,
        floor: int,
        balcony: bool,
        rooms: int
    ) -> Apartment:
        """Создание квартиры"""

        return Apartment(
            price,
            area,
            [street, house_number],
            for_rent,
            rent_terms,
            floor,
            balcony,
            rooms
        )

    # РАБОТА С КОЛЛЕКЦИЕЙ
    def add_property(self, item) -> None:
        """Добавление объекта"""

        try:
            self._agency.add(item)

        except ValueError:
            raise DuplicateItemError(
                "Такой объект уже существует"
            )

    def remove_property(self, item) -> None:
        """Удаление объекта"""

        try:
            self._agency.remove(item)

        except ValueError:
            raise ItemNotFoundError(
                "Объект не найден"
            )

    def get_all(self):
        """Получить все объекты"""

        return self._agency.get_all()

    def find_by_price(self, price: float):
        """Поиск по цене"""

        return self._agency.find_by_price(price)

    def sort_by_price(self) -> None:
        """Сортировка по цене"""

        self._agency.sort_by_price()

    def sort_by_area(self) -> None:
        """Сортировка по площади"""

        self._agency.sort_by_area()

    def get_active(self):
        """Только активные"""

        return self._agency.get_active()

    def get_for_rent(self):
        """Только аренда"""

        return self._agency.get_for_rent()