#find the prime factorization
#take each exponenet up by 1 and multiply the exponenets to get number of factors
def is_Prime(n)
    i = 2
    for i in 2..Math.sqrt(n)
        if n%i==0
            return false
        end
    end
    return true
end


def prime_factorization(n)
   ceiling = n
   prime_candidates = []
   i = 2
   while ceiling > 1
        if ceiling%i == 0 && is_Prime(i)
            prime_candidates.push(i)
            ceiling = ceiling/i
            i = 2
        else 
            i += 1
        end
    end
   
    
    unique_prime_factors = []
    x = prime_candidates.length
    i = 0
    while i<x
        if unique_prime_factors.include?(prime_candidates[i])
            i += 1
        else 
            unique_prime_factors.push(prime_candidates[i])
        end
    end

    #factors of n is the number of times each element of unique_prime_factors
    #appears in prime_candidates + 1
    x1 = unique_prime_factors.length
    j = 0
    k = 0
    num_divisors = []
    count = 0
    while j < x1
        while k < x
            if prime_candidates[k]==unique_prime_factors[j]
                count += 1
                k += 1
            else 
                k += 1
            end
        end
        k = 0
        j += 1
        count += 1
        num_divisors.push(count)
        count = 0
    end
    
    x3 = num_divisors.length
    m = 0
    total_divisors = 1
    while m < x3
        total_divisors = total_divisors*num_divisors[m]
        m += 1
    end
    
    return total_divisors
    
end

#now I can find how many divisors a number has
#next I need to find the first TRIANGLE number n such that
#is_triangle(n) is true and prime_factorization(n)>500

def is_triangle(n)
   i = 1 
   sum = 0
   while sum < n
        sum = sum + i
        i += 1
    end
    
    if sum == n
        return true
    else
        return false
    end
    
end

def euler12(n)
   i = 1
   sum = 1
   still_looking = true
   while still_looking
        if prime_factorization(sum) > n && is_triangle(sum)
            return sum
        else
            i+=1
            sum += i
        end
    end
end

puts(euler12(500))