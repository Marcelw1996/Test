#Dieses Programm berechnet das Wechselgeld mit der kleinsten Anzahl an Münzen bzw Scheinen
print("Bitte geben sie den Wechselgeld Betrag in Cent an:")
wechsel = int(input())
zwei = 0
ein = 0
fünfzig = 0
zwan = 0
zehn = 0
fünf = 0
zweict = 0
einct = 0

while wechsel != 0:
    if wechsel >= 200:
        wechsel -= 200
        zwei = zwei + 1


    elif wechsel >= 100:
        wechsel = wechsel - 100
        ein = ein +1

    elif wechsel >= 50:
        wechsel = wechsel - 50
        fünfzig = fünfzig +1

    elif wechsel >= 20:
        wechsel = wechsel - 20
        zwan = zwan +1

    elif wechsel >= 10:
        wechsel = wechsel - 10
        zehn = zehn +1

    elif wechsel >= 5:
        wechsel = wechsel - 5
        fünf = fünf +1 

    elif wechsel >= 2:
        wechsel = wechsel - 2
        zweict = zweict +1

    elif wechsel >= 1:
        wechsel = wechsel -1 
        einct = einct +1

print("Die Anzahl der 2-Euro-Münzen beträgt: ",zwei)
print("Die Anzahl der 1-Euro-Münzen beträgt: ", ein)
print("Die Anzahl der 50-Cent-Münzen beträgt: ", fünfzig)
print("Die Anzahl der 20-Cent-Münzen beträgt: ", zwan)
print("Die Anzahl der 10-Cent-Münzen beträgt: ", zehn)
print("Die Anzahl der 5-Cent-Münzen beträgt: ", fünf)
print("Die Anzahl der 2-Cent-Münzen beträgt: ", zweict)
print("Die Anzahl der 1-Cent-Münzen beträgt: ", einct)