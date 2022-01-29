s = 'spam'
s = 'z' + s[1:]             # = zpam

s = 'shrubbery'
L = list(s)                 # expand to a list
L[1] = 'c'                  # Change it in place
''.join(L)                  # join it with empty delimiter
print(L)
