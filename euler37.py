"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import math
import time
start_time = time.time()

def is_prime(n):
    if n ==1:
        return False
    if n == 2:
        return True
    for i in range(2,1+int(math.ceil(math.sqrt(n)))):
        if n%i==0:
            return False
        
    
    return True

def generate_list(n):
    primes = []
    for i in range(10,n):
        if is_prime(i):
            primes.append(i)
    return primes

def truncate(n):
    number = str(n)
    truncate_list = []
    for i in range(1, len(number)):
        truncate_list.append(number[i:])
    for i in range(1, len(number)):
        index = i*(-1)
        truncate_list.append(number[:index])
    truncate_list = [int(x) for x in truncate_list]
    return truncate_list


def determine_if_truncates_are_all_prime(n):
    candidates = truncate(n)
    for candidate in candidates:
        if not is_prime(candidate):
            return False
    return True

def find_truncatable_primes(n):
    prime_list = generate_list(n)
    truncatable_primes = []
    for prime in prime_list:
        if determine_if_truncates_are_all_prime(prime):
            truncatable_primes.append(prime)
    return truncatable_primes, sum(truncatable_primes)



if __name__ == '__main__':
    print find_truncatable_primes(1000000)
    print ">> Result returned in: ", (time.time() - start_time), "seconds"

    