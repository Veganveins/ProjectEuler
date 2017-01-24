"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def sum_square(n1, n2):
    sum = 0
    for i in range(n1, n2+1):
        sum += i**2
    return sum

def square_sum(n1,n2):
    sum = 0
    for i in range(n1, n2+1):
        sum += i
    return sum**2

if __name__ == '__main__':
    print square_sum(1,100) - sum_square(1,100) 