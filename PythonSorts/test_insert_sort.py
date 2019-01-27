import unittest
import PythonSorts as ps

class insert_sort_Test(unittest.TestCase):
    sList = list()

    #set up list for tests
    def setUp(self):
        self.sList = list()

    #Make sure list used is cleard before being used again.
    def tearDown(self):
        if self.sList is None:
            self.sList = list()
        self.sList.clear()

    #Test that function is fine taking in an empty list`
    def test_EmptyList_InsertSort(self):
        aList = list()
        self.sList = ps.insert_Sort(aList)
        self.assertEqual(self.sList, [], 
                         "Insert_Sort did not return an empty list!")

    #Test that function handles reciving value None, by returning same for you to handle.
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

        self.sList = ps.insert_Sort(aPositiveInt)
        self.assertEqual(self.sList, [100089], 'should return list of single element: 100089')

    #Test function being able to handle and return single str variables.
    def test_LoneStrings_InsertSort(self):
        aEmpty = ""
        aSpace = " "
        aChar = "c"
        aWord = "Word"
        aLongString = "This is a really long string with spaces and a \n newline!"
        self.fail("Not Implemented Yet")

    #Test that function can handle and return single numeric values in str form.
    #any numeric value that does NOT have text should be returned converted into int/float
    #rather than remain as text, 5Five, should be fine and remain text
    def test_LoneStringNumerics_InsertSort(self):
        aIntString = "-47"
        aFloatString = "-0.15647"
        aStringWithNumbers = "5Five"
        self.fail("Not Implemented Yet")

    #Test that function handles(exception) single var data of type bool.
    def test_InvalidLoneData_InsertSort(self):
        boolTrue = True
        boolFalse = False
        self.fail("Not Implemented Yet")

if __name__ == '__main__':
    unittest.main()
