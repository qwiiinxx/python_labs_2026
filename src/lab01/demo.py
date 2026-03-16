from model import Agency

# print("Создание объекта Agency")


# print("Объект создан")
# print(flat1)



# print("\n=== ПРОВЕРКА СВОЙСТВ property ===")

# print("Цена:", flat1.price)
# print("Площадь:", flat1.area)
# print("Адрес:", flat1.adress)
# print("Активен:", flat1.is_active)


# print("=== ППОВЕРКА setter ===")
# flat1 = Agency(price=10000000, area=50, adress=["Ленинский проспект", 10], for_rent=False, rent_terms=None)
# flat1.deactivate()
# flat1.price = 10000000
# print(flat1)


# print("=== ПРОВЕРКА АКТИВНОСТИ ===")
# flat1.activate()
# print("Активен:", flat1.is_active)


# print("=== ПРОВЕРКА ВАЛИДАЦИИ ===")
# print("Пробуем снять в аренду объект который на продаже")
# flat1 = Agency(price=10000000, area=50, adress=["Ленинский проспект", 10], for_rent=False, rent_terms=3)

print("=== ПРОВЕРКА РАСЧЕТА НАЛОГА ===")
flat1 = Agency(price=680000000, area=50, adress=["Фрунзенская набережная", 10], for_rent=False, rent_terms=None)
print("Цена объекта:", flat1.price)
print("Устанавливаем налог 10 %")
price_with_tax = flat1.tax_price(10)
print("Цена объекта c налогом:", price_with_tax)

print("\n=== РАСЧЕТ С ДРУГИМ НАЛОГОМ ===")
price_with_tax = flat1.tax_price(25)
print("Устанавливаем налог 25 %")
print("Цена с налогом 25%:", price_with_tax)
