s = 'spam'
s.find('pa')                    # find the offset of a substring in s

s.replace('pa', 'xyz')          # Replace occurrences of a string in s with another

line = 'aaa,bbb,cccc,ddd'
line.split(',')                 # split on a delimiter into a list of substrings

s.upper()                       # Upper- and lowercase conversions
s.isalpha()                     # content tests: isalpha, isdigit, ect...

line = 'aaa,bbb,cccc,ddd\n'
line.rstrip()                   # Remove withespace characters on the right side
line.rstrip().split(',')        # combine two operations


