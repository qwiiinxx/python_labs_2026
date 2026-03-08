def validate_price(price) -> float:
    if not isinstance(price, (float, int)):
        raise TypeError("Цена должна быть числом с запятой")

    if price <= 0:
        raise ValueError("Цена должна быть больше 0")
    
    return float(price)

def validate_area(area) -> float:
    if not isinstance(area, (float, int)):
        raise TypeError("Площадь должна быть числом")

    if area <= 20:
        raise ValueError("Площадь должна быть больше 20 м^2")

    return float(area)

def validate_adress(adress) -> str:
    
    if not isinstance(adress, list):
        raise TypeError(f"Адрес должен быть списком типа [Улица, номер]")
    
    if len(adress) != 2:
        raise ValueError("Адрес должен содержать 2 элемента")

    street, number = adress

    if not isinstance(street, str):
        raise TypeError("Улица должна быть строкой одним слововм")

    if not isinstance(number, int):
        raise TypeError("Номер дома должен быть цифрой")

    if not street.strip():
        raise ValueError("Улица не должна быть пустой")

    if number <= 0:
        raise ValueError("Номер дома должен быть положительным")

    street = street.strip()

    return (street, number)

def validate_rent_logic(for_rent, rent_terms) -> int | None:
    if not isinstance(for_rent, bool):
        raise TypeError("Опция аренды должна быть True или False")

    if for_rent == True:
        if rent_terms is None:
            raise ValueError("У объекта должен быть срок аренды")

        if not isinstance(rent_terms, int):
            raise TypeError("Срок аренды должен быть количеством месяцев")

        if rent_terms < 1:
            raise ValueError("Срок аренды должен быть от 1 месяца")

        return rent_terms

    else:
        if rent_terms is not None:
            raise ValueError("Объект на продаже, его нельзя арендовать")
        return None

