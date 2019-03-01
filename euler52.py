def qualifies(n):
	array = [n, 2*n, 3*n, 4*n, 5*n, 6*n]
	stringn = [str(i) for i in array]
	

	for n in stringn:
		if set(n) != set(stringn[0]):
			return False
	return True


def find_permuted_multiples(n):

	permuted_multiples = []

	for i in range(1,n):
		if qualifies(i):
			return i


print(find_permuted_multiples(1000000))
