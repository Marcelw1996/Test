import random
#lotto programm

class lotto:
    
    numbers  = [0,0,0,0,0,0]
    for i in range(6):
        zahl = random.randint(1,49)
        numbers[i] = zahl
        if zahl in numbers:
            numbers[i] = random.randint(1,49)
    numbers.sort()
    

print('was möchten Sie machen?')
print('1: eigene lottozahlen vorgeben')
print('2: automatische Lottozahlen berechnen lassen')
user = int(input())

if user == 1:
    usernumbers=[0,0,0,0,0,0]
    for i in usernumbers:
        x = int(input('geben sie die erste Zahl ein:'))
        if x in range(1,49,1) and x not in usernumbers and x > 0:
            usernumbers[i] = x
            if x <= 0 and x not in range(1,49,1):
                x = int(input('geben sie die erste Zahl ein zwischen 1 und 49:'))
                usernumbers[i] = x
if user == 2:
    lotto2 = lotto()
    usernumbers = lotto2.numbers
    
lotto = lotto()
zahler = 0
for j in range(6):
    for z in range(6):
        if lotto.numbers[z] == usernumbers[z]:
                zahler += 1
usernumbers.sort()
print(lotto.numbers)
print(usernumbers)
print('Sie haben ' + str(zahler) + ' richtige zahlen')



