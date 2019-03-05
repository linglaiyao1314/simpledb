from src.dbfile import DbFile
from src.page import Page
from src.pageid import PageId
from src.tupledesc import TupleDesc


class SkeletonFile(DbFile):
    def write_page(self, p: Page):
        pass

    def read_page(self, pid: PageId) -> Page:
        pass

    def get_tupledesc(self):
        return self.td

    def __init__(self, table_id, td: TupleDesc):
        self.table_id = table_id
        self.td = td

    def get_id(self) -> int:
        return self.table_id

