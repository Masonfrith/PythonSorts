import unittest
import PythonSorts as ps

class insert_sort_Test(unittest.TestCase):
    def test_EmptyList_InsertSort(self):
        aList = list()
        sList = ps.insert_Sort(aList)
        self.assertEqual(sList, [], 
                         "Insert_Sort did not return an empty list!")

    def test_NoneData_InsertSort(self):
        x = None
        sList = ps.insert_Sort(x)
        self.assertIs(sList, None,
                      'insert_sort should return value None without error when passed data with value None')

    def test_LoneNumbers_InsertSort(self):
        aInt = -4
        aFloat = -0.1159
        aZero = 0
        aPositiveInt = 100089
        self.fail("Not Implemented Yet")

    def test_LoneStrings_InsertSort(self):
        aEmpty = ""
        aSpace = " "
        aChar = "c"
        aWord = "Word"
        aLongString = "This is a really long string with spaces and a \n newline!"
        self.fail("Not Implemented Yet")

    def test_LoneStringNumerics_InsertSort(self):
        aIntString = "-47"
        aFloatString = "-0.15647"
        aStringWithNumbers = "5Five"
        self.fail("Not Implemented Yet")

    def test_InvalidLoneData_InsertSort(self):
        boolTrue = True
        boolFalse = False
        self.fail("Not Implemented Yet")

if __name__ == '__main__':
    unittest.main()
