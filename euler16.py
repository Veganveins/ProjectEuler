def digit_sum(n):
	
	return sum(map(int, str(n)))

print(digit_sum(2**1000))