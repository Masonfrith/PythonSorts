import unittest
import PythonSorts as ps

class insert_sort_Test(unittest.TestCase):
    sList = list()

    def setUp(self):
        self.sList = list()

    def tearDown(self):
        if self.sList is None:
            self.sList = list()
        self.sList.clear()

    def test_EmptyList_InsertSort(self):
        aList = list()
        self.sList = ps.insert_Sort(aList)
        self.assertEqual(self.sList, [], 
                         "Insert_Sort did not return an empty list!")

    def test_NoneData_InsertSort(self):
        x = None
        self.sList = ps.insert_Sort(x)
        self.assertIs(self.sList, None,
                      'insert_sort should return value None without error when passed data with value None')

    # Test passing non-list single element numeric variables.
    def test_LoneNumbers_InsertSort(self):
        aInt = -4
        aFloat = -0.1159
        aZero = 0
        aPositiveInt = 100089

        self.sList = ps.insert_Sort(aInt)
        self.assertEqual(self.sList, [-4], 'should return a list of single element :-4')

        self.sList = ps.insert_Sort(aFloat)
        self.assertEqual(self.sList, [-0.1159], 'Should return a list of single element of type float which is: -0.1159')

        self.sList = ps.insert_Sort(aZero)
        self.assertEqual(self.sList, [0], 'Should return a list of single element: 0')

        self.sList = ps.insert_Sort(aPosaPositiveInt)
        self.assertEqual(self.sList, [100089], 'should return list of single element: 100089')

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
