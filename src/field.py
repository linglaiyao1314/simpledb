from abc import ABC, abstractmethod
from src.type import Type


class Field(ABC):
    @abstractmethod
    def get_type(self) -> Type:
        """"""

    @abstractmethod
    def __hash__(self):
        """"""

    @abstractmethod
    def __str__(self):
        """"""

    @abstractmethod
    def __eq__(self, other):
        """"""



