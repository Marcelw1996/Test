def fib(n=5):                               # wenn benutzer keine Zahl eingibt, dann ist n=5
    if n < 2:
        return n
    else:
        return fib(n-1)+fib(n-2)

var = fib(10)
print(var)