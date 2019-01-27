print('test if pythonsorts file runs')

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
        sortedData, but will be returned sorted.
        Note: if passed numeric strings, they will be returned as int/float as
        Dictated by form, mixed numeric and text is fine, will remain as text.
        !!! The origional sequence given may be altered or even deleted by this
        method !!!
    Return:
        sortedListData: a new list sorted in acending order made from the elements
        in dataToSort, if given an empty set, returns a new empty list.
        all numeric data is treated as coming before text data, eg 999 comes before '0a'
    """
    sData = list() #new list to hold sorted data and be returned
    if dataToSort is None: #make sure not passed value None
        return None
    #Check for data being valid signle types int or float
    elif type(dataToSort) is int or type(dataToSort) is float:
        sData.append(dataToSort)
    elif type(dataToSort) is list: #check for a list, if yes, make copy to sort
        sData = list(dataToSort).copy()
    else:
        raise TypeError("InsertSort does not support data of type:", type(dataToSort))
    
    return sData

