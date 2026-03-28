from model import Property

# print("Создание объекта Property")


# print("Объект создан")
# print(flat1)



# print("\n=== ПРОВЕРКА СВОЙСТВ property ===")

# print("Цена:", flat1.price)
# print("Площадь:", flat1.area)
# print("Адрес:", flat1.adress)
# print("Активен:", flat1.is_active)


print("=== ППОВЕРКА setter ===")
flat1 = Property(price=10000000, area=50, adress=["Ленинский проспект", 10], for_rent=False, rent_terms=None)
print("=== БЫЛО ===")
print("Цена:", flat1.price)
flat1.price = 20000000
print("=== СТАЛО ===")
print("Цена:", flat1.price)


# print("=== ПРОВЕРКА АКТИВНОСТИ ===")
# flat1.activate()
# print("Активен:", flat1.is_active)



# print("=== ПРОВЕРКА ВАЛИДАЦИИ ===")
# try:
#     flat22 = Property(price=100000000, area=95, adress=("ленина", 10), for_rent=True, rent_terms=1)
# except Exception as e:
#     print("Ошибка:", e)



# print("=== ПРОВЕРКА ВАЛИДАЦИИ ===")
# try:
#     flat22 = Property(price=-100, area=70, adress=["Ленина", 10], for_rent=True, rent_terms=1)
# except Exception as e:
#     print("Ошибка:", e)



# print("=== ПРОВЕРКА ВАЛИДАЦИИ ===")
# try:
#     flat22 = Property(price=100000000, area=95, adress=["", 10], for_rent=True, rent_terms=1)
# except Exception as e:
#     print("Ошибка:", e)



# print("=== ПРОВЕРКА ВАЛИДАЦИИ ===")
# print("Пробуем снять в аренду объект который на продаже")
# try:
#     flat1 = Property(price=10000000, area=50, adress=["Ленинский проспект", 10], for_rent=False, rent_terms=3)
# except Exception as e:
#     print("Ошибка:", e)

# print("=== ПРОВЕРКА РАСЧЕТА НАЛОГА ===")
# flat1 = Property(price=680000000, area=50, adress=["Фрунзенская набережная", 10], for_rent=False, rent_terms=None)
# print("Цена объекта:", flat1.price)
# print("Устанавливаем налог 10 %")
# price_with_tax = flat1.tax_price(10)
# print("Цена объекта c налогом:", price_with_tax)

# print("\n=== РАСЧЕТ С ДРУГИМ НАЛОГОМ ===")
# price_with_tax = flat1.tax_price(25)
# print("Устанавливаем налог 25 %")
# print("Цена с налогом 25%:", price_with_tax)


# print("=== ПРОВЕРКА repr ===")
# flat1 = Property(price=1800000000, area=500, adress=["Фрунзенская набережная", 10], for_rent=True, rent_terms=2)
# print(repr(flat1))

# print("\n=== ПРОВЕРКА __eq__ (РАЗНЫЕ ОБЪЕКТЫ) ===")
# flat1 = Property(price=1800000000, area=500, adress=["Фрунзенская набережная", 10], for_rent=True, rent_terms=2)
# flat2 = Property(
#     price=500000,
#     area=80,
#     adress=["Большая Полянка", 5],
#     for_rent=True,
#     rent_terms=12
# )

# print("flat1 == flat2:", flat1 == flat2)


# print("\n=== ПРОВЕРКА __eq__ (ОДИНАКОВЫЕ ОБЪЕКТЫ) ===")
# flat1 = Property(price=1800000000, area=500, adress=["Фрунзенская набережная", 10], for_rent=True, rent_terms=2)
# flat2 = Property(
#     price=flat1._price,
#     area=flat1._area,
#     adress=["Фрунзенская набережная", 10],
#     for_rent=True,
#     rent_terms=2
# )

# print("flat1 == flat2:", flat1 == flat2)

