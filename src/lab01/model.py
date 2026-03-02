from .validate import validate_adress, validate_price, validate_area, validate_rent_logic


class Agency:


    def __init__(self, price: float, area: float, adress: str, for_rent: bool, rent_terms: int | None = None) -> None:

        self._price = validate_price(price)
        self._area = validate_area(area)
        self._adress = validate_adress(adress)

        if not isinstance(for_rent, bool):
            raise TypeError("Опция аренды должна быть True или False")

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
        return(self._is_active)

    
    @price.setter
    def price(self, new_price: float) -> None:
        if self._is_active == False:
            raise RuntimeError("Цена не может быть установлена, так как объект неактивен")
        
        self._price = validate_price(new_price)

