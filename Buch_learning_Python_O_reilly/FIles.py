f = open('data.txt', 'w')                   # make a new file in output mode ('w' = write)
f.write('Hello\n')                          # write strings of characters to it
f.write('world\n')                          
f.close()

g = open('data.txt')                        # r = read = default
text = g.read()
print(text)

text.split()                                # convert text to strings
print(text)

for line in open('data.txt'):
    print(line)