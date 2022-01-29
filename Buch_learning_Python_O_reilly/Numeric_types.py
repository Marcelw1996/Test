x = 40 + 3.14                   # Integer to float, float math/result
print(x)

int(3.1415)                     # truncates float to integer
float(3)                        # converts integer to float


a = 3
b = 4

print(a+1, a-1)
print(b*3, b/2)
print(a%2, b**2)                # modulos and power
print(2+4.0, 2.0**b)            # mixed-type conversions

print(b/2+a)
print(b/(2.0+a))
num = 1/3.0
print(num)                    # auto  echos
print('%e' % num)               # string formating expression
print(num)
print('{0:4.2f}'.format(num))       # 2 gives the amount of numbers after the .

print(1<2)                          #less than
print(2.0>=1)                       # Greater than or equal: mixed time: 1 converted to 1.0
print(2.0 == 2.0)                   # equal
print(2.0 != 2.0)                   #not equal value

x = 2
y = 4
z = 6

print(x<y<z)
print(x<y and y<z)
print(1.1+2.2 == 3.3)                   # false, because of limited precision
print(int(1.1+2.2)==int(3.3))    

print(10/4)
print(10/4.0)
print(10//4.0)                          # rest

# Complex numbers

print(1j * 1J)
print(2+ 1j *3)

# Hex, Octal, Binary
print(0o1, 0o20, 0o377)             #octal basis
print(0x01, 0x10, 0xFF)             # hex basis
print(0b1, 0b10000, 0b11111111111)        #binary basis
print(oct(100), hex(40), bin(64))      #convert decimal to hex bin oct
x  = 0xFFFFFFFFFFFFFFFFFFFFFF
print(x)
print(oct(x))
print(bin(x))

# bitwise operation
y = 1
z = y << 2                          #shift left 2 bits:0100
print(z)
e = y | 2                               # bitwise OR
print(e)
w = y & 1                               # bitwise AND
print(w)

#build in numeric tools

import math
print(math.pi, math.e)
print(math.sin(2*math.pi/180))
print(math.sqrt(144), math.sqrt(2))
print(pow(2,4), 2**4, 2.0**4.0)
print(abs(-30), sum((1,2,3,4,5,6,7,7,8,8)))
print(min(8,1238,217,0,832,-1), max(18128383,823841,23848120432,3841))
print(round(2.567),round(2.456),round(2.567,2))
