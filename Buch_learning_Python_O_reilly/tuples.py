T = (1,2,3,4)                       # A 4-item tuple
len(T)                              # length

T + (5,6)                           # Concatenation

T[0]                                # first element of T

print(T.index(4))                   # 4 at postion 3
print(T.count(4))                   # 4 is once in the tuple

# T[0] = 2                          Doesn´t work

T = (2,) + T[1:]                    # make a new tuple for a new value


