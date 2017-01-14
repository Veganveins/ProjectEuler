from math import ceil
"""
The upper right diagonal will follow the pattern (1^2, 3^2, 5^2, 7^2, 9^2, ....)

So a 1001 by 1001 spiral will have 1000^2 on the upper right diagonal

The upper left diagonal will be equal to:




1 --> 1 -->  0
2 --> 9 -->  2
3 --> 25 --> 4       5x5
4 --> 49 --> 6
5 --> 81 --> 8
6 --> 121 --> 10


X? --> 1002001 ---> Y?      1001 x 1001

Need to find X?

X is just the square root of the value, divided by 2, rounded up. 

So X? is 501

Y? is just X? * 2 - 2 

So Y? is 1000

So the sum is 1002001 + (1002001 - 1000) + (1002001 - 2000) + (1002001 - 3000)

"""


def find_spiral_sum(n):

    dimension = n*n
    subtractor = n-1
    cumulative_sum = dimension*4 - subtractor*6

    return cumulative_sum

def number_spiral_diagonals(n):
    cumulative_sum = 1
    for i in range(3,n+1,2):
        cumulative_sum += find_spiral_sum(i)

    return cumulative_sum

if __name__ == '__main__':
    print number_spiral_diagonals(1001)
    
