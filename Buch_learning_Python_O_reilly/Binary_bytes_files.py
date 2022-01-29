import struct
packed = struct.pack('>i4sh',7, b'spam',8)                  #create packed binary data
print(packed)                                               # 10 bytes, not objects or text

file = open('data.bin', 'wb')
file.write(packed)                                          # open binary output file
file.close()                                                # write packed binary data

data = open('data.bin','rb').read()                         # open/read binary data file
print(data)

data[4:8]                                                   # slice bytes in the middle
list(data)
print(data)