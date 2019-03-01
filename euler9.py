#46.7 seconds
#Find the only pythagorean triplet for which a + b + c = 1000
import time
start_time = time.time()

def is_triplet(n):
    for i in range(1,n-2):
        for j in range(1,n-2):
            for k in range(1, n-2):
                if (i+j+k) == n and i**2 + j**2 == k**2:
                    return i, j, k, i*j*k

print(is_triplet(1000), ' found in: ', time.time() - start_time, ' seconds')