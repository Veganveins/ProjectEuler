"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import math
import time
start_time = time.time()
#for some reason this is_prime function is much slower, thought it would be faster
#to only check if prime numbers were
# def is_prime(n):
#     primes = [] 
#     if n == 4 or n ==9:
#         return False
#     for i in range(2,int(math.ceil(math.sqrt(n)))):
#         if i in primes:
#             if n%i == 0:
#                 return False

#     return True

def is_prime(n):
    i = 2
    for i in range(2,1+int(math.ceil(math.sqrt(n)))):
        if n%i==0:
            return False
        
    
    return True


def get_rotations(n):
    number = str(n)
    rotated_number = number
    rotations = [n]
    for i in range(0, len(number) - 1):
        special_digit = rotated_number[0]
        rotated_number = rotated_number[1:]
        rotated_number = rotated_number + special_digit
        rotations.append(int(rotated_number))
    return rotations

def is_circular(n):
        nums_to_search = get_rotations(n)
        for num in nums_to_search:
            if is_prime(num) == False:
                return False
        return True
                

def find_circular_primes(n):
    circular_primes = [2]
    for i in range(3,n,2):
        if is_prime(i):
            if is_circular(i):
                circular_primes.append(i)
    return len(circular_primes)
    

if __name__ == '__main__':
    print find_circular_primes(1000000)
    print ">> Result returned in: ", (time.time() - start_time), "seconds"

    


