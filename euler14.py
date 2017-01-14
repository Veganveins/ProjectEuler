#Colatz sequence
#102 seconds

#need to be able to determine the length of a colatz sequence
#need to have an array with all of the potential checks and to be able to remove items from that array
#need to be able to save the longest chain so far and compare it to the current check
#this file definitely needs to go faster
import time
start_time = time.time()

def how_long(n):

	arr = [n]
	while n != 1:
		if n%2==0:
			n = n/2
			arr.append(n)
		else:
			n = 3*n + 1
			arr.append(n)
	length = len(arr)

	return length

def tricky(n):
	number = 13
	length = 10
	arr = [number, length]
	for i in range(13,n):
		trying_number = how_long(i)
		if trying_number > number:
			number = trying_number
			arr = [trying_number, i]
	return 'Of the numbers less than a million, the one giving the longest Collatz chain is: ', arr[1], 'with a length of:', arr[0],  'found in: ', (time.time() - start_time), "seconds"


print tricky(1000000), ' found in: ', time.time() - start_time, ' seconds'
