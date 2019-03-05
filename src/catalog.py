"""

"""
import os
import uuid
from src.dbfile import DbFile
from src.tupledesc import TupleDesc


class DbTable:
    def __init__(self, dbfile, name, pk_field):
        self.__dbfile = dbfile
        self.__name = name
        self.__pk_field = pk_field

    @property
    def dbfile(self):
        return self.__dbfile

    @property
    def name(self):
        return self.__name

    @property
    def pk_field(self):
        return self.__pk_field


class Catalog:
    def __init__(self):
        self.__catalog = {}
        self.__name2id = {}

    def add_table(self, dbfile: DbFile, name: str = None, pk_field: str = None):
        """
        Add a new table to the catalog.
        This table's contents are stored in the specified DbFile.
        :param dbfile: the contents of the table to add;  dbfile.get_id() is the identfier of
        this file/tupledesc param for the calls getTupleDesc and getFile
        :param name: the name of the table -- may be an empty string.  May not be null.  If a name
        conflict exists, use the last table to be added as the table for a given name.
        :param pk_field: the name of the primary key field
        """
        if pk_field is None:
            pk_field = ""
        if name is None:
            name = str(uuid.uuid4())
        new_table = DbTable(dbfile, name, pk_field)
        table_id = dbfile.get_id()
        self.__catalog.update({table_id: new_table})
        self.__name2id.update({name: table_id})

    def get_table_id(self, name)->int:
        """Return the id of the table with a specified name"""
        table_id = self.__name2id.get(name, None)
        if table_id is None:
            raise KeyError("name not exists")
        return table_id

    def get_tupledesc(self, table_id: int) -> TupleDesc:
        table = self.get_table(table_id)
        return table.dbfile.get_tupledesc()

    def get_database_file(self, table_id: int)-> DbFile:
        table = self.get_table(table_id)
        return table.dbfile

    def get_primary_key(self, table_id: int)->str:
        table = self.get_table(table_id)
        return table.pk_field

    def get_table(self, table_id: int) -> DbTable:
        table = self.__catalog.get(table_id, None)
        if table is None:
            raise KeyError("table id is not exists")
        return table

    def get_table_name(self, table_id):
        table = self.get_table(table_id)
        return table.name

    def table_id_iterator(self):
        return self.__catalog.keys()

    def clear(self):
        self.__catalog.clear()
        self.__name2id.clear()

    def load_schema(self, catalog_file):
        base_folder = os.path.dirname(os.path.abspath(catalog_file))
        with open(catalog_file) as f:
            for line in f:
                pass

