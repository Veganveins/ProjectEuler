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

def get_list(n):
	primes = []
	for i in range(2,n):
		if is_prime(i):
			primes.append(i)
	return primes

def find_run(n):
	primes = get_list(100)
	for i in primes:
		



print(get_list(100))