from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def to_str(self) -> str:
        pass


class Calculatable(ABC):
    @abstractmethod
    def calculate(self) -> float:
        pass

