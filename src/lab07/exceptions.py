class DuplicateItemError(Exception):
    """Объект уже существует в коллекции"""
    pass


class ItemNotFoundError(Exception):
    """Объект не найден"""
    pass


class InvalidMenuChoiceError(Exception):
    """Неверный пункт меню"""
    pass