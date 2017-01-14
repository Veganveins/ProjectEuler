"""
The trick here is to find the upper bound. Since we will be checking
fifth powers, we need to know how many digits the numbers are going to have.

We can start by considering 9^5, which is 59049 (5 digits). So we need to
at least check all numbers with 5 digits. The biggest number with 5 digits
is 99999, which would have a sum of 5*9^5 = 295245 (6 digits). 

This tells us that we can't only check numbers with 5 digits, since
some numbers with 5 digits will have digit sums that are 6 digits long.
The biggest number with 6 digits is 999999 which has a digit sum of 354294.

So that is our upper bound.

"""


def sum_of_fourth_powers(n):
    temp_n = str(n)
    length = len(temp_n)
    digit_sum = 0
    for i in range(0, length):
        digit = int(temp_n[i])
        digit_sum += pow(digit, 5)
    if  digit_sum == n:
        return True
    else:
        return False

def find_fourth_power_numbers(n):
    fourth_powers = []
    for i in range(2,n):
        if sum_of_fourth_powers(i) == True:
            fourth_powers.append(i)
    return sum(fourth_powers)


if __name__ == '__main__':
    print find_fourth_power_numbers(354294)