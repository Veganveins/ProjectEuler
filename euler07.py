"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
start_time = time.time()

def is_prime(n):
    if n > 7:
        if n%2 == 0:
            return False
        if n%3 == 0:
            return False
        if n%5 == 0:
            return False
        if n%6 == 0:
            return False
        if n%7 == 0:
            return False
        for i in range(2,n/2):
            if n%i == 0:
                return False
        return True
    else:
        if n == 1:
            return False
        for i in range(2,n/2):
            if n%i == 0:
                return False
        return True


def nth_prime(n):
    primes = []
    i = 1
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
            i += 1
        
        i += 1
    return primes[n-1]

if __name__ == '__main__': 
    print nth_prime(10001), ' found in: ', time.time() - start_time, ' seconds'


