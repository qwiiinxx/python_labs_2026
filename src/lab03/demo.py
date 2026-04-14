#python3 -m src.lab03.demo

from src.lab02.collection import Agency
from src.lab03.models import Apartment, House, PentHouse

print("=== СОЗДАНИЕ ОБЪЕКТОВ ===")

flat1 = Apartment(10_000_000, 55.5, ["Ленина", 10], False, None, 5, True, 2)
flat2 = Apartment(7_500_000, 40.0, ["Пушкина", 3], True, 12, 2, False, 1)

house1 = House(25_000_000, 120.0, ["Садовая", 15], False, None, 2, True, 300.0, 5)
house2 = House(18_000_000, 90.0, ["Лесная", 7], True, 6, 1, False, 150.0, 4)

pent1 = PentHouse(50_000_000, 200.0, ["Центральная", 1], False, None, 6, True)

# --- создаем агентство ---
agency = Agency("EliteEstate")

print("=== ДОБАВЛЕНИЕ В КОЛЛЕКЦИЮ ===")

agency.add(flat1)
agency.add(flat2)
agency.add(house1)
agency.add(house2)
agency.add(pent1)

print(f"Всего объектов: {len(agency)}\n")

# --- вывод всех объектов ---
print("=== ВСЕ ОБЪЕКТЫ ===")
for item in agency:
    print(item)
    print("-" * 40)

# --- полиморфизм ---
print("=== РАСЧЕТ ЦЕНЫ С НАЛОГОМ (полиморфизм) ===")
for item in agency:
    print(f"Цена с налогом: {item.calculate():,.2f}")
print()

# --- фильтрация ---
print("=== ТОЛЬКО КВАРТИРЫ ===")
apartments = agency.get_only_apartments()
for item in apartments:
    print(item)

print("=== ТОЛЬКО ДОМА ===")
houses = agency.get_only_houses()
for item in houses:
    print(item)

print("=== ТОЛЬКО ПЕНТХАУСЫ ===")
penthouses = agency.get_only_penthouses()
for item in penthouses:
    print(item)


# кейс 1
print("КЕЙС 1: Квартиры + активные + расчет цены")

apartments = agency.get_only_apartments()
active_apartments = apartments.get_active()

for item in active_apartments:
    print(item)
    print(f"Цена с налогом: {item.calculate():,.2f}")
    print("-" * 30)
