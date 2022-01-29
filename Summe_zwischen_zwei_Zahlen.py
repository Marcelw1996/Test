# Dieses Programm berechnet die Summe aus allen Zahlen zwischen einer Ober- und Untergrenze
zahl1 = int(input("Geben Sie eine Zahl ein: "))
zahl2 = int(input("Geben Sie eine weitere Zahl ein: "))
zahlen = [zahl1, zahl2]
zahlen.sort()
#Schleife zur berechnung:
ergebnis = 0
for zahl in range(zahlen[0], zahlen[1] + 1):
    ergebnis += zahl #ist wie ergebnis = ergebnis + zahl
print(ergebnis)

