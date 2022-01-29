# for-schleife
x = ['python', 'Java', 'C++', 'Pascal']     # Liste für for-Schleife definieren
# einfache for-Schleife
for w in x:                                 # w ist iterator, welcher durch die schleife geht
    print(w)

# Verschachtelte for-Schleife

for w in x:                                 #Ausgabe von liste mit jedem element zusammen mit jedem andern
    for y in x:                             # Iterator muss unterschiedlich zum verschachtelten sein
        print(w,y)
        