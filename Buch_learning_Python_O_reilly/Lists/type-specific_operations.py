L = [123, 'spam', 1.23]
L.append('NI')                              # growing: add object at end of list
L.pop(2)                                    # shrinking: delete an item in the middle

M = ['bb', 'aa','cc']
M.sort()                                    # sort for the alphabet
M.reverse()                                 # reverse the order of the elements

M = [   [1,2,3]
        [4,5,6]                             # 3x3 Matrix
        [7,8,9]]
M[1]                                        # get row 2
M[1][2]                                     # get row 2 then get item 3 in the row

col2 =[row[1] for row in M]                 # collect the items in column 2
[row[1] +1 for row in M]                    # add 1 to each item in column 2
[row[1] for row in M if row[1]% 2 ==0]      # filter out odd items

diag = [M[i][i] for i in [0,1,2]]           # collect a diagonal from matrix

list((range(-6,7,2)))                       # -6 to 6 by 2 in a list