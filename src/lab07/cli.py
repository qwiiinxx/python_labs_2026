from src.lab07.app import RealEstateApp
from src.lab03.models import Apartment, House, PentHouse

from src.lab07.exceptions import (
    DuplicateItemError,
    ItemNotFoundError
)


app = RealEstateApp()


def show_menu() -> None:
    print("\n=== АГЕНТСТВО НЕДВИЖИМОСТИ ===")
    print("1. Добавить квартиру")
    print("2. Показать все объекты")
    print("3. Найти по цене")
    print("4. Удалить объект")
    print("5. Сортировка по цене")
    print("6. Только активные")
    print("7. Только аренда")
    print("0. Выход")


def add_apartment() -> None:
    try:
        price = float(input("Цена: "))
        area = float(input("Площадь: "))

        street = input("Улица: ")
        house_number = int(input("Номер дома: "))

        for_rent = input("Для аренды? (y/n): ").lower() == "y"

        rent_terms = None

        if for_rent:
            rent_terms = int(input("Срок аренды: "))

        floor = int(input("Этаж: "))
        balcony = input("Балкон? (y/n): ").lower() == "y"
        rooms = int(input("Комнат: "))

        flat = Apartment(
            price,
            area,
            [street, house_number],
            for_rent,
            rent_terms,
            floor,
            balcony,
            rooms
        )

        app.add_property(flat)

        print("Объект успешно добавлен")

    except ValueError:
        print("Ошибка ввода данных")

    except DuplicateItemError as e:
        print(e)


def show_all() -> None:
    items = app.get_all()

    if not items:
        print("Коллекция пуста")
        return

    for index, item in enumerate(items, start=1):
        print(f"\n--- ОБЪЕКТ {index} ---")
        print(item)


def find_by_price() -> None:
    try:
        price = float(input("Введите цену: "))

        result = app.find_by_price(price)

        if result:
            for item in result:
                print(item)
        else:
            print("Ничего не найдено")

    except ValueError:
        print("Ошибка ввода")


def remove_property() -> None:
    items = app.get_all()

    if not items:
        print("Коллекция пуста")
        return

    show_all()

    try:
        index = int(input("Введите номер объекта: ")) - 1

        item = items[index]

        confirm = input(
            "Удалить объект? (y/n): "
        ).lower()

        if confirm == "y":
            app.remove_property(item)
            print("Объект удален")

    except IndexError:
        print("Неверный индекс")

    except ItemNotFoundError as e:
        print(e)

    except ValueError:
        print("Ошибка ввода")


def sort_by_price() -> None:
    app.sort_by_price()

    print("Сортировка выполнена")

    show_all()


def show_active() -> None:
    active = app.get_active()

    for item in active:
        print(item)


def show_rent() -> None:
    rent = app.get_for_rent()

    for item in rent:
        print(item)


def run_cli() -> None:
    while True:

        show_menu()

        try:
            choice = int(
                input("\nВыберите пункт: ")
            )

            if choice == 1:
                add_apartment()

            elif choice == 2:
                show_all()

            elif choice == 3:
                find_by_price()

            elif choice == 4:
                remove_property()

            elif choice == 5:
                sort_by_price()

            elif choice == 6:
                show_active()

            elif choice == 7:
                show_rent()

            elif choice == 0:
                print("Выход из программы")
                break

            else:
                print("Неверный пункт меню")

        except ValueError:
            print("Введите число")