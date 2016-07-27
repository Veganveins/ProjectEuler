def collatz(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return count
 
max = [0,0]
for i in range(100000):
    c = collatz(i)
    if c > max[0]:
        max[0] = c
        max[1] = i

print "found %s at length %s"  % (max[1],max[0])