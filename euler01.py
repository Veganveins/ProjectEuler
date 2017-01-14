#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def is_multiple(n, m):
    if n%m == 0:
        return True
    else:
        return False

def find_sum(n):
    candidates = []
    for i in range(0,n):
        if is_multiple(i,3) or is_multiple(i,5):
            candidates.append(i)
    return sum(candidates)

if __name__ == '__main__':
    print find_sum(1000)
