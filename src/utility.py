from typing import List
from src.type import Type, IntType
from src.tupledesc import TupleDesc


class Utility:
    @staticmethod
    def get_types(length: int) -> List[Type]:
        """a Type array of length len populated with Type.INT_TYPE"""
        return [IntType for i in range(length)]

    @staticmethod
    def get_strings(length: int, val: str) -> List[str]:
        return [val + str(i) for i in range(length)]

    @staticmethod
    def get_tupledesc(n, name=None):
        if name is None:
            return TupleDesc(Utility.get_types(n))
        return TupleDesc(Utility.get_types(n),
                         Utility.get_strings(n, name))


