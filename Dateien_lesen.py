# 'w' überschreibt die ganze datei
# 'a' fügt string hinzu
f = open ('c:/Users/Marcel_Progr/Desktop/Programme_Python/text','r+')
print(f.read())                     # ganze Datei lesen
print(f.readline())                 # nur erste zeile lesen
f.close()
f = open('c:/Users/Marcel_Progr/Desktop/Programme_Python/text','r+')
f.write('Hallooo')
f.close()