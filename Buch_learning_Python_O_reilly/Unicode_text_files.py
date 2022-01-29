S = 'sp\xc4m'                               # non-ASCII Unicode text
print(S)
S[2]
file = open('unidata.txt', 'w', encoding='utf-8')       # write/endcode UTF-8 text
file.write(S)                                           # write string to file
file.close

text = open('unidata.txt', encoding='utf-8').read()     # read/decode UTF-8 text
print(text)

raw = open('unidata.txt', 'rb').read()                  # Read raw encoded bytes
print(raw)

