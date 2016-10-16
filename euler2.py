#2-13
#17
#21
#25
#67

def is_even(n):
    if n%2 ==0:
        return True
    else:
        return False

def fibonacci():
    even_sequence = [2]
    sequence = [1, 2]
    i = 0
    while sequence[i+1] < 4000000:
        fib1 = sequence[i]
        fib2 = sequence[i+1]
        sequence.append(fib1+fib2)
        if is_even(fib1+fib2):
            even_sequence.append(fib1+fib2)
        i += 1
    return sum(even_sequence)

print fibonacci()
