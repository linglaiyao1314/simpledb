import unittest
from src.tupledesc import TupleDesc
from src.type import IntType
from src.utility import Utility


class TestFundedResearch(unittest.TestCase):
    def setUp(self):
        pass

    def test_combine(self):
        td1 = Utility.get_tupledesc(1, "td1")
        td2 = Utility.get_tupledesc(2, "td2")

        td3 = TupleDesc.merge(td1, td2)
        self.assertEqual(3, td3.num_fields())
        self.assertEqual(3 * IntType.get_len(), td3.get_size())
        for i in range(3):
            self.assertEqual(IntType, td3.get_field_type(i))

        self.assertEqual(self.combined_string_arrays(td1, td2, td3), True)

    def test_get_type(self):
        length = [1, 2, 1000]
        for len in length:
            td = Utility.get_tupledesc(len)
            for i in range(len):
                self.assertEqual(IntType, td.get_field_type(i))

    def combined_string_arrays(self, td1: TupleDesc, td2: TupleDesc, combined: TupleDesc):
        for i in range(td1.num_fields()):
            if not (((td1.get_field_name(i) is None) and
                     (combined.get_field_name(i) is None))
                    or td1.get_field_name(i) == combined.get_field_name(i)):
                return False

        for i in range(td1.num_fields(), td1.num_fields() + td2.num_fields()):
            if not (((td2.get_field_name(i - td1.num_fields()) is None) and
                     (combined.get_field_name(i) is None))
                    or td2.get_field_name(i-td1.num_fields()) == combined.get_field_name(i)):
                return False

        return True


if __name__ == '__main__':
    unittest.main()
