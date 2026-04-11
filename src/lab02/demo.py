# python3 -m src.lab02.demo

from src.lab01.model import Property 
from src.lab02.collection import Agency

flat1 = Property(80_000_000, 45, ["Ленина", 10], False)
flat2 = Property(9_000_000, 60, ["Пушкина", 5], True, 12)
flat3 = Property(88_000_000, 35, ["Гагарина", 7], False)
flat4 = Property(66_666_666, 80, ["Тверская", 1], True, 6)
flat5 = Property(500_000, 25, ["Мира", 3], True, 3)
flat6 = Property(90_000_000, 120, ["Арбат", 12], False)
flat7 = Property(12_000_000, 55, ["Садовая", 8], True, 24)
flat8 = Property(12_000_000, 30, ["Озерная", 2], False)

agency = Agency("Elite Estate")
for flat in [flat1, flat2, flat3, flat4, flat5, flat6, flat7, flat8]:
    agency.add(flat)

print("=== ВСЕ ОБЪЕКТЫ ===")
for item in agency:
    print(item)

print("===ДОСТУП ПО ИНДЕКСУ===")
print(agency[0])
print(agency[3])

print("===КОЛИЧЕСТВО ДОБАВЛЕННЫХ ОБЪЕКТОВ===")
print(len(agency))

print("\n===ПОИСК ПО ЦЕНЕ (10 млн)===")
result = agency.find_by_price(10_000_000)
for item in result:
    print(item)

print("\n===СОРТИРОВКА ПО ЦЕНЕ===")
agency.sort_by_price()
for item in agency:
    print(item)

print("\nДОРОГИЕ ОБЪЕКТЫ (>= 30 млн):")
expensive = agency.get_expensive(30_000_000)

for item in expensive:
    print(item)

print("\n===ТОЛЬКО АКТИВНЫЕ===")
flat1 = flat1.deactivate()
flat3 = flat3.deactivate()
flat5 = flat5.deactivate()
flat7 = flat7.deactivate()

active = agency.get_active()

for item in active:
    print(item)

print("===ТОЛЬКО АРЕНДА===")
rent = agency.get_for_rent()
for item in rent:
    print(item)

print("ОШИБКА ДОБАВЛЕНИЯ:")
try:
    agency.add("не объект")
except Exception as e:
    print("Ошибка:", e)

print("ОШИБКА ДУБЛИКАТА:")
try:
    agency.add(flat1)
except Exception as e:
    print("Ошибка:", e)

print("ОШИБКА УДАЛЕНИЯ:")
try:
    agency.remove(Property(1, 1, ["Тест", 1], False))
except Exception as e:
    print("Ошибка:", e)

print("КЕЙС: КЛИЕНТ ИЩЕТ КВАРТИРУ ДЛЯ АРЕНДЫ С БЮДЖЕТОМ 6 МЛН")

# 1. только активные
active = agency.get_active()

# 2. только аренда
rent = active.get_for_rent()

# 3. только дешевые
result = rent.get_expensive(6_000_000)

for item in result:
    print(item)