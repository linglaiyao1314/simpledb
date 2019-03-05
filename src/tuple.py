from src.tupledesc import TupleDesc
from src.field import Field


class Tuple:
    def __init__(self, td: TupleDesc):
        self.__tuple_desc = None
        self.__record_id = None
        self.__fields = None
        self.reset_tupledesc(td)

    @property
    def tuple_desc(self):
        return self.__tuple_desc

    @property
    def record_id(self):
        return self.__record_id

    @record_id.setter
    def record_id(self, rid):
        self.__record_id = rid

    def set_field(self, i, f: Field):
        """
        Change the value of the ith field of this tuple.
        :param i: index of the field to change. It must be a valid index.
        :param f:  new value for the field.
        :return:
        """
        self.__fields[i] = f

    def get_field(self, i)-> Field:
        return self.__fields[i]

    def fields(self):
        for f in self.__fields:
            yield f

    def reset_tupledesc(self, td: TupleDesc):
        self.__tuple_desc = td
        self.__fields = [None for i in range(td.num_fields())]

    def __str__(self):
        """
        Returns the contents of this Tuple as a string.
         Note that to pass the
        system tests, the format needs to be as follows:
        column1\tcolumn2\tcolumn3\t...\tcolumnN
        where \t is any whitespace (except a newline)
        """
        return "\t".join([str(f) for f in self.__fields]) + "\n"



