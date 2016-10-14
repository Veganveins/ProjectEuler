#What is the sum of the digits of the number 2^1000 ?
x=2**1000
x=list(str(x))
x = map(int, x)
x = sum(x)
print x