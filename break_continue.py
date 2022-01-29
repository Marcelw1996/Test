for i in range(0,20):
    if i%2 == 0:                                  # wenn zahl gerade ist
        continue                                  # continue überspringt einen durchlauf der schleife
    if i > 15:
        break                                       # Schleife wird komplett unterbrochen
    print(i)
    