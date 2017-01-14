
#you know you will start repeating when you get a divisor/remainder pair that you have seen before
def long_division(n, d):
    remainders = []
    divisors = []

    divisor = 0
    remainder = 0
    
    if d < 10:
        multiplier = 10
    elif d < 100:
        divisors.append(0)
        multiplier = 100
    elif d <= 1500:
        divisors.append(0)
        divisors.append(0)
        multiplier = 1000

    divisor = n*multiplier/d
    #divisor = 1
    remainder = n*multiplier - d*divisor
    #remainder = 10 - 7 = 3
    remainders.append(remainder)
    divisors.append(divisor)
    
    # print ["d= ", divisor, "r= ", remainder]
    

    while n%d:
        # if remainder < 10:
        #     multiplier = 10
        # elif remainder < 100:
        #     multiplier = 100
        # elif remainder < 1000:
        #     multiplier = 1000
        multiplier = 10

        

        while n%d:
            divisor = remainder*multiplier / d
            remainder = remainder*multiplier - d*divisor
            
            # print ["d= ", divisor, "r= ", remainder]
        
    
            if divisor not in divisors and remainder not in remainders:
                remainders.append(remainder)
                divisors.append(divisor)
            elif divisor not in divisors:
                divisors.append(divisor)
            elif remainder not in remainders:
                remainders.append(remainder)

            else:
                if divisor == 0 and remainder == 0:
                    return 0
                return len(remainders), remainders

def find_longest_cycle(n):
    longest_cycle = 0
    for i in range(2, n+1):
        if long_division(1, i) > longest_cycle:
            longest_cycle = long_division(1, i)
            saved_digit = i
    return ["d= ", saved_digit, "cycle = ", longest_cycle]


if __name__ == '__main__':
    print long_division(1,6)




