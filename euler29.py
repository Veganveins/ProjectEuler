def distinct_powers(a,b):
    powers = []
    for i in range (2,a+1):
        for j in range(2,b+1):
            if i**j not in powers:
                powers.append(i**j)
    return len(powers)
    

if __name__ == '__main__':
    print distinct_powers(100,100) 