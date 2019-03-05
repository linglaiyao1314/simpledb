from abc import ABC, abstractmethod
from typing import List


class PageId(ABC):
    @abstractmethod
    def serialize(self) -> List[int]:
        """
        :return: Return a representation of this page id object as a collection of
        integers (used for logging)

        This class MUST have a constructor that accepts n integer parameters,
        where n is the number of integers returned in the array from serialize.
        """

    @abstractmethod
    def get_table_id(self) -> int:
        """
        :return: the unique tableid hashcode with this PageId
        """

    @abstractmethod
    def hash_code(self) -> int:
        """
        :return: a hash code for this page, represented by the concatenation of
        the table number and the page number (needed if a PageId is used as a
        key in a hash table in the BufferPool, for example.)
        """
        pass

    @abstractmethod
    def __eq__(self, other):
        """
        Compares one PageId to another.
        :param other:
        :return: true if the objects are equal (e.g., page numbers and table
        ids are the same)
        """
        pass

    @abstractmethod
    def get_page_number(self) -> int:
        pass


