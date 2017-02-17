def self_powers(n):
    this_sum = 0
    for i in range(1,n+1):
        this_sum += pow(i,i)
        result = str(this_sum)
    return result[-10:]

print self_powers(1000)