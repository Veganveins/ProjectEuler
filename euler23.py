from itertools import combinations
#n is PERFECT if the sum of the proper divisors of n equals n
#n is deficient if the sum of proper divisors < n
#n is abundant if the sum of proper divisors > n

#12 is the smallest abundant number
#---> the smallest number that can be written as the sum of 
#two abundant numbers is 24


#all integers greater than 28123 can be written as the sum of two
#abundant numbers


#Find the sum of all the positive integers which CANNOT be 
#written as the sum of two abundant numbers

#ie, check all numbers 12 to 28123. 
#find all abundant numbers
#find all the possible ways to add two of them together, 
#and remove those from the list of all numbers less than 28123

#task 1, find all abundant numbers between 12 and 28123
#find all the factors

def find_factors(n):
    factors = []
    for i in range(1,n/2 + 1):
        if n%i == 0:
            factors.append(i)
    return factors, sum(factors)

def is_abundant(n):
    if find_factors(n)[1] > n:
        return True
    return False

#find abundant numbers less than n
def abundant_list(n):
    abundant_numbers = []
    for i in range(0,n):
        if is_abundant(i):
            abundant_numbers.append(i)
    return abundant_numbers

#find all numbers that can be written as the sum of two abundant numbers
def find_combinations(n):
    abundant = abundant_list(n)
    combs = list(combinations(abundant, 2))
    combs = map(sum, combs)
    abundant = [x*2 for x in abundant if x*2 < n]
    cansum = set(abundant + combs)
    return set(sorted(i for i in cansum if i<n))

#find numbers not in the list from find_combinations
def numbers_of_interest(n):
    blacklist = find_combinations(n)
    interest_list = []
    for i in range(1,n):
        if i not in blacklist:
            interest_list.append(i)
    return sum(interest_list)

print numbers_of_interest(28124)












