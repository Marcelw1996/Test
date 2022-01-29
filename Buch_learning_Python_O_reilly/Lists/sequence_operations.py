L = [123, 'spam', 1.23]             # A list of 3 different-type Objects
len(L)                              # Number of items in List

L[0]                                # indexing by position = 123
L[:-1]                              # slicing a list returns a new list [123,'spam']
L + [4,5,6]                         # concat/repeat make new lists too
L * 2                               # double the items in the list
L                                   # is still [123,'spam', 1.23]
