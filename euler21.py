#Evaluate the sum of all the amicable numbers under 10000
#Runs in ~30 seconds, can be faster...
import time
start_time = time.time()


def is_factor(n,m):
    if n%m == 0:
        return True
    else:
        return False


def d(n):
    array = []
    for i in range(1,n):
        if is_factor(n,i):
            array.append(i)
    return sum(array)

def is_amicable(n):
    first_part = []
    second_part = []
    for i in range(0,n):
        first_part.append(d(i))
        second_part.append(d(first_part[i]))

    amicables = []
    for i in range(0,n):
        if d(first_part[i]) != d(second_part[i]) first_part[i] == d(second_part[i]) and second_part[i] not in amicables:
            amicables.append(second_part[i])
            if first_part[i] not in amicables:
                amicables.append(first_part[i])
    return sum(amicables)

print is_amicable(10000), ' found in: ', time.time() - start_time, ' seconds'