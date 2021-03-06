"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import time
start_time = time.time()

def is_factor(n,m):
    if n%m == 0:
        return True
    else:
        return False

def is_Prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def largest_prime(n):
    ceiling = n
    largest = 1
    i = 2
    while i < ceiling:
        if n%i == 0 and is_Prime(i):
            largest = i
            ceiling = n/i
            i += 1
        i += 1
        
    return largest, i


if __name__ == '__main__':
    print(largest_prime(600851475143), ' found in: ', time.time() - start_time, ' seconds')


