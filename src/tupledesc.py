from typing import List
from src.type import Type


class TDItem:
    def __init__(self, t: Type, n: str):
        self.field_type = t
        self.field_name = n

    def __str__(self):
        return f"{self.field_name}({self.field_type})"


class TupleDesc:
    def __init__(self, type_arr: List[Type], field_arr: List[str] = None):
        if field_arr is None:
            field_arr = [str() for i in range(len(type_arr))]
        self.__items = [TDItem(t, n) for t, n in zip(type_arr, field_arr)]

    def num_fields(self):
        return len(self.items)

    def get_field_name(self, i):
        if len(self.items) <= i:
            raise IndexError("No such index")
        return self.items[i].field_name

    def get_field_type(self, i):
        if len(self.items) <= i:
            raise IndexError("No such index")
        return self.items[i].field_type

    def field_name_to_index(self, name):
        for index, item in enumerate(self.items):
            if item.field_name == name:
                return index
        raise ValueError("no such field name")

    def get_size(self):
        """
        :return: The size (in bytes) of tuples corresponding to this TupleDesc.
        Note that tuples from a given TupleDesc are of a fixed size.
        """
        size = 0
        for item in self.items:
            size += item.field_type.get_len()
        return size

    @staticmethod
    def merge(td1, td2):
        """
        Merge two TupleDescs into one, with td1.numFields + td2.numFields fields,
        with the first td1.numFields coming from td1 and the remaining from td2.
        :param td1: The TupleDesc with the first fields of the new TupleDesc
        :param td2: The TupleDesc with the last fields of the TupleDesc
        :return: the new TupleDesc
        """
        td3 = td1.__items + td2.__items
        type_arr = []
        field_arr = []
        for i in td3:
            type_arr.append(i.field_type)
            field_arr.append(i.field_name)

        return TupleDesc(type_arr, field_arr)

    def __eq__(self, o) -> bool:
        if not isinstance(o, TupleDesc):
            return False
        if self.get_size() != o.get_size():
            return False
        for i in range(self.num_fields()):
            if self.items[i].field_type != o.items[i].field_type:
                return False
        return True

    @property
    def items(self):
        return self.__items

    def __str__(self):
        return ",".join([f"{item.field_type}({item.field_name})"
                         for item in self.items])

