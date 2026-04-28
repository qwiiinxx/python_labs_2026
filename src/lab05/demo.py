from src.lab05.collection import Agency
from src.lab05.strategies import (
    by_price,
    by_area,
    by_per_metr,
    is_expensive,
    is_for_rent,
    make_price_filter,
    get_price,
    DiscountStrategy,
    TaxStrategy
)

from src.lab03.models import Apartments, House, PentHouse


# ==========================================
# СОЗДАНИЕ ОБЪЕКТОВ

flat1 = Apartments(10_000_000, 45, ["Ленина", 10], True, 12, 3, True, 2)
flat2 = Apartments(25_000_000, 70, ["Пушкина", 5], False, None, 5, False, 3)
flat3 = Apartments(15_000_000, 55, ["Гагарина", 7], True, 6, 2, True, 2)

house1 = House(40_000_000, 120, ["Садовая", 1], False, None, 2, True, 300, 5)
house2 = House(18_000_000, 90, ["Полевая", 12], True, 24, 1, False, 200, 4)

pent1 = PentHouse(60_000_000, 150, ["Центр", 1], False, None, 4, True)


# ==========================================
# СОЗДАЕМ КОЛЛЕКЦИЮ

agency = Agency("Elite Estate")

agency.add(flat1)
agency.add(flat2)
agency.add(flat3)
agency.add(house1)
agency.add(house2)
agency.add(pent1)


print("\n=== ВСЕ ОБЪЕКТЫ ===")
for item in agency:
    print(item)


# ==========================================
# СЦЕНАРИЙ 1: СОРТИРОВКА РАЗНЫМИ СТРАТЕГИЯМИ

print("\n=== СОРТИРОВКА ПО ЦЕНЕ ===")
agency.sort_by(by_price)
for item in agency:
    print(item.price)

print("\n=== СОРТИРОВКА ПО ПЛОЩАДИ ===")
agency.sort_by(by_area)
for item in agency:
    print(item.area)

print("\n=== СОРТИРОВКА ПО ЦЕНЕ ЗА М² ===")
agency.sort_by(by_per_metr)
for item in agency:
    print(item.price / item.area)


# ==========================================
# СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ

print("\n=== ДОРОГИЕ ОБЪЕКТЫ (>30 млн) ===")
expensive = agency.filter_by(is_expensive)
for item in expensive:
    print(item.price)

print("\n=== ТОЛЬКО ДЛЯ АРЕНДЫ ===")
rent = agency.filter_by(is_for_rent)
for item in rent:
    print(item)


# ==========================================
# СЦЕНАРИЙ 3: ФАБРИКА ФУНКЦИЙ

print("\n=== ОБЪЕКТЫ ДО 20 МЛН ===")
cheap_filter = make_price_filter(20_000_000)
cheap = agency.filter_by(cheap_filter)

for item in cheap:
    print(item.price)


# ==========================================
# СЦЕНАРИЙ 4: MAP

print("\n=== ВСЕ ЦЕНЫ (map) ===")
prices = list(map(get_price, agency))
print(prices)


# ==========================================
# СЦЕНАРИЙ 5: СТРАТЕГИИ (объекты)

print("\n=== СКИДКА 10% ===")
discount = DiscountStrategy(10)

for item in agency:
    print(discount(item))

print("\n=== НАЛОГ 20% ===")
tax = TaxStrategy(20)

for item in agency:
    print(tax(item))


# ==========================================
# СЦЕНАРИЙ 6: ЦЕПОЧКА (САМОЕ ГЛАВНОЕ)

print("\n=== ЦЕПОЧКА: дорогие → сортировка → налог ===")

result = (
    agency
    .filter_by(is_expensive)
    .sort_by(by_price)
    .apply(TaxStrategy(10))
)

print(result)