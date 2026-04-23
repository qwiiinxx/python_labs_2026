from src.lab04.models import Apartments, House, PentHouse
from src.lab04.interfaces import Printable, Calculatable
from src.lab02.collection import Agency


# универсальная функция через интерфейс
def print_all(items: list[Printable]):
    for item in items:
        print(item.to_str())


def main():
    #  создаем объекты
    flat1 = Apartments(10_000_000, 55.0, ["Ленина", 10], True, 12, 5, True, 2)
    flat2 = Apartments(8_000_000, 45.0, ["Пушкина", 5], False, None, 3, False, 1)

    house1 = House(25_000_000, 120.0, ["Садовая", 7], False, None, 2, False, 300.0, 4)
    house2 = House(30_000_000, 150.0, ["Лесная", 3], True, 6, 3, True, 500.0, 5)

    pent1 = PentHouse(50_000_000, 200.0, ["Центральная", 1], False, None, 5, True)
    pent2 = PentHouse(60_000_000, 250.0, ["Арбат", 12], True, 12, 6, True)

    #  создаем коллекцию
    agency = Agency("Elite Estate")

    agency.add(flat1)
    agency.add(flat2)
    agency.add(house1)
    agency.add(house2)
    agency.add(pent1)
    agency.add(pent2)

    # ================================
    print("\n=== ВСЕ ОБЪЕКТЫ (через интерфейс Printable) ===")
    print_all(agency)

    # ================================
    print("\n=== ПОЛИМОРФИЗМ calculate() ===")
    for item in agency:
        print(f"{type(item).__name__}: {item.calculate():,.2f}")

    # ================================
    print("\n=== ФИЛЬТРАЦИЯ ПО Printable ===")
    printable_items = agency.get_printable()

    for item in printable_items:
        print(item.to_str())

    # ================================
    print("\n=== ФИЛЬТРАЦИЯ ПО Calculatable ===")
    calculatable_items = agency.get_calculatable()

    for item in calculatable_items:
        print(item.calculate())

    # ===============================
    print("\n===КЕЙС: ")

    # ================================
    print("\n=== КЕЙС: дорогие + расчет ===")
    expensive = agency.get_expensive(20_000_000)

    for item in expensive:
        print(item.to_str())
        print(f"С налогом: {item.calculate():,.2f}")
        print("-" * 30)


if __name__ == "__main__":
    main()