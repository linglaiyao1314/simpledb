"""
Page表示驻留在BufferPool的页
"""
from abc import ABC, abstractmethod
from src.pageid import PageId


class Page(ABC):
    @abstractmethod
    def get_id(self)->PageId:
        """"""

