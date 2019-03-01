# def is_prime(n):
#     if n > 7:
#         if n%2 == 0:
#             return False
#         if n%3 == 0:
#             return False
#         if n%5 == 0:
#             return False
#         if n%6 == 0:
#             return False
#         if n%7 == 0:
#             return False
#         for i in range(2,int(n/2)):
#             if n%i == 0:
#                 return False
#         return True
#     else:
#         if n == 1:
#             return False
#         for i in range(2,int(n/2)):
#             if n%i == 0:
#                 return False
#         return True

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


def get_primes(n):
    primes = []
    for i in range(999999,n):
        if is_prime(i) and i not in primes:
            primes.append(i)
    print(primes)
    pandigital_primes = []
    for prime in primes:
        if is_pandigital(prime):
            pandigital_primes.append(prime)

    return pandigital_primes

def is_pandigital(n):
    n = str(n)
    if "0" in str(n):
        return False
    elif len(set(n)) != len(n):
        return False
    elif max([int(c) for c in n]) > len(set(n)):
        return False
    else:
        return True



print(get_primes(7654321))