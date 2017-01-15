"""
The upper bound depends in part on 9!, which is 362880.

This tells us we have to check at least all 6 digit numbers.
So we'd have to check 999999 which would have a factorial sum of
2177280 which is a 7 digit number.

So we have to check all 7 digit numbers. So we'd have to check
9999999 which is 2540160. This is our upper bound.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def is_curious(n):
    temp_n = str(n)
    length = len(temp_n)
    factorial_sum = 0
    for i in range(0, length):
        digit = int(temp_n[i])
        factorial_sum += factorial(digit)
    if factorial_sum == n:
        return True
    else:
        return False

def find_curious(n):
    curious_numbers = []
    for i in range(3,n):
        if is_curious(i):
            curious_numbers.append(i)
    return sum(curious_numbers)

if __name__ == "__main__":
    print find_curious(2540160)

