print("Dieses Programm berechnet die Fakultät der eingegebenen Zahl")
eing = int(input("Bitte eine ganze Zahl eingeben"))

def fakultät(n):
    if n == 1:
        return 1
    else:
        return n*fakultät(n-1)

ausg = fakultät(eing)
print(ausg)