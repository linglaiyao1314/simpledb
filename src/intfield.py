from src.field import Field
from src.type import IntType


class IntField(Field):
    def __init__(self, v):
        self.__value = v

    def __hash__(self):
        return self.__value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    def get_type(self):
        return IntType
