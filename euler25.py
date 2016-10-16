#1000 digit fibonacci number
def fib():
    fib0 = 1
    fib1 = 1
    fib2 = 2
    count = 3
    digits = [fib2]
    
    
    while len(str(digits[0])) < 1000:
        fib0 = fib1
        fib1 = fib2
        fib2 = fib1 + fib0
        digits[0] = fib2
        count += 1
    
    
    
    
    return len(str(digits[0])), count

print fib()
    

    
    
