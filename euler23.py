import numpy as np
import time

start = time.time()

def get_divisors(n):
	divisors = []
	for i in range(1,n):
		if n % i == 0:
			divisors.append(i)
	return divisors

def is_abundant(n):
	if sum(get_divisors(n)) > n:
		return True
	return False



def get_abundants(n):
	abundants = []
	for i in range(1,n):
		if is_abundant(i):
			abundants.append(i)
	return abundants

def find_pairs(source):
        result = []
        for p1 in range(len(source)):
                for p2 in range(p1,len(source)):
                        result.append(source[p1]+source[p2])
        return result


def find_unabundants(n):
	
	candidates = range(1,28123)
	pairable = find_pairs(get_abundants(n))
	main_list = np.setdiff1d(candidates,pairable, assume_unique=True)
	return sum(main_list), main_list



print(find_unabundants(28123))
print("---- %s seconds ---" % (time.time() - start))