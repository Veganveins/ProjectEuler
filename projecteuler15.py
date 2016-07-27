
    #i think we want 40 choose 20
    #holy shit balls I was right
    # :) :) :) :) :) :) :) :) :) :) :) :)
    #for the 2x2 case, we know we need to go right twice and down twice
    #so we need 4 choose 2 ( how many ways to choose 4 from 2 types (right and down))
    #the formula for n choose k is n!/(k!(n-k)!), which in the case of 4 choose 2 is
    #4!/(2!(4-2)!)=6

    #there are n choose k ways to choose k elements from a set of n elements, 
    #disregarding their order
    #we know the set will have 40 elements (have to go down 20 and right 20)
    #we only need to know how many ways their are to go right (or down) because
    #they will be the same
def factorial(x):
    product = 1
    n = 2
    while n < x+1:
        product = product * n
        n += 1

    return product

def routes(x,y):
    n = x+y
    k = x
    routes = factorial(n)/(factorial(k)*factorial(n-k))
    return routes

print routes(20,20)





