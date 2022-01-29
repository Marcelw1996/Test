import random
# randint generates a random integar between the first parameter and the second
print(random.randint(1, 100))
y = int(input())
eins = 0
zwei = 0
drei = 0
vier = 0
funf = 0
sechs = 0
sieben = 0
acht = 0
neun = 0 
zehn = 0

for i in range (y):
    x = random.randint(1,10)
    if x == 1:
        eins += 1
    elif x == 2:
        zwei += 1
    elif x == 3:
        drei += 1
    elif x == 4:
        vier += 1
    elif x == 5:
        funf += 1
    elif x == 6:
        sechs += 1
    elif x == 7:
        sieben += 1
    elif x == 8:
        acht += 1
    elif x == 9:
        neun += 1
    elif x == 10:
        zehn +=1
    else:
        print("Fehler")

print("Häufigkeit von 1: ") 
print(eins/y)
print("Häufigkeit von 2: ") 
print(zwei/y)
print("Häufigkeit von 3: ") 
print(drei/y)
print("Häufigkeit von 4: ") 
print(vier/y)
print("Häufigkeit von 5: ") 
print(funf/y)
print("Häufigkeit von 6: ") 
print(sechs/y)
print("Häufigkeit von 7: ") 
print(sieben/y)
print("Häufigkeit von 8: ") 
print(acht/y)
print("Häufigkeit von 9: ") 
print(neun/y)
print("Häufigkeit von 10: ") 
print(zehn/y)
