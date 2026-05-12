from src.lab06.container import (
    TypedCollection,
    Displayable,
    Scorable
)

from src.lab03.models import Apartment, House, PentHouse


print("\n========== ЛР-6 GENERICS & TYPING ==========")

# =========================================
# СОЗДАНИЕ ОБЪЕКТОВ
# =========================================

flat1 = Apartment(
    12_000_000,
    65.5,
    ["Ленина", 10],
    True,
    12,
    5,
    True,
    2
)

flat2 = Apartment(
    18_500_000,
    82.0,
    ["Пушкина", 7],
    False,
    None,
    9,
    False,
    3
)

house1 = House(
    45_000_000,
    180.0,
    ["Садовая", 15],
    False,
    None,
    2,
    False,
    400.0,
    5
)

pent1 = PentHouse(
    95_000_000,
    210.0,
    ["Невский", 1],
    False,
    None,
    6,
    True
)

# =========================================
# TYPED COLLECTION
# =========================================

print("\n=== TypedCollection[Apartment] ===")

apartments = TypedCollection[Apartment]()

apartments.add(flat1)
apartments.add(flat2)

for item in apartments.get_all():
    print(item)

# =========================================
# FIND
# =========================================

print("\n=== FIND ===")

found = apartments.find(lambda x: x.price > 15_000_000)

print("Найден объект:")
print(found)

not_found = apartments.find(lambda x: x.price > 100_000_000)

print("\nНичего не найдено:")
print(not_found)

# =========================================
# FILTER
# =========================================

print("\n=== FILTER ===")

big_flats = apartments.filter(lambda x: x.area > 70)

for item in big_flats:
    print(item)

# =========================================
# MAP
# =========================================

print("\n=== MAP -> list[str] ===")

addresses = apartments.map(lambda x: x.adress)

print(addresses)

print("\n=== MAP -> list[float] ===")

prices = apartments.map(lambda x: x.price)

print(prices)

# =========================================
# PROTOCOL DISPLAYABLE
# =========================================

print("\n=== Protocol Displayable ===")

display_collection = TypedCollection[Displayable]()

display_collection.add(flat1)
display_collection.add(house1)
display_collection.add(pent1)

for item in display_collection.get_all():
    print(item.display())

# =========================================
# PROTOCOL SCORABLE
# =========================================

print("\n=== Protocol Scorable ===")

score_collection = TypedCollection[Scorable]()

score_collection.add(flat2)
score_collection.add(house1)
score_collection.add(pent1)

for item in score_collection.get_all():
    print(item.score())

# =========================================
# ПРОВЕРКА РАЗНЫХ ТИПОВ
# =========================================

print("\n=== Разные типы в одной коллекции ===")

mixed = TypedCollection[Displayable]()

mixed.add(flat1)
mixed.add(house1)
mixed.add(pent1)

for item in mixed:
    print(type(item).__name__)
    print(item.display())
    print()

# =========================================
# ВАЛИДАЦИЯ
# =========================================

print("\n=== ВАЛИДАЦИЯ ===")

try:
    apartments.add("не объект")
except Exception as error:
    print(error)