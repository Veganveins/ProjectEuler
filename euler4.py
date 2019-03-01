"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    number = str(n)
    num_digits = len(number)
    num_checks = int(num_digits/2)
    if num_digits == 1:
        return True
    for i in range(0, num_checks):
        if number[i] == number[num_digits-i-1]:
            continue
        else:
            return False
    return True


def largest_palindrome():
    i = 999
    j = 999
    max_pal = 0
    i_stuck = 0
    j_stuck = 0
    while i*j > i_stuck*j_stuck:
        if is_palindrome(i*j) and i*j > max_pal:
            max_pal = i*j
            i_stuck = i
            j_stuck = j
            i -= 1
            j = 999
        if j > 100 and (i+j) > i_stuck+j_stuck:
            j -= 1
        else:
            i -= 1
            j = 999
    return max_pal, i_stuck, j_stuck



if __name__ == '__main__':
    print(largest_palindrome())


