import random


numbers = [0,0,0,0,0,0]
for i in range(6):
    x = int(input('geben sie die erste Zahl ein:'))
    if x in range(1,49,1):
        numbers[i] = x
    else:
        numbers[i] = int(input('geben sie die erste Zahl ein zwischen 1 und 49:'))
print(numbers)
