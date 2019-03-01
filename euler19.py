import time

start = time.perf_counter()

first_sundays = 0
#weekdays = ['Tues','Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon']
sunday = 5
counter = 0
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1901, 2001):
	if (i % 4 == 0 and i % 100 != 0) | (i % 400 == 0):
		months[1] = 29
	else:
		months[1] = 28
	for month in months:
		candidate = month % 7
		counter = (candidate + counter) % 7
		if counter == 5:
			first_sundays += 1


print(first_sundays)




print("---- %s seconds ---" % (time.perf_counter() - start))

