import json

from src.lab03.models import (
    Apartment,
    House,
    PentHouse
)


def save(collection, filepath: str) -> None:
    """Сохранение объектов в JSON."""

    data = []

    for item in collection:

        item_data = {
            "type": item.__class__.__name__,
            "price": item.price,
            "area": item.area,
            "adress": item.adress,
            "for_rent": item.for_rent,
            "rent_terms": item.rent_terms
        }

        # Apartment
        if isinstance(item, Apartment):
            item_data.update({
                "floor": item._floor,
                "balcony": item._balcony,
                "rooms": item._rooms
            })

        # House
        elif isinstance(item, House):
            item_data.update({
                "own_floors": item._own_floors,
                "elevator": item._elevator,
                "ground_area": item._ground_area,
                "rooms": item._rooms
            })

        # PentHouse
        elif isinstance(item, PentHouse):
            item_data.update({
                "own_floors": item._own_floors,
                "balcony": item._balcony,
                "rooms": item._rooms
            })

        data.append(item_data)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


def load(filepath: str) -> list:
    """Загрузка объектов из JSON."""

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        return []

    items = []

    for item in data:

        item_type = item["type"]

        # Apartment
        if item_type == "Apartment":

            obj = Apartment(
                item["price"],
                item["area"],
                item["adress"],
                item["for_rent"],
                item["rent_terms"],
                item["floor"],
                item["balcony"],
                item["rooms"]
            )

        # House
        elif item_type == "House":

            obj = House(
                item["price"],
                item["area"],
                item["adress"],
                item["for_rent"],
                item["rent_terms"],
                item["own_floors"],
                item["elevator"],
                item["ground_area"],
                item["rooms"]
            )

        # PentHouse
        elif item_type == "PentHouse":

            obj = PentHouse(
                item["price"],
                item["area"],
                item["adress"],
                item["for_rent"],
                item["rent_terms"],
                item["rooms"],
                item["balcony"],
                item["own_floors"]
            )

        else:
            continue

        items.append(obj)

    return items