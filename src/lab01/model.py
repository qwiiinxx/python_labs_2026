from validate import validate_adress, validate_price, validate_area, validate_rent_logic


class Property:

    def __init__(self, price: float, area: float, adress: str, for_rent: bool, rent_terms: int | None = None) -> None:

        self._price = validate_price(price)
        self._area = validate_area(area)
        self._adress = validate_adress(adress) 

        self._for_rent = for_rent
        self._rent_terms = validate_rent_logic(for_rent, rent_terms)

        self._is_active = True

    @property
    def price(self) -> float:
        return self._price

    @property
    def area(self) -> float:
        return(self._area)

    @property
    def adress(self) -> str:
        return(self._adress)

    @property
    def is_active(self) -> bool:
        return self._is_active

    def activate(self) -> None:
        self._is_active = True

    def deactivate(self) -> None:
        self._is_active = False

    
    @price.setter
    def price(self, new_price: float) -> None:
        if self._is_active == False:
            raise RuntimeError("Цена не может быть установлена, так как объект неактивен")
        
        self._price = validate_price(new_price)

    # бизнес методы
    def set_active(self, is_active: bool) -> None:
        if not isinstance(is_active, bool):
            raise TypeError("Статус должен быть True или False")
        
        self._is_active = is_active

    def tax_price(self, tax: int) -> float:
        if not self._is_active:
            raise RuntimeError("Объект неактивен, нельзя рассчитать цену")
        if not isinstance(tax, int):
            raise TypeError("Налог должен быть целым числом процентов")
        if tax <= 0:
            raise ValueError("Налог должен быть больше 0")
        return self._price * (1 + tax / 100)

    # мета-методы
    def __str__(self) -> str:
        street, number = self._adress

        text = (
            f"Адрес: Улица {street}, дом {number}\n"
            f"Площадь: {self._area} м^2\n"
            f"Цена: {self._price} руб.\n"
            f"Аренда: {'Да' if self._for_rent else 'Нет'}\n"
            f"Срок аренды: {self._rent_terms if self._for_rent else 'Объект на продаже'}\n"
            f"Статус: {'Активен' if self._is_active else 'Неактивен'}\n"
        )
        return text

    def __repr__(self) -> str:
        return (
            f"Agency("
            f"price={self._price}, "
            f"area={self._area}, "
            f"adress={self._adress}, "
            f"for_rent={self._for_rent}, "
            f"rent_terms={self._rent_terms}, "
            f"is_active={self._is_active}"
            f")"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Property):
            return NotImplemented
        
        return (
            self._price,
            self._area,
            self._adress,
            self._for_rent,
            self._rent_terms,
            self._is_active
        ) == (
            other._price,
            other._area,
            other._adress,
            other._for_rent,
            other._rent_terms,
            other._is_active
        )