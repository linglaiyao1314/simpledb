import unittest
import random
import uuid
from src.tupledesc import TupleDesc
from src.tuple import Tuple
from src.intfield import IntField
from src.utility import Utility
from src.catalog import Catalog
from test.testutils import SkeletonFile

class TestCatalog(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        self.id1 = random.randint(1, 10000)
        self.id2 = random.randint(1, 10000)
        self.name1 = str(uuid.uuid4())
        self.name2 = str(uuid.uuid4())
        self.catalog = Catalog()
        self.catalog.add_table(SkeletonFile(self.id1, Utility.get_tupledesc(2)), self.name1)
        self.catalog.add_table(SkeletonFile(self.id2, Utility.get_tupledesc(2)), self.name2)

    def test_get_tupledesc(self):
        self.assertEqual(Utility.get_tupledesc(2),
                         self.catalog.get_tupledesc(self.id1))


    def test_get_table_id(self):
        self.assertEqual(self.id2, self.catalog.get_table_id(self.name2))
        self.assertEqual(self.id1, self.catalog.get_table_id(self.name1))
        try:
            self.catalog.get_table_id("foo")
        except KeyError as e:
            print(f"{e}")

    def test_getdbfile(self):
        self.assertEqual(self.id1, self.catalog.get_database_file(self.id1).get_id())

    def test_duplicate_names(self):
        id3 = self.id1 + self.id2
        self.catalog.add_table(SkeletonFile(id3, Utility.get_tupledesc(2)), self.name1)

        self.assertEqual(id3, self.catalog.get_table_id(self.name1))

    def test_duplicate_ids(self):
        new_name = str(uuid.uuid4())
        f = SkeletonFile(self.id2, Utility.get_tupledesc(2))

        self.catalog.add_table(f, new_name)
        self.assertEqual(new_name, self.catalog.get_table_name(self.id2))
        self.assertEqual(f, self.catalog.get_database_file(self.id2))


if __name__ == '__main__':
    unittest.main()

