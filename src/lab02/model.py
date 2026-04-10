from lab01.model import Property
from typing import Iterator

class Agency:
    def __init__(self, name: str):
        self._items = []
        self._name = name


    #базовые методы агенства
    def add(self, item: Property):
        if not isinstance(item, Property):
            raise TypeError("Объект должен быть типом Property")
        if item in self._items:
            raise ValueError("Объект уже добавлен")
        self._items.append(item)

    def remove(self, item: Property):
        if not isinstance(item, Property):
            raise TypeError("Объект должен быть типом Property")
        if item not in self._items:
            raise ValueError("Объект не найден")
        self._items.remove(item)

    def remove_at(self, index: int):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть числом")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс выходит за пределы списка")
        self._items.pop(index)

    def get_all(self) -> list[Property]:
        return list(self._items)
    


    # методы поиска объектов по атрибутам
    def find_by_price(self, price: float) -> list[Property]:
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if price > 0:
            return [item for item in self._items if item.price == price]
        else:
            raise ValueError("Цена должна быть больше 0")
    
    def find_by_area(self, area: float) -> list[Property]:
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь должна быть числом")
        if area <= 20:
            raise ValueError("Площадь должны быть больше 20")
        return [item for item in self._items if item.area == area]
        
    
    def find_by_adress(self, adress: str) -> list[Property]:
        if not isinstance(adress, str):
            raise TypeError("Адресс должен быть строуой")
        if not adress.strip():
            raise ValueError("Адресс не может быть пустым")
        return [item for item in self._items if item.adress == adress]
    


    #колличество объектов в агенстве
    def __len__(self) -> int:
        return len(self._items)

    #метод перебора объектов
    def __iter__(self) -> Iterator[Property]:
        return iter(self._items)

    #метод поиска объекта по индексу
    def __getitem__(self, index: int) -> Property:
        return self._items[index]



    #сортировка объектов по цене
    def sort_by_price(self) -> None:
        self._items.sort(key=lambda x: x.price)

    #сортировка объектов по площади
    def sort_by_area(self) -> None:
        self._items.sort(key=lambda x: x.area)



    #сортировка объектов ...
    def get_expensive(self, min_price: float) -> list[Property]:
        if not isinstance(min_price, (int, float)):
            raise TypeError("Минимальная цена должна быть числом")
        if min_price > 0:
            return [item for item in self._items if item.price >= min_price]
        else:
            raise ValueError("Минимальная цена должна быть больше 0")

    #сортировка только активных готовых к продаже объектов
    def get_active(self) -> "Agency":
        for_clients = Agency(self._name + "_active")
        for item in self._items:
            if item.is_active:
                for_clients.add(item)
        return for_clients

    def get_for_rent(self) -> "Agency":
        result = Agency(self._name + "_rent")
        for item in self._items:
            if item.for_rent:
                result.add(item)
        return result
    