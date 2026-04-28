# ключи для сортировки
def by_price(item):
    """сортировка по цене"""
    return item.price

def by_area(item):
    """Сортировка по площади"""
    return item.area

def by_per_metr(item):
    """Сортировка по цене за м^2"""
    return item.price / item.area
# ================================

# фильтры
def is_expensive(item):
    """Дорогие объекты > 30 млн"""
    return item.price > 30_000_000

def is_cheap(item):
    """Дешевые объекты < 30 млн"""
    return item.price <= 30_000_000

def is_for_rent(item):
    """Объекты доступные для аренды"""
    return item.for_rent
# ====================================


# фабрика функций
def make_price_filter(max_price):
    """Создает фильтр по макс. цене"""
    def filter_fn(item):
        return item.price <= max_price
    return filter_fn
# ====================================

# для map
def get_price(item):
    """Получить цену"""
    return item.price

def to_str(item):
    """Преобразовывает в строку"""
    return str(item)
# =================================

# стратегии
class DiscountStrategy:
    """Стратегия: скидка"""

    def __init__(self, percent: float):
        self._percent = percent

    def __call__(self, item):
        return item.price * (1 - self._percent / 100)


class TaxStrategy:
    """Стратегия: налог"""

    def __init__(self, percent: float):
        self._percent = percent

    def __call__(self, item):
        return item.price * (1 + self._percent / 100)
# ===================================================

# ...
def apply(self, func):
    return [func(item) for item in self._items]
# =============================================