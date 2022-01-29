#for-loop
for c in 'spam':
    print(c.upper())

#while-loop
x = 4

while x > 0:
    print('spam!'*x)
    x -= 1

squares = [x**2 for x in [1,2,3,4,5,6,7,8,9,10]]
print(squares)

squares = []
for x in [1,2,3,4,5,6,7,8,9,10]:                
    squares.append(x**2)                            # list append
print(squares)
