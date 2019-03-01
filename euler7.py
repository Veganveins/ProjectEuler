"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import time
start_time = time.time()

import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
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
    print(nth_prime(10000), ' found in: ', time.time() - start_time, ' seconds')