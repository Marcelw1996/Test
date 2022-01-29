s = "Spam"                  # make a 4-character Strin and assign it to a name
len(s)                      # length
s[0]                        # The first item on s, indexing by zero-based position
s[1]                        # The second item from the left

s[-1]                       # The last item from the end in s
s[-2]                       # the second-to-last item form the end

s[len(s)-1]                 # Negative indexing, the hard way
s[1:3]                      # Slice of s from offsets 1 through 2 (not 3)

s[1:]                       # same as s[1:len(s)]
s[0:3]                      # everything but the last
s[:3]                       # same as s[0:3]

s[:-1]                      #everything but the last but simpler s[0:-1]
s[:]                        # All of s same as s[0:len(s)]

s + "xyz"                   # Concatenation IMPORTANT s is still unchanged

s * 8                       # repetition



