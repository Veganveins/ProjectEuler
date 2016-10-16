#Find the difference between the sum of the squares of the first 
#one hundred natural numbers and the square of the sum.
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

print square_sum(1,100) - sum_square(1,100) 