def is_multiple(n, m):
    if n%m == 0:
        return True
    else:
        return False

def find_sum(n):
    candidates = []
    for i in range(0,n):
        if is_multiple(i,3) or is_multiple(i,5):
            candidates.append(i)
    return sum(candidates)

print find_sum(1000)