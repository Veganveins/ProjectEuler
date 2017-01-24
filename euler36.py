"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindrome(string):
    length = len(string) - 1
    for i in range(0, len(string)/2):
        if string[i] != string[length - i]:
            return False
    return True


def double_base(n):
    palindromes = []
    for j in range(1,n):
        i = str(j)
        binary = str(bin(j))
        if is_palindrome(i) and is_palindrome(binary[2:]):
            palindromes.append(j)
    
    sums = sum(palindromes)
    return sums

if __name__ == '__main__':
    print double_base(1000000)

