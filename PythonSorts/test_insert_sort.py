import unittest
import PythonSorts as ps

class insert_sort_Test(unittest.TestCase):
    def test_InsertSortEmptyList(self):
        aList = list()
        sList = ps.insert_Sort(aList)
        self.assertEqual(sList, [], 
                         "Insert_Sort did not return an empty list!")

    def test_InsertSortNoneData(self):
        x = None
        sList = ps.insert_Sort(x)
        self.assertIs(sList, None,
                      'insert_sort should return value None without error when passed data with value None')

if __name__ == '__main__':
    unittest.main()
