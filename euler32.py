import math

def f(x,y):
	z = str(str(x) + str(y))
	return z

def digit_sum(n):
	
	return sum(map(int, str(n)))



def is__one_to_nine__pandigital(multiplicand, multiplier):
	
	product = multiplier*multiplicand
	combined = f(product,f(multiplicand, multiplier))
	if len(combined) != 9:
		return False
	elif "0" in combined:
		return False
	elif len(set(combined)) != len(combined):
		return False
	elif digit_sum(combined) != 45:
		return False
	else:
		return product



def find_pandigitals(x):
	pandigits = []
	for i in range(1,x):
		for j in range(1,x):
			if is__one_to_nine__pandigital(i,j):
				if is__one_to_nine__pandigital(i,j) not in pandigits:
					pandigits.append(is__one_to_nine__pandigital(i,j))
	return pandigits, len(pandigits), sum(pandigits)

print(find_pandigitals(2200))


