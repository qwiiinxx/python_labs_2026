from src.lab02.collection import Agency as BaseAgency


class Agency(BaseAgency):
    """
    Расширенная коллекция для ЛР-5
    Добавляет поддержку стратегий
    """

    # сортировка через функцию
    def sort_by(self, key_func):
        self._items.sort(key=key_func)
        return self

    # фильтрация через функцию
    def filter_by(self, predicate):
        result = Agency(self._name + "_filtered")

        for item in self._items:
            if predicate(item):
                result.add(item)

        return result

    # применение функции
    def apply(self, func):
        return [func(item) for item in self._items]