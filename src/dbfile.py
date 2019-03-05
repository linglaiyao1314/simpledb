from abc import ABC, abstractmethod
from src.pageid import PageId
from src.page import Page


class DbFile(ABC):
    @abstractmethod
    def get_id(self)->int:
        """
        Returns a unique ID used to identify this DbFile in the Catalog. This id
        can be used to look up the table via
        {@link Catalog#getDatabaseFile} and
        {@link Catalog#getTupleDesc}.
        <p>
        Implementation note:  you will need to generate this tableid somewhere,
        ensure that each HeapFile has a "unique id," and that you always
        return the same value for a particular HeapFile. A simple implementation
        is to use the hash code of the absolute path of the file underlying
        the HeapFile, i.e. <code>f.getAbsoluteFile().hashCode()</code>.
        return an ID uniquely identifying this HeapFile.
        """

    @abstractmethod
    def get_tupledesc(self):
        """Returns the TupleDesc of the table stored in this DbFile."""

    @abstractmethod
    def read_page(self, pid: PageId) -> Page:
        """"""

    @abstractmethod
    def write_page(self, p: Page):
        """"""

