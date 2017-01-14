import math
"""
Find the product of the coefficients, a and b, for the 
quadratic expression that produces the maximum number of 
primes for consecutive values of n, starting with n=0.

Since the consecutive string must start with n=0, we know
we need only check for values of b such that b is prime.

Create a list of primes below 1000. That will be the list
of b's to check. There are 168 such primes to check.
"""
def _is_prime(n):
    ceiling = int(math.sqrt(n) +1)
    for i in range (2, ceiling):
        if n%i == 0:
            return False
    return True

def _quadratic_formula_inputs_(a,n,b):
    output = n*n + a*n + b
    if output < 0:
        return False
    elif _is_prime(output):
        return True
    return False

def _primes_below_1000():
    primes = []
    for i in range(2,1000):
        if _is_prime(i):
            primes.append(i)
    return primes[::-1]

def find_longest_string_for_combination(a,b):
    n = 0
    for n1 in range(0,b+1):


        if _quadratic_formula_inputs_(a,n1,b):
            n += 1
        else:
            return n
    return n

def find_best_combo():
    prime_list = _primes_below_1000()
    max_num_of_primes = 0
    best_a = 0
    best_prime = 0
    for prime in prime_list:
        for a in range(-999,1000):
            if find_longest_string_for_combination(a,prime) > max_num_of_primes:
                max_num_of_primes = find_longest_string_for_combination(a,prime)
                best_prime = prime
                best_a = a 
    return best_prime, best_a, best_a*best_prime

print find_best_combo()


    
    






