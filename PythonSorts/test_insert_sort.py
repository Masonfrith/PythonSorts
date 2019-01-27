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
        self.assertEqual(len(self.sList), 0, "Size of returned list did not equal size of given data (0)")

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
        self.assertEqual(len(self.sList), 1, "Size of returned list did not equal size of given data")

        self.sList = ps.insert_Sort(aFloat)
        self.assertEqual(self.sList, [-0.1159], 'Should return a list of single element of type float which is: -0.1159')
        self.assertEqual(len(self.sList), 1, "Size of returned list did not equal size of given data")

        self.sList = ps.insert_Sort(aZero)
        self.assertEqual(self.sList, [0], 'Should return a list of single element: 0')
        self.assertEqual(len(self.sList), 1, "Size of returned list did not equal size of given data")

        self.sList = ps.insert_Sort(aPositiveInt)
        self.assertEqual(self.sList, [100089], 'should return list of single element: 100089')
        self.assertEqual(len(self.sList), 1, "Size of returned list did not equal size of given data")

    #Test function being able to handle and return single str variables.
    def test_LoneStrings_InsertSort(self):
        aEmpty = ""
        aSpace = " "
        aChar = "c"
        aWord = "Word"
        aLongString = "This is a really long string with spaces and a \n newline!"

        self.sList = ps.insert_Sort(aEmpty)
        self.assertEqual(self.sList, [""], "Empty String should return a list with a single empty string ''")
        self.assertEqual(len(self.sList), 1, "Size of returned list did not equal size of given data")

        self.sList.clear()
        self.sList = ps.insert_Sort(aSpace)
        self.assertEqual(self.sList, [" "], "Giving a str space ' ' should return size one list containing ' ' ")
        self.assertEqual(len(self.sList), 1, "Size of returned list did not equal size of given data")



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
