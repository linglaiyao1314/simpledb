import unittest
from src.tupledesc import TupleDesc
from src.tuple import Tuple
from src.intfield import IntField
from src.utility import Utility


class TestTuple(unittest.TestCase):
    def setUp(self):
        pass

    def test_combine(self):
        td = Utility.get_tupledesc(2)
        tup = Tuple(td)
        tup.set_field(0, IntField(-1))
        tup.set_field(1, IntField(0))

        self.assertEqual(IntField(-1), tup.get_field(0))
        self.assertEqual(IntField(0), tup.get_field(1))

        tup.set_field(0, IntField(1))
        tup.set_field(1, IntField(37))

        self.assertEqual(IntField(1), tup.get_field(0))
        self.assertEqual(IntField(37), tup.get_field(1))

    def test_get_tupledesc(self):
        td = Utility.get_tupledesc(5)
        tup = Tuple(td)
        self.assertEqual(td, tup.tuple_desc)


if __name__ == '__main__':
    unittest.main()

