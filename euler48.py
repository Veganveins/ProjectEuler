def self_powers(n):
    this_sum = 0
    for i in range(1,n):
        this_sum += pow(i,i)
    return this_sum

print self_powers(1001)%10000000000 