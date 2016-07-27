#Colatz sequence

#need to be able to determine the length of a colatz sequence
#need to have an array with all of the potential checks and to be able to remove items from that array
#need to be able to save the longest chain so far and compare it to the current check


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
	return "Of the numbers less than a million, the one giving the longest Collatz chain is %s, with a length of %s" % (arr[1], arr[0])

print tricky(1000000) 


# def get_array(n):

# 	arr = [n]
# 	while n != 1:
# 		if n%2==0:
# 			n = n/2
# 			arr.append(n)
# 		else:
# 			n = 3*n + 1
# 			arr.append(n)

# 	return arr



# def check_all(n):
# 	arr = range(14,n)
# 	checking = arr[0]
# 	best = 10
# 	our_friend = 13
# 	while len(arr)>1:
# 		if how_long(checking) > best:
# 			best = how_long(checking)
# 			our_friend = checking
# 			arr = [x for x in arr if x not in get_array(checking)]
# 			checking = arr[0]
# 		else:
# 			arr = [x for x in arr if x not in get_array(checking)]
# 			checking = arr[0]

# 	return our_friend, best

# print(check_all(10000))









