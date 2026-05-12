from typing import (
    TypeVar,
    Generic,
    Callable,
    Optional,
    Protocol,
    Iterator
)

# =========================================
# PROTOCOL
# =========================================

class Displayable(Protocol):
    def display(self) -> str:
        ...


class Scorable(Protocol):
    def score(self) -> float:
        ...


# =========================================
# TYPEVAR
# =========================================

T = TypeVar("T")
R = TypeVar("R")

D = TypeVar("D", bound=Displayable)
S = TypeVar("S", bound=Scorable)


# =========================================
# GENERIC COLLECTION
# =========================================

class TypedCollection(Generic[T]):

    def __init__(self) -> None:
        self._items: list[T] = []

    # =====================================
    # БАЗОВЫЕ МЕТОДЫ
    # =====================================

    def add(self, item: T) -> None:
        if item in self._items:
            raise ValueError("Объект уже существует")
        self._items.append(item)

    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError("Объект не найден")
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)

    # =====================================
    # MAGIC METHODS
    # =====================================

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    # =====================================
    # GENERIC METHODS
    # =====================================

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:

        for item in self._items:
            if predicate(item):
                return item

        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:

        return [
            item for item in self._items
            if predicate(item)
        ]

    def map(self, transform: Callable[[T], R]) -> list[R]:

        return [
            transform(item)
            for item in self._items
        ]


# =========================================
# COLLECTION FOR DISPLAYABLE
# =========================================

class DisplayCollection(Generic[D]):

    def __init__(self) -> None:
        self._items: list[D] = []

    def add(self, item: D) -> None:
        self._items.append(item)

    def show_all(self) -> None:

        for item in self._items:
            print(item.display())


# =========================================
# COLLECTION FOR SCORABLE
# =========================================

class ScoreCollection(Generic[S]):

    def __init__(self) -> None:
        self._items: list[S] = []

    def add(self, item: S) -> None:
        self._items.append(item)

    def show_scores(self) -> None:

        for item in self._items:
            print(item.score())