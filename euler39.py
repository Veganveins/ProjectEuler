def find_solutions(n):
    solutions = 0
    array = []
    for i in range(1,n):
        for j in range(1,n-i):
            k = n-i-j
            if i*i+j*j == k*k:
                solutions += 1
                values = [i,j,k]
                values = sorted(values, key=int, reverse=True)
                if not values in array:
                    array.append(values)
    return len(array)

max_sols = 0
for n in range(1,1000):
    if find_solutions(n) > max_sols:
        max_sols = find_solutions(n)
        perimeter = n
print max_sols, perimeter


    



