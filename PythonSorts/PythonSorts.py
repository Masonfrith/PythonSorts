

def insert_Sort(dataToSort):
    """
    Purpose:
        Given a numeric, or text, data sequence (dataToSort), return a new sorted list using
        insertion sort to do so.
    Preconditions:
        dataToSort: a data sequence whose elements must be text, or base 10
        numeric data, or empty.
    Post-condition:
        A new list is made which will contain the same elements passed by
        dataToSort, but will be returned sorted.
        !!! The origional sequence given may be altered or even deleted by this
        method !!!
    Return:
        sortedListData: a new list sorted in acending order made from the elements
        in dataToSort, if given an empty set, returns a new empty list.
        all numeric data is treated as coming before text data, eg 999 comes before '0a'
    """
