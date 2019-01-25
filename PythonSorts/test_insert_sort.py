import unittest
import PythonSorts as ps

class insert_sort_Test(unittest.TestCase):
    def test_InsertSortEmptyList(self):
        aList = list()
        sList = ps.insert_Sort(aList)
        self.assertEqual(sList, [], 
                         "Insert_Sort did not return an empty list!")

if __name__ == '__main__':
    unittest.main()
