from src.pageid import PageId


class RecordId:
    def __init__(self, pid: PageId, tupleno: int):
        self.__pid = pid
        self.__tupleno = tupleno

    def get_tuple_number(self):
        return self.__tupleno

    def get_page_id(self) -> PageId:
        return self.__pid
